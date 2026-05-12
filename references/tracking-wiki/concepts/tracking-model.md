---
title: 埋点平台对象模型
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - model
  - ainvest
---

# 埋点平台对象模型

ainvest 知识库围绕 `App -> Page -> Section -> Element -> Track` 五层对象展开。

## 对象定义

- `App`：应用级实体，来自 `app_info.csv`，包含 `app_id`、`app_sign`、`app_key`、topic 和 payload 状态。
- `Page`：页面实体，来自 `page_info.csv`，包含 `page_short`、`page_name`、截图引用和所属应用。
- `Section`：页面区块，来自 `qk1.csv`，对应后端 `functionInfo`。
- `Element`：区块内元素，来自 `ys1.csv`，对应后端 `controlInfo`。
- `Track`：埋点实体，来自 `track_info.csv`，核心标识是 `track_key`，并关联 app/page/section/element、业务线、动作类型和参数字段。
- `Relation`：真实前后序关系，来自 `track_info_realtion.csv`，按 `from_stat_id -> stat_id` 理解。

## 当前快照规模

| 对象 | 数量 |
| --- | --- |
| 应用 | 23 |
| 页面 | 1279 |
| 区块 | 1690 |
| 元素 | 2801 |
| 埋点 | 13500 |
| 关系行 | 29301 |

## 关联完整性

| 检查项 | 异常数 |
| --- | --- |
| pages.app_id 找不到 App | 1 |
| tracks.app_id 找不到 App | 0 |
| tracks.page_id 找不到 Page | 0 |
| tracks.function_id 找不到 Section | 0 |
| tracks.control_id 找不到 Element | 0 |

## 文档组织

- `entities/apps/`：按应用聚合页面、埋点和关系覆盖，是查询 `track_key` 的主入口。
- `entities/lookups/`：页面、区块、元素的反查索引。
- `entities/relations/`：真实前后序关系的枢纽节点和连通分量。
