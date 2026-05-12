---
title: 应用 - PC客户端（AInvestPC）
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - lhspc
  - ainvest
---

# PC客户端（AInvestPC）

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 10 |
| appSign | lhspc |
| appKey | 71a7548313 |
| creator | huangjiarong@myhexin.com |
| createTime | 2026-04-28 15:03:37 |
| topicName | spider-ainvest |
| payloadStatus | 0 |
| pageCount(snapshot) | 60 |
| trackCount(snapshot) | 408 |
| relationTrackCount | 8 |
| tracksWithActionFields | 126 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| pc | 60 | 408 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 176 | aiReturn | AI收益预测模块 | 0 | 1 |
| 272 | chartSettings | Chart设置页面 | 2 | 24 |
| 432 | etfs | ETF榜单 | 0 | 10 |
| 4 | chart | K线主图（chart） | 7 | 58 |
| 426 | pinescriptEditor | PineScript指标编辑器 | 2 | 1 |
| 9 | miniWatchlist | mini股票列表（miniWatchlist） | 3 | 14 |
| 511 | push | push弹窗 | 0 | 2 |
| 445 | Stocks | 个股 | 0 | 8 |
| 178 | news | 个股新闻模块 | 3 | 5 |
| 181 | smartMoney | 主力资金追踪模块 | 3 | 4 |
| 131 | trade | 交易下单模块 | 4 | 6 |
| 132 | tradeLog | 交易登陆页面 | 0 | 1 |
| 715 | tradeError | 交易相关错误弹窗 | 0 | 1 |
| 441 | mainEvent | 全局功能 | 0 | 4 |
| 431 | globalMovers | 全球榜单 | 0 | 14 |
| 179 | filings | 公告模块 | 3 | 5 |
| 8 | keyStatistics | 关键数据（keyStatistics） | 3 | 7 |
| 143 | incomState | 利润表模块 | 3 | 4 |
| 555 | selectBrokers | 券商选择页面 | 0 | 4 |
| 177 | update | 升级页面 | 3 | 2 |
| 127 | uninstal | 卸载页面 | 0 | 1 |
| 487 | feedbackCenter | 反馈中心 | 4 | 7 |
| 717 | orderCancel | 取消订单弹窗 | 0 | 2 |
| 126 | setUp | 安装页面 | 4 | 6 |
| 427 | marketIndex | 市场指数 | 0 | 4 |
| 180 | delayTip | 延时行情提示模块 | 3 | 2 |
| 7 | timeSales | 成交明细（timeSales） | 3 | 4 |
| 6 | headQuotes | 报价头（headQuotes） | 3 | 4 |
| 129 | position | 持仓模块 | 4 | 7 |
| 206 | indicatorEditor | 指标编辑器页面 | 0 | 1 |
| 205 | indicatorsSet | 指标设置弹窗 | 0 | 2 |
| 292 | newuserPop | 新用户股票池弹窗 | 0 | 3 |
| 428 | advancersDecliners | 涨跌统计 | 0 | 4 |
| 291 | visitorPop | 游客弹窗 | 0 | 3 |
| 430 | trendingStocks | 热度榜单 | 0 | 6 |
| 145 | cashFlow | 现金流量表模块 | 3 | 4 |
| 125 | pageLogi | 登录页面 | 2 | 4 |
| 294 | stocksMonitor | 短线精灵模块 | 3 | 11 |
| 509 | profile | 简况Profile | 0 | 4 |
| 1086 | manageFlags | 管理标记弹窗 | 4 | 6 |
| 302 | systemSettings | 系统设置 | 4 | 22 |
| 142 | operaAnalys | 经营分析模块 | 3 | 4 |
| 271 | customTools | 自定义工具箱页面 | 0 | 3 |
| 270 | custom | 自定义页面 | 3 | 3 |
| 442 | Watchlist | 自选列表 | 0 | 3 |
| 108 | wtclists | 行情列表 | 3 | 20 |
| 429 | marketMovers | 行情榜单 | 0 | 11 |
| 716 | orderPending | 订单排队弹窗 | 0 | 2 |
| 130 | orders | 订单模块 | 4 | 8 |
| 714 | orderSubmit | 订单确认弹窗 | 0 | 2 |
| 5 | orderbook | 订单表（orderbook） | 3 | 4 |
| 558 | setPin | 设置PIN弹窗 | 0 | 1 |
| 516 | financials | 财务 | 0 | 4 |
| 128 | secAccou | 账户信息模块 | 3 | 8 |
| 144 | balanSheet | 资产负债表模块 | 3 | 4 |
| 556 | enterPin | 输入PIN弹窗页面 | 0 | 2 |
| 119 | minChart | 迷你走势图（miniChart） | 3 | 4 |
| 557 | resetPin | 重置PIN弹窗 | 0 | 1 |
| 304 | hideConfirm | 隐藏提示弹窗 | 0 | 3 |
| 124 | mainPage | 页面主框架 | 8 | 39 |

## 关系枢纽埋点

| trackKey | 应用 | 页面 | 区块 | 元素 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- |
| lhspc_pc_mainEvent_navigation_search | PC客户端（AInvestPC） | 全局功能 | 导航栏 | 搜索按钮 | 6 | 5 |
| lhspc_pc_mainEvent | PC客户端（AInvestPC） | 全局功能 | - | - | 5 | 4 |
| lhspc_pc_Stocks_Stock_quotes | PC客户端（AInvestPC） | 个股 | 个股 | 行情 | 4 | 3 |
| lhspc_pc_Stocks_Stock_interval | PC客户端（AInvestPC） | 个股 | 个股 | 周期 | 3 | 3 |
| lhspc_pc_Watchlist_Watchlists_mywatchlist | PC客户端（AInvestPC） | 自选列表 | 自选列表 | 我的自选股 | 3 | 3 |
| lhspc_pc_mainEvent_search_addWatch | PC客户端（AInvestPC） | 全局功能 | 搜索模块按钮 | 加自选 | 1 | 3 |
| lhspc_pc_mainEvent_search_openchart | PC客户端（AInvestPC） | 全局功能 | 搜索模块按钮 | 打开行情 | 1 | 3 |
| lhspc_pc_Stocks_Stock_linestyle | PC客户端（AInvestPC） | 个股 | 个股 | 线型 | 1 | 0 |

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1308 | lhspc_pc_aiReturn | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_AI收益预测模块 | pc | AI收益预测模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2220 | lhspc_pc_chartSettings_axisPlac_axisPlace | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线纵坐标位置_坐标轴位置 | pc | Chart设置页面 | K线纵坐标位置 | 坐标轴位置 | 0 | 1 | content | 0 | 0 |
| 2219 | lhspc_pc_chartSettings_caAxtype_axisType | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线纵坐标类型_坐标轴类型 | pc | Chart设置页面 | K线纵坐标类型 | 坐标轴类型 | 0 | 1 | content | 0 | 0 |
| 2218 | lhspc_pc_chartSettings_candMode_type | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线主图模式_类型 | pc | Chart设置页面 | K线主图模式 | 类型 | 0 | 1 | content | 0 | 0 |
| 2216 | lhspc_pc_chartSettings_candlGap_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线缺口gap_关闭 | pc | Chart设置页面 | K线缺口gap | 关闭 | 0 | 0 | - | 0 | 0 |
| 2215 | lhspc_pc_chartSettings_candlGap_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线缺口gap_打开 | pc | Chart设置页面 | K线缺口gap | 打开 | 0 | 1 | content | 0 | 0 |
| 2203 | lhspc_pc_chartSettings_crosline_color | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_十字线_颜色 | pc | Chart设置页面 | 十字线 | 颜色 | 0 | 1 | content | 0 | 0 |
| 2204 | lhspc_pc_chartSettings_crosline_style | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_十字线_风格 | pc | Chart设置页面 | 十字线 | 风格 | 0 | 1 | content | 0 | 0 |
| 2224 | lhspc_pc_chartSettings_flipSub_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_副图翻转_关闭 | pc | Chart设置页面 | 副图翻转 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2223 | lhspc_pc_chartSettings_flipSub_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_副图翻转_打开 | pc | Chart设置页面 | 副图翻转 | 打开 | 0 | 0 | - | 0 | 0 |
| 2226 | lhspc_pc_chartSettings_funcBar_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_功能按钮_关闭 | pc | Chart设置页面 | 功能按钮 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2225 | lhspc_pc_chartSettings_funcBar_reset | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_功能按钮_重置 | pc | Chart设置页面 | 功能按钮 | 重置 | 0 | 0 | - | 0 | 0 |
| 2210 | lhspc_pc_chartSettings_highLow_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_最高价最低价_关闭 | pc | Chart设置页面 | 最高价最低价 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2209 | lhspc_pc_chartSettings_highLow_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_最高价最低价_打开 | pc | Chart设置页面 | 最高价最低价 | 打开 | 0 | 0 | - | 0 | 0 |
| 2217 | lhspc_pc_chartSettings_inAxtype_axisType | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_分时纵坐标类型_坐标轴类型 | pc | Chart设置页面 | 分时纵坐标类型 | 坐标轴类型 | 0 | 1 | content | 0 | 0 |
| 2205 | lhspc_pc_chartSettings_intrLine_color | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_分时线_颜色 | pc | Chart设置页面 | 分时线 | 颜色 | 0 | 1 | content | 0 | 0 |
| 2206 | lhspc_pc_chartSettings_intrLine_width | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_分时线_线宽 | pc | Chart设置页面 | 分时线 | 线宽 | 0 | 1 | content | 0 | 0 |
| 2212 | lhspc_pc_chartSettings_intraAvg_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_分时均线_关闭 | pc | Chart设置页面 | 分时均线 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2211 | lhspc_pc_chartSettings_intraAvg_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_分时均线_打开 | pc | Chart设置页面 | 分时均线 | 打开 | 0 | 0 | - | 0 | 0 |
| 2208 | lhspc_pc_chartSettings_lastPric_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_最新价线_关闭 | pc | Chart设置页面 | 最新价线 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2207 | lhspc_pc_chartSettings_lastPric_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_最新价线_打开 | pc | Chart设置页面 | 最新价线 | 打开 | 0 | 0 | - | 0 | 0 |
| 2221 | lhspc_pc_chartSettings_leftAxis_axisType | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线左侧纵坐标_坐标轴类型 | pc | Chart设置页面 | K线左侧纵坐标 | 坐标轴类型 | 0 | 1 | content | 0 | 0 |
| 2222 | lhspc_pc_chartSettings_righAxis_axisType | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_K线右侧纵坐标_坐标轴类型 | pc | Chart设置页面 | K线右侧纵坐标 | 坐标轴类型 | 0 | 1 | content | 0 | 0 |
| 2214 | lhspc_pc_chartSettings_window_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_主图浮窗_关闭 | pc | Chart设置页面 | 主图浮窗 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2213 | lhspc_pc_chartSettings_window_open | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_Chart设置页面_主图浮窗_打开 | pc | Chart设置页面 | 主图浮窗 | 打开 | 0 | 1 | content | 0 | 0 |
| 4656 | lhspc_pc_etfs | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单 | pc | ETF榜单 | - | - | 2 | 1 | tab | 0 | 0 |
| 4697 | lhspc_pc_etfs_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_功能按钮_弹出 | pc | ETF榜单 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4696 | lhspc_pc_etfs_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_功能按钮_插入 | pc | ETF榜单 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4698 | lhspc_pc_etfs_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_功能按钮_删除 | pc | ETF榜单 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 4680 | lhspc_pc_etfs_rangeBox_range | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_排序浮框_排序方式 | pc | ETF榜单 | 排序浮框 | 排序方式 | 0 | 1 | content | 0 | 0 |
| 4679 | lhspc_pc_etfs_secClass_52highTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_二级分类_52周最高tab | pc | ETF榜单 | 二级分类 | 52周最高tab | 0 | 0 | - | 0 | 0 |
| 5050 | lhspc_pc_etfs_secClass_52lowTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_二级分类_52周最低tab | pc | ETF榜单 | 二级分类 | 52周最低tab | 0 | 0 | - | 0 | 0 |
| 4678 | lhspc_pc_etfs_secClass_actTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_二级分类_ActiveTab | pc | ETF榜单 | 二级分类 | ActiveTab | 0 | 0 | - | 0 | 0 |
| 4676 | lhspc_pc_etfs_secClass_gainTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_二级分类_gainersTab | pc | ETF榜单 | 二级分类 | gainersTab | 0 | 0 | - | 0 | 0 |
| 4677 | lhspc_pc_etfs_secClass_losTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_ETF榜单_二级分类_losersTab | pc | ETF榜单 | 二级分类 | losersTab | 0 | 0 | - | 0 | 0 |
| 17 | lhspc_pc_chart | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart） | pc | K线主图（chart） | - | - | 2 | 3 | tab, mkt, stock | 0 | 0 |
| 1802 | lhspc_pc_chart_allDraw_customize | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_所有画线_定制 | pc | K线主图（chart） | 所有画线 | 定制 | 0 | 0 | - | 0 | 0 |
| 1801 | lhspc_pc_chart_allDraw_drawName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_所有画线_画线名称 | pc | K线主图（chart） | 所有画线 | 画线名称 | 0 | 1 | content | 0 | 0 |
| 1793 | lhspc_pc_chart_candStat_candleStat | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_区间统计_区间统计 | pc | K线主图（chart） | 区间统计 | 区间统计 | 2 | 0 | - | 0 | 0 |
| 1102 | lhspc_pc_chart_change_symbol | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_更换内容_股票代码 | pc | K线主图（chart） | 更换内容 | 股票代码 | 2 | 3 | periods, stock, mkt | 0 | 0 |
| 12 | lhspc_pc_chart_chart_chartSet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_主图设置（chartSet） | pc | K线主图（chart） | K线主图（chart） | 主图设置（chartSet） | 0 | 0 | - | 0 | 0 |
| 8 | lhspc_pc_chart_chart_drawlines | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_画线（drawlines） | pc | K线主图（chart） | K线主图（chart） | 画线（drawlines） | 0 | 1 | line | 0 | 0 |
| 9 | lhspc_pc_chart_chart_indicators | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_指标（indicators） | pc | K线主图（chart） | K线主图（chart） | 指标（indicators） | 0 | 1 | tab | 0 | 0 |
| 11 | lhspc_pc_chart_chart_indicatorsSet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_指标设置（indicatorsSet） | pc | K线主图（chart） | K线主图（chart） | 指标设置（indicatorsSet） | 0 | 0 | - | 0 | 0 |
| 3 | lhspc_pc_chart_chart_intervalsSet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_周期设置（intervalsSet） | pc | K线主图（chart） | K线主图（chart） | 周期设置（intervalsSet） | 0 | 0 | - | 0 | 0 |
| 10 | lhspc_pc_chart_chart_lineStyle | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线主图（chart）_线型（lineStyle） | pc | K线主图（chart） | K线主图（chart） | 线型（lineStyle） | 0 | 1 | tab | 0 | 0 |
| 1804 | lhspc_pc_chart_draStbar_background | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_背景 | pc | K线主图（chart） | 画笔设置条 | 背景 | 0 | 1 | content | 0 | 0 |
| 1803 | lhspc_pc_chart_draStbar_color | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_颜色 | pc | K线主图（chart） | 画笔设置条 | 颜色 | 0 | 1 | content | 0 | 0 |
| 1812 | lhspc_pc_chart_draStbar_fontColor | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_字体颜色 | pc | K线主图（chart） | 画笔设置条 | 字体颜色 | 0 | 1 | content | 0 | 0 |
| 1811 | lhspc_pc_chart_draStbar_fontSize | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_字体大小 | pc | K线主图（chart） | 画笔设置条 | 字体大小 | 0 | 1 | content | 0 | 0 |
| 1808 | lhspc_pc_chart_draStbar_lock | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_锁定 | pc | K线主图（chart） | 画笔设置条 | 锁定 | 0 | 0 | - | 0 | 0 |
| 1810 | lhspc_pc_chart_draStbar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_删除 | pc | K线主图（chart） | 画笔设置条 | 删除 | 0 | 0 | - | 0 | 0 |
| 1807 | lhspc_pc_chart_draStbar_settings | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_settings | pc | K线主图（chart） | 画笔设置条 | settings | 0 | 0 | - | 0 | 0 |
| 1806 | lhspc_pc_chart_draStbar_style | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_风格 | pc | K线主图（chart） | 画笔设置条 | 风格 | 0 | 1 | content | 0 | 0 |
| 1809 | lhspc_pc_chart_draStbar_unlock | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_解锁 | pc | K线主图（chart） | 画笔设置条 | 解锁 | 0 | 0 | - | 0 | 0 |
| 1805 | lhspc_pc_chart_draStbar_width | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画笔设置条_线宽 | pc | K线主图（chart） | 画笔设置条 | 线宽 | 0 | 1 | content | 0 | 0 |
| 1800 | lhspc_pc_chart_drawings_allTools | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_全部工具 | pc | K线主图（chart） | 画线显示区域 | 全部工具 | 0 | 0 | - | 0 | 0 |
| 1795 | lhspc_pc_chart_drawings_crossPerid | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_跨周期 | pc | K线主图（chart） | 画线显示区域 | 跨周期 | 0 | 1 | switch | 0 | 0 |
| 986 | lhspc_pc_chart_drawings_drawName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_画线名称 | pc | K线主图（chart） | 画线显示区域 | 画线名称 | 0 | 3 | content, switch, periods | 0 | 0 |
| 1797 | lhspc_pc_chart_drawings_hideAll | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_隐藏全部 | pc | K线主图（chart） | 画线显示区域 | 隐藏全部 | 0 | 0 | - | 0 | 0 |
| 1794 | lhspc_pc_chart_drawings_magnet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_自动吸附 | pc | K线主图（chart） | 画线显示区域 | 自动吸附 | 0 | 1 | switch | 0 | 0 |
| 1799 | lhspc_pc_chart_drawings_removeAll | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_删除全部 | pc | K线主图（chart） | 画线显示区域 | 删除全部 | 0 | 0 | - | 0 | 0 |
| 1798 | lhspc_pc_chart_drawings_showAll | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_显示全部 | pc | K线主图（chart） | 画线显示区域 | 显示全部 | 0 | 0 | - | 0 | 0 |
| 1796 | lhspc_pc_chart_drawings_stayDraw | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_画线显示区域_连续画线 | pc | K线主图（chart） | 画线显示区域 | 连续画线 | 0 | 1 | switch | 0 | 0 |
| 2188 | lhspc_pc_chart_funcBar_chartSet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_主图设置（chartSet） | pc | K线主图（chart） | 功能按钮 | 主图设置（chartSet） | 0 | 0 | - | 0 | 0 |
| 2228 | lhspc_pc_chart_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_弹出 | pc | K线主图（chart） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 911 | lhspc_pc_chart_funcBar_drawings | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_画线（drawings） | pc | K线主图（chart） | 功能按钮 | 画线（drawings） | 0 | 0 | - | 0 | 0 |
| 909 | lhspc_pc_chart_funcBar_indicators | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_指标（indicators） | pc | K线主图（chart） | 功能按钮 | 指标（indicators） | 0 | 0 | - | 0 | 0 |
| 2227 | lhspc_pc_chart_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_插入 | pc | K线主图（chart） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 910 | lhspc_pc_chart_funcBar_lineStyle | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_线型（lineStyle） | pc | K线主图（chart） | 功能按钮 | 线型（lineStyle） | 0 | 0 | - | 0 | 0 |
| 912 | lhspc_pc_chart_funcBar_more | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_更多 | pc | K线主图（chart） | 功能按钮 | 更多 | 0 | 0 | - | 0 | 0 |
| 2229 | lhspc_pc_chart_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_功能按钮_删除 | pc | K线主图（chart） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 984 | lhspc_pc_chart_indctors_indicaName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_指标显示区域_指标名称 | pc | K线主图（chart） | 指标显示区域 | 指标名称 | 0 | 3 | content, switch, periods | 0 | 0 |
| 987 | lhspc_pc_chart_interval_tsFrame | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_时段_变更周期按钮 | pc | K线主图（chart） | 时段 | 变更周期按钮 | 0 | 1 | content | 0 | 0 |
| 985 | lhspc_pc_chart_lineStyl_listyName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_线型显示区域_线型名称 | pc | K线主图（chart） | 线型显示区域 | 线型名称 | 0 | 2 | content, periods | 0 | 0 |
| 913 | lhspc_pc_chart_more_chipDibtin | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_more浮框_筹码 | pc | K线主图（chart） | more浮框 | 筹码 | 0 | 0 | - | 0 | 0 |
| 1319 | lhspc_pc_chart_quoteCha_1d | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_行情切换_盘中 | pc | K线主图（chart） | 行情切换 | 盘中 | 0 | 0 | - | 0 | 0 |
| 1320 | lhspc_pc_chart_quoteCha_after | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_行情切换_盘后 | pc | K线主图（chart） | 行情切换 | 盘后 | 0 | 0 | - | 0 | 0 |
| 1318 | lhspc_pc_chart_quoteCha_pre | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_行情切换_盘前 | pc | K线主图（chart） | 行情切换 | 盘前 | 0 | 0 | - | 0 | 0 |
| 1541 | lhspc_pc_chart_range_timeFrame | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线Range_时间范围 | pc | K线主图（chart） | K线Range | 时间范围 | 0 | 1 | content | 0 | 0 |
| 914 | lhspc_pc_chart_rigtMenu_addStock | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_addStock | pc | K线主图（chart） | 右键菜单 | addStock | 0 | 0 | - | 0 | 0 |
| 2197 | lhspc_pc_chart_rigtMenu_axisPlace | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_坐标轴位置 | pc | K线主图（chart） | 右键菜单 | 坐标轴位置 | 0 | 1 | content | 0 | 0 |
| 2196 | lhspc_pc_chart_rigtMenu_axisType | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_坐标轴类型 | pc | K线主图（chart） | 右键菜单 | 坐标轴类型 | 0 | 1 | content | 0 | 0 |
| 2199 | lhspc_pc_chart_rigtMenu_chartSet | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_主图设置（chartSet） | pc | K线主图（chart） | 右键菜单 | 主图设置（chartSet） | 0 | 0 | - | 0 | 0 |
| 915 | lhspc_pc_chart_rigtMenu_delete | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_删除 | pc | K线主图（chart） | 右键菜单 | 删除 | 0 | 0 | - | 0 | 0 |
| 2198 | lhspc_pc_chart_rigtMenu_invertScal | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_坐标轴翻转 | pc | K线主图（chart） | 右键菜单 | 坐标轴翻转 | 0 | 0 | - | 0 | 0 |
| 2194 | lhspc_pc_chart_rigtMenu_removeDraw | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_删除全部画线 | pc | K线主图（chart） | 右键菜单 | 删除全部画线 | 0 | 0 | - | 0 | 0 |
| 2195 | lhspc_pc_chart_rigtMenu_removeIndi | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_删除全部指标 | pc | K线主图（chart） | 右键菜单 | 删除全部指标 | 0 | 0 | - | 0 | 0 |
| 2200 | lhspc_pc_chart_rigtMenu_resetChart | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_右键菜单_重置图表 | pc | K线主图（chart） | 右键菜单 | 重置图表 | 0 | 0 | - | 0 | 0 |
| 2193 | lhspc_pc_chart_search_symbol | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_搜索模块按钮_股票代码 | pc | K线主图（chart） | 搜索模块按钮 | 股票代码 | 0 | 1 | content | 0 | 0 |
| 1075 | lhspc_pc_chart_topInfo_symbol | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_顶部股票信息区域_股票代码 | pc | K线主图（chart） | 顶部股票信息区域 | 股票代码 | 2 | 3 | stock, mkt, periods | 0 | 0 |
| 2202 | lhspc_pc_chart_yAxis_reset | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线Y轴_重置 | pc | K线主图（chart） | K线Y轴 | 重置 | 7 | 0 | - | 0 | 0 |
| 2201 | lhspc_pc_chart_yAxis_zoom | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_K线主图（chart）_K线Y轴_缩放 | pc | K线主图（chart） | K线Y轴 | 缩放 | 6 | 0 | - | 0 | 0 |
| 4637 | lhspc_pc_pinescriptEditor | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_PineScript指标编辑器 | pc | PineScript指标编辑器 | - | - | 2 | 1 | tab | 0 | 0 |
| 904 | lhspc_pc_miniWatchlist | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist） | pc | mini股票列表（miniWatchlist） | - | - | 2 | 1 | tab | 0 | 0 |
| 2189 | lhspc_pc_miniWatchlist_funcBar_1d | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_盘中 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 盘中 | 0 | 0 | - | 0 | 0 |
| 2190 | lhspc_pc_miniWatchlist_funcBar_60d | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_60日 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 60日 | 0 | 0 | - | 0 | 0 |
| 2191 | lhspc_pc_miniWatchlist_funcBar_PE | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_市盈率 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 市盈率 | 0 | 0 | - | 0 | 0 |
| 2192 | lhspc_pc_miniWatchlist_funcBar_change | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_change | pc | mini股票列表（miniWatchlist） | 功能按钮 | change | 0 | 0 | - | 0 | 0 |
| 2246 | lhspc_pc_miniWatchlist_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_弹出 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2245 | lhspc_pc_miniWatchlist_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_插入 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2247 | lhspc_pc_miniWatchlist_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_功能按钮_删除 | pc | mini股票列表（miniWatchlist） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 905 | lhspc_pc_miniWatchlist_midColum_1d | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_中间项_盘中 | pc | mini股票列表（miniWatchlist） | 中间项 | 盘中 | 2 | 0 | - | 0 | 0 |
| 906 | lhspc_pc_miniWatchlist_midColum_60d | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_中间项_60日 | pc | mini股票列表（miniWatchlist） | 中间项 | 60日 | 2 | 0 | - | 0 | 0 |
| 907 | lhspc_pc_miniWatchlist_midColum_PE | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_中间项_市盈率 | pc | mini股票列表（miniWatchlist） | 中间项 | 市盈率 | 2 | 0 | - | 0 | 0 |
| 908 | lhspc_pc_miniWatchlist_midColum_change | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_中间项_change | pc | mini股票列表（miniWatchlist） | 中间项 | change | 2 | 0 | - | 0 | 0 |
| 13 | lhspc_pc_miniWatchlist_miniWatchlist_flag | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_mini股票列表（miniWatchlist）_标记（flag） | pc | mini股票列表（miniWatchlist） | mini股票列表（miniWatchlist） | 标记（flag） | 0 | 0 | - | 0 | 0 |
| 14 | lhspc_pc_miniWatchlist_miniWatchlist_flagSymbol | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_mini股票列表（miniWatchlist）_mini股票列表（miniWatchlist）_标记符号（flagSymbo… | pc | mini股票列表（miniWatchlist） | mini股票列表（miniWatchlist） | 标记符号（flagSymbol） | 0 | 0 | - | 0 | 0 |
| 5962 | lhspc_pc_push_funcBar_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_push弹窗_功能按钮_关闭 | pc | push弹窗 | 功能按钮 | 关闭 | 0 | 0 | - | 0 | 0 |
| 5963 | lhspc_pc_push_funcBar_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_push弹窗_功能按钮_打开 | pc | push弹窗 | 功能按钮 | 打开 | 0 | 1 | content | 0 | 0 |
| 4867 | lhspc_pc_Stocks_Stock_indicators | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_个股_指标（indicators） | pc | 个股 | 个股 | 指标（indicators） | 0 | 1 | tab | 0 | 0 |
| 4865 | lhspc_pc_Stocks_Stock_interval | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_个股_周期 | pc | 个股 | 个股 | 周期 | 0 | 1 | tab | 3 | 3 |
| 4866 | lhspc_pc_Stocks_Stock_linestyle | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_个股_线型 | pc | 个股 | 个股 | 线型 | 0 | 1 | tab | 1 | 0 |
| 4862 | lhspc_pc_Stocks_Stock_quotes | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_个股_行情 | pc | 个股 | 个股 | 行情 | 2 | 0 | - | 4 | 3 |
| 4886 | lhspc_pc_Stocks_Stock_search | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_个股_搜索按钮 | pc | 个股 | 个股 | 搜索按钮 | 0 | 0 | - | 0 | 0 |
| 4864 | lhspc_pc_Stocks_leftlist_Lastviewed | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_小列表_最近浏览 | pc | 个股 | 小列表 | 最近浏览 | 0 | 0 | - | 0 | 0 |
| 4863 | lhspc_pc_Stocks_leftlist_mywatchlist | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_小列表_我的自选股 | pc | 个股 | 小列表 | 我的自选股 | 0 | 0 | - | 0 | 0 |
| 4887 | lhspc_pc_Stocks_search_openchart | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_个股_搜索模块按钮_打开行情 | pc | 个股 | 搜索模块按钮 | 打开行情 | 7 | 0 | - | 0 | 0 |
| 1314 | lhspc_pc_news | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_个股新闻模块 | pc | 个股新闻模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2281 | lhspc_pc_news_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_个股新闻模块_功能按钮_弹出 | pc | 个股新闻模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2280 | lhspc_pc_news_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_个股新闻模块_功能按钮_插入 | pc | 个股新闻模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2282 | lhspc_pc_news_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_个股新闻模块_功能按钮_删除 | pc | 个股新闻模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 1316 | lhspc_pc_news_news_newsList | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_个股新闻模块_news资讯_newsList | pc | 个股新闻模块 | news资讯 | newsList | 0 | 1 | news | 0 | 0 |
| 1309 | lhspc_pc_smartMoney | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_主力资金追踪模块 | pc | 主力资金追踪模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2287 | lhspc_pc_smartMoney_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_主力资金追踪模块_功能按钮_弹出 | pc | 主力资金追踪模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2286 | lhspc_pc_smartMoney_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_主力资金追踪模块_功能按钮_插入 | pc | 主力资金追踪模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2288 | lhspc_pc_smartMoney_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_主力资金追踪模块_功能按钮_删除 | pc | 主力资金追踪模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 1010 | lhspc_pc_trade | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块 | pc | 交易下单模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 1013 | lhspc_pc_trade_buy_buy | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块_买入_buy | pc | 交易下单模块 | 买入 | buy | 0 | 0 | - | 0 | 0 |
| 2252 | lhspc_pc_trade_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块_功能按钮_弹出 | pc | 交易下单模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2251 | lhspc_pc_trade_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块_功能按钮_插入 | pc | 交易下单模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2253 | lhspc_pc_trade_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块_功能按钮_删除 | pc | 交易下单模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 1014 | lhspc_pc_trade_sell_sell | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易下单模块_卖出_sell | pc | 交易下单模块 | 卖出 | sell | 0 | 0 | - | 0 | 0 |
| 1011 | lhspc_pc_tradeLog_login_login | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_交易登陆页面_登陆_login | pc | 交易登陆页面 | 登陆 | login | 0 | 0 | - | 0 | 0 |
| 6721 | lhspc_pc_tradeError | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_交易相关错误弹窗 | pc | 交易相关错误弹窗 | - | - | 2 | 1 | content | 0 | 0 |
| 9826 | lhspc_pc_mainEvent | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_全局功能 | pc | 全局功能 | - | - | 2 | 0 | - | 5 | 4 |
| 4868 | lhspc_pc_mainEvent_navigation_search | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全局功能_导航栏_搜索按钮 | pc | 全局功能 | 导航栏 | 搜索按钮 | 0 | 0 | - | 6 | 5 |
| 4888 | lhspc_pc_mainEvent_search_addWatch | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全局功能_搜索模块按钮_加自选 | pc | 全局功能 | 搜索模块按钮 | 加自选 | 0 | 0 | - | 1 | 3 |
| 4869 | lhspc_pc_mainEvent_search_openchart | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全局功能_搜索模块按钮_打开行情 | pc | 全局功能 | 搜索模块按钮 | 打开行情 | 7 | 0 | - | 1 | 3 |
| 4653 | lhspc_pc_globalMovers | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单 | pc | 全球榜单 | - | - | 2 | 1 | tab | 0 | 0 |
| 4691 | lhspc_pc_globalMovers_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_功能按钮_弹出 | pc | 全球榜单 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4690 | lhspc_pc_globalMovers_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_功能按钮_插入 | pc | 全球榜单 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4692 | lhspc_pc_globalMovers_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_功能按钮_删除 | pc | 全球榜单 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 4673 | lhspc_pc_globalMovers_rangeBox_range | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_排序浮框_排序方式 | pc | 全球榜单 | 排序浮框 | 排序方式 | 0 | 1 | content | 0 | 0 |
| 4672 | lhspc_pc_globalMovers_secClass_argentina | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_阿根廷 | pc | 全球榜单 | 二级分类 | 阿根廷 | 0 | 0 | - | 0 | 0 |
| 4671 | lhspc_pc_globalMovers_secClass_brazil | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_巴西 | pc | 全球榜单 | 二级分类 | 巴西 | 0 | 0 | - | 0 | 0 |
| 4666 | lhspc_pc_globalMovers_secClass_canada | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_加拿大 | pc | 全球榜单 | 二级分类 | 加拿大 | 0 | 0 | - | 0 | 0 |
| 4664 | lhspc_pc_globalMovers_secClass_china | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_中国 | pc | 全球榜单 | 二级分类 | 中国 | 0 | 0 | - | 0 | 0 |
| 4668 | lhspc_pc_globalMovers_secClass_eu | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_欧盟 | pc | 全球榜单 | 二级分类 | 欧盟 | 0 | 0 | - | 0 | 0 |
| 4665 | lhspc_pc_globalMovers_secClass_india | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_印度(India) | pc | 全球榜单 | 二级分类 | 印度(India) | 0 | 0 | - | 0 | 0 |
| 4669 | lhspc_pc_globalMovers_secClass_japan | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_日本 | pc | 全球榜单 | 二级分类 | 日本 | 0 | 0 | - | 0 | 0 |
| 4670 | lhspc_pc_globalMovers_secClass_korea | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_韩国 | pc | 全球榜单 | 二级分类 | 韩国 | 0 | 0 | - | 0 | 0 |
| 4667 | lhspc_pc_globalMovers_secClass_uk | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_全球榜单_二级分类_英国 | pc | 全球榜单 | 二级分类 | 英国 | 0 | 0 | - | 0 | 0 |
| 1315 | lhspc_pc_filings | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_公告模块 | pc | 公告模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 1317 | lhspc_pc_filings_filings_filingList | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_公告模块_公告_公告列表 | pc | 公告模块 | 公告 | 公告列表 | 0 | 1 | news | 0 | 0 |
| 2284 | lhspc_pc_filings_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_公告模块_功能按钮_弹出 | pc | 公告模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2283 | lhspc_pc_filings_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_公告模块_功能按钮_插入 | pc | 公告模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2285 | lhspc_pc_filings_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_公告模块_功能按钮_删除 | pc | 公告模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6 | lhspc_pc_keyStatistics | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics） | pc | 关键数据（keyStatistics） | - | - | 2 | 4 | indicatorsState, stock, mkt, tab | 0 | 0 |
| 2187 | lhspc_pc_keyStatistics_funcBar_collapse | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_功能按钮_收起 | pc | 关键数据（keyStatistics） | 功能按钮 | 收起 | 0 | 0 | - | 0 | 0 |
| 2234 | lhspc_pc_keyStatistics_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_功能按钮_弹出 | pc | 关键数据（keyStatistics） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2186 | lhspc_pc_keyStatistics_funcBar_expand | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_功能按钮_展开 | pc | 关键数据（keyStatistics） | 功能按钮 | 展开 | 0 | 0 | - | 0 | 0 |
| 2233 | lhspc_pc_keyStatistics_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_功能按钮_插入 | pc | 关键数据（keyStatistics） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2235 | lhspc_pc_keyStatistics_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_功能按钮_删除 | pc | 关键数据（keyStatistics） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 15 | lhspc_pc_keyStatistics_keyStatistics_angle | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_关键数据（keyStatistics）_关键数据（keyStatistics）_展开控件 | pc | 关键数据（keyStatistics） | 关键数据（keyStatistics） | 展开控件 | 0 | 1 | indicatorsState | 0 | 0 |
| 1095 | lhspc_pc_incomState | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_利润表模块 | pc | 利润表模块 | - | - | 2 | 2 | stock, mkt | 0 | 0 |
| 2272 | lhspc_pc_incomState_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_利润表模块_功能按钮_弹出 | pc | 利润表模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2271 | lhspc_pc_incomState_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_利润表模块_功能按钮_插入 | pc | 利润表模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2273 | lhspc_pc_incomState_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_利润表模块_功能按钮_删除 | pc | 利润表模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6518 | lhspc_pc_selectBrokers | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_券商选择页面 | pc | 券商选择页面 | - | - | 2 | 0 | - | 0 | 0 |
| 6521 | lhspc_pc_selectBrokers_funcBar_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_券商选择页面_功能按钮_关闭 | pc | 券商选择页面 | 功能按钮 | 关闭 | 0 | 0 | - | 0 | 0 |
| 6519 | lhspc_pc_selectBrokers_funcBar_connect | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_券商选择页面_功能按钮_连接 | pc | 券商选择页面 | 功能按钮 | 连接 | 0 | 1 | content | 0 | 0 |
| 6520 | lhspc_pc_selectBrokers_funcBar_openAccount | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_券商选择页面_功能按钮_开户 | pc | 券商选择页面 | 功能按钮 | 开户 | 0 | 1 | content | 0 | 0 |
| 1313 | lhspc_pc_update_update_failed | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_升级页面_更新_失败 | pc | 升级页面 | 更新 | 失败 | 2 | 0 | - | 0 | 0 |
| 1312 | lhspc_pc_update_update_success | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_升级页面_更新_成功 | pc | 升级页面 | 更新 | 成功 | 2 | 0 | - | 0 | 0 |
| 1005 | lhspc_pc_uninstal_uninstal_uninstall | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_卸载页面_卸载_卸载 | pc | 卸载页面 | 卸载 | 卸载 | 0 | 0 | - | 0 | 0 |
| 5594 | lhspc_pc_feedbackCenter_feedbackDetails_display | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_反馈详情_曝光 | pc | 反馈中心 | 反馈详情 | 曝光 | 2 | 0 | - | 0 | 0 |
| 5596 | lhspc_pc_feedbackCenter_feedbackDetails_noResolve | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_反馈详情_未解决 | pc | 反馈中心 | 反馈详情 | 未解决 | 0 | 0 | - | 0 | 0 |
| 5597 | lhspc_pc_feedbackCenter_feedbackDetails_reSubmit | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_反馈详情_再次提交 | pc | 反馈中心 | 反馈详情 | 再次提交 | 0 | 0 | - | 0 | 0 |
| 5595 | lhspc_pc_feedbackCenter_feedbackDetails_resolve | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_反馈详情_已解决 | pc | 反馈中心 | 反馈详情 | 已解决 | 0 | 0 | - | 0 | 0 |
| 5591 | lhspc_pc_feedbackCenter_feedback_display | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_意见反馈_曝光 | pc | 反馈中心 | 意见反馈 | 曝光 | 2 | 0 | - | 0 | 0 |
| 5592 | lhspc_pc_feedbackCenter_feedback_submit | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_意见反馈_提交 | pc | 反馈中心 | 意见反馈 | 提交 | 0 | 0 | - | 0 | 0 |
| 5593 | lhspc_pc_feedbackCenter_myFeedback_display | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_反馈中心_我的反馈列表_曝光 | pc | 反馈中心 | 我的反馈列表 | 曝光 | 2 | 0 | - | 0 | 0 |
| 6724 | lhspc_pc_orderCancel | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_取消订单弹窗 | pc | 取消订单弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 6725 | lhspc_pc_orderCancel_funcBar_confirm | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_取消订单弹窗_功能按钮_确认 | pc | 取消订单弹窗 | 功能按钮 | 确认 | 0 | 0 | - | 0 | 0 |
| 2601 | lhspc_pc_setUp_autStart_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_安装页面_开机自启动_关闭 | pc | 安装页面 | 开机自启动 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2600 | lhspc_pc_setUp_autStart_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_安装页面_开机自启动_打开 | pc | 安装页面 | 开机自启动 | 打开 | 0 | 0 | - | 0 | 0 |
| 2602 | lhspc_pc_setUp_funcBar_openClient | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_安装页面_功能按钮_打开客户端 | pc | 安装页面 | 功能按钮 | 打开客户端 | 0 | 0 | - | 0 | 0 |
| 2599 | lhspc_pc_setUp_install_failed | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_安装页面_安装_失败 | pc | 安装页面 | 安装 | 失败 | 2 | 0 | - | 0 | 0 |
| 1003 | lhspc_pc_setUp_install_start | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_安装页面_安装_开始 | pc | 安装页面 | 安装 | 开始 | 0 | 0 | - | 0 | 0 |
| 1004 | lhspc_pc_setUp_install_success | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_安装页面_安装_成功 | pc | 安装页面 | 安装 | 成功 | 2 | 0 | - | 0 | 0 |
| 4643 | lhspc_pc_marketIndex | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_市场指数 | pc | 市场指数 | - | - | 2 | 1 | tab | 0 | 0 |
| 4682 | lhspc_pc_marketIndex_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_市场指数_功能按钮_弹出 | pc | 市场指数 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4681 | lhspc_pc_marketIndex_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_市场指数_功能按钮_插入 | pc | 市场指数 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4683 | lhspc_pc_marketIndex_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_市场指数_功能按钮_删除 | pc | 市场指数 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 4043 | lhspc_pc_delayTip_delayTip_learnMore | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_延时行情提示模块_延时行情提示_查看详情 | pc | 延时行情提示模块 | 延时行情提示 | 查看详情 | 0 | 0 | - | 0 | 0 |
| 1321 | lhspc_pc_delayTip_delayTip_login | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_延时行情提示模块_延时行情提示_login | pc | 延时行情提示模块 | 延时行情提示 | login | 0 | 0 | - | 0 | 0 |
| 16 | lhspc_pc_timeSales | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_成交明细（timeSales） | pc | 成交明细（timeSales） | - | - | 2 | 3 | stock, mkt, tab | 0 | 0 |
| 2240 | lhspc_pc_timeSales_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_成交明细（timeSales）_功能按钮_弹出 | pc | 成交明细（timeSales） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2239 | lhspc_pc_timeSales_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_成交明细（timeSales）_功能按钮_插入 | pc | 成交明细（timeSales） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2241 | lhspc_pc_timeSales_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_成交明细（timeSales）_功能按钮_删除 | pc | 成交明细（timeSales） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 5 | lhspc_pc_headQuotes | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_报价头（headQuotes） | pc | 报价头（headQuotes） | - | - | 2 | 3 | stock, mkt, tab | 0 | 0 |
| 2231 | lhspc_pc_headQuotes_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_报价头（headQuotes）_功能按钮_弹出 | pc | 报价头（headQuotes） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2230 | lhspc_pc_headQuotes_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_报价头（headQuotes）_功能按钮_插入 | pc | 报价头（headQuotes） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2232 | lhspc_pc_headQuotes_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_报价头（headQuotes）_功能按钮_删除 | pc | 报价头（headQuotes） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 1007 | lhspc_pc_position | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_持仓模块 | pc | 持仓模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2263 | lhspc_pc_position_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_持仓模块_功能按钮_弹出 | pc | 持仓模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2262 | lhspc_pc_position_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_持仓模块_功能按钮_插入 | pc | 持仓模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2264 | lhspc_pc_position_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_持仓模块_功能按钮_删除 | pc | 持仓模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6713 | lhspc_pc_position_link_linkBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_持仓模块_连接_连接券商 | pc | 持仓模块 | 连接 | 连接券商 | 0 | 0 | - | 0 | 0 |
| 6714 | lhspc_pc_position_login_loginBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_持仓模块_登陆_登录券商 | pc | 持仓模块 | 登陆 | 登录券商 | 0 | 0 | - | 0 | 0 |
| 6712 | lhspc_pc_position_operation_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_持仓模块_操作_关闭 | pc | 持仓模块 | 操作 | 关闭 | 0 | 0 | - | 0 | 0 |
| 1540 | lhspc_pc_indicatorEditor | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_指标编辑器页面 | pc | 指标编辑器页面 | - | - | 2 | 0 | - | 0 | 0 |
| 1537 | lhspc_pc_indicatorsSet | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_指标设置弹窗 | pc | 指标设置弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 1538 | lhspc_pc_indicatorsSet_funcBar_newIndica | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_指标设置弹窗_功能按钮_新建指标 | pc | 指标设置弹窗 | 功能按钮 | 新建指标 | 0 | 0 | - | 0 | 0 |
| 2468 | lhspc_pc_newuserPop | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_新用户股票池弹窗 | pc | 新用户股票池弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 2469 | lhspc_pc_newuserPop_funcBar_addWatch | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_新用户股票池弹窗_功能按钮_加自选 | pc | 新用户股票池弹窗 | 功能按钮 | 加自选 | 0 | 0 | - | 0 | 0 |
| 2470 | lhspc_pc_newuserPop_funcBar_notInt | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_新用户股票池弹窗_功能按钮_不感兴趣 | pc | 新用户股票池弹窗 | 功能按钮 | 不感兴趣 | 0 | 0 | - | 0 | 0 |
| 4651 | lhspc_pc_advancersDecliners | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_涨跌统计 | pc | 涨跌统计 | - | - | 2 | 1 | tab | 0 | 0 |
| 4685 | lhspc_pc_advancersDecliners_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_涨跌统计_功能按钮_弹出 | pc | 涨跌统计 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4684 | lhspc_pc_advancersDecliners_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_涨跌统计_功能按钮_插入 | pc | 涨跌统计 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4686 | lhspc_pc_advancersDecliners_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_涨跌统计_功能按钮_删除 | pc | 涨跌统计 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 2465 | lhspc_pc_visitorPop | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_游客弹窗 | pc | 游客弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 2466 | lhspc_pc_visitorPop_funcBar_login | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_游客弹窗_功能按钮_login | pc | 游客弹窗 | 功能按钮 | login | 0 | 0 | - | 0 | 0 |
| 2467 | lhspc_pc_visitorPop_funcBar_signup | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_游客弹窗_功能按钮_注册 | pc | 游客弹窗 | 功能按钮 | 注册 | 0 | 0 | - | 0 | 0 |
| 4654 | lhspc_pc_trendingStocks | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单 | pc | 热度榜单 | - | - | 2 | 1 | tab | 0 | 0 |
| 4694 | lhspc_pc_trendingStocks_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单_功能按钮_弹出 | pc | 热度榜单 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4693 | lhspc_pc_trendingStocks_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单_功能按钮_插入 | pc | 热度榜单 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4695 | lhspc_pc_trendingStocks_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单_功能按钮_删除 | pc | 热度榜单 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 4674 | lhspc_pc_trendingStocks_secClass_24hHot | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单_二级分类_24hHot | pc | 热度榜单 | 二级分类 | 24hHot | 0 | 0 | - | 0 | 0 |
| 4675 | lhspc_pc_trendingStocks_secClass_mostMen | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_热度榜单_二级分类_最多提及 | pc | 热度榜单 | 二级分类 | 最多提及 | 0 | 0 | - | 0 | 0 |
| 1097 | lhspc_pc_cashFlow | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_现金流量表模块 | pc | 现金流量表模块 | - | - | 2 | 2 | stock, mkt | 0 | 0 |
| 2278 | lhspc_pc_cashFlow_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_现金流量表模块_功能按钮_弹出 | pc | 现金流量表模块 | 功能按钮 | 弹出 | 2 | 0 | - | 0 | 0 |
| 2277 | lhspc_pc_cashFlow_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_现金流量表模块_功能按钮_插入 | pc | 现金流量表模块 | 功能按钮 | 插入 | 2 | 1 | tab | 0 | 0 |
| 2279 | lhspc_pc_cashFlow_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_现金流量表模块_功能按钮_删除 | pc | 现金流量表模块 | 功能按钮 | 删除 | 2 | 0 | - | 0 | 0 |
| 2952 | lhspc_pc_pageLogi_login_success | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_登录页面_登陆_成功 | pc | 登录页面 | 登陆 | 成功 | 0 | 1 | content | 0 | 0 |
| 1000 | lhspc_pc_pageLogi_password_login | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_登录页面_账密登录_login | pc | 登录页面 | 账密登录 | login | 0 | 0 | - | 0 | 0 |
| 1002 | lhspc_pc_pageLogi_signUp_signup | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_登录页面_注册（signUp）_注册 | pc | 登录页面 | 注册（signUp） | 注册 | 0 | 0 | - | 0 | 0 |
| 1001 | lhspc_pc_pageLogi_sms_login | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_登录页面_验证码登录_login | pc | 登录页面 | 验证码登录 | login | 0 | 0 | - | 0 | 0 |
| 2487 | lhspc_pc_stocksMonitor | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块 | pc | 短线精灵模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2495 | lhspc_pc_stocksMonitor_funcBar_all | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_全部 | pc | 短线精灵模块 | 功能按钮 | 全部 | 0 | 0 | - | 0 | 0 |
| 2489 | lhspc_pc_stocksMonitor_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_弹出 | pc | 短线精灵模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2491 | lhspc_pc_stocksMonitor_funcBar_filter | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_filter | pc | 短线精灵模块 | 功能按钮 | filter | 0 | 1 | content | 0 | 0 |
| 2488 | lhspc_pc_stocksMonitor_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_插入 | pc | 短线精灵模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2497 | lhspc_pc_stocksMonitor_funcBar_monitoItem | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_监控数据项 | pc | 短线精灵模块 | 功能按钮 | 监控数据项 | 0 | 1 | content | 0 | 0 |
| 2492 | lhspc_pc_stocksMonitor_funcBar_pause | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_暂停 | pc | 短线精灵模块 | 功能按钮 | 暂停 | 0 | 0 | - | 0 | 0 |
| 2493 | lhspc_pc_stocksMonitor_funcBar_play | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_播放 | pc | 短线精灵模块 | 功能按钮 | 播放 | 0 | 0 | - | 0 | 0 |
| 2490 | lhspc_pc_stocksMonitor_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_删除 | pc | 短线精灵模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 2496 | lhspc_pc_stocksMonitor_funcBar_watchlists | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_功能按钮_自选股 | pc | 短线精灵模块 | 功能按钮 | 自选股 | 0 | 0 | - | 0 | 0 |
| 2494 | lhspc_pc_stocksMonitor_tipBar_play | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_短线精灵模块_更新提示按钮_播放 | pc | 短线精灵模块 | 更新提示按钮 | 播放 | 0 | 0 | - | 0 | 0 |
| 5945 | lhspc_pc_profile | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_简况Profile | pc | 简况Profile | - | - | 2 | 1 | tab | 0 | 0 |
| 5947 | lhspc_pc_profile_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_简况Profile_功能按钮_弹出 | pc | 简况Profile | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 5946 | lhspc_pc_profile_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_简况Profile_功能按钮_插入 | pc | 简况Profile | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 5948 | lhspc_pc_profile_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_简况Profile_功能按钮_删除 | pc | 简况Profile | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 9433 | lhspc_pc_manageFlags | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗 | pc | 管理标记弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 9438 | lhspc_pc_manageFlags_batchModify_cancelFlags | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗_批量修改_取消所有标记 | pc | 管理标记弹窗 | 批量修改 | 取消所有标记 | 0 | 0 | - | 0 | 0 |
| 9437 | lhspc_pc_manageFlags_batchModify_color | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗_批量修改_颜色 | pc | 管理标记弹窗 | 批量修改 | 颜色 | 0 | 0 | - | 0 | 0 |
| 9436 | lhspc_pc_manageFlags_batchModify_digital | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗_批量修改_数字 | pc | 管理标记弹窗 | 批量修改 | 数字 | 0 | 0 | - | 0 | 0 |
| 9435 | lhspc_pc_manageFlags_flag_color | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗_标记_颜色 | pc | 管理标记弹窗 | 标记 | 颜色 | 0 | 0 | - | 0 | 0 |
| 9434 | lhspc_pc_manageFlags_flag_digital | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_管理标记弹窗_标记_数字 | pc | 管理标记弹窗 | 标记 | 数字 | 0 | 0 | - | 0 | 0 |
| 2605 | lhspc_pc_systemSettings_autStart_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_开机自启动_关闭 | pc | 系统设置 | 开机自启动 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2604 | lhspc_pc_systemSettings_autStart_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_开机自启动_打开 | pc | 系统设置 | 开机自启动 | 打开 | 0 | 0 | - | 0 | 0 |
| 2639 | lhspc_pc_systemSettings_checkNew_checkNew | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_检查更新按钮_检查更新按钮 | pc | 系统设置 | 检查更新按钮 | 检查更新按钮 | 0 | 0 | - | 0 | 0 |
| 2616 | lhspc_pc_systemSettings_cycScrol_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_循环翻页_关闭 | pc | 系统设置 | 循环翻页 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2615 | lhspc_pc_systemSettings_cycScrol_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_循环翻页_打开 | pc | 系统设置 | 循环翻页 | 打开 | 0 | 0 | - | 0 | 0 |
| 2640 | lhspc_pc_systemSettings_funcBar_reset | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_功能按钮_重置 | pc | 系统设置 | 功能按钮 | 重置 | 0 | 0 | - | 0 | 0 |
| 2622 | lhspc_pc_systemSettings_hideShrt_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_快捷键隐藏客户端_关闭 | pc | 系统设置 | 快捷键隐藏客户端 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2621 | lhspc_pc_systemSettings_hideShrt_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_快捷键隐藏客户端_打开 | pc | 系统设置 | 快捷键隐藏客户端 | 打开 | 0 | 0 | - | 0 | 0 |
| 4639 | lhspc_pc_systemSettings_languageSet_chinese | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_语言选择_中文 | pc | 系统设置 | 语言选择 | 中文 | 0 | 0 | - | 0 | 0 |
| 4638 | lhspc_pc_systemSettings_languageSet_english | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_语言选择_英文 | pc | 系统设置 | 语言选择 | 英文 | 0 | 0 | - | 0 | 0 |
| 5587 | lhspc_pc_systemSettings_languageSet_french | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_语言选择_法语 | pc | 系统设置 | 语言选择 | 法语 | 0 | 0 | - | 0 | 0 |
| 5586 | lhspc_pc_systemSettings_languageSet_german | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_语言选择_德语 | pc | 系统设置 | 语言选择 | 德语 | 0 | 0 | - | 0 | 0 |
| 5585 | lhspc_pc_systemSettings_languageSet_spanish | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_语言选择_西班牙语 | pc | 系统设置 | 语言选择 | 西班牙语 | 0 | 0 | - | 0 | 0 |
| 2611 | lhspc_pc_systemSettings_listScro_type | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_列表滚动_类型 | pc | 系统设置 | 列表滚动 | 类型 | 0 | 1 | content | 0 | 0 |
| 2607 | lhspc_pc_systemSettings_miniHide_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_最小化到托盘_关闭 | pc | 系统设置 | 最小化到托盘 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2606 | lhspc_pc_systemSettings_miniHide_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_最小化到托盘_打开 | pc | 系统设置 | 最小化到托盘 | 打开 | 0 | 0 | - | 0 | 0 |
| 2638 | lhspc_pc_systemSettings_noNotify_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_不再提示_关闭 | pc | 系统设置 | 不再提示 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2637 | lhspc_pc_systemSettings_noNotify_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_不再提示_打开 | pc | 系统设置 | 不再提示 | 打开 | 0 | 0 | - | 0 | 0 |
| 6524 | lhspc_pc_systemSettings_pin_change | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_PIN_change | pc | 系统设置 | PIN | change | 0 | 0 | - | 0 | 0 |
| 6523 | lhspc_pc_systemSettings_push_close | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_提醒好友_关闭 | pc | 系统设置 | 提醒好友 | 关闭 | 0 | 0 | - | 0 | 0 |
| 6522 | lhspc_pc_systemSettings_push_open | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_提醒好友_打开 | pc | 系统设置 | 提醒好友 | 打开 | 0 | 0 | - | 0 | 0 |
| 2614 | lhspc_pc_systemSettings_stkPlace_type | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_系统设置_新增股票位置_类型 | pc | 系统设置 | 新增股票位置 | 类型 | 0 | 1 | content | 0 | 0 |
| 1094 | lhspc_pc_operaAnalys | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_经营分析模块 | pc | 经营分析模块 | - | - | 2 | 2 | stock, mkt | 0 | 0 |
| 2269 | lhspc_pc_operaAnalys_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_经营分析模块_功能按钮_弹出 | pc | 经营分析模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2268 | lhspc_pc_operaAnalys_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_经营分析模块_功能按钮_插入 | pc | 经营分析模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2270 | lhspc_pc_operaAnalys_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_经营分析模块_功能按钮_删除 | pc | 经营分析模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 2175 | lhspc_pc_customTools_allTools_toolName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_自定义工具箱页面_所有组件工具_组件工具名称 | pc | 自定义工具箱页面 | 所有组件工具 | 组件工具名称 | 0 | 1 | content | 0 | 0 |
| 2181 | lhspc_pc_customTools_pageTop_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_自定义工具箱页面_页面顶部_关闭 | pc | 自定义工具箱页面 | 页面顶部 | 关闭 | 0 | 0 | - | 0 | 0 |
| 2174 | lhspc_pc_customTools_secClass_catName | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_自定义工具箱页面_二级分类_分类名称 | pc | 自定义工具箱页面 | 二级分类 | 分类名称 | 0 | 1 | content | 0 | 0 |
| 2173 | lhspc_pc_custom_blankPag_addWidgets | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_自定义页面_空页面_组件工具箱 | pc | 自定义页面 | 空页面 | 组件工具箱 | 0 | 0 | - | 0 | 0 |
| 4044 | lhspc_pc_custom_launchPage_createOwn | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_自定义页面_自定义页面模板选择_自定义创建 | pc | 自定义页面 | 自定义页面模板选择 | 自定义创建 | 0 | 0 | - | 0 | 0 |
| 4045 | lhspc_pc_custom_launchPage_template | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_自定义页面_自定义页面模板选择_模版 | pc | 自定义页面 | 自定义页面模板选择 | 模版 | 0 | 1 | content | 0 | 0 |
| 4848 | lhspc_pc_Watchlist_Watchlists_mywatchlist | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_自选列表_自选列表_我的自选股 | pc | 自选列表 | 自选列表 | 我的自选股 | 2 | 0 | - | 3 | 3 |
| 4889 | lhspc_pc_Watchlist_mywatchlist_deleteWat | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_自选列表_我的自选股_删除自选 | pc | 自选列表 | 我的自选股 | 删除自选 | 0 | 0 | - | 0 | 0 |
| 4849 | lhspc_pc_Watchlist_mywatchlist_openchart | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_自选列表_我的自选股_打开行情 | pc | 自选列表 | 我的自选股 | 打开行情 | 7 | 0 | - | 0 | 0 |
| 784 | lhspc_pc_wtclists | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表 | pc | 行情列表 | - | - | 2 | 1 | tab | 0 | 0 |
| 893 | lhspc_pc_wtclists_funcBar_addList | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_功能按钮_addList | pc | 行情列表 | 功能按钮 | addList | 0 | 0 | - | 0 | 0 |
| 894 | lhspc_pc_wtclists_funcBar_editWatch | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_功能按钮_板块/列表编辑 | pc | 行情列表 | 功能按钮 | 板块/列表编辑 | 0 | 0 | - | 0 | 0 |
| 1104 | lhspc_pc_wtclists_funcBar_multiLists | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_功能按钮_板块同列 | pc | 行情列表 | 功能按钮 | 板块同列 | 0 | 1 | switch | 0 | 0 |
| 1103 | lhspc_pc_wtclists_funcBar_stkColumn | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_功能按钮_多股同列 | pc | 行情列表 | 功能按钮 | 多股同列 | 0 | 1 | switch | 0 | 0 |
| 6727 | lhspc_pc_wtclists_metrics_delete | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_表头项区域_删除 | pc | 行情列表 | 表头项区域 | 删除 | 0 | 0 | - | 0 | 0 |
| 6729 | lhspc_pc_wtclists_metrics_editMetrics | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_表头项区域_编辑表头项 | pc | 行情列表 | 表头项区域 | 编辑表头项 | 0 | 0 | - | 0 | 0 |
| 6728 | lhspc_pc_wtclists_metrics_reset | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_表头项区域_重置 | pc | 行情列表 | 表头项区域 | 重置 | 0 | 0 | - | 0 | 0 |
| 6726 | lhspc_pc_wtclists_metrics_switchPlan | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_表头项区域_切换方案 | pc | 行情列表 | 表头项区域 | 切换方案 | 0 | 0 | - | 0 | 0 |
| 900 | lhspc_pc_wtclists_rigtMenu_addWatch | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_右键菜单_加自选 | pc | 行情列表 | 右键菜单 | 加自选 | 0 | 0 | - | 0 | 0 |
| 902 | lhspc_pc_wtclists_rigtMenu_bottom | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_右键菜单_底部 | pc | 行情列表 | 右键菜单 | 底部 | 0 | 0 | - | 0 | 0 |
| 9440 | lhspc_pc_wtclists_rigtMenu_cancelFlags | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_右键菜单_取消所有标记 | pc | 行情列表 | 右键菜单 | 取消所有标记 | 0 | 0 | - | 0 | 0 |
| 899 | lhspc_pc_wtclists_rigtMenu_delete | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_右键菜单_删除 | pc | 行情列表 | 右键菜单 | 删除 | 0 | 0 | - | 0 | 0 |
| 9439 | lhspc_pc_wtclists_rigtMenu_flag | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_右键菜单_标记（flag） | pc | 行情列表 | 右键菜单 | 标记（flag） | 0 | 1 | content | 0 | 0 |
| 9441 | lhspc_pc_wtclists_rigtMenu_manageFlags | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_右键菜单_管理标记 | pc | 行情列表 | 右键菜单 | 管理标记 | 0 | 0 | - | 0 | 0 |
| 901 | lhspc_pc_wtclists_rigtMenu_top | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_右键菜单_顶部 | pc | 行情列表 | 右键菜单 | 顶部 | 0 | 0 | - | 0 | 0 |
| 9443 | lhspc_pc_wtclists_setting_sortColor | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_设置_按颜色标记排序 | pc | 行情列表 | 设置 | 按颜色标记排序 | 0 | 0 | - | 0 | 0 |
| 9442 | lhspc_pc_wtclists_setting_sortDigital | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情列表_设置_按数字排序 | pc | 行情列表 | 设置 | 按数字排序 | 0 | 0 | - | 0 | 0 |
| 897 | lhspc_pc_wtclists_stoList_addStock | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_股票列表（stockList）_addStock | pc | 行情列表 | 股票列表（stockList） | addStock | 0 | 0 | - | 0 | 0 |
| 898 | lhspc_pc_wtclists_stoList_listItems | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_行情列表_股票列表（stockList）_表头编辑 | pc | 行情列表 | 股票列表（stockList） | 表头编辑 | 2 | 0 | - | 0 | 0 |
| 4652 | lhspc_pc_marketMovers | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单 | pc | 行情榜单 | - | - | 2 | 1 | tab | 0 | 0 |
| 4688 | lhspc_pc_marketMovers_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_功能按钮_弹出 | pc | 行情榜单 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 4687 | lhspc_pc_marketMovers_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_功能按钮_插入 | pc | 行情榜单 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 4689 | lhspc_pc_marketMovers_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_功能按钮_删除 | pc | 行情榜单 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 4663 | lhspc_pc_marketMovers_rangeBox_range | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_排序浮框_排序方式 | pc | 行情榜单 | 排序浮框 | 排序方式 | 0 | 1 | content | 0 | 0 |
| 4660 | lhspc_pc_marketMovers_secClass_52Wtab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_52WHighTab | pc | 行情榜单 | 二级分类 | 52WHighTab | 0 | 0 | - | 0 | 0 |
| 4659 | lhspc_pc_marketMovers_secClass_actTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_ActiveTab | pc | 行情榜单 | 二级分类 | ActiveTab | 0 | 0 | - | 0 | 0 |
| 4657 | lhspc_pc_marketMovers_secClass_gainTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_gainersTab | pc | 行情榜单 | 二级分类 | gainersTab | 0 | 0 | - | 0 | 0 |
| 4658 | lhspc_pc_marketMovers_secClass_losTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_losersTab | pc | 行情榜单 | 二级分类 | losersTab | 0 | 0 | - | 0 | 0 |
| 4662 | lhspc_pc_marketMovers_secClass_mktcapTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_MarketcapTab | pc | 行情榜单 | 二级分类 | MarketcapTab | 0 | 0 | - | 0 | 0 |
| 4661 | lhspc_pc_marketMovers_secClass_turnTab | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_行情榜单_二级分类_TurnoverTab | pc | 行情榜单 | 二级分类 | TurnoverTab | 0 | 0 | - | 0 | 0 |
| 6722 | lhspc_pc_orderPending | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_订单排队弹窗 | pc | 订单排队弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 6723 | lhspc_pc_orderPending_funcBar_cancel | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单排队弹窗_功能按钮_取消 | pc | 订单排队弹窗 | 功能按钮 | 取消 | 0 | 0 | - | 0 | 0 |
| 1009 | lhspc_pc_orders | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单模块 | pc | 订单模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2266 | lhspc_pc_orders_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单模块_功能按钮_弹出 | pc | 订单模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2265 | lhspc_pc_orders_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单模块_功能按钮_插入 | pc | 订单模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2267 | lhspc_pc_orders_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单模块_功能按钮_删除 | pc | 订单模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6717 | lhspc_pc_orders_link_linkBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单模块_连接_连接券商 | pc | 订单模块 | 连接 | 连接券商 | 0 | 0 | - | 0 | 0 |
| 6718 | lhspc_pc_orders_login_loginBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单模块_登陆_登录券商 | pc | 订单模块 | 登陆 | 登录券商 | 0 | 0 | - | 0 | 0 |
| 6716 | lhspc_pc_orders_operation_cancel | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单模块_操作_取消 | pc | 订单模块 | 操作 | 取消 | 0 | 0 | - | 0 | 0 |
| 6715 | lhspc_pc_orders_operation_reorder | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单模块_操作_重新下单 | pc | 订单模块 | 操作 | 重新下单 | 0 | 0 | - | 0 | 0 |
| 6719 | lhspc_pc_orderSubmit | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_订单确认弹窗 | pc | 订单确认弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 6720 | lhspc_pc_orderSubmit_funcBar_confirm | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_订单确认弹窗_功能按钮_确认 | pc | 订单确认弹窗 | 功能按钮 | 确认 | 0 | 0 | - | 0 | 0 |
| 4 | lhspc_pc_orderbook | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单表（orderbook） | pc | 订单表（orderbook） | - | - | 2 | 3 | stock, mkt, tab | 0 | 0 |
| 2237 | lhspc_pc_orderbook_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单表（orderbook）_功能按钮_弹出 | pc | 订单表（orderbook） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2236 | lhspc_pc_orderbook_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单表（orderbook）_功能按钮_插入 | pc | 订单表（orderbook） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2238 | lhspc_pc_orderbook_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_订单表（orderbook）_功能按钮_删除 | pc | 订单表（orderbook） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6528 | lhspc_pc_setPin | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_设置PIN弹窗 | pc | 设置PIN弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 6033 | lhspc_pc_financials | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_财务 | pc | 财务 | - | - | 2 | 1 | tab | 0 | 0 |
| 6035 | lhspc_pc_financials_funcBar_detach | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_财务_功能按钮_弹出 | pc | 财务 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 6034 | lhspc_pc_financials_funcBar_insert | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_财务_功能按钮_插入 | pc | 财务 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 6036 | lhspc_pc_financials_funcBar_remove | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_财务_功能按钮_删除 | pc | 财务 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 1006 | lhspc_pc_secAccou | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_账户信息模块 | pc | 账户信息模块 | - | - | 2 | 1 | tab | 0 | 0 |
| 2249 | lhspc_pc_secAccou_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_账户信息模块_功能按钮_弹出 | pc | 账户信息模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2248 | lhspc_pc_secAccou_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_账户信息模块_功能按钮_插入 | pc | 账户信息模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2250 | lhspc_pc_secAccou_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_账户信息模块_功能按钮_删除 | pc | 账户信息模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6710 | lhspc_pc_secAccou_link_linkBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_账户信息模块_连接_连接券商 | pc | 账户信息模块 | 连接 | 连接券商 | 0 | 0 | - | 0 | 0 |
| 6711 | lhspc_pc_secAccou_login_loginBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_账户信息模块_登陆_登录券商 | pc | 账户信息模块 | 登陆 | 登录券商 | 0 | 0 | - | 0 | 0 |
| 1012 | lhspc_pc_secAccou_logout_logout | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_账户信息模块_登出_登出客户端 | pc | 账户信息模块 | 登出 | 登出客户端 | 0 | 0 | - | 0 | 0 |
| 6709 | lhspc_pc_secAccou_transfer_transfer | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_账户信息模块_转账_转账 | pc | 账户信息模块 | 转账 | 转账 | 0 | 0 | - | 0 | 0 |
| 1096 | lhspc_pc_balanSheet | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_资产负债表模块 | pc | 资产负债表模块 | - | - | 2 | 2 | stock, mkt | 0 | 0 |
| 2275 | lhspc_pc_balanSheet_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_资产负债表模块_功能按钮_弹出 | pc | 资产负债表模块 | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2274 | lhspc_pc_balanSheet_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_资产负债表模块_功能按钮_插入 | pc | 资产负债表模块 | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2276 | lhspc_pc_balanSheet_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_资产负债表模块_功能按钮_删除 | pc | 资产负债表模块 | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6526 | lhspc_pc_enterPin_funcBar_forgot | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_输入PIN弹窗页面_功能按钮_忘记 | pc | 输入PIN弹窗页面 | 功能按钮 | 忘记 | 0 | 0 | - | 0 | 0 |
| 6525 | lhspc_pc_enterPin_funcBar_ok | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_输入PIN弹窗页面_功能按钮_ok按钮 | pc | 输入PIN弹窗页面 | 功能按钮 | ok按钮 | 0 | 0 | - | 0 | 0 |
| 903 | lhspc_pc_minChart | 页面埋点 | PC客户端（LightHouse PC）_Ainvest PC_迷你走势图（miniChart） | pc | 迷你走势图（miniChart） | - | - | 2 | 1 | tab | 0 | 0 |
| 2243 | lhspc_pc_minChart_funcBar_detach | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_迷你走势图（miniChart）_功能按钮_弹出 | pc | 迷你走势图（miniChart） | 功能按钮 | 弹出 | 0 | 0 | - | 0 | 0 |
| 2242 | lhspc_pc_minChart_funcBar_insert | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_迷你走势图（miniChart）_功能按钮_插入 | pc | 迷你走势图（miniChart） | 功能按钮 | 插入 | 0 | 1 | tab | 0 | 0 |
| 2244 | lhspc_pc_minChart_funcBar_remove | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_迷你走势图（miniChart）_功能按钮_删除 | pc | 迷你走势图（miniChart） | 功能按钮 | 删除 | 0 | 0 | - | 0 | 0 |
| 6527 | lhspc_pc_resetPin | 页面埋点 | PC客户端（AInvestPC）_Ainvest PC_重置PIN弹窗 | pc | 重置PIN弹窗 | - | - | 2 | 0 | - | 0 | 0 |
| 2642 | lhspc_pc_hideConfirm_funcBar_cancel | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_隐藏提示弹窗_功能按钮_cancel按钮 | pc | 隐藏提示弹窗 | 功能按钮 | 取消 | 0 | 0 | - | 0 | 0 |
| 2641 | lhspc_pc_hideConfirm_funcBar_confirm | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_隐藏提示弹窗_功能按钮_确认 | pc | 隐藏提示弹窗 | 功能按钮 | 确认 | 0 | 0 | - | 0 | 0 |
| 2643 | lhspc_pc_hideConfirm_funcBar_noLonger | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_隐藏提示弹窗_功能按钮_不再提示 | pc | 隐藏提示弹窗 | 功能按钮 | 不再提示 | 0 | 0 | - | 0 | 0 |
| 5964 | lhspc_pc_mainPage_errorMessage_crash | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_错误信息_崩溃 | pc | 页面主框架 | 错误信息 | 崩溃 | 0 | 1 | content | 0 | 0 |
| 5965 | lhspc_pc_mainPage_errorMessage_loginFailed | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_错误信息_登录失败 | pc | 页面主框架 | 错误信息 | 登录失败 | 0 | 1 | content | 0 | 0 |
| 4042 | lhspc_pc_mainPage_naviBar_aime | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_导航栏（navigationBar）_AIME | pc | 页面主框架 | 导航栏（navigationBar） | AIME | 0 | 0 | - | 0 | 0 |
| 998 | lhspc_pc_mainPage_naviBar_collapse | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_收起 | pc | 页面主框架 | 导航栏（navigationBar） | 收起 | 0 | 0 | - | 0 | 0 |
| 2167 | lhspc_pc_mainPage_naviBar_customPage | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_自定义页面 | pc | 页面主框架 | 导航栏（navigationBar） | 自定义页面 | 3,0 | 0 | - | 0 | 0 |
| 997 | lhspc_pc_mainPage_naviBar_expand | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_展开 | pc | 页面主框架 | 导航栏（navigationBar） | 展开 | 0 | 0 | - | 0 | 0 |
| 1310 | lhspc_pc_mainPage_naviBar_feedback | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_意见反馈 | pc | 页面主框架 | 导航栏（navigationBar） | 意见反馈 | 0 | 0 | - | 0 | 0 |
| 4642 | lhspc_pc_mainPage_naviBar_markets | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_导航栏（navigationBar）_市场 | pc | 页面主框架 | 导航栏（navigationBar） | 市场 | 0,3 | 0 | - | 0 | 0 |
| 995 | lhspc_pc_mainPage_naviBar_stock | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_股票 | pc | 页面主框架 | 导航栏（navigationBar） | 股票 | 3,0 | 0 | - | 0 | 0 |
| 5588 | lhspc_pc_mainPage_naviBar_support | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_导航栏（navigationBar）_客服/帮助 | pc | 页面主框架 | 导航栏（navigationBar） | 客服/帮助 | 0 | 0 | - | 0 | 0 |
| 2603 | lhspc_pc_mainPage_naviBar_systemSet | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_导航栏（navigationBar）_系统设置 | pc | 页面主框架 | 导航栏（navigationBar） | 系统设置 | 0 | 0 | - | 0 | 0 |
| 996 | lhspc_pc_mainPage_naviBar_trade | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_交易 | pc | 页面主框架 | 导航栏（navigationBar） | 交易 | 3,0 | 0 | - | 0 | 0 |
| 1311 | lhspc_pc_mainPage_naviBar_update | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_更新按钮 | pc | 页面主框架 | 导航栏（navigationBar） | 更新按钮 | 0 | 0 | - | 0 | 0 |
| 994 | lhspc_pc_mainPage_naviBar_watList | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_导航栏（navigationBar）_watchList | pc | 页面主框架 | 导航栏（navigationBar） | watchList | 3,0 | 0 | - | 0 | 0 |
| 999 | lhspc_pc_mainPage_pageBot_index | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面底部_指数 | pc | 页面主框架 | 页面底部 | 指数 | 3,0 | 2 | stock, mkt | 0 | 0 |
| 6516 | lhspc_pc_mainPage_pageTop_addBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_添加券商 | pc | 页面主框架 | 页面顶部 | 添加券商 | 0 | 0 | - | 0 | 0 |
| 2170 | lhspc_pc_mainPage_pageTop_addWidgets | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_组件工具箱 | pc | 页面主框架 | 页面顶部 | 组件工具箱 | 0 | 0 | - | 0 | 0 |
| 993 | lhspc_pc_mainPage_pageTop_close | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_关闭 | pc | 页面主框架 | 页面顶部 | 关闭 | 0 | 0 | - | 0 | 0 |
| 6517 | lhspc_pc_mainPage_pageTop_deleteBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_删除券商 | pc | 页面主框架 | 页面顶部 | 删除券商 | 0 | 0 | - | 0 | 0 |
| 6515 | lhspc_pc_mainPage_pageTop_displayBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_显示券商 | pc | 页面主框架 | 页面顶部 | 显示券商 | 0 | 0 | - | 0 | 0 |
| 6514 | lhspc_pc_mainPage_pageTop_hideBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_隐藏券商 | pc | 页面主框架 | 页面顶部 | 隐藏券商 | 0 | 0 | - | 0 | 0 |
| 6512 | lhspc_pc_mainPage_pageTop_linkBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_连接券商 | pc | 页面主框架 | 页面顶部 | 连接券商 | 0 | 0 | - | 0 | 0 |
| 6513 | lhspc_pc_mainPage_pageTop_loginBrokers | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_登录券商 | pc | 页面主框架 | 页面顶部 | 登录券商 | 0 | 0 | - | 0 | 0 |
| 990 | lhspc_pc_mainPage_pageTop_logout | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_登出客户端 | pc | 页面主框架 | 页面顶部 | 登出客户端 | 0 | 0 | - | 0 | 0 |
| 992 | lhspc_pc_mainPage_pageTop_max | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_最大化客户端 | pc | 页面主框架 | 页面顶部 | 最大化客户端 | 0 | 0 | - | 0 | 0 |
| 991 | lhspc_pc_mainPage_pageTop_mini | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_最小化客户端 | pc | 页面主框架 | 页面顶部 | 最小化客户端 | 0 | 0 | - | 0 | 0 |
| 2169 | lhspc_pc_mainPage_pageTop_rigadWiget | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_右键添加组件 | pc | 页面主框架 | 页面顶部 | 右键添加组件 | 0 | 1 | tab | 0 | 0 |
| 2168 | lhspc_pc_mainPage_pageTop_rigreLyout | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_右键重置页面 | pc | 页面主框架 | 页面顶部 | 右键重置页面 | 0 | 1 | tab | 0 | 0 |
| 988 | lhspc_pc_mainPage_pageTop_search | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_搜索按钮 | pc | 页面主框架 | 页面顶部 | 搜索按钮 | 0 | 1 | searchContent | 0 | 0 |
| 989 | lhspc_pc_mainPage_pageTop_swiAccount | 元素埋点 | PC客户端（LightHouse PC）_Ainvest PC_页面主框架_页面顶部_切换账号 | pc | 页面主框架 | 页面顶部 | 切换账号 | 0 | 0 | - | 0 | 0 |
| 2953 | lhspc_pc_mainPage_pageTop_userCenter | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_页面顶部_个人中心 | pc | 页面主框架 | 页面顶部 | 个人中心 | 0 | 0 | - | 0 | 0 |
| 4454 | lhspc_pc_mainPage_requestTime_marketChange | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_请求耗时_市场状态切换 | pc | 页面主框架 | 请求耗时 | 市场状态切换 | 2 | 1 | content | 0 | 0 |
| 4455 | lhspc_pc_mainPage_requestTime_openClient | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_请求耗时_打开客户端 | pc | 页面主框架 | 请求耗时 | 打开客户端 | 2 | 1 | content | 0 | 0 |
| 2644 | lhspc_pc_mainPage_shortCut_hideShort | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_快捷键_隐藏客户端 | pc | 页面主框架 | 快捷键 | 隐藏客户端 | 0 | 1 | content | 0 | 0 |
| 5589 | lhspc_pc_mainPage_support_discord | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_客服/帮助_Discord社群 | pc | 页面主框架 | 客服/帮助 | Discord社群 | 0 | 0 | - | 0 | 0 |
| 5590 | lhspc_pc_mainPage_support_feedback | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_客服/帮助_意见反馈 | pc | 页面主框架 | 客服/帮助 | 意见反馈 | 0 | 0 | - | 0 | 0 |
| 9472 | lhspc_pc_mainPage_tradeStatus_login | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_交易状态相关_login | pc | 页面主框架 | 交易状态相关 | login | 0 | 0 | - | 0 | 0 |
| 9473 | lhspc_pc_mainPage_tradeStatus_trade | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_交易状态相关_交易 | pc | 页面主框架 | 交易状态相关 | 交易 | 0 | 0 | - | 0 | 0 |
| 5598 | lhspc_pc_mainPage_userSystem_computer | 元素埋点 | PC客户端（AInvestPC）_Ainvest PC_页面主框架_用户系统信息_电脑信息 | pc | 页面主框架 | 用户系统信息 | 电脑信息 | 8 | 1 | content | 0 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### lhspc_pc_aiReturn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_chartSettings_axisPlac_axisPlace

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Axis placement的类型，both、left、right、not displayed | string | 0 |

### lhspc_pc_chartSettings_caAxtype_axisType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Candlestick axis type的类型，Linear、Percentage、Logarithmic | string | 0 |

### lhspc_pc_chartSettings_candMode_type

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Candlestick chart mode的类型，Auto、Adaptive、Unrestricted | string | 0 |

### lhspc_pc_chartSettings_candlGap_open

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报gap数量，1~5 | string | 0 |

### lhspc_pc_chartSettings_crosline_color

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报具体色值 | string | 0 |

### lhspc_pc_chartSettings_crosline_style

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报线型类型，包括Solid、Dash、Dashdot | string | 0 |

### lhspc_pc_chartSettings_inAxtype_axisType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Axis的类型，General、Adaptive | string | 0 |

### lhspc_pc_chartSettings_intrLine_color

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报具体色值 | string | 0 |

### lhspc_pc_chartSettings_intrLine_width

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报线宽，从细到粗4个等级分别上报1、2、3、4 | string | 0 |

### lhspc_pc_chartSettings_leftAxis_axisType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Left axis的类型，Value、Percentage | string | 0 |

### lhspc_pc_chartSettings_righAxis_axisType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报Right axis的类型，Value、Percentage | string | 0 |

### lhspc_pc_chartSettings_window_open

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报window类型，General、Fixed | string | 0 |

### lhspc_pc_etfs

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab上传ETF榜单组件当前所属的tab名称 | string | 2 |

### lhspc_pc_etfs_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上报所属tab | string | 0 |

### lhspc_pc_etfs_rangeBox_range

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content字段上报对应的表名称以及选择的周期，比如Gainers+Today | string | 0 |

### lhspc_pc_chart

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |
| 市场编码 | mkt | - | int | 2 |
| 股票代码 | stock | - | int | 2 |

### lhspc_pc_chart_allDraw_drawName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_change_symbol

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 周期，包含3日、周、月度、季度、年度 | periods | - | enum | 2 |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |

### lhspc_pc_chart_chart_drawlines

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | line | - | int | 0 |

### lhspc_pc_chart_chart_indicators

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 标识点击指标（indicators）的具体名称 | string | 0 |

### lhspc_pc_chart_chart_lineStyle

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | PC画线线型 | string | 0 |

### lhspc_pc_chart_draStbar_background

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_draStbar_color

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_draStbar_fontColor

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_draStbar_fontSize

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_draStbar_style

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_draStbar_width

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_drawings_crossPerid

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |

### lhspc_pc_chart_drawings_drawName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |
| 周期，包含3日、周、月度、季度、年度 | periods | - | enum | 0 |

### lhspc_pc_chart_drawings_magnet

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |

### lhspc_pc_chart_drawings_stayDraw

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |

### lhspc_pc_chart_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将所属tab名上报至tab字段 | string | 0 |

### lhspc_pc_chart_indctors_indicaName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |
| 周期，包含3日、周、月度、季度、年度 | periods | - | enum | 0 |

### lhspc_pc_chart_interval_tsFrame

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_lineStyl_listyName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 周期，包含3日、周、月度、季度、年度 | periods | - | enum | 0 |

### lhspc_pc_chart_range_timeFrame

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhspc_pc_chart_rigtMenu_axisPlace

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报坐标轴显示类型，包括both、left、right、not displayed | string | 0 |

### lhspc_pc_chart_rigtMenu_axisType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报坐标轴类型，包括Linear、Percentage、Logarithmic | string | 0 |

### lhspc_pc_chart_search_symbol

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 在chart组件内进行股票搜索，点击或enter某一搜索结果时，上传埋点，content上报搜索的股票代码 | string | 0 |

### lhspc_pc_chart_topInfo_symbol

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |
| 周期，包含3日、周、月度、季度、年度 | periods | - | enum | 2 |

### lhspc_pc_pinescriptEditor

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 编辑器曝光时上报埋点，tab字段上报所属tab - Stocks | string | 2 |

### lhspc_pc_miniWatchlist

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_miniWatchlist_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_push_funcBar_open

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报push的标题和内容 | string | 0 |

### lhspc_pc_Stocks_Stock_indicators

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 各指标类型 | string | 0 |

### lhspc_pc_Stocks_Stock_interval

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 具体周期选项 | string | 0 |

### lhspc_pc_Stocks_Stock_linestyle

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 各线型类别 | string | 0 |

### lhspc_pc_news

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_news_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将组件插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_news_news_newsList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | - | string | 0 |

### lhspc_pc_smartMoney

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_smartMoney_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将组件插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_trade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_trade_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_tradeError

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 曝光时content字段上报后端返回的错误信息内容 | string | 2 |

### lhspc_pc_globalMovers

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab上传全球榜单组件当前所属的tab名称 | string | 2 |

### lhspc_pc_globalMovers_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上报所属tab | string | 0 |

### lhspc_pc_globalMovers_rangeBox_range

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报对应的表名称以及选择的周期，比如China+Today | string | 0 |

### lhspc_pc_filings

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_filings_filings_filingList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | - | string | 0 |

### lhspc_pc_filings_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将组件插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_keyStatistics

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记页面/模块/元素的状态 | indicatorsState | - | enum | 2 |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_keyStatistics_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入时的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_keyStatistics_keyStatistics_angle

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记页面/模块/元素的状态 | indicatorsState | - | enum | 0 |

### lhspc_pc_incomState

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |

### lhspc_pc_incomState_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_selectBrokers_funcBar_connect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击某一券商的connect按钮时，上报埋点，content字段上报券商名称 | string | 0 |

### lhspc_pc_selectBrokers_funcBar_openAccount

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击某一券商的Open Account按钮时，上报埋点，content字段上报券商名称 | string | 0 |

### lhspc_pc_marketIndex

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab上报Market Index当前所属的tab名称 | string | 2 |

### lhspc_pc_marketIndex_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上报所属tab | string | 0 |

### lhspc_pc_timeSales

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_timeSales_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_headQuotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_headQuotes_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名上报至tab字段 | string | 0 |

### lhspc_pc_position

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_position_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_advancersDecliners

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab字段上传涨跌统计组件当前所属tab名称 | string | 2 |

### lhspc_pc_advancersDecliners_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上传所属tab | string | 0 |

### lhspc_pc_trendingStocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab上传热度榜单组件当前所属的tab名称 | string | 2 |

### lhspc_pc_trendingStocks_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上报所属tab | string | 0 |

### lhspc_pc_cashFlow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |

### lhspc_pc_cashFlow_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将组件插入的tab名称上传至tab字段 | string | 2 |

### lhspc_pc_pageLogi_login_success

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上传登陆方式：Google、Email/Phone | string | 0 |

### lhspc_pc_stocksMonitor

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 组件曝光时上报埋点，同时将所属tab上报至tab字段 | string | 2 |

### lhspc_pc_stocksMonitor_funcBar_filter

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | filter有具体勾选改变时上报埋点，content上报全部已勾选的类型名称和数据项名称 | string | 0 |

### lhspc_pc_stocksMonitor_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将stocks monitor组件插入时上报埋点，tab上报插入时所属tab名称 | string | 0 |

### lhspc_pc_stocksMonitor_funcBar_monitoItem

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 有勾选项改变时上报埋点，content上报全部已勾选的监控数据项名称 | string | 0 |

### lhspc_pc_profile

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | Profile组件曝光时上报组件所在的tab名称 | string | 2 |

### lhspc_pc_profile_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | Profile组件被插入客户端时，上报所属tab名称 | string | 0 |

### lhspc_pc_systemSettings_listScro_type

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户点击切换列表滚动方式时，上报该埋点，content上报滚动方式名称Three rows、One screen | string | 0 |

### lhspc_pc_systemSettings_stkPlace_type

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击切换新增股票位置选项时上报该埋点，content上报新增股票位置类型名称Top、Bottom | string | 0 |

### lhspc_pc_operaAnalys

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |

### lhspc_pc_operaAnalys_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_customTools_allTools_toolName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报具体功能组件名称，比如Chart、Quote、Key Statistics等 | string | 0 |

### lhspc_pc_customTools_secClass_catName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报具体分类名称，比如Quotes、Trade、Stocks | string | 0 |

### lhspc_pc_custom_launchPage_template

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击自定义启动页中预设模板，content上传模板名称 | string | 0 |

### lhspc_pc_wtclists

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_wtclists_funcBar_multiLists

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |

### lhspc_pc_wtclists_funcBar_stkColumn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述开关状态：1表示开，0表示关 | switch | - | string | 0 |

### lhspc_pc_wtclists_rigtMenu_flag

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content上报digital、color字段，用于表示用户点击的是数字标记还是颜色标记 | string | 0 |

### lhspc_pc_marketMovers

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab上报行情榜单组件当前所属的tab名称 | string | 2 |

### lhspc_pc_marketMovers_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 上报所属tab | string | 0 |

### lhspc_pc_marketMovers_rangeBox_range

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content字段上报对应的表名称以及选择的周期，比如Gainers+Pre-market | string | 0 |

### lhspc_pc_orders

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_orders_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_orderbook

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_orderbook_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_financials

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | financials曝光时上报埋点 | string | 2 |

### lhspc_pc_financials_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将financials组件插入客户端时，上报埋点，并上报所属tab | string | 0 |

### lhspc_pc_secAccou

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_secAccou_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_balanSheet

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |
| 市场编码 | mkt | - | int | 2 |

### lhspc_pc_balanSheet_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将组件插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_minChart

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 2 |

### lhspc_pc_minChart_funcBar_insert

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 将插入的tab名称上传至tab字段 | string | 0 |

### lhspc_pc_mainPage_errorMessage_crash

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content记录错误信息 | string | 0 |

### lhspc_pc_mainPage_errorMessage_loginFailed

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | content记录错误信息 | string | 0 |

### lhspc_pc_mainPage_pageBot_index

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 3,0 |
| 市场编码 | mkt | - | int | 3,0 |

### lhspc_pc_mainPage_pageTop_rigadWiget

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhspc_pc_mainPage_pageTop_rigreLyout

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhspc_pc_mainPage_pageTop_search

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时用户输入的搜索内容 | searchContent | - | string | 0 |

### lhspc_pc_mainPage_requestTime_marketChange

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 市场状态切换时，content上报请求耗时数组 | string | 2 |

### lhspc_pc_mainPage_requestTime_openClient

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 打开客户端时，content上报请求耗时数组 | string | 2 |

### lhspc_pc_mainPage_shortCut_hideShort

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 使用快捷键时，content上报快捷键组合 | string | 0 |

### lhspc_pc_mainPage_userSystem_computer

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 客户端打开时上报埋点，content记录屏幕宽高，比如1920*1080 | string | 8 |
