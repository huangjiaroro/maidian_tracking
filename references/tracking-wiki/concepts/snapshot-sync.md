---
title: 数据同步说明
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - sync
  - snapshot
  - ainvest
---

# 数据同步说明

- 环境：`ainvest`
- 生成时间：`2026-05-11T13:50:00+08:00`
- 数据来源：下载目录 CSV 文件
- 输出目录：`references/tracking-wiki/`

## 当前使用的主文件

| 对象 | 主文件 |
| --- | --- |
| apps | app_info.csv |
| pages | page_info.csv |
| sections | qk1.csv |
| elements | ys1.csv |
| tracks | track_info.csv |
| relations | track_info_realtion.csv |

## 重新生成

重新导出 CSV 后，用相同文件名放到 `/Users/zyhjr/Downloads`，再重新运行 wiki 生成流程。

## 当前保留范围

- 当前只保留 ainvest 知识库，位于 `references/tracking-wiki/`。
- prod 知识库已移除。
- 当前快照包含 `track_info_realtion.csv`，因此支持前序 / 后序关系查询。
