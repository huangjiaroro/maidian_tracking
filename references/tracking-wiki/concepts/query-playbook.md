---
title: 埋点查询策略
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - query
  - playbook
  - ainvest
---

# 埋点查询策略

埋点信息查询默认以 wiki 知识库优先；只有 wiki 查不到、用户明确要求实时复核，或执行简单 CRUD / list 命令时，才调用 `manage-tracking` 管理 CLI 兜底。

当用户用自然语言提问时，按下面顺序定位埋点：

1. 先读唯一知识库入口 `references/tracking-wiki/index.md`。
2. 不要因为用户提到某个产品词就直接锁定单个应用页。例如用户说 `aime无处不在` 时，不能只读 `app-23-aime.md`。
3. 先在 `entities/lookups/page-lookup.md` 反查页面名或 `page_short`，列出所有同名或近似页面对应的应用。
4. 再在 `entities/lookups/section-lookup.md`、`entities/lookups/element-lookup.md` 反查区块和元素，补充全局候选。
5. 对每个候选应用，再进入 `entities/apps/` 下对应应用页读取实际埋点清单，并检查 `business_line`、`allow_action`、参数字段。
6. 如果 lookup 只给出对象 ID、英文名、中文名和关联数量，直接在 `entities/apps/app-*.md` 中搜索该英文名或中文名，读取匹配的埋点清单行和字段明细；不要为了反推归属分页扫描实时 CLI。
7. 如果用户给了应用名、`appSign` 或业务系统，可以优先展示该应用候选，但仍需说明是否存在其他应用同名页面 / 区块 / 元素。
8. 如果问题涉及前序 / 后序动作，继续查 `entities/relations/high-degree-tracks.md`，再用 `track_info_realtion.csv` 语义：`from_stat_id` 是前序，`stat_id` 是当前埋点。

## 跨应用页面规则

同一个页面、区块或元素可能同时存在于多个应用。查询时必须先保留跨应用候选，再按用户语境收敛。

典型例子：`aime无处不在` 同时分布在多个应用中，包括 `aime`、`lhsa`、`lhssc`、`lhsps`、`lhspt`、`lhsws` 等。若用户没有明确指定应用，必须列出这些候选及其差异，不要自动只选 `aime` 应用。

## 回答约束

- 返回候选埋点时，同时给出 `track_key`、应用、页面、区块、元素。
- 如果同一页面、区块或元素在多个应用中都有候选，必须列出差异。
- 如果只匹配到页面级埋点，不要臆造区块级或元素级埋点。
- 关系查询只能说明导出关系中存在的前后序，不要推断未覆盖的链路。
- wiki 精确命中时直接回答，不要分页扫描 CLI。
- wiki 查不到时优先用 `track search <keyword>` 或 `track get-by-key --key <trackKey>` 兜底；`list` 命令都是分页列表，只在用户明确要求列表或已有过滤条件时使用。
- 如果用户明确要求实时复核且 CLI 与 wiki 不一致，同时说明实时结果和 wiki 快照差异，不要静默覆盖 wiki 结论。
