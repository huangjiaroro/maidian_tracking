---
title: 关系连通分量
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - relation
  - component
  - ainvest
---

# 关系连通分量

将 `from_stat_id -> stat_id` 视为无向边后得到的连通分量，用于识别可能属于同一用户路径或功能域的埋点簇。

| 序号 | 节点数 | 主要应用 | 样例 trackKey |
| --- | --- | --- | --- |
| 1 | 2420 | 手机客户端（AInvestApp）(1105), AInvestWebScreener(611), 选股(StockScreener)(461) | aime_aime_aime_voiceInputEverywhere_clickToenter, aime_aime_aime_voiceInputEverywhere_longPressinput, aime_aime_aime_voiceInput_cancelSending, aime_aime_aime_voiceInput_clickToenter, aime_aime_aime_voiceInput_longPressinput… |
| 2 | 287 | 模拟炒股(StockSimulator)(287) | lhspt_aime_aimemix_button_everywhere, lhspt_aime_aimemix_hover_everywhere, lhspt_ainvest_unistall, lhspt_ainvest_unistall_bottom_cancel, lhspt_ainvest_unistall_buttom_continueunistall… |
| 3 | 147 | Readify(147) | rdify_ainvest_accountSetting, rdify_ainvest_accountSetting_deleteConfirmDialog_confirmDeleteBtn, rdify_ainvest_accountSetting_settingArea_deactivateAccountBtn, rdify_ainvest_accountSetting_settingArea_logoutBtn, rdify_ainvest_askAI… |
| 4 | 96 | aime(96) | aime_aime_AgentStore_agent_add, aime_aime_AgentStore_agent_clickagent, aime_aime_aimetalk, aime_aime_aimetalk_activeRecom_aimeexplain, aime_aime_aimetalk_activeRecom_heatTopic… |
| 5 | 90 | Readify(90) | rdify_ainvest_webAccountSetting, rdify_ainvest_webAccountSetting_accountSetting_languageDropdown, rdify_ainvest_webAccountSetting_accountSetting_themeToggleBtn, rdify_ainvest_webBookDetail, rdify_ainvest_webBookDetail_bookDetail_downloadBook… |
| 6 | 58 | 券商(AinvestBroker)(58) | lhsbd_mob_Search, lhsbd_mob_Search_common_cancel, lhsbd_mob_accSecu, lhsbd_mob_accSecu_pageTop_back, lhsbd_mob_liQuotes… |
| 7 | 38 | 手机客户端（AInvestApp）(38) | lhsa_mob_community_discussbot_back, lhsa_mob_community_discussbot_shareReflux, lhsa_mob_newsDetailPage, lhsa_mob_newsDetailPage_AIMEanalyze_PageShow, lhsa_mob_newsDetailPage_AIMEanalyze_recquestions… |
| 8 | 37 | 手机客户端（AInvestApp）(37) | lhsa_f10_profileUS, lhsa_f10_profileUS_MergerAcquire_module, lhsa_f10_profileUS_companyProfile_expand, lhsa_f10_profileUS_companyProfile_module, lhsa_f10_profileUS_companyProfile_more… |
| 9 | 29 | 手机客户端（AInvestApp）(29) | lhsa_f10_financialsUS, lhsa_f10_financialsUS_all_Share, lhsa_f10_financialsUS_balancechart_indicator, lhsa_f10_financialsUS_balancechart_module, lhsa_f10_financialsUS_balancechart_selection… |
| 10 | 29 | 券商(AinvestBroker)(29) | lhsbd_cot_newOAOH5_address_continue, lhsbd_cot_newOAOH5_address_editInformation, lhsbd_cot_newOAOH5_address_pageShow, lhsbd_cot_newOAOH5_choosePop_pageShow, lhsbd_cot_newOAOH5_citizen_choose… |
| 11 | 26 | 手机客户端（AInvestApp）(26) | lhsa_mob_litef10_analystprice_display, lhsa_mob_litef10_analystrating_More, lhsa_mob_litef10_analystrating_display, lhsa_mob_litef10_earning_display, lhsa_mob_litef10_financiallist_More… |
| 12 | 26 | 选股(StockScreener)(26) | lhssc_mob_community_discussbot_back, lhssc_mob_newsDetailPage, lhssc_mob_newsDetailPage_AIMEanalyze_PageShow, lhssc_mob_newsDetailPage_AIMEanalyze_recquestions, lhssc_mob_newsDetailPage_aimevisual_aimevisualdisplay… |
| 13 | 24 | 资讯(AinvestNews)(18), 手机客户端（AInvestApp）(6) | lhsa_ainvest_LiveTV_podcast_PageShow, lhsa_ainvest_LiveTV_podcast_clicklist, lhsa_ainvest_LiveTV_podcast_slide, lhsa_ainvest_LiveTV_podcastlist_PageShow, lhsa_mob_hotnews_tradeIdea_readmore… |
| 14 | 23 | 选股(StockScreener)(23) | lhssc_mob_litef10_analystprice_display, lhssc_mob_litef10_analystrating_More, lhssc_mob_litef10_analystrating_display, lhssc_mob_litef10_earning_display, lhssc_mob_litef10_financiallist_More… |
| 15 | 20 | 手机客户端（AInvestApp）(20) | lhsa_mob_cryptohomepage_me_tabname, lhsa_mob_socialtrade, lhsa_mob_socialtrade_article_cardList, lhsa_mob_socialtrade_leadersprofile_action, lhsa_mob_socialtrade_leadersprofile_backtestab… |
| 16 | 20 | 券商(AinvestBroker)(20) | lhsbd_mob_crePass, lhsbd_mob_crePass_pageTop_back, lhsbd_mob_emaSign, lhsbd_mob_emaSign_main_inputBox, lhsbd_mob_emaSign_pageTop_back… |
| 17 | 20 | PennyStock(20) | lhsps_mob_community_discussbot_back, lhsps_mob_newsDetailPage, lhsps_mob_newsDetailPage_AIMEanalyze_PageShow, lhsps_mob_newsDetailPage_AIMEanalyze_recquestions, lhsps_mob_newsDetailPage_aimevisual_aimevisualdisplay… |
| 18 | 20 | 模拟炒股(StockSimulator)(20) | lhspt_mob_newsDetailPage, lhspt_mob_newsDetailPage_AIMEanalyze_PageShow, lhspt_mob_newsDetailPage_AIMEanalyze_recquestions, lhspt_mob_newsDetailPage_aimevisual_aimevisualdisplay, lhspt_mob_newsDetailPage_channel_display… |
| 19 | 20 | 选股(StockScreener)(20) | lhssc_mob_StockForest, lhssc_mob_StockForestGuide, lhssc_mob_StockForestGuide_guide_Collect, lhssc_mob_StockForestLoading, lhssc_mob_StockForestLoading_UserAgre_Agree… |
| 20 | 18 | 手机客户端（AInvestApp）(18) | lhsa_mob_accountAnalysis, lhsa_mob_accountAnalysis_main_eye, lhsa_mob_accountAnalysis_perfChart_aseet, lhsa_mob_accountAnalysis_perfChart_buysellswitch, lhsa_mob_accountAnalysis_perfChart_pl… |
| 21 | 17 | 选股(StockScreener)(17) | lhssc_mob_socialtrade, lhssc_mob_socialtrade_leadersprofile_action, lhssc_mob_socialtrade_leadersprofile_backtestab, lhssc_mob_socialtrade_leadersprofile_biomore, lhssc_mob_socialtrade_leadersprofile_changePic… |
| 22 | 16 | 手机客户端（AInvestApp）(16) | lhsa_cot_newOAOH5_address_continue, lhsa_cot_newOAOH5_address_editInformation, lhsa_cot_newOAOH5_address_pageShow, lhsa_cot_newOAOH5_choosePop_pageShow, lhsa_cot_newOAOH5_home_openWithoutID… |
| 23 | 16 | 手机客户端（AInvestApp）(16) | lhsa_mob_deleteaccount, lhsa_mob_deleteaccount_cancelsubscription_gotit, lhsa_mob_deleteaccount_deleteaccount_close, lhsa_mob_deleteaccount_deleteaccount_return, lhsa_mob_deleteaccount_deleteagreement_check… |
| 24 | 14 | 手机客户端（AInvestApp）(14) | lhsa_mob_StockForest, lhsa_mob_StockForestGuide, lhsa_mob_StockForestGuide_guide_Collect, lhsa_mob_StockForestLoading, lhsa_mob_StockForestRulePage… |
| 25 | 14 | 手机客户端（AInvestApp）(14) | lhsa_mob_contestDet_answserQ_answerQues, lhsa_mob_contestDet_answserQ_cancel, lhsa_mob_contestDet_answserQ_confirm, lhsa_mob_contestDet_enroll_confirm, lhsa_mob_contestDet_main_enroll… |
| 26 | 14 | 手机客户端（AInvestApp）(14) | lhsa_mob_watchdetail_analystrating_Card, lhsa_mob_watchdetail_analystrating_buyclick, lhsa_mob_watchdetail_analystrating_sellclick, lhsa_mob_watchdetail_fundtrack_inflow, lhsa_mob_watchdetail_fundtrack_outflow… |
| 27 | 13 | 手机客户端（AInvestApp）(13) | lhsa_f10_DividendStrategy, lhsa_f10_DividendStrategy_Calculator_DivBar, lhsa_f10_DividendStrategy_Conclusion_Conclusion, lhsa_f10_DividendStrategy_Conclusion_ConclusionScan, lhsa_f10_DividendStrategy_Conclusion_Replay… |
| 28 | 13 | 手机客户端（AInvestApp）(13) | lhsa_mob_newsEarningsDetail, lhsa_mob_newsEarningsDetail_AIMarketAnalysis_askAime, lhsa_mob_newsEarningsDetail_AIMarketAnalysis_viewMore, lhsa_mob_newsEarningsDetail_earningsHead_earningsSeason, lhsa_mob_newsEarningsDetail_earningsHead_filings… |
| 29 | 12 | 手机客户端（AInvestApp）(12) | lhsa_mob_contestsList, lhsa_mob_contestsList_main_college, lhsa_mob_contestsList_main_friends, lhsa_mob_contestsList_main_hot, lhsa_mob_contestsList_main_public… |
| 30 | 12 | 手机客户端（AInvestApp）(12) | lhsa_mob_newprofile, lhsa_mob_newprofile_myprofile_chatButton, lhsa_mob_newprofile_myprofile_firsttab, lhsa_mob_newprofile_myprofile_pressfollow, lhsa_mob_newprofile_ordersTab_stockList… |
| 31 | 12 | 手机客户端（AInvestApp）(12) | lhsa_mob_paperTradingHome, lhsa_mob_paperTradingHome_Rewarded_viewall, lhsa_mob_paperTradingHome_accInfo_detail, lhsa_mob_paperTradingHome_hot_contestDet, lhsa_mob_paperTradingHome_hot_viewAll… |
| 32 | 12 | 模拟炒股(StockSimulator)(12) | lhspt_mob_litef10_analystprice_display, lhspt_mob_litef10_analystrating_More, lhspt_mob_litef10_analystrating_display, lhspt_mob_litef10_earning_display, lhspt_mob_litef10_financiallist_More… |
| 33 | 12 | 选股(StockScreener)(12) | lhssc_mob_watchdetail_analystrating_Card, lhssc_mob_watchdetail_analystrating_buyclick, lhssc_mob_watchdetail_analystrating_sellclick, lhssc_mob_watchdetail_fundtrack_inflow, lhssc_mob_watchdetail_fundtrack_outflow… |
| 34 | 11 | 模拟炒股(StockSimulator)(11) | lhspt_mob_paperTradingHome, lhspt_mob_paperTradingHome_Rewarded_detail, lhspt_mob_paperTradingHome_accInfo_detail, lhspt_mob_paperTradingHome_hot_contestDet, lhspt_mob_paperTradingHome_hot_viewAll… |
| 35 | 11 | 选股(StockScreener)(11) | lhssc_mob_newsCalendar, lhssc_mob_newsCalendar_calDate_date, lhssc_mob_newsCalendar_calEar_calQuote, lhssc_mob_newsCalendar_calEar_calReport, lhssc_mob_newsCalendar_calEar_calSnap… |
| 36 | 10 | 手机客户端（AInvestApp）(10) | lhsa_mob_optionentitlement, lhsa_mob_optionentitlement_agreement_next, lhsa_mob_optionentitlement_company_click, lhsa_mob_optionentitlement_email_click, lhsa_mob_optionentitlement_name_next… |
| 37 | 10 | AInvestWebScreener(10) | lhsws_aime_aimetalk_cowork_mainpage, lhsws_aime_aimetalk_cowork_skillhub, lhsws_ainvest_aimetalk_cowork_chatting, lhsws_ainvest_aimetalk_cowork_fileaimeclaw, lhsws_ainvest_aimetalk_cowork_startonboarding… |
| 38 | 9 | 手机客户端（AInvestApp）(9) | lhsa_mob_pattern_pattern_Pattern, lhsa_mob_pattern_pattern_catedrop, lhsa_mob_pattern_pattern_checkOut, lhsa_mob_pattern_pattern_kLine, lhsa_mob_pattern_pattern_scan… |
| 39 | 9 | PennyStock(9) | lhsps_mob_litef10_analystprice_display, lhsps_mob_litef10_analystrating_display, lhsps_mob_litef10_earning_display, lhsps_mob_litef10_financiallist_display, lhsps_mob_litef10_keyStatistics_show… |
| 40 | 9 | 模拟炒股(StockSimulator)(9) | lhspt_mob_contestDet_enroll_confirm, lhspt_mob_contestDet_main_enroll, lhspt_mob_contestDet_main_trade, lhspt_mob_paperContestDetail, lhspt_mob_paperContestDetail_leaderBoard_me… |
| 41 | 9 | 模拟炒股(StockSimulator)(9) | lhspt_mob_tradeIdeaScreener, lhspt_mob_tradeIdeaScreener_aimechatbox_bookmarkltem, lhspt_mob_tradeIdeaScreener_aimechatbox_filter, lhspt_mob_tradeIdeaScreener_aimechatbox_runquery, lhspt_mob_tradeIdeaScreener_congress_detail… |
| 42 | 9 | 选股(StockScreener)(9) | lhssc_mob_marketingpage, lhssc_mob_marketingpage_comment2_comment, lhssc_mob_marketingpage_pageBot_bottom, lhssc_mob_marketingpage_pay_goToPaywall, lhssc_mob_marketingpage_pay_open… |
| 43 | 8 | 手机客户端（AInvestApp）(8) | lhsa_mob_discoverCalendarAll, lhsa_mob_discoverCalendarAll_calDate_calDate, lhsa_mob_discoverCalendarAll_calDate_date, lhsa_mob_discoverCalendarAll_calEar_calQuote, lhsa_mob_discoverCalendarAll_calEar_calSnap… |
| 44 | 8 | PC客户端（AInvestPC）(8) | lhspc_pc_Stocks_Stock_interval, lhspc_pc_Stocks_Stock_linestyle, lhspc_pc_Stocks_Stock_quotes, lhspc_pc_Watchlist_Watchlists_mywatchlist, lhspc_pc_mainEvent… |
| 45 | 8 | 选股(StockScreener)(8) | lhssc_mob_accountAnalysis, lhssc_mob_accountAnalysis_perfChart_pl, lhssc_mob_accountAnalysis_perfChart_plRate, lhssc_mob_accountAnalysis_perfChart_timearea, lhssc_mob_accountAnalysis_plCalendar_calMonth… |
| 46 | 8 | 选股(StockScreener)(8) | lhssc_mob_contestDet_enroll_confirm, lhssc_mob_contestDet_main_enroll, lhssc_mob_contestDet_main_trade, lhssc_mob_paperContestDetail, lhssc_mob_paperContestDetail_leaderBoard_player… |
| 47 | 7 | 手机客户端（AInvestApp）(7) | lhsa_f10_etff10_allocate_show, lhsa_f10_etff10_dividends_show, lhsa_f10_etff10_etfmanager_show, lhsa_f10_etff10_holdings_show, lhsa_f10_etff10_profile_show… |
| 48 | 7 | 手机客户端（AInvestApp）(7) | lhsa_mob_appheatmaps_heatmaplayer2_backBtn, lhsa_mob_appheatmaps_heatmaplayer2_clickStock, lhsa_mob_appheatmaps_heatmaplayer2_clickindustry, lhsa_mob_appheatmaps_heatmaplayer2_clicktopsymbol, lhsa_mob_appheatmaps_heatmaplayer2_indexfilter… |
| 49 | 7 | 手机客户端（AInvestApp）(7) | lhsa_mob_cataprod, lhsa_mob_cataprod_list_paidproduct, lhsa_mob_cataprod_toptab_back, lhsa_mob_cataprod_toptab_share, lhsa_mob_guidelineconte… |
| 50 | 7 | 手机客户端（AInvestApp）(7) | lhsa_mob_newsEarningsHub, lhsa_mob_newsEarningsHub_calEar_Card, lhsa_mob_newsEarningsHub_forwardEarnings_Card, lhsa_mob_newsEarningsHub_hotEarnings_Card, lhsa_mob_newsEarningsHub_indthm_subtab… |
| 51 | 7 | PennyStock(7) | lhsps_f10_etff10_allocate_show, lhsps_f10_etff10_dividends_show, lhsps_f10_etff10_etfmanager_show, lhsps_f10_etff10_holdings_show, lhsps_f10_etff10_profile_show… |
| 52 | 7 | 模拟炒股(StockSimulator)(7) | lhspt_mob_cataprod, lhspt_mob_cataprod_list_paidproduct, lhspt_mob_cataprod_toptab_back, lhspt_mob_guidelineconte, lhspt_mob_guidelineconte_list_catalog… |
| 53 | 7 | 选股(StockScreener)(7) | lhssc_f10_etff10_allocate_show, lhssc_f10_etff10_dividends_show, lhssc_f10_etff10_etfmanager_show, lhssc_f10_etff10_holdings_show, lhssc_f10_etff10_profile_show… |
| 54 | 7 | 选股(StockScreener)(7) | lhssc_mob_cataprod, lhssc_mob_cataprod_list_paidproduct, lhssc_mob_cataprod_toptab_back, lhssc_mob_guidelineconte, lhssc_mob_guidelineconte_list_catalog… |
| 55 | 7 | 选股(StockScreener)(7) | lhssc_mob_insiderStrategy, lhssc_mob_insiderStrategy_position_clickStock, lhssc_mob_insiderStrategy_position_tab, lhssc_mob_insiderTrading, lhssc_mob_insiderTrading_selectedsignals_card… |
| 56 | 6 | 手机客户端（AInvestApp）(6) | lhsa_ainvest_zhuanpan, lhsa_ainvest_zhuanpan_guidepopup_addwidget, lhsa_ainvest_zhuanpan_guidepopup_giveup, lhsa_ainvest_zhuanpan_midColum_myReward, lhsa_ainvest_zhuanpan_midColum_rule… |
| 57 | 6 | 手机客户端（AInvestApp）(6) | lhsa_mob_magicportdet, lhsa_mob_magicportdet_detailspage_back, lhsa_mob_magicportdet_portintro_back, lhsa_mob_magicportdet_rangeset_tsDim, lhsa_mob_magicportdet_stocklist_removed… |
| 58 | 6 | 手机客户端（AInvestApp）(6) | lhsa_mob_paymentResult, lhsa_mob_paymentResult_paymentPending_close, lhsa_mob_paymentResult_paymentPending_continue, lhsa_mob_paymentResult_paymentPending_customersupport, lhsa_mob_paymentResult_paymentSuccess_continue… |
| 59 | 6 | 手机客户端（AInvestApp）(6) | lhsa_mob_sharingtrial, lhsa_mob_sharingtrial_Subplans_buybutton, lhsa_mob_sharingtrial_Subplans_clickShared, lhsa_mob_sharingtrial_Subplans_viewlist, lhsa_mob_sharingtrial_Subplans_viewmore… |
| 60 | 6 | 模拟炒股(StockSimulator)(6) | lhspt_mob_watchdetail_analystrating_Card, lhspt_mob_watchdetail_analystrating_buyclick, lhspt_mob_watchdetail_fundtrack_show, lhspt_mob_watchdetail_highlightmonitor_show, lhspt_mob_watchdetail_overall_CardClick… |
| 61 | 6 | 选股(StockScreener)(6) | lhssc_mob_contestsList, lhssc_mob_contestsList_main_college, lhssc_mob_contestsList_main_public, lhssc_mob_paperContestList, lhssc_mob_paperContestList_list_contestDet… |
| 62 | 6 | 选股(StockScreener)(6) | lhssc_mob_guideline, lhssc_mob_guideline_assocart_functbar, lhssc_mob_guideline_feedback_functbar, lhssc_mob_guideline_functjump_functbar, lhssc_mob_guideline_toptab_back… |
| 63 | 6 | 选股(StockScreener)(6) | lhssc_mob_paperTradingHome, lhssc_mob_paperTradingHome_accInfo_detail, lhssc_mob_paperTradingHome_hot_contestDet, lhssc_mob_paperTradingHome_main_allContestList, lhssc_mob_paperTradingHome_main_myContests… |
| 64 | 6 | 选股(StockScreener)(6) | lhssc_mob_paymentResult, lhssc_mob_paymentResult_paymentPending_close, lhssc_mob_paymentResult_paymentPending_continue, lhssc_mob_paymentResult_paymentPending_customersupport, lhssc_mob_paymentResult_paymentSuccess_continue… |
| 65 | 5 | aime(5) | aime_aime_AgentStore_createagent_choosevoice, aime_aime_AgentStore_createagent_creatcomfirm, aime_aime_AgentStore_createagent_polish, aime_aime_AgentStore_createagent_profile, aime_aime_AgentStore_createagent_promptTemp |
| 66 | 5 | 手机客户端（AInvestApp）(5) | lhsa_mob_hub, lhsa_mob_hub_aiagent_cardList, lhsa_mob_hub_highreturns_cardList, lhsa_mob_hub_kolstrategy_card, lhsa_mob_hub_kolstrategy_cardList |
| 67 | 5 | 手机客户端（AInvestApp）(5) | lhsa_mob_tradeIdeaScreener, lhsa_mob_tradeIdeaScreener_congress_detail, lhsa_mob_tradeIdeaScreener_hotnews_title, lhsa_mob_tradeIdeaScreener_screenerCard_Screener, lhsa_mob_tradeIdeaScreener_screenerCard_symbol |
| 68 | 5 | PennyStock(5) | lhsps_mob_marketingpage, lhsps_mob_marketingpage_comment2_comment, lhsps_mob_marketingpage_pageBot_bottom, lhsps_mob_marketingpage_pay_goToPaywall, lhsps_mob_marketingpage_pay_open |
| 69 | 5 | PennyStock(5) | lhsps_mob_newsCalendar, lhsps_mob_newsCalendar_calDate_date, lhsps_mob_newsCalendar_calEar_calQuote, lhsps_mob_newsCalendar_calTab_earnings, lhsps_mob_newsCalendar_calTab_featured |
| 70 | 5 | 模拟炒股(StockSimulator)(5) | lhspt_mob_contestsList, lhspt_mob_contestsList_main_public, lhspt_mob_paperContestList, lhspt_mob_paperContestList_list_contestDet, lhspt_mob_paperContestList_main_homefilter |
| 71 | 4 | aime(4) | aime_aime_aimetalk_aimeprofile_adjust, aime_aime_aimetalk_aimeprofile_livetv, aime_aime_aimetalk_aimeprofile_tabSwift, aime_aime_aimetalk_fintuneAime_save |
| 72 | 4 | aime(4) | aime_aime_memory_aimeMemDisp_chatButton, aime_aime_memory_aimeMemDisp_deletebutton, aime_aime_memory_aimeMemDisp_tabclick, aime_aime_memory_memorypage_PageShow |
| 73 | 4 | 手机客户端（AInvestApp）(4) | lhsa_f10_f10fda_Upcoming_cardSlide, lhsa_f10_f10fda_page_movedown, lhsa_f10_f10fda_toptab_Back, lhsa_f10_f10fda_toptab_quotes |
| 74 | 4 | 手机客户端（AInvestApp）(4) | lhsa_f10_revenueBreakdown, lhsa_f10_revenueBreakdown_page_chart, lhsa_f10_revenueBreakdown_page_tab, lhsa_f10_revenueBreakdown_page_timebar |
| 75 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_2025AppBFEvent_2025BlackFridayevent_drawchance, lhsa_mob_2025AppBFEvent_2025BlackFridayevent_drawreward, lhsa_mob_2025AppBFEvent_drawchance_spin, lhsa_mob_2025AppBFEvent_drawrewards_getitfree |
| 76 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_LiveTV, lhsa_mob_LiveTV_Newslive_slide, lhsa_mob_LiveTV_videosection_play, lhsa_mob_LiveTV_videosection_videodisplay |
| 77 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_PricingPage, lhsa_mob_PricingPage_learnmore_content, lhsa_mob_PricingPage_menu_timeswitch, lhsa_mob_PricingPage_pageBot_paidbotton |
| 78 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_bioedit, lhsa_mob_bioedit_myprofile_changelable, lhsa_mob_bioedit_myprofile_changename, lhsa_mob_bioedit_myprofile_save |
| 79 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_communityforyou, lhsa_mob_communityforyou_communitycard_capsulelabel, lhsa_mob_communityforyou_communitycard_hottopicsrecommend, lhsa_mob_communityforyou_communitycard_postentry |
| 80 | 4 | 手机客户端（AInvestApp）(4) | lhsa_mob_kolfocusdetails, lhsa_mob_kolfocusdetails_Time_timeselect, lhsa_mob_kolfocusdetails_focustrends_tabs, lhsa_mob_kolfocusdetails_paidproducts_locked |
