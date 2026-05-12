---
title: 应用 - 埋点管理平台
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - maidian
  - ainvest
---

# 埋点管理平台

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 30 |
| appSign | maidian |
| appKey | 528779ed3d |
| creator | huangjiarong@myhexin.com |
| createTime | 2025-06-16 19:36:37 |
| topicName | spider-ainvest |
| payloadStatus | 1 |
| pageCount(snapshot) | 1 |
| trackCount(snapshot) | 5 |
| relationTrackCount | 0 |
| tracksWithActionFields | 2 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| cbas | 1 | 5 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1434 | aimeDesign | aime设计页 | 3 | 5 |

## 关系枢纽埋点

暂无关系覆盖。

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14365 | maidian_cbas_aimeDesign | 页面埋点 | 埋点管理平台_cbas_aime设计页 | cbas | aime设计页 | - | - | 2 | 0 | - | 0 | 0 |
| 14700 | maidian_cbas_aimeDesign_importDialog_closeBtn | 元素埋点 | 埋点管理平台_cbas_aime设计页_导入文件弹窗_关闭按钮 | cbas | aime设计页 | 导入文件弹窗 | 关闭按钮 | 0 | 0 | - | 0 | 0 |
| 14701 | maidian_cbas_aimeDesign_importDialog_cryptofeed | 元素埋点 | 埋点管理平台_cbas_aime设计页_导入文件弹窗_cryptofeed | cbas | aime设计页 | 导入文件弹窗 | cryptofeed | 0 | 1 | source | 0 | 0 |
| 14665 | maidian_cbas_aimeDesign_importDialog_selectLocalFileBtn | 元素埋点 | 埋点管理平台_cbas_aime设计页_导入文件弹窗_选择本地文件按钮 | cbas | aime设计页 | 导入文件弹窗 | 选择本地文件按钮 | 0 | 0 | - | 0 | 0 |
| 14364 | maidian_cbas_aimeDesign_reader_subscribe | 元素埋点 | 埋点管理平台_cbas_aime设计页_阅读器_subscribe | cbas | aime设计页 | 阅读器 | subscribe | 0 | 2 | tab, chanId | 0 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### maidian_cbas_aimeDesign_importDialog_cryptofeed

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道,来源 | source | 标识导入来源为Google Drive | string | 0 |

### maidian_cbas_aimeDesign_reader_subscribe

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 套餐类型 | tab | 选择的套餐类型（Professional/Basic） | string | 0 |
| 付费周期 | chanId | 付费周期（年付/季付/月付） | string | 0 |
