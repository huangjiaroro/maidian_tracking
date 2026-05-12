---
title: 应用 - Readify
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - rdify
  - ainvest
---

# Readify

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 35 |
| appSign | rdify |
| appKey | cda3c81997 |
| creator | huangjiarong@myhexin.com |
| createTime | 2025-12-24 15:25:40 |
| topicName | spider-ainvest |
| payloadStatus | 0 |
| pageCount(snapshot) | 29 |
| trackCount(snapshot) | 329 |
| relationTrackCount | 239 |
| tracksWithActionFields | 89 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| ainvest | 28 | 327 |
| rdify | 1 | 2 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1448 | askAI | AI问答页 | 3 | 8 |
| 1454 | readifyWebHome | Readify Web首页 | 3 | 0 |
| 1437 | readifyProfile | Readify个人中心 | 4 | 11 |
| 1452 | webNotes | Web笔记页 | 0 | 4 |
| 1457 | webDownloadPage | web下载页 | 0 | 4 |
| 1460 | webBookDetail | web书籍详情页 | 0 | 2 |
| 1456 | webMyVoice | web我的音色 | 2 | 7 |
| 1455 | webFindBooks | web搜书页 | 3 | 8 |
| 1458 | webAccountSetting | web账号设置 | 0 | 4 |
| 1459 | webReader | web阅读器 | 16 | 50 |
| 1453 | webHome | web首页 | 9 | 28 |
| 1506 | searchInBook | 书内搜索 | 3 | 8 |
| 1541 | bookmarkList | 书签列表页 | 0 | 4 |
| 1442 | bookSearchResult | 书籍搜索结果页 | 0 | 2 |
| 1444 | findBooksPage | 书籍搜索页 | 0 | 6 |
| 1449 | bookContents | 书籍目录页 | 0 | 3 |
| 1443 | bookDetail | 书籍详情页 | 0 | 2 |
| 1483 | collectionList | 分类列表页 | 7 | 22 |
| 1468 | extBar | 插件条 | 0 | 2 |
| 1441 | findBook | 搜索书籍页 | 2 | 3 |
| 1469 | newHome | 新首页 | 3 | 12 |
| 1445 | loginPage | 登录页 | 2 | 6 |
| 1451 | accountSetting | 账号设置 | 2 | 5 |
| 1446 | reader | 阅读器 | 22 | 63 |
| 1440 | readingNotesList | 阅读笔记列表页 | 0 | 2 |
| 1465 | voiceCloneSave | 音色克隆保存页 | 0 | 3 |
| 1463 | voiceCloneGuide | 音色克隆引导页 | 4 | 7 |
| 1447 | voice | 音色选择 | 5 | 12 |
| 1438 | readifyHome | 首页 | 14 | 41 |

## 关系枢纽埋点

| trackKey | 应用 | 页面 | 区块 | 元素 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- |
| rdify_ainvest_readifyHome | Readify | 首页 | - | - | 118 | 113 |
| rdify_ainvest_reader_bottomPlayerBar_pause | Readify | 阅读器 | 底部播放控制栏 | 暂停 | 87 | 74 |
| rdify_ainvest_reader_menucard_readerMenu | Readify | 阅读器 | 菜单栏 | 阅读菜单栏 | 92 | 69 |
| rdify_ainvest_reader | Readify | 阅读器 | - | - | 81 | 74 |
| rdify_ainvest_reader_topBar_moreBtn | Readify | 阅读器 | app顶部栏 | 更多按钮 | 52 | 44 |
| rdify_ainvest_reader_reader_play | Readify | 阅读器 | 阅读器 | 播放 | 37 | 54 |
| rdify_ainvest_reader_bottomPlayerBar_play | Readify | 阅读器 | 底部播放控制栏 | 播放 | 42 | 46 |
| rdify_ainvest_reader_reader_readerRight | Readify | 阅读器 | 阅读器 | 阅读器右侧 | 54 | 26 |
| rdify_ainvest_reader_bottomPlayerBar_goBack | Readify | 阅读器 | 底部播放控制栏 | 返回播放 | 38 | 33 |
| rdify_ainvest_reader_topBar_contents | Readify | 阅读器 | app顶部栏 | 目录 | 46 | 20 |
| rdify_ainvest_reader_floatActionBar_stopAudio | Readify | 阅读器 | 悬浮操作栏 | 关闭听书 | 30 | 35 |
| rdify_ainvest_reader_progressBar_progressIndicator | Readify | 阅读器 | 播放进度栏 | 进度指示器 | 30 | 34 |
| rdify_ainvest_reader_reader_readerLeft | Readify | 阅读器 | 阅读器 | 阅读器左侧 | 43 | 21 |
| rdify_ainvest_bookContents | Readify | 书籍目录页 | - | - | 16 | 47 |
| rdify_ainvest_newHome | Readify | 新首页 | - | - | 46 | 17 |
| rdify_ainvest_reader_drawtoolbar_ttsBtn | Readify | 阅读器 | 画线工具栏 | 听这里按钮 | 35 | 27 |
| rdify_ainvest_reader_bottomPlayerBar_choosevoice | Readify | 阅读器 | 底部播放控制栏 | 选择声音 | 30 | 31 |
| rdify_ainvest_reader_bottomPlayerBar_playHere | Readify | 阅读器 | 底部播放控制栏 | 从本页听 | 39 | 22 |
| rdify_ainvest_readifyHome_bookList_saveToLib | Readify | 首页 | 书籍列表区 | 保存到书架 | 26 | 34 |
| rdify_ainvest_reader_topBar_fontSettingBtn | Readify | 阅读器 | app顶部栏 | 字体设置按钮 | 40 | 15 |
| rdify_ainvest_voice | Readify | 音色选择 | - | - | 30 | 25 |
| rdify_ainvest_bookContents_contents_contents | Readify | 书籍目录页 | 文章目录 | 目录 | 16 | 38 |
| rdify_ainvest_webHome | Readify | web首页 | - | - | 25 | 29 |
| rdify_ainvest_voice_voiceSelect_voiceCardList | Readify | 音色选择 | 声音选择 | 音色卡片列表 | 18 | 35 |
| rdify_ainvest_reader_bottomPlayerBar_rewindBtn | Readify | 阅读器 | 底部播放控制栏 | 后退按钮 | 23 | 27 |
| rdify_ainvest_askAI | Readify | AI问答页 | - | - | 22 | 27 |
| rdify_ainvest_reader_drawtoolbar_highlightBtn | Readify | 阅读器 | 画线工具栏 | 划线按钮 | 33 | 16 |
| rdify_ainvest_reader_speedSetting_speedBtn | Readify | 阅读器 | 倍速选择 | 倍速按钮 | 13 | 36 |
| rdify_ainvest_readifyHome_bookList_bookCard | Readify | 首页 | 书籍列表区 | 书籍卡片 | 26 | 23 |
| rdify_ainvest_voice_voiceSelect_proTypeTab | Readify | 音色选择 | 声音选择 | Pro类型标签 | 28 | 21 |

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14336 | rdify_ainvest_askAI | 页面埋点 | Readify_Ainvest_AI问答页 | ainvest | AI问答页 | - | - | 2 | 0 | - | 22 | 27 |
| 14335 | rdify_ainvest_askAI_aiChatArea_stopAiBtn | 元素埋点 | Readify_Ainvest_AI问答页_AI对话区域_停止AI回答按钮 | ainvest | AI问答页 | AI对话区域 | 停止AI回答按钮 | 0 | 1 | content | 1 | 2 |
| 14334 | rdify_ainvest_askAI_aiInputArea_sendQuestionBtn | 元素埋点 | Readify_Ainvest_AI问答页_AI输入区域_发送问题按钮 | ainvest | AI问答页 | AI输入区域 | 发送问题按钮 | 0 | 3 | content, activityId, function | 7 | 23 |
| 15223 | rdify_ainvest_askAI_aiReplyArea_copyBtn | 元素埋点 | Readify_Ainvest_AI问答页_AI回复区域_复制按钮 | ainvest | AI问答页 | AI回复区域 | 复制按钮 | 0 | 0 | - | 0 | 0 |
| 15225 | rdify_ainvest_askAI_aiReplyFeedback_dislikeBtn | 元素埋点 | Readify_Ainvest_AI问答页_AI回复反馈区域_踩按钮 | ainvest | AI问答页 | AI回复反馈区域 | 踩按钮 | 0 | 0 | - | 0 | 0 |
| 15224 | rdify_ainvest_askAI_aiReplyFeedback_likebutton | 元素埋点 | Readify_Ainvest_AI问答页_AI回复反馈区域_点赞按钮 | ainvest | AI问答页 | AI回复反馈区域 | 点赞按钮 | 0 | 0 | - | 0 | 0 |
| 14641 | rdify_ainvest_askAI_deepRead_deepRead | 元素埋点 | Readify_Ainvest_AI问答页_深度研读_深度研读 | ainvest | AI问答页 | 深度研读 | 深度研读 | 0,4 | 1 | state | 0 | 0 |
| 15222 | rdify_ainvest_askAI_textSelectionMenu_copyBtn | 元素埋点 | Readify_Ainvest_AI问答页_文本选择菜单_复制按钮 | ainvest | AI问答页 | 文本选择菜单 | 复制按钮 | 0 | 0 | - | 0 | 0 |
| 14223 | rdify_ainvest_readifyProfile | 页面埋点 | Readify_Ainvest_Readify个人中心 | ainvest | Readify个人中心 | - | - | 2 | 0 | - | 15 | 16 |
| 14262 | rdify_ainvest_readifyProfile_actionArea_submitBtn | 元素埋点 | Readify_Ainvest_Readify个人中心_操作区域_提交按钮 | ainvest | Readify个人中心 | 操作区域 | 提交按钮 | 0 | 2 | content, regisId | 2 | 6 |
| 14373 | rdify_ainvest_readifyProfile_bottom_loginBtn | 元素埋点 | Readify_Ainvest_Readify个人中心_页面底部_登录按钮 | ainvest | Readify个人中心 | 页面底部 | 登录按钮 | 0 | 0 | - | 9 | 1 |
| 14221 | rdify_ainvest_readifyProfile_functionList_about | 元素埋点 | Readify_Ainvest_Readify个人中心_功能列表区_关于 | ainvest | Readify个人中心 | 功能列表区 | 关于 | 0 | 0 | - | 10 | 10 |
| 14217 | rdify_ainvest_readifyProfile_functionList_readingNotesEntry | 元素埋点 | Readify_Ainvest_Readify个人中心_功能列表区_阅读笔记入口 | ainvest | Readify个人中心 | 功能列表区 | 阅读笔记入口 | 0 | 0 | - | 11 | 1 |
| 14220 | rdify_ainvest_readifyProfile_functionList_settingsEntry | 元素埋点 | Readify_Ainvest_Readify个人中心_功能列表区_设置入口 | ainvest | Readify个人中心 | 功能列表区 | 设置入口 | 0 | 0 | - | 13 | 11 |
| 14218 | rdify_ainvest_readifyProfile_functionList_shareBtn | 元素埋点 | Readify_Ainvest_Readify个人中心_功能列表区_分享按钮 | ainvest | Readify个人中心 | 功能列表区 | 分享按钮 | 0 | 0 | - | 7 | 7 |
| 14219 | rdify_ainvest_readifyProfile_functionList_userFeedback | 元素埋点 | Readify_Ainvest_Readify个人中心_功能列表区_用户反馈 | ainvest | Readify个人中心 | 功能列表区 | 用户反馈 | 0 | 0 | - | 8 | 10 |
| 14263 | rdify_ainvest_readifyProfile_guideArea_communityLink | 元素埋点 | Readify_Ainvest_Readify个人中心_引导区域_社区链接 | ainvest | Readify个人中心 | 引导区域 | 社区链接 | 0 | 0 | - | 1 | 2 |
| 14636 | rdify_ainvest_readifyProfile_myVoice_myVoice | 元素埋点 | Readify_Ainvest_Readify个人中心_我的音色_我的音色 | ainvest | Readify个人中心 | 我的音色 | 我的音色 | 0 | 0 | - | 0 | 0 |
| 14222 | rdify_ainvest_readifyProfile_webAppArea_webUrlCopy | 元素埋点 | Readify_Ainvest_Readify个人中心_Web应用区_Web应用URL复制 | ainvest | Readify个人中心 | Web应用区 | Web应用URL复制 | 0 | 0 | - | 6 | 7 |
| 14412 | rdify_ainvest_webNotes | 页面埋点 | Readify_Ainvest_Web笔记页 | ainvest | Web笔记页 | - | - | 2 | 0 | - | 4 | 6 |
| 14410 | rdify_ainvest_webNotes_actionArea_deleteBtn | 元素埋点 | Readify_Ainvest_Web笔记页_操作区域_删除按钮 | ainvest | Web笔记页 | 操作区域 | 删除按钮 | 0 | 0 | - | 0 | 0 |
| 14409 | rdify_ainvest_webNotes_actionArea_moreBtn | 元素埋点 | Readify_Ainvest_Web笔记页_操作区域_更多按钮 | ainvest | Web笔记页 | 操作区域 | 更多按钮 | 0 | 0 | - | 0 | 0 |
| 14411 | rdify_ainvest_webNotes_bookList_bookCard | 元素埋点 | Readify_Ainvest_Web笔记页_书籍列表区_书籍卡片 | ainvest | Web笔记页 | 书籍列表区 | 书籍卡片 | 0 | 2 | itemId, title | 1 | 1 |
| 14509 | rdify_ainvest_webDownloadPage | 页面埋点 | Readify_Ainvest_web下载页 | ainvest | web下载页 | - | - | 2 | 0 | - | 3 | 7 |
| 14507 | rdify_ainvest_webDownloadPage_downloadArea_IOSdownlod | 元素埋点 | Readify_Ainvest_web下载页_下载区域_IOSdownlod | ainvest | web下载页 | 下载区域 | IOSdownlod | 0 | 0 | - | 1 | 1 |
| 14508 | rdify_ainvest_webDownloadPage_downloadArea_chromeplugin | 元素埋点 | Readify_Ainvest_web下载页_下载区域_chrome插件 | ainvest | web下载页 | 下载区域 | chrome插件 | 0 | 0 | - | 1 | 3 |
| 14506 | rdify_ainvest_webDownloadPage_downloadArea_googleplaydownload | 元素埋点 | Readify_Ainvest_web下载页_下载区域_安卓下载 | ainvest | web下载页 | 下载区域 | 安卓下载 | 0 | 0 | - | 1 | 0 |
| 14564 | rdify_ainvest_webBookDetail | 页面埋点 | Readify_Ainvest_web书籍详情页 | ainvest | web书籍详情页 | - | - | 2 | 0 | - | 2 | 4 |
| 14565 | rdify_ainvest_webBookDetail_bookDetail_downloadBook | 元素埋点 | Readify_Ainvest_web书籍详情页_书籍详情_下载书籍 | ainvest | web书籍详情页 | 书籍详情 | 下载书籍 | 0 | 0 | - | 1 | 2 |
| 14505 | rdify_ainvest_webMyVoice | 页面埋点 | Readify_Ainvest_web我的音色 | ainvest | web我的音色 | - | - | 2 | 0 | - | 3 | 8 |
| 14504 | rdify_ainvest_webMyVoice_actionMenu_deleteBtn | 元素埋点 | Readify_Ainvest_web我的音色_操作菜单_删除按钮 | ainvest | web我的音色 | 操作菜单 | 删除按钮 | 0 | 0 | - | 1 | 1 |
| 14503 | rdify_ainvest_webMyVoice_actionMenu_editVoiceBtn | 元素埋点 | Readify_Ainvest_web我的音色_操作菜单_编辑音色按钮 | ainvest | web我的音色 | 操作菜单 | 编辑音色按钮 | 0 | 0 | - | 1 | 1 |
| 14502 | rdify_ainvest_webMyVoice_contentArea_moreBtn | 元素埋点 | Readify_Ainvest_web我的音色_内容区域_更多按钮 | ainvest | web我的音色 | 内容区域 | 更多按钮 | 0 | 0 | - | 3 | 3 |
| 14571 | rdify_ainvest_webMyVoice_creatVoice_creatVoice4 | 元素埋点 | Readify_Ainvest_web我的音色_音色克隆_音色克隆-4 | ainvest | web我的音色 | 音色克隆 | 音色克隆-4 | 2 | 0 | - | 2 | 4 |
| 14570 | rdify_ainvest_webMyVoice_creatVoice_savebutton | 元素埋点 | Readify_Ainvest_web我的音色_音色克隆_保存按钮 | ainvest | web我的音色 | 音色克隆 | 保存按钮 | 0 | 0 | - | 2 | 1 |
| 14500 | rdify_ainvest_webMyVoice_topBar_createVoiceBtn | 元素埋点 | Readify_Ainvest_web我的音色_app顶部栏_创建音色按钮 | ainvest | web我的音色 | app顶部栏 | 创建音色按钮 | 0 | 1 | from | 7 | 8 |
| 14499 | rdify_ainvest_webFindBooks | 页面埋点 | Readify_Ainvest_web搜书页 | ainvest | web搜书页 | - | - | 2 | 0 | - | 7 | 9 |
| 14563 | rdify_ainvest_webFindBooks_bookList_bookCard | 元素埋点 | Readify_Ainvest_web搜书页_书籍列表区_书籍卡片 | ainvest | web搜书页 | 书籍列表区 | 书籍卡片 | 0 | 2 | num, type | 3 | 7 |
| 14497 | rdify_ainvest_webFindBooks_historyArea_historyItem | 元素埋点 | Readify_Ainvest_web搜书页_历史搜索区_历史搜索项 | ainvest | web搜书页 | 历史搜索区 | 历史搜索项 | 0 | 1 | content | 1 | 2 |
| 14494 | rdify_ainvest_webFindBooks_searchArea_searchBtn | 元素埋点 | Readify_Ainvest_web搜书页_搜索区域_搜索按钮 | ainvest | web搜书页 | 搜索区域 | 搜索按钮 | 0 | 2 | content, type | 8 | 8 |
| 14492 | rdify_ainvest_webFindBooks_searchArea_searchInput | 元素埋点 | Readify_Ainvest_web搜书页_搜索区域_搜索框 | ainvest | web搜书页 | 搜索区域 | 搜索框 | 0 | 0 | - | 5 | 5 |
| 14493 | rdify_ainvest_webFindBooks_searchArea_storePreferencesBtn | 元素埋点 | Readify_Ainvest_web搜书页_搜索区域_偏好设置按钮 | ainvest | web搜书页 | 搜索区域 | 偏好设置按钮 | 0 | 0 | - | 2 | 2 |
| 14562 | rdify_ainvest_webFindBooks_storeSetting_savebutton | 元素埋点 | Readify_Ainvest_web搜书页_书源设置_保存按钮 | ainvest | web搜书页 | 书源设置 | 保存按钮 | 0 | 0 | - | 0 | 0 |
| 14495 | rdify_ainvest_webFindBooks_suggestionArea_suggestionItem | 元素埋点 | Readify_Ainvest_web搜书页_搜索建议区_搜索建议项 | ainvest | web搜书页 | 搜索建议区 | 搜索建议项 | 0 | 0 | - | 2 | 2 |
| 14516 | rdify_ainvest_webAccountSetting | 页面埋点 | Readify_Ainvest_web账号设置 | ainvest | web账号设置 | - | - | 2 | 0 | - | 2 | 6 |
| 14514 | rdify_ainvest_webAccountSetting_accountSetting_deactivateAccountBtn | 元素埋点 | Readify_Ainvest_web账号设置_账号设置_注销账户按钮 | ainvest | web账号设置 | 账号设置 | 注销账户按钮 | 0 | 0 | - | 0 | 0 |
| 14515 | rdify_ainvest_webAccountSetting_accountSetting_languageDropdown | 元素埋点 | Readify_Ainvest_web账号设置_账号设置_语言下拉选择 | ainvest | web账号设置 | 账号设置 | 语言下拉选择 | 0 | 1 | language | 1 | 1 |
| 14513 | rdify_ainvest_webAccountSetting_accountSetting_themeToggleBtn | 元素埋点 | Readify_Ainvest_web账号设置_账号设置_主题切换按钮 | ainvest | web账号设置 | 账号设置 | 主题切换按钮 | 0 | 1 | mode | 1 | 1 |
| 14541 | rdify_ainvest_webReader | 页面埋点 | Readify_Ainvest_web阅读器 | ainvest | web阅读器 | - | - | 2 | 1 | dateTime | 11 | 5 |
| 14552 | rdify_ainvest_webReader_aiChatArea_closeBtn | 元素埋点 | Readify_Ainvest_web阅读器_AI对话区域_关闭按钮 | ainvest | web阅读器 | AI对话区域 | 关闭按钮 | 0 | 0 | - | 9 | 9 |
| 14550 | rdify_ainvest_webReader_aiInputArea_sendQuestionBtn | 元素埋点 | Readify_Ainvest_web阅读器_AI输入区域_发送问题按钮 | ainvest | web阅读器 | AI输入区域 | 发送问题按钮 | 0 | 2 | content, activityId | 4 | 2 |
| 14551 | rdify_ainvest_webReader_aiInputArea_stopAiBtn | 元素埋点 | Readify_Ainvest_web阅读器_AI输入区域_停止AI回答按钮 | ainvest | web阅读器 | AI输入区域 | 停止AI回答按钮 | 0 | 0 | - | 1 | 2 |
| 14569 | rdify_ainvest_webReader_aiLayoutDone_aiLayoutDone | 元素埋点 | Readify_Ainvest_web阅读器_ai排版完成弹窗_ai排版完成弹窗 | ainvest | web阅读器 | ai排版完成弹窗 | ai排版完成弹窗 | 2 | 0 | - | 3 | 2 |
| 14568 | rdify_ainvest_webReader_aiOptimizationDialog_confirmbutton | 元素埋点 | Readify_Ainvest_web阅读器_AI排版优化弹窗_确定按钮 | ainvest | web阅读器 | AI排版优化弹窗 | 确定按钮 | 0 | 0 | - | 6 | 5 |
| 14545 | rdify_ainvest_webReader_aotuSkip_closeBtn | 元素埋点 | Readify_Ainvest_web阅读器_智能跳过弹窗_关闭按钮 | ainvest | web阅读器 | 智能跳过弹窗 | 关闭按钮 | 5 | 1 | state | 5 | 14 |
| 14533 | rdify_ainvest_webReader_contentBar_readBtn | 元素埋点 | Readify_Ainvest_web阅读器_内容操作栏_朗读按钮 | ainvest | web阅读器 | 内容操作栏 | 朗读按钮 | 0 | 1 | dateTime | 20 | 20 |
| 14566 | rdify_ainvest_webReader_deleteConfirmDialog_confirmDeleteBtn | 元素埋点 | Readify_Ainvest_web阅读器_删除确认弹窗_确认删除按钮 | ainvest | web阅读器 | 删除确认弹窗 | 确认删除按钮 | 0 | 0 | - | 1 | 1 |
| 14548 | rdify_ainvest_webReader_deletepop_deleteBtn | 元素埋点 | Readify_Ainvest_web阅读器_删除确认_删除按钮 | ainvest | web阅读器 | 删除确认 | 删除按钮 | 0 | 0 | - | 3 | 1 |
| 14554 | rdify_ainvest_webReader_feedbackModalBar_confirmbutton | 元素埋点 | Readify_Ainvest_web阅读器_反馈弹窗操作栏_确定按钮 | ainvest | web阅读器 | 反馈弹窗操作栏 | 确定按钮 | 0 | 1 | type | 0 | 0 |
| 14559 | rdify_ainvest_webReader_floatActionBar_addNote | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_添加笔记 | ainvest | web阅读器 | 悬浮操作栏 | 添加笔记 | 0 | 0 | - | 3 | 2 |
| 14560 | rdify_ainvest_webReader_floatActionBar_askAI | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_AI问答 | ainvest | web阅读器 | 悬浮操作栏 | AI问答 | 0 | 1 | content | 2 | 1 |
| 14561 | rdify_ainvest_webReader_floatActionBar_audioFix | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_音频纠错 | ainvest | web阅读器 | 悬浮操作栏 | 音频纠错 | 0 | 0 | - | 1 | 1 |
| 14556 | rdify_ainvest_webReader_floatActionBar_copyBtn | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_复制按钮 | ainvest | web阅读器 | 悬浮操作栏 | 复制按钮 | 0 | 0 | - | 8 | 5 |
| 14558 | rdify_ainvest_webReader_floatActionBar_highlightBtn | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_划线按钮 | ainvest | web阅读器 | 悬浮操作栏 | 划线按钮 | 0 | 0 | - | 9 | 8 |
| 14555 | rdify_ainvest_webReader_floatActionBar_playBtn | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_朗读播放按钮 | ainvest | web阅读器 | 悬浮操作栏 | 朗读播放按钮 | 0 | 0 | - | 12 | 12 |
| 14557 | rdify_ainvest_webReader_floatActionBar_searchBtn | 元素埋点 | Readify_Ainvest_web阅读器_悬浮操作栏_搜索按钮 | ainvest | web阅读器 | 悬浮操作栏 | 搜索按钮 | 0 | 1 | content | 1 | 1 |
| 14526 | rdify_ainvest_webReader_menu_searchInput | 元素埋点 | Readify_Ainvest_web阅读器_收费套餐_搜索框 | ainvest | web阅读器 | 收费套餐 | 搜索框 | 0 | 1 | content | 1 | 2 |
| 14543 | rdify_ainvest_webReader_noteArea_clickNote | 元素埋点 | Readify_Ainvest_web阅读器_笔记区_点击笔记 | ainvest | web阅读器 | 笔记区 | 点击笔记 | 0 | 0 | - | 5 | 4 |
| 14544 | rdify_ainvest_webReader_noteArea_deleteBtn | 元素埋点 | Readify_Ainvest_web阅读器_笔记区_删除按钮 | ainvest | web阅读器 | 笔记区 | 删除按钮 | 0 | 0 | - | 1 | 1 |
| 14553 | rdify_ainvest_webReader_noteWindow_savebutton | 元素埋点 | Readify_Ainvest_web阅读器_笔记弹窗_保存按钮 | ainvest | web阅读器 | 笔记弹窗 | 保存按钮 | 0 | 0 | - | 1 | 2 |
| 14535 | rdify_ainvest_webReader_playControl_choosevoice | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_选择声音 | ainvest | web阅读器 | 播放控制栏 | 选择声音 | 0 | 0 | - | 11 | 12 |
| 14540 | rdify_ainvest_webReader_playControl_closeBtn | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_关闭按钮 | ainvest | web阅读器 | 播放控制栏 | 关闭按钮 | 0 | 0 | - | 7 | 9 |
| 14538 | rdify_ainvest_webReader_playControl_forwardBtn | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_前进按钮 | ainvest | web阅读器 | 播放控制栏 | 前进按钮 | 0 | 0 | - | 8 | 7 |
| 14537 | rdify_ainvest_webReader_playControl_pause | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_暂停 | ainvest | web阅读器 | 播放控制栏 | 暂停 | 0 | 2 | dateTime, stayLen | 21 | 19 |
| 14536 | rdify_ainvest_webReader_playControl_rewindBtn | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_后退按钮 | ainvest | web阅读器 | 播放控制栏 | 后退按钮 | 0 | 0 | - | 4 | 5 |
| 14539 | rdify_ainvest_webReader_playControl_speedBtn | 元素埋点 | Readify_Ainvest_web阅读器_播放控制栏_倍速按钮 | ainvest | web阅读器 | 播放控制栏 | 倍速按钮 | 0 | 0 | - | 10 | 1 |
| 14546 | rdify_ainvest_webReader_readSetting_settingsPanel | 元素埋点 | Readify_Ainvest_web阅读器_阅读设置弹窗_阅读设置面板 | ainvest | web阅读器 | 阅读设置弹窗 | 阅读设置面板 | 5 | 0 | - | 5 | 15 |
| 14549 | rdify_ainvest_webReader_speedSetting_speedBtn | 元素埋点 | Readify_Ainvest_web阅读器_倍速选择_倍速按钮 | ainvest | web阅读器 | 倍速选择 | 倍速按钮 | 5 | 1 | value | 8 | 25 |
| 14547 | rdify_ainvest_webReader_themeSetting_changeTheme | 元素埋点 | Readify_Ainvest_web阅读器_主题设置弹窗_选择主题 | ainvest | web阅读器 | 主题设置弹窗 | 选择主题 | 5 | 1 | state | 2 | 24 |
| 14858 | rdify_ainvest_webReader_titleBar_shareBtn | 元素埋点 | Readify_Ainvest_web阅读器_顶部标题栏_分享按钮 | ainvest | web阅读器 | 顶部标题栏 | 分享按钮 | 0,4 | 2 | state, name | 0 | 0 |
| 14522 | rdify_ainvest_webReader_toolBar_aiSkip | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_智能跳过 | ainvest | web阅读器 | 工具栏 | 智能跳过 | 0 | 0 | - | 12 | 1 |
| 14523 | rdify_ainvest_webReader_toolBar_fontBtn | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_字体设置按钮 | ainvest | web阅读器 | 工具栏 | 字体设置按钮 | 0 | 0 | - | 16 | 2 |
| 14525 | rdify_ainvest_webReader_toolBar_pageMode | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_页面模式 | ainvest | web阅读器 | 工具栏 | 页面模式 | 0 | 0 | - | 16 | 18 |
| 14524 | rdify_ainvest_webReader_toolBar_themeBtn | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_主题切换按钮 | ainvest | web阅读器 | 工具栏 | 主题切换按钮 | 0 | 0 | - | 8 | 1 |
| 14521 | rdify_ainvest_webReader_toolBar_zoomInBtn | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_放大按钮 | ainvest | web阅读器 | 工具栏 | 放大按钮 | 0 | 0 | - | 9 | 9 |
| 14520 | rdify_ainvest_webReader_toolBar_zoomOutBtn | 元素埋点 | Readify_Ainvest_web阅读器_工具栏_缩小按钮 | ainvest | web阅读器 | 工具栏 | 缩小按钮 | 0 | 0 | - | 5 | 9 |
| 14517 | rdify_ainvest_webReader_topBar_backBtn | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_返回按钮 | ainvest | web阅读器 | app顶部栏 | 返回按钮 | 0 | 2 | stayLen, dateTime | 26 | 2 |
| 14518 | rdify_ainvest_webReader_topBar_contents | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_目录 | ainvest | web阅读器 | app顶部栏 | 目录 | 0 | 0 | - | 20 | 24 |
| 14519 | rdify_ainvest_webReader_topBar_readingNotesEntry | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_阅读笔记入口 | ainvest | web阅读器 | app顶部栏 | 阅读笔记入口 | 0 | 0 | - | 7 | 8 |
| 14567 | rdify_ainvest_webReader_topBar_switchToAILayout | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_切换成AI排版 | ainvest | web阅读器 | app顶部栏 | 切换成AI排版 | 0 | 0 | - | 5 | 4 |
| 14670 | rdify_ainvest_webReader_topBar_switchToEPUB | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_PDF转EPUB | ainvest | web阅读器 | app顶部栏 | PDF转EPUB | 4 | 0 | - | 0 | 0 |
| 14671 | rdify_ainvest_webReader_topBar_switchToEbookBtn | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_切换到电子书按钮 | ainvest | web阅读器 | app顶部栏 | 切换到电子书按钮 | 0 | 0 | - | 0 | 0 |
| 14672 | rdify_ainvest_webReader_topBar_switchToPDF | 元素埋点 | Readify_Ainvest_web阅读器_app顶部栏_切换到PDF | ainvest | web阅读器 | app顶部栏 | 切换到PDF | 0 | 0 | - | 0 | 0 |
| 14530 | rdify_ainvest_webReader_voiceSelect_allVoice | 元素埋点 | Readify_Ainvest_web阅读器_声音选择_全部声音 | ainvest | web阅读器 | 声音选择 | 全部声音 | 0 | 0 | - | 0 | 0 |
| 14542 | rdify_ainvest_webReader_voiceSelect_myVoice | 元素埋点 | Readify_Ainvest_web阅读器_声音选择_我的音色 | ainvest | web阅读器 | 声音选择 | 我的音色 | 0 | 0 | - | 3 | 6 |
| 14532 | rdify_ainvest_webReader_voiceSelect_recentlyUse | 元素埋点 | Readify_Ainvest_web阅读器_声音选择_最近使用 | ainvest | web阅读器 | 声音选择 | 最近使用 | 0 | 0 | - | 0 | 0 |
| 14531 | rdify_ainvest_webReader_voiceSelect_recmdVoice | 元素埋点 | Readify_Ainvest_web阅读器_声音选择_推荐声音 | ainvest | web阅读器 | 声音选择 | 推荐声音 | 0 | 0 | - | 3 | 6 |
| 14534 | rdify_ainvest_webReader_voiceSelect_voiceCardList | 元素埋点 | Readify_Ainvest_web阅读器_声音选择_音色卡片列表 | ainvest | web阅读器 | 声音选择 | 音色卡片列表 | 0 | 2 | name, language | 5 | 15 |
| 14420 | rdify_ainvest_webHome | 页面埋点 | Readify_Ainvest_web首页 | ainvest | web首页 | - | - | 2,8 | 4 | type, regisId, num, dateTime | 25 | 29 |
| 14857 | rdify_ainvest_webHome_MoreActions_deleteBtn | 元素埋点 | Readify_Ainvest_web首页_更多操作_删除按钮 | ainvest | web首页 | 更多操作 | 删除按钮 | 0 | 1 | state | 0 | 0 |
| 14855 | rdify_ainvest_webHome_MoreActions_renameBtn | 元素埋点 | Readify_Ainvest_web首页_更多操作_重命名按钮 | ainvest | web首页 | 更多操作 | 重命名按钮 | 0 | 0 | - | 0 | 0 |
| 14856 | rdify_ainvest_webHome_MoreActions_shareBtn | 元素埋点 | Readify_Ainvest_web首页_更多操作_分享按钮 | ainvest | web首页 | 更多操作 | 分享按钮 | 0,4 | 2 | state, name | 0 | 0 |
| 14463 | rdify_ainvest_webHome_accountSetting_accountSetting | 元素埋点 | Readify_Ainvest_web首页_账号设置_账号设置 | ainvest | web首页 | 账号设置 | 账号设置 | 0 | 0 | - | 3 | 1 |
| 14464 | rdify_ainvest_webHome_accountSetting_logoutBtn | 元素埋点 | Readify_Ainvest_web首页_账号设置_登出按钮 | ainvest | web首页 | 账号设置 | 登出按钮 | 0 | 0 | - | 1 | 0 |
| 14462 | rdify_ainvest_webHome_accountSetting_userFeedback | 元素埋点 | Readify_Ainvest_web首页_账号设置_用户反馈 | ainvest | web首页 | 账号设置 | 用户反馈 | 0 | 0 | - | 1 | 1 |
| 14859 | rdify_ainvest_webHome_bookList_bookShared | 元素埋点 | Readify_Ainvest_web首页_书籍列表区_接收分享书籍 | ainvest | web首页 | 书籍列表区 | 接收分享书籍 | 4 | 2 | state, name | 0 | 0 |
| 14580 | rdify_ainvest_webHome_bookList_saveToLib | 元素埋点 | Readify_Ainvest_web首页_书籍列表区_保存到书架 | ainvest | web首页 | 书籍列表区 | 保存到书架 | 4 | 3 | name, type, content | 17 | 22 |
| 14480 | rdify_ainvest_webHome_bottomBar_deleteBtn | 元素埋点 | Readify_Ainvest_web首页_底部操作栏_删除按钮 | ainvest | web首页 | 底部操作栏 | 删除按钮 | 0 | 0 | - | 6 | 1 |
| 14479 | rdify_ainvest_webHome_bottomBar_selectall | 元素埋点 | Readify_Ainvest_web首页_底部操作栏_选择全部 | ainvest | web首页 | 底部操作栏 | 选择全部 | 0 | 0 | - | 1 | 2 |
| 14854 | rdify_ainvest_webHome_bottomBar_shareBtn | 元素埋点 | Readify_Ainvest_web首页_底部操作栏_分享按钮 | ainvest | web首页 | 底部操作栏 | 分享按钮 | 0,4 | 2 | state, name | 0 | 0 |
| 14477 | rdify_ainvest_webHome_contentArea_bookCard | 元素埋点 | Readify_Ainvest_web首页_内容区域_书籍卡片 | ainvest | web首页 | 内容区域 | 书籍卡片 | 0 | 2 | itemId, title | 10 | 12 |
| 14419 | rdify_ainvest_webHome_deleteConfirmDialog_confirmDeleteBtn | 元素埋点 | Readify_Ainvest_web首页_删除确认弹窗_确认删除按钮 | ainvest | web首页 | 删除确认弹窗 | 确认删除按钮 | 0 | 1 | num | 1 | 6 |
| 14475 | rdify_ainvest_webHome_filterArea_fileTypeDropdown | 元素埋点 | Readify_Ainvest_web首页_筛选区域_文件类型下拉 | ainvest | web首页 | 筛选区域 | 文件类型下拉 | 0 | 1 | type | 3 | 2 |
| 14474 | rdify_ainvest_webHome_filterArea_searchBtn | 元素埋点 | Readify_Ainvest_web首页_筛选区域_搜索按钮 | ainvest | web首页 | 筛选区域 | 搜索按钮 | 0 | 0 | - | 2 | 4 |
| 14476 | rdify_ainvest_webHome_filterArea_sortDropdown | 元素埋点 | Readify_Ainvest_web首页_筛选区域_排序方式下拉 | ainvest | web首页 | 筛选区域 | 排序方式下拉 | 0 | 1 | order | 3 | 3 |
| 14482 | rdify_ainvest_webHome_importDialog_importFromGoogle | 元素埋点 | Readify_Ainvest_web首页_导入文件弹窗_谷歌网盘登录 | ainvest | web首页 | 导入文件弹窗 | 谷歌网盘登录 | 0 | 0 | - | 1 | 1 |
| 14481 | rdify_ainvest_webHome_importDialog_selectLocalFileBtn | 元素埋点 | Readify_Ainvest_web首页_导入文件弹窗_选择本地文件按钮 | ainvest | web首页 | 导入文件弹窗 | 选择本地文件按钮 | 0 | 0 | - | 4 | 10 |
| 14473 | rdify_ainvest_webHome_navigation_downloadNav | 元素埋点 | Readify_Ainvest_web首页_导航栏_下载导航 | ainvest | web首页 | 导航栏 | 下载导航 | 0 | 0 | - | 11 | 4 |
| 14468 | rdify_ainvest_webHome_navigation_importFromFilesBtn | 元素埋点 | Readify_Ainvest_web首页_导航栏_从文件导入按钮 | ainvest | web首页 | 导航栏 | 从文件导入按钮 | 0 | 0 | - | 8 | 8 |
| 14466 | rdify_ainvest_webHome_navigation_myBookshelfNav | 元素埋点 | Readify_Ainvest_web首页_导航栏_我的书架导航 | ainvest | web首页 | 导航栏 | 我的书架导航 | 0 | 0 | - | 25 | 7 |
| 14470 | rdify_ainvest_webHome_navigation_myVoiceNav | 元素埋点 | Readify_Ainvest_web首页_导航栏_我的音色导航 | ainvest | web首页 | 导航栏 | 我的音色导航 | 0 | 0 | - | 15 | 3 |
| 14469 | rdify_ainvest_webHome_navigation_notes | 元素埋点 | Readify_Ainvest_web首页_导航栏_笔记导航 | ainvest | web首页 | 导航栏 | 笔记导航 | 0 | 0 | - | 11 | 3 |
| 14486 | rdify_ainvest_webHome_renameDialog_confirmbutton | 元素埋点 | Readify_Ainvest_web首页_重命名弹窗_确定按钮 | ainvest | web首页 | 重命名弹窗 | 确定按钮 | 0 | 2 | name, title | 3 | 4 |
| 14467 | rdify_ainvest_webHome_topBar_smartSearchNav | 元素埋点 | Readify_Ainvest_web首页_app顶部栏_智能搜书导航 | ainvest | web首页 | app顶部栏 | 智能搜书导航 | 0 | 0 | - | 6 | 2 |
| 14491 | rdify_ainvest_webHome_userFeedback_communityLink | 元素埋点 | Readify_Ainvest_web首页_用户反馈区域_社区链接 | ainvest | web首页 | 用户反馈区域 | 社区链接 | 0 | 0 | - | 1 | 1 |
| 14490 | rdify_ainvest_webHome_userFeedback_submitBtn | 元素埋点 | Readify_Ainvest_web首页_用户反馈区域_提交按钮 | ainvest | web首页 | 用户反馈区域 | 提交按钮 | 0 | 2 | content, regisId | 0 | 0 |
| 15235 | rdify_ainvest_searchInBook | 页面埋点 | Readify_Ainvest_书内搜索 | ainvest | 书内搜索 | - | - | 2 | 0 | - | 8 | 18 |
| 15240 | rdify_ainvest_searchInBook_contentsTab_searchInput | 元素埋点 | Readify_Ainvest_书内搜索_目录tab_搜索框 | ainvest | 书内搜索 | 目录tab | 搜索框 | 0 | 0 | - | 6 | 14 |
| 15232 | rdify_ainvest_searchInBook_searchArea_cancelBtn | 元素埋点 | Readify_Ainvest_书内搜索_搜索区域_取消按钮 | ainvest | 书内搜索 | 搜索区域 | 取消按钮 | 0 | 0 | - | 4 | 20 |
| 15233 | rdify_ainvest_searchInBook_searchArea_clearHistoryBtn | 元素埋点 | Readify_Ainvest_书内搜索_搜索区域_清除历史按钮 | ainvest | 书内搜索 | 搜索区域 | 清除历史按钮 | 0 | 0 | - | 3 | 2 |
| 15236 | rdify_ainvest_searchInBook_searchArea_clearthecontext | 元素埋点 | Readify_Ainvest_书内搜索_搜索区域_清除上下文 | ainvest | 书内搜索 | 搜索区域 | 清除上下文 | 0 | 0 | - | 9 | 7 |
| 15234 | rdify_ainvest_searchInBook_searchArea_historyItem | 元素埋点 | Readify_Ainvest_书内搜索_搜索区域_历史搜索项 | ainvest | 书内搜索 | 搜索区域 | 历史搜索项 | 0 | 0 | - | 3 | 7 |
| 15231 | rdify_ainvest_searchInBook_searchArea_searchInput | 元素埋点 | Readify_Ainvest_书内搜索_搜索区域_搜索框 | ainvest | 书内搜索 | 搜索区域 | 搜索框 | 0 | 1 | content | 11 | 16 |
| 15238 | rdify_ainvest_searchInBook_searchResultList_searchResult | 元素埋点 | Readify_Ainvest_书内搜索_搜索结果列表_搜索结果 | ainvest | 书内搜索 | 搜索结果列表 | 搜索结果 | 0 | 0 | - | 5 | 13 |
| 15533 | rdify_ainvest_bookmarkList | 页面埋点 | Readify_Ainvest_书签列表页 | ainvest | 书签列表页 | - | - | 2 | 0 | - | 2 | 20 |
| 15532 | rdify_ainvest_bookmarkList_bookmarkItem_deleteBtn | 元素埋点 | Readify_Ainvest_书签列表页_书签项_删除按钮 | ainvest | 书签列表页 | 书签项 | 删除按钮 | 0 | 0 | - | 1 | 11 |
| 15531 | rdify_ainvest_bookmarkList_bookmarkList_bookmarkltem | 元素埋点 | Readify_Ainvest_书签列表页_书签列表区域_书签项 | ainvest | 书签列表页 | 书签列表区域 | 书签项 | 0 | 0 | - | 2 | 10 |
| 15530 | rdify_ainvest_bookmarkList_contentsTab_bookmarkTab | 元素埋点 | Readify_Ainvest_书签列表页_目录tab_书签Tab | ainvest | 书签列表页 | 目录tab | 书签Tab | 0 | 0 | - | 4 | 1 |
| 14268 | rdify_ainvest_bookSearchResult | 页面埋点 | Readify_Ainvest_书籍搜索结果页 | ainvest | 书籍搜索结果页 | - | - | 2 | 0 | - | 3 | 11 |
| 14267 | rdify_ainvest_bookSearchResult_bookList_bookCard | 元素埋点 | Readify_Ainvest_书籍搜索结果页_书籍列表区_书籍卡片 | ainvest | 书籍搜索结果页 | 书籍列表区 | 书籍卡片 | 0 | 1 | num | 10 | 8 |
| 14277 | rdify_ainvest_findBooksPage | 页面埋点 | Readify_Ainvest_书籍搜索页 | ainvest | 书籍搜索页 | - | - | 2 | 0 | - | 14 | 13 |
| 14275 | rdify_ainvest_findBooksPage_historyArea_historyItem | 元素埋点 | Readify_Ainvest_书籍搜索页_历史搜索区_历史搜索项 | ainvest | 书籍搜索页 | 历史搜索区 | 历史搜索项 | 0 | 0 | - | 6 | 8 |
| 14272 | rdify_ainvest_findBooksPage_searchArea_searchInput | 元素埋点 | Readify_Ainvest_书籍搜索页_搜索区域_搜索框 | ainvest | 书籍搜索页 | 搜索区域 | 搜索框 | 0 | 1 | content | 19 | 6 |
| 14273 | rdify_ainvest_findBooksPage_searchArea_searchSubmitBtn | 元素埋点 | Readify_Ainvest_书籍搜索页_搜索区域_搜索提交按钮 | ainvest | 书籍搜索页 | 搜索区域 | 搜索提交按钮 | 0 | 2 | content, type | 16 | 7 |
| 14276 | rdify_ainvest_findBooksPage_settingArea_storePreferencesBtn | 元素埋点 | Readify_Ainvest_书籍搜索页_设置区域_偏好设置按钮 | ainvest | 书籍搜索页 | 设置区域 | 偏好设置按钮 | 0 | 0 | - | 6 | 5 |
| 14274 | rdify_ainvest_findBooksPage_suggestionArea_suggestionItem | 元素埋点 | Readify_Ainvest_书籍搜索页_搜索建议区_搜索建议项 | ainvest | 书籍搜索页 | 搜索建议区 | 搜索建议项 | 0 | 0 | - | 2 | 5 |
| 14340 | rdify_ainvest_bookContents | 页面埋点 | Readify_Ainvest_书籍目录页 | ainvest | 书籍目录页 | - | - | 2 | 0 | - | 16 | 47 |
| 14338 | rdify_ainvest_bookContents_contents_contents | 元素埋点 | Readify_Ainvest_书籍目录页_文章目录_目录 | ainvest | 书籍目录页 | 文章目录 | 目录 | 0 | 0 | - | 16 | 38 |
| 14339 | rdify_ainvest_bookContents_titleBar_titleBar | 元素埋点 | Readify_Ainvest_书籍目录页_顶部标题栏_标题栏 | ainvest | 书籍目录页 | 顶部标题栏 | 标题栏 | 0 | 0 | - | 1 | 3 |
| 14271 | rdify_ainvest_bookDetail | 页面埋点 | Readify_Ainvest_书籍详情页 | ainvest | 书籍详情页 | - | - | 2 | 0 | - | 8 | 6 |
| 14270 | rdify_ainvest_bookDetail_bottomActionBar_saveToLibraryBtn | 元素埋点 | Readify_Ainvest_书籍详情页_底部操作栏_保存到图书馆按钮 | ainvest | 书籍详情页 | 底部操作栏 | 保存到图书馆按钮 | 0 | 0 | - | 3 | 6 |
| 14881 | rdify_ainvest_collectionList_MoreActions_deleteBtn | 元素埋点 | Readify_Ainvest_分类列表页_更多操作_删除按钮 | ainvest | 分类列表页 | 更多操作 | 删除按钮 | 0 | 0 | - | 0 | 0 |
| 14880 | rdify_ainvest_collectionList_MoreActions_renameBtn | 元素埋点 | Readify_Ainvest_分类列表页_更多操作_重命名按钮 | ainvest | 分类列表页 | 更多操作 | 重命名按钮 | 0 | 0 | - | 0 | 0 |
| 14879 | rdify_ainvest_collectionList_MoreActions_selectButton | 元素埋点 | Readify_Ainvest_分类列表页_更多操作_选择按钮 | ainvest | 分类列表页 | 更多操作 | 选择按钮 | 0 | 0 | - | 0 | 0 |
| 14878 | rdify_ainvest_collectionList_MoreActions_viewSwitchBtn | 元素埋点 | Readify_Ainvest_分类列表页_更多操作_视图切换按钮 | ainvest | 分类列表页 | 更多操作 | 视图切换按钮 | 0 | 1 | name | 0 | 0 |
| 14874 | rdify_ainvest_collectionList_bookList_bookCard | 元素埋点 | Readify_Ainvest_分类列表页_书籍列表区_书籍卡片 | ainvest | 分类列表页 | 书籍列表区 | 书籍卡片 | 0,9 | 2 | itemId, title | 0 | 0 |
| 14892 | rdify_ainvest_collectionList_bookList_select | 元素埋点 | Readify_Ainvest_分类列表页_书籍列表区_选择 | ainvest | 分类列表页 | 书籍列表区 | 选择 | 0 | 2 | name, direct | 0 | 0 |
| 14904 | rdify_ainvest_collectionList_collectionPanel_collectionBtn | 元素埋点 | Readify_Ainvest_分类列表页_分类面板_分类按钮 | ainvest | 分类列表页 | 分类面板 | 分类按钮 | 0 | 1 | name | 0 | 0 |
| 14905 | rdify_ainvest_collectionList_collectionPanel_confirmbutton | 元素埋点 | Readify_Ainvest_分类列表页_分类面板_确定按钮 | ainvest | 分类列表页 | 分类面板 | 确定按钮 | 0 | 1 | name | 0 | 0 |
| 14903 | rdify_ainvest_collectionList_collectionPanel_createButton | 元素埋点 | Readify_Ainvest_分类列表页_分类面板_创建按钮 | ainvest | 分类列表页 | 分类面板 | 创建按钮 | 0 | 0 | - | 0 | 0 |
| 14901 | rdify_ainvest_collectionList_collectionPanel_quickpanel | 元素埋点 | Readify_Ainvest_分类列表页_分类面板_快捷面板 | ainvest | 分类列表页 | 分类面板 | 快捷面板 | 2,5 | 0 | - | 0 | 0 |
| 14889 | rdify_ainvest_collectionList_deleteConfirmDialog_pop | 元素埋点 | Readify_Ainvest_分类列表页_删除确认弹窗_弹窗 | ainvest | 分类列表页 | 删除确认弹窗 | 弹窗 | 2 | 0 | - | 0 | 0 |
| 14896 | rdify_ainvest_collectionList_deleteconfirm_check | 元素埋点 | Readify_Ainvest_分类列表页_删除二次确认_勾选 | ainvest | 分类列表页 | 删除二次确认 | 勾选 | 0 | 1 | direct | 0 | 0 |
| 14895 | rdify_ainvest_collectionList_deleteconfirm_deleteBtn | 元素埋点 | Readify_Ainvest_分类列表页_删除二次确认_删除按钮 | ainvest | 分类列表页 | 删除二次确认 | 删除按钮 | 0 | 1 | name | 0 | 0 |
| 14894 | rdify_ainvest_collectionList_deleteconfirm_deleteDialogTitle | 元素埋点 | Readify_Ainvest_分类列表页_删除二次确认_删除弹窗标题 | ainvest | 分类列表页 | 删除二次确认 | 删除弹窗标题 | 2,5 | 0 | - | 0 | 0 |
| 14886 | rdify_ainvest_collectionList_libraryToolbar_deleteBtn | 元素埋点 | Readify_Ainvest_分类列表页_图书馆工具栏_删除按钮 | ainvest | 分类列表页 | 图书馆工具栏 | 删除按钮 | 0 | 0 | - | 0 | 0 |
| 14885 | rdify_ainvest_collectionList_libraryToolbar_exportBtn | 元素埋点 | Readify_Ainvest_分类列表页_图书馆工具栏_导出按钮 | ainvest | 分类列表页 | 图书馆工具栏 | 导出按钮 | 0 | 0 | - | 0 | 0 |
| 14883 | rdify_ainvest_collectionList_libraryToolbar_renameBtn | 元素埋点 | Readify_Ainvest_分类列表页_图书馆工具栏_重命名按钮 | ainvest | 分类列表页 | 图书馆工具栏 | 重命名按钮 | 0 | 0 | - | 0 | 0 |
| 14884 | rdify_ainvest_collectionList_libraryToolbar_shareBtn | 元素埋点 | Readify_Ainvest_分类列表页_图书馆工具栏_分享按钮 | ainvest | 分类列表页 | 图书馆工具栏 | 分享按钮 | 0 | 0 | - | 0 | 0 |
| 14888 | rdify_ainvest_collectionList_shareBook_shareResult | 元素埋点 | Readify_Ainvest_分类列表页_分享书籍_分享结果 | ainvest | 分类列表页 | 分享书籍 | 分享结果 | 4 | 2 | state, name | 0 | 0 |
| 14882 | rdify_ainvest_collectionList_titleBar_done | 元素埋点 | Readify_Ainvest_分类列表页_顶部标题栏_完成 | ainvest | 分类列表页 | 顶部标题栏 | 完成 | 0 | 0 | - | 0 | 0 |
| 14872 | rdify_ainvest_collectionList_topNavBar_backBtn | 元素埋点 | Readify_Ainvest_分类列表页_顶部导航栏_返回按钮 | ainvest | 分类列表页 | 顶部导航栏 | 返回按钮 | 0 | 0 | - | 0 | 0 |
| 14873 | rdify_ainvest_collectionList_topNavBar_moreBtn | 元素埋点 | Readify_Ainvest_分类列表页_顶部导航栏_更多按钮 | ainvest | 分类列表页 | 顶部导航栏 | 更多按钮 | 0 | 0 | - | 0 | 0 |
| 14648 | rdify_ainvest_extBar | 页面埋点 | Readify_Ainvest_插件条 | ainvest | 插件条 | - | - | 2 | 0 | - | 0 | 1 |
| 14650 | rdify_ainvest_extBar_playControl_playBtn | 元素埋点 | Readify_Ainvest_插件条_播放控制栏_朗读播放按钮 | ainvest | 插件条 | 播放控制栏 | 朗读播放按钮 | 0 | 0 | - | 1 | 0 |
| 14265 | rdify_ainvest_findBook | 页面埋点 | Readify_Ainvest_搜索书籍页 | ainvest | 搜索书籍页 | - | - | 2 | 0 | - | 3 | 7 |
| 14264 | rdify_ainvest_findBook_bottomBar_applyBtn | 元素埋点 | Readify_Ainvest_搜索书籍页_底部操作栏_应用按钮 | ainvest | 搜索书籍页 | 底部操作栏 | 应用按钮 | 0 | 0 | - | 2 | 7 |
| 14266 | rdify_ainvest_findBook_searchArea_stop | 元素埋点 | Readify_Ainvest_搜索书籍页_搜索区域_停止 | ainvest | 搜索书籍页 | 搜索区域 | 停止 | 0 | 1 | content | 7 | 5 |
| 14651 | rdify_ainvest_newHome | 页面埋点 | Readify_Ainvest_新首页 | ainvest | 新首页 | - | - | 2 | 0 | - | 46 | 17 |
| 14662 | rdify_ainvest_newHome_bookList_bookList | 元素埋点 | Readify_Ainvest_新首页_书籍列表区_书籍列表 | ainvest | 新首页 | 书籍列表区 | 书籍列表 | 0,2 | 2 | name, tab | 6 | 5 |
| 14909 | rdify_ainvest_newHome_bookList_tabs | 元素埋点 | Readify_Ainvest_新首页_书籍列表区_tab | ainvest | 新首页 | 书籍列表区 | tab | 0 | 1 | name | 0 | 0 |
| 14654 | rdify_ainvest_newHome_collections_collections | 元素埋点 | Readify_Ainvest_新首页_专题推荐_专题 | ainvest | 新首页 | 专题推荐 | 专题 | 0 | 0 | - | 3 | 4 |
| 14655 | rdify_ainvest_newHome_collections_seeAll | 元素埋点 | Readify_Ainvest_新首页_专题推荐_查看全部 | ainvest | 新首页 | 专题推荐 | 查看全部 | 0 | 0 | - | 4 | 4 |
| 14660 | rdify_ainvest_newHome_contentBar_saveToLib | 元素埋点 | Readify_Ainvest_新首页_内容操作栏_保存到书架 | ainvest | 新首页 | 内容操作栏 | 保存到书架 | 0 | 0 | - | 2 | 4 |
| 14661 | rdify_ainvest_newHome_contentBar_startReading | 元素埋点 | Readify_Ainvest_新首页_内容操作栏_开始阅读 | ainvest | 新首页 | 内容操作栏 | 开始阅读 | 0 | 0 | - | 6 | 6 |
| 14652 | rdify_ainvest_newHome_continueReading_bookCard | 元素埋点 | Readify_Ainvest_新首页_继续阅读_书籍卡片 | ainvest | 新首页 | 继续阅读 | 书籍卡片 | 0 | 0 | - | 8 | 10 |
| 14907 | rdify_ainvest_newHome_guideArea_importPcBtn | 元素埋点 | Readify_Ainvest_新首页_引导区域_从电脑导入按钮 | ainvest | 新首页 | 引导区域 | 从电脑导入按钮 | 0 | 0 | - | 0 | 0 |
| 14906 | rdify_ainvest_newHome_guideArea_selectLocalFileBtn | 元素埋点 | Readify_Ainvest_新首页_引导区域_选择本地文件按钮 | ainvest | 新首页 | 引导区域 | 选择本地文件按钮 | 0 | 0 | - | 0 | 0 |
| 14653 | rdify_ainvest_newHome_recommended_bookCard | 元素埋点 | Readify_Ainvest_新首页_为您推荐_书籍卡片 | ainvest | 新首页 | 为您推荐 | 书籍卡片 | 0 | 0 | - | 6 | 4 |
| 14656 | rdify_ainvest_newHome_tab_library | 元素埋点 | Readify_Ainvest_新首页_底部Tab_书架 | ainvest | 新首页 | 底部Tab | 书架 | 0 | 0 | - | 14 | 12 |
| 14279 | rdify_ainvest_loginPage | 页面埋点 | Readify_Ainvest_登录页 | ainvest | 登录页 | - | - | 2 | 0 | - | 9 | 13 |
| 14399 | rdify_ainvest_loginPage_IOSlog_loginBtn | 元素埋点 | Readify_Ainvest_登录页_IOS登录_登录按钮 | ainvest | 登录页 | IOS登录 | 登录按钮 | 0 | 1 | type | 0 | 0 |
| 14400 | rdify_ainvest_loginPage_UserAgre_priSta | 元素埋点 | Readify_Ainvest_登录页_用户协议_用户隐私协议 | ainvest | 登录页 | 用户协议 | 用户隐私协议 | 0 | 0 | - | 0 | 0 |
| 14401 | rdify_ainvest_loginPage_UserAgre_privacyPolicy | 元素埋点 | Readify_Ainvest_登录页_用户协议_privacyPolicy | ainvest | 登录页 | 用户协议 | privacyPolicy | 0 | 0 | - | 0 | 0 |
| 14278 | rdify_ainvest_loginPage_login_thirdPartyLogin | 元素埋点 | Readify_Ainvest_登录页_登陆_第三方登录 | ainvest | 登录页 | 登陆 | 第三方登录 | 0 | 2 | loginStatus, type | 3 | 14 |
| 14398 | rdify_ainvest_loginPage_topBar_backBtn | 元素埋点 | Readify_Ainvest_登录页_app顶部栏_返回按钮 | ainvest | 登录页 | app顶部栏 | 返回按钮 | 0 | 0 | - | 0 | 0 |
| 14368 | rdify_ainvest_accountSetting | 页面埋点 | Readify_Ainvest_账号设置 | ainvest | 账号设置 | - | - | 2 | 0 | - | 10 | 11 |
| 14366 | rdify_ainvest_accountSetting_deleteConfirmDialog_cancelDeleteBtn | 元素埋点 | Readify_Ainvest_账号设置_删除确认弹窗_取消注销按钮 | ainvest | 账号设置 | 删除确认弹窗 | 取消注销按钮 | 0 | 0 | - | 0 | 0 |
| 14367 | rdify_ainvest_accountSetting_deleteConfirmDialog_confirmDeleteBtn | 元素埋点 | Readify_Ainvest_账号设置_删除确认弹窗_确认删除按钮 | ainvest | 账号设置 | 删除确认弹窗 | 确认删除按钮 | 0 | 0 | - | 1 | 2 |
| 14375 | rdify_ainvest_accountSetting_settingArea_deactivateAccountBtn | 元素埋点 | Readify_Ainvest_账号设置_设置区域_注销账户按钮 | ainvest | 账号设置 | 设置区域 | 注销账户按钮 | 0 | 0 | - | 1 | 1 |
| 14376 | rdify_ainvest_accountSetting_settingArea_logoutBtn | 元素埋点 | Readify_Ainvest_账号设置_设置区域_登出按钮 | ainvest | 账号设置 | 设置区域 | 登出按钮 | 0 | 0 | - | 1 | 3 |
| 14295 | rdify_ainvest_reader | 页面埋点 | Readify_Ainvest_阅读器 | ainvest | 阅读器 | - | - | 2,4 | 5 | mode, name, language, function, dateTime | 81 | 74 |
| 14371 | rdify_ainvest_reader_aiOptimizationDialog_laterBtn | 元素埋点 | Readify_Ainvest_阅读器_AI排版优化弹窗_稍后按钮 | ainvest | 阅读器 | AI排版优化弹窗 | 稍后按钮 | 0 | 0 | - | 6 | 4 |
| 14372 | rdify_ainvest_reader_aiOptimizationDialog_viewNowBtn | 元素埋点 | Readify_Ainvest_阅读器_AI排版优化弹窗_立即查看按钮 | ainvest | 阅读器 | AI排版优化弹窗 | 立即查看按钮 | 0 | 0 | - | 22 | 3 |
| 14357 | rdify_ainvest_reader_bottomBar_playPdfBtn | 元素埋点 | Readify_Ainvest_阅读器_底部操作栏_播放PDF按钮 | ainvest | 阅读器 | 底部操作栏 | 播放PDF按钮 | 0 | 0 | - | 13 | 15 |
| 14288 | rdify_ainvest_reader_bottomPlayerBar_choosevoice | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_选择声音 | ainvest | 阅读器 | 底部播放控制栏 | 选择声音 | 0 | 0 | - | 30 | 31 |
| 14290 | rdify_ainvest_reader_bottomPlayerBar_forwardBtn | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_前进按钮 | ainvest | 阅读器 | 底部播放控制栏 | 前进按钮 | 0 | 0 | - | 22 | 26 |
| 14362 | rdify_ainvest_reader_bottomPlayerBar_goBack | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_返回播放 | ainvest | 阅读器 | 底部播放控制栏 | 返回播放 | 0 | 0 | - | 38 | 33 |
| 14297 | rdify_ainvest_reader_bottomPlayerBar_pause | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_暂停 | ainvest | 阅读器 | 底部播放控制栏 | 暂停 | 0 | 2 | dateTime, stayLen | 87 | 74 |
| 14344 | rdify_ainvest_reader_bottomPlayerBar_play | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_播放 | ainvest | 阅读器 | 底部播放控制栏 | 播放 | 0 | 0 | - | 42 | 46 |
| 14363 | rdify_ainvest_reader_bottomPlayerBar_playHere | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_从本页听 | ainvest | 阅读器 | 底部播放控制栏 | 从本页听 | 0 | 0 | - | 39 | 22 |
| 14289 | rdify_ainvest_reader_bottomPlayerBar_rewindBtn | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_后退按钮 | ainvest | 阅读器 | 底部播放控制栏 | 后退按钮 | 0 | 0 | - | 23 | 27 |
| 14291 | rdify_ainvest_reader_bottomPlayerBar_speedBtn | 元素埋点 | Readify_Ainvest_阅读器_底部播放控制栏_倍速按钮 | ainvest | 阅读器 | 底部播放控制栏 | 倍速按钮 | 0 | 0 | - | 28 | 13 |
| 14322 | rdify_ainvest_reader_drawtoolbar_askAI | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_AI问答 | ainvest | 阅读器 | 画线工具栏 | AI问答 | 0 | 1 | content | 15 | 9 |
| 14345 | rdify_ainvest_reader_drawtoolbar_audioFix | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_音频纠错 | ainvest | 阅读器 | 画线工具栏 | 音频纠错 | 0 | 0 | - | 9 | 8 |
| 14319 | rdify_ainvest_reader_drawtoolbar_copyBtn | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_复制按钮 | ainvest | 阅读器 | 画线工具栏 | 复制按钮 | 0 | 0 | - | 21 | 11 |
| 14320 | rdify_ainvest_reader_drawtoolbar_highlightBtn | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_划线按钮 | ainvest | 阅读器 | 画线工具栏 | 划线按钮 | 0 | 0 | - | 33 | 16 |
| 14321 | rdify_ainvest_reader_drawtoolbar_notesMenuItem | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_笔记菜单项 | ainvest | 阅读器 | 画线工具栏 | 笔记菜单项 | 0 | 0 | - | 19 | 11 |
| 14323 | rdify_ainvest_reader_drawtoolbar_ttsBtn | 元素埋点 | Readify_Ainvest_阅读器_画线工具栏_听这里按钮 | ainvest | 阅读器 | 画线工具栏 | 听这里按钮 | 0 | 0 | - | 35 | 27 |
| 14369 | rdify_ainvest_reader_feedbackModalBar_confirmBtn | 元素埋点 | Readify_Ainvest_阅读器_反馈弹窗操作栏_我知道了按钮 | ainvest | 阅读器 | 反馈弹窗操作栏 | 我知道了按钮 | 0 | 1 | type | 1 | 6 |
| 14293 | rdify_ainvest_reader_floatActionBar_askAI | 元素埋点 | Readify_Ainvest_阅读器_悬浮操作栏_AI问答 | ainvest | 阅读器 | 悬浮操作栏 | AI问答 | 0 | 0 | - | 27 | 13 |
| 14292 | rdify_ainvest_reader_floatActionBar_stopAudio | 元素埋点 | Readify_Ainvest_阅读器_悬浮操作栏_关闭听书 | ainvest | 阅读器 | 悬浮操作栏 | 关闭听书 | 0 | 0 | - | 30 | 35 |
| 14374 | rdify_ainvest_reader_formatConvertDialog_startConvertBtn | 元素埋点 | Readify_Ainvest_阅读器_格式转换弹窗_开始转换按钮 | ainvest | 阅读器 | 格式转换弹窗 | 开始转换按钮 | 0 | 0 | - | 8 | 11 |
| 14383 | rdify_ainvest_reader_menucard_backBtn | 元素埋点 | Readify_Ainvest_阅读器_菜单栏_返回按钮 | ainvest | 阅读器 | 菜单栏 | 返回按钮 | 0 | 3 | stayLen, dateTime, mode | 41 | 7 |
| 14341 | rdify_ainvest_reader_menucard_readerMenu | 元素埋点 | Readify_Ainvest_阅读器_菜单栏_阅读菜单栏 | ainvest | 阅读器 | 菜单栏 | 阅读菜单栏 | 2 | 0 | - | 92 | 69 |
| 15528 | rdify_ainvest_reader_pagePreview_backBtn | 元素埋点 | Readify_Ainvest_阅读器_页码预览_返回按钮 | ainvest | 阅读器 | 页码预览 | 返回按钮 | 0 | 0 | - | 2 | 4 |
| 14294 | rdify_ainvest_reader_progressBar_progressIndicator | 元素埋点 | Readify_Ainvest_阅读器_播放进度栏_进度指示器 | ainvest | 阅读器 | 播放进度栏 | 进度指示器 | 1 | 0 | - | 30 | 34 |
| 15525 | rdify_ainvest_reader_readerMenu_addBookmark | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_添加书签 | ainvest | 阅读器 | 阅读器菜单 | 添加书签 | 0 | 0 | - | 2 | 6 |
| 15526 | rdify_ainvest_reader_readerMenu_deleteBookmark | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_删除书签 | ainvest | 阅读器 | 阅读器菜单 | 删除书签 | 0 | 0 | - | 1 | 3 |
| 14303 | rdify_ainvest_reader_readerMenu_exportBtn | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_导出按钮 | ainvest | 阅读器 | 阅读器菜单 | 导出按钮 | 0 | 0 | - | 1 | 1 |
| 14301 | rdify_ainvest_reader_readerMenu_notesMenuItem | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_笔记菜单项 | ainvest | 阅读器 | 阅读器菜单 | 笔记菜单项 | 0 | 0 | - | 4 | 22 |
| 14762 | rdify_ainvest_reader_readerMenu_shareBtn | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_分享按钮 | ainvest | 阅读器 | 阅读器菜单 | 分享按钮 | 0 | 0 | - | 0 | 0 |
| 14302 | rdify_ainvest_reader_readerMenu_timerMenuItem | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_计时器菜单项 | ainvest | 阅读器 | 阅读器菜单 | 计时器菜单项 | 0 | 0 | - | 6 | 7 |
| 15677 | rdify_ainvest_reader_readerMenu_translateBtn | 元素埋点 | Readify_Ainvest_阅读器_阅读器菜单_翻译按钮 | ainvest | 阅读器 | 阅读器菜单 | 翻译按钮 | 0 | 2 | startStatus, endStatus | 11 | 10 |
| 15534 | rdify_ainvest_reader_reader_addBookmark | 元素埋点 | Readify_Ainvest_阅读器_阅读器_添加书签 | ainvest | 阅读器 | 阅读器 | 添加书签 | 1 | 0 | - | 22 | 11 |
| 15536 | rdify_ainvest_reader_reader_backBtn | 元素埋点 | Readify_Ainvest_阅读器_阅读器_返回按钮 | ainvest | 阅读器 | 阅读器 | 返回按钮 | 0 | 1 | source | 1 | 2 |
| 15535 | rdify_ainvest_reader_reader_deleteBookmark | 元素埋点 | Readify_Ainvest_阅读器_阅读器_删除书签 | ainvest | 阅读器 | 阅读器 | 删除书签 | 1 | 0 | - | 12 | 10 |
| 14712 | rdify_ainvest_reader_reader_play | 元素埋点 | Readify_Ainvest_阅读器_阅读器_播放 | ainvest | 阅读器 | 阅读器 | 播放 | 4 | 1 | dateTime | 37 | 54 |
| 14342 | rdify_ainvest_reader_reader_readerLeft | 元素埋点 | Readify_Ainvest_阅读器_阅读器_阅读器左侧 | ainvest | 阅读器 | 阅读器 | 阅读器左侧 | 0 | 0 | - | 43 | 21 |
| 14343 | rdify_ainvest_reader_reader_readerRight | 元素埋点 | Readify_Ainvest_阅读器_阅读器_阅读器右侧 | ainvest | 阅读器 | 阅读器 | 阅读器右侧 | 0 | 0 | - | 54 | 26 |
| 14370 | rdify_ainvest_reader_reader_switchToAILayout | 元素埋点 | Readify_Ainvest_阅读器_阅读器_切换成AI排版 | ainvest | 阅读器 | 阅读器 | 切换成AI排版 | 0 | 0 | - | 14 | 9 |
| 14381 | rdify_ainvest_reader_reader_switchToTXT | 元素埋点 | Readify_Ainvest_阅读器_阅读器_切换成TXT | ainvest | 阅读器 | 阅读器 | 切换成TXT | 0 | 0 | - | 11 | 5 |
| 15246 | rdify_ainvest_reader_searchBar_backBtn | 元素埋点 | Readify_Ainvest_阅读器_搜索操作条_返回按钮 | ainvest | 阅读器 | 搜索操作条 | 返回按钮 | 0 | 0 | - | 5 | 3 |
| 15247 | rdify_ainvest_reader_searchBar_continueBtn | 元素埋点 | Readify_Ainvest_阅读器_搜索操作条_继续按钮 | ainvest | 阅读器 | 搜索操作条 | 继续按钮 | 0 | 0 | - | 6 | 2 |
| 15249 | rdify_ainvest_reader_searchBar_next | 元素埋点 | Readify_Ainvest_阅读器_搜索操作条_下一步 | ainvest | 阅读器 | 搜索操作条 | 下一步 | 0 | 0 | - | 6 | 4 |
| 15248 | rdify_ainvest_reader_searchBar_prev | 元素埋点 | Readify_Ainvest_阅读器_搜索操作条_上一个 | ainvest | 阅读器 | 搜索操作条 | 上一个 | 0 | 0 | - | 4 | 4 |
| 15250 | rdify_ainvest_reader_searchBar_stay | 元素埋点 | Readify_Ainvest_阅读器_搜索操作条_停留 | ainvest | 阅读器 | 搜索操作条 | 停留 | 0 | 0 | - | 10 | 5 |
| 14316 | rdify_ainvest_reader_settingsArea_settingsPanel | 元素埋点 | Readify_Ainvest_阅读器_设置区域_阅读设置面板 | ainvest | 阅读器 | 设置区域 | 阅读设置面板 | 5 | 0 | - | 8 | 38 |
| 14763 | rdify_ainvest_reader_shareBook_shareResult | 元素埋点 | Readify_Ainvest_阅读器_分享书籍_分享结果 | ainvest | 阅读器 | 分享书籍 | 分享结果 | 4 | 2 | state, name | 0 | 0 |
| 14317 | rdify_ainvest_reader_speedSetting_speedBtn | 元素埋点 | Readify_Ainvest_阅读器_倍速选择_倍速按钮 | ainvest | 阅读器 | 倍速选择 | 倍速按钮 | 5 | 1 | value | 13 | 36 |
| 14331 | rdify_ainvest_reader_timerDialog_timerDialogPage | 元素埋点 | Readify_Ainvest_阅读器_定时器设置弹窗_定时器弹窗页面 | ainvest | 阅读器 | 定时器设置弹窗 | 定时器弹窗页面 | 5 | 2 | value, dateTime | 14 | 28 |
| 14330 | rdify_ainvest_reader_timerDialog_timerSwitch | 元素埋点 | Readify_Ainvest_阅读器_定时器设置弹窗_定时器开关 | ainvest | 阅读器 | 定时器设置弹窗 | 定时器开关 | 0 | 0 | - | 10 | 4 |
| 14674 | rdify_ainvest_reader_topBar_aiLayout | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_AI排版 | ainvest | 阅读器 | app顶部栏 | AI排版 | 4 | 0 | - | 11 | 20 |
| 14296 | rdify_ainvest_reader_topBar_contents | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_目录 | ainvest | 阅读器 | app顶部栏 | 目录 | 0 | 0 | - | 46 | 20 |
| 14286 | rdify_ainvest_reader_topBar_fontSettingBtn | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_字体设置按钮 | ainvest | 阅读器 | app顶部栏 | 字体设置按钮 | 0 | 0 | - | 40 | 15 |
| 14287 | rdify_ainvest_reader_topBar_moreBtn | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_更多按钮 | ainvest | 阅读器 | app顶部栏 | 更多按钮 | 0 | 0 | - | 52 | 44 |
| 14337 | rdify_ainvest_reader_topBar_savebutton | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_保存按钮 | ainvest | 阅读器 | app顶部栏 | 保存按钮 | 0 | 0 | - | 1 | 10 |
| 14669 | rdify_ainvest_reader_topBar_switchToEPUB | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_PDF转EPUB | ainvest | 阅读器 | app顶部栏 | PDF转EPUB | 4 | 0 | - | 8 | 10 |
| 14356 | rdify_ainvest_reader_topBar_switchToEbookBtn | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_切换到电子书按钮 | ainvest | 阅读器 | app顶部栏 | 切换到电子书按钮 | 0 | 0 | - | 12 | 11 |
| 14380 | rdify_ainvest_reader_topBar_switchToPDF | 元素埋点 | Readify_Ainvest_阅读器_app顶部栏_切换到PDF | ainvest | 阅读器 | app顶部栏 | 切换到PDF | 0 | 0 | - | 13 | 3 |
| 15675 | rdify_ainvest_reader_trans_playBtn | 元素埋点 | Readify_Ainvest_阅读器_翻译_朗读播放按钮 | ainvest | 阅读器 | 翻译 | 朗读播放按钮 | 0 | 0 | - | 2 | 5 |
| 15676 | rdify_ainvest_reader_trans_transPopupSwipeUp | 元素埋点 | Readify_Ainvest_阅读器_翻译_翻译弹窗上滑展开 | ainvest | 阅读器 | 翻译 | 翻译弹窗上滑展开 | 1 | 0 | - | 2 | 6 |
| 14258 | rdify_ainvest_readingNotesList | 页面埋点 | Readify_Ainvest_阅读笔记列表页 | ainvest | 阅读笔记列表页 | - | - | 2 | 0 | - | 1 | 12 |
| 14257 | rdify_ainvest_readingNotesList_bookList_bookCard | 元素埋点 | Readify_Ainvest_阅读笔记列表页_书籍列表区_书籍卡片 | ainvest | 阅读笔记列表页 | 书籍列表区 | 书籍卡片 | 0 | 0 | - | 1 | 4 |
| 14627 | rdify_ainvest_voiceCloneSave | 页面埋点 | Readify_Ainvest_音色克隆保存页 | ainvest | 音色克隆保存页 | - | - | 2 | 0 | - | 0 | 0 |
| 14626 | rdify_ainvest_voiceCloneSave_creatVoice_saveButton | 元素埋点 | Readify_Ainvest_音色克隆保存页_音色克隆_保存按钮 | ainvest | 音色克隆保存页 | 音色克隆 | 保存按钮 | 0 | 2 | name, type | 0 | 0 |
| 14625 | rdify_ainvest_voiceCloneSave_creatVoice_voicePlayBtn | 元素埋点 | Readify_Ainvest_音色克隆保存页_音色克隆_音色试听播放按钮 | ainvest | 音色克隆保存页 | 音色克隆 | 音色试听播放按钮 | 0 | 0 | - | 0 | 0 |
| 14617 | rdify_ainvest_voiceCloneGuide | 页面埋点 | Readify_Ainvest_音色克隆引导页 | ainvest | 音色克隆引导页 | - | - | 2 | 0 | - | 0 | 0 |
| 14616 | rdify_ainvest_voiceCloneGuide_bottomActionBar_startRecordBtn | 元素埋点 | Readify_Ainvest_音色克隆引导页_底部操作栏_开始录制按钮 | ainvest | 音色克隆引导页 | 底部操作栏 | 开始录制按钮 | 0 | 0 | - | 0 | 0 |
| 14628 | rdify_ainvest_voiceCloneGuide_bottomBar_reRecordBtn | 元素埋点 | Readify_Ainvest_音色克隆引导页_底部操作栏_重新录制按钮 | ainvest | 音色克隆引导页 | 底部操作栏 | 重新录制按钮 | 0 | 0 | - | 0 | 0 |
| 14631 | rdify_ainvest_voiceCloneGuide_bottomBar_startRecordBtn | 元素埋点 | Readify_Ainvest_音色克隆引导页_底部操作栏_开始录制按钮 | ainvest | 音色克隆引导页 | 底部操作栏 | 开始录制按钮 | 0 | 1 | language | 0 | 0 |
| 14629 | rdify_ainvest_voiceCloneGuide_bottomBar_submitRecordBtn | 元素埋点 | Readify_Ainvest_音色克隆引导页_底部操作栏_提交录制按钮 | ainvest | 音色克隆引导页 | 底部操作栏 | 提交录制按钮 | 0 | 1 | type | 0 | 0 |
| 14630 | rdify_ainvest_voiceCloneGuide_contentArea_audioPlayBtn | 元素埋点 | Readify_Ainvest_音色克隆引导页_内容区域_录音播放按钮 | ainvest | 音色克隆引导页 | 内容区域 | 录音播放按钮 | 0 | 0 | - | 0 | 0 |
| 14632 | rdify_ainvest_voiceCloneGuide_loadanima_cloning | 元素埋点 | Readify_Ainvest_音色克隆引导页_加载动画_克隆中动画 | ainvest | 音色克隆引导页 | 加载动画 | 克隆中动画 | 2,0 | 0 | - | 0 | 0 |
| 14329 | rdify_ainvest_voice | 页面埋点 | Readify_Ainvest_音色选择 | ainvest | 音色选择 | - | - | 2 | 0 | - | 30 | 25 |
| 14614 | rdify_ainvest_voice_creatVoice_add | 元素埋点 | Readify_Ainvest_音色选择_音色克隆_添加 | ainvest | 音色选择 | 音色克隆 | 添加 | 0 | 1 | from | 0 | 0 |
| 14623 | rdify_ainvest_voice_creatVoice_recordAudioBtn | 元素埋点 | Readify_Ainvest_音色选择_音色克隆_录制音频按钮 | ainvest | 音色选择 | 音色克隆 | 录制音频按钮 | 0 | 0 | - | 0 | 0 |
| 14624 | rdify_ainvest_voice_creatVoice_uploadAudioBtn | 元素埋点 | Readify_Ainvest_音色选择_音色克隆_上传音频按钮 | ainvest | 音色选择 | 音色克隆 | 上传音频按钮 | 0 | 0 | - | 0 | 0 |
| 14635 | rdify_ainvest_voice_editVoice_confirmDeleteBtn | 元素埋点 | Readify_Ainvest_音色选择_音色编辑_确认删除按钮 | ainvest | 音色选择 | 音色编辑 | 确认删除按钮 | 0 | 0 | - | 0 | 0 |
| 14634 | rdify_ainvest_voice_editVoice_deleteBtn | 元素埋点 | Readify_Ainvest_音色选择_音色编辑_删除按钮 | ainvest | 音色选择 | 音色编辑 | 删除按钮 | 0 | 0 | - | 0 | 0 |
| 14633 | rdify_ainvest_voice_editVoice_editVoiceBtn | 元素埋点 | Readify_Ainvest_音色选择_音色编辑_编辑音色按钮 | ainvest | 音色选择 | 音色编辑 | 编辑音色按钮 | 0 | 0 | - | 0 | 0 |
| 14326 | rdify_ainvest_voice_voiceSelect_languageSelector | 元素埋点 | Readify_Ainvest_音色选择_声音选择_语言选择器 | ainvest | 音色选择 | 声音选择 | 语言选择器 | 0 | 0 | - | 13 | 18 |
| 14328 | rdify_ainvest_voice_voiceSelect_offlineTypeTab | 元素埋点 | Readify_Ainvest_音色选择_声音选择_Offline类型标签 | ainvest | 音色选择 | 声音选择 | Offline类型标签 | 0 | 0 | - | 14 | 19 |
| 14325 | rdify_ainvest_voice_voiceSelect_proTypeTab | 元素埋点 | Readify_Ainvest_音色选择_声音选择_Pro类型标签 | ainvest | 音色选择 | 声音选择 | Pro类型标签 | 0 | 0 | - | 28 | 21 |
| 14327 | rdify_ainvest_voice_voiceSelect_reset | 元素埋点 | Readify_Ainvest_音色选择_声音选择_重置 | ainvest | 音色选择 | 声音选择 | 重置 | 0 | 0 | - | 12 | 19 |
| 14324 | rdify_ainvest_voice_voiceSelect_voiceCardList | 元素埋点 | Readify_Ainvest_音色选择_声音选择_音色卡片列表 | ainvest | 音色选择 | 声音选择 | 音色卡片列表 | 0,2 | 3 | name, language, type | 18 | 35 |
| 14229 | rdify_ainvest_readifyHome | 页面埋点 | Readify_Ainvest_首页 | ainvest | 首页 | - | - | 2,end,8 | 5 | type, regisId, num, state, dateTime | 118 | 113 |
| 14877 | rdify_ainvest_readifyHome_MoreActions_collectionBtn | 元素埋点 | Readify_Ainvest_首页_更多操作_分类按钮 | ainvest | 首页 | 更多操作 | 分类按钮 | 0 | 0 | - | 0 | 0 |
| 14876 | rdify_ainvest_readifyHome_MoreActions_modeswitch | 元素埋点 | Readify_Ainvest_首页_更多操作_视图切换 | ainvest | 首页 | 更多操作 | 视图切换 | 0 | 0 | - | 0 | 0 |
| 14875 | rdify_ainvest_readifyHome_MoreActions_selectButton | 元素埋点 | Readify_Ainvest_首页_更多操作_选择按钮 | ainvest | 首页 | 更多操作 | 选择按钮 | 0 | 1 | name | 0 | 0 |
| 14228 | rdify_ainvest_readifyHome_bookList_bookCard | 元素埋点 | Readify_Ainvest_首页_书籍列表区_书籍卡片 | ainvest | 首页 | 书籍列表区 | 书籍卡片 | 0,9 | 2 | itemId, title | 26 | 23 |
| 14864 | rdify_ainvest_readifyHome_bookList_collectionCard | 元素埋点 | Readify_Ainvest_首页_书籍列表区_分类卡片 | ainvest | 首页 | 书籍列表区 | 分类卡片 | 0,9 | 2 | itemId, title | 0 | 0 |
| 14868 | rdify_ainvest_readifyHome_bookList_deletedly | 元素埋点 | Readify_Ainvest_首页_书籍列表区_删除成功 | ainvest | 首页 | 书籍列表区 | 删除成功 | 4 | 3 | num, type, name | 0 | 0 |
| 14230 | rdify_ainvest_readifyHome_bookList_importBtn | 元素埋点 | Readify_Ainvest_首页_书籍列表区_导入按钮 | ainvest | 首页 | 书籍列表区 | 导入按钮 | 0 | 0 | - | 22 | 25 |
| 14382 | rdify_ainvest_readifyHome_bookList_saveToLib | 元素埋点 | Readify_Ainvest_首页_书籍列表区_保存到书架 | ainvest | 首页 | 书籍列表区 | 保存到书架 | 4 | 4 | name, type, content, from | 26 | 34 |
| 14890 | rdify_ainvest_readifyHome_bookList_select | 元素埋点 | Readify_Ainvest_首页_书籍列表区_选择 | ainvest | 首页 | 书籍列表区 | 选择 | 0 | 2 | name, direct | 0 | 0 |
| 14259 | rdify_ainvest_readifyHome_bottomBar_webUrlCopy | 元素埋点 | Readify_Ainvest_首页_底部操作栏_Web应用URL复制 | ainvest | 首页 | 底部操作栏 | Web应用URL复制 | 0 | 0 | - | 6 | 2 |
| 14869 | rdify_ainvest_readifyHome_collectionPanel_collectionBtn | 元素埋点 | Readify_Ainvest_首页_分类面板_分类按钮 | ainvest | 首页 | 分类面板 | 分类按钮 | 0 | 1 | name | 0 | 0 |
| 14902 | rdify_ainvest_readifyHome_collectionPanel_confirmbutton | 元素埋点 | Readify_Ainvest_首页_分类面板_确定按钮 | ainvest | 首页 | 分类面板 | 确定按钮 | 0 | 1 | name | 0 | 0 |
| 14870 | rdify_ainvest_readifyHome_collectionPanel_createButton | 元素埋点 | Readify_Ainvest_首页_分类面板_创建按钮 | ainvest | 首页 | 分类面板 | 创建按钮 | 0 | 0 | - | 0 | 0 |
| 14900 | rdify_ainvest_readifyHome_collectionPanel_quickpanel | 元素埋点 | Readify_Ainvest_首页_分类面板_快捷面板 | ainvest | 首页 | 分类面板 | 快捷面板 | 2,5 | 0 | - | 0 | 0 |
| 14256 | rdify_ainvest_readifyHome_deleteConfirmDialog_confirmDeleteBtn | 元素埋点 | Readify_Ainvest_首页_删除确认弹窗_确认删除按钮 | ainvest | 首页 | 删除确认弹窗 | 确认删除按钮 | 0 | 2 | num, type | 2 | 11 |
| 14898 | rdify_ainvest_readifyHome_deleteconfirm_check | 元素埋点 | Readify_Ainvest_首页_删除二次确认_勾选 | ainvest | 首页 | 删除二次确认 | 勾选 | 0 | 1 | direct | 0 | 0 |
| 14899 | rdify_ainvest_readifyHome_deleteconfirm_deleteBtn | 元素埋点 | Readify_Ainvest_首页_删除二次确认_删除按钮 | ainvest | 首页 | 删除二次确认 | 删除按钮 | 0 | 1 | name | 0 | 0 |
| 14897 | rdify_ainvest_readifyHome_deleteconfirm_deleteDialogTitle | 元素埋点 | Readify_Ainvest_首页_删除二次确认_删除弹窗标题 | ainvest | 首页 | 删除二次确认 | 删除弹窗标题 | 2,5 | 0 | - | 0 | 0 |
| 15723 | rdify_ainvest_readifyHome_homepage_librarySearch | 元素埋点 | Readify_Ainvest_首页_首页_搜索按钮点击 | ainvest | 首页 | 首页 | 搜索按钮点击 | 0 | 0 | - | 9 | 3 |
| 14248 | rdify_ainvest_readifyHome_libraryToolbar_cancelBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_取消按钮 | ainvest | 首页 | 图书馆工具栏 | 取消按钮 | 0 | 0 | - | 13 | 13 |
| 14867 | rdify_ainvest_readifyHome_libraryToolbar_collectionBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_分类按钮 | ainvest | 首页 | 图书馆工具栏 | 分类按钮 | 0 | 1 | num | 0 | 0 |
| 14251 | rdify_ainvest_readifyHome_libraryToolbar_deleteBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_删除按钮 | ainvest | 首页 | 图书馆工具栏 | 删除按钮 | 0 | 1 | type | 9 | 12 |
| 14250 | rdify_ainvest_readifyHome_libraryToolbar_exportBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_导出按钮 | ainvest | 首页 | 图书馆工具栏 | 导出按钮 | 0 | 0 | - | 0 | 0 |
| 15721 | rdify_ainvest_readifyHome_libraryToolbar_librarypin | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_置顶按钮 | ainvest | 首页 | 图书馆工具栏 | 置顶按钮 | 0 | 0 | - | 5 | 4 |
| 15722 | rdify_ainvest_readifyHome_libraryToolbar_libraryunpin | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_取消置顶点击 | ainvest | 首页 | 图书馆工具栏 | 取消置顶点击 | 0 | 0 | - | 3 | 5 |
| 14249 | rdify_ainvest_readifyHome_libraryToolbar_renameBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_重命名按钮 | ainvest | 首页 | 图书馆工具栏 | 重命名按钮 | 0 | 1 | type | 4 | 6 |
| 14226 | rdify_ainvest_readifyHome_libraryToolbar_selectButton | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_选择按钮 | ainvest | 首页 | 图书馆工具栏 | 选择按钮 | 0 | 0 | - | 9 | 9 |
| 14760 | rdify_ainvest_readifyHome_libraryToolbar_shareBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_分享按钮 | ainvest | 首页 | 图书馆工具栏 | 分享按钮 | 0 | 0 | - | 0 | 0 |
| 14227 | rdify_ainvest_readifyHome_libraryToolbar_viewSwitchBtn | 元素埋点 | Readify_Ainvest_首页_图书馆工具栏_视图切换按钮 | ainvest | 首页 | 图书馆工具栏 | 视图切换按钮 | 0 | 1 | name | 16 | 15 |
| 14908 | rdify_ainvest_readifyHome_navigation_hometab | 元素埋点 | Readify_Ainvest_首页_导航栏_首页tab | ainvest | 首页 | 导航栏 | 首页tab | 0 | 0 | - | 0 | 0 |
| 14252 | rdify_ainvest_readifyHome_popup_close | 元素埋点 | Readify_Ainvest_首页_弹窗_关闭 | ainvest | 首页 | 弹窗 | 关闭 | 0 | 0 | - | 3 | 10 |
| 14253 | rdify_ainvest_readifyHome_popup_findBooksBtn | 元素埋点 | Readify_Ainvest_首页_弹窗_查找书籍按钮 | ainvest | 首页 | 弹窗 | 查找书籍按钮 | 0 | 0 | - | 3 | 14 |
| 14254 | rdify_ainvest_readifyHome_popup_importFromFilesBtn | 元素埋点 | Readify_Ainvest_首页_弹窗_从文件导入按钮 | ainvest | 首页 | 弹窗 | 从文件导入按钮 | 0 | 0 | - | 8 | 15 |
| 14255 | rdify_ainvest_readifyHome_popup_importPcBtn | 元素埋点 | Readify_Ainvest_首页_弹窗_从电脑导入按钮 | ainvest | 首页 | 弹窗 | 从电脑导入按钮 | 0 | 0 | - | 2 | 3 |
| 14318 | rdify_ainvest_readifyHome_popup_save | 元素埋点 | Readify_Ainvest_首页_弹窗_保存 | ainvest | 首页 | 弹窗 | 保存 | 0 | 2 | name, title | 3 | 5 |
| 14225 | rdify_ainvest_readifyHome_searchArea_searchInput | 元素埋点 | Readify_Ainvest_首页_搜索区域_搜索框 | ainvest | 首页 | 搜索区域 | 搜索框 | 0 | 0 | - | 11 | 3 |
| 14761 | rdify_ainvest_readifyHome_shareBook_shareResult | 元素埋点 | Readify_Ainvest_首页_分享书籍_分享结果 | ainvest | 首页 | 分享书籍 | 分享结果 | 4 | 2 | state, name | 0 | 0 |
| 15720 | rdify_ainvest_readifyHome_sortfilter_elementClick | 元素埋点 | Readify_Ainvest_首页_排序筛选_元素点击 | ainvest | 首页 | 排序筛选 | 元素点击 | 0 | 1 | state | 6 | 7 |
| 14865 | rdify_ainvest_readifyHome_titleBar_moreBtn | 元素埋点 | Readify_Ainvest_首页_顶部标题栏_更多按钮 | ainvest | 首页 | 顶部标题栏 | 更多按钮 | 0 | 0 | - | 0 | 0 |
| 14224 | rdify_ainvest_readifyHome_topBar_profileBtn | 元素埋点 | Readify_Ainvest_首页_app顶部栏_个人中心按钮 | ainvest | 首页 | app顶部栏 | 个人中心按钮 | 0 | 0 | - | 18 | 4 |
| 14358 | rdify_rdify_reader | 页面埋点 | Readify_rdify_阅读器 | rdify | 阅读器 | - | - | 2 | 0 | - | 19 | 16 |
| 14361 | rdify_rdify_reader_aiOptimizationDialog_start | 元素埋点 | Readify_rdify_阅读器_AI排版优化弹窗_开始 | rdify | 阅读器 | AI排版优化弹窗 | 开始 | 0 | 0 | - | 2 | 15 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### rdify_ainvest_askAI_aiChatArea_stopAiBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问题原文，如果是针对段落的，用{问题};{引用内容}的格式 | string | 0 |

### rdify_ainvest_askAI_aiInputArea_sendQuestionBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问题原文，如果是针对段落的，用{问题};{引用内容}的格式 | string | 0 |
| 描述活动id名称 | activityId | 上报这个问题的id | string | 0 |
| 功能类型 | function | 普通问答：normal 深度研读：deepRead | string | 0 |

### rdify_ainvest_askAI_deepRead_deepRead

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 只在首次开启深度研读上报该事件 转换成功：succeeded 失败：failed | enum | 4 |

### rdify_ainvest_readifyProfile_actionArea_submitBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的反馈问题内容 | string | 0 |
| 用户完成注册后，标识用户的id | regisId | 用户输入的联系邮箱(可选) | string | 0 |

### rdify_ainvest_webNotes_bookList_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 点击的书籍ID | string | 0 |
| 标题 | title | 书籍标题名称 | string | 0 |

### rdify_ainvest_webMyVoice_topBar_createVoiceBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | 创建音色的入口来源（myVoice/Reader） | string | 0 |

### rdify_ainvest_webFindBooks_bookList_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 上报用户点击列表里的第几本书 | int | 0 |
| 类型 | type | search_type 'precise''ai_search"上报搜索类型 | string | 0 |

### rdify_ainvest_webFindBooks_historyArea_historyItem

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的历史搜索标签文案 | string | 0 |

### rdify_ainvest_webFindBooks_searchArea_searchBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的搜索关键词内容 | string | 0 |
| 类型 | type | search_type 'precise''ai_search"上报搜索类型 | string | 0 |

### rdify_ainvest_webAccountSetting_accountSetting_languageDropdown

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 语言 | language | 用户选择的语言选项（中文/英文） | string | 0 |

### rdify_ainvest_webAccountSetting_accountSetting_themeToggleBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 模式 | mode | 选择的主题模式（light/dark/auto） | string | 0 |

### rdify_ainvest_webReader

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报时间，精确到分钟，格式格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 2 |

### rdify_ainvest_webReader_aiInputArea_sendQuestionBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问题原文，如果是针对段落的，用{问题};{引用内容}的格式 | string | 0 |
| 描述活动id名称 | activityId | 上报这个问题的id | string | 0 |

### rdify_ainvest_webReader_aotuSkip_closeBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 注意点击关闭按钮和点击空白弹窗都会消失 任意一个开启就是：on 全关就是：off | enum | 5 |

### rdify_ainvest_webReader_contentBar_readBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 事件开始时间，格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 0 |

### rdify_ainvest_webReader_feedbackModalBar_confirmbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 用户选择的错误类型：mispronunciation(多音字/书名错误)、omission(语言/措辞)、intonation(语气/节奏不对)、mechanical_noise(机械音等)、other_issues(其他问题) | string | 0 |

### rdify_ainvest_webReader_floatActionBar_askAI

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户请求AI分析的文本内容 | string | 0 |

### rdify_ainvest_webReader_floatActionBar_searchBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户选中搜索的文本内容 | string | 0 |

### rdify_ainvest_webReader_menu_searchInput

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的搜索关键词 | string | 0 |

### rdify_ainvest_webReader_playControl_pause

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 听书开始的时间，不是点击返回的时间，当地手机事件 | string | 0 |
| 停留时长 | stayLen | 触发： 暂停、结束播放模式、数据播放完时上报（关闭听书模式/书架x掉播放条、换一本书进行播放） 统计逻辑： 1. 听书模式下，播放器在播放状态的时长统计 2. 要定时在本地更新累计的时长数据，包含开始时间，如果意外杀死退出，要在下次打开app时补充上报） 3. 暂停时不计算时间，计算真实听书时长，无视倍速。 | int | 0 |

### rdify_ainvest_webReader_speedSetting_speedBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 数值 | value | 倍速调节完成后，关闭弹窗时上报用户选择的倍速值，如1.0、1.2、1.5、2.0、3.0。不区分用户时怎么设置的，只关注结果 | string | 5 |

### rdify_ainvest_webReader_themeSetting_changeTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 有修改主题：changed 无修改：noChange | enum | 5 |

### rdify_ainvest_webReader_titleBar_shareBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | succeed (生成分享链接), restricted (敏感文件无法分享), uploadFailed (上传失败), canceled (处理过程中停止) | enum | 4 |
| 名称 | name | 上报书籍名称，无论是否分享成功 | string | 4 |

### rdify_ainvest_webReader_topBar_backBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 阅读时长累计上报 | int | 0 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报时的当地时间 | string | 0 |

### rdify_ainvest_webReader_voiceSelect_voiceCardList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 音色名称 | string | 0 |
| 语言 | language | 音色语言（如：CN、EN等） | string | 0 |

### rdify_ainvest_webHome

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | guest（游客用户） free（普通登录用户） vvip（VVIP） | string | 2 |
| 用户完成注册后，标识用户的id | regisId | 上报用户邮箱 | string | 2 |
| 标记列表行数 | num | 22 上报用户书架书籍数量 触发：每次启动App时上报 参数：个人文件数量 | int | 2 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 记录用户启动app的时间，记录手机时间，格式：2026-01-19T07:30Z | string | 8 |

### rdify_ainvest_webHome_MoreActions_deleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | normal（正常文件）、waiting（等待上传）、importing（正在上传）、failed（上传失败） | enum | 0 |

### rdify_ainvest_webHome_MoreActions_shareBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | succeed (生成分享链接), restricted (敏感文件无法分享), uploadFailed (上传失败), canceled (处理过程中停止) | enum | 4 |
| 名称 | name | 上报书籍名称，无论是否分享成功 | string | 4 |

### rdify_ainvest_webHome_bookList_bookShared

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | suceed (全部接收成功), partSucceed (部分接收成功), failed(接收失败) | enum | 4 |
| 名称 | name | 上报接收的全部接收成功的书籍名称 | string | 4 |

### rdify_ainvest_webHome_bookList_saveToLib

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 导入的书籍名称。注意，所有导入书籍到书架，都报到这个埋点事件。 - 本地文件导入 - 网络搜书导入 - 从云盘导入 | string | 4 |
| 类型 | type | 书籍类型format（txt/pdf/epub/mobi/azw/docx）原始格式，不是转码后的 | string | 4 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 书籍具体大小，单位M，保留两位小数 | string | 4 |

### rdify_ainvest_webHome_bottomBar_shareBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | succeed (生成分享链接), partSucceed (部分文件分享成功), Restricted (全部文件敏感无法分享), uploadFailed (全部文件上传失败), canceled (处理过程中停止) | enum | 4 |
| 名称 | name | 上报全部书籍名称，无论是否分享成功 | string | 4 |

### rdify_ainvest_webHome_contentArea_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 书籍ID | string | 0 |
| 标题 | title | 书籍标题 | string | 0 |

### rdify_ainvest_webHome_deleteConfirmDialog_confirmDeleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 被删除的书籍数量 | int | 0 |

### rdify_ainvest_webHome_filterArea_fileTypeDropdown

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 选中的文件类型：全部/PDF/EPUB/网页 | string | 0 |

### rdify_ainvest_webHome_filterArea_sortDropdown

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 表示增序降序等 | order | 选中的排序方式：添加时间/更新时间/按字母排序 | string | 0 |

### rdify_ainvest_webHome_renameDialog_confirmbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 书籍的新名称（用户输入的新书名） | string | 0 |
| 标题 | title | 原书名 | string | 0 |

### rdify_ainvest_webHome_userFeedback_submitBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的内容 | string | 0 |
| 用户完成注册后，标识用户的id | regisId | 用户邮箱，如果有的话 | string | 0 |

### rdify_ainvest_searchInBook_searchArea_searchInput

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录用户关键词，触发时机和生成历史记录一样。要么用户手动点击搜索，要么点击了列表中的结果，只上报实际搜索关键词。 | string | 0 |

### rdify_ainvest_bookSearchResult_bookList_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 上报用户点击列表里的第几本书 | int | 0 |

### rdify_ainvest_findBooksPage_searchArea_searchInput

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的搜索关键词 | string | 0 |

### rdify_ainvest_findBooksPage_searchArea_searchSubmitBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 提交搜索时输入框中的内容 | string | 0 |
| 类型 | type | search_type 'precise''ai_search"上报搜索类型 | string | 0 |

### rdify_ainvest_collectionList_MoreActions_viewSwitchBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 切换后的视图模式名称（grid/list） | string | 0 |

### rdify_ainvest_collectionList_bookList_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 点击/长按的书籍唯一标识 | string | 0,9 |
| 标题 | title | 点击/长按的书籍名称 | string | 0,9 |

### rdify_ainvest_collectionList_bookList_select

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 选中/取消选中的书籍名称 | string | 0 |
| 方向 | direct | select或Deselect | string | 0 |

### rdify_ainvest_collectionList_collectionPanel_collectionBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 点击的分类名称（包括：移出当前分类） | string | 0 |

### rdify_ainvest_collectionList_collectionPanel_confirmbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 确定移入的分类名称（包括：移出当前分组） | string | 0 |

### rdify_ainvest_collectionList_deleteconfirm_check

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 方向 | direct | Check或Uncheck | string | 0 |

### rdify_ainvest_collectionList_deleteconfirm_deleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 确认删除的全部书籍名称 | string | 0 |

### rdify_ainvest_collectionList_shareBook_shareResult

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | succeed：生成分享链接 partSucceed：部分文件分享成功 uploadFailed：全部文件上传失败 canceled：处理过程中停止 | enum | 4 |
| 名称 | name | 上报全部书籍名称，无论是否分享成功 | string | 4 |

### rdify_ainvest_findBook_searchArea_stop

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 当前搜索框中的内容（如：西游记） | string | 0 |

### rdify_ainvest_newHome_bookList_bookList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 点击的书籍名称 | string | 0 |
| 可点击的菜单表头名称 | tab | 显示的是哪个tab下的列表 | string | 2 |

### rdify_ainvest_newHome_bookList_tabs

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | tab名称 | string | 0 |

### rdify_ainvest_loginPage_IOSlog_loginBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 登录方式类型，值为"apple" | string | 0 |

### rdify_ainvest_loginPage_login_thirdPartyLogin

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 登录状态 | loginStatus | 登录成功或失败的状态标识 login_status（success/faild​） | string | 0 |
| 类型 | type | 登录方式类型，取值为apple或google，用于区分用户选择的第三方登录渠道 login_type（google/apple） | string | 0 |

### rdify_ainvest_reader

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 模式 | mode | 上报旁白是否开启voiceover：open/close | string | 2 |
| 名称 | name | 上报书籍名称，最长30个字符 | string | 2 |
| 语言 | language | 上报书籍语言 | string | 2 |
| 功能类型 | function | ui_mode：阅读还是听书模式：listening_mode/read_mode | string | 2 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报进入时间。格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 2 |

### rdify_ainvest_reader_bottomPlayerBar_pause

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 听书开始的时间，不是点击返回的时间，格式调整为：格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 0 |
| 停留时长 | stayLen | 触发： 暂停、结束播放模式、数据播放完时上报（关闭听书模式/书架x掉播放条、换一本书进行播放） 统计逻辑： 1. 听书模式下，播放器在播放状态的时长统计 2. 要定时在本地更新累计的时长数据，包含开始时间，如果意外杀死退出，要在下次打开app时补充上报） 3. 暂停时不计算时间，计算真实听书时长，无视倍速。 | int | 0 |

### rdify_ainvest_reader_drawtoolbar_askAI

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户选中的文本内容 | string | 0 |

### rdify_ainvest_reader_feedbackModalBar_confirmBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 用户选择的错误类型：mispronunciation(多音字/书名错误)、omission(语言/措辞)、intonation(语气/节奏不对)、mechanical_noise(机械音等)、other_issues(其他问题) | string | 0 |

### rdify_ainvest_reader_menucard_backBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 阅读时长累计上报 | int | 0 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报时的当地时间 | string | 0 |
| 模式 | mode | 阅读还是听书模式：listening_mode/read_mode | string | 0 |

### rdify_ainvest_reader_readerMenu_translateBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 起始状态 | startStatus | 源语言，即书籍语言 | - | 0 |
| 终点状态 | endStatus | 翻译的目标语言，当前是系统语言 | - | - |

### rdify_ainvest_reader_reader_backBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回来源 | source | 触发返回的来源位置：bookmark-书签跳转、catalog-目录跳转、note-划线笔记跳转 | string | 0 |

### rdify_ainvest_reader_reader_play

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报开始时间，格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 4 |

### rdify_ainvest_reader_shareBook_shareResult

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | "result: succeed (生成分享链接), partSucceed (部分文件分享成功), Restricted (全部文件敏感无法分享), uploadFailed (全部文件上传失败), canceled (处理过程中停止) name: 上报全部书籍名称，无论是否分享成功" | enum | 4 |
| 名称 | name | name: 上报书籍名称，无论是否分享成功" | string | 4 |

### rdify_ainvest_reader_speedSetting_speedBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 数值 | value | 倍速调节完成后，关闭弹窗时上报用户选择的倍速值，如1.0、1.2、1.5、2.0、3.0。不区分用户时怎么设置的，只关注结果 | string | 5 |

### rdify_ainvest_reader_timerDialog_timerDialogPage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 数值 | value | 用户设置的定时时长（分钟）。在关闭弹窗时上报，如果未设置或关闭定时器则上报0。 | string | 5 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 设置时，当前的时间格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 5 |

### rdify_ainvest_voiceCloneSave_creatVoice_saveButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 保存的音色名称 | string | 0 |
| 类型 | type | 使用的头像是默认的还是上传的 默认的：default 上传的：upload | string | 0 |

### rdify_ainvest_voiceCloneGuide_bottomBar_startRecordBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 语言 | language | 上报用户选择的语言名称 | string | 0 |

### rdify_ainvest_voiceCloneGuide_bottomBar_submitRecordBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 是从哪里来的： 录制：record 上传音频：upload | string | 0 |

### rdify_ainvest_voice_creatVoice_add

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | 我的音色：myvoice 音色选择列表；voice | string | 0 |

### rdify_ainvest_voice_voiceSelect_voiceCardList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 用户选择的音色名字（如：华祺、晚吟、疏影等） | string | 0 |
| 语言 | language | 音色语言（如：CN、EN等） | string | 0 |
| 类型 | type | 音色类型：Pro（大模型音色）或Offline（内置音色） | string | 0 |

### rdify_ainvest_readifyHome

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | guest（游客用户） free（普通登录用户） vvip（VVIP） | string | 2 |
| 用户完成注册后，标识用户的id | regisId | 上报用户邮箱 | string | 2 |
| 标记列表行数 | num | 22 上报用户书架书籍数量 触发：每次启动App时上报 参数：个人文件数量 | int | 2 |
| 状态 | state | 是否开启无障碍：voiceoveropen/voiceoverclose | enum | 2 |
| 返回日期。粒度为日，示例20220102；粒度为周20200101-20200107；粒度为月，示例202001 | dateTime | 上报应用启动时的具体时间，格式模板： YYYY-MM-DDTHH:mm:ss.SSS±HH:mm 具体示例： 2024-05-20T15:30:00.123+08:00 字段拆解说明： YYYY-MM-DD : 日期 T : 分隔符 (固定字符) HH:mm:ss.SSS : 用户当地时间 (24小时制，保留毫秒) +08:00 : 时区偏移 (关键点：请传用户当前时区 | string | 8 |

### rdify_ainvest_readifyHome_MoreActions_selectButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 切换后的视图模式名称（grid/list） | string | 0 |

### rdify_ainvest_readifyHome_bookList_bookCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 点击/长按的书籍唯一标识ID | string | 0,9 |
| 标题 | title | 点击/长按的书籍名称 | string | 0,9 |

### rdify_ainvest_readifyHome_bookList_collectionCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 点击或长按的分组id | string | 0,9 |
| 标题 | title | 点击或长按的分类名称 | string | 0,9 |

### rdify_ainvest_readifyHome_bookList_deletedly

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 删除的书籍数量 | int | 4 |
| 类型 | type | book：删除的全部是书籍 collection：删除的全部是分类 mix：删除包含书籍和分类 | string | 4 |
| 名称 | name | 上报全部被删除的书籍名称（不用上报分类名称） | string | 4 |

### rdify_ainvest_readifyHome_bookList_saveToLib

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 导入的书籍名称。注意，所有导入书籍到书架，都报到这个埋点事件。 - 本地文件导入 - 网络搜书导入 - 从app打开导入 | string | 4 |
| 类型 | type | 书籍类型format（txt/pdf/epub/mobi/azw/docx）原始格式，不是转码后的 | string | 4 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 书籍具体大小，单位M，保留两位小数 | string | 4 |
| 入口 | from | 导入的书籍来源： - file：本地文件 - search：网络搜书 - classics：公版书库 - shared：从他人的分享导入 - external：用readify打开的外部app的文件 | string | 4 |

### rdify_ainvest_readifyHome_bookList_select

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 选择/取消选择的书籍或分类名称 | string | 0 |
| 方向 | direct | select或Deselect | string | 0 |

### rdify_ainvest_readifyHome_collectionPanel_collectionBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 选中的分类名称 | string | 0 |

### rdify_ainvest_readifyHome_collectionPanel_confirmbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 确定移入的分类名称 | string | 0 |

### rdify_ainvest_readifyHome_deleteConfirmDialog_confirmDeleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 被删除的书籍数量 | int | 0 |
| 类型 | type | book: 删除的都是书籍 collection：删除的都是分类 mix：删除的有书籍也有分类 | string | 0 |

### rdify_ainvest_readifyHome_deleteconfirm_check

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 方向 | direct | check或uncheck | string | 0 |

### rdify_ainvest_readifyHome_deleteconfirm_deleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 被删除的全部书名 | string | 0 |

### rdify_ainvest_readifyHome_libraryToolbar_collectionBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 选择的书籍数量 | int | 0 |

### rdify_ainvest_readifyHome_libraryToolbar_deleteBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | book：全部是书籍 collection：全部是分类 mix：分类和书籍都有 | string | 0 |

### rdify_ainvest_readifyHome_libraryToolbar_renameBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | book: 重命名一本书 collection：重命名一个分类 | string | 0 |

### rdify_ainvest_readifyHome_libraryToolbar_viewSwitchBtn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 切换后的视图模式名称（grid/list） | string | 0 |

### rdify_ainvest_readifyHome_popup_save

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 名称 | name | 书籍的新名称（用户输入的新书名） | string | 0 |
| 标题 | title | 原书名 | object | 0 |

### rdify_ainvest_readifyHome_shareBook_shareResult

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | "result: succeed (生成分享链接), partSucceed (部分文件分享成功), Restricted (全部文件敏感无法分享), uploadFailed (全部文件上传失败), canceled (处理过程中停止) | enum | 4 |
| 名称 | name | name: 上报全部书籍名称，无论是否分享成功" | string | 4 |

### rdify_ainvest_readifyHome_sortfilter_elementClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 点的哪个就记录哪个 | enum | 0 |
