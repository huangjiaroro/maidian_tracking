---
title: 数据质量与缺口
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - quality
  - ainvest
---

# 数据质量与缺口

## 总览

| 问题 | 数量 | 说明 |
| --- | --- | --- |
| 缺失 page_info1.csv | 1 | 下载目录没有 `page_info1.csv`，但存在与 `page_info.csv` 完全一致的 `page_info2.csv`。 |
| 重复区块文件 | 1 | `qk1.csv` 与 `qk2.csv` byte-identical。 |
| 重复元素文件 | 2 | `ys1.csv`、`ys2.csv`、`ys3.csv` byte-identical。 |
| 页面引用缺失应用 | 1 | 页面 `id=368` 引用 `app_id=26`，应用表中不存在。 |
| 重复 track_key | 2 | 同一 `track_key` 对应多个 track id。 |
| 缺失 page_id 的埋点 | 18 | 页面归属不完整。 |
| 缺失 function_id/control_id 的埋点 | 931 | 通常是页面级埋点，也可能是归属缺失。 |
| 无 action_fields 的埋点 | 6800 | 无额外参数字段。 |

## 重复 track_key

| track_key | 数量 | track ids |
| --- | --- | --- |
| lhsa_mob_socialtrade_highreturns_timeswitch | 2 | 10296, 10316 |
| lhssc_mob_socialtrade_highreturns_timeswitch | 2 | 10950, 10952 |

## 重复 function_code

| function_code | 数量 | section ids |
| --- | --- | --- |
| collectionPanel | 2 | 1668, 1669 |
| langpage | 2 | 1715, 1716 |

## 重复 control_code

| control_code | 数量 | element ids |
| --- | --- | --- |
| opportunitytab | 9 | 2862, 2863, 2864, 2865, 2866, 2867, 2868, 2869, 2870 |
| Rank | 2 | 1535, 1536 |
| Traceable link | 2 | 1022, 1024 |
| aimesidebarpopup | 2 | 2875, 2876 |
| watchlistTab | 2 | 2858, 2859 |

## 页面短码重复

`page_short` 在不同应用之间重复是常见情况，查询时必须结合 `app_id`。当前重复短码数量：`209`。
