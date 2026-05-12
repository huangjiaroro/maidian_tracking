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

当用户用自然语言提问时，优先按下面顺序定位埋点：

1. 先读唯一知识库入口 `references/tracking-wiki/index.md`。
2. 不要因为用户提到某个产品词就直接锁定单个应用页。例如用户说 `aime无处不在` 时，不能只读 `app-23-aime.md`。
3. 先在 `entities/lookups/page-lookup.md` 反查页面名或 `page_short`，列出所有同名或近似页面对应的应用。
4. 再在 `entities/lookups/section-lookup.md`、`entities/lookups/element-lookup.md` 反查区块和元素，补充全局候选。
5. 对每个候选应用，再进入 `entities/apps/` 下对应应用页读取实际埋点清单，并检查 `business_line`、`allow_action`、参数字段。
6. 如果用户给了应用名、`appSign` 或业务系统，可以优先展示该应用候选，但仍需说明是否存在其他应用同名页面 / 区块 / 元素。
7. 如果问题涉及前序 / 后序动作，继续查 `entities/relations/high-degree-tracks.md`，再用 `track_info_realtion.csv` 语义：`from_stat_id` 是前序，`stat_id` 是当前埋点。

## 跨应用页面规则

同一个页面、区块或元素可能同时存在于多个应用。查询时必须先保留跨应用候选，再按用户语境收敛。

典型例子：`aime无处不在` 同时分布在多个应用中，包括 `aime`、`lhsa`、`lhssc`、`lhsps`、`lhspt`、`lhsws` 等。若用户没有明确指定应用，必须列出这些候选及其差异，不要自动只选 `aime` 应用。

## 回答约束

- 返回候选埋点时，同时给出 `track_key`、应用、页面、区块、元素。
- 如果同一页面、区块或元素在多个应用中都有候选，必须列出差异。
- 如果只匹配到页面级埋点，不要臆造区块级或元素级埋点。
- 关系查询只能说明导出关系中存在的前后序，不要推断未覆盖的链路。
- 如果知识库结果和实时 CLI 查询不一致，以 CLI 返回为准，并说明 wiki 是快照数据。
