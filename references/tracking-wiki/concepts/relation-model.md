---
title: 真实前后序关系模型
type: concept
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - relation
  - graph
  - ainvest
---

# 真实前后序关系模型

`track_info_realtion.csv` 提供当前埋点和上一个埋点的实际关系。本文档按下面方向解释：

```text
from_stat_id -> stat_id
前序埋点      -> 当前埋点
```

## 覆盖情况

| 指标 | 值 |
| --- | --- |
| 关系总行数 | 29301 |
| 自环关系 | 1423 |
| 非自环关系行 | 27878 |
| 唯一非自环边 | 27878 |
| 覆盖唯一 track_key | 4096 / 13498 |
| 连通分量数 | 144 |
| 最大连通分量节点数 | 2420 |

## 使用方式

- 查某个埋点的前序：找 `stat_id = track_key` 的行，读取 `from_stat_id`。
- 查某个埋点的后序：找 `from_stat_id = track_key` 的行，读取 `stat_id`。
- 查页面或应用级流程：先在应用页找到候选 `track_key`，再扩展其前序/后序。

## 示例 Mermaid

```mermaid
flowchart LR
    A[from_stat_id: previous track] --> B[stat_id: current track]
```

## 注意事项

- 当前关系没有样本量、时间窗口、用户分群和会话口径字段。
- 自环关系通常表示同一埋点重复出现，不能直接解读成页面跳转。
- 关系覆盖约 30% 的唯一 `track_key`，没有关系不代表线上不会发生。
