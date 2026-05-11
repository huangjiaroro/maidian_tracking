---
name: manage-tracking
name_zh: 埋点管理
description: Load when 用户要管理或查询埋点：app/page/section/element/track 增删改查、trackKey/stat_id 搜索、页面/区块/元素/按钮反查、AInvest 前后序关系、埋点 PV/UV/明细/list SQL。不要因泛 BI 分析、原因诊断、归因、策略建议触发，除非明确需要埋点数据查询。
artifact_type: cli
runtime: python
python_version: 3.12.10
offline_install: true
entrypoint: manage-tracking
---

# manage-tracking

## 概览

`manage-tracking` 是埋点管理系统的命令行入口。当前项目已经按 SkillHub Python CLI 源码包约定整理，可直接通过 `pyproject.toml` 安装，并由 SkillHub CLI 的统一安装器完成离线安装、wrapper 生成和 smoke test 校验。

## 核心能力

- 查询当前认证身份和环境配置
- 管理 `app`、`page`、`section`、`element`、`track`
- 通过 `track key` 搜索埋点
- 根据页面、区块、元素、按钮或业务场景反查候选埋点
- 查询 AInvest 埋点前序 / 后序关系
- 查询埋点 PV、UV、明细或埋点列表数据
- 在需要自动化消费结果时输出 JSON
- 通过 `ping` 和 `config show` 做离线健康检查

## 标准源码包文件

当前 Python CLI 源码包根目录包含以下关键文件：

- `pyproject.toml`
- `requirements.lock.txt`
- `smoke-test.json`
- `cli-capabilities.csv`
- `.skillhubignore`
- `manage_tracking/`
- `references/prod/tracking-wiki/`
- `references/ainvest/tracking-wiki/`
- `scripts/sync_tracking_wiki_refs.sh`

## 先判断是否可用

默认先执行：

```sh
manage-tracking --json ping
```

如果只是确认本地配置，也可以先看：

```sh
manage-tracking --json config show
```

如果报命令不存在、证书错误、URL 错误或 API 错误，再看 `assets/SETUP_GUIDE.md` 完成初始化。

## 环境与认证

- 业务环境支持 `dev`、`test`、`prod`、`dreamface`、`ainvest`
- 根命令支持 `--env`、`--url`、`--cert-path`、`--cert-password`、`--token`
- SkillHub 安装环境通过 `$HOME/.skillhub-cli/config.json` 中的 `skillhub_env` 感知，也支持 `SKILLHUB_ENV` 覆盖
- `skillhub_env=office/prod` 时，默认访问地址由代码中的 `manage_tracking/env.py` 决定：
  - `office -> DEFAULT_SKILLHUB_BASE_URLS["office"]`
  - `prod -> DEFAULT_SKILLHUB_BASE_URLS["prod"]`
- 如需覆盖代码默认值，可配置 skill 私有文件中的 `office_base_url` / `prod_base_url`
- 如果存在 `$HOME/.skillhub-cli/config.json`，wrapper 会自动读取：
  - `ssl_cert_file`
  - `ssl_cert_password`
  - `user_email`
- skill 私有配置位于 `$HOME/.skillhub-cli/skills-conf/manage-tracking/`

常用命令：

```sh
manage-tracking --env prod app list
manage-tracking --json track list --app-id 12
manage-tracking track search home_click
manage-tracking config show
```

## 埋点数据查询

埋点数据查询采用“agent 生成 SQL，CLI 只执行 SQL”的模式。CLI 不负责拼 SQL，不做表检索，也不做字段元数据检索。

当用户要求查询埋点 PV、UV、明细、埋点列表，或需要执行 `data explain`、`data preview`、`data download` 时，先读 `references/data-query.md`，再生成和执行 SQL。

Gotchas:

- 只查埋点数据，不做原因诊断、归因、异常检测、留存、漏斗、人群洞察或业务策略建议。
- 分析型问题先改写成可查询的 UV、PV、明细或埋点列表 SQL，并只返回原始查询结果。
- 必须生成 `p_date` 分区条件；小时级查询再补 `p_hour` 条件。
- 先执行 `data explain`，再执行 `data preview`；用户需要全量数据时再执行 `data download`。

## 对象层级

```text
App
  └── Page
        └── Section
              └── Element
                    └── Track
```

其中：

- `section` 对应后端 `functionInfo`
- `element` 对应后端 `controlInfo`

## 内置埋点知识库

当前 skill 内置了按环境区分的埋点知识库：

- prod：`references/prod/tracking-wiki/index.md`
- ainvest：`references/ainvest/tracking-wiki/index.md`

每个环境知识库都包含：

- `concepts/query-playbook.md` — 查询策略
- `concepts/snapshot-sync.md` — 快照来源和同步说明
- `entities/lookups/` — 页面 / 区块 / 元素反查索引
- `entities/apps/` — 按应用聚合的页面和埋点清单

ainvest 额外包含：

- `concepts/relation-model.md` — `track_info_realtion.csv` 的前后序关系语义
- `entities/relations/high-degree-tracks.md` — 高连接埋点
- `entities/relations/relation-components.md` — 关系连通分量

知识库适合处理这些问题：

- 用户只给了页面名、区块名、元素名、按钮名或业务场景，没有直接给 `trackKey`
- 需要先做页面 / 区块 / 元素反查，再按应用枚举候选
- 需要快速浏览某个应用下的页面级埋点和元素级埋点分布
- 在 ainvest 中，需要查询某个埋点的前序 / 后序关系

## 知识库联动流程

当用户没有直接提供 `trackKey`，而是用自然语言描述埋点时，优先按下面顺序执行：

1. 先判断用户要查的环境：明确提到 `ainvest`、`AInvest`、北美、海外或相关业务线时读 `references/ainvest/tracking-wiki/index.md`，否则默认读 `references/prod/tracking-wiki/index.md`。
2. 再读对应环境的 `concepts/query-playbook.md`，按知识库约定的查询顺序定位候选。
3. 必须先做跨应用反查，不要因为用户提到 `aime` 就只读 `app-23-aime.md`：
   - 先搜 `entities/lookups/page-lookup.md`，找出同名或近似页面在所有应用中的分布。
   - 再搜 `entities/lookups/section-lookup.md` 和 `entities/lookups/element-lookup.md`，找出同名区块和元素的全局候选。
   - 然后按候选里的 `appSign` / 应用名进入对应 `entities/apps/app-*.md`，读取实际埋点清单。
   - 如果 ainvest 问题涉及前后序关系，再搜 `entities/relations/`，补充高连接埋点和关系覆盖情况。
4. 同一个页面、区块或元素可能同时存在于多个应用，例如 `aime无处不在` 可出现在 `aime`、`lhsa`、`lhssc`、`lhsps`、`lhspt`、`lhsws` 等应用中；必须保留这些候选，不能只返回某一个应用的结果。
5. 找到候选后，如果当前 CLI 支持该运行环境，再调用 `manage-tracking --json` 的只读命令做实时确认。
6. 如果知识库结果和 CLI 实时返回不一致，以 CLI 结果为准，并明确说明知识库是快照数据。

推荐的只读确认命令：

```sh
manage-tracking --json app list
manage-tracking --json page list
manage-tracking --json section list
manage-tracking --json element list
manage-tracking --json track list
manage-tracking track search <keyword>
```

回答约束：

- 返回候选埋点时，尽量同时给出 `trackKey`、所属应用、页面 / 区块 / 元素归属。
- 如果存在多个应用或业务线候选，必须全部列出并说明差异；除非用户明确指定应用，否则不要自动丢弃候选。
- 如果只匹配到页面级埋点，不要臆造区块级或元素级埋点。
- 如果问题涉及前序 / 后序动作关系，prod 不能仅根据结构推断；ainvest 可引用 `track_info_realtion.csv` 生成的实际关系，但要说明其快照口径限制。

## 知识库同步

内置知识库不是实时数据。快照时间和导出范围以对应环境的 `concepts/snapshot-sync.md` 为准。

prod wiki 当前位于：

```text
references/prod/tracking-wiki/
```

ainvest wiki 当前位于：

```text
references/ainvest/tracking-wiki/
```

刷新 prod 快照时可继续使用：

```sh
scripts/sync_tracking_wiki_refs.sh <source-wiki-root> references/prod/tracking-wiki
```

ainvest 当前由下载目录 CSV 生成；重新导出 CSV 后，需要重新生成 `references/ainvest/tracking-wiki/`。

## 重要行为

- `--json` 必须放在根命令前
- 默认先用 `ping`、`list`、`get`、`search` 做只读确认
- `create`、`delete` 有副作用，只在用户明确要求时执行
- Python CLI 的主安装链路不再依赖 `skill-install.sh`
- 如需确认实现细节，优先查看：
  - `manage_tracking/cli.py`
  - `manage_tracking/skillhub_entry.py`
  - `manage_tracking/core/config.py`
  - `manage_tracking/core/client.py`
  - `manage_tracking/core/api.py`
