---
title: 埋点命名规则
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - naming
  - track-key
  - ainvest
---

# 埋点命名规则

当前平台以 `track_key` 作为埋点主标识。ainvest 快照中的主流形态是五段式：

```text
应用_业务线_页面_区块_元素
```

当 `function_id` / `control_id` 为空时，一般表示页面级埋点；当它们存在时，通常表示区块或元素级埋点。

## 分段统计

| track_key 段数 | 埋点数 |
| --- | --- |
| 2 | 4 |
| 3 | 927 |
| 4 | 23 |
| 5 | 12546 |

## 示例

| 段数 | track_key | track_name |
| --- | --- | --- |
| 5 | lhspc_pc_chart_chart_intervalsSet | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_周期设置（intervalsSet） |
| 3 | lhspc_pc_orderbook | PC客户端（LightHouse PC）_Ainvest PC_订单表（orderbook） |
| 4 | lhsa_f10_MergerAcquire_Cartoon | 手机客户端（AInvestApp）_F10_资产重组_动画 |
| 2 | lhsa_mob | 手机客户端（AInvestApp）_Ainvest APP |

## 动作类型分布

`allow_action` 保留为原始编码，避免在没有权威枚举表时误译。

| allow_action | 出现次数 |
| --- | --- |
| 0 | 11162 |
| 2 | 3136 |
| 1 | 583 |
| 4 | 453 |
| 3 | 131 |
| 5 | 66 |
| 6 | 66 |
| 9 | 59 |
| 8 | 19 |
| end | 11 |
| 7 | 10 |

## 高频参数字段

| fieldCode | 出现次数 |
| --- | --- |
| stock | 1871 |
| content | 1612 |
| tab | 971 |
| type | 702 |
| name | 641 |
| targetName | 486 |
| logmap | 409 |
| state | 403 |
| mkt | 287 |
| from | 274 |
| news | 264 |
| chanId | 242 |
| stayLen | 233 |
| goodsId | 190 |
| num | 179 |
| source | 173 |
| title | 169 |
| sessionId | 161 |
| mode | 143 |
| itemId | 114 |
| listRow | 107 |
| position | 106 |
| regisId | 105 |
| visitId | 93 |
| impsId | 84 |
| targetId | 76 |
| url | 69 |
| logId | 68 |
| symbol | 66 |
| newsId | 62 |
