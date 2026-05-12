---
name: manage-tracking
name_zh: 埋点管理
description: 埋点管理与查询技能，用于查询埋点数据信息；当需要进行埋点信息查询、埋点 PV/UV/明细时使用；泛 BI 分析、原因诊断、归因、策略建议不触发。
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
- `references/tracking-wiki/`
- `scripts/sync_tracking_wiki_refs.sh`

## 先判断是否可用

默认先执行：

```sh
manage-tracking --json ping
```

`ping` 只验证 CLI 入口和本地配置加载，不会访问后端；不能据此判断网络或 API 是否可达。需要确认真实接口时，用只读的 `list`、`search` 或 `auth whoami`。

如果只是确认本地配置，也可以先看：

```sh
manage-tracking --json config show
```

如果报命令不存在、证书错误、URL 错误或 API 错误，再看 `assets/SETUP_GUIDE.md` 完成初始化。

## 环境与认证

- 运行环境只读取 SkillHub 共享配置中的 `skillhub_env`
- `skillhub_env` 支持 `office`、`prod`
- 未配置或配置非法时默认使用 `prod`
- 访问地址按 `skillhub_env` 自动选择，不再支持技能私有环境配置或 session 持久化
- CLI 优先读取 `$HOME/.skillhub-cli/config.json`；如果不存在，再读取 `/root/.skillhub-cli/config.json`
- 共享配置中会读取：
  - `skillhub_env`
  - `ssl_cert_file`
  - `ssl_cert_password`
  - `user_email`
- `registry`、`openclaw_skill_dir`、`ssl_legacy_mode` 等字段属于 SkillHub CLI 安装 / 平台配置，不参与 manage-tracking 运行时鉴权
- 当前 `ping` / `config show` 输出不包含 `environment`、`has_token`；如果出现这些字段，说明执行到旧版 CLI 或旧 wrapper

常用命令：

```sh
manage-tracking app list
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

当前 skill 只内置一份来自 AInvest 的埋点知识库，固定入口在：

- `references/tracking-wiki/index.md`

不要按环境名或业务线名拼接知识库目录；当前技能包只使用上面的固定入口。

知识库包含：

- `concepts/query-playbook.md` — 查询策略
- `concepts/snapshot-sync.md` — 快照来源和同步说明
- `concepts/relation-model.md` — `track_info_realtion.csv` 的前后序关系语义
- `entities/lookups/` — 页面 / 区块 / 元素反查索引
- `entities/apps/` — 按应用聚合的页面、埋点清单和字段明细
- `entities/relations/` — 高连接埋点和关系连通分量

知识库适合处理这些问题：

- 用户只给了页面名、区块名、元素名、按钮名或业务场景，没有直接给 `trackKey`
- 需要先做页面 / 区块 / 元素反查，再按应用枚举候选
- 需要快速浏览某个应用下的页面级埋点和元素级埋点分布
- 需要查看某个埋点的额外字段中文名、英文名和备注
- 需要查询某个埋点的前序 / 后序关系

## 知识库联动流程

埋点信息查询默认以 wiki 知识库优先；只有 wiki 查不到、用户明确要求实时复核，或执行简单 CRUD / list 命令时，才调用 `manage-tracking` 管理 CLI。埋点 PV/UV/明细查询属于数据查询，按 `references/data-query.md` 生成 SQL 并用 `data` 命令执行。

当用户没有直接提供 `trackKey`，而是用自然语言描述埋点时，按下面顺序执行：

1. 先读 `references/tracking-wiki/index.md`，确认可用的概念页、反查索引、应用文档和关系文档。
2. 再读 `references/tracking-wiki/concepts/query-playbook.md`，按知识库约定的查询顺序定位候选。
3. 必须先做跨应用反查，不要因为用户提到 `aime` 就只读 `app-23-aime.md`：
   - 先搜 `entities/lookups/page-lookup.md`，找出同名或近似页面在所有应用中的分布。
   - 再搜 `entities/lookups/section-lookup.md` 和 `entities/lookups/element-lookup.md`，找出同名区块和元素的全局候选。
   - 然后按候选里的 `appSign` / 应用名进入对应 `entities/apps/app-*.md`，读取实际埋点清单和字段明细。
   - 如果 lookup 只给出对象 ID、英文名、中文名和关联数量，直接在 `entities/apps/app-*.md` 中搜索该英文名或中文名；不要为了反推归属去分页扫描 CLI 的 `element list` / `section list`。
   - 如果问题涉及前后序关系，再搜 `entities/relations/`，补充高连接埋点和关系覆盖情况。
4. 同一个页面、区块或元素可能同时存在于多个应用，例如 `aime无处不在` 可出现在 `aime`、`lhsa`、`lhssc`、`lhsps`、`lhspt`、`lhsws` 等应用中；必须保留这些候选，不能只返回某一个应用的结果。
5. 如果 wiki 已经精确命中，直接基于 wiki 回答，不要再用分页 CLI 扫描找归属。
6. 如果 wiki 查不到，再在 CLI 命令可用且网络 / API 可达时，用 `manage-tracking --json` 的只读命令兜底查询。
7. 如果用户明确要求实时复核，才补充 CLI 结果；若 CLI 与 wiki 不一致，同时说明实时结果和 wiki 快照差异，不要静默覆盖 wiki 结论。

wiki 查不到时的只读兜底命令优先用精准查询：

```sh
manage-tracking track search <keyword>
manage-tracking --json track get-by-key --key <trackKey>
```

`app/page/section/element/track list` 都是分页列表，不作为确认某个自然语言候选的推荐命令；只有用户明确要求列列表，或已知 `--app-id`、`--page-id`、`--function-id` 等过滤条件时才使用。

回答约束：

- 返回候选埋点时，尽量同时给出 `trackKey`、所属应用、页面 / 区块 / 元素归属。
- 如果存在多个应用或业务线候选，必须全部列出并说明差异；除非用户明确指定应用，否则不要自动丢弃候选。
- 如果只匹配到页面级埋点，不要臆造区块级或元素级埋点。
- 如果问题涉及前序 / 后序动作关系，可引用 `track_info_realtion.csv` 生成的实际关系，但要说明其快照口径限制。
- wiki 精确命中时直接回答，不要为了确认而分页扫描 CLI。

## 知识库同步

内置知识库不是实时数据。当前只保留一份 ainvest 快照，位置为：

```text
references/tracking-wiki/
```

不要按 `prod` / `ainvest` 目录拆分知识库路径。

快照时间、导出范围和源文件以 `references/tracking-wiki/concepts/snapshot-sync.md` 为准。

重新导出 CSV 后，用相同文件名放到 `/Users/zyhjr/Downloads`，再重新生成 `references/tracking-wiki/`。

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
