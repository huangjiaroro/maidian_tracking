---
title: 应用 - 资讯(AinvestNews)
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - lhsn
  - ainvest
---

# 资讯(AinvestNews)

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 22 |
| appSign | lhsn |
| appKey | 4930f0ca0d |
| creator | huangjiarong@myhexin.com |
| createTime | 2026-04-28 15:05:11 |
| topicName | spider-ainvest |
| payloadStatus | 0 |
| pageCount(snapshot) | 5 |
| trackCount(snapshot) | 117 |
| relationTrackCount | 19 |
| tracksWithActionFields | 99 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| mob | 5 | 93 |
| web | 2 | 24 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1223 | newsEarningsDetail | 北美资讯财报站个股页 | 8 | 37 |
| 1220 | newsEarningsHub | 北美资讯财报站聚合页 | 6 | 21 |
| 242 | Wire | 快讯 | 2 | 5 |
| 1093 | newsFeed | 资讯Feed流 | 11 | 51 |
| 547 | newslistpage | 资讯列表页 | 2 | 2 |

## 关系枢纽埋点

| trackKey | 应用 | 页面 | 区块 | 元素 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- |
| lhsn_mob_newsFeed | 资讯(AinvestNews) | 资讯Feed流 | - | - | 16 | 13 |
| lhsn_mob_newsFeed_Newsarticles_newsShow | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | 资讯曝光 | 10 | 19 |
| lhsn_mob_newsFeed_comment_show | 资讯(AinvestNews) | 资讯Feed流 | ios评论引导弹窗评论按钮 | 显示 | 13 | 11 |
| lhsn_mob_newsFeed_content_refresh | 资讯(AinvestNews) | 资讯Feed流 | 内容 | 刷新 | 12 | 12 |
| lhsn_mob_newsFeed_aimeRecSentence_display | 资讯(AinvestNews) | 资讯Feed流 | Aime问句推荐模块 | 曝光 | 4 | 5 |
| lhsn_mob_newsFeed_stockViewpoint_content | 资讯(AinvestNews) | 资讯Feed流 | 个股观点 | 内容 | 5 | 4 |
| lhsn_mob_newsFeed_stockViewpoint_show | 资讯(AinvestNews) | 资讯Feed流 | 个股观点 | 显示 | 4 | 5 |
| lhsn_mob_newsFeed_Newsarticles_click | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | click | 5 | 3 |
| lhsn_mob_newsFeed_Newsarticles_comment | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | 评论 | 5 | 3 |
| lhsn_mob_newsFeed_follow_addfollow | 资讯(AinvestNews) | 资讯Feed流 | 关注 | 加关注 | 3 | 5 |
| lhsn_mob_newsFeed_topnews_click | 资讯(AinvestNews) | 资讯Feed流 | 热点新闻 | click | 5 | 3 |
| lhsn_mob_newsFeed_comment_seeAll | 资讯(AinvestNews) | 资讯Feed流 | ios评论引导弹窗评论按钮 | 查看全部 | 3 | 1 |
| lhsn_mob_newsFeed_stockViewpoint_stocks | 资讯(AinvestNews) | 资讯Feed流 | 个股观点 | 股票 | 2 | 2 |
| lhsn_mob_newsFeed_Newsarticles_like | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | like | 2 | 1 |
| lhsn_mob_newsEarningsDetail_earningsHead_chartbutton | 资讯(AinvestNews) | 北美资讯财报站个股页 | 财报页头部区域 | 图表开关 | 1 | 1 |
| lhsn_mob_newsFeed_Newsarticles_remove | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | 删除 | 1 | 1 |
| lhsn_mob_newsFeed_Newsarticles_share | 资讯(AinvestNews) | 资讯Feed流 | 新闻文章 | 分享 | 1 | 1 |
| lhsn_mob_newsFeed_aimeRecSentence_queryClick | 资讯(AinvestNews) | 资讯Feed流 | Aime问句推荐模块 | 点击问句 | 1 | 1 |
| lhsn_mob_newsFeed_follow_unfollow | 资讯(AinvestNews) | 资讯Feed流 | 关注 | unfollow | 1 | 1 |

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11948 | lhsn_mob | 页面埋点 | 资讯(AinvestNews)_Ainvest APP | mob | - | - | - | 0,2 | 1 | stock | 0 | 0 |
| 12000 | lhsn_mob_newsEarningsDetail | 页面埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页 | mob | 北美资讯财报站个股页 | - | - | 0,1,2,4 | 1 | stock | 0 | 0 |
| 12022 | lhsn_mob_newsEarningsDetail_AIMarketAnalysis_askAime | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_AI解盘_开始对话 | mob | 北美资讯财报站个股页 | AI解盘 | 开始对话 | 0 | 1 | stock | 0 | 0 |
| 12020 | lhsn_mob_newsEarningsDetail_AIMarketAnalysis_share | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_AI解盘_分享 | mob | 北美资讯财报站个股页 | AI解盘 | 分享 | 0 | 1 | stock | 0 | 0 |
| 12021 | lhsn_mob_newsEarningsDetail_AIMarketAnalysis_viewMore | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_AI解盘_查看更多 | mob | 北美资讯财报站个股页 | AI解盘 | 查看更多 | 0 | 1 | stock | 0 | 0 |
| 12028 | lhsn_mob_newsEarningsDetail_aime_askAime | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_aime_开始对话 | mob | 北美资讯财报站个股页 | aime | 开始对话 | 0 | 1 | stock | 0 | 0 |
| 12027 | lhsn_mob_newsEarningsDetail_aime_viewall | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_aime_展开 | mob | 北美资讯财报站个股页 | aime | 展开 | 0 | 1 | stock | 0 | 0 |
| 11999 | lhsn_mob_newsEarningsDetail_earningsCardEntry_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报站卡片入口_卡片 | mob | 北美资讯财报站个股页 | 财报站卡片入口 | 卡片 | 0,2 | 1 | stock | 0 | 0 |
| 12009 | lhsn_mob_newsEarningsDetail_earningsHead_chart | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_图表 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 图表 | 0,1 | 1 | stock | 0 | 0 |
| 12010 | lhsn_mob_newsEarningsDetail_earningsHead_chartbutton | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_图表开关 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 图表开关 | 0 | 1 | stock | 1 | 1 |
| 12004 | lhsn_mob_newsEarningsDetail_earningsHead_earningsSeason | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_财报季度 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 财报季度 | 0 | 1 | stock | 0 | 0 |
| 12007 | lhsn_mob_newsEarningsDetail_earningsHead_filings | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_公告 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 公告 | 0 | 1 | stock | 0 | 0 |
| 12005 | lhsn_mob_newsEarningsDetail_earningsHead_financial | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_财务 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 财务 | 0 | 1 | stock | 0 | 0 |
| 12003 | lhsn_mob_newsEarningsDetail_earningsHead_quotes | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_行情 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 行情 | 0 | 1 | stock | 0 | 0 |
| 12001 | lhsn_mob_newsEarningsDetail_earningsHead_return | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_返回 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 返回 | 0 | 1 | stock | 0 | 0 |
| 12002 | lhsn_mob_newsEarningsDetail_earningsHead_share | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_分享 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 分享 | 0 | 1 | stock | 0 | 0 |
| 12008 | lhsn_mob_newsEarningsDetail_earningsHead_transcript | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_财报页头部区域_会议文稿 | mob | 北美资讯财报站个股页 | 财报页头部区域 | 会议文稿 | 0 | 1 | stock | 0 | 0 |
| 12024 | lhsn_mob_newsEarningsDetail_earningscall_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_电话会议_卡片 | mob | 北美资讯财报站个股页 | 电话会议 | 卡片 | 0,2 | 1 | stock | 0 | 0 |
| 12023 | lhsn_mob_newsEarningsDetail_earningscall_source | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_电话会议_来源 | mob | 北美资讯财报站个股页 | 电话会议 | 来源 | 0 | 1 | stock | 0 | 0 |
| 12026 | lhsn_mob_newsEarningsDetail_news_relatednews | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_news资讯_相关资讯 | mob | 北美资讯财报站个股页 | news资讯 | 相关资讯 | 0,2 | 2 | stock, newsId | 0 | 0 |
| 12025 | lhsn_mob_newsEarningsDetail_vote_polling | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站个股页_投票_投票组件 | mob | 北美资讯财报站个股页 | 投票 | 投票组件 | 0 | 1 | stock | 0 | 0 |
| 11981 | lhsn_mob_newsEarningsHub | 页面埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页 | mob | 北美资讯财报站聚合页 | - | - | 0,1,2,4 | 0 | - | 0 | 0 |
| 11984 | lhsn_mob_newsEarningsHub_calEar_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_日历财报_卡片 | mob | 北美资讯财报站聚合页 | 日历财报 | 卡片 | 0 | 1 | stock | 0 | 0 |
| 11990 | lhsn_mob_newsEarningsHub_earningsCardEntry_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_财报站卡片入口_卡片 | mob | 北美资讯财报站聚合页 | 财报站卡片入口 | 卡片 | 2,0 | 1 | stock | 0 | 0 |
| 11988 | lhsn_mob_newsEarningsHub_earningsCardEntry_moreEarningsEntry | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_财报站卡片入口_跳转更多财报 | mob | 北美资讯财报站聚合页 | 财报站卡片入口 | 跳转更多财报 | 0 | 0 | - | 0 | 0 |
| 11989 | lhsn_mob_newsEarningsHub_earningsCardEntry_subtab | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_财报站卡片入口_子tab | mob | 北美资讯财报站聚合页 | 财报站卡片入口 | 子tab | 0,1 | 1 | tab | 0 | 0 |
| 11982 | lhsn_mob_newsEarningsHub_forwardEarnings_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_热门财报前瞻_卡片 | mob | 北美资讯财报站聚合页 | 热门财报前瞻 | 卡片 | 0 | 1 | stock | 0 | 0 |
| 11987 | lhsn_mob_newsEarningsHub_hotEarnings_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_热门财报卡片_卡片 | mob | 北美资讯财报站聚合页 | 热门财报卡片 | 卡片 | 0,1 | 1 | stock | 0 | 0 |
| 11986 | lhsn_mob_newsEarningsHub_indthm_subtab | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_行业/概念_子tab | mob | 北美资讯财报站聚合页 | 行业/概念 | 子tab | 0,1 | 1 | tab | 0 | 0 |
| 12223 | lhsn_mob_newsEarningsHub_market_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_市场_卡片 | mob | 北美资讯财报站聚合页 | 市场 | 卡片 | 0,2 | 1 | stock | 0 | 0 |
| 12222 | lhsn_mob_newsEarningsHub_market_earningscall | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_市场_三级tab | mob | 北美资讯财报站聚合页 | 市场 | 三级tab | 0,1 | 1 | tab | 0 | 0 |
| 12221 | lhsn_mob_newsEarningsHub_market_moreEarningsEntry | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_市场_跳转更多财报 | mob | 北美资讯财报站聚合页 | 市场 | 跳转更多财报 | 0 | 0 | - | 0 | 0 |
| 12228 | lhsn_mob_newsEarningsHub_market_viewAllEarnings | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_市场_查看全部财报 | mob | 北美资讯财报站聚合页 | 市场 | 查看全部财报 | 0 | 0 | - | 0 | 0 |
| 11991 | lhsn_mob_newsEarningsHub_searchbar_Search | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_搜索框_搜索 | mob | 北美资讯财报站聚合页 | 搜索框 | 搜索 | 0 | 0 | - | 0 | 0 |
| 11992 | lhsn_mob_newsEarningsHub_searchresult_stock | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_北美资讯财报站聚合页_搜索结果_股票 | mob | 北美资讯财报站聚合页 | 搜索结果 | 股票 | 0 | 1 | stock | 0 | 0 |
| 1928 | lhsn_mob_Wire_724_display | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_快讯_快讯_曝光 | mob | 快讯 | 快讯 | 曝光 | 2 | 0 | - | 0 | 0 |
| 1927 | lhsn_mob_Wire_724_share | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_快讯_快讯_分享 | mob | 快讯 | 快讯 | 分享 | 0 | 0 | - | 0 | 0 |
| 1929 | lhsn_mob_Wire_724_stocks | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_快讯_快讯_股票 | mob | 快讯 | 快讯 | 股票 | 0 | 1 | stock | 0 | 0 |
| 1926 | lhsn_mob_Wire_pageTop_tab | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_快讯_页面顶部_tab | mob | 快讯 | 页面顶部 | tab | 0,1 | 1 | tab | 0 | 0 |
| 1925 | lhsn_mob_Wire_topBar_search | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_快讯_app顶部栏_搜索按钮 | mob | 快讯 | app顶部栏 | 搜索按钮 | 0 | 0 | - | 0 | 0 |
| 9489 | lhsn_mob_newsFeed | 页面埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流 | mob | 资讯Feed流 | - | - | 2,4,1,6 | 1 | stayLen | 16 | 13 |
| 9492 | lhsn_mob_newsFeed_Articletab_click | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_ArticleTab_click | mob | 资讯Feed流 | ArticleTab | click | 0 | 1 | content | 0 | 0 |
| 10869 | lhsn_mob_newsFeed_Newsarticles_cancelDown | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_取消点踩 | mob | 资讯Feed流 | 新闻文章 | 取消点踩 | 0 | 1 | content | 0 | 0 |
| 9493 | lhsn_mob_newsFeed_Newsarticles_click | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_click | mob | 资讯Feed流 | 新闻文章 | click | 0 | 1 | content | 5 | 3 |
| 9500 | lhsn_mob_newsFeed_Newsarticles_comment | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_评论 | mob | 资讯Feed流 | 新闻文章 | 评论 | 0 | 1 | content | 5 | 3 |
| 10866 | lhsn_mob_newsFeed_Newsarticles_down | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_点踩 | mob | 资讯Feed流 | 新闻文章 | 点踩 | 0 | 1 | content | 0 | 0 |
| 9497 | lhsn_mob_newsFeed_Newsarticles_like | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_like | mob | 资讯Feed流 | 新闻文章 | like | 0 | 1 | content | 2 | 1 |
| 9510 | lhsn_mob_newsFeed_Newsarticles_newsShow | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_资讯曝光 | mob | 资讯Feed流 | 新闻文章 | 资讯曝光 | 2 | 1 | content | 10 | 19 |
| 9496 | lhsn_mob_newsFeed_Newsarticles_remove | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_删除 | mob | 资讯Feed流 | 新闻文章 | 删除 | 0 | 1 | content | 1 | 1 |
| 9501 | lhsn_mob_newsFeed_Newsarticles_share | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_分享 | mob | 资讯Feed流 | 新闻文章 | 分享 | 0 | 1 | content | 1 | 1 |
| 9498 | lhsn_mob_newsFeed_Newsarticles_unlike | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_新闻文章_取消点赞 | mob | 资讯Feed流 | 新闻文章 | 取消点赞 | 0 | 1 | content | 0 | 0 |
| 9504 | lhsn_mob_newsFeed_aimeRecSentence_aimequestion | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_Aime问句推荐模块_aime问句 | mob | 资讯Feed流 | Aime问句推荐模块 | aime问句 | 0 | 1 | content | 0 | 0 |
| 9502 | lhsn_mob_newsFeed_aimeRecSentence_display | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_Aime问句推荐模块_曝光 | mob | 资讯Feed流 | Aime问句推荐模块 | 曝光 | 2 | 1 | content | 4 | 5 |
| 9540 | lhsn_mob_newsFeed_aimeRecSentence_queryClick | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_Aime问句推荐模块_点击问句 | mob | 资讯Feed流 | Aime问句推荐模块 | 点击问句 | 0 | 1 | content | 1 | 1 |
| 9503 | lhsn_mob_newsFeed_aimeRecSentence_remove | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_Aime问句推荐模块_删除 | mob | 资讯Feed流 | Aime问句推荐模块 | 删除 | 0 | 1 | content | 0 | 0 |
| 10243 | lhsn_mob_newsFeed_comment_seeAll | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_ios评论引导弹窗评论按钮_查看全部 | mob | 资讯Feed流 | ios评论引导弹窗评论按钮 | 查看全部 | 0 | 1 | newsId | 3 | 1 |
| 10244 | lhsn_mob_newsFeed_comment_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_ios评论引导弹窗评论按钮_显示 | mob | 资讯Feed流 | ios评论引导弹窗评论按钮 | 显示 | 2 | 1 | newsId | 13 | 11 |
| 9499 | lhsn_mob_newsFeed_content_refresh | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_内容_刷新 | mob | 资讯Feed流 | 内容 | 刷新 | 6 | 1 | num | 12 | 12 |
| 9509 | lhsn_mob_newsFeed_feedbackWindow_cancel | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_负反馈浮窗_取消 | mob | 资讯Feed流 | 负反馈浮窗 | 取消 | 0 | 0 | - | 0 | 0 |
| 10868 | lhsn_mob_newsFeed_feedbackWindow_close | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_负反馈浮窗_关闭 | mob | 资讯Feed流 | 负反馈浮窗 | 关闭 | 0 | 1 | content | 0 | 0 |
| 10867 | lhsn_mob_newsFeed_feedbackWindow_confirm | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_负反馈浮窗_确认 | mob | 资讯Feed流 | 负反馈浮窗 | 确认 | 0 | 1 | content | 0 | 0 |
| 9508 | lhsn_mob_newsFeed_feedbackWindow_select | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_负反馈浮窗_选择 | mob | 资讯Feed流 | 负反馈浮窗 | 选择 | 0 | 2 | content, itemId | 0 | 0 |
| 9494 | lhsn_mob_newsFeed_follow_addfollow | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_关注_加关注 | mob | 资讯Feed流 | 关注 | 加关注 | 0 | 1 | content | 3 | 5 |
| 9495 | lhsn_mob_newsFeed_follow_unfollow | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_关注_unfollow | mob | 资讯Feed流 | 关注 | unfollow | 0 | 1 | content | 1 | 1 |
| 9490 | lhsn_mob_newsFeed_multilingual_click | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_多语言_click | mob | 资讯Feed流 | 多语言 | click | 0 | 1 | content | 0 | 0 |
| 9710 | lhsn_mob_newsFeed_multilingual_languages | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_多语言_多语言切换 | mob | 资讯Feed流 | 多语言 | 多语言切换 | 0 | 1 | content | 0 | 0 |
| 9708 | lhsn_mob_newsFeed_multilingual_optButton | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_多语言_自选按钮 | mob | 资讯Feed流 | 多语言 | 自选按钮 | 0 | 0 | - | 0 | 0 |
| 9507 | lhsn_mob_newsFeed_rateInterest_remove | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_兴趣评分_删除 | mob | 资讯Feed流 | 兴趣评分 | 删除 | 0 | 0 | - | 0 | 0 |
| 9506 | lhsn_mob_newsFeed_rateInterest_select | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_兴趣评分_选择 | mob | 资讯Feed流 | 兴趣评分 | 选择 | 0 | 1 | value | 0 | 0 |
| 9505 | lhsn_mob_newsFeed_rateInterest_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_兴趣评分_显示 | mob | 资讯Feed流 | 兴趣评分 | 显示 | 2 | 0 | - | 0 | 0 |
| 11363 | lhsn_mob_newsFeed_screenerCard_Screener | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_选股策略卡片_选股 | mob | 资讯Feed流 | 选股策略卡片 | 选股 | 0 | 1 | content | 0 | 0 |
| 11361 | lhsn_mob_newsFeed_screenerCard_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_选股策略卡片_显示 | mob | 资讯Feed流 | 选股策略卡片 | 显示 | 2 | 1 | content | 0 | 0 |
| 11364 | lhsn_mob_newsFeed_screenerCard_stocks | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_选股策略卡片_股票 | mob | 资讯Feed流 | 选股策略卡片 | 股票 | 0 | 2 | stock, content | 0 | 0 |
| 11365 | lhsn_mob_newsFeed_screenerCard_viewAll | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_选股策略卡片_viewAll | mob | 资讯Feed流 | 选股策略卡片 | viewAll | 0 | 1 | content | 0 | 0 |
| 9709 | lhsn_mob_newsFeed_search_buttons | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_搜索模块按钮_按钮 | mob | 资讯Feed流 | 搜索模块按钮 | 按钮 | 0 | 0 | - | 0 | 0 |
| 11362 | lhsn_mob_newsFeed_socialtrading_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_高手平台_显示 | mob | 资讯Feed流 | 高手平台 | 显示 | 2 | 0 | - | 0 | 0 |
| 10240 | lhsn_mob_newsFeed_stockViewpoint_comment | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_评论 | mob | 资讯Feed流 | 个股观点 | 评论 | 0 | 2 | stock, itemId | 0 | 0 |
| 10238 | lhsn_mob_newsFeed_stockViewpoint_content | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_内容 | mob | 资讯Feed流 | 个股观点 | 内容 | 0,1 | 2 | stock, itemId | 5 | 4 |
| 10239 | lhsn_mob_newsFeed_stockViewpoint_like | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_like | mob | 资讯Feed流 | 个股观点 | like | 0 | 2 | stock, itemId | 0 | 0 |
| 10241 | lhsn_mob_newsFeed_stockViewpoint_share | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_分享 | mob | 资讯Feed流 | 个股观点 | 分享 | 0 | 2 | stock, itemId | 0 | 0 |
| 10237 | lhsn_mob_newsFeed_stockViewpoint_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_显示 | mob | 资讯Feed流 | 个股观点 | 显示 | 2 | 2 | stock, itemId | 4 | 5 |
| 10242 | lhsn_mob_newsFeed_stockViewpoint_stocks | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_个股观点_股票 | mob | 资讯Feed流 | 个股观点 | 股票 | 0 | 1 | stock | 2 | 2 |
| 10235 | lhsn_mob_newsFeed_topnews | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_热点新闻 | mob | 资讯Feed流 | 热点新闻 | 显示 | 2 | 1 | newsId | 0 | 0 |
| 10236 | lhsn_mob_newsFeed_topnews_click | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_热点新闻_click | mob | 资讯Feed流 | 热点新闻 | click | 0 | 1 | newsId | 5 | 3 |
| 10559 | lhsn_mob_newsFeed_trackleaders_fullview | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_大v跟踪_显示全部 | mob | 资讯Feed流 | 大v跟踪 | 显示全部 | 0 | 0 | - | 0 | 0 |
| 10561 | lhsn_mob_newsFeed_trackleaders_leaders | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_大v跟踪_高手列表 | mob | 资讯Feed流 | 大v跟踪 | 高手列表 | 0,2 | 2 | tab, content | 0 | 0 |
| 10560 | lhsn_mob_newsFeed_trackleaders_tab | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_大v跟踪_tab | mob | 资讯Feed流 | 大v跟踪 | tab | 0 | 2 | content, targetId | 0 | 0 |
| 10562 | lhsn_mob_newsFeed_trackleaders_viewmore | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_大v跟踪_查看更多 | mob | 资讯Feed流 | 大v跟踪 | 查看更多 | 0 | 0 | - | 0 | 0 |
| 9512 | lhsn_mob_newsFeed_unfollowWindow_cancel | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_取消关注弹窗_取消 | mob | 资讯Feed流 | 取消关注弹窗 | 取消 | 0 | 1 | content | 0 | 0 |
| 9511 | lhsn_mob_newsFeed_unfollowWindow_show | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_取消关注弹窗_显示 | mob | 资讯Feed流 | 取消关注弹窗 | 显示 | 2 | 1 | content | 0 | 0 |
| 9513 | lhsn_mob_newsFeed_unfollowWindow_unfollow | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯Feed流_取消关注弹窗_unfollow | mob | 资讯Feed流 | 取消关注弹窗 | unfollow | 0 | 1 | content | 0 | 0 |
| 6452 | lhsn_mob_newslistpage_articlelist_banner | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯列表页_要闻列表页_banner位 | mob | 资讯列表页 | 要闻列表页 | banner位 | 0,1,2 | 1 | bannerId | 0 | 0 |
| 6453 | lhsn_mob_newslistpage_newswirelist_banner | 元素埋点 | 资讯(AinvestNews)_Ainvest APP_资讯列表页_快讯列表页_banner位 | mob | 资讯列表页 | 快讯列表页 | banner位 | 0,1,2 | 1 | bannerId | 0 | 0 |
| 12030 | lhsn_web_newsEarningsDetail | 页面埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页 | web | 北美资讯财报站个股页 | - | - | 0,1,2,4 | 1 | stock | 0 | 0 |
| 12039 | lhsn_web_newsEarningsDetail_AIMarketAnalysis_askAime | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_AI解盘_开始对话 | web | 北美资讯财报站个股页 | AI解盘 | 开始对话 | 0 | 1 | stock | 0 | 0 |
| 12037 | lhsn_web_newsEarningsDetail_AIMarketAnalysis_share | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_AI解盘_分享 | web | 北美资讯财报站个股页 | AI解盘 | 分享 | 0 | 1 | stock | 0 | 0 |
| 12038 | lhsn_web_newsEarningsDetail_AIMarketAnalysis_viewMore | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_AI解盘_查看更多 | web | 北美资讯财报站个股页 | AI解盘 | 查看更多 | 0 | 1 | stock | 0 | 0 |
| 12045 | lhsn_web_newsEarningsDetail_aime_askAime | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_aime_开始对话 | web | 北美资讯财报站个股页 | aime | 开始对话 | 0 | 1 | stock | 0 | 0 |
| 12044 | lhsn_web_newsEarningsDetail_aime_viewall | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_aime_展开 | web | 北美资讯财报站个股页 | aime | 展开 | 0 | 1 | stock | 0 | 0 |
| 12029 | lhsn_web_newsEarningsDetail_earningsCardEntry_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报站卡片入口_卡片 | web | 北美资讯财报站个股页 | 财报站卡片入口 | 卡片 | 0,2 | 1 | stock | 0 | 0 |
| 12036 | lhsn_web_newsEarningsDetail_earningsHead_chart | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_图表 | web | 北美资讯财报站个股页 | 财报页头部区域 | 图表 | 0 | 1 | stock | 0 | 0 |
| 12032 | lhsn_web_newsEarningsDetail_earningsHead_earningsSeason | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_财报季度 | web | 北美资讯财报站个股页 | 财报页头部区域 | 财报季度 | 0 | 2 | stock, tab | 0 | 0 |
| 12034 | lhsn_web_newsEarningsDetail_earningsHead_filings | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_公告 | web | 北美资讯财报站个股页 | 财报页头部区域 | 公告 | 0 | 1 | stock | 0 | 0 |
| 12033 | lhsn_web_newsEarningsDetail_earningsHead_financial | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_财务 | web | 北美资讯财报站个股页 | 财报页头部区域 | 财务 | 0 | 1 | stock | 0 | 0 |
| 12031 | lhsn_web_newsEarningsDetail_earningsHead_quotes | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_行情 | web | 北美资讯财报站个股页 | 财报页头部区域 | 行情 | 0 | 1 | stock | 0 | 0 |
| 12035 | lhsn_web_newsEarningsDetail_earningsHead_transcript | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_财报页头部区域_会议文稿 | web | 北美资讯财报站个股页 | 财报页头部区域 | 会议文稿 | 0 | 1 | stock | 0 | 0 |
| 12041 | lhsn_web_newsEarningsDetail_earningscall_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_电话会议_卡片 | web | 北美资讯财报站个股页 | 电话会议 | 卡片 | 0,2 | 1 | stock | 0 | 0 |
| 12040 | lhsn_web_newsEarningsDetail_earningscall_source | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_电话会议_来源 | web | 北美资讯财报站个股页 | 电话会议 | 来源 | 0 | 1 | stock | 0 | 0 |
| 12043 | lhsn_web_newsEarningsDetail_news_relatednews | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_news资讯_相关资讯 | web | 北美资讯财报站个股页 | news资讯 | 相关资讯 | 0,2 | 2 | stock, newsId | 0 | 0 |
| 12042 | lhsn_web_newsEarningsDetail_vote_polling | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站个股页_投票_投票组件 | web | 北美资讯财报站个股页 | 投票 | 投票组件 | 0 | 1 | stock | 0 | 0 |
| 11993 | lhsn_web_newsEarningsHub | 页面埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页 | web | 北美资讯财报站聚合页 | - | - | 0,1,2,4 | 0 | - | 0 | 0 |
| 12229 | lhsn_web_newsEarningsHub_calEar_stockclick | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_日历财报_个股点击 | web | 北美资讯财报站聚合页 | 日历财报 | 个股点击 | 0 | 1 | stock | 0 | 0 |
| 11995 | lhsn_web_newsEarningsHub_forwardEarnings_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_热门财报前瞻_卡片 | web | 北美资讯财报站聚合页 | 热门财报前瞻 | 卡片 | 0 | 1 | stock | 0 | 0 |
| 11997 | lhsn_web_newsEarningsHub_hotEarnings_Card | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_热门财报卡片_卡片 | web | 北美资讯财报站聚合页 | 热门财报卡片 | 卡片 | 0,1 | 1 | stock | 0 | 0 |
| 11996 | lhsn_web_newsEarningsHub_indthm_subtab | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_行业/概念_子tab | web | 北美资讯财报站聚合页 | 行业/概念 | 子tab | 0,1 | 1 | tab | 0 | 0 |
| 11994 | lhsn_web_newsEarningsHub_searchbar_Search | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_搜索框_搜索 | web | 北美资讯财报站聚合页 | 搜索框 | 搜索 | 0 | 0 | - | 0 | 0 |
| 11998 | lhsn_web_newsEarningsHub_searchresult_stocks | 元素埋点 | 资讯(AinvestNews)_Ainvest Web_北美资讯财报站聚合页_搜索结果_股票 | web | 北美资讯财报站聚合页 | 搜索结果 | 股票 | 0 | 1 | stock | 0 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### lhsn_mob

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,1,4 |

### lhsn_mob_newsEarningsDetail_AIMarketAnalysis_askAime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_AIMarketAnalysis_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_AIMarketAnalysis_viewMore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_aime_askAime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_aime_viewall

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsCardEntry_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,2 |

### lhsn_mob_newsEarningsDetail_earningsHead_chart

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_chartbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_earningsSeason

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_filings

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_financial

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_return

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningsHead_transcript

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,2 |

### lhsn_mob_newsEarningsDetail_earningscall_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_earningscall_source

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsDetail_news_relatednews

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 资讯ID | newsId | - | string | 0 |

### lhsn_mob_newsEarningsDetail_vote_polling

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_calEar_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_earningsCardEntry_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_earningsCardEntry_subtab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsn_mob_newsEarningsHub_forwardEarnings_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_hotEarnings_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_indthm_subtab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsn_mob_newsEarningsHub_market_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsEarningsHub_market_earningscall

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsn_mob_newsEarningsHub_searchresult_stock

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_Wire_724_stocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 通过点击股票标签，跳转到对应个股详情页 | string | 0 |

### lhsn_mob_Wire_pageTop_tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 记录用户点击与滑动切换表头的行为，通过不同值区分不同的tab | string | 1,0 |

### lhsn_mob_newsFeed

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 携带停留时长 | int | 4 |

### lhsn_mob_newsFeed_Articletab_click

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带选择的TAB | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_cancelDown

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带rec_info | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_click

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带用户点击的资讯标识 | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_comment

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带评论的文章标识 | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_down

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带rec_INFO | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_like

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带点赞的文章标识 | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_newsShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带卡片ID | string | 2 |

### lhsn_mob_newsFeed_Newsarticles_remove

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带需要移除的文章标识 | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带分享的文章标识 | string | 0 |

### lhsn_mob_newsFeed_Newsarticles_unlike

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带取消点赞的文章标识 | string | 0 |

### lhsn_mob_newsFeed_aimeRecSentence_aimequestion

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带点击的问句标识 | string | 0 |

### lhsn_mob_newsFeed_aimeRecSentence_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带展示问句标识 | string | 2 |

### lhsn_mob_newsFeed_aimeRecSentence_queryClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带点击的问句标识 | string | 0 |

### lhsn_mob_newsFeed_aimeRecSentence_remove

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带相关删除的问句标识 | string | 0 |

### lhsn_mob_newsFeed_comment_seeAll

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 资讯ID | newsId | 携带newsid | string | 0 |

### lhsn_mob_newsFeed_comment_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 资讯ID | newsId | 携带newsid | string | 2 |

### lhsn_mob_newsFeed_content_refresh

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 统计下拉刷新次数 | int | 6 |

### lhsn_mob_newsFeed_feedbackWindow_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带rec_info | string | 0 |

### lhsn_mob_newsFeed_feedbackWindow_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带所选的负反馈类型 | string | 0 |

### lhsn_mob_newsFeed_feedbackWindow_select

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带选择的原因类型（1.不感兴趣 2.不喜欢这一类 2.无用 4.质量低） | string | 0 |
| 物品id | itemId | 携带负反馈的物品ID | string | 0 |

### lhsn_mob_newsFeed_follow_addfollow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带关注的作者标识 | string | 0 |

### lhsn_mob_newsFeed_follow_unfollow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带取消关注的作者标识 | string | 0 |

### lhsn_mob_newsFeed_multilingual_click

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带语言类型 | string | 0 |

### lhsn_mob_newsFeed_multilingual_languages

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带语言标识 | string | 0 |

### lhsn_mob_newsFeed_rateInterest_select

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 数值 | value | 携带选择的评价等级 | string | 0 |

### lhsn_mob_newsFeed_screenerCard_Screener

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带策略id | string | 0 |

### lhsn_mob_newsFeed_screenerCard_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带展示的策略id | string | 2 |

### lhsn_mob_newsFeed_screenerCard_stocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 携带点击的个股id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带点击策略id | string | 0 |

### lhsn_mob_newsFeed_screenerCard_viewAll

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带点击的策略id | string | 0 |

### lhsn_mob_newsFeed_stockViewpoint_comment

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 物品id | itemId | 携带物品id | string | 0 |

### lhsn_mob_newsFeed_stockViewpoint_content

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 携带股票代码 | string | 0 |
| 物品id | itemId | 携带物品ID | string | 0 |

### lhsn_mob_newsFeed_stockViewpoint_like

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 物品id | itemId | 携带物品ID | string | 0 |

### lhsn_mob_newsFeed_stockViewpoint_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 物品id | itemId | 携带物品ID | string | 0 |

### lhsn_mob_newsFeed_stockViewpoint_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 携带展示的股票代码 | string | 2 |
| 物品id | itemId | 携带物品ID数组 | string | 2 |

### lhsn_mob_newsFeed_stockViewpoint_stocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_mob_newsFeed_topnews

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 资讯ID | newsId | 参数携带资讯ID或标识 | string | 2 |

### lhsn_mob_newsFeed_topnews_click

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 资讯ID | newsId | 携带资讯ID或标识 | string | 0 |

### lhsn_mob_newsFeed_trackleaders_leaders

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | financial influencer、high return、most followers、best risk control、stability、high frequency、rising stars、top etf returns | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回高手用户昵称 | string | 0 |

### lhsn_mob_newsFeed_trackleaders_tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | financial influencer、high return、most followers、best risk control、stability、high frequency、rising stars、top etf returns | string | 0 |
| 场景ID | targetId | 返回第几个tab“1、2、3.... | string | 0 |

### lhsn_mob_newsFeed_unfollowWindow_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带作者标识 | string | 0 |

### lhsn_mob_newsFeed_unfollowWindow_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带取消关注作者标识 | string | 2 |

### lhsn_mob_newsFeed_unfollowWindow_unfollow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带作者标识 | string | 0 |

### lhsn_mob_newslistpage_articlelist_banner

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| banner位id | bannerId | 记录用户点击的banner id；及每个banner id的曝光数量，需要根据用户id做去重处理 | string | 0,2 |

### lhsn_mob_newslistpage_newswirelist_banner

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| banner位id | bannerId | 记录用户点击的banner id；及每个banner id的曝光数量，需要根据用户id做去重处理 | string | 0,2 |

### lhsn_web_newsEarningsDetail

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,1,2,4 |

### lhsn_web_newsEarningsDetail_AIMarketAnalysis_askAime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_AIMarketAnalysis_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_AIMarketAnalysis_viewMore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_aime_askAime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_aime_viewall

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsCardEntry_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,2 |

### lhsn_web_newsEarningsDetail_earningsHead_chart

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsHead_earningsSeason

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsHead_filings

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsHead_financial

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsHead_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningsHead_transcript

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningscall_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_earningscall_source

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsDetail_news_relatednews

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 资讯ID | newsId | - | string | 0 |

### lhsn_web_newsEarningsDetail_vote_polling

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsHub_calEar_stockclick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsHub_forwardEarnings_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsHub_hotEarnings_Card

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsn_web_newsEarningsHub_indthm_subtab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsn_web_newsEarningsHub_searchresult_stocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
