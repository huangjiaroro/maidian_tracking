# SkillHub CLI 类型技能开发文档

## 1. 适用范围

本文档面向当前 `cbasclaw-portal` 仓库中的 SkillHub CLI 技能开发流程，重点说明：

1. Python CLI 技能现在需要满足什么结构和约束。
2. `skillhub publish`、`skillhub install`、`skillhub update` 分别会做什么。
3. `prod` 和 `office` 两个环境下，统一安装流程是怎么落地的。
4. 技能开发时如何正确处理 `~/.skillhub-cli/config.json` 中的 `skillhub_env`。

本文主要针对：

- `artifact_type: cli`
- `runtime: python`

非 Python CLI 技能当前仍走 legacy `skill-install.sh` 路径，本文不展开。

## 2. 先说结论

当前 Python CLI 技能的核心原则可以直接记成下面几条：

1. 发布到 SkillHub 的是源码包，不是 runtime 包。
2. Python CLI 的主安装逻辑在 SkillHub CLI 内置安装器里，不要求技能开发者自己写一套安装主流程。
3. `prod` 和 `office` 共用同一套安装骨架：
   下载源码包 -> 解压到 stage -> 写入正式目录 -> 创建 venv -> 安装技能 -> 生成 wrapper -> `--help` 验证 -> `smoke-test.json` 验证。
4. 两个环境的主要差异不在技能包结构，而在 Python 选择策略和依赖安装策略。
5. 技能内部如果需要区分业务环境，应读取 `~/.skillhub-cli/config.json` 中的 `skillhub_env`，必要时支持 `SKILLHUB_ENV` 覆盖。
6. Python CLI 技能当前不应再把环境兼容逻辑塞进 `skill-install.sh`；这部分逻辑应该由 SkillHub CLI 统一处理。

## 3. 推荐目录结构

一个最小可工作的 Python CLI 技能目录，建议至少包含下面这些文件：

```text
your-skill/
├── SKILL.md
├── pyproject.toml
├── requirements.lock.txt
├── smoke-test.json
├── cli-capabilities.csv
├── .skillhubignore
└── your_package/
    ├── __init__.py
    └── cli.py
```

说明：

1. `SKILL.md` 是技能说明和 frontmatter 的入口文件。
2. `pyproject.toml` 定义 Python 包元数据、`requires-python` 和 console script。
3. `requirements.lock.txt` 用来描述运行期依赖。
4. `smoke-test.json` 用来做安装后的自动验证。
5. `cli-capabilities.csv` 用来给前端和平台展示 CLI 的能力说明。
6. `.skillhubignore` 用来排除本地调试文件、缓存文件和不需要发布的内容。

## 4. SKILL.md 要求

### 4.1 必填 frontmatter

当前 Python CLI 技能至少应包含下面这些 frontmatter 字段：

```yaml
---
name: data-asset-query
name_zh: 数据资产查询
description: 查询数据资产并输出结构化结果的 Python CLI 技能
artifact_type: cli
runtime: python
python_version: 3.12.10
offline_install: true
entrypoint: data-asset-query
---
```

字段说明：

1. `name`：英文展示名。
2. `name_zh`：中文展示名。
3. `description`：技能摘要。
4. `artifact_type: cli`：声明这是 CLI 技能。
5. `runtime: python`：声明这是 Python CLI。
6. `python_version`：声明目标 Python 版本。
7. `offline_install: true`：声明该技能遵循统一离线安装契约。
8. `entrypoint`：CLI 入口名，当前要求与 slug 完全一致。

### 4.2 额外说明

1. `entrypoint` 必须和发布时的 slug 一致。
2. 对 Python CLI 来说，当前不要求再提供 `skill-install.sh` 作为主安装入口。

## 5. pyproject.toml 要求

当前安装器的关键点不是“读你的依赖树自动安装”，而是：

1. office 环境会先执行 `pip install -r requirements.lock.txt`。
2. 然后再执行 `pip install --no-deps .` 安装技能自身包。
3. prod 环境不会执行 `pip install -r requirements.lock.txt`，而是依赖平台预装依赖。

所以 `pyproject.toml` 建议至少满足下面几件事：

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "data-asset-query"
version = "1.0.0"
description = "CLI skill for querying data assets"
readme = "SKILL.md"
requires-python = ">=3.12,<3.13"
dependencies = [
  "click==8.1.8",
]

[project.scripts]
data-asset-query = "your_package.cli:main"
```

开发时要注意：

1. `requires-python` 很重要，office 环境在找不到精确平台 Python 时，会用它来选择兼容的本机 Python。
2. `[project.scripts]` 中的命令名必须和 `entrypoint` 一致。
3. `dependencies` 和 `requirements.lock.txt` 应保持一致。
4. 当前 prod 安装策略要求基础环境中已经具备你运行所需的依赖；也就是说，开发者不需要在 `skill-install.sh` 做兼容，但所依赖的库仍然需要由平台统一预装或提前提供。

## 6. 其他必需文件

### 6.1 `cli-capabilities.csv`

格式要求非常简单，但很严格：

1. 文件名必须是 `cli-capabilities.csv`。
2. 表头必须严格等于 `category,capabilities`。
3. 至少有一行数据。
4. 每一行必须正好两列。

示例：

```csv
category,capabilities
资产查询,"按资产 ID 查询元信息并返回 JSON"
健康检查,"快速验证 CLI 可执行性与当前环境"
```

### 6.2 `requirements.lock.txt`

要求：

1. 文件必须存在。
2. office 环境会直接拿它执行 `pip install -r requirements.lock.txt`。
3. prod 环境不会执行这一步，所以不要把“只能靠线上临时 pip install 才能跑起来”当作前提。

### 6.3 `smoke-test.json`

格式要求：

1. 必须是 JSON 对象。
2. `version` 必须等于 `1`。
3. `commands` 必须是非空数组。
4. 每个 command 至少需要 `args: string[]`。

示例：

```json
{
  "version": 1,
  "commands": [
    {
      "args": ["ping"],
      "expect_exit_code": 0,
      "expect_stdout_contains": ["\"status\": \"ok\""]
    },
    {
      "args": ["query", "--asset-id", "demo-asset"],
      "expect_exit_code": 0,
      "expect_stdout_contains": ["\"asset_id\": \"demo-asset\""]
    }
  ]
}
```

安装完成后，SkillHub CLI 会按这个文件自动执行 smoke test。

### 6.4 `.skillhubignore`

建议显式忽略本地开发产生的无关文件，比如：

```gitignore
dist/
build/
__pycache__/
.venv/
*.egg-info/
wheelhouse/
```

补充说明：

1. Python CLI 发布时会自动排除本地 `wheelhouse/` 文件。
2. 当前服务端也不希望收到 `wheelhouse/` 里的 wheel 文件。

## 7. skill 内部如何处理 `skillhub_env`

### 7.1 为什么要处理

当前 SkillHub 有两个运行环境：

1. `prod`
2. `office`

对于很多技能来说，这两个环境对应的业务入口、认证方式、数据源或者调试开关并不完全一样。所以技能内部应该自己感知当前环境，并做业务分支。

### 7.2 读取位置

SkillHub CLI 的本地配置文件路径是：

```text
$HOME/.skillhub-cli/config.json
```

其中与环境相关的字段是：

```json
{
  "skillhub_env": "office"
}
```

当前代码里，CLI 也支持用环境变量 `SKILLHUB_ENV` 覆盖这个值。

### 7.3 推荐做法

推荐你的技能代码按下面这个优先级取环境：

1. 先读 `SKILLHUB_ENV`
2. 再读 `~/.skillhub-cli/config.json` 里的 `skillhub_env`
3. 都没有时，默认按 `office`

Python 示例：

```python
from __future__ import annotations

import json
import os
from pathlib import Path


def read_skillhub_env() -> str:
    env = os.getenv("SKILLHUB_ENV", "").strip().lower()
    if env in {"prod", "office"}:
        return env

    config_path = Path.home() / ".skillhub-cli" / "config.json"
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception:
        data = {}

    raw = str(data.get("skillhub_env", "")).strip().lower()
    if raw in {"prod", "office"}:
        return raw

    return "office"
```

然后在业务逻辑里做分支：

```python
def resolve_api_base() -> str:
    skillhub_env = read_skillhub_env()
    if skillhub_env == "prod":
        return "https://prod.example.internal"
    return "https://office.example.internal"
```

### 7.4 不推荐做法

不推荐把环境兼容逻辑写进 `skill-install.sh`，因为：

1. Python CLI 的主安装链路已经不依赖 `skill-install.sh`。
2. `prod` / `office` 的安装差异应该由 SkillHub CLI 统一处理。
3. 技能自身只需要在运行时处理业务环境差异。

## 8. 本地开发和发布前验证

推荐开发顺序：

1. 先写好 `SKILL.md`、`pyproject.toml`、`requirements.lock.txt`、`smoke-test.json`。
2. 先运行源包验证。
3. 再运行完整安装验证。
4. 最后再发布。

常用命令：

```bash
skillhub verify-source /path/to/your-skill
skillhub verify /path/to/your-skill
skillhub publish /path/to/your-skill --name data-asset-query --name-zh 数据资产查询
```

补充说明：

1. `verify-source` 主要校验源包结构和 smoke-test 协议。
2. `verify` 会真正走一次统一安装器。
3. `publish` 对 Python CLI 目前主要做 source package 预检，不会先在本地执行完整安装。

## 9. `skillhub publish` 当前流程

当前 Python CLI 的发布流程大致如下。

### 9.1 CLI 侧

`skillhub publish <path>` 会做这些事：

1. 读取 `SKILL.md` frontmatter。
2. 校验 `name`、`name_zh`、`description`、`artifact_type` 等基本发布字段。
3. 收集待发布文件。
4. 对 Python CLI 自动过滤 `wheelhouse/`。
5. 校验 `cli-capabilities.csv`。
6. 对 Python CLI 执行 `verifyLocalPythonCliSourceSkill`：
   - 校验 Python CLI 基础声明
   - 校验源包必需文件
   - 校验 `smoke-test.json` 协议
   - 如果传了 `--python`，额外探测本地 Python 兼容性
7. 把 payload 和所有文件作为 multipart form 上传到后端。

### 9.2 后端侧

后端收到发布请求后会：

1. 解析 `SKILL.md` frontmatter。
2. 如果识别到这是 Python CLI，则执行源包契约校验。
3. 校验通过后，写入版本记录、source zip 信息和 runtime verification 元数据。

后端当前会检查的关键点包括：

1. `runtime: python`
2. `python_version`
3. `offline_install: true`
4. `entrypoint`
5. `cli-capabilities.csv`
6. `pyproject.toml`
7. `requirements.lock.txt`
8. `smoke-test.json`

## 10. `skillhub install` / `skillhub update` 当前流程

当前 Python CLI 的安装与更新主流程如下：

1. 从 registry 下载 source zip。
2. 解压到临时 stage 目录。
3. 读取 `SKILL.md` 并识别技能类型。
4. 对 Python CLI 做安装契约检查。
5. 将 stage 提升为正式技能目录，并保留回滚点。
6. 调用内置 Python CLI 安装器：
   - 解析 `skillhub_env`
   - 选择 Python
   - 创建 `.skillhub/runtime/venv`
   - 安装技能
   - 生成 `.skillhub/bin/<slug>` wrapper
   - 写入 `.skillhub/install-meta.json`
7. 执行 `--help` 验证 CLI 可执行入口。
8. 执行 `smoke-test.json` 验证。
9. 写入本地安装元数据：
   - `.skillhub/origin.json`
   - `.skillhub/VERSION`
   - workdir 下的 `.skillhub/lock.json`
10. 在本地 managed bin 目录中建立命令入口。

安装后，技能目录下通常会出现：

```text
.skillhub/
├── VERSION
├── install-meta.json
├── origin.json
├── runtime/
│   └── venv/
└── bin/
    └── <slug>
```

## 11. office 与 prod 的差异

### 11.1 相同点

两个环境的安装主流程骨架是一样的：

1. 都是 source package。
2. 都由 SkillHub CLI 内置安装器负责。
3. 都会创建技能自己的 venv。
4. 都会生成 wrapper。
5. 都会跑 `--help` 和 `smoke-test.json`。

### 11.2 prod 环境

当前 prod 策略的特点：

1. 目标 Python 是统一的平台 Python。
2. 安装器会创建带 `--system-site-packages` 的 venv。
3. 不会执行 `pip install -r requirements.lock.txt`。
4. 会执行 `pip install --no-index --no-build-isolation --no-deps .`。
5. 安装前会检查 `setuptools` 和 `wheel` 是否已存在于运行时中。

换句话说，prod 里你不能指望安装时再去拉新的三方依赖；运行依赖需要由平台基础环境提前提供。

### 11.3 office 环境

当前 office 策略的特点：

1. 本机 Python 版本可能不统一。
2. 安装器会优先找平台期望的 Python。
3. 如果找不到精确版本，会尝试根据 `pyproject.toml` 里的 `requires-python` 选择兼容解释器。
4. 会执行 `pip install -r requirements.lock.txt`。
5. 然后执行 `pip install --no-deps .`。

## 12. office 环境寻找 Python 的逻辑

当前 office 环境的 Python 选择顺序大致如下：

1. `skillhub install ... --python <path>`
2. 环境变量 `SKILLHUB_PYTHON_31210`
3. `~/.skillhub-cli/config.json` 中的 `python_31210_path`
4. 兼容保留字段 `SKILLHUB_PYTHON_3135`
5. 兼容保留字段 `python_3135_path`
6. 环境变量 `SKILLHUB_PYTHON`
7. `config.json` 中的 `python_path`
8. 命令名探测：
   - `python3.12`
   - `python3.13`
   - `python3.11`
   - `python3.10`
   - `python3.9`
   - `python3`

选择规则：

1. 如果能找到精确的平台 Python，优先使用它。
2. 如果找不到精确版本，则要求 `pyproject.toml` 中声明了 `requires-python`。
3. 此时安装器会选择一个满足 `requires-python` 的本机 Python。
4. 如果既没有精确版本，也没有能满足 `requires-python` 的解释器，安装会失败。

这也是为什么推荐你一定要写清楚 `requires-python`。

## 13. 建议的 `config.json`

本地开发时，建议至少把下面这些配置项说明清楚：

```json
{
  "registry": "https://your-registry.example/api/skill",
  "user_email": "your.name@example.com",
  "skillhub_env": "office",
  "openclaw_skill_dir": ".openclaw/skills",
  "python_31210_path": "/path/to/python3.12.10",
  "python_path": "/path/to/default-python"
}
```

说明：

1. `skillhub_env` 决定 SkillHub CLI 当前按 `prod` 还是 `office` 逻辑安装 Python CLI。
2. `python_31210_path` 用来显式指定平台要求的 Python。
3. `python_path` 是 office 的通用 fallback。

## 14. 当前已知差异与注意事项

这部分很重要，因为当前仓库里还存在一些常量没有完全统一。

### 14.1 Python 版本常量存在不一致

当前主链路已经统一到 `3.12.10`：

1. SkillHub CLI 的 Python 安装链路按 `3.12.10` 工作。
2. 后端 `runtime_verification_service`、Python CLI 源包校验和 publish 返回的运行时元数据也应按 `3.12.10` 工作。

仍需注意：

1. 历史设计文档或未清理的旧分支代码里，可能还会看到 `3.13.5` 这样的旧描述。
2. 如果你发现线上环境行为和这里不一致，应以部署环境里的实际代码为准，再做一次确认。

### 14.2 Python CLI 不应再依赖 `skill-install.sh`

对 Python CLI 来说：

1. 当前主安装链路不再依赖 `skill-install.sh`。
2. 不需要为了兼容 `prod` / `office` 在 `skill-install.sh` 里写分支逻辑。
3. 环境分支应写在技能自身业务代码中。

### 14.3 prod 依赖供给仍然是平台责任

统一安装流程并不代表“任意依赖都能在 prod 现场自动安装”。

当前真实情况是：

1. office 可以在 venv 中执行 `pip install -r requirements.lock.txt`。
2. prod 不会执行这一步。
3. 所以如果你的技能依赖某些第三方库，这些库需要由平台基础 Python 环境统一提供。

## 15. 推荐开发流程

最后给一个最实用的开发顺序：

1. 先写包代码和 CLI 入口。
2. 写 `SKILL.md`、`pyproject.toml`、`requirements.lock.txt`、`cli-capabilities.csv`、`smoke-test.json`。
3. 在技能代码中加入 `skillhub_env` 读取逻辑。
4. 运行 `skillhub verify-source <path>`。
5. 运行 `skillhub verify <path>`。
6. 确认 `ping`、`--help`、关键业务命令都能通过 smoke test。
7. 最后运行 `skillhub publish <path> ...`。

如果你开发的是面向 `prod` 的技能，除了本地 office 验证外，还要额外确认一件事：

1. 你的依赖是否已经由平台基础 Python 运行时提供。
