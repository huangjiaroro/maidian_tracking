---
title: 应用 - 券商(AinvestBroker)
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - lhsbd
  - ainvest
---

# 券商(AinvestBroker)

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 16 |
| appSign | lhsbd |
| appKey | 0f6ccbe4a5 |
| creator | huangjiarong@myhexin.com |
| createTime | 2026-04-28 15:04:55 |
| topicName | spider-ainvest |
| payloadStatus | 0 |
| pageCount(snapshot) | 50 |
| trackCount(snapshot) | 385 |
| relationTrackCount | 114 |
| tracksWithActionFields | 232 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| mob | 48 | 286 |
| cot | 1 | 99 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1083 | uppage | App启动页面 | 2 | 3 |
| 1077 | ETFcenter | ETF行情中心 | 2 | 1 |
| 1079 | H5IndustryQuote | H5版板块分时 | 2 | 4 |
| 1073 | systempage | SystemPage | 0 | 2 |
| 1057 | cryptoLQ | cryptoLiteQuote | 2 | 3 |
| 1075 | myrew | myrewards | 6 | 1 |
| 1058 | newsCalendar | news日历 | 8 | 5 |
| 207 | test | test | 0 | 0 |
| 1041 | userCen | 个人中心(userCenter) | 11 | 1 |
| 1064 | livePlaceOrder | 全屏下单（实盘） | 22 | 43 |
| 1063 | ppPlaceOrder | 全屏下单（模拟） | 9 | 7 |
| 1046 | crePass | 创建密码(createPassword) | 0 | 4 |
| 1081 | marketingpage | 商品营销页 | 4 | 2 |
| 1066 | appOpen | 应用启动 | 0 | 2 |
| 1067 | oaopersonalinfo | 开户个人信息 | 13 | 15 |
| 1068 | oaoemployfinancial | 开户工作资产状态页 | 5 | 10 |
| 1069 | oaoinvestexp | 开户投资经验页 | 8 | 13 |
| 1070 | oaoagreement | 开户披露和协议 | 6 | 7 |
| 1071 | oaostatush5 | 开户状态页（H5） | 4 | 3 |
| 1047 | phoSign | 手机号登录(phoneSignin) | 2 | 4 |
| 1065 | twiWire | 推特化快讯列表页 | 6 | 4 |
| 1074 | pushnotificationbar | 推送通知栏 | 0 | 1 |
| 1061 | Search | 搜索详情页 | 12 | 3 |
| 1056 | newPass | 新密码(newPassword) | 0 | 2 |
| 1107 | newOAOH5 | 新开户H5 | 32 | 99 |
| 1054 | newPhone | 新手机号(newPhone) | 2 | 4 |
| 1055 | newEmail | 新邮箱(newEmail) | 0 | 3 |
| 1078 | IndustryTheme | 板块 | 0 | 1 |
| 1059 | paperTrade | 模拟炒股首页 | 14 | 5 |
| 1050 | welBack | 欢迎回来(welcomeBack) | 0 | 1 |
| 1049 | welcome | 欢迎页(welcome) | 0 | 1 |
| 1082 | onboard | 注册登录 | 11 | 10 |
| 1044 | signin | 登录(signin) | 2 | 4 |
| 1076 | litef10 | 简版F10 | 6 | 3 |
| 444 | bsktotalamount | 篮子交易输入总金额 | 9 | 12 |
| 443 | bskchoose | 篮子交易选择股票 | 9 | 8 |
| 1060 | pipQuotes | 股票专业分时 | 21 | 1 |
| 1043 | liQuotes | 股票简版分时（liteQuotes） | 25 | 18 |
| 1335 | customheader | 自定义表头 | 4 | 9 |
| 1336 | watchlistpage | 自选独立页 | 2 | 1 |
| 1072 | watch | 自选股页 | 23 | 1 |
| 1042 | quotes | 行情(quotes) | 21 | 9 |
| 1053 | accSecu | 账号安全(accountSecurity) | 4 | 7 |
| 1080 | accountAnalysis | 账户分析 | 2 | 6 |
| 540 | trade | 资产首页 | 22 | 21 |
| 1062 | newsDetailPage | 资讯底层页 | 20 | 10 |
| 1051 | entPass | 输入密码(enterPassword) | 0 | 4 |
| 1045 | emaSign | 邮箱登录(emailSignin) | 0 | 3 |
| 1052 | rePassSu | 重置密码成功(resetPasswordSuccess) | 0 | 2 |
| 1048 | verify | 验证码(verify) | 0 | 2 |

## 关系枢纽埋点

| trackKey | 应用 | 页面 | 区块 | 元素 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- |
| lhsbd_mob_trade_pageTop_tradeTab | 券商(AinvestBroker) | 资产首页 | 页面顶部 | 交易tab | 12 | 11 |
| lhsbd_mob_trade_position_stoList | 券商(AinvestBroker) | 资产首页 | 持仓 | stockList | 11 | 8 |
| lhsbd_mob_liQuotes | 券商(AinvestBroker) | 股票简版分时（liteQuotes） | - | - | 7 | 10 |
| lhsbd_mob_livePlaceOrder_main_adjAmount | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | 调整数额 | 5 | 9 |
| lhsbd_mob_livePlaceOrder_main_inputquantity | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | 输入份额 | 4 | 8 |
| lhsbd_cot_newOAOH5_permanentResident_pageShow | 券商(AinvestBroker) | 新开户H5 | 永久居民 | 界面展示 | 5 | 6 |
| lhsbd_mob_livePlaceOrder | 券商(AinvestBroker) | 全屏下单（实盘） | - | - | 1 | 10 |
| lhsbd_mob_Search | 券商(AinvestBroker) | 搜索详情页 | - | - | 8 | 2 |
| lhsbd_mob_livePlaceOrder_main_sell | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | sell | 8 | 2 |
| lhsbd_mob_Search_common_cancel | 券商(AinvestBroker) | 搜索详情页 | 通用页面 | 取消 | 5 | 4 |
| lhsbd_mob_livePlaceOrder_position_tab | 券商(AinvestBroker) | 全屏下单（实盘） | 持仓 | tab | 7 | 2 |
| lhsbd_cot_newOAOH5_screenertoptab_back | 券商(AinvestBroker) | 新开户H5 | 顶部tab | 返回 | 4 | 4 |
| lhsbd_cot_newOAOH5_visatype_pageShow | 券商(AinvestBroker) | 新开户H5 | 签证类型 | 界面展示 | 4 | 4 |
| lhsbd_mob_livePlaceOrder_FullOrderConfirm_confirm | 券商(AinvestBroker) | 全屏下单（实盘） | 完整下单确认框 | 确认 | 1 | 7 |
| lhsbd_mob_quotes_stock_stockTab | 券商(AinvestBroker) | 行情(quotes) | stock | stockTab | 5 | 3 |
| lhsbd_mob_trade_sumAsset_angle | 券商(AinvestBroker) | 资产首页 | 总资产 | 展开控件 | 3 | 4 |
| lhsbd_cot_newOAOH5_uploadLicense_pageShow | 券商(AinvestBroker) | 新开户H5 | 上传驾照 | 界面展示 | 3 | 3 |
| lhsbd_mob_liQuotes_interval_day | 券商(AinvestBroker) | 股票简版分时（liteQuotes） | 时段 | 当日分时 | 5 | 1 |
| lhsbd_mob_livePlaceOrder_main_buy | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | buy | 4 | 2 |
| lhsbd_mob_livePlaceOrder_main_orderType | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | 点击订单类型OrderType | 4 | 2 |
| lhsbd_mob_livePlaceOrder_orderCfm_confirm | 券商(AinvestBroker) | 全屏下单（实盘） | 闪电下单确认框 | 确认 | 1 | 5 |
| lhsbd_mob_trade_position_sell | 券商(AinvestBroker) | 资产首页 | 持仓 | sell | 5 | 1 |
| lhsbd_mob_trade_position_tab | 券商(AinvestBroker) | 资产首页 | 持仓 | tab | 4 | 2 |
| lhsbd_cot_newOAOH5_placeOfBirth_pageShow | 券商(AinvestBroker) | 新开户H5 | 出生地址 | 界面展示 | 3 | 2 |
| lhsbd_mob_liQuotes_interval_1m | 券商(AinvestBroker) | 股票简版分时（liteQuotes） | 时段 | 1月 | 3 | 2 |
| lhsbd_mob_liQuotes_interval_3m | 券商(AinvestBroker) | 股票简版分时（liteQuotes） | 时段 | 3月 | 3 | 2 |
| lhsbd_mob_livePlaceOrder_main_search | 券商(AinvestBroker) | 全屏下单（实盘） | app主体部分 | 搜索按钮 | 3 | 2 |
| lhsbd_mob_onboard_emailphone_continue | 券商(AinvestBroker) | 注册登录 | 邮箱/手机号登录页 | continue | 2 | 3 |
| lhsbd_mob_trade_position_quotes | 券商(AinvestBroker) | 资产首页 | 持仓 | 行情 | 4 | 1 |
| lhsbd_cot_newOAOH5_address_editInformation | 券商(AinvestBroker) | 新开户H5 | residentialAddress | 编辑信息 | 2 | 2 |

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9925 | lhsbd_cot_newOAOH5_Success_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_成功页_continue | cot | 新开户H5 | 成功页 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9924 | lhsbd_cot_newOAOH5_Success_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_成功页_界面展示 | cot | 新开户H5 | 成功页 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 10059 | lhsbd_cot_newOAOH5_address_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_residentialAddress_continue | cot | 新开户H5 | residentialAddress | continue | 0 | 1 | targetName | 1 | 1 |
| 9887 | lhsbd_cot_newOAOH5_address_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_residentialAddress_编辑信息 | cot | 新开户H5 | residentialAddress | 编辑信息 | 0 | 2 | targetName, name | 2 | 2 |
| 9886 | lhsbd_cot_newOAOH5_address_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_residentialAddress_界面展示 | cot | 新开户H5 | residentialAddress | 界面展示 | 2 | 1 | targetName | 2 | 2 |
| 9912 | lhsbd_cot_newOAOH5_agreement_agreementList | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_协议页面_协议列表 | cot | 新开户H5 | 协议页面 | 协议列表 | 0 | 4 | targetName, name, logmap, listRow | 0 | 0 |
| 9914 | lhsbd_cot_newOAOH5_agreement_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_协议页面_continue | cot | 新开户H5 | 协议页面 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9911 | lhsbd_cot_newOAOH5_agreement_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_协议页面_界面展示 | cot | 新开户H5 | 协议页面 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9913 | lhsbd_cot_newOAOH5_agreement_selectButton | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_协议页面_选择按钮 | cot | 新开户H5 | 协议页面 | 选择按钮 | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9929 | lhsbd_cot_newOAOH5_choosePop_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_选择弹窗_界面展示 | cot | 新开户H5 | 选择弹窗 | 界面展示 | 2,4 | 5 | targetName, name, logmap, stayLen, title | 2 | 2 |
| 9889 | lhsbd_cot_newOAOH5_citizen_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_citizenship_选择 | cot | 新开户H5 | citizenship | 选择 | 0 | 3 | targetName, name, logmap | 1 | 1 |
| 9890 | lhsbd_cot_newOAOH5_citizen_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_citizenship_continue | cot | 新开户H5 | citizenship | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9888 | lhsbd_cot_newOAOH5_citizen_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_citizenship_界面展示 | cot | 新开户H5 | citizenship | 界面展示 | 2 | 2 | targetName, logmap | 2 | 2 |
| 9905 | lhsbd_cot_newOAOH5_dependNo_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_NoOfDependents_continue | cot | 新开户H5 | NoOfDependents | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9904 | lhsbd_cot_newOAOH5_dependNo_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_NoOfDependents_编辑信息 | cot | 新开户H5 | NoOfDependents | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 9903 | lhsbd_cot_newOAOH5_dependNo_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_NoOfDependents_界面展示 | cot | 新开户H5 | NoOfDependents | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9910 | lhsbd_cot_newOAOH5_disclosure_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_声明披露_continue | cot | 新开户H5 | 声明披露 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9909 | lhsbd_cot_newOAOH5_disclosure_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_声明披露_界面展示 | cot | 新开户H5 | 声明披露 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 10031 | lhsbd_cot_newOAOH5_dueDiligence_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_尽职调查_continue | cot | 新开户H5 | 尽职调查 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10070 | lhsbd_cot_newOAOH5_dueDiligence_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_尽职调查_编辑信息 | cot | 新开户H5 | 尽职调查 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10020 | lhsbd_cot_newOAOH5_dueDiligence_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_尽职调查_界面展示 | cot | 新开户H5 | 尽职调查 | 界面展示 | 2,4 | 0 | - | 0 | 0 |
| 9920 | lhsbd_cot_newOAOH5_employinfo_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作信息_continue | cot | 新开户H5 | 工作信息 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9919 | lhsbd_cot_newOAOH5_employinfo_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作信息_编辑信息 | cot | 新开户H5 | 工作信息 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 9918 | lhsbd_cot_newOAOH5_employinfo_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作信息_界面展示 | cot | 新开户H5 | 工作信息 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9922 | lhsbd_cot_newOAOH5_employstatus_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作状态_选择 | cot | 新开户H5 | 工作状态 | 选择 | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9923 | lhsbd_cot_newOAOH5_employstatus_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作状态_continue | cot | 新开户H5 | 工作状态 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9921 | lhsbd_cot_newOAOH5_employstatus_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_工作状态_界面展示 | cot | 新开户H5 | 工作状态 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9893 | lhsbd_cot_newOAOH5_financialstatus_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入资产状况_continue | cot | 新开户H5 | 收入资产状况 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9892 | lhsbd_cot_newOAOH5_financialstatus_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入资产状况_编辑信息 | cot | 新开户H5 | 收入资产状况 | 编辑信息 | 0 | 4 | name, targetName, logmap, title | 0 | 0 |
| 9891 | lhsbd_cot_newOAOH5_financialstatus_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入资产状况_界面展示 | cot | 新开户H5 | 收入资产状况 | 界面展示 | 2 | 3 | targetName, logmap, name | 0 | 0 |
| 10060 | lhsbd_cot_newOAOH5_fundingsource_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入来源_选择 | cot | 新开户H5 | 收入来源 | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 10029 | lhsbd_cot_newOAOH5_fundingsource_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入来源_continue | cot | 新开户H5 | 收入来源 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10017 | lhsbd_cot_newOAOH5_fundingsource_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_收入来源_界面展示 | cot | 新开户H5 | 收入来源 | 界面展示 | 2,4 | 0 | - | 0 | 0 |
| 9872 | lhsbd_cot_newOAOH5_home_openWithoutID | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_新户引导首页_无ID开户 | cot | 新开户H5 | 新户引导首页 | 无ID开户 | 0 | 1 | targetName | 0 | 0 |
| 9871 | lhsbd_cot_newOAOH5_home_openaccount | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_新户引导首页_开始开户 | cot | 新开户H5 | 新户引导首页 | 开始开户 | 0 | 1 | targetName | 1 | 1 |
| 9868 | lhsbd_cot_newOAOH5_home_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_新户引导首页_界面展示 | cot | 新开户H5 | 新户引导首页 | 界面展示 | 2 | 1 | targetName | 1 | 2 |
| 9898 | lhsbd_cot_newOAOH5_horizon_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_timeHorizon_选择 | cot | 新开户H5 | timeHorizon | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 9899 | lhsbd_cot_newOAOH5_horizon_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_timeHorizon_continue | cot | 新开户H5 | timeHorizon | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9897 | lhsbd_cot_newOAOH5_horizon_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_timeHorizon_界面展示 | cot | 新开户H5 | timeHorizon | 界面展示 | 2 | 3 | targetName, name, logmap | 0 | 0 |
| 9901 | lhsbd_cot_newOAOH5_liquidiyimportance_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_流动性重要程度_选择 | cot | 新开户H5 | 流动性重要程度 | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 9902 | lhsbd_cot_newOAOH5_liquidiyimportance_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_流动性重要程度_continue | cot | 新开户H5 | 流动性重要程度 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9900 | lhsbd_cot_newOAOH5_liquidiyimportance_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_流动性重要程度_界面展示 | cot | 新开户H5 | 流动性重要程度 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9907 | lhsbd_cot_newOAOH5_marital_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_maritalStatus_选择 | cot | 新开户H5 | maritalStatus | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 9908 | lhsbd_cot_newOAOH5_marital_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_maritalStatus_continue | cot | 新开户H5 | maritalStatus | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9906 | lhsbd_cot_newOAOH5_marital_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_maritalStatus_界面展示 | cot | 新开户H5 | maritalStatus | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9916 | lhsbd_cot_newOAOH5_object_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_investmentObjective_选择 | cot | 新开户H5 | investmentObjective | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 9917 | lhsbd_cot_newOAOH5_object_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_investmentObjective_continue | cot | 新开户H5 | investmentObjective | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9915 | lhsbd_cot_newOAOH5_object_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_investmentObjective_界面展示 | cot | 新开户H5 | investmentObjective | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9882 | lhsbd_cot_newOAOH5_ocrResult_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_ocr结果_continue | cot | 新开户H5 | ocr结果 | continue | 0 | 1 | targetName | 0 | 0 |
| 9881 | lhsbd_cot_newOAOH5_ocrResult_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_ocr结果_编辑信息 | cot | 新开户H5 | ocr结果 | 编辑信息 | 0 | 2 | targetName, title | 0 | 0 |
| 9879 | lhsbd_cot_newOAOH5_ocrResult_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_ocr结果_界面展示 | cot | 新开户H5 | ocr结果 | 界面展示 | 2 | 1 | targetName | 0 | 0 |
| 9880 | lhsbd_cot_newOAOH5_ocrResult_reUpload | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_ocr结果_重新上传 | cot | 新开户H5 | ocr结果 | 重新上传 | 0 | 1 | targetName | 0 | 0 |
| 10068 | lhsbd_cot_newOAOH5_permanentResident_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_永久居民_选择 | cot | 新开户H5 | 永久居民 | 选择 | 0 | 4 | targetName, name, logmap, content | 1 | 1 |
| 10030 | lhsbd_cot_newOAOH5_permanentResident_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_永久居民_continue | cot | 新开户H5 | 永久居民 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10019 | lhsbd_cot_newOAOH5_permanentResident_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_永久居民_界面展示 | cot | 新开户H5 | 永久居民 | 界面展示 | 2,4 | 0 | - | 5 | 6 |
| 9885 | lhsbd_cot_newOAOH5_personalInformation_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_个人信息_continue | cot | 新开户H5 | 个人信息 | continue | 0 | 1 | targetName | 1 | 1 |
| 9884 | lhsbd_cot_newOAOH5_personalInformation_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_个人信息_编辑信息 | cot | 新开户H5 | 个人信息 | 编辑信息 | 0 | 2 | targetName, name | 1 | 1 |
| 9883 | lhsbd_cot_newOAOH5_personalInformation_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_个人信息_界面展示 | cot | 新开户H5 | 个人信息 | 界面展示 | 2 | 1 | targetName | 2 | 2 |
| 10066 | lhsbd_cot_newOAOH5_placeOfBirth_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_出生地址_选择 | cot | 新开户H5 | 出生地址 | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 10067 | lhsbd_cot_newOAOH5_placeOfBirth_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_出生地址_continue | cot | 新开户H5 | 出生地址 | continue | 0 | 3 | targetName, name, logmap | 1 | 1 |
| 10018 | lhsbd_cot_newOAOH5_placeOfBirth_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_出生地址_界面展示 | cot | 新开户H5 | 出生地址 | 界面展示 | 2,4 | 0 | - | 3 | 2 |
| 9927 | lhsbd_cot_newOAOH5_recallpop_bottomButton | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_挽留弹窗_底部按钮 | cot | 新开户H5 | 挽留弹窗 | 底部按钮 | 0 | 5 | targetName, name, logmap, fid, content | 0 | 0 |
| 9928 | lhsbd_cot_newOAOH5_recallpop_closebutton | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_挽留弹窗_关闭按钮 | cot | 新开户H5 | 挽留弹窗 | 关闭按钮 | 0 | 4 | targetName, name, fid, logmap | 0 | 0 |
| 9926 | lhsbd_cot_newOAOH5_recallpop_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_挽留弹窗_界面展示 | cot | 新开户H5 | 挽留弹窗 | 界面展示 | 2,4 | 5 | targetName, name, logmap, fid, stayLen | 1 | 0 |
| 9895 | lhsbd_cot_newOAOH5_risktolerance_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_风险承受能力_选择 | cot | 新开户H5 | 风险承受能力 | 选择 | 0 | 4 | targetName, name, logmap, content | 0 | 0 |
| 9896 | lhsbd_cot_newOAOH5_risktolerance_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_风险承受能力_continue | cot | 新开户H5 | 风险承受能力 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 9894 | lhsbd_cot_newOAOH5_risktolerance_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_风险承受能力_界面展示 | cot | 新开户H5 | 风险承受能力 | 界面展示 | 2 | 3 | targetName, name, logmap | 0 | 0 |
| 9869 | lhsbd_cot_newOAOH5_screenertoptab_back | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_顶部tab_返回 | cot | 新开户H5 | 顶部tab | 返回 | 0 | 2 | targetName, fid | 4 | 4 |
| 9870 | lhsbd_cot_newOAOH5_screenertoptab_quit | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_顶部tab_退出 | cot | 新开户H5 | 顶部tab | 退出 | 0 | 2 | targetName, fid | 1 | 1 |
| 10026 | lhsbd_cot_newOAOH5_ssn_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_SSN_continue | cot | 新开户H5 | SSN | continue | 0 | 3 | targetName, name, logmap | 1 | 1 |
| 10063 | lhsbd_cot_newOAOH5_ssn_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_SSN_编辑信息 | cot | 新开户H5 | SSN | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 1 | 1 |
| 10015 | lhsbd_cot_newOAOH5_ssn_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_SSN_界面展示 | cot | 新开户H5 | SSN | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 2 | 2 |
| 10024 | lhsbd_cot_newOAOH5_taxID_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_税收ID_continue | cot | 新开户H5 | 税收ID | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10061 | lhsbd_cot_newOAOH5_taxID_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_税收ID_编辑信息 | cot | 新开户H5 | 税收ID | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10013 | lhsbd_cot_newOAOH5_taxID_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_税收ID_界面展示 | cot | 新开户H5 | 税收ID | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 9875 | lhsbd_cot_newOAOH5_uploadLicense_backpage | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_反面 | cot | 新开户H5 | 上传驾照 | 反面 | 0 | 1 | targetName | 1 | 1 |
| 9877 | lhsbd_cot_newOAOH5_uploadLicense_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_continue | cot | 新开户H5 | 上传驾照 | continue | 0 | 1 | targetName | 0 | 0 |
| 9873 | lhsbd_cot_newOAOH5_uploadLicense_front | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_正面 | cot | 新开户H5 | 上传驾照 | 正面 | 0 | 1 | targetName | 1 | 1 |
| 9878 | lhsbd_cot_newOAOH5_uploadLicense_manualInput | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_手动输入 | cot | 新开户H5 | 上传驾照 | 手动输入 | 0 | 1 | targetName | 1 | 1 |
| 9874 | lhsbd_cot_newOAOH5_uploadLicense_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_界面展示 | cot | 新开户H5 | 上传驾照 | 界面展示 | 2 | 1 | targetName | 3 | 3 |
| 9876 | lhsbd_cot_newOAOH5_uploadLicense_reUpload | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_上传驾照_重新上传 | cot | 新开户H5 | 上传驾照 | 重新上传 | 0 | 2 | targetName, type | 0 | 0 |
| 10032 | lhsbd_cot_newOAOH5_uploadPassport_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_护照上传_continue | cot | 新开户H5 | 护照上传 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10069 | lhsbd_cot_newOAOH5_uploadPassport_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_护照上传_编辑信息 | cot | 新开户H5 | 护照上传 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10023 | lhsbd_cot_newOAOH5_uploadPassport_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_护照上传_界面展示 | cot | 新开户H5 | 护照上传 | 界面展示 | 2,4 | 0 | - | 2 | 2 |
| 10027 | lhsbd_cot_newOAOH5_verifyIdentity1_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认1_continue | cot | 新开户H5 | 身份确认1 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10064 | lhsbd_cot_newOAOH5_verifyIdentity1_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认1_编辑信息 | cot | 新开户H5 | 身份确认1 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10016 | lhsbd_cot_newOAOH5_verifyIdentity1_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认1_界面展示 | cot | 新开户H5 | 身份确认1 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 10028 | lhsbd_cot_newOAOH5_verifyIdentity_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认2_continue | cot | 新开户H5 | 身份确认2 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10065 | lhsbd_cot_newOAOH5_verifyIdentity_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认2_编辑信息 | cot | 新开户H5 | 身份确认2 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10022 | lhsbd_cot_newOAOH5_verifyIdentity_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_身份确认2_界面展示 | cot | 新开户H5 | 身份确认2 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 10012 | lhsbd_cot_newOAOH5_visaexpire_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证到期日_continue | cot | 新开户H5 | 签证到期日 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10011 | lhsbd_cot_newOAOH5_visaexpire_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证到期日_编辑信息 | cot | 新开户H5 | 签证到期日 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10010 | lhsbd_cot_newOAOH5_visaexpire_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证到期日_界面展示 | cot | 新开户H5 | 签证到期日 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 2 | 2 |
| 10008 | lhsbd_cot_newOAOH5_visatype_choose | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证类型_选择 | cot | 新开户H5 | 签证类型 | 选择 | 0 | 4 | targetName, name, logmap, content | 1 | 1 |
| 10009 | lhsbd_cot_newOAOH5_visatype_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证类型_continue | cot | 新开户H5 | 签证类型 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10007 | lhsbd_cot_newOAOH5_visatype_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_签证类型_界面展示 | cot | 新开户H5 | 签证类型 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 4 | 4 |
| 10025 | lhsbd_cot_newOAOH5_visaupload_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_Visa上传页_continue | cot | 新开户H5 | Visa上传页 | continue | 0 | 3 | targetName, name, logmap | 0 | 0 |
| 10062 | lhsbd_cot_newOAOH5_visaupload_editInformation | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_Visa上传页_编辑信息 | cot | 新开户H5 | Visa上传页 | 编辑信息 | 0 | 4 | targetName, name, logmap, title | 0 | 0 |
| 10014 | lhsbd_cot_newOAOH5_visaupload_pageShow | 元素埋点 | 券商(AinvestBroker)_Ainvest Brokers_新开户H5_Visa上传页_界面展示 | cot | 新开户H5 | Visa上传页 | 界面展示 | 2,4 | 4 | targetName, name, logmap, stayLen | 0 | 0 |
| 13085 | lhsbd_mob_uppage_frontbackswitch_enterback | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_App启动页面_前后台切换_进入后台 | mob | App启动页面 | 前后台切换 | 进入后台 | 5 | 4 | logmap, country, language, progId | 0 | 0 |
| 13084 | lhsbd_mob_uppage_frontbackswitch_enterfront | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_App启动页面_前后台切换_进入前台 | mob | App启动页面 | 前后台切换 | 进入前台 | 5 | 4 | logmap, language, country, progId | 0 | 0 |
| 9369 | lhsbd_mob_uppage_page_Start | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_App启动页面_页面_启动 | mob | App启动页面 | 页面 | 启动 | 8 | 4 | logmap, progId, language, country | 0 | 3 |
| 9333 | lhsbd_mob_ETFcenter | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_ETF行情中心 | mob | ETF行情中心 | - | - | 2 | 0 | - | 0 | 0 |
| 9346 | lhsbd_mob_H5IndustryQuote | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_H5版板块分时 | mob | H5版板块分时 | - | - | 2 | 1 | content | 0 | 0 |
| 9347 | lhsbd_mob_H5IndustryQuote_chart_LineHover | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_H5版板块分时_K线主图（chart）_行情组件浮层 | mob | H5版板块分时 | K线主图（chart） | 行情组件浮层 | 3 | 0 | - | 0 | 0 |
| 9349 | lhsbd_mob_H5IndustryQuote_chart_linestyle | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_H5版板块分时_K线主图（chart）_线型 | mob | H5版板块分时 | K线主图（chart） | 线型 | 0 | 1 | content | 0 | 0 |
| 9348 | lhsbd_mob_H5IndustryQuote_chart_timearea | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_H5版板块分时_K线主图（chart）_时间周期 | mob | H5版板块分时 | K线主图（chart） | 时间周期 | 0 | 1 | content | 0 | 0 |
| 9328 | lhsbd_mob_systempage_systemnotification_turnoff | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_SystemPage_systemnotification_turnoff | mob | SystemPage | systemnotification | turnoff | 2 | 0 | - | 0 | 0 |
| 9327 | lhsbd_mob_systempage_systemnotification_turnon | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_SystemPage_systemnotification_turnon | mob | SystemPage | systemnotification | turnon | 2 | 0 | - | 0 | 0 |
| 9175 | lhsbd_mob_cryptoLQ | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_cryptoLiteQuote | mob | cryptoLiteQuote | - | - | 2 | 1 | symbol | 0 | 0 |
| 9177 | lhsbd_mob_cryptoLQ_index_kLine | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_cryptoLiteQuote_指标区域_k线 | mob | cryptoLiteQuote | 指标区域 | k线 | 0 | 0 | - | 0 | 0 |
| 9176 | lhsbd_mob_cryptoLQ_index_tsDim | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_cryptoLiteQuote_指标区域_时间维度选择列表 | mob | cryptoLiteQuote | 指标区域 | 时间维度选择 | 0 | 1 | tab | 0 | 0 |
| 9330 | lhsbd_mob_myrew_rewtab_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_myrewards_rewardstab_tab | mob | myrewards | rewardstab | tab | 0,2 | 1 | type | 0 | 0 |
| 9185 | lhsbd_mob_newsCalendar | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_news日历 | mob | news日历 | - | - | 2,1 | 0 | - | 0 | 0 |
| 9201 | lhsbd_mob_newsCalendar_calDate_date | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_news日历_日历切换视图_日历 | mob | news日历 | 日历切换视图 | 日历 | 0 | 1 | dateTime | 0 | 0 |
| 9204 | lhsbd_mob_newsCalendar_calEar_calQuote | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_news日历_日历财报_日历行情标签 | mob | news日历 | 日历财报 | 日历行情标签 | 0 | 1 | stock | 0 | 0 |
| 9202 | lhsbd_mob_newsCalendar_calTab_featured | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_news日历_日历板块_日历焦点板块 | mob | news日历 | 日历板块 | 日历焦点板块 | 0 | 0 | - | 0 | 0 |
| 9203 | lhsbd_mob_newsCalendar_calTab_splits | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_news日历_日历板块_日历拆合股板块 | mob | news日历 | 日历板块 | 日历拆合股板块 | 0 | 0 | - | 0 | 0 |
| 9132 | lhsbd_mob_userCen_funcList_helpFeed | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_个人中心(userCenter)_functionList_helpAndFeedback | mob | 个人中心(userCenter) | functionList | helpAndFeedback | 0 | 1 | state | 0 | 0 |
| 9260 | lhsbd_mob_livePlaceOrder | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘） | mob | 全屏下单（实盘） | - | - | 2 | 2 | stock, tab | 1 | 10 |
| 9270 | lhsbd_mob_livePlaceOrder_FullOrderConfirm_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_完整下单确认框_取消 | mob | 全屏下单（实盘） | 完整下单确认框 | 取消 | 0 | 1 | stock | 0 | 0 |
| 9271 | lhsbd_mob_livePlaceOrder_FullOrderConfirm_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_完整下单确认框_确认 | mob | 全屏下单（实盘） | 完整下单确认框 | 确认 | 0 | 1 | stock | 1 | 7 |
| 9289 | lhsbd_mob_livePlaceOrder_FullOrderConfirm_orderCfm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_完整下单确认框_订单确认框 | mob | 全屏下单（实盘） | 完整下单确认框 | 订单确认框 | 2 | 1 | stock | 3 | 1 |
| 9252 | lhsbd_mob_livePlaceOrder_cnlCfm_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_撤单确认框_确认 | mob | 全屏下单（实盘） | 撤单确认框 | 确认 | 0 | 0 | - | 0 | 0 |
| 9342 | lhsbd_mob_livePlaceOrder_deal_ask1pricefilling | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_盘口_卖一价填充 | mob | 全屏下单（实盘） | 盘口 | 卖一价填充 | 0 | 0 | - | 0 | 0 |
| 9341 | lhsbd_mob_livePlaceOrder_deal_bid1pricefilling | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_盘口_买一价填充 | mob | 全屏下单（实盘） | 盘口 | 买一价填充 | 0 | 0 | - | 0 | 0 |
| 9230 | lhsbd_mob_livePlaceOrder_main_adjAmount | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_调整数额 | mob | 全屏下单（实盘） | app主体部分 | 调整数额 | 0 | 4 | stock, tab, type, mode | 5 | 9 |
| 9245 | lhsbd_mob_livePlaceOrder_main_adjPrice | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_调整价格AdjustPrice | mob | 全屏下单（实盘） | app主体部分 | 调整价格AdjustPrice | 0 | 4 | stock, type, mode, tab | 1 | 3 |
| 9232 | lhsbd_mob_livePlaceOrder_main_buy | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_buy | mob | 全屏下单（实盘） | app主体部分 | buy | 0 | 4 | stock, tab, type, mode | 4 | 2 |
| 9234 | lhsbd_mob_livePlaceOrder_main_buytab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_buytab | mob | 全屏下单（实盘） | app主体部分 | buytab | 0 | 1 | stock | 0 | 0 |
| 9262 | lhsbd_mob_livePlaceOrder_main_inputquantity | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_输入份额 | mob | 全屏下单（实盘） | app主体部分 | 输入份额 | 0 | 5 | stock, tab, type, mode, value | 4 | 8 |
| 9229 | lhsbd_mob_livePlaceOrder_main_kbdecimal | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_键盘小数点 | mob | 全屏下单（实盘） | app主体部分 | 键盘小数点 | 0 | 4 | tab, type, stock, mode | 1 | 1 |
| 9237 | lhsbd_mob_livePlaceOrder_main_orderCfm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_订单确认框 | mob | 全屏下单（实盘） | app主体部分 | 订单确认框 | 2 | 4 | stock, tab, type, mode | 2 | 1 |
| 9233 | lhsbd_mob_livePlaceOrder_main_orderMode | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_切换下单模式 | mob | 全屏下单（实盘） | app主体部分 | 切换下单模式 | 0 | 4 | stock, tab, type, mode | 1 | 2 |
| 9228 | lhsbd_mob_livePlaceOrder_main_orderType | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_点击订单类型OrderType | mob | 全屏下单（实盘） | app主体部分 | 点击订单类型OrderType | 0 | 3 | tab, stock, type | 4 | 2 |
| 9236 | lhsbd_mob_livePlaceOrder_main_qckAmount | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_快捷仓位 | mob | 全屏下单（实盘） | app主体部分 | 快捷仓位 | 0 | 5 | stock, tab, type, content, mode | 1 | 2 |
| 9221 | lhsbd_mob_livePlaceOrder_main_search | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_搜索按钮 | mob | 全屏下单（实盘） | app主体部分 | 搜索按钮 | 0 | 1 | tab | 3 | 2 |
| 9231 | lhsbd_mob_livePlaceOrder_main_sell | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_sell | mob | 全屏下单（实盘） | app主体部分 | sell | 0 | 4 | stock, tab, type, mode | 8 | 2 |
| 9235 | lhsbd_mob_livePlaceOrder_main_selltab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_selltab | mob | 全屏下单（实盘） | app主体部分 | selltab | 0 | 1 | stock | 0 | 0 |
| 9244 | lhsbd_mob_livePlaceOrder_main_tradinghoursselect | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_app主体部分_交易时间选择 | mob | 全屏下单（实盘） | app主体部分 | 交易时间选择 | 0 | 4 | stock, tab, type, mode | 1 | 2 |
| 9268 | lhsbd_mob_livePlaceOrder_modify_ModifyCfm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_改单_确认改单 | mob | 全屏下单（实盘） | 改单 | 确认改单 | 0 | 1 | stock | 0 | 0 |
| 9269 | lhsbd_mob_livePlaceOrder_modify_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_改单_取消 | mob | 全屏下单（实盘） | 改单 | 取消 | 0 | 1 | stock | 0 | 0 |
| 9239 | lhsbd_mob_livePlaceOrder_orderCfm_cancel | 元素埋点 | 券商(AinvestBroker)_闪电下单确认框 | mob | 全屏下单（实盘） | 闪电下单确认框 | 取消 | 0 | 4 | stock, tab, type, mode | 0 | 0 |
| 9238 | lhsbd_mob_livePlaceOrder_orderCfm_confirm | 元素埋点 | 券商(AinvestBroker)_闪电下单确认框 | mob | 全屏下单（实盘） | 闪电下单确认框 | 确认 | 0 | 4 | stock, tab, type, mode | 1 | 5 |
| 9243 | lhsbd_mob_livePlaceOrder_orderType_limitOdr | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_订单类型_限价单 | mob | 全屏下单（实盘） | 订单类型 | 限价单 | 0 | 4 | stock, tab, type, mode | 0 | 0 |
| 9242 | lhsbd_mob_livePlaceOrder_orderType_marketOdr | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_订单类型_市价单 | mob | 全屏下单（实盘） | 订单类型 | 市价单 | 0 | 4 | stock, tab, type, mode | 1 | 3 |
| 9267 | lhsbd_mob_livePlaceOrder_ordercancelCfm_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_单笔撤单确认框_确认 | mob | 全屏下单（实盘） | 单笔撤单确认框 | 确认 | 0 | 1 | stock | 1 | 1 |
| 9223 | lhsbd_mob_livePlaceOrder_position_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_关闭 | mob | 全屏下单（实盘） | 持仓 | 关闭 | 0 | 1 | stock | 0 | 0 |
| 9226 | lhsbd_mob_livePlaceOrder_position_detail | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_详情 | mob | 全屏下单（实盘） | 持仓 | 详情 | 0 | 1 | stock | 0 | 0 |
| 9222 | lhsbd_mob_livePlaceOrder_position_quotes | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_行情 | mob | 全屏下单（实盘） | 持仓 | 行情 | 0 | 1 | stock | 0 | 0 |
| 9224 | lhsbd_mob_livePlaceOrder_position_sell | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_sell | mob | 全屏下单（实盘） | 持仓 | sell | 0 | 1 | stock | 0 | 0 |
| 9259 | lhsbd_mob_livePlaceOrder_position_sort | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_顺序调整 | mob | 全屏下单（实盘） | 持仓 | 顺序调整 | 0 | 1 | order | 0 | 1 |
| 9225 | lhsbd_mob_livePlaceOrder_position_stoList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_stockList | mob | 全屏下单（实盘） | 持仓 | stockList | 0 | 1 | stock | 0 | 0 |
| 9227 | lhsbd_mob_livePlaceOrder_position_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_持仓_tab | mob | 全屏下单（实盘） | 持仓 | tab | 0 | 0 | - | 7 | 2 |
| 9261 | lhsbd_mob_livePlaceOrder_prompt_notextended | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_提示框_仅允许盘中时段提示 | mob | 全屏下单（实盘） | 提示框 | 仅允许盘中时段提示 | 0 | 1 | stock | 1 | 1 |
| 9272 | lhsbd_mob_livePlaceOrder_selecttradinghours_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_选择交易时段_取消 | mob | 全屏下单（实盘） | 选择交易时段 | 取消 | 0 | 3 | stock, mode, tab | 0 | 0 |
| 9273 | lhsbd_mob_livePlaceOrder_selecttradinghours_extendedhours | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_选择交易时段_含额外时段 | mob | 全屏下单（实盘） | 选择交易时段 | 含额外时段 | 0 | 3 | stock, mode, tab | 1 | 1 |
| 9263 | lhsbd_mob_livePlaceOrder_todayorder_Modify | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_当日订单_改单 | mob | 全屏下单（实盘） | 当日订单 | 改单 | 0 | 0 | - | 0 | 0 |
| 9264 | lhsbd_mob_livePlaceOrder_todayorder_cancelorder | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_当日订单_撤单 | mob | 全屏下单（实盘） | 当日订单 | 撤单 | 0 | 0 | - | 1 | 1 |
| 9250 | lhsbd_mob_livePlaceOrder_todayorder_columns | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_当日订单_列表 | mob | 全屏下单（实盘） | 当日订单 | 列表 | 0 | 0 | - | 1 | 1 |
| 9266 | lhsbd_mob_livePlaceOrder_todayorder_ordercancelCfm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_当日订单_单笔撤单确认框 | mob | 全屏下单（实盘） | 当日订单 | 单笔撤单确认框 | 0 | 2 | stock, symbol | 1 | 1 |
| 9265 | lhsbd_mob_livePlaceOrder_todayorder_quotes | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（实盘）_当日订单_行情 | mob | 全屏下单（实盘） | 当日订单 | 行情 | 0 | 0 | - | 2 | 1 |
| 9220 | lhsbd_mob_ppPlaceOrder | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟） | mob | 全屏下单（模拟） | - | - | 2 | 5 | stock | 0 | 0 |
| 9240 | lhsbd_mob_ppPlaceOrder_main_orderCfm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_app主体部分_订单确认框 | mob | 全屏下单（模拟） | app主体部分 | 订单确认框 | 2 | 4 | stock, tab, type, mode | 0 | 0 |
| 9241 | lhsbd_mob_ppPlaceOrder_orderCfm_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_闪电下单确认框_确认 | mob | 全屏下单（模拟） | 闪电下单确认框 | 确认 | 0 | 4 | stock | 0 | 0 |
| 9251 | lhsbd_mob_ppPlaceOrder_order_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_orderBook_tab | mob | 全屏下单（模拟） | orderBook | tab | 0 | 0 | - | 0 | 0 |
| 9217 | lhsbd_mob_ppPlaceOrder_position_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_持仓_关闭 | mob | 全屏下单（模拟） | 持仓 | 关闭 | 0 | 1 | stock | 0 | 0 |
| 9218 | lhsbd_mob_ppPlaceOrder_position_stoList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_持仓_stockList | mob | 全屏下单（模拟） | 持仓 | stockList | 0 | 1 | stock | 0 | 0 |
| 9219 | lhsbd_mob_ppPlaceOrder_position_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_全屏下单（模拟）_持仓_tab | mob | 全屏下单（模拟） | 持仓 | tab | 0 | 0 | - | 0 | 0 |
| 9142 | lhsbd_mob_crePass | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_创建密码(createPassword) | mob | 创建密码(createPassword) | - | - | 2 | 0 | - | 1 | 1 |
| 9144 | lhsbd_mob_crePass_main_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_创建密码(createPassword)_app主体部分_continue | mob | 创建密码(createPassword) | app主体部分 | continue | 0 | 0 | - | 0 | 0 |
| 9143 | lhsbd_mob_crePass_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_创建密码(createPassword)_app主体部分_输入框 | mob | 创建密码(createPassword) | app主体部分 | 输入框 | 0 | 0 | - | 0 | 0 |
| 9145 | lhsbd_mob_crePass_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_创建密码(createPassword)_页面顶部_返回 | mob | 创建密码(createPassword) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 1 |
| 9357 | lhsbd_mob_marketingpage | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_商品营销页 | mob | 商品营销页 | - | - | 2 | 1 | goodsId | 0 | 0 |
| 9356 | lhsbd_mob_marketingpage_pageBot_bottom | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_商品营销页_页面底部_底部 | mob | 商品营销页 | 页面底部 | 底部 | 2 | 1 | goodsId | 0 | 0 |
| 9258 | lhsbd_mob_appOpen_app_online | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_应用启动_应用_在线 | mob | 应用启动 | 应用 | 在线 | 4 | 0 | - | 0 | 0 |
| 9257 | lhsbd_mob_appOpen_station_online | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_应用启动_主站_在线 | mob | 应用启动 | 主站 | 在线 | 4 | 0 | - | 0 | 0 |
| 9283 | lhsbd_mob_oaopersonalinfo_address_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_residentialAddress_continue | mob | 开户个人信息 | residentialAddress | continue | 0 | 0 | - | 0 | 0 |
| 9279 | lhsbd_mob_oaopersonalinfo_birthday_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页生日_continue | mob | 开户个人信息 | 个人信息页生日 | continue | 0 | 0 | - | 0 | 0 |
| 9278 | lhsbd_mob_oaopersonalinfo_birthday_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页生日_输入框 | mob | 开户个人信息 | 个人信息页生日 | 输入框 | 0 | 0 | - | 0 | 0 |
| 9286 | lhsbd_mob_oaopersonalinfo_citizen_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_citizenship_continue | mob | 开户个人信息 | citizenship | continue | 0 | 0 | - | 0 | 0 |
| 9277 | lhsbd_mob_oaopersonalinfo_fullname_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页名字_continue | mob | 开户个人信息 | 个人信息页名字 | continue | 0 | 0 | - | 0 | 0 |
| 9274 | lhsbd_mob_oaopersonalinfo_fullname_firstname | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页名字_名 | mob | 开户个人信息 | 个人信息页名字 | 名 | 0 | 0 | - | 0 | 0 |
| 9276 | lhsbd_mob_oaopersonalinfo_fullname_lastname | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页名字_姓 | mob | 开户个人信息 | 个人信息页名字 | 姓 | 0 | 0 | - | 0 | 0 |
| 9275 | lhsbd_mob_oaopersonalinfo_fullname_midname | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_个人信息页名字_中间名 | mob | 开户个人信息 | 个人信息页名字 | 中间名 | 0 | 0 | - | 0 | 0 |
| 9282 | lhsbd_mob_oaopersonalinfo_gender_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_gender_continue | mob | 开户个人信息 | gender | continue | 0 | 0 | - | 0 | 0 |
| 9281 | lhsbd_mob_oaopersonalinfo_gender_female | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_gender_女 | mob | 开户个人信息 | gender | 女 | 0 | 0 | - | 0 | 0 |
| 9280 | lhsbd_mob_oaopersonalinfo_gender_male | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_gender_男 | mob | 开户个人信息 | gender | 男 | 0 | 0 | - | 0 | 0 |
| 9288 | lhsbd_mob_oaopersonalinfo_marital_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_maritalStatus_continue | mob | 开户个人信息 | maritalStatus | continue | 0 | 0 | - | 0 | 0 |
| 9287 | lhsbd_mob_oaopersonalinfo_marital_single | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_maritalStatus_单身 | mob | 开户个人信息 | maritalStatus | 单身 | 0 | 0 | - | 0 | 0 |
| 9285 | lhsbd_mob_oaopersonalinfo_ssn_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_SSN_continue | mob | 开户个人信息 | SSN | continue | 0 | 0 | - | 0 | 0 |
| 9284 | lhsbd_mob_oaopersonalinfo_ssn_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户个人信息_SSN_输入框 | mob | 开户个人信息 | SSN | 输入框 | 0 | 0 | - | 0 | 0 |
| 9292 | lhsbd_mob_oaoemployfinancial_employinfo_company | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作信息_公司 | mob | 开户工作资产状态页 | 工作信息 | 公司 | 0 | 0 | - | 0 | 0 |
| 9295 | lhsbd_mob_oaoemployfinancial_employinfo_industry | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作信息_行业 | mob | 开户工作资产状态页 | 工作信息 | 行业 | 0 | 0 | - | 0 | 0 |
| 9293 | lhsbd_mob_oaoemployfinancial_employinfo_position | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作信息_岗位 | mob | 开户工作资产状态页 | 工作信息 | 岗位 | 0 | 0 | - | 0 | 0 |
| 9294 | lhsbd_mob_oaoemployfinancial_employinfo_years | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作信息_年 | mob | 开户工作资产状态页 | 工作信息 | 年 | 0 | 0 | - | 0 | 0 |
| 9291 | lhsbd_mob_oaoemployfinancial_employstatus_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作状态_continue | mob | 开户工作资产状态页 | 工作状态 | continue | 0 | 0 | - | 0 | 0 |
| 9290 | lhsbd_mob_oaoemployfinancial_employstatus_employed | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_工作状态_在职 | mob | 开户工作资产状态页 | 工作状态 | 在职 | 0 | 0 | - | 0 | 0 |
| 9296 | lhsbd_mob_oaoemployfinancial_financialstatus_annualincome | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_收入资产状况_年收入 | mob | 开户工作资产状态页 | 收入资产状况 | 年收入 | 0 | 0 | - | 0 | 0 |
| 9299 | lhsbd_mob_oaoemployfinancial_financialstatus_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_收入资产状况_continue | mob | 开户工作资产状态页 | 收入资产状况 | continue | 0 | 0 | - | 0 | 0 |
| 9297 | lhsbd_mob_oaoemployfinancial_financialstatus_liquidnetworth | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_收入资产状况_流动资产 | mob | 开户工作资产状态页 | 收入资产状况 | 流动资产 | 0 | 0 | - | 0 | 0 |
| 9298 | lhsbd_mob_oaoemployfinancial_financialstatus_totalnetworth | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户工作资产状态页_收入资产状况_总资产 | mob | 开户工作资产状态页 | 收入资产状况 | 总资产 | 0 | 0 | - | 0 | 0 |
| 9309 | lhsbd_mob_oaoinvestexp_horizon_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_timeHorizon_continue | mob | 开户投资经验页 | timeHorizon | continue | 0 | 0 | - | 0 | 0 |
| 9308 | lhsbd_mob_oaoinvestexp_horizon_short | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_timeHorizon_短 | mob | 开户投资经验页 | timeHorizon | 短 | 0 | 0 | - | 0 | 0 |
| 9301 | lhsbd_mob_oaoinvestexp_investexp_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_投资经验_continue | mob | 开户投资经验页 | 投资经验 | continue | 0 | 0 | - | 0 | 0 |
| 9300 | lhsbd_mob_oaoinvestexp_investexp_none | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_投资经验_无 | mob | 开户投资经验页 | 投资经验 | 无 | 0 | 0 | - | 0 | 0 |
| 9302 | lhsbd_mob_oaoinvestexp_investobjective_growth | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_投资目的_增长 | mob | 开户投资经验页 | 投资目的 | 增长 | 0 | 0 | - | 0 | 0 |
| 9303 | lhsbd_mob_oaoinvestexp_investobjective_income | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_投资目的_收入 | mob | 开户投资经验页 | 投资目的 | 收入 | 0 | 0 | - | 0 | 0 |
| 9304 | lhsbd_mob_oaoinvestexp_investobjective_preservation | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_投资目的_保值 | mob | 开户投资经验页 | 投资目的 | 保值 | 0 | 0 | - | 0 | 0 |
| 9312 | lhsbd_mob_oaoinvestexp_liquidiyimportance_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_流动性重要程度_continue | mob | 开户投资经验页 | 流动性重要程度 | continue | 0 | 0 | - | 0 | 0 |
| 9311 | lhsbd_mob_oaoinvestexp_liquidiyimportance_somewhat | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_流动性重要程度_一般重要 | mob | 开户投资经验页 | 流动性重要程度 | 一般重要 | 0 | 0 | - | 0 | 0 |
| 9310 | lhsbd_mob_oaoinvestexp_liquidiyimportance_very | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_流动性重要程度_非常重要 | mob | 开户投资经验页 | 流动性重要程度 | 非常重要 | 0 | 0 | - | 0 | 0 |
| 9307 | lhsbd_mob_oaoinvestexp_risktolerance_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_风险承受能力_continue | mob | 开户投资经验页 | 风险承受能力 | continue | 0 | 0 | - | 0 | 0 |
| 9305 | lhsbd_mob_oaoinvestexp_risktolerance_high | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_风险承受能力_高 | mob | 开户投资经验页 | 风险承受能力 | 高 | 0 | 0 | - | 0 | 0 |
| 9306 | lhsbd_mob_oaoinvestexp_risktolerance_medium | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户投资经验页_风险承受能力_中 | mob | 开户投资经验页 | 风险承受能力 | 中 | 0 | 0 | - | 0 | 0 |
| 9320 | lhsbd_mob_oaoagreement_agreement_check | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_协议页面_勾选 | mob | 开户披露和协议 | 协议页面 | 勾选 | 0 | 0 | - | 0 | 0 |
| 9321 | lhsbd_mob_oaoagreement_agreement_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_协议页面_continue | mob | 开户披露和协议 | 协议页面 | continue | 0 | 0 | - | 0 | 0 |
| 9315 | lhsbd_mob_oaoagreement_disclosure_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_声明披露_continue | mob | 开户披露和协议 | 声明披露 | continue | 0 | 0 | - | 0 | 0 |
| 9318 | lhsbd_mob_oaoagreement_id_backpage | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_ID上传页_反面 | mob | 开户披露和协议 | ID上传页 | 反面 | 0 | 0 | - | 0 | 0 |
| 9316 | lhsbd_mob_oaoagreement_id_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_ID上传页_关闭 | mob | 开户披露和协议 | ID上传页 | 关闭 | 0 | 0 | - | 0 | 0 |
| 9319 | lhsbd_mob_oaoagreement_id_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_ID上传页_continue | mob | 开户披露和协议 | ID上传页 | continue | 0 | 0 | - | 0 | 0 |
| 9317 | lhsbd_mob_oaoagreement_id_front | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户披露和协议_ID上传页_正面 | mob | 开户披露和协议 | ID上传页 | 正面 | 0 | 0 | - | 0 | 0 |
| 9324 | lhsbd_mob_oaostatush5_statusdetails_agreement | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户状态页（H5）_状态详情_披露协议 | mob | 开户状态页（H5） | 状态详情 | 披露协议 | 0 | 0 | - | 0 | 0 |
| 9322 | lhsbd_mob_oaostatush5_statusdetails_employfinancial | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户状态页（H5）_状态详情_工作收入 | mob | 开户状态页（H5） | 状态详情 | 工作收入 | 0 | 0 | - | 0 | 0 |
| 9323 | lhsbd_mob_oaostatush5_statusdetails_investexp | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_开户状态页（H5）_状态详情_投资经验 | mob | 开户状态页（H5） | 状态详情 | 投资经验 | 0 | 0 | - | 0 | 0 |
| 9146 | lhsbd_mob_phoSign | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_手机号登录(phoneSignin) | mob | 手机号登录(phoneSignin) | - | - | 2 | 0 | - | 0 | 0 |
| 9148 | lhsbd_mob_phoSign_main_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_手机号登录(phoneSignin)_app主体部分_continue | mob | 手机号登录(phoneSignin) | app主体部分 | continue | 0 | 0 | - | 0 | 0 |
| 9147 | lhsbd_mob_phoSign_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_手机号登录(phoneSignin)_app主体部分_输入框 | mob | 手机号登录(phoneSignin) | app主体部分 | 输入框 | 0 | 0 | - | 1 | 1 |
| 9149 | lhsbd_mob_phoSign_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_手机号登录(phoneSignin)_页面顶部_返回 | mob | 手机号登录(phoneSignin) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 1 |
| 9314 | lhsbd_mob_twiWire | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_推特化快讯列表页 | mob | 推特化快讯列表页 | - | - | 2 | 3 | ffid, tab, impsId | 0 | 2 |
| 9340 | lhsbd_mob_twiWire_noti_remind | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_推特化快讯列表页_通知_提醒 | mob | 推特化快讯列表页 | 通知 | 提醒 | 2,0 | 0 | - | 1 | 0 |
| 9255 | lhsbd_mob_twiWire_pageTop_2tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_推特化快讯列表页_页面顶部_二级tab | mob | 推特化快讯列表页 | 页面顶部 | 二级tab | 1,0 | 3 | tab, ffid, impsId | 0 | 0 |
| 9313 | lhsbd_mob_twiWire_pageTop_refresh | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_推特化快讯列表页_页面顶部_刷新 | mob | 推特化快讯列表页 | 页面顶部 | 刷新 | 1 | 0 | - | 1 | 0 |
| 9329 | lhsbd_mob_pushnotificationbar | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_推送通知栏 | mob | 推送通知栏 | - | - | 0,2 | 1 | pushId | 1 | 1 |
| 9214 | lhsbd_mob_Search | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_搜索详情页 | mob | 搜索详情页 | - | - | 2 | 0 | - | 8 | 2 |
| 9212 | lhsbd_mob_Search_common_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_搜索详情页_通用页面_cancel按钮 | mob | 搜索详情页 | 通用页面 | 取消 | 0 | 1 | searchContent | 5 | 4 |
| 9213 | lhsbd_mob_Search_common_delete | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_搜索详情页_通用页面_删除 | mob | 搜索详情页 | 通用页面 | 删除 | 0 | 1 | searchContent | 0 | 0 |
| 9173 | lhsbd_mob_newPass | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_新密码(newPassword) | mob | 新密码(newPassword) | - | - | 2 | 0 | - | 0 | 0 |
| 9174 | lhsbd_mob_newPass_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新密码(newPassword)_app主体部分_输入框 | mob | 新密码(newPassword) | app主体部分 | 输入框 | 0 | 0 | - | 0 | 0 |
| 9166 | lhsbd_mob_newPhone | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_新手机号(newPhone) | mob | 新手机号(newPhone) | - | - | 2 | 0 | - | 0 | 1 |
| 9168 | lhsbd_mob_newPhone_main_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新手机号(newPhone)_app主体部分_continue | mob | 新手机号(newPhone) | app主体部分 | continue | 0 | 0 | - | 1 | 1 |
| 9167 | lhsbd_mob_newPhone_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新手机号(newPhone)_app主体部分_输入框 | mob | 新手机号(newPhone) | app主体部分 | 输入框 | 0 | 0 | - | 1 | 1 |
| 9169 | lhsbd_mob_newPhone_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新手机号(newPhone)_页面顶部_返回 | mob | 新手机号(newPhone) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 1 |
| 9170 | lhsbd_mob_newEmail | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_新邮箱(newEmail) | mob | 新邮箱(newEmail) | - | - | 2 | 0 | - | 0 | 0 |
| 9171 | lhsbd_mob_newEmail_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新邮箱(newEmail)_app主体部分_输入框 | mob | 新邮箱(newEmail) | app主体部分 | 输入框 | 0 | 0 | - | 0 | 0 |
| 9172 | lhsbd_mob_newEmail_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_新邮箱(newEmail)_页面顶部_返回 | mob | 新邮箱(newEmail) | 页面顶部 | 返回 | 0 | 0 | - | 0 | 0 |
| 9345 | lhsbd_mob_IndustryTheme | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_板块 | mob | 板块 | - | - | 2 | 1 | tab | 0 | 0 |
| 9206 | lhsbd_mob_paperTrade_order_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_模拟炒股首页_orderBook_cancel按钮 | mob | 模拟炒股首页 | orderBook | 取消 | 0 | 1 | orderId | 0 | 0 |
| 9205 | lhsbd_mob_paperTrade_order_list | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_模拟炒股首页_orderBook_list | mob | 模拟炒股首页 | orderBook | list | 0 | 1 | orderId | 0 | 0 |
| 9247 | lhsbd_mob_paperTrade_position_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_模拟炒股首页_持仓_关闭 | mob | 模拟炒股首页 | 持仓 | 关闭 | 0 | 1 | stock | 0 | 0 |
| 9246 | lhsbd_mob_paperTrade_position_quotes | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_模拟炒股首页_持仓_行情 | mob | 模拟炒股首页 | 持仓 | 行情 | 0 | 1 | stock | 1 | 1 |
| 9248 | lhsbd_mob_paperTrade_position_stoList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_模拟炒股首页_持仓_stockList | mob | 模拟炒股首页 | 持仓 | stockList | 0 | 1 | stock | 0 | 1 |
| 9153 | lhsbd_mob_welBack | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_欢迎回来(welcomeBack) | mob | 欢迎回来(welcomeBack) | - | - | 2 | 0 | - | 0 | 0 |
| 9152 | lhsbd_mob_welcome | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_欢迎页(welcome) | mob | 欢迎页(welcome) | - | - | 2 | 0 | - | 0 | 0 |
| 9367 | lhsbd_mob_onboard_createpassword_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_创建密码_continue | mob | 注册登录 | 创建密码 | continue | 0 | 0 | - | 0 | 0 |
| 9362 | lhsbd_mob_onboard_emailphone_Phone | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_邮箱/手机号登录页_手机 | mob | 注册登录 | 邮箱/手机号登录页 | 手机 | 0 | 0 | - | 1 | 1 |
| 9363 | lhsbd_mob_onboard_emailphone_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_邮箱/手机号登录页_continue | mob | 注册登录 | 邮箱/手机号登录页 | continue | 0 | 1 | logmap | 2 | 3 |
| 9361 | lhsbd_mob_onboard_emailphone_email | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_邮箱/手机号登录页_email | mob | 注册登录 | 邮箱/手机号登录页 | email | 0 | 0 | - | 0 | 0 |
| 9359 | lhsbd_mob_onboard_homepage_AppLogin | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_首页_苹果登录 | mob | 注册登录 | 首页 | 苹果登录 | 0 | 0 | - | 0 | 0 |
| 9358 | lhsbd_mob_onboard_homepage_emaPhone | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_首页_邮箱/手机号登录 | mob | 注册登录 | 首页 | 邮箱/手机号登录 | 0 | 0 | - | 0 | 1 |
| 9360 | lhsbd_mob_onboard_homepage_googLogIn | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_首页_谷歌登录 | mob | 注册登录 | 首页 | 谷歌登录 | 0 | 0 | - | 0 | 1 |
| 9366 | lhsbd_mob_onboard_passwordlogin_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_密码登录_continue | mob | 注册登录 | 密码登录 | continue | 0 | 0 | - | 1 | 1 |
| 9365 | lhsbd_mob_onboard_passwordlogin_forgotpassword | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_密码登录_忘记密码 | mob | 注册登录 | 密码登录 | 忘记密码 | 0 | 0 | - | 0 | 0 |
| 9364 | lhsbd_mob_onboard_sms_resend | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_注册登录_验证码登录_resend | mob | 注册登录 | 验证码登录 | resend | 0 | 0 | - | 0 | 0 |
| 9135 | lhsbd_mob_signin | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_登录(signin) | mob | 登录(signin) | - | - | 2 | 1 | state | 1 | 0 |
| 9138 | lhsbd_mob_signin_main_emaPhone | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_登录(signin)_app主体部分_邮箱/手机号登录 | mob | 登录(signin) | app主体部分 | 邮箱/手机号登录 | 0 | 0 | - | 0 | 0 |
| 9137 | lhsbd_mob_signin_main_google | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_登录(signin)_app主体部分_google | mob | 登录(signin) | app主体部分 | google | 0 | 0 | - | 0 | 0 |
| 9136 | lhsbd_mob_signin_pageTop_skip | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_登录(signin)_页面顶部_skip | mob | 登录(signin) | 页面顶部 | skip | 0 | 0 | - | 0 | 0 |
| 9331 | lhsbd_mob_litef10_about_seemore | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_简版F10_about_seemore | mob | 简版F10 | about | seemore | 0 | 1 | stock | 0 | 0 |
| 9368 | lhsbd_mob_litef10_keyStatistics_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_简版F10_关键数据（keyStatistics）_曝光 | mob | 简版F10 | 关键数据（keyStatistics） | 曝光 | 2 | 1 | stock | 0 | 0 |
| 9332 | lhsbd_mob_litef10_news_newsList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_简版F10_news资讯_newsList | mob | 简版F10 | news资讯 | newsList | 0,2 | 3 | stock, listRow, impsId | 0 | 0 |
| 4850 | lhsbd_mob_bsktotalamount | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额 | mob | 篮子交易输入总金额 | - | - | 2 | 0 | - | 0 | 0 |
| 4858 | lhsbd_mob_bsktotalamount_confirm_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_确认_关闭 | mob | 篮子交易输入总金额 | 确认 | 关闭 | 0 | 1 | content | 0 | 0 |
| 4860 | lhsbd_mob_bsktotalamount_confirm_collapse | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_确认_收起 | mob | 篮子交易输入总金额 | 确认 | 收起 | 0 | 1 | content | 0 | 0 |
| 4857 | lhsbd_mob_bsktotalamount_confirm_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_确认_确认 | mob | 篮子交易输入总金额 | 确认 | 确认 | 0 | 1 | content | 0 | 0 |
| 4859 | lhsbd_mob_bsktotalamount_confirm_unfold | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_确认_全部展开 | mob | 篮子交易输入总金额 | 确认 | 全部展开 | 0 | 1 | content | 0 | 0 |
| 4852 | lhsbd_mob_bsktotalamount_inputBox_clear | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_对话输入框(inputBox)_清除记录 | mob | 篮子交易输入总金额 | 对话输入框(inputBox) | 清除记录 | 0 | 0 | - | 0 | 0 |
| 4851 | lhsbd_mob_bsktotalamount_inputBox_input | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_对话输入框(inputBox)_输入框 | mob | 篮子交易输入总金额 | 对话输入框(inputBox) | 输入框 | 0 | 0 | - | 0 | 0 |
| 4853 | lhsbd_mob_bsktotalamount_main_buy | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_app主体部分_buy | mob | 篮子交易输入总金额 | app主体部分 | buy | 0 | 0 | - | 0 | 0 |
| 4855 | lhsbd_mob_bsktotalamount_main_popUp | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_app主体部分_异常弹窗 | mob | 篮子交易输入总金额 | app主体部分 | 异常弹窗 | 2 | 1 | content | 0 | 0 |
| 4861 | lhsbd_mob_bsktotalamount_popup_Pop | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_弹窗_弹窗 | mob | 篮子交易输入总金额 | 弹窗 | 弹窗 | 2 | 1 | content | 0 | 0 |
| 4856 | lhsbd_mob_bsktotalamount_popup_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_弹窗_取消 | mob | 篮子交易输入总金额 | 弹窗 | 取消 | 0 | 1 | content | 0 | 0 |
| 4854 | lhsbd_mob_bsktotalamount_popup_deposit | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易输入总金额_弹窗_转入 | mob | 篮子交易输入总金额 | 弹窗 | 转入 | 0 | 1 | content | 0 | 0 |
| 4833 | lhsbd_mob_bskchoose | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票 | mob | 篮子交易选择股票 | - | - | 2 | 0 | - | 0 | 0 |
| 4836 | lhsbd_mob_bskchoose_main_add | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_app主体部分_添加 | mob | 篮子交易选择股票 | app主体部分 | 添加 | 0 | 1 | num | 0 | 0 |
| 4834 | lhsbd_mob_bskchoose_main_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_app主体部分_返回 | mob | 篮子交易选择股票 | app主体部分 | 返回 | 0 | 0 | - | 0 | 0 |
| 4837 | lhsbd_mob_bskchoose_main_search | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_app主体部分_搜索按钮 | mob | 篮子交易选择股票 | app主体部分 | 搜索按钮 | 0 | 0 | - | 0 | 0 |
| 4835 | lhsbd_mob_bskchoose_main_selectall | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_app主体部分_选择全部 | mob | 篮子交易选择股票 | app主体部分 | 选择全部 | 0 | 1 | state | 0 | 0 |
| 4838 | lhsbd_mob_bskchoose_search_add | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_搜索模块按钮_添加 | mob | 篮子交易选择股票 | 搜索模块按钮 | 添加 | 0 | 2 | content, num | 0 | 0 |
| 4839 | lhsbd_mob_bskchoose_search_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_搜索模块按钮_取消 | mob | 篮子交易选择股票 | 搜索模块按钮 | 取消 | 0 | 2 | content, num | 0 | 0 |
| 4840 | lhsbd_mob_bskchoose_search_empty | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_篮子交易选择股票_搜索模块按钮_empty | mob | 篮子交易选择股票 | 搜索模块按钮 | empty | 2 | 1 | content | 0 | 0 |
| 9207 | lhsbd_mob_pipQuotes_ppTrade_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_标准分时_模拟炒股浮框_cancel按钮 | mob | 股票专业分时 | 模拟炒股浮框 | 取消 | 0 | 0 | - | 0 | 0 |
| 9370 | lhsbd_mob_liQuotes | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes） | mob | 股票简版分时（liteQuotes） | - | - | 2 | 1 | ticker | 7 | 10 |
| 9208 | lhsbd_mob_liQuotes_about_area | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_about_区域 | mob | 股票简版分时（liteQuotes） | about | 区域 | 2 | 0 | - | 0 | 0 |
| 9377 | lhsbd_mob_liQuotes_interval_1d | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_盘中 | mob | 股票简版分时（liteQuotes） | 时段 | 盘中 | 0 | 1 | stock | 0 | 0 |
| 9373 | lhsbd_mob_liQuotes_interval_1m | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_1月 | mob | 股票简版分时（liteQuotes） | 时段 | 1月 | 0 | 1 | stock | 3 | 2 |
| 9372 | lhsbd_mob_liQuotes_interval_1w | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_1周区间 | mob | 股票简版分时（liteQuotes） | 时段 | 1周区间 | 0 | 1 | stock | 1 | 2 |
| 9374 | lhsbd_mob_liQuotes_interval_3m | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_3月 | mob | 股票简版分时（liteQuotes） | 时段 | 3月 | 0 | 1 | stock | 3 | 2 |
| 9380 | lhsbd_mob_liQuotes_interval_5y | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_5年 | mob | 股票简版分时（liteQuotes） | 时段 | 5年 | 0 | 1 | stock | 0 | 1 |
| 9378 | lhsbd_mob_liQuotes_interval_after | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_盘后 | mob | 股票简版分时（liteQuotes） | 时段 | 盘后 | 0 | 1 | stock | 0 | 0 |
| 9379 | lhsbd_mob_liQuotes_interval_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_cancel按钮 | mob | 股票简版分时（liteQuotes） | 时段 | 取消 | 0 | 1 | stock | 0 | 0 |
| 9371 | lhsbd_mob_liQuotes_interval_day | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_当日分时 | mob | 股票简版分时（liteQuotes） | 时段 | 当日分时 | 0,7 | 1 | stock | 5 | 1 |
| 9375 | lhsbd_mob_liQuotes_interval_lineSwitch | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_线性切换 | mob | 股票简版分时（liteQuotes） | 时段 | 线性切换 | 0 | 1 | stock | 0 | 0 |
| 9376 | lhsbd_mob_liQuotes_interval_pre | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_时段_盘前 | mob | 股票简版分时（liteQuotes） | 时段 | 盘前 | 0 | 1 | stock | 0 | 0 |
| 9209 | lhsbd_mob_liQuotes_news_area | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_news资讯_区域 | mob | 股票简版分时（liteQuotes） | news资讯 | 区域 | 2 | 0 | - | 0 | 0 |
| 9210 | lhsbd_mob_liQuotes_opinions_area | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_opinions_区域 | mob | 股票简版分时（liteQuotes） | opinions | 区域 | 2 | 0 | - | 0 | 0 |
| 9134 | lhsbd_mob_liQuotes_pageTop_optButton | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_页面顶部_自选按钮 | mob | 股票简版分时（liteQuotes） | 页面顶部 | 自选按钮 | 0 | 2 | optType, stock | 0 | 0 |
| 9382 | lhsbd_mob_liQuotes_stats_area | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_keyStats_区域 | mob | 股票简版分时（liteQuotes） | keyStats | 区域 | 2 | 0 | - | 0 | 0 |
| 9211 | lhsbd_mob_liQuotes_stockrec_area | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_PeopleAlsoWatch_区域 | mob | 股票简版分时（liteQuotes） | PeopleAlsoWatch | 区域 | 2 | 0 | - | 0 | 0 |
| 9381 | lhsbd_mob_liQuotes_wlDrawer_wlDrawer | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_股票简版分时（liteQuotes）_自选抽屉（watchlistdrawer）_自选抽屉（watchlistdrawer） | mob | 股票简版分时（liteQuotes） | 自选抽屉（watchlistdrawer） | 自选抽屉（watchlistdrawer） | 2 | 1 | stock | 0 | 0 |
| 13361 | lhsbd_mob_customheader_editpopup_Pop | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_弹窗 | mob | 自定义表头 | 编辑弹窗 | 弹窗 | 2 | 1 | targetName | 0 | 0 |
| 13366 | lhsbd_mob_customheader_editpopup_confirm | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_确认 | mob | 自定义表头 | 编辑弹窗 | 确认 | 0 | 0 | - | 0 | 0 |
| 13363 | lhsbd_mob_customheader_editpopup_deleteheader | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_表头删除 | mob | 自定义表头 | 编辑弹窗 | 表头删除 | 0 | 2 | name, itemId | 0 | 0 |
| 13365 | lhsbd_mob_customheader_editpopup_headerincrease | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_表头增加 | mob | 自定义表头 | 编辑弹窗 | 表头增加 | 0 | 3 | name, itemId, tab | 0 | 0 |
| 13364 | lhsbd_mob_customheader_editpopup_renametheheader | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_表头改名 | mob | 自定义表头 | 编辑弹窗 | 表头改名 | 0 | 2 | name, itemId | 0 | 0 |
| 13368 | lhsbd_mob_customheader_editpopup_reset | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_重置 | mob | 自定义表头 | 编辑弹窗 | 重置 | 0 | 0 | - | 0 | 0 |
| 13362 | lhsbd_mob_customheader_editpopup_sortmetric | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_表头排序 | mob | 自定义表头 | 编辑弹窗 | 表头排序 | 6 | 2 | name, itemId | 0 | 0 |
| 13369 | lhsbd_mob_customheader_editpopup_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_编辑弹窗_tab | mob | 自定义表头 | 编辑弹窗 | tab | 0 | 1 | tab | 0 | 0 |
| 13367 | lhsbd_mob_customheader_stockchart_optionalheaderedite | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自定义表头_个股chart_自选表头编辑 | mob | 自定义表头 | 个股chart | 自选表头编辑 | 0 | 0 | - | 0 | 0 |
| 13370 | lhsbd_mob_watchlistpage_Watchlists_listItems | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自选独立页_自选列表_表头编辑 | mob | 自选独立页 | 自选列表 | 表头编辑 | 0 | 0 | - | 0 | 0 |
| 9325 | lhsbd_mob_watch_pageTop_search | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_自选股页_页面顶部_搜索按钮 | mob | 自选股页 | 页面顶部 | 搜索按钮 | 0 | 0 | - | 0 | 1 |
| 9182 | lhsbd_mob_quotes_dist_today | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_distribution分布_today | mob | 行情(quotes) | distribution分布 | today | 0 | 1 | num | 0 | 0 |
| 9183 | lhsbd_mob_quotes_dist_twoWeeks | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_distribution分布_twoWeeks | mob | 行情(quotes) | distribution分布 | twoWeeks | 0 | 0 | - | 0 | 0 |
| 9133 | lhsbd_mob_quotes_etf_etfTab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_etf板块_ETFTab | mob | 行情(quotes) | etf板块 | ETFTab | 0 | 0 | - | 0 | 0 |
| 9256 | lhsbd_mob_quotes_industry_stockLabel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_行业_股票行情标签 | mob | 行情(quotes) | 行业 | 股票行情标签 | 0 | 1 | stock | 0 | 0 |
| 9181 | lhsbd_mob_quotes_monitor_index | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_monitor_指数 | mob | 行情(quotes) | monitor | 指数 | 0 | 1 | num | 0 | 0 |
| 9179 | lhsbd_mob_quotes_pageTop_search | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_页面顶部_搜索按钮 | mob | 行情(quotes) | 页面顶部 | 搜索按钮 | 0 | 0 | - | 0 | 0 |
| 9178 | lhsbd_mob_quotes_pageTop_userCenter | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_页面顶部_个人中心 | mob | 行情(quotes) | 页面顶部 | 个人中心 | 0 | 0 | - | 0 | 0 |
| 9180 | lhsbd_mob_quotes_stock_stockTab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_stock_stockTab | mob | 行情(quotes) | stock | stockTab | 0,2 | 0 | - | 5 | 3 |
| 9184 | lhsbd_mob_quotes_topGain_stockList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_行情(quotes)_涨幅榜_股票列表 | mob | 行情(quotes) | 涨幅榜 | 股票列表 | 0 | 3 | stock, num, gainLoserTab | 0 | 0 |
| 9160 | lhsbd_mob_accSecu | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity) | mob | 账号安全(accountSecurity) | - | - | 2 | 0 | - | 1 | 1 |
| 9164 | lhsbd_mob_accSecu_disconAc_discon | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_disconnectAccount_disconnect | mob | 账号安全(accountSecurity) | disconnectAccount | disconnect | 0 | 1 | content | 0 | 0 |
| 9161 | lhsbd_mob_accSecu_main_email | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_app主体部分_email | mob | 账号安全(accountSecurity) | app主体部分 | email | 0 | 0 | - | 0 | 0 |
| 9162 | lhsbd_mob_accSecu_main_phone | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_app主体部分_mobilePhone | mob | 账号安全(accountSecurity) | app主体部分 | mobilePhone | 0 | 0 | - | 0 | 0 |
| 9165 | lhsbd_mob_accSecu_main_setPass | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_app主体部分_setPassword | mob | 账号安全(accountSecurity) | app主体部分 | setPassword | 0 | 0 | - | 0 | 0 |
| 9163 | lhsbd_mob_accSecu_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_页面顶部_返回 | mob | 账号安全(accountSecurity) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 1 |
| 9326 | lhsbd_mob_accSecu_security_deleteaccount | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账号安全(accountSecurity)_安全_注销账户 | mob | 账号安全(accountSecurity) | 安全 | 注销账户 | 0 | 0 | - | 0 | 0 |
| 9350 | lhsbd_mob_accountAnalysis | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析 | mob | 账户分析 | - | - | 2 | 1 | type | 0 | 0 |
| 9353 | lhsbd_mob_accountAnalysis_perfChart_maxdd | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析_收益曲线_最大回撤 | mob | 账户分析 | 收益曲线 | 最大回撤 | 0 | 2 | content, state | 0 | 0 |
| 9352 | lhsbd_mob_accountAnalysis_perfChart_timearea | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析_收益曲线_时间周期 | mob | 账户分析 | 收益曲线 | 时间周期 | 0 | 3 | content, from, name | 0 | 0 |
| 9354 | lhsbd_mob_accountAnalysis_plDeatils_long | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析_盈亏详情_长 | mob | 账户分析 | 盈亏详情 | 长 | 0 | 1 | content | 0 | 0 |
| 9355 | lhsbd_mob_accountAnalysis_plDeatils_stocks | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析_盈亏详情_股票 | mob | 账户分析 | 盈亏详情 | 股票 | 0 | 2 | content, stock | 0 | 0 |
| 9351 | lhsbd_mob_accountAnalysis_title_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_账户分析_标题栏_返回 | mob | 账户分析 | 标题栏 | 返回 | 0 | 1 | content | 0 | 0 |
| 6385 | lhsbd_mob_trade | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_资产首页 | mob | 资产首页 | - | - | 2 | 0 | - | 0 | 0 |
| 9215 | lhsbd_mob_trade_common_search | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_通用页面_搜索按钮 | mob | 资产首页 | 通用页面 | 搜索按钮 | 0 | 0 | - | 0 | 1 |
| 9199 | lhsbd_mob_trade_order_cancel | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_orderBook_cancel按钮 | mob | 资产首页 | orderBook | 取消 | 0 | 1 | orderId | 0 | 0 |
| 9197 | lhsbd_mob_trade_order_list | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_orderBook_list | mob | 资产首页 | orderBook | list | 0 | 1 | orderId | 0 | 0 |
| 9198 | lhsbd_mob_trade_order_modify | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_orderBook_修改 | mob | 资产首页 | orderBook | 修改 | 0 | 1 | orderId | 0 | 0 |
| 9200 | lhsbd_mob_trade_order_quotes | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_orderBook_行情 | mob | 资产首页 | orderBook | 行情 | 0 | 1 | orderId | 0 | 0 |
| 9249 | lhsbd_mob_trade_order_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_orderBook_tab | mob | 资产首页 | orderBook | tab | 0 | 0 | - | 1 | 2 |
| 9186 | lhsbd_mob_trade_pageTop_tradeTab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_页面顶部_交易tab | mob | 资产首页 | 页面顶部 | 交易tab | 0,2 | 1 | tab | 12 | 11 |
| 9192 | lhsbd_mob_trade_position_buy | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_buy | mob | 资产首页 | 持仓 | buy | 0 | 1 | stock | 1 | 1 |
| 9194 | lhsbd_mob_trade_position_close | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_关闭 | mob | 资产首页 | 持仓 | 关闭 | 0 | 1 | stock | 2 | 1 |
| 9191 | lhsbd_mob_trade_position_detail | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_详情 | mob | 资产首页 | 持仓 | 详情 | 0 | 1 | stock | 2 | 2 |
| 9254 | lhsbd_mob_trade_position_liquidated | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_已清仓 | mob | 资产首页 | 持仓 | 已清仓 | 0 | 1 | mode | 1 | 1 |
| 9195 | lhsbd_mob_trade_position_quotes | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_行情 | mob | 资产首页 | 持仓 | 行情 | 0 | 1 | stock | 4 | 1 |
| 9193 | lhsbd_mob_trade_position_sell | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_sell | mob | 资产首页 | 持仓 | sell | 0 | 1 | stock | 5 | 1 |
| 9189 | lhsbd_mob_trade_position_sort | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_顺序调整 | mob | 资产首页 | 持仓 | 顺序调整 | 0 | 2 | state, order | 0 | 2 |
| 9190 | lhsbd_mob_trade_position_stoList | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_stockList | mob | 资产首页 | 持仓 | stockList | 0 | 1 | stock | 11 | 8 |
| 9188 | lhsbd_mob_trade_position_tab | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_tab | mob | 资产首页 | 持仓 | tab | 0 | 0 | - | 4 | 2 |
| 9253 | lhsbd_mob_trade_position_trade | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_持仓_交易 | mob | 资产首页 | 持仓 | 交易 | 0 | 1 | mode | 2 | 1 |
| 9187 | lhsbd_mob_trade_sumAsset_angle | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_总资产_展开控件 | mob | 资产首页 | 总资产 | 展开控件 | 0 | 1 | angleSta | 3 | 4 |
| 9196 | lhsbd_mob_trade_sumAsset_risk | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_总资产_风控状态 | mob | 资产首页 | 总资产 | 风控状态 | 0 | 0 | - | 0 | 0 |
| 9343 | lhsbd_mob_trade_titlemodule_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_交易(trade)_标题模组_返回 | mob | 资产首页 | 标题模组 | 返回 | 0 | 0 | - | 0 | 0 |
| 9383 | lhsbd_mob_newsDetailPage | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页 | mob | 资讯底层页 | - | - | 2 | 1 | news | 1 | 0 |
| 9344 | lhsbd_mob_newsDetailPage_aimevisual_aimevisualdisplay | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_aime可视化组件_aime可视化组件曝光 | mob | 资讯底层页 | aime可视化组件 | aime可视化组件曝光 | 2 | 2 | news, title | 0 | 0 |
| 9335 | lhsbd_mob_newsDetailPage_channel_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_渠道_曝光 | mob | 资讯底层页 | 渠道 | 曝光 | 2 | 1 | news | 0 | 0 |
| 9338 | lhsbd_mob_newsDetailPage_comment2_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_评论区_曝光 | mob | 资讯底层页 | 评论区 | 曝光 | 2 | 1 | news | 0 | 0 |
| 9337 | lhsbd_mob_newsDetailPage_image_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_图片_曝光 | mob | 资讯底层页 | 图片 | 曝光 | 2 | 2 | workId, news | 0 | 0 |
| 9334 | lhsbd_mob_newsDetailPage_items_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_关联物品_曝光 | mob | 资讯底层页 | 关联物品 | 曝光 | 2 | 1 | news | 0 | 0 |
| 9384 | lhsbd_mob_newsDetailPage_news_h5display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_news资讯_H5曝光 | mob | 资讯底层页 | news资讯 | H5曝光 | 2 | 2 | from, news | 0 | 1 |
| 9216 | lhsbd_mob_newsDetailPage_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_页面顶部_返回 | mob | 资讯底层页 | 页面顶部 | 返回 | 0 | 1 | news | 0 | 1 |
| 9339 | lhsbd_mob_newsDetailPage_page_stay | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_页面_停留 | mob | 资讯底层页 | 页面 | 停留 | 4 | 2 | news, stayLen | 1 | 0 |
| 9336 | lhsbd_mob_newsDetailPage_stock_display | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_资讯底层页_stock_曝光 | mob | 资讯底层页 | stock | 曝光 | 2 | 2 | stock, news | 0 | 0 |
| 9154 | lhsbd_mob_entPass | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_输入密码(enterPassword) | mob | 输入密码(enterPassword) | - | - | 2 | 0 | - | 1 | 1 |
| 9156 | lhsbd_mob_entPass_main_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_输入密码(enterPassword)_app主体部分_continue | mob | 输入密码(enterPassword) | app主体部分 | continue | 0 | 0 | - | 0 | 0 |
| 9155 | lhsbd_mob_entPass_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_输入密码(enterPassword)_app主体部分_输入框 | mob | 输入密码(enterPassword) | app主体部分 | 输入框 | 0 | 0 | - | 1 | 1 |
| 9157 | lhsbd_mob_entPass_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_输入密码(enterPassword)_页面顶部_返回 | mob | 输入密码(enterPassword) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 0 |
| 9139 | lhsbd_mob_emaSign | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_邮箱登录(emailSignin) | mob | 邮箱登录(emailSignin) | - | - | 2 | 0 | - | 2 | 2 |
| 9140 | lhsbd_mob_emaSign_main_inputBox | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_邮箱登录(emailSignin)_app主体部分_输入框 | mob | 邮箱登录(emailSignin) | app主体部分 | 输入框 | 0 | 0 | - | 1 | 1 |
| 9141 | lhsbd_mob_emaSign_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_邮箱登录(emailSignin)_页面顶部_返回 | mob | 邮箱登录(emailSignin) | 页面顶部 | 返回 | 0 | 0 | - | 1 | 1 |
| 9158 | lhsbd_mob_rePassSu | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_重置密码成功(resetPasswordSuccess) | mob | 重置密码成功(resetPasswordSuccess) | - | - | 2 | 0 | - | 0 | 0 |
| 9159 | lhsbd_mob_rePassSu_main_continue | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_重置密码成功(resetPasswordSuccess)_app主体部分_continue | mob | 重置密码成功(resetPasswordSuccess) | app主体部分 | continue | 0 | 0 | - | 0 | 0 |
| 9150 | lhsbd_mob_verify | 页面埋点 | 券商(AinvestBroker)_Ainvest APP_验证码(verify) | mob | 验证码(verify) | - | - | 2 | 0 | - | 2 | 2 |
| 9151 | lhsbd_mob_verify_pageTop_back | 元素埋点 | 券商(AinvestBroker)_Ainvest APP_验证码(verify)_页面顶部_返回 | mob | 验证码(verify) | 页面顶部 | 返回 | 0 | 0 | - | 2 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### lhsbd_cot_newOAOH5_Success_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_Success_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_address_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_address_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | 编辑区域的标题名称 | string | 0 |

### lhsbd_cot_newOAOH5_address_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |

### lhsbd_cot_newOAOH5_agreement_agreementList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 列表中操作行为发生时，所在的行信息 | listRow | - | string | 0 |

### lhsbd_cot_newOAOH5_agreement_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_agreement_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_agreement_selectButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_choosePop_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |
| 标题 | title | - | string | 2,4 |

### lhsbd_cot_newOAOH5_citizen_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | 选择的国家 | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | 用户的居住国家（简称） | object | 0 |

### lhsbd_cot_newOAOH5_citizen_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | 用户提交的国籍 | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | 用户选择的居住国家 | object | 0 |

### lhsbd_cot_newOAOH5_citizen_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | 用户的residentCountry | object | 2 |

### lhsbd_cot_newOAOH5_dependNo_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_dependNo_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_dependNo_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_disclosure_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_disclosure_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_dueDiligence_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_dueDiligence_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_employinfo_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_employinfo_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_employinfo_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 4,2 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_employstatus_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_employstatus_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_employstatus_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_financialstatus_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_financialstatus_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | - | string | 0 |
| 场景名 | targetName | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_financialstatus_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2 |
| 名称 | name | - | string | 2 |

### lhsbd_cot_newOAOH5_fundingsource_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_fundingsource_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_home_openWithoutID

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_home_openaccount

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_home_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | 渠道名称 | string | 2 |

### lhsbd_cot_newOAOH5_horizon_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_horizon_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_horizon_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |
| 名称 | name | - | string | 2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2 |

### lhsbd_cot_newOAOH5_liquidiyimportance_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_liquidiyimportance_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_liquidiyimportance_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_marital_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_marital_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_marital_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_object_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_object_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_object_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_ocrResult_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_ocrResult_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 标题 | title | 点击区域的标题名称 | string | 0 |

### lhsbd_cot_newOAOH5_ocrResult_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |

### lhsbd_cot_newOAOH5_ocrResult_reUpload

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_permanentResident_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_permanentResident_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_personalInformation_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_personalInformation_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | 编辑区域的标题 | string | 0 |

### lhsbd_cot_newOAOH5_personalInformation_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |

### lhsbd_cot_newOAOH5_placeOfBirth_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_placeOfBirth_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_recallpop_bottomButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 当前页面id，业务方自定义的页面标识，一般为数字 | fid | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_recallpop_closebutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 当前页面id，业务方自定义的页面标识，一般为数字 | fid | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_recallpop_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 当前页面id，业务方自定义的页面标识，一般为数字 | fid | - | string | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_risktolerance_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_risktolerance_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_risktolerance_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |
| 名称 | name | - | string | 2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2 |

### lhsbd_cot_newOAOH5_screenertoptab_back

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | 渠道名称 | string | 0 |
| 当前页面id，业务方自定义的页面标识，一般为数字 | fid | 当前页面ID | string | 0 |

### lhsbd_cot_newOAOH5_screenertoptab_quit

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 当前页面id，业务方自定义的页面标识，一般为数字 | fid | - | string | 0 |

### lhsbd_cot_newOAOH5_ssn_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_ssn_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_ssn_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_taxID_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_taxID_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_taxID_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 4,2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_uploadLicense_backpage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_uploadLicense_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_uploadLicense_front

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_uploadLicense_manualInput

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |

### lhsbd_cot_newOAOH5_uploadLicense_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2 |

### lhsbd_cot_newOAOH5_uploadLicense_reUpload

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 类型 | type | 正面：font 反面：back | string | 0 |

### lhsbd_cot_newOAOH5_uploadPassport_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_uploadPassport_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_verifyIdentity1_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_verifyIdentity1_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_verifyIdentity1_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_verifyIdentity_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_verifyIdentity_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_verifyIdentity_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_visaexpire_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_visaexpire_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_visaexpire_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_visatype_choose

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_cot_newOAOH5_visatype_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_visatype_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_cot_newOAOH5_visaupload_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |

### lhsbd_cot_newOAOH5_visaupload_editInformation

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 0 |
| 名称 | name | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0 |
| 标题 | title | - | string | 0 |

### lhsbd_cot_newOAOH5_visaupload_pageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | - | string | 2,4 |
| 名称 | name | - | string | 2,4 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 2,4 |
| 停留时长 | stayLen | - | int | 4 |

### lhsbd_mob_uppage_frontbackswitch_enterback

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | language、prog_id、country | object | 5 |
| 国家 | country | - | string | 5 |
| 语言 | language | - | string | 5 |
| app的标识ID | progId | - | string | 5 |

### lhsbd_mob_uppage_frontbackswitch_enterfront

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | language、prog_id、country | object | 5 |
| 语言 | language | - | string | 5 |
| 国家 | country | - | string | 5 |
| app的标识ID | progId | - | string | 5 |

### lhsbd_mob_uppage_page_Start

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | language | object | 8 |
| app的标识ID | progId | - | string | 8 |
| 语言 | language | - | string | 8 |
| 国家 | country | - | string | 8 |

### lhsbd_mob_H5IndustryQuote

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回页面的概念/行业名称 | string | 2 |

### lhsbd_mob_H5IndustryQuote_chart_linestyle

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回选择的线型 | string | 0 |

### lhsbd_mob_H5IndustryQuote_chart_timearea

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回选择的时间区间 | string | 0 |

### lhsbd_mob_cryptoLQ

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 币种代码，可能是英文或数字代码 | symbol | - | string | 2 |

### lhsbd_mob_cryptoLQ_index_tsDim

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### lhsbd_mob_myrew_rewtab_tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 点击的具体tab | string | 0 |

### lhsbd_mob_newsCalendar_calDate_date

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期 | dateTime | - | string | 0 |

### lhsbd_mob_newsCalendar_calEar_calQuote

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_userCen_funcList_helpFeed

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 登录 ”login“ 未登录"not_login" | enum | 0 |

### lhsbd_mob_livePlaceOrder

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |
| 可点击的菜单表头名称 | tab | 买卖方向，含Buy/Sell | string | 2 |

### lhsbd_mob_livePlaceOrder_FullOrderConfirm_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_FullOrderConfirm_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_FullOrderConfirm_orderCfm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |

### lhsbd_mob_livePlaceOrder_main_adjAmount

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_adjPrice

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 类型 | type | 订单类型，含market / limit / stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |

### lhsbd_mob_livePlaceOrder_main_buy

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_buytab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_main_inputquantity

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 0 |
| 数值 | value | - | string | 0 |

### lhsbd_mob_livePlaceOrder_main_kbdecimal

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含market / limit / stop | string | 0 |
| 股票代码 | stock | - | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_orderCfm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 2 |
| 类型 | type | 订单类型，含limit/market/stop | string | 2 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 2 |

### lhsbd_mob_livePlaceOrder_main_orderMode

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_orderType

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 股票代码 | stock | - | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |

### lhsbd_mob_livePlaceOrder_main_qckAmount

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的仓位，包含all /pct后跟具体百分比/ xxShare / xxUSD | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_search

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |

### lhsbd_mob_livePlaceOrder_main_sell

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_main_selltab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_main_tradinghoursselect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含market / limit / stop | string | 0 |
| 模式 | mode | "含盘前盘后"点击后的状态，含extendOn / extendOff | string | 0 |

### lhsbd_mob_livePlaceOrder_modify_ModifyCfm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_modify_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_orderCfm_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_orderCfm_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_orderType_limitOdr

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_orderType_marketOdr

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |
| 类型 | type | 订单类型，含limit/market/stop | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |

### lhsbd_mob_livePlaceOrder_ordercancelCfm_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_detail

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_sell

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_sort

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 表示增序降序等 | order | - | string | 0 |

### lhsbd_mob_livePlaceOrder_position_stoList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_prompt_notextended

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_livePlaceOrder_selecttradinghours_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |

### lhsbd_mob_livePlaceOrder_selecttradinghours_extendedhours

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares/dollars | string | 0 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 0 |

### lhsbd_mob_livePlaceOrder_todayorder_ordercancelCfm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| 币种代码，可能是英文或数字代码 | symbol | - | string | 0 |

### lhsbd_mob_ppPlaceOrder

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |
| - | - | - | - | 2 |
| - | - | - | - | 2 |
| - | - | - | - | 2 |
| - | - | - | - | 2 |

### lhsbd_mob_ppPlaceOrder_main_orderCfm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |
| 可点击的菜单表头名称 | tab | 买卖方向，含buy/sell | string | 2 |
| 类型 | type | 订单类型，含limit/market/stop | string | 2 |
| 模式 | mode | 下单模式，按数量或者按金额分为shares / dollars | string | 2 |

### lhsbd_mob_ppPlaceOrder_orderCfm_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |
| - | - | - | - | 0 |
| - | - | - | - | 0 |
| - | - | - | - | 0 |

### lhsbd_mob_ppPlaceOrder_position_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_ppPlaceOrder_position_stoList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_marketingpage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 商品id | goodsId | 商品sid | string | 2 |

### lhsbd_mob_marketingpage_pageBot_bottom

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 商品id | goodsId | 商品sid | string | 2 |

### lhsbd_mob_twiWire

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| fromFrameId，来源页面id，即上一条埋点日志所在页面的id | ffid | 返回用户上一条埋点日志 | string | 2 |
| 可点击的菜单表头名称 | tab | 返回默认展示的一级以及二级tab名称 | string | 2 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 2 |

### lhsbd_mob_twiWire_pageTop_2tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 获取点击前往的tab的名称，不同tab用不同值对应 | string | 1,0 |
| fromFrameId，来源页面id，即上一条埋点日志所在页面的id | ffid | 获取用户前往该埋点的上一个埋点，构建用户路径 | string | 1,0 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 0,1 |

### lhsbd_mob_pushnotificationbar

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 运营平台对应的push id，content推送内容的title | pushId | 各推送的pushid，以区分每条数据； | string | 2,0 |

### lhsbd_mob_Search_common_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时用户输入的搜索内容 | searchContent | - | string | 0 |

### lhsbd_mob_Search_common_delete

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时用户输入的搜索内容 | searchContent | - | string | 0 |

### lhsbd_mob_IndustryTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 返回Tab类型为Theme/Industry/Sub-Industry | string | 2 |

### lhsbd_mob_paperTrade_order_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_paperTrade_order_list

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_paperTrade_position_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_paperTrade_position_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_paperTrade_position_stoList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_onboard_emailphone_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | 1.way：phone,email，记录用户手机还是邮箱继续登录 2.from：记录手机登录用户，手机号所属地区 | object | 0 |

### lhsbd_mob_signin

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 获取用户系统显示颜色 | enum | 2 |

### lhsbd_mob_litef10_about_seemore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_litef10_keyStatistics_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 2 |

### lhsbd_mob_litef10_news_newsList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0,2 |
| 列表中操作行为发生时，所在的行信息 | listRow | - | string | 0 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 0,2 |

### lhsbd_mob_bsktotalamount_confirm_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 不能提交的股票只数，大于0时提交：umsubmitted(1) | string | 0 |

### lhsbd_mob_bsktotalamount_confirm_collapse

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 不能提交的股票只数，大于0时提交：umsubmitted(1) | string | 0 |

### lhsbd_mob_bsktotalamount_confirm_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 不能提交的股票只数，大于0时提交：umsubmitted(1) | string | 0 |

### lhsbd_mob_bsktotalamount_confirm_unfold

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 不能提交的股票只数，大于0时提交：umsubmitted(1) | string | 0 |

### lhsbd_mob_bsktotalamount_main_popUp

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 弹框类型：insufficientbp | string | 2 |

### lhsbd_mob_bsktotalamount_popup_Pop

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 弹框类型：submitfailed | string | 2 |

### lhsbd_mob_bsktotalamount_popup_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 弹框类型：insufficientbp | string | 0 |

### lhsbd_mob_bsktotalamount_popup_deposit

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 弹框类型：insufficientbp | string | 0 |

### lhsbd_mob_bskchoose_main_add

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 选中的数量 | int | 0 |

### lhsbd_mob_bskchoose_main_selectall

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 选中：1，取消选中：0 | enum | 0 |

### lhsbd_mob_bskchoose_search_add

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 搜索框中的内容 | string | 0 |
| 标记列表行数 | num | 选中的条数 | int | 0 |

### lhsbd_mob_bskchoose_search_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 搜索框中的内容 | string | 0 |
| 标记列表行数 | num | 搜索出来的条数 | int | 0 |

### lhsbd_mob_bskchoose_search_empty

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 搜索框中的内容 | string | 2 |

### lhsbd_mob_liQuotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | ticker | - | string | 2 |

### lhsbd_mob_liQuotes_interval_1d

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_1m

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_1w

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_3m

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_5y

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_after

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_day

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0,7 |

### lhsbd_mob_liQuotes_interval_lineSwitch

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_interval_pre

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_pageTop_optButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述是否添加，0表示添加，1表示移除 | optType | - | string | 0 |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_liQuotes_wlDrawer_wlDrawer

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 2 |

### lhsbd_mob_customheader_editpopup_Pop

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 场景名 | targetName | 弹窗所在的页面，如：watchlist | string | 2 |

### lhsbd_mob_customheader_editpopup_deleteheader

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 点击删除的表头名称 | string | 0 |
| 物品id | itemId | 点击删除的表头ID | string | 0 |

### lhsbd_mob_customheader_editpopup_headerincrease

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 点击添加的表头名称 | string | 0 |
| 物品id | itemId | 点击添加的表头ID | string | 0 |
| 可点击的菜单表头名称 | tab | 表头所属tab的名称（英文） | string | 0 |

### lhsbd_mob_customheader_editpopup_renametheheader

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 点击的表头当时的名字 | string | 0 |
| 物品id | itemId | 点击的表头的ID | string | 0 |

### lhsbd_mob_customheader_editpopup_sortmetric

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 拖拽表头的显示名称 | string | 6 |
| 物品id | itemId | 点击和拖拽表头的ID | string | 6 |

### lhsbd_mob_customheader_editpopup_tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | tab显示的名称（英文） | string | 0 |

### lhsbd_mob_quotes_dist_today

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 用户点击的第几个位置 | num | - | int | 0 |

### lhsbd_mob_quotes_industry_stockLabel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | string | 0 |

### lhsbd_mob_quotes_monitor_index

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 用户点击的第几个位置 | num | - | int | 0 |

### lhsbd_mob_quotes_topGain_stockList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |
| 用户点击的第几个位置 | num | - | int | 0 |
| ainvest app中涨/跌幅的tab，分为preMarket、afterHours、1min、today | gainLoserTab | - | string | 0 |

### lhsbd_mob_accSecu_disconAc_discon

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### lhsbd_mob_accountAnalysis

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 券商名字 | string | 2 |

### lhsbd_mob_accountAnalysis_perfChart_maxdd

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 券商名字 | string | 0 |
| 状态 | state | 本次操作选中：1，取消选中：0 | enum | 0 |

### lhsbd_mob_accountAnalysis_perfChart_timearea

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 券商名字 | string | 0 |
| 入口 | from | 时间区间来源：mtd，3m，ytd，total，custom | string | 0 |
| 名称 | name | 选中的时间区间：mtd，3m，ytd，total，custom | string | 0 |

### lhsbd_mob_accountAnalysis_plDeatils_long

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 券商名字 | string | 0 |

### lhsbd_mob_accountAnalysis_plDeatils_stocks

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 券商名字 | string | 0 |
| 股票代码 | stock | 股票代码 | string | 0 |

### lhsbd_mob_accountAnalysis_title_back

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 券商的名称 | string | 0 |

### lhsbd_mob_trade_order_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_trade_order_list

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_trade_order_modify

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_trade_order_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 订单号 | orderId | - | string | 0 |

### lhsbd_mob_trade_pageTop_tradeTab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | - | string | 0,2 |

### lhsbd_mob_trade_position_buy

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_close

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_detail

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_liquidated

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 模式 | mode | 资产状态：NoCapital（资产为0）、NoPosition（有资产无持仓）、Holding（持有股票） | string | 0 |

### lhsbd_mob_trade_position_quotes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_sell

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_sort

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 点击的排序字段新增break-even price对应的参数为beprice | enum | 0 |
| 表示增序降序等 | order | - | string | 0 |

### lhsbd_mob_trade_position_stoList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | - | int | 0 |

### lhsbd_mob_trade_position_trade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 模式 | mode | 资产状态：NoCapital（资产为0）、NoPosition（有资产无持仓）、Holding（持有股票） | string | 0 |

### lhsbd_mob_trade_sumAsset_angle

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 三角icon的状态，表示展开/合起 | angleSta | - | string | 0 |

### lhsbd_mob_newsDetailPage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 获取曝光的文章标题 | string | 2 |

### lhsbd_mob_newsDetailPage_aimevisual_aimevisualdisplay

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 可视化组件曝光所在news id | string | 2 |
| 标题 | title | 可视化组件曝光所在news标题 | string | 2 |

### lhsbd_mob_newsDetailPage_channel_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 返回曝光分享渠道的文章标题 | string | 2 |

### lhsbd_mob_newsDetailPage_comment2_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 返回评论区曝光文章标题 | string | 2 |

### lhsbd_mob_newsDetailPage_image_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 作品id | workId | 返回曝光图片对应的图片id | string | 2 |
| 文章、资讯、新闻id | news | 返回曝光图片所在的文章标题 | string | 2 |

### lhsbd_mob_newsDetailPage_items_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 返回曝光文章的id | string | 2 |

### lhsbd_mob_newsDetailPage_news_h5display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | push或是inapp | string | 2 |
| 文章、资讯、新闻id | news | newsid | string | 2 |

### lhsbd_mob_newsDetailPage_pageTop_back

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 获取用户离开的文章标题 | string | 0 |

### lhsbd_mob_newsDetailPage_page_stay

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 文章、资讯、新闻id | news | 获取用户在底层页的停留的文章标题 | string | 4 |
| 停留时长 | stayLen | 获取用户在底层页停留的时长 | int | 4 |

### lhsbd_mob_newsDetailPage_stock_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 返回曝光的个股标签的个股代码 | string | 2 |
| 文章、资讯、新闻id | news | 返回曝光个股标签的文章标题 | string | 2 |
