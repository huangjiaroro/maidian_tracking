---
name: manage-tracking
name_zh: 埋点管理
description: 用于埋点的增删改查，并支持埋点数据查询；当用户提及埋点管理、埋点配置、埋点关系排查或埋点数据查询时触发
artifact_type: cli
runtime: python
python_version: 3.12.10
offline_install: true
entrypoint: manage-tracking
---

# manage-tracking

## 概览

`manage-tracking` 是埋点管理系统的命令行入口。当前项目已经按 SkillHub Python CLI 源码包约定整理，可直接通过 `pyproject.toml` 安装，并由 SkillHub CLI 的统一安装器完成离线安装、wrapper 生成和 smoke test 校验。

## 技能作用与触发

- 技能作用：支持埋点的新增、查询、修改、删除，以及埋点配置维护、关联关系排查和埋点数据查询。
- 何时触发：当用户提及埋点管理、埋点新增、埋点查询、埋点修改、埋点删除、埋点配置、埋点关系排查或埋点数据查询时触发。

它主要用于：

- 查询当前认证身份和环境配置
- 管理 `app`、`page`、`section`、`element`、`track`
- 通过 `track key` 搜索埋点
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
- `references/tracking-wiki/`
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

当前 skill 内置了一份由 `manage_tracking` 只读接口导出的埋点知识库，入口在：

- `references/tracking-wiki/index.md`
- `references/tracking-wiki/concepts/query-playbook.md`
- `references/tracking-wiki/concepts/snapshot-sync.md`

知识库适合处理这些问题：

- 用户只给了页面名、区块名、元素名、按钮名或业务场景，没有直接给 `trackKey`
- 需要先做页面 / 区块 / 元素反查，再缩小到单个应用
- 需要快速浏览某个应用下的页面级埋点和元素级埋点分布

## 知识库联动流程

当用户没有直接提供 `trackKey`，而是用自然语言描述埋点时，优先按下面顺序执行：

1. 先读 `references/tracking-wiki/index.md`，确认可用的概念页、反查索引和应用文档。
2. 再读 `references/tracking-wiki/concepts/query-playbook.md`，按知识库约定的查询顺序定位候选。
3. 优先在这些目录中搜索候选：
   - `references/tracking-wiki/entities/lookups/`
   - `references/tracking-wiki/entities/apps/`
4. 找到候选后，再调用 `manage-tracking --json` 的只读命令做实时确认。
5. 如果知识库结果和 CLI 实时返回不一致，以 CLI 结果为准，并明确说明知识库是快照数据。

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
- 如果存在多个业务线候选，必须全部列出并说明差异。
- 如果只匹配到页面级埋点，不要臆造区块级或元素级埋点。
- 如果问题涉及前序 / 后序动作关系，不要只根据知识库结构推断运行时顺序。

## 知识库同步

内置知识库不是实时数据。需要刷新时执行：

```sh
scripts/sync_tracking_wiki_refs.sh
```

默认会从 `/Users/zyhjr/Desktop/source/llm-wiki-skill/tracking-wiki` 同步最新渲染结果到 `references/tracking-wiki/`。快照时间和导出范围以 `references/tracking-wiki/concepts/snapshot-sync.md` 为准。

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
