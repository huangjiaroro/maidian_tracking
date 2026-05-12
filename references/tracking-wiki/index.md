---
title: Index — ainvest 埋点平台 Wiki
type: index
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
tags:
  - tracking
  - ainvest
  - index
---

# Index — ainvest 埋点平台 Wiki

> 基于下载目录 CSV 构建的 ainvest 环境埋点结构化知识库，用于回答应用、页面、区块、元素、埋点 ID 和真实前后序关系查询。

## Navigation

- [[#Concepts]] · [[#Lookups]] · [[#Relations]] · [[#Applications]] · [[#Open Questions]]

## Concepts

- [[concepts/tracking-model|埋点平台对象模型]]
- [[concepts/track-key-patterns|埋点命名规则]]
- [[concepts/query-playbook|埋点查询策略]]
- [[concepts/relation-model|真实前后序关系模型]]
- [[concepts/data-quality|数据质量与缺口]]
- [[concepts/snapshot-sync|数据同步说明]]
- [[entities/business-lines|业务线索引]]

## Lookups

- [[entities/lookups/page-lookup|页面反查索引]]
- [[entities/lookups/section-lookup|区块反查索引]]
- [[entities/lookups/element-lookup|元素反查索引]]

## Relations

- [[entities/relations/high-degree-tracks|高连接埋点]]
- [[entities/relations/relation-components|关系连通分量]]

## Applications

- [[entities/apps/app-11-lhsws|AInvestWebScreener]]
- [[entities/apps/app-21-aichat|AI万事屋]]
- [[entities/apps/app-31-dailybrew|DailyBrew]]
- [[entities/apps/app-32-hxkline|HXKline]]
- [[entities/apps/app-20-notex|Notex.ai]]
- [[entities/apps/app-10-lhspc|PC客户端（AInvestPC）]]
- [[entities/apps/app-19-lhsps|PennyStock]]
- [[entities/apps/app-33-pixlore|Pixlore]]
- [[entities/apps/app-35-rdify|Readify]]
- [[entities/apps/app-38-tf|TalkFlow]]
- [[entities/apps/app-23-aime|aime]]
- [[entities/apps/app-40-aimeapp|aimeApp]]
- [[entities/apps/app-36-deepa|deepAnalysis]]
- [[entities/apps/app-37-deepad|deepAnalysisDreamface]]
- [[entities/apps/app-16-lhsbd|券商(AinvestBroker)]]
- [[entities/apps/app-27-lhsbdw|券商Web(AInvestBrokersWeb)]]
- [[entities/apps/app-30-maidian|埋点管理平台]]
- [[entities/apps/app-12-lhsa|手机客户端（AInvestApp）]]
- [[entities/apps/app-39-quickbi|敏捷BI]]
- [[entities/apps/app-29-chatbi|智能BI]]
- [[entities/apps/app-17-lhspt|模拟炒股(StockSimulator)]]
- [[entities/apps/app-22-lhsn|资讯(AinvestNews)]]
- [[entities/apps/app-18-lhssc|选股(StockScreener)]]

## Open Questions

- `track_info_realtion.csv` 的关系来自当前导出的实际数据，但未包含时间窗口、用户分群和样本量口径，需要补充来源口径。
- `page_info1.csv` 未出现在下载目录；当前使用 `page_info.csv`，并确认 `page_info2.csv` 与它完全一致。
- `qk1/qk2` 与 `ys1/ys2/ys3` 是重复导出还是多环境分片，需要从导出任务侧确认。
