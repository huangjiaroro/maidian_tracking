---
title: 应用 - aime
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - aime
  - ainvest
---

# aime

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 23 |
| appSign | aime |
| appKey | b2d05b899f |
| creator | huangjiarong@myhexin.com |
| createTime | 2026-04-28 15:03:26 |
| topicName | spider-ainvest |
| payloadStatus | 0 |
| pageCount(snapshot) | 23 |
| trackCount(snapshot) | 414 |
| relationTrackCount | 127 |
| tracksWithActionFields | 270 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| aime | 21 | 407 |
| iwc | 1 | 6 |
| web | 1 | 1 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1383 | aime | AIME | 3 | 5 |
| 459 | canvas | Aime可视化看板 | 0 | 0 |
| 460 | canvas | Aime可视化看板 | 2 | 14 |
| 394 | explore | Aime广场 | 14 | 54 |
| 409 | webexplore | Aime网页发现广场 | 5 | 16 |
| 439 | aimeApp | aimeapp | 10 | 19 |
| 276 | aimetalk | aime对话页 | 95 | 165 |
| 278 | chatTheme | aime形象设置 | 0 | 5 |
| 377 | aimemix | aime无处不在 | 4 | 1 |
| 362 | aimeweb | aime网页对话 | 15 | 33 |
| 277 | robotCenter | 个人中心 | 2 | 6 |
| 395 | landingpage | 产品落地页 | 8 | 9 |
| 463 | roleplay | 人设对话 | 6 | 11 |
| 1439 | importBook | 前往电脑版导入书籍 | 0 | 0 |
| 1087 | quickpanel | 快捷面板 | 6 | 8 |
| 532 | AgentStore | 智能体商店 | 7 | 22 |
| 1524 | hotpredictions | 热点预测 | 2 | 2 |
| 1565 | socialLandingPage | 社媒爆款落地页 | 2 | 2 |
| 533 | webagentstore | 网页智能体商店 | 6 | 18 |
| 1321 | memory | 记忆落地页 | 4 | 7 |
| 489 | multimodal | 语音助手多模态 | 2 | 5 |
| 1513 | voice | 语音选择广场 | 2 | 4 |
| 1278 | screenerPage | 选股落地页 | 0 | 7 |

## 关系枢纽埋点

| trackKey | 应用 | 页面 | 区块 | 元素 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- |
| aime_aime_aimetalk_inputBox_input | aime | aime对话页 | 对话输入框(inputBox) | 输入框 | 44 | 34 |
| aime_aime_aimetalk | aime | aime对话页 | - | - | 61 | 14 |
| aime_aime_aimetalk_aiChatArea_leaveTalk | aime | aime对话页 | AI对话区域 | 离开对话 | 21 | 48 |
| aime_aime_aimetalk_bottomQuickInput_bottomButton | aime | aime对话页 | 底部快捷输入 | 底部按钮 | 32 | 27 |
| aime_aime_aimetalk_tkPanel_traceability | aime | aime对话页 | 对话界面 | 点击文字溯源 | 27 | 30 |
| aime_aime_aimetalk_list_slide | aime | aime对话页 | 列表 | 滑动 | 23 | 33 |
| aime_aime_aimetalk_tkPanel_ansBubble | aime | aime对话页 | 对话界面 | 机器人答案气泡 | 31 | 22 |
| aime_aime_aimetalk_tkPanel_share | aime | aime对话页 | 对话界面 | 分享 | 8 | 43 |
| aime_aime_aimetalk_activeRecom_tkPanel | aime | aime对话页 | 主动式问句推荐 | 问句推荐 | 19 | 27 |
| aime_aime_aimetalk_inputBox_openVoice | aime | aime对话页 | 对话输入框(inputBox) | 开启语音播报 | 27 | 19 |
| aime_aime_aimetalk_lpFb_feedback | aime | aime对话页 | 长按反馈页 | 意见反馈 | 22 | 23 |
| aime_aime_aimetalk_tkPanel_userQue | aime | aime对话页 | 对话界面 | 用户对话气泡 | 27 | 18 |
| aime_aime_aimetalk_aimetoainvestnews_gomore | aime | aime对话页 | 主动对话跳咨询 | 跳转更多 | 17 | 27 |
| aime_aime_aimetalk_inputMenu_open | aime | aime对话页 | 加号面板 | 打开 | 23 | 16 |
| aime_aime_aimetalk_feedback_up | aime | aime对话页 | 意见反馈 | 点赞 | 31 | 6 |
| aime_aime_aimetalk_morefunction_voice | aime | aime对话页 | 更多功能 | 语音 | 17 | 18 |
| aime_aime_aimetalk_activepage_insightNewsQuery | aime | aime对话页 | 主动式页卡 | 新闻问句主动式 | 13 | 21 |
| aime_aime_aimetalk_inputMenu_close | aime | aime对话页 | 加号面板 | 关闭 | 14 | 17 |
| aime_aime_aimetalk_modelSwitch_buttons | aime | aime对话页 | 模型切换按钮 | 按钮 | 18 | 13 |
| aime_aime_aimetalk_activepage_polling | aime | aime对话页 | 主动式页卡 | 投票组件 | 10 | 18 |
| aime_aime_aimetalk_inputBox_sendQuery | aime | aime对话页 | 对话输入框(inputBox) | 发送问句 | 17 | 9 |
| aime_aime_aimeweb_sharePage_recommendation | aime | aime网页对话 | Aime分享页面 | 推荐模块 | 10 | 16 |
| aime_aime_aime_voiceInputEverywhere_longPressinput | aime | AIME | 无处不在语音输入 | 长按输入 | 3 | 19 |
| aime_aime_aimetalk_more_aimequestion | aime | aime对话页 | more浮框 | aime问句 | 7 | 15 |
| aime_aime_aimetalk_more_explore | aime | aime对话页 | more浮框 | explore | 16 | 6 |
| aime_aime_aime_voiceInput_longPressinput | aime | AIME | 语音输入 | 长按输入 | 4 | 17 |
| aime_aime_aimetalk_explore_foruCard | aime | aime对话页 | 探索 | foru卡片 | 10 | 10 |
| aime_aime_aimetalk_tkPanel_intradayChart | aime | aime对话页 | 对话界面 | 跳转分时 | 11 | 8 |
| aime_aime_aime_voiceInput_cancelSending | aime | AIME | 语音输入 | 取消发送 | 4 | 14 |
| aime_aime_aimetalk_skillpopup_skillchoosed | aime | aime对话页 | skill显示框 | skill | 5 | 13 |

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13168 | aime_aime_aimePortconbottom_touchConsent | 元素埋点 | aime_Ainvest Aime_影子账户确认按钮_点击确认 | aime | - | 影子账户确认按钮 | 点击确认 | 0 | 2 | logmap, tab | 0 | 0 |
| 13896 | aime_aime_aime_voiceInputEverywhere_clickToenter | 元素埋点 | aime_Ainvest Aime_AIME_无处不在语音输入_点击输入 | aime | AIME | 无处不在语音输入 | 点击输入 | 0 | 0 | - | 0 | 10 |
| 13895 | aime_aime_aime_voiceInputEverywhere_longPressinput | 元素埋点 | aime_Ainvest Aime_AIME_无处不在语音输入_长按输入 | aime | AIME | 无处不在语音输入 | 长按输入 | 9 | 0 | - | 3 | 19 |
| 13877 | aime_aime_aime_voiceInput_cancelSending | 元素埋点 | aime_Ainvest Aime_AIME_语音输入_取消发送 | aime | AIME | 语音输入 | 取消发送 | 0,1 | 0 | - | 4 | 14 |
| 13898 | aime_aime_aime_voiceInput_clickToenter | 元素埋点 | aime_Ainvest Aime_AIME_语音输入_点击输入 | aime | AIME | 语音输入 | 点击输入 | 0 | 0 | - | 3 | 14 |
| 13897 | aime_aime_aime_voiceInput_longPressinput | 元素埋点 | aime_Ainvest Aime_AIME_语音输入_长按输入 | aime | AIME | 语音输入 | 长按输入 | 9 | 0 | - | 4 | 17 |
| 5064 | aime_aime_canvas | 页面埋点 | aime_Ainvest Aime_Aime可视化看板 | aime | Aime可视化看板 | - | - | 0,2,1 | 1 | from | 0 | 0 |
| 5065 | aime_aime_canvas_creat_confirm | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_生成看板_确认 | aime | Aime可视化看板 | 生成看板 | 确认 | 0,1,2 | 1 | from | 0 | 0 |
| 5068 | aime_aime_canvas_creat_shuffle | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_生成看板_随机生成 | aime | Aime可视化看板 | 生成看板 | 随机生成 | 0,1,2 | 0 | - | 0 | 0 |
| 5075 | aime_aime_canvas_detail_create | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_新增 | aime | Aime可视化看板 | detail | 新增 | 0,1,2 | 1 | stayLen | 0 | 0 |
| 5070 | aime_aime_canvas_detail_creatownsize | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_用户自定义尺寸 | aime | Aime可视化看板 | detail | 用户自定义尺寸 | 0,1,2 | 0 | - | 0 | 0 |
| 5077 | aime_aime_canvas_detail_delete | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_删除 | aime | Aime可视化看板 | detail | 删除 | 0,1,2 | 0 | - | 0 | 0 |
| 5076 | aime_aime_canvas_detail_editQues | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_编辑问题 | aime | Aime可视化看板 | detail | 编辑问题 | 0,1,2 | 0 | - | 0 | 0 |
| 5072 | aime_aime_canvas_detail_ownchart | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_用户自定义图标 | aime | Aime可视化看板 | detail | 用户自定义图标 | 0,1,2 | 0 | - | 0 | 0 |
| 5074 | aime_aime_canvas_detail_shuffle | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_随机生成 | aime | Aime可视化看板 | detail | 随机生成 | 0,1,2 | 0 | - | 0 | 0 |
| 5073 | aime_aime_canvas_detail_systemchart | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_系统推荐图表 | aime | Aime可视化看板 | detail | 系统推荐图表 | 0,1,2 | 0 | - | 0 | 0 |
| 5071 | aime_aime_canvas_detail_systemsize | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_detail_系统尺寸 | aime | Aime可视化看板 | detail | 系统尺寸 | 0,1,2 | 0 | - | 0 | 0 |
| 5069 | aime_aime_canvas_list_delete | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_列表_删除 | aime | Aime可视化看板 | 列表 | 删除 | 0,1,2 | 0 | - | 0 | 0 |
| 5067 | aime_aime_canvas_list_detail | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_列表_详情 | aime | Aime可视化看板 | 列表 | 详情 | 0,1,2 | 1 | stayLen | 0 | 0 |
| 5066 | aime_aime_canvas_navigation_create | 元素埋点 | aime_Ainvest Aime_Aime可视化看板_导航栏_新增 | aime | Aime可视化看板 | 导航栏 | 新增 | 0,1,2 | 2 | from, stayLen | 0 | 0 |
| 4159 | aime_aime_explore | 页面埋点 | aime_Ainvest Aime_Aime广场 | aime | Aime广场 | - | - | 0,1,2,4 | 1 | sessionId | 1 | 0 |
| 4193 | aime_aime_explore_Aimetab_more | 元素埋点 | aime_Ainvest Aime_Aime广场_Aime顶部tab_更多 | aime | Aime广场 | Aime顶部tab | 更多 | 0 | 1 | sessionId | 0 | 0 |
| 4160 | aime_aime_explore_Aimetab_tabcontent | 元素埋点 | aime_Ainvest Aime_Aime广场_Aime顶部tab_tab选项 | aime | Aime广场 | Aime顶部tab | tab选项 | 0,1,2,4 | 3 | stayLen, sessionId, content | 0 | 0 |
| 10340 | aime_aime_explore_agent_agent | 元素埋点 | aime_Ainvest Aime_Aime广场_智能体_智能体 | aime | Aime广场 | 智能体 | 智能体 | 0 | 0 | - | 0 | 0 |
| 4171 | aime_aime_explore_clickShared_askTopic | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_聊同款话题按钮 | aime | Aime广场 | 查看他人分享 | 聊同款话题按钮 | 0,2 | 2 | sessionId, content | 0 | 0 |
| 4200 | aime_aime_explore_clickShared_cancelUp | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_取消点赞 | aime | Aime广场 | 查看他人分享 | 取消点赞 | 0 | 2 | sessionId, content | 0 | 0 |
| 4177 | aime_aime_explore_clickShared_closebutton | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_关闭按钮 | aime | Aime广场 | 查看他人分享 | 关闭按钮 | 0 | 1 | sessionId | 0 | 0 |
| 4168 | aime_aime_explore_clickShared_content | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_内容 | aime | Aime广场 | 查看他人分享 | 内容 | 1,2,4 | 2 | sessionId, content | 0 | 0 |
| 4176 | aime_aime_explore_clickShared_portfolioshare | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_分享 | aime | Aime广场 | 查看他人分享 | 分享 | 0 | 2 | content, sessionId | 0 | 0 |
| 4175 | aime_aime_explore_clickShared_up | 元素埋点 | aime_Ainvest Aime_Aime广场_查看他人分享_点赞 | aime | Aime广场 | 查看他人分享 | 点赞 | 0 | 2 | sessionId, content | 0 | 0 |
| 10342 | aime_aime_explore_community_community | 元素埋点 | aime_Ainvest Aime_Aime广场_社区_社区 | aime | Aime广场 | 社区 | 社区 | 0 | 0 | - | 8 | 2 |
| 4166 | aime_aime_explore_contest_askquestions | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_提问 | aime | Aime广场 | 比赛 | 提问 | 0 | 1 | sessionId | 0 | 0 |
| 4173 | aime_aime_explore_contest_latest | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_最新榜 | aime | Aime广场 | 比赛 | 最新榜 | 0 | 1 | sessionId | 0 | 0 |
| 4167 | aime_aime_explore_contest_lottery | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_抽奖 | aime | Aime广场 | 比赛 | 抽奖 | 0 | 1 | sessionId | 0 | 0 |
| 4165 | aime_aime_explore_contest_more | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_更多 | aime | Aime广场 | 比赛 | 更多 | 0 | 1 | sessionId | 0 | 0 |
| 4170 | aime_aime_explore_contest_mostLikes | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_点赞榜 | aime | Aime广场 | 比赛 | 点赞榜 | 0 | 1 | sessionId | 0 | 0 |
| 4169 | aime_aime_explore_contest_mostShares | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_分享榜 | aime | Aime广场 | 比赛 | 分享榜 | 0 | 1 | sessionId | 0 | 0 |
| 4172 | aime_aime_explore_contest_myPrompt | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_我的比赛分享 | aime | Aime广场 | 比赛 | 我的比赛分享 | 0 | 1 | sessionId | 0 | 0 |
| 4181 | aime_aime_explore_contest_queryList | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_排行榜问句 | aime | Aime广场 | 比赛 | 排行榜问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4183 | aime_aime_explore_contest_share | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_分享 | aime | Aime广场 | 比赛 | 分享 | 0,2 | 3 | sessionId, type, content | 0 | 0 |
| 4182 | aime_aime_explore_contest_up | 元素埋点 | aime_Ainvest Aime_Aime广场_比赛_点赞 | aime | Aime广场 | 比赛 | 点赞 | 0 | 3 | sessionId, content, type | 0 | 0 |
| 4158 | aime_aime_explore_exploreTab_contests | 元素埋点 | aime_Ainvest Aime_Aime广场_广场的业务分类_比赛 | aime | Aime广场 | 广场的业务分类 | 比赛 | 2,0 | 0 | - | 0 | 0 |
| 5513 | aime_aime_explore_exploreTab_switch | 元素埋点 | aime_Ainvest Aime_Aime广场_广场的业务分类_切换 | aime | Aime广场 | 广场的业务分类 | 切换 | 0 | 5 | state, sessionId, from, source, tab | 0 | 0 |
| 4161 | aime_aime_explore_exploreTab_tabcontent | 元素埋点 | aime_Ainvest Aime_Aime广场_广场的业务分类_tab选项 | aime | Aime广场 | 广场的业务分类 | tab选项 | 0,1,2,4 | 3 | sessionId, content, stayLen | 6 | 10 |
| 15303 | aime_aime_explore_explore_foruCard | 元素埋点 | aime_Ainvest Aime_Aime广场_探索_foru卡片 | aime | Aime广场 | 探索 | foru卡片 | 2,0 | 2 | state, recInfo | 0 | 0 |
| 4184 | aime_aime_explore_explorecategories_myFav | 元素埋点 | aime_Ainvest Aime_Aime广场_explore下的各类tab_我的收藏 | aime | Aime广场 | explore下的各类tab | 我的收藏 | 0 | 1 | sessionId | 2 | 2 |
| 4179 | aime_aime_explore_inputBox_input | 元素埋点 | aime_Ainvest Aime_Aime广场_对话输入框(inputBox)_输入框 | aime | Aime广场 | 对话输入框(inputBox) | 输入框 | 0 | 2 | sessionId, content | 0 | 0 |
| 4180 | aime_aime_explore_inputBox_sendQuery | 元素埋点 | aime_Ainvest Aime_Aime广场_对话输入框(inputBox)_发送问句 | aime | Aime广场 | 对话输入框(inputBox) | 发送问句 | 0 | 3 | type, content, sessionId | 0 | 0 |
| 4194 | aime_aime_explore_morefunction_AimeProfile | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_aime形象1 | aime | Aime广场 | 更多功能 | aime形象1 | 0 | 1 | sessionId | 0 | 0 |
| 4198 | aime_aime_explore_morefunction_allsetting | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_全部设置 | aime | Aime广场 | 更多功能 | 全部设置 | 0 | 1 | sessionId | 0 | 0 |
| 4195 | aime_aime_explore_morefunction_broadcast | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_语音播报 | aime | Aime广场 | 更多功能 | 语音播报 | 0 | 2 | sessionId, type | 0 | 0 |
| 4163 | aime_aime_explore_morefunction_category | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_类别 | aime | Aime广场 | 更多功能 | 类别 | 0 | 0 | - | 0 | 0 |
| 4197 | aime_aime_explore_morefunction_feedback | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_意见反馈 | aime | Aime广场 | 更多功能 | 意见反馈 | 0 | 1 | sessionId | 0 | 0 |
| 4196 | aime_aime_explore_morefunction_livsupport | 元素埋点 | aime_Ainvest Aime_Aime广场_更多功能_人工客服 | aime | Aime广场 | 更多功能 | 人工客服 | 0 | 1 | sessionId | 0 | 0 |
| 10341 | aime_aime_explore_my_my | 元素埋点 | aime_Ainvest Aime_Aime广场_我的_我的 | aime | Aime广场 | 我的 | 我的 | 0 | 0 | - | 7 | 5 |
| 4185 | aime_aime_explore_myfavor_collectQue | 元素埋点 | aime_Ainvest Aime_Aime广场_我的收藏_收藏问句 | aime | Aime广场 | 我的收藏 | 收藏问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4186 | aime_aime_explore_myfavor_disCollect | 元素埋点 | aime_Ainvest Aime_Aime广场_我的收藏_取消收藏问句 | aime | Aime广场 | 我的收藏 | 取消收藏问句 | 0 | 1 | sessionId | 0 | 0 |
| 5531 | aime_aime_explore_pushShare_askquestions | 元素埋点 | aime_Ainvest Aime_Aime广场_Push后的分享浮窗_提问 | aime | Aime广场 | Push后的分享浮窗 | 提问 | 0 | 4 | pushId, content, from, source | 0 | 0 |
| 5526 | aime_aime_explore_pushShare_collectQue | 元素埋点 | aime_Ainvest Aime_Aime广场_Push后的分享浮窗_收藏问句 | aime | Aime广场 | Push后的分享浮窗 | 收藏问句 | 0 | 4 | pushId, content, from, source | 0 | 0 |
| 5528 | aime_aime_explore_pushShare_share | 元素埋点 | aime_Ainvest Aime_Aime广场_Push后的分享浮窗_分享 | aime | Aime广场 | Push后的分享浮窗 | 分享 | 0 | 4 | pushId, content, from, source | 0 | 0 |
| 5524 | aime_aime_explore_pushShare_up | 元素埋点 | aime_Ainvest Aime_Aime广场_Push后的分享浮窗_点赞 | aime | Aime广场 | Push后的分享浮窗 | 点赞 | 0 | 4 | pushId, content, from, source | 0 | 0 |
| 5508 | aime_aime_explore_queryDetail_askquestions | 元素埋点 | aime_Ainvest Aime_Aime广场_分享问句详情_提问 | aime | Aime广场 | 分享问句详情 | 提问 | 0 | 5 | session_id, content, from, source, tab | 0 | 0 |
| 5516 | aime_aime_explore_queryDetail_collectQue | 元素埋点 | aime_Ainvest Aime_Aime广场_分享问句详情_收藏问句 | aime | Aime广场 | 分享问句详情 | 收藏问句 | 0 | 5 | content, sessionId, from, source, tab | 0 | 2 |
| 5518 | aime_aime_explore_queryDetail_share | 元素埋点 | aime_Ainvest Aime_Aime广场_分享问句详情_分享 | aime | Aime广场 | 分享问句详情 | 分享 | 0 | 5 | content, sessionId, from, source, tab | 0 | 0 |
| 5514 | aime_aime_explore_queryDetail_up | 元素埋点 | aime_Ainvest Aime_Aime广场_分享问句详情_点赞 | aime | Aime广场 | 分享问句详情 | 点赞 | 0 | 5 | content, sessionId, from, source, tab | 0 | 0 |
| 5520 | aime_aime_explore_queryDetails_clickShared | 元素埋点 | aime_Ainvest Aime_Aime广场_问句详情_点击分享 | aime | Aime广场 | 问句详情 | 点击分享 | 0 | 5 | content, sessionId, from, source, tab | 0 | 0 |
| 4174 | aime_aime_explore_queryList_collectQue | 元素埋点 | aime_Ainvest Aime_Aime广场_问句区域_收藏问句 | aime | Aime广场 | 问句区域 | 收藏问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4199 | aime_aime_explore_queryList_disCollect | 元素埋点 | aime_Ainvest Aime_Aime广场_问句区域_取消收藏问句 | aime | Aime广场 | 问句区域 | 取消收藏问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4164 | aime_aime_explore_queryList_queryCard | 元素埋点 | aime_Ainvest Aime_Aime广场_问句区域_问句卡片 | aime | Aime广场 | 问句区域 | 问句卡片 | 0 | 2 | sessionId, content | 0 | 0 |
| 4190 | aime_aime_explore_share_sharecancel | 元素埋点 | aime_Ainvest Aime_Aime广场_分享_取消分享 | aime | Aime广场 | 分享 | 取消分享 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4178 | aime_aime_explore_share_shareface | 元素埋点 | aime_Ainvest Aime_Aime广场_分享_分享渠道Facebook | aime | Aime广场 | 分享 | 分享渠道Facebook | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4189 | aime_aime_explore_share_sharelink | 元素埋点 | aime_Ainvest Aime_Aime广场_分享_分享link | aime | Aime广场 | 分享 | 分享link | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4187 | aime_aime_explore_share_sharetwitter | 元素埋点 | aime_Ainvest Aime_Aime广场_分享_分享渠道推特 | aime | Aime广场 | 分享 | 分享渠道推特 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4188 | aime_aime_explore_share_whatsApp | 元素埋点 | aime_Ainvest Aime_Aime广场_分享_whatsApp | aime | Aime广场 | 分享 | whatsApp | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4400 | aime_aime_webexplore | 页面埋点 | aime_Ainvest Aime_Aime网页发现广场 | aime | Aime网页发现广场 | - | - | 0,1,2,4,3 | 2 | sessionId, content | 0 | 0 |
| 4417 | aime_aime_webexplore_clickShared_askTopic | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_查看他人分享_聊同款话题按钮 | aime | Aime网页发现广场 | 查看他人分享 | 聊同款话题按钮 | 0,2 | 2 | sessionId, content | 0 | 0 |
| 4415 | aime_aime_webexplore_clickShared_portfolioshare | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_查看他人分享_分享 | aime | Aime网页发现广场 | 查看他人分享 | 分享 | 0 | 2 | content, sessionId | 0 | 0 |
| 4416 | aime_aime_webexplore_clickShared_up | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_查看他人分享_点赞 | aime | Aime网页发现广场 | 查看他人分享 | 点赞 | 0 | 2 | sessionId, content | 0 | 0 |
| 4408 | aime_aime_webexplore_contest_askquestions | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_提问 | aime | Aime网页发现广场 | 比赛 | 提问 | 0 | 1 | sessionId | 0 | 0 |
| 4411 | aime_aime_webexplore_contest_latest | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_最新榜 | aime | Aime网页发现广场 | 比赛 | 最新榜 | 0 | 1 | sessionId | 0 | 0 |
| 4409 | aime_aime_webexplore_contest_mostLikes | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_点赞榜 | aime | Aime网页发现广场 | 比赛 | 点赞榜 | 0 | 1 | sessionId | 0 | 0 |
| 4410 | aime_aime_webexplore_contest_mostShares | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_分享榜 | aime | Aime网页发现广场 | 比赛 | 分享榜 | 0 | 1 | sessionId | 0 | 0 |
| 4412 | aime_aime_webexplore_contest_myPrompt | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_我的比赛分享 | aime | Aime网页发现广场 | 比赛 | 我的比赛分享 | 0 | 1 | sessionId | 0 | 0 |
| 4413 | aime_aime_webexplore_contest_queryList | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_排行榜问句 | aime | Aime网页发现广场 | 比赛 | 排行榜问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4407 | aime_aime_webexplore_contest_share | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_分享 | aime | Aime网页发现广场 | 比赛 | 分享 | 0,2 | 3 | session_id, type, content | 0 | 0 |
| 4414 | aime_aime_webexplore_contest_up | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_比赛_点赞 | aime | Aime网页发现广场 | 比赛 | 点赞 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4401 | aime_aime_webexplore_exploreTab_tabcontent | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_广场的业务分类_tab选项 | aime | Aime网页发现广场 | 广场的业务分类 | tab选项 | 0,1,2,3,4 | 3 | sessionId, content, stayLen | 0 | 0 |
| 4403 | aime_aime_webexplore_queryList_collectQue | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_问句区域_收藏问句 | aime | Aime网页发现广场 | 问句区域 | 收藏问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4404 | aime_aime_webexplore_queryList_disCollect | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_问句区域_取消收藏问句 | aime | Aime网页发现广场 | 问句区域 | 取消收藏问句 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 4402 | aime_aime_webexplore_queryList_queryCard | 元素埋点 | aime_Ainvest Aime_Aime网页发现广场_问句区域_问句卡片 | aime | Aime网页发现广场 | 问句区域 | 问句卡片 | 0 | 2 | sessionId, content | 0 | 0 |
| 4768 | aime_aime_aimeApp | 页面埋点 | aime_Ainvest Aime_aimeapp | aime | aimeapp | - | - | 2 | 0 | - | 0 | 0 |
| 4750 | aime_aime_aimeApp_Aimetab_userCenter | 元素埋点 | aime_Ainvest Aime_aimeapp_Aime顶部tab_个人中心 | aime | aimeapp | Aime顶部tab | 个人中心 | 0 | 1 | sessionId | 0 | 0 |
| 4751 | aime_aime_aimeApp_Googlelog_googLogIn | 元素埋点 | aime_Ainvest Aime_aimeapp_Google登录_谷歌登录 | aime | aimeapp | Google登录 | 谷歌登录 | 0 | 1 | sessionId | 0 | 0 |
| 4752 | aime_aime_aimeApp_IOSlog_appleLogIn | 元素埋点 | aime_Ainvest Aime_aimeapp_IOS登录_苹果ID登录 | aime | aimeapp | IOS登录 | 苹果ID登录 | 0 | 1 | sessionId | 0 | 0 |
| 4753 | aime_aime_aimeApp_LS_emaPhone | 元素埋点 | aime_Ainvest Aime_aimeapp_注册登录_邮箱/手机号登录 | aime | aimeapp | 注册登录 | 邮箱/手机号登录 | 0 | 1 | session_id | 0 | 0 |
| 4764 | aime_aime_aimeApp_emaiCreate_continue | 元素埋点 | aime_Ainvest Aime_aimeapp_邮箱注册_continue | aime | aimeapp | 邮箱注册 | continue | 0 | 1 | sessionId | 0 | 0 |
| 4761 | aime_aime_aimeApp_emailSignin_continue | 元素埋点 | aime_Ainvest Aime_aimeapp_邮箱登录_continue | aime | aimeapp | 邮箱登录 | continue | 0 | 0 | - | 0 | 0 |
| 4766 | aime_aime_aimeApp_emailSignin_continueLogin | 元素埋点 | aime_Ainvest Aime_aimeapp_邮箱登录_确认登录 | aime | aimeapp | 邮箱登录 | 确认登录 | 0 | 1 | sessionId | 0 | 0 |
| 4767 | aime_aime_aimeApp_emailSignin_forPass | 元素埋点 | aime_Ainvest Aime_aimeapp_邮箱登录_forgetPassword | aime | aimeapp | 邮箱登录 | forgetPassword | 0 | 1 | sessionId | 0 | 0 |
| 4760 | aime_aime_aimeApp_emailSignin_phoneSin | 元素埋点 | aime_Ainvest Aime_aimeapp_邮箱登录_phoneSignin | aime | aimeapp | 邮箱登录 | phoneSignin | 0 | 1 | sessionId | 0 | 0 |
| 4756 | aime_aime_aimeApp_phoneSignin_continue | 元素埋点 | aime_Ainvest Aime_aimeapp_手机登录_continue | aime | aimeapp | 手机登录 | continue | 0 | 1 | sessionId | 0 | 0 |
| 4757 | aime_aime_aimeApp_phoneSignin_emailSin | 元素埋点 | aime_Ainvest Aime_aimeapp_手机登录_emailSignin | aime | aimeapp | 手机登录 | emailSignin | 0 | 1 | sessionId | 0 | 0 |
| 4748 | aime_aime_aimeApp_rbtCen_ads | 元素埋点 | aime_Ainvest Aime_aimeapp_aime个人中心_运营位 | aime | aimeapp | aime个人中心 | 运营位 | 0,2 | 2 | sessionId, content | 0 | 0 |
| 4746 | aime_aime_aimeApp_rbtCen_changePic | 元素埋点 | aime_Ainvest Aime_aimeapp_aime个人中心_上传头像 | aime | aimeapp | aime个人中心 | 上传头像 | 0 | 1 | sessionId | 0 | 0 |
| 4747 | aime_aime_aimeApp_rbtCen_editName | 元素埋点 | aime_Ainvest Aime_aimeapp_aime个人中心_编辑名字 | aime | aimeapp | aime个人中心 | 编辑名字 | 0 | 1 | sessionId | 0 | 0 |
| 4749 | aime_aime_aimeApp_rbtCen_tabcontent | 元素埋点 | aime_Ainvest Aime_aimeapp_aime个人中心_tab选项 | aime | aimeapp | aime个人中心 | tab选项 | 0 | 2 | sessionId, content | 0 | 0 |
| 4755 | aime_aime_aimeApp_setting_logout | 元素埋点 | aime_Ainvest Aime_aimeapp_设置_登出客户端 | aime | aimeapp | 设置 | 登出客户端 | 0 | 1 | sessionId | 0 | 0 |
| 4754 | aime_aime_aimeApp_setting_tabcontent | 元素埋点 | aime_Ainvest Aime_aimeapp_设置_tab选项 | aime | aimeapp | 设置 | tab选项 | 0,2 | 2 | content, sessionId | 0 | 0 |
| 4762 | aime_aime_aimeApp_sms_inputBox | 元素埋点 | aime_Ainvest Aime_aimeapp_验证码登录_输入框 | aime | aimeapp | 验证码登录 | 输入框 | 1,0 | 1 | sessionId | 0 | 0 |
| 2303 | aime_aime_aimetalk | 页面埋点 | aime_Ainvest Aime_aime对话页 | aime | aime对话页 | - | - | 4,1,2,8 | 2 | sessionId, stayLen | 61 | 14 |
| 14076 | aime_aime_aimetalk_2025yearSummary_clickInteract | 元素埋点 | aime_Ainvest Aime_aime对话页_2025年年度总结_点击互动 | aime | aime对话页 | 2025年年度总结 | 点击互动 | 0 | 0 | - | 0 | 0 |
| 14087 | aime_aime_aimetalk_2025yearSummary_communityforum | 元素埋点 | aime_Ainvest Aime_aime对话页_2025年年度总结_社区卡片 | aime | aime对话页 | 2025年年度总结 | 社区卡片 | 0,2 | 0 | - | 0 | 0 |
| 14075 | aime_aime_aimetalk_2025yearSummary_finishseen | 元素埋点 | aime_Ainvest Aime_aime对话页_2025年年度总结_详情页完播 | aime | aime对话页 | 2025年年度总结 | 详情页完播 | 2 | 0 | - | 0 | 0 |
| 14074 | aime_aime_aimetalk_2025yearSummary_transferTodetails | 元素埋点 | aime_Ainvest Aime_aime对话页_2025年年度总结_跳转详细 | aime | aime对话页 | 2025年年度总结 | 跳转详细 | 0,4 | 0 | - | 0 | 0 |
| 4227 | aime_aime_aimetalk_Aimetab_moreFunction | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime顶部tab_更多功能 | aime | aime对话页 | Aime顶部tab | 更多功能 | 0,2 | 1 | sessionId | 0 | 0 |
| 4592 | aime_aime_aimetalk_DR_link | 元素埋点 | aime_Ainvest Aime_aime对话页_DailyReport_链接 | aime | aime对话页 | DailyReport | 链接 | 0,2 | 1 | source | 0 | 0 |
| 4593 | aime_aime_aimetalk_DR_viewAll | 元素埋点 | aime_Ainvest Aime_aime对话页_DailyReport_viewAll | aime | aime对话页 | DailyReport | viewAll | 0,2 | 4 | source, content, logId, recInfo | 0 | 0 |
| 4203 | aime_aime_aimetalk_Inputlock_Share | 元素埋点 | aime_Ainvest Aime_aime对话页_输入区解锁_按钮 | aime | aime对话页 | 输入区解锁 | 按钮 | 0,2 | 0 | - | 0 | 0 |
| 4204 | aime_aime_aimetalk_Inputlock_upgrade | 元素埋点 | aime_Ainvest Aime_aime对话页_输入区解锁_解锁按钮 | aime | aime对话页 | 输入区解锁 | 解锁按钮 | 0,2 | 1 | itemId | 0 | 0 |
| 4201 | aime_aime_aimetalk_Mulpoint_upgradeaime | 元素埋点 | aime_Ainvest Aime_aime对话页_右上角多功能区_升级AIME | aime | aime对话页 | 右上角多功能区 | 升级AIME | 0,2 | 1 | itemId | 0 | 0 |
| 4202 | aime_aime_aimetalk_Taghint_taghint | 元素埋点 | aime_Ainvest Aime_aime对话页_tag提示_tag提示 | aime | aime对话页 | tag提示 | tag提示 | 0,2 | 1 | itemId | 0 | 0 |
| 11744 | aime_aime_aimetalk_Upgrade_Upgrade | 元素埋点 | aime_Ainvest Aime_aime对话页_升级_升级 | aime | aime对话页 | 升级 | 升级 | 0,2 | 2 | source, from | 0 | 0 |
| 12290 | aime_aime_aimetalk_activeRecom_aimeexplain | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_Aime解读 | aime | aime对话页 | 主动式问句推荐 | Aime解读 | 0,2 | 3 | source, from, logId | 3 | 1 |
| 13649 | aime_aime_aimetalk_activeRecom_backest | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_回测 | aime | aime对话页 | 主动式问句推荐 | 回测 | 2,0 | 0 | - | 0 | 0 |
| 15205 | aime_aime_aimetalk_activeRecom_heatTopic | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_热点专题推荐 | aime | aime对话页 | 主动式问句推荐 | 热点专题推荐 | 0,2 | 2 | tab, source | 1 | 1 |
| 15206 | aime_aime_aimetalk_activeRecom_heatTopicQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_热点专题问句 | aime | aime对话页 | 主动式问句推荐 | 热点专题问句 | 0,2,1 | 6 | recInfo, content, tab, source, num +1 | 2 | 2 |
| 15752 | aime_aime_aimetalk_activeRecom_insightWatchlistAlrt | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_自选加提醒主动式 | aime | aime对话页 | 主动式问句推荐 | 自选加提醒主动式 | 0,2 | 4 | state, content, recInfo, groupId | 0 | 0 |
| 2698 | aime_aime_aimetalk_activeRecom_tkPanel | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式问句推荐_问句推荐 | aime | aime对话页 | 主动式问句推荐 | 问句推荐 | 2,0 | 12 | num, from, sessionId, stayLen, content +7 | 19 | 27 |
| 9743 | aime_aime_aimetalk_activepage_activequery | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_主动式问句 | aime | aime对话页 | 主动式页卡 | 主动式问句 | 0,2,1 | 4 | content, from, sessionId, source | 0 | 0 |
| 13319 | aime_aime_aimetalk_activepage_afterVotingQueries | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_投票问句推荐 | aime | aime对话页 | 主动式页卡 | 投票问句推荐 | 0,2 | 6 | source, from, content, session_id, logId +1 | 0 | 0 |
| 12289 | aime_aime_aimetalk_activepage_aimeprofile | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_Aime账户 | aime | aime对话页 | 主动式页卡 | Aime账户 | 0,2 | 3 | source, from, logId | 0 | 0 |
| 13536 | aime_aime_aimetalk_activepage_dialoguePure | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_对话 | aime | aime对话页 | 主动式页卡 | 对话 | 2 | 0 | - | 0 | 0 |
| 13533 | aime_aime_aimetalk_activepage_forecast | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_预测 | aime | aime对话页 | 主动式页卡 | 预测 | 2 | 0 | - | 0 | 0 |
| 14664 | aime_aime_aimetalk_activepage_insightForecastQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_预测问句主动式 | aime | aime对话页 | 主动式页卡 | 预测问句主动式 | 0,2 | 1 | recInfo | 10 | 2 |
| 14663 | aime_aime_aimetalk_activepage_insightNewsQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_新闻问句主动式 | aime | aime对话页 | 主动式页卡 | 新闻问句主动式 | 0,2 | 2 | state, recInfo | 13 | 21 |
| 15443 | aime_aime_aimetalk_activepage_insightSwipe | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_滑动主动式 | aime | aime对话页 | 主动式页卡 | 滑动主动式 | 0,1,2 | 4 | state, content, recInfo, source | 5 | 7 |
| 13318 | aime_aime_aimetalk_activepage_polling | 元素埋点 | aime_Ainvest Aime_aime对话页_主动式页卡_投票组件 | aime | aime对话页 | 主动式页卡 | 投票组件 | 0,2 | 6 | source, from, content, session_id, logId +1 | 10 | 18 |
| 2319 | aime_aime_aimetalk_addPanel_queryClick | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_点击问句 | aime | aime对话页 | 加号面板 | 点击问句 | 0,4,2 | 3 | sessionId, content, type | 1 | 3 |
| 15604 | aime_aime_aimetalk_aiChatArea_leaveTalk | 元素埋点 | aime_Ainvest Aime_aime对话页_AI对话区域_离开对话 | aime | aime对话页 | AI对话区域 | 离开对话 | 5,2 | 1 | logId | 21 | 48 |
| 11862 | aime_aime_aimetalk_aimeHome_more | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime首页运营_更多 | aime | aime对话页 | Aime首页运营 | 更多 | 0,2 | 3 | sessionId, source, from | 0 | 0 |
| 11865 | aime_aime_aimetalk_aimeHome_newChat | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime首页运营_新建对话 | aime | aime对话页 | Aime首页运营 | 新建对话 | 0 | 3 | sessionId, from, source | 0 | 0 |
| 11864 | aime_aime_aimetalk_aimeHome_recQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime首页运营_推荐问句 | aime | aime对话页 | Aime首页运营 | 推荐问句 | 0,1,2 | 5 | source, from, sessionId, content, recInfo | 0 | 0 |
| 13156 | aime_aime_aimetalk_aimeMemMsg_cancelbutton | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime记忆消息_取消选项 | aime | aime对话页 | Aime记忆消息 | 取消选项 | 0 | 3 | content, logId, itemId | 0 | 0 |
| 13155 | aime_aime_aimetalk_aimeMemMsg_functioncard | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime记忆消息_功能卡片 | aime | aime对话页 | Aime记忆消息 | 功能卡片 | 2 | 3 | content, logId, itemId | 0 | 1 |
| 13157 | aime_aime_aimetalk_aimeMemMsg_savebutton | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime记忆消息_保存按钮 | aime | aime对话页 | Aime记忆消息 | 保存按钮 | 0 | 0 | - | 1 | 1 |
| 13303 | aime_aime_aimetalk_aimePortCreate_aimePortClik | 元素埋点 | aime_Ainvest Aime_aime对话页_影子账户创建_用户同意点击 | aime | aime对话页 | 影子账户创建 | 用户同意点击 | 0,4 | 0 | - | 0 | 0 |
| 12282 | aime_aime_aimetalk_aimeprofile_adjust | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime账户_调整 | aime | aime对话页 | Aime账户 | 调整 | 0 | 2 | source, from | 3 | 3 |
| 12284 | aime_aime_aimetalk_aimeprofile_livetv | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime账户_二级Tab | aime | aime对话页 | Aime账户 | 二级Tab | 0 | 3 | source, from, content | 3 | 2 |
| 12283 | aime_aime_aimetalk_aimeprofile_tabSwift | 元素埋点 | aime_Ainvest Aime_aime对话页_Aime账户_Tab切换 | aime | aime对话页 | Aime账户 | Tab切换 | 0 | 3 | source, from, content | 3 | 2 |
| 13438 | aime_aime_aimetalk_aimetoainvestnews_gomore | 元素埋点 | aime_Ainvest Aime_aime对话页_主动对话跳咨询_跳转更多 | aime | aime对话页 | 主动对话跳咨询 | 跳转更多 | 0,4 | 0 | - | 17 | 27 |
| 11315 | aime_aime_aimetalk_answer_deepThought | 元素埋点 | aime_Ainvest Aime_aime对话页_答案_深度思考 | aime | aime对话页 | 答案 | 深度思考 | 0,2 | 4 | sessionId, source, from, content | 0 | 0 |
| 12373 | aime_aime_aimetalk_answserQ_expand | 元素埋点 | aime_Ainvest Aime_aime对话页_回答问题_展开 | aime | aime对话页 | 回答问题 | 展开 | 0,2 | 0 | - | 0 | 0 |
| 12258 | aime_aime_aimetalk_answserQ_viewall | 元素埋点 | aime_Ainvest Aime_aime对话页_回答问题_展开 | aime | aime对话页 | 回答问题 | 展开 | 0,2 | 0 | - | 0 | 0 |
| 11050 | aime_aime_aimetalk_bottomQuickInput_bottomButton | 元素埋点 | aime_Ainvest Aime_aime对话页_底部快捷输入_底部按钮 | aime | aime对话页 | 底部快捷输入 | 底部按钮 | 0 | 1 | content | 32 | 27 |
| 11051 | aime_aime_aimetalk_bottomQuickInput_subtab | 元素埋点 | aime_Ainvest Aime_aime对话页_底部快捷输入_子tab | aime | aime对话页 | 底部快捷输入 | 子tab | 0 | 1 | content | 7 | 4 |
| 11453 | aime_aime_aimetalk_bottomQuickInput_unlockPro | 元素埋点 | aime_Ainvest Aime_aime对话页_底部快捷输入_解锁 | aime | aime对话页 | 底部快捷输入 | 解锁 | 0 | 4 | from, source, logId, sessionId | 0 | 0 |
| 15294 | aime_aime_aimetalk_broadcastpodcast_broadcast1 | 元素埋点 | aime_Ainvest Aime_aime对话页_播放卡片_播报 | aime | aime对话页 | 播放卡片 | 播报 | 2,0 | 2 | type, title | 0 | 0 |
| 2314 | aime_aime_aimetalk_collect_collectQue | 元素埋点 | aime_Ainvest Aime_aime对话页_问句收藏_收藏问句 | aime | aime对话页 | 问句收藏 | 收藏问句 | 0 | 5 | sessionId, content, logId, source, from | 5 | 2 |
| 2315 | aime_aime_aimetalk_collect_disCollect | 元素埋点 | aime_Ainvest Aime_aime对话页_问句收藏_取消收藏问句 | aime | aime对话页 | 问句收藏 | 取消收藏问句 | 0 | 2 | sessionId, content | 1 | 0 |
| 2473 | aime_aime_aimetalk_diafufei_unlock | 元素埋点 | aime_Ainvest Aime_aime对话页_对话付费组件_解锁 | aime | aime对话页 | 对话付费组件 | 解锁 | 0,2 | 5 | type, logId, itemId, stayLen, sessionId | 2 | 2 |
| 2474 | aime_aime_aimetalk_diagRe_levelcard | 元素埋点 | aime_Ainvest Aime_aime对话页_对话后付费推荐_等级卡片 | aime | aime对话页 | 对话后付费推荐 | 等级卡片 | 0,2,6 | 4 | type, logId, itemId, sessionId | 2 | 1 |
| 2476 | aime_aime_aimetalk_diagRe_unlock | 元素埋点 | aime_Ainvest Aime_aime对话页_对话后付费推荐_解锁 | aime | aime对话页 | 对话后付费推荐 | 解锁 | 0,2 | 4 | type, logId, itemId, sessionId | 1 | 1 |
| 4205 | aime_aime_aimetalk_diagRe_upgrade | 元素埋点 | aime_Ainvest Aime_aime对话页_对话后付费推荐_解锁按钮 | aime | aime对话页 | 对话后付费推荐 | 解锁按钮 | 0,2 | 1 | itemId | 0 | 0 |
| 15311 | aime_aime_aimetalk_explore_foruCard | 元素埋点 | aime_Ainvest Aime_aime对话页_探索_foru卡片 | aime | aime对话页 | 探索 | foru卡片 | 0,2 | 2 | recInfo, state | 10 | 10 |
| 2321 | aime_aime_aimetalk_fdPanel_cancel | 元素埋点 | aime_Ainvest Aime_aime对话页_反馈详情页_cancel按钮 | aime | aime对话页 | 反馈详情页 | 取消 | 0 | 1 | sessionId | 0 | 0 |
| 2322 | aime_aime_aimetalk_fdPanel_confirm | 元素埋点 | aime_Ainvest Aime_aime对话页_反馈详情页_确认 | aime | aime对话页 | 反馈详情页 | 确认 | 0 | 2 | sessionId, content | 0 | 0 |
| 2323 | aime_aime_aimetalk_fdPanel_fdQues | 元素埋点 | aime_Ainvest Aime_aime对话页_反馈详情页_反馈的问题 | aime | aime对话页 | 反馈详情页 | 反馈的问题 | 0 | 2 | sessionId, content | 0 | 1 |
| 6029 | aime_aime_aimetalk_feedbackDetails_feedbackContent | 元素埋点 | aime_Ainvest Aime_aime对话页_反馈详情_反馈内容 | aime | aime对话页 | 反馈详情 | 反馈内容 | 0 | 7 | content, sessionId, logId, type, from +2 | 0 | 0 |
| 2312 | aime_aime_aimetalk_feedback_down | 元素埋点 | aime_Ainvest Aime_aime对话页_意见反馈_点踩 | aime | aime对话页 | 意见反馈 | 点踩 | 0,2 | 6 | sessionId, content, type, logId, source +1 | 2 | 5 |
| 2313 | aime_aime_aimetalk_feedback_more | 元素埋点 | aime_Ainvest Aime_aime对话页_意见反馈_更多 | aime | aime对话页 | 意见反馈 | 更多 | 0,2 | 3 | sessionId, content, type | 0 | 0 |
| 2310 | aime_aime_aimetalk_feedback_up | 元素埋点 | aime_Ainvest Aime_aime对话页_意见反馈_点赞 | aime | aime对话页 | 意见反馈 | 点赞 | 0,2 | 6 | sessionId, content, type, logId, source +1 | 31 | 6 |
| 12281 | aime_aime_aimetalk_fintuneAime_save | 元素埋点 | aime_Ainvest Aime_aime对话页_定制aime_保存 | aime | aime对话页 | 定制aime | 保存 | 0 | 2 | source, from | 1 | 3 |
| 13532 | aime_aime_aimetalk_forYou_letTalk | 元素埋点 | aime_Ainvest Aime_aime对话页_为你准备_聊一聊 | aime | aime对话页 | 为你准备 | 聊一聊 | 2,0 | 0 | - | 0 | 0 |
| 13439 | aime_aime_aimetalk_forYou_toDialogue | 元素埋点 | aime_Ainvest Aime_aime对话页_为你准备_跳转对话 | aime | aime对话页 | 为你准备 | 跳转对话 | 0,4 | 0 | - | 4 | 7 |
| 2311 | aime_aime_aimetalk_guide_queryClick | 元素埋点 | aime_Ainvest Aime_aime对话页_引导_点击问句 | aime | aime对话页 | 引导 | 点击问句 | 0,1,6 | 3 | type, content, sessionId | 0 | 0 |
| 2318 | aime_aime_aimetalk_history_disCollect | 元素埋点 | aime_Ainvest Aime_aime对话页_historicalPerformance_取消收藏问句 | aime | aime对话页 | historicalPerformance | 取消收藏问句 | 0,1,2,4 | 3 | sessionId, content, type | 0 | 0 |
| 2309 | aime_aime_aimetalk_inputBox_addPanel | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_加号面板 | aime | aime对话页 | 对话输入框(inputBox) | 加号面板 | 0 | 1 | sessionId | 0 | 0 |
| 2327 | aime_aime_aimetalk_inputBox_input | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_输入框 | aime | aime对话页 | 对话输入框(inputBox) | 输入框 | 0 | 1 | sessionId | 44 | 34 |
| 2308 | aime_aime_aimetalk_inputBox_openVoice | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_开启语音播报 | aime | aime对话页 | 对话输入框(inputBox) | 开启语音播报 | 0 | 1 | sessionId | 27 | 19 |
| 2328 | aime_aime_aimetalk_inputBox_sendQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_发送问句 | aime | aime对话页 | 对话输入框(inputBox) | 发送问句 | 0 | 4 | sessionId, type, content, childType | 17 | 9 |
| 10593 | aime_aime_aimetalk_inputBox_sign | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_登录 | aime | aime对话页 | 对话输入框(inputBox) | 登录 | 0,2 | 0 | - | 1 | 1 |
| 15407 | aime_aime_aimetalk_inputBox_skilltrigger | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_skill触发 | aime | aime对话页 | 对话输入框(inputBox) | skill触发 | 0 | 0 | - | 3 | 1 |
| 5164 | aime_aime_aimetalk_inputBox_tkPanel | 元素埋点 | aime_Ainvest Aime_aime对话页_对话输入框(inputBox)_问句推荐 | aime | aime对话页 | 对话输入框(inputBox) | 问句推荐 | 0,2 | 11 | type, content, logId, from, sessionId +6 | 0 | 0 |
| 13008 | aime_aime_aimetalk_inputMenu_close | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_关闭 | aime | aime对话页 | 加号面板 | 关闭 | 0 | 0 | - | 14 | 17 |
| 12994 | aime_aime_aimetalk_inputMenu_fileUpload | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_文件上传 | aime | aime对话页 | 加号面板 | 文件上传 | 0 | 0 | - | 2 | 2 |
| 12991 | aime_aime_aimetalk_inputMenu_open | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_打开 | aime | aime对话页 | 加号面板 | 打开 | 0 | 0 | - | 23 | 16 |
| 12992 | aime_aime_aimetalk_inputMenu_photograph | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_拍照 | aime | aime对话页 | 加号面板 | 拍照 | 0 | 0 | - | 1 | 1 |
| 12993 | aime_aime_aimetalk_inputMenu_picupload | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_上传图片 | aime | aime对话页 | 加号面板 | 上传图片 | 0 | 0 | - | 6 | 3 |
| 12995 | aime_aime_aimetalk_inputMenu_voiceChat | 元素埋点 | aime_Ainvest Aime_aime对话页_加号面板_语音通话 | aime | aime对话页 | 加号面板 | 语音通话 | 0 | 0 | - | 0 | 0 |
| 15438 | aime_aime_aimetalk_list_slide | 元素埋点 | aime_Ainvest Aime_aime对话页_列表_滑动 | aime | aime对话页 | 列表 | 滑动 | 1 | 3 | stayLen, logId, direct | 23 | 33 |
| 5201 | aime_aime_aimetalk_lpFb_collectQue | 元素埋点 | aime_Ainvest Aime_aime对话页_长按反馈页_收藏问句 | aime | aime对话页 | 长按反馈页 | 收藏问句 | 0 | 3 | sessionId, logId, content | 0 | 0 |
| 4220 | aime_aime_aimetalk_lpFb_contest | 元素埋点 | aime_Ainvest Aime_aime对话页_长按反馈页_比赛 | aime | aime对话页 | 长按反馈页 | 比赛 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 2325 | aime_aime_aimetalk_lpFb_down | 元素埋点 | aime_Ainvest Aime_aime对话页_长按反馈页_点踩 | aime | aime对话页 | 长按反馈页 | 点踩 | 0 | 6 | sessionId, content, type, logId, source +1 | 1 | 1 |
| 2326 | aime_aime_aimetalk_lpFb_feedback | 元素埋点 | aime_Ainvest Aime_aime对话页_长按反馈页_意见反馈 | aime | aime对话页 | 长按反馈页 | 意见反馈 | 0 | 3 | sessionId, content, type | 22 | 23 |
| 2324 | aime_aime_aimetalk_lpFb_up | 元素埋点 | aime_Ainvest Aime_aime对话页_长按反馈页_点赞 | aime | aime对话页 | 长按反馈页 | 点赞 | 0 | 6 | sessionId, content, type, logId, source +1 | 3 | 3 |
| 9413 | aime_aime_aimetalk_memoryToast_content | 元素埋点 | aime_Ainvest Aime_aime对话页_记忆提醒_内容 | aime | aime对话页 | 记忆提醒 | 内容 | 2,0 | 5 | from, sessionId, source, content, logId | 0 | 0 |
| 9414 | aime_aime_aimetalk_memorypage_remove | 元素埋点 | aime_Ainvest Aime_aime对话页_记忆页面_删除 | aime | aime对话页 | 记忆页面 | 删除 | 0 | 1 | content | 0 | 0 |
| 11742 | aime_aime_aimetalk_modelSwitch_buttons | 元素埋点 | aime_Ainvest Aime_aime对话页_模型切换按钮_按钮 | aime | aime对话页 | 模型切换按钮 | 按钮 | 0,2 | 2 | source, from | 18 | 13 |
| 11747 | aime_aime_aimetalk_modelSwitchmenu_Upgrade | 元素埋点 | aime_Ainvest Aime_aime对话页_模型切换菜单_升级 | aime | aime对话页 | 模型切换菜单 | 升级 | 0,2 | 3 | type, source, from | 0 | 0 |
| 11746 | aime_aime_aimetalk_modelSwitchmenu_feedback | 元素埋点 | aime_Ainvest Aime_aime对话页_模型切换菜单_意见反馈 | aime | aime对话页 | 模型切换菜单 | 意见反馈 | 0,2 | 2 | source, from | 0 | 0 |
| 11745 | aime_aime_aimetalk_modelSwitchmenu_login | 元素埋点 | aime_Ainvest Aime_aime对话页_模型切换菜单_login | aime | aime对话页 | 模型切换菜单 | login | 0,2 | 2 | source, from | 0 | 0 |
| 11743 | aime_aime_aimetalk_modelSwitchmenu_type | 元素埋点 | aime_Ainvest Aime_aime对话页_模型切换菜单_类型 | aime | aime对话页 | 模型切换菜单 | 类型 | 0,2 | 3 | content, from, source | 3 | 12 |
| 11868 | aime_aime_aimetalk_more_agent | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_智能体 | aime | aime对话页 | more浮框 | 智能体 | 0,2 | 2 | source, from | 1 | 4 |
| 12280 | aime_aime_aimetalk_more_aimeprofile | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_Aime账户 | aime | aime对话页 | more浮框 | Aime账户 | 0 | 2 | source, from | 2 | 1 |
| 11871 | aime_aime_aimetalk_more_aimequestion | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_aime问句 | aime | aime对话页 | more浮框 | aime问句 | 0,2 | 3 | content, source, from | 7 | 15 |
| 12279 | aime_aime_aimetalk_more_dna | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_投资DNA | aime | aime对话页 | more浮框 | 投资DNA | 0 | 2 | source, from | 0 | 1 |
| 11867 | aime_aime_aimetalk_more_explore | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_explore | aime | aime对话页 | more浮框 | explore | 0,2 | 2 | source, from | 16 | 6 |
| 11866 | aime_aime_aimetalk_more_newChat | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_新建对话 | aime | aime对话页 | more浮框 | 新建对话 | 0,2 | 3 | source, from, sessionId | 1 | 4 |
| 11870 | aime_aime_aimetalk_more_setting | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_setting | aime | aime对话页 | more浮框 | setting | 0,2 | 2 | source, from | 4 | 11 |
| 11869 | aime_aime_aimetalk_more_tab | 元素埋点 | aime_Ainvest Aime_aime对话页_more浮框_tab | aime | aime对话页 | more浮框 | tab | 0,2 | 3 | source, from, content | 0 | 0 |
| 4228 | aime_aime_aimetalk_morefunction_AimeProfile | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_aime形象1 | aime | aime对话页 | 更多功能 | aime形象1 | 0 | 1 | sessionId | 1 | 1 |
| 6342 | aime_aime_aimetalk_morefunction_clearthecontext | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_清除上下文 | aime | aime对话页 | 更多功能 | 清除上下文 | 0 | 5 | from, session_id, logId, source, content | 1 | 1 |
| 4232 | aime_aime_aimetalk_morefunction_feedback | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_意见反馈 | aime | aime对话页 | 更多功能 | 意见反馈 | 0 | 1 | sessionId | 1 | 2 |
| 4405 | aime_aime_aimetalk_morefunction_livesupport | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_人工客服 | aime | aime对话页 | 更多功能 | 人工客服 | 0 | 1 | sessionId | 1 | 1 |
| 4233 | aime_aime_aimetalk_morefunction_setting | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_setting | aime | aime对话页 | 更多功能 | setting | 0 | 1 | sessionId | 2 | 1 |
| 4406 | aime_aime_aimetalk_morefunction_upgrade | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_解锁按钮 | aime | aime对话页 | 更多功能 | 解锁按钮 | 0 | 4 | sessionId, impsId, source, from | 14 | 1 |
| 4229 | aime_aime_aimetalk_morefunction_voice | 元素埋点 | aime_Ainvest Aime_aime对话页_更多功能_语音 | aime | aime对话页 | 更多功能 | 语音 | 0 | 0 | - | 17 | 18 |
| 12996 | aime_aime_aimetalk_multiModalInput_recommendQuery | 元素埋点 | aime_Ainvest Aime_aime对话页_多模态输入_推荐问句 | aime | aime对话页 | 多模态输入 | 推荐问句 | 2,0 | 0 | - | 2 | 12 |
| 12997 | aime_aime_aimetalk_multiModalInput_uploadFileAdd | 元素埋点 | aime_Ainvest Aime_aime对话页_多模态输入_添加上传文件 | aime | aime对话页 | 多模态输入 | 添加上传文件 | 2,0 | 0 | - | 3 | 3 |
| 12999 | aime_aime_aimetalk_multiModalInput_uploadFileClose | 元素埋点 | aime_Ainvest Aime_aime对话页_多模态输入_关闭上传文件 | aime | aime对话页 | 多模态输入 | 关闭上传文件 | 2,0 | 0 | - | 6 | 6 |
| 12998 | aime_aime_aimetalk_multiModalInput_uploadFilePreview | 元素埋点 | aime_Ainvest Aime_aime对话页_多模态输入_上传文件预览 | aime | aime对话页 | 多模态输入 | 上传文件预览 | 2,0 | 1 | type | 7 | 4 |
| 2304 | aime_aime_aimetalk_naviBar_avatar | 元素埋点 | aime_Ainvest Aime_aime对话页_导航栏（navigationBar）_avatar点击 | aime | aime对话页 | 导航栏（navigationBar） | avatar点击 | 0 | 1 | sessionId | 0 | 0 |
| 2305 | aime_aime_aimetalk_naviBar_quit | 元素埋点 | aime_Ainvest Aime_aime对话页_导航栏（navigationBar）_退出 | aime | aime对话页 | 导航栏（navigationBar） | 退出 | 0 | 1 | sessionId | 1 | 0 |
| 2306 | aime_aime_aimetalk_naviBar_voice | 元素埋点 | aime_Ainvest Aime_aime对话页_导航栏（navigationBar）_语音 | aime | aime对话页 | 导航栏（navigationBar） | 语音 | 0 | 2 | sessionId, state | 0 | 0 |
| 13001 | aime_aime_aimetalk_reference_referenceAll | 元素埋点 | aime_Ainvest Aime_aime对话页_引用_所有文件 | aime | aime对话页 | 引用 | 所有文件 | 0,2 | 0 | - | 0 | 0 |
| 13000 | aime_aime_aimetalk_reference_referenceOne | 元素埋点 | aime_Ainvest Aime_aime对话页_引用_单个文件 | aime | aime对话页 | 引用 | 单个文件 | 0,2 | 0 | - | 2 | 2 |
| 6027 | aime_aime_aimetalk_regenerateFeedback_better | 元素埋点 | aime_Ainvest Aime_aime对话页_重生成后反馈_更好 | aime | aime对话页 | 重生成后反馈 | 更好 | 0 | 6 | logId, sessionId, content, from, preLogId +1 | 0 | 1 |
| 6110 | aime_aime_aimetalk_regenerateFeedback_same | 元素埋点 | aime_Ainvest Aime_aime对话页_重生成后反馈_一样 | aime | aime对话页 | 重生成后反馈 | 一样 | 0 | 6 | logId, content, sessionId, from, source +1 | 0 | 0 |
| 6030 | aime_aime_aimetalk_regenerateFeedback_switchAnswer | 元素埋点 | aime_Ainvest Aime_aime对话页_重生成后反馈_切换答案 | aime | aime对话页 | 重生成后反馈 | 切换答案 | 0 | 5 | logId, sessionId, content, from, source | 3 | 3 |
| 6028 | aime_aime_aimetalk_regenerateFeedback_worse | 元素埋点 | aime_Ainvest Aime_aime对话页_重生成后反馈_更差 | aime | aime对话页 | 重生成后反馈 | 更差 | 0 | 6 | from, logId, sessionId, content, preLogId +1 | 1 | 2 |
| 5620 | aime_aime_aimetalk_screenResult_Rank | 元素埋点 | aime_Ainvest Aime_aime对话页_选股结果（screenResult）_排序 | aime | aime对话页 | 选股结果（screenResult） | 排序 | 0 | 3 | sessionId, from, logId | 0 | 0 |
| 5608 | aime_aime_aimetalk_screenResult_source | 元素埋点 | aime_Ainvest Aime_aime对话页_选股结果（screenResult）_来源 | aime | aime对话页 | 选股结果（screenResult） | 来源 | 0 | 4 | sessionId, source, content, from | 0 | 0 |
| 5619 | aime_aime_aimetalk_screenResult_stockName | 元素埋点 | aime_Ainvest Aime_aime对话页_选股结果（screenResult）_股票链接 | aime | aime对话页 | 选股结果（screenResult） | 股票链接 | 0 | 5 | stock, sessionId, logId, from, source | 0 | 0 |
| 12339 | aime_aime_aimetalk_searchresult_gomore | 元素埋点 | aime_Ainvest Aime_aime对话页_搜索结果_跳转更多 | aime | aime对话页 | 搜索结果 | 跳转更多 | 0,2 | 5 | source, from, logId, session_id, content | 0 | 0 |
| 4221 | aime_aime_aimetalk_shareContest_createCon | 元素埋点 | aime_Ainvest Aime_aime对话页_发送到比赛_创建比赛 | aime | aime对话页 | 发送到比赛 | 创建比赛 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 15408 | aime_aime_aimetalk_skillpopup_skillchoosed | 元素埋点 | aime_Ainvest Aime_aime对话页_skill显示框_skill | aime | aime对话页 | skill显示框 | skill | 0 | 1 | content | 5 | 13 |
| 10166 | aime_aime_aimetalk_sourcePopUp_Traceable link | 元素埋点 | aime_Ainvest Aime_aime对话页_溯源弹窗_网页链接溯源 | aime | aime对话页 | 溯源弹窗 | 网页链接溯源 | 0,2,1 | 4 | logId, experInfo, position, itemId | 0 | 0 |
| 15607 | aime_aime_aimetalk_stateRemind_display | 元素埋点 | aime_Ainvest Aime_aime对话页_状态推广弹窗_曝光 | aime | aime对话页 | 状态推广弹窗 | 曝光 | 4,2 | 1 | stayLen | 0 | 0 |
| 15608 | aime_aime_aimetalk_stateRemind_leaveTalk | 元素埋点 | aime_Ainvest Aime_aime对话页_状态推广弹窗_离开对话 | aime | aime对话页 | 状态推广弹窗 | 离开对话 | 0 | 1 | logmap | 0 | 0 |
| 2348 | aime_aime_aimetalk_tkPanel_ansBubble | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_机器人答案气泡 | aime | aime对话页 | 对话界面 | 机器人答案气泡 | 2,0,1 | 5 | sessionId, content, type, logId, childType | 31 | 22 |
| 2356 | aime_aime_aimetalk_tkPanel_ansLoading | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_答案加载 | aime | aime对话页 | 对话界面 | 答案加载 | 2 | 5 | sessionId, content, logId, stayLen, state | 4 | 7 |
| 2355 | aime_aime_aimetalk_tkPanel_ansResp | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_等待答案回复 | aime | aime对话页 | 对话界面 | 等待答案回复 | 2 | 4 | sessionId, content, type, logId | 5 | 2 |
| 2677 | aime_aime_aimetalk_tkPanel_bottomTag | 元素埋点 | _对话界面 | aime | aime对话页 | 对话界面 | 底部Tag推荐 | 0,2,1 | 11 | type, content, logId, num, from +6 | 1 | 4 |
| 4219 | aime_aime_aimetalk_tkPanel_contest | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_比赛 | aime | aime对话页 | 对话界面 | 比赛 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 13013 | aime_aime_aimetalk_tkPanel_dialogCutOff | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_对话中断 | aime | aime对话页 | 对话界面 | 对话中断 | 2,end | 2 | session_id, content | 0 | 0 |
| 2440 | aime_aime_aimetalk_tkPanel_firstBub | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_机器人第一个答案气泡 | aime | aime对话页 | 对话界面 | 机器人第一个答案气泡 | 2,4 | 4 | sessionId, content, logId, stayLen | 1 | 0 |
| 3120 | aime_aime_aimetalk_tkPanel_intradayChart | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_跳转分时 | aime | aime对话页 | 对话界面 | 跳转分时 | 0,2 | 3 | content, sessionId, from | 11 | 8 |
| 2560 | aime_aime_aimetalk_tkPanel_lenovo | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_输入联想 | aime | aime对话页 | 对话界面 | 输入联想 | 1,2,0 | 4 | sessionId, content, from, num | 2 | 2 |
| 3122 | aime_aime_aimetalk_tkPanel_linkTracing | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_点击网页链接溯源 | aime | aime对话页 | 对话界面 | 点击网页链接溯源 | 0,2 | 7 | sessionId, content, from, logId, itemId +2 | 0 | 0 |
| 3123 | aime_aime_aimetalk_tkPanel_moreLinksButton | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_显示更多链接开关 | aime | aime对话页 | 对话界面 | 显示更多链接开关 | 0,2 | 2 | sessionId, from | 0 | 0 |
| 6016 | aime_aime_aimetalk_tkPanel_moreTrace | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_更多溯源 | aime | aime对话页 | 对话界面 | 更多溯源 | 0 | 1 | content | 0 | 0 |
| 6026 | aime_aime_aimetalk_tkPanel_regenerate | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_换一批 | aime | aime对话页 | 对话界面 | 换一批 | 0 | 6 | logId, sessionId, content, from, source +1 | 1 | 0 |
| 2984 | aime_aime_aimetalk_tkPanel_resultPage | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_结果页 | aime | aime对话页 | 对话界面 | 结果页 | 0,2,4 | 6 | sessionId, logId, stayLen, type, from +1 | 8 | 4 |
| 2985 | aime_aime_aimetalk_tkPanel_resultPageGraph | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_图表类型 | aime | aime对话页 | 对话界面 | 图表类型 | 0,2,4 | 4 | sessionId, logId, type, from | 0 | 0 |
| 2477 | aime_aime_aimetalk_tkPanel_role | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_人设 | aime | aime对话页 | 对话界面 | 人设 | 2,0 | 3 | content, sessionId, from | 1 | 1 |
| 3854 | aime_aime_aimetalk_tkPanel_share | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_分享 | aime | aime对话页 | 对话界面 | 分享 | 2,0 | 6 | from, sessionId, type, logId, content +1 | 8 | 43 |
| 4551 | aime_aime_aimetalk_tkPanel_shareform | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_分享形式 | aime | aime对话页 | 对话界面 | 分享形式 | 0,2 | 7 | childType, from, sessionId, logId, content +2 | 2 | 6 |
| 6015 | aime_aime_aimetalk_tkPanel_trace | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_溯源 | aime | aime对话页 | 对话界面 | 溯源 | 2,0 | 5 | content, itemId, position, experInfo, logId | 0 | 0 |
| 6017 | aime_aime_aimetalk_tkPanel_tracePopUp | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_溯源弹窗 | aime | aime对话页 | 对话界面 | 溯源弹窗 | 2,1,0 | 1 | content | 0 | 0 |
| 3121 | aime_aime_aimetalk_tkPanel_traceability | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_点击文字溯源 | aime | aime对话页 | 对话界面 | 点击文字溯源 | 0,2 | 7 | content, sessionId, from, logId, position +2 | 27 | 30 |
| 2320 | aime_aime_aimetalk_tkPanel_userQue | 元素埋点 | aime_Ainvest Aime_aime对话页_对话界面_用户对话气泡 | aime | aime对话页 | 对话界面 | 用户对话气泡 | 9,2,0 | 3 | sessionId, content, logId | 27 | 18 |
| 4462 | aime_aime_aimetalk_topbanner_unlock | 元素埋点 | aime_Ainvest Aime_aime对话页_顶部区域_解锁 | aime | aime对话页 | 顶部区域 | 解锁 | 0,2 | 1 | itemId | 0 | 0 |
| 2317 | aime_aime_aimetalk_voiInput_endVoice | 元素埋点 | aime_Ainvest Aime_aime对话页_语音输入_结束语音输入 | aime | aime对话页 | 语音输入 | 结束语音输入 | 0,4,2 | 3 | sessionId, content, type | 4 | 2 |
| 15296 | aime_aime_aimetalk_voice_broadcast | 元素埋点 | aime_Ainvest Aime_aime对话页_语音播报_语音播报 | aime | aime对话页 | 语音播报 | 语音播报 | 0 | 0 | - | 7 | 9 |
| 15295 | aime_aime_aimetalk_voice_broadcast1 | 元素埋点 | aime_Ainvest Aime_aime对话页_语音播报_播报 | aime | aime对话页 | 语音播报 | 播报 | 0 | 0 | - | 2 | 5 |
| 15308 | aime_aime_aimetalk_voice_moreFunction | 元素埋点 | aime_Ainvest Aime_aime对话页_语音播报_更多功能 | aime | aime对话页 | 语音播报 | 更多功能 | 0 | 1 | content | 10 | 6 |
| 15309 | aime_aime_aimetalk_voice_switchLatestStatus | 元素埋点 | aime_Ainvest Aime_aime对话页_语音播报_开关最新状态 | aime | aime对话页 | 语音播报 | 开关最新状态 | 8 | 1 | state | 1 | 14 |
| 15297 | aime_aime_aimetalk_voice_voicechange | 元素埋点 | aime_Ainvest Aime_aime对话页_语音播报_音色广场 | aime | aime对话页 | 语音播报 | 音色广场 | 0 | 0 | - | 1 | 1 |
| 2340 | aime_aime_chatTheme | 页面埋点 | aime_Ainvest Aime_aime形象设置 | aime | aime形象设置 | - | - | 2 | 1 | sessionId | 0 | 1 |
| 2339 | aime_aime_chatTheme_Theme_huTheme | 元素埋点 | aime_Ainvest Aime_aime形象设置_对话主题选择_虚拟人主题 | aime | aime形象设置 | 对话主题选择 | 虚拟人主题 | 0 | 1 | sessionId | 0 | 0 |
| 2338 | aime_aime_chatTheme_Theme_techTheme | 元素埋点 | aime_Ainvest Aime_aime形象设置_对话主题选择_科技主题 | aime | aime形象设置 | 对话主题选择 | 科技主题 | 0 | 1 | sessionId | 0 | 0 |
| 2337 | aime_aime_chatTheme_Theme_tradTheme | 元素埋点 | aime_Ainvest Aime_aime形象设置_对话主题选择_传统主题 | aime | aime形象设置 | 对话主题选择 | 传统主题 | 0 | 1 | sessionId | 0 | 0 |
| 2336 | aime_aime_chatTheme_naviBar_quit | 元素埋点 | aime_Ainvest Aime_aime形象设置_导航栏（navigationBar）_退出 | aime | aime形象设置 | 导航栏（navigationBar） | 退出 | 0 | 1 | sessionId | 1 | 1 |
| 14035 | aime_aime_aimemix_aimeEverywhere_aimeNewUserGuide | 元素埋点 | aime_Ainvest Aime_aime无处不在_Aime无处不在_aime新手引导 | aime | aime无处不在 | Aime无处不在 | aime新手引导 | 0,2 | 2 | state, mode | 0 | 0 |
| 3852 | aime_aime_aimeweb | 页面埋点 | aime_Ainvest Aime_aime网页对话 | aime | aime网页对话 | - | - | 0,1,2,4 | 2 | stayLen, from | 8 | 6 |
| 4216 | aime_aime_aimeweb_Inputlock_upgrade | 元素埋点 | aime_Ainvest Aime_aime网页对话_输入区解锁_解锁按钮 | aime | aime网页对话 | 输入区解锁 | 解锁按钮 | 0,2 | 2 | itemId, from | 0 | 0 |
| 4218 | aime_aime_aimeweb_Subplans_Aimepro | 元素埋点 | aime_Ainvest Aime_aime网页对话_商品订阅页面_商品卡片 | aime | aime网页对话 | 商品订阅页面 | 商品卡片 | 0,2 | 4 | itemId, type, source, from | 0 | 0 |
| 4214 | aime_aime_aimeweb_Taghint_taghint | 元素埋点 | aime_Ainvest Aime_aime网页对话_tag提示_tag提示 | aime | aime网页对话 | tag提示 | tag提示 | 0,2 | 2 | itemId, from | 0 | 0 |
| 4311 | aime_aime_aimeweb_activeRecom_tkPanel | 元素埋点 | aime_Ainvest Aime_aime网页对话_主动式问句推荐_问句推荐 | aime | aime网页对话 | 主动式问句推荐 | 问句推荐 | 0,2 | 2 | content, function | 1 | 2 |
| 11784 | aime_aime_aimeweb_aimeHome_explore | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime首页运营_explore | aime | aime网页对话 | Aime首页运营 | explore | 0,1 | 2 | source, from | 0 | 1 |
| 11783 | aime_aime_aimeweb_aimeHome_history | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime首页运营_记录 | aime | aime网页对话 | Aime首页运营 | 记录 | 0,1 | 2 | source, from | 6 | 2 |
| 11781 | aime_aime_aimeweb_aimeHome_newChat | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime首页运营_新建对话 | aime | aime网页对话 | Aime首页运营 | 新建对话 | 0 | 2 | source, from | 5 | 2 |
| 11780 | aime_aime_aimeweb_aimeHome_recquestions | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime首页运营_推荐问句 | aime | aime网页对话 | Aime首页运营 | 推荐问句 | 0,2 | 5 | source, from, content, sessionId, recInfo | 0 | 0 |
| 11782 | aime_aime_aimeweb_aimeHome_switchTab | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime首页运营_tab页面切换 | aime | aime网页对话 | Aime首页运营 | tab页面切换 | 0,1 | 3 | source, from, content | 0 | 0 |
| 3851 | aime_aime_aimeweb_dialogDetail_details | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话详情页_查看详情 | aime | aime网页对话 | 对话详情页 | 查看详情 | end,4,2,1,0 | 4 | type, url, content, stayLen | 1 | 2 |
| 4210 | aime_aime_aimeweb_function_subsCard | 元素埋点 | aime_Ainvest Aime_aime网页对话_功能组件_商品卡片 | aime | aime网页对话 | 功能组件 | 商品卡片 | 0,2 | 2 | itemId, from | 0 | 0 |
| 15442 | aime_aime_aimeweb_list_slide | 元素埋点 | aime_Ainvest Aime_aime网页对话_列表_滑动 | aime | aime网页对话 | 列表 | 滑动 | 1 | 3 | logId, stayLen, direct | 0 | 0 |
| 3846 | aime_aime_aimeweb_naviBar_askAime | 元素埋点 | aime_Ainvest Aime_aime网页对话_导航栏（navigationBar）_开始对话 | aime | aime网页对话 | 导航栏（navigationBar） | 开始对话 | 0 | 1 | from | 0 | 0 |
| 3845 | aime_aime_aimeweb_naviBar_collectQue | 元素埋点 | aime_Ainvest Aime_aime网页对话_导航栏（navigationBar）_收藏问句 | aime | aime网页对话 | 导航栏（navigationBar） | 收藏问句 | 0,1,2,3 | 3 | type, content, logId | 0 | 0 |
| 3848 | aime_aime_aimeweb_naviBar_logout | 元素埋点 | aime_Ainvest Aime_aime网页对话_导航栏（navigationBar）_登出客户端 | aime | aime网页对话 | 导航栏（navigationBar） | 登出客户端 | 0 | 0 | - | 0 | 0 |
| 3844 | aime_aime_aimeweb_naviBar_recQuery | 元素埋点 | aime_Ainvest Aime_aime网页对话_导航栏（navigationBar）_推荐问句 | aime | aime网页对话 | 导航栏（navigationBar） | 推荐问句 | 0,1,2,3 | 9 | type, content, logId, num, recInfo +4 | 0 | 0 |
| 3847 | aime_aime_aimeweb_naviBar_sign | 元素埋点 | aime_Ainvest Aime_aime网页对话_导航栏（navigationBar）_登录 | aime | aime网页对话 | 导航栏（navigationBar） | 登录 | 0 | 0 | - | 0 | 0 |
| 4420 | aime_aime_aimeweb_shareContest_createCon | 元素埋点 | aime_Ainvest Aime_aime网页对话_发送到比赛_创建比赛 | aime | aime网页对话 | 发送到比赛 | 创建比赛 | 0 | 3 | sessionId, type, content | 0 | 0 |
| 9745 | aime_aime_aimeweb_sharePage_explodRecommend | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime分享页面_广场问句推荐模块 | aime | aime网页对话 | Aime分享页面 | 广场问句推荐模块 | 0,2 | 0 | - | 0 | 0 |
| 9744 | aime_aime_aimeweb_sharePage_recommendation | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime分享页面_推荐模块 | aime | aime网页对话 | Aime分享页面 | 推荐模块 | 0,2 | 0 | - | 10 | 16 |
| 5944 | aime_aime_aimeweb_sharePage_shareReflux | 元素埋点 | aime_Ainvest Aime_aime网页对话_Aime分享页面_分享回流按钮 | aime | aime网页对话 | Aime分享页面 | 分享回流按钮 | 0,2 | 0 | - | 1 | 1 |
| 11819 | aime_aime_aimeweb_tkPanel_activequery | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_主动式问句 | aime | aime网页对话 | 对话界面 | 主动式问句 | 0,2 | 2 | source, from | 1 | 4 |
| 6185 | aime_aime_aimeweb_tkPanel_betterredo | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_重新生成更好 | aime | aime网页对话 | 对话界面 | 重新生成更好 | 0 | 0 | - | 0 | 0 |
| 4312 | aime_aime_aimeweb_tkPanel_bottomTag | 元素埋点 | _对话界面 | aime | aime网页对话 | 对话界面 | 底部Tag推荐 | 0,1,2 | 9 | type, content, logId, num, from +4 | 0 | 0 |
| 4419 | aime_aime_aimeweb_tkPanel_contest | 元素埋点 | _对话界面 | aime | aime网页对话 | 对话界面 | 比赛 | 0 | 3 | sessionId, content, type | 0 | 0 |
| 6153 | aime_aime_aimeweb_tkPanel_link | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_链接 | aime | aime网页对话 | 对话界面 | 链接 | 0 | 0 | - | 1 | 4 |
| 6184 | aime_aime_aimeweb_tkPanel_redo | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_重新生成 | aime | aime网页对话 | 对话界面 | 重新生成 | 0 | 0 | - | 1 | 0 |
| 6187 | aime_aime_aimeweb_tkPanel_sameredo | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_重新生成一样 | aime | aime网页对话 | 对话界面 | 重新生成一样 | 0 | 0 | - | 0 | 0 |
| 6152 | aime_aime_aimeweb_tkPanel_share | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_分享 | aime | aime网页对话 | 对话界面 | 分享 | 0,3 | 0 | - | 5 | 6 |
| 6154 | aime_aime_aimeweb_tkPanel_toExplore | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_到广场 | aime | aime网页对话 | 对话界面 | 到广场 | 0 | 0 | - | 1 | 0 |
| 6186 | aime_aime_aimeweb_tkPanel_worseredo | 元素埋点 | aime_Ainvest Aime_aime网页对话_对话界面_重新生成更差 | aime | aime网页对话 | 对话界面 | 重新生成更差 | 0 | 0 | - | 0 | 0 |
| 2330 | aime_aime_robotCenter | 页面埋点 | aime_Ainvest Aime_个人中心 | aime | 个人中心 | - | - | 2,4,1 | 1 | sessionId | 0 | 0 |
| 2331 | aime_aime_robotCenter_rbtCen_chatTheme | 元素埋点 | aime_Ainvest Aime_个人中心_aime个人中心_aime形象设置 | aime | 个人中心 | aime个人中心 | aime形象设置 | 0 | 1 | sessionId | 0 | 0 |
| 2334 | aime_aime_robotCenter_rbtCen_faq | 元素埋点 | aime_Ainvest Aime_个人中心_aime个人中心_客服问句 | aime | 个人中心 | aime个人中心 | 客服问句 | 0 | 3 | sessionId, content, type | 0 | 0 |
| 2333 | aime_aime_robotCenter_rbtCen_research | 元素埋点 | aime_Ainvest Aime_个人中心_aime个人中心_诊股 | aime | 个人中心 | aime个人中心 | 诊股 | 0 | 3 | sessionId, content, type | 0 | 0 |
| 2332 | aime_aime_robotCenter_rbtCen_screener | 元素埋点 | aime_Ainvest Aime_个人中心_aime个人中心_选股表格 | aime | 个人中心 | aime个人中心 | 选股表格 | 0 | 3 | sessionId, content, type | 0 | 0 |
| 9742 | aime_aime_robotCenter_setting_everywhereswitch | 元素埋点 | aime_Ainvest Aime_个人中心_设置_aime无处不在开关 | aime | 个人中心 | 设置 | aime无处不在开关 | 0 | 1 | state | 0 | 0 |
| 4217 | aime_aime_landingpage | 页面埋点 | aime_Ainvest Aime_产品落地页 | aime | 产品落地页 | - | - | 0,2,1 | 3 | itemId, type, source | 0 | 0 |
| 13173 | aime_aime_landingpage_aIMEPortOppSl_slide | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户机会落地页_滑动 | aime | 产品落地页 | 影子账户机会落地页 | 滑动 | 1,2 | 0 | - | 0 | 0 |
| 13171 | aime_aime_landingpage_aIMEPortfoOppo_tranpagebutton | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户盘前机会_过渡页按钮 | aime | 产品落地页 | 影子账户盘前机会 | 过渡页按钮 | 0,2 | 0 | - | 0 | 0 |
| 13170 | aime_aime_landingpage_aIMEPortfolioFirst_tranpagebutton | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户纳新过度按钮_过渡页按钮 | aime | 产品落地页 | 影子账户纳新过度按钮 | 过渡页按钮 | 0,2 | 0 | - | 0 | 0 |
| 13172 | aime_aime_landingpage_aIMEPortfolioReb_tranpagebutton | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户调仓跳转_过渡页按钮 | aime | 产品落地页 | 影子账户调仓跳转 | 过渡页按钮 | 0,2 | 0 | - | 0 | 0 |
| 13302 | aime_aime_landingpage_aimePortCreate_aimePortClik | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户创建_用户同意点击 | aime | 产品落地页 | 影子账户创建 | 用户同意点击 | 0,4 | 0 | - | 0 | 0 |
| 13169 | aime_aime_landingpage_aimePortconbottom_touchConsent | 元素埋点 | aime_Ainvest Aime_产品落地页_影子账户确认按钮_点击确认 | aime | 产品落地页 | 影子账户确认按钮 | 点击确认 | 0,2 | 0 | - | 0 | 0 |
| 4461 | aime_aime_landingpage_button_submit | 元素埋点 | aime_Ainvest Aime_产品落地页_按钮_提交 | aime | 产品落地页 | 按钮 | 提交 | 0,2 | 0 | - | 0 | 0 |
| 4206 | aime_aime_landingpage_topbanner_restore | 元素埋点 | aime_Ainvest Aime_产品落地页_顶部区域_恢复订阅 | aime | 产品落地页 | 顶部区域 | 恢复订阅 | 0,2 | 0 | - | 0 | 0 |
| 5110 | aime_aime_roleplay | 页面埋点 | aime_Ainvest Aime_人设对话 | aime | 人设对话 | - | - | 2 | 0 | - | 0 | 0 |
| 5118 | aime_aime_roleplay_characterProfile_chatButton | 元素埋点 | aime_Ainvest Aime_人设对话_人设详情_开始对话 | aime | 人设对话 | 人设详情 | 开始对话 | 0 | 0 | - | 0 | 0 |
| 5117 | aime_aime_roleplay_characterProfile_delete | 元素埋点 | aime_Ainvest Aime_人设对话_人设详情_删除 | aime | 人设对话 | 人设详情 | 删除 | 0 | 0 | - | 0 | 0 |
| 5116 | aime_aime_roleplay_characterProfile_modify | 元素埋点 | aime_Ainvest Aime_人设对话_人设详情_修改 | aime | 人设对话 | 人设详情 | 修改 | 0 | 0 | - | 0 | 0 |
| 5111 | aime_aime_roleplay_craeteCharacter_createButton | 元素埋点 | aime_Ainvest Aime_人设对话_创建角色_创建按钮 | aime | 人设对话 | 创建角色 | 创建按钮 | 0 | 1 | sessionId | 0 | 0 |
| 5113 | aime_aime_roleplay_createCharacterlist_createButton | 元素埋点 | aime_Ainvest Aime_人设对话_创建人设表单_创建按钮 | aime | 人设对话 | 创建人设表单 | 创建按钮 | 0 | 0 | - | 0 | 0 |
| 5115 | aime_aime_roleplay_createCharacterlist_savebutton | 元素埋点 | aime_Ainvest Aime_人设对话_创建人设表单_保存按钮 | aime | 人设对话 | 创建人设表单 | 保存按钮 | 0 | 0 | - | 0 | 0 |
| 5114 | aime_aime_roleplay_createCharacterlist_tabcontent | 元素埋点 | aime_Ainvest Aime_人设对话_创建人设表单_tab选项 | aime | 人设对话 | 创建人设表单 | tab选项 | 0 | 1 | content | 0 | 0 |
| 5119 | aime_aime_roleplay_rateInterest_rate | 元素埋点 | aime_Ainvest Aime_人设对话_兴趣评分_评分分数 | aime | 人设对话 | 兴趣评分 | 评分分数 | 0 | 2 | value, type | 0 | 0 |
| 5112 | aime_aime_roleplay_selectGuru_guruList | 元素埋点 | aime_Ainvest Aime_人设对话_选择角色_人设列表 | aime | 人设对话 | 选择角色 | 人设列表 | 0 | 1 | content | 0 | 0 |
| 5120 | aime_aime_roleplay_voiceSelect_selectButton | 元素埋点 | aime_Ainvest Aime_人设对话_声音选择_选择按钮 | aime | 人设对话 | 声音选择 | 选择按钮 | 0 | 0 | - | 0 | 0 |
| 9450 | aime_aime_quickpanel_agentwindow_remove | 元素埋点 | aime_Ainvest Aime_快捷面板_智能体浮窗_删除 | aime | 快捷面板 | 智能体浮窗 | 删除 | 0 | 0 | - | 0 | 0 |
| 9444 | aime_aime_quickpanel_historys_listview | 元素埋点 | aime_Ainvest Aime_快捷面板_历史_历史列表查看 | aime | 快捷面板 | 历史 | 历史列表查看 | 0,2 | 0 | - | 0 | 0 |
| 9448 | aime_aime_quickpanel_quickpanel_agent | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_智能体 | aime | 快捷面板 | 快捷面板 | 智能体 | 0,2 | 0 | - | 0 | 0 |
| 9446 | aime_aime_quickpanel_quickpanel_collectQue | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_收藏问句 | aime | 快捷面板 | 快捷面板 | 收藏问句 | 0 | 0 | - | 0 | 0 |
| 9445 | aime_aime_quickpanel_quickpanel_quickpanel | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_快捷面板 | aime | 快捷面板 | 快捷面板 | 快捷面板 | 0 | 0 | - | 0 | 0 |
| 9447 | aime_aime_quickpanel_quickpanel_remove | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_删除 | aime | 快捷面板 | 快捷面板 | 删除 | 0 | 0 | - | 0 | 0 |
| 9469 | aime_aime_quickpanel_quickpanel_viewallagent | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_查询全部智能体 | aime | 快捷面板 | 快捷面板 | 查询全部智能体 | 0 | 0 | - | 0 | 0 |
| 9449 | aime_aime_quickpanel_quickpanel_viewmore | 元素埋点 | aime_Ainvest Aime_快捷面板_快捷面板_查看更多 | aime | 快捷面板 | 快捷面板 | 查看更多 | 0,2 | 0 | - | 0 | 0 |
| 6257 | aime_aime_AgentStore_agent_More | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体_更多 | aime | 智能体商店 | 智能体 | 更多 | 0,2 | 0 | - | 0 | 0 |
| 6256 | aime_aime_AgentStore_agent_add | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体_添加 | aime | 智能体商店 | 智能体 | 添加 | 0,2 | 0 | - | 3 | 1 |
| 6259 | aime_aime_AgentStore_agent_addagent | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体_添加智能体 | aime | 智能体商店 | 智能体 | 添加智能体 | 0,2 | 0 | - | 0 | 0 |
| 6258 | aime_aime_AgentStore_agent_clickagent | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体_点击智能体 | aime | 智能体商店 | 智能体 | 点击智能体 | 0,2 | 0 | - | 2 | 3 |
| 6274 | aime_aime_AgentStore_agentpages_clickShared | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体主页_点击分享 | aime | 智能体商店 | 智能体主页 | 点击分享 | 0,2 | 0 | - | 0 | 0 |
| 6273 | aime_aime_AgentStore_agentpages_rate | 元素埋点 | aime_Ainvest Aime_智能体商店_智能体主页_评分分数 | aime | 智能体商店 | 智能体主页 | 评分分数 | 0,2 | 0 | - | 0 | 0 |
| 6269 | aime_aime_AgentStore_createagent_addfile | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_添加文档 | aime | 智能体商店 | 创建智能体 | 添加文档 | 0,2 | 0 | - | 0 | 0 |
| 6271 | aime_aime_AgentStore_createagent_addtool | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_添加工具 | aime | 智能体商店 | 创建智能体 | 添加工具 | 0,2 | 0 | - | 0 | 0 |
| 6268 | aime_aime_AgentStore_createagent_addweb | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_添加网页 | aime | 智能体商店 | 创建智能体 | 添加网页 | 0,2 | 0 | - | 0 | 0 |
| 6262 | aime_aime_AgentStore_createagent_allTools | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_全部工具 | aime | 智能体商店 | 创建智能体 | 全部工具 | 0,2 | 0 | - | 0 | 0 |
| 6272 | aime_aime_AgentStore_createagent_canceltools | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_取消工具 | aime | 智能体商店 | 创建智能体 | 取消工具 | 0,2 | 0 | - | 0 | 0 |
| 6263 | aime_aime_AgentStore_createagent_choosevoice | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_选择声音 | aime | 智能体商店 | 创建智能体 | 选择声音 | 0,2 | 0 | - | 1 | 1 |
| 6267 | aime_aime_AgentStore_createagent_creatcomfirm | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_确认创建 | aime | 智能体商店 | 创建智能体 | 确认创建 | 0,2 | 0 | - | 3 | 0 |
| 6266 | aime_aime_AgentStore_createagent_inputBoxClearAll | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_编辑框清空（screenerInputBoxClearAll） | aime | 智能体商店 | 创建智能体 | 编辑框清空（screenerInputBoxClearAll） | 0,2 | 0 | - | 0 | 0 |
| 6261 | aime_aime_AgentStore_createagent_knowledge | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_知识库 | aime | 智能体商店 | 创建智能体 | 知识库 | 0,2 | 0 | - | 0 | 0 |
| 6265 | aime_aime_AgentStore_createagent_polish | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_优化 | aime | 智能体商店 | 创建智能体 | 优化 | 0,2 | 0 | - | 1 | 1 |
| 6260 | aime_aime_AgentStore_createagent_profile | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_简况 | aime | 智能体商店 | 创建智能体 | 简况 | 0,2 | 0 | - | 0 | 3 |
| 6264 | aime_aime_AgentStore_createagent_promptTemp | 元素埋点 | aime_Ainvest Aime_智能体商店_创建智能体_提示词模版 | aime | 智能体商店 | 创建智能体 | 提示词模版 | 0,2 | 0 | - | 1 | 1 |
| 6255 | aime_aime_AgentStore_explore_agent | 元素埋点 | aime_Ainvest Aime_智能体商店_探索_智能体 | aime | 智能体商店 | 探索 | 智能体 | 0,2 | 0 | - | 0 | 0 |
| 6254 | aime_aime_AgentStore_explore_explore | 元素埋点 | aime_Ainvest Aime_智能体商店_探索_explore | aime | 智能体商店 | 探索 | explore | 0,2 | 0 | - | 0 | 0 |
| 6270 | aime_aime_AgentStore_knowledge_delete | 元素埋点 | aime_Ainvest Aime_智能体商店_知识库_删除 | aime | 智能体商店 | 知识库 | 删除 | 0,2 | 0 | - | 0 | 0 |
| 9416 | aime_aime_AgentStore_memorypage_forgot | 元素埋点 | aime_Ainvest Aime_智能体商店_记忆页面_忘记 | aime | 智能体商店 | 记忆页面 | 忘记 | 0 | 1 | content | 0 | 0 |
| 15365 | aime_aime_hotpredictions_signaltracker_dislikeBtn | 元素埋点 | aime_Ainvest Aime_热点预测_信号追踪_踩按钮 | aime | 热点预测 | 信号追踪 | 踩按钮 | 0 | 0 | - | 0 | 0 |
| 15366 | aime_aime_hotpredictions_signaltracker_signalDetected | 元素埋点 | aime_Ainvest Aime_热点预测_信号追踪_信号触发 | aime | 热点预测 | 信号追踪 | 信号触发 | 0 | 0 | - | 0 | 0 |
| 15753 | aime_aime_socialLandingPage | 页面埋点 | aime_Ainvest Aime_社媒爆款落地页 | aime | 社媒爆款落地页 | - | - | 2 | 1 | state | 0 | 0 |
| 15754 | aime_aime_socialLandingPage_aimeQuestion_aimeQuestionBlock | 元素埋点 | aime_Ainvest Aime_社媒爆款落地页_aime推荐问句_推荐问句区块 | aime | 社媒爆款落地页 | aime推荐问句 | 推荐问句区块 | 0,2 | 2 | state, num | 0 | 0 |
| 6279 | aime_aime_webagentstore_agent_addagent | 元素埋点 | aime_Ainvest Aime_网页智能体商店_智能体_添加智能体 | aime | 网页智能体商店 | 智能体 | 添加智能体 | 0 | 0 | - | 0 | 0 |
| 6291 | aime_aime_webagentstore_agentpages_rate | 元素埋点 | aime_Ainvest Aime_网页智能体商店_智能体主页_评分分数 | aime | 网页智能体商店 | 智能体主页 | 评分分数 | 0 | 0 | - | 0 | 0 |
| 6292 | aime_aime_webagentstore_agentpages_share | 元素埋点 | aime_Ainvest Aime_网页智能体商店_智能体主页_分享 | aime | 网页智能体商店 | 智能体主页 | 分享 | 0 | 0 | - | 0 | 0 |
| 6289 | aime_aime_webagentstore_allTools_addtool | 元素埋点 | aime_Ainvest Aime_网页智能体商店_所有组件工具_添加工具 | aime | 网页智能体商店 | 所有组件工具 | 添加工具 | 0 | 0 | - | 0 | 0 |
| 6290 | aime_aime_webagentstore_allTools_canceltools | 元素埋点 | aime_Ainvest Aime_网页智能体商店_所有组件工具_取消工具 | aime | 网页智能体商店 | 所有组件工具 | 取消工具 | 0 | 0 | - | 0 | 0 |
| 6282 | aime_aime_webagentstore_createagent_allTools | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_全部工具 | aime | 网页智能体商店 | 创建智能体 | 全部工具 | 0 | 0 | - | 0 | 0 |
| 6283 | aime_aime_webagentstore_createagent_choosevoice | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_选择声音 | aime | 网页智能体商店 | 创建智能体 | 选择声音 | 0 | 0 | - | 0 | 0 |
| 6286 | aime_aime_webagentstore_createagent_createButton | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_创建按钮 | aime | 网页智能体商店 | 创建智能体 | 创建按钮 | 0 | 0 | - | 0 | 0 |
| 6281 | aime_aime_webagentstore_createagent_knowledge | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_知识库 | aime | 网页智能体商店 | 创建智能体 | 知识库 | 0 | 0 | - | 0 | 0 |
| 6285 | aime_aime_webagentstore_createagent_polish | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_优化 | aime | 网页智能体商店 | 创建智能体 | 优化 | 0 | 0 | - | 0 | 0 |
| 6280 | aime_aime_webagentstore_createagent_profile | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_简况 | aime | 网页智能体商店 | 创建智能体 | 简况 | 0 | 0 | - | 0 | 0 |
| 6284 | aime_aime_webagentstore_createagent_promptTemp | 元素埋点 | aime_Ainvest Aime_网页智能体商店_创建智能体_提示词模版 | aime | 网页智能体商店 | 创建智能体 | 提示词模版 | 0 | 0 | - | 0 | 0 |
| 6278 | aime_aime_webagentstore_explore_More | 元素埋点 | aime_Ainvest Aime_网页智能体商店_探索_更多 | aime | 网页智能体商店 | 探索 | 更多 | 0 | 0 | - | 0 | 0 |
| 6276 | aime_aime_webagentstore_explore_addagent | 元素埋点 | aime_Ainvest Aime_网页智能体商店_探索_添加智能体 | aime | 网页智能体商店 | 探索 | 添加智能体 | 0 | 0 | - | 0 | 0 |
| 6275 | aime_aime_webagentstore_explore_agent | 元素埋点 | aime_Ainvest Aime_网页智能体商店_探索_智能体 | aime | 网页智能体商店 | 探索 | 智能体 | 0 | 0 | - | 0 | 0 |
| 6277 | aime_aime_webagentstore_explore_clickagent | 元素埋点 | aime_Ainvest Aime_网页智能体商店_探索_点击智能体 | aime | 网页智能体商店 | 探索 | 点击智能体 | 0 | 0 | - | 0 | 0 |
| 6288 | aime_aime_webagentstore_knowledge_addfile | 元素埋点 | aime_Ainvest Aime_网页智能体商店_知识库_添加文档 | aime | 网页智能体商店 | 知识库 | 添加文档 | 0 | 0 | - | 0 | 0 |
| 6287 | aime_aime_webagentstore_knowledge_addweb | 元素埋点 | aime_Ainvest Aime_网页智能体商店_知识库_添加网页 | aime | 网页智能体商店 | 知识库 | 添加网页 | 0 | 0 | - | 0 | 0 |
| 13317 | aime_aime_memory | 页面埋点 | aime_Ainvest Aime_记忆落地页 | aime | 记忆落地页 | - | - | 2 | 0 | - | 0 | 0 |
| 13301 | aime_aime_memory_aimeMemDisp_chatButton | 元素埋点 | aime_Ainvest Aime_记忆落地页_Aime记忆展示_开始对话 | aime | 记忆落地页 | Aime记忆展示 | 开始对话 | 0 | 1 | groupId | 2 | 1 |
| 13165 | aime_aime_memory_aimeMemDisp_deletebutton | 元素埋点 | aime_Ainvest Aime_记忆落地页_Aime记忆展示_删除按钮 | aime | 记忆落地页 | Aime记忆展示 | 删除按钮 | 0 | 2 | content, logId | 2 | 1 |
| 13166 | aime_aime_memory_aimeMemDisp_savebutton | 元素埋点 | aime_Ainvest Aime_记忆落地页_Aime记忆展示_保存按钮 | aime | 记忆落地页 | Aime记忆展示 | 保存按钮 | 0 | 1 | content | 0 | 0 |
| 13167 | aime_aime_memory_aimeMemDisp_tabclick | 元素埋点 | aime_Ainvest Aime_记忆落地页_Aime记忆展示_tab点击 | aime | 记忆落地页 | Aime记忆展示 | tab点击 | 0 | 0 | - | 3 | 2 |
| 13827 | aime_aime_memory_aimeMemTrace_PageShow | 元素埋点 | aime_Ainvest Aime_记忆落地页_Aime记忆溯源_页面展示 | aime | 记忆落地页 | Aime记忆溯源 | 页面展示 | 2 | 0 | - | 0 | 0 |
| 13320 | aime_aime_memory_memorypage_PageShow | 元素埋点 | aime_Ainvest Aime_记忆落地页_记忆页面_页面展示 | aime | 记忆落地页 | 记忆页面 | 页面展示 | 2 | 0 | - | 0 | 3 |
| 6383 | aime_aime_multimodal_addPanel_ToolPanel | 元素埋点 | aime_Ainvest Aime_语音助手多模态_加号面板_加号面板 | aime | 语音助手多模态 | 加号面板 | 加号面板 | 0,2 | 0 | - | 0 | 0 |
| 5622 | aime_aime_multimodal_imaShow_successinput | 元素埋点 | aime_Ainvest Aime_语音助手多模态_图片展示_上传成功 | aime | 语音助手多模态 | 图片展示 | 上传成功 | 0,2 | 0 | - | 0 | 0 |
| 5623 | aime_aime_multimodal_inputBox_sendmsg | 元素埋点 | aime_Ainvest Aime_语音助手多模态_对话输入框(inputBox)_消息发送 | aime | 语音助手多模态 | 对话输入框(inputBox) | 消息发送 | 0,2 | 0 | - | 0 | 0 |
| 6381 | aime_aime_multimodal_upload_addfile | 元素埋点 | aime_Ainvest Aime_语音助手多模态_上传_添加文档 | aime | 语音助手多模态 | 上传 | 添加文档 | 0,2 | 0 | - | 0 | 0 |
| 6382 | aime_aime_multimodal_upload_sendImg | 元素埋点 | aime_Ainvest Aime_语音助手多模态_上传_上传图片 | aime | 语音助手多模态 | 上传 | 上传图片 | 0,2 | 0 | - | 0 | 0 |
| 15300 | aime_aime_voice_langpage_PageShow | 元素埋点 | aime_Ainvest Aime_语音选择广场_语言选择_页面展示 | aime | 语音选择广场 | 语言选择 | 页面展示 | 0,2 | 1 | state | 0 | 0 |
| 15299 | aime_aime_voice_langpage_langClick | 元素埋点 | aime_Ainvest Aime_语音选择广场_语言选择_对应语言选择 | aime | 语音选择广场 | 语言选择 | 对应语言选择 | 0 | 1 | itemId | 0 | 0 |
| 15298 | aime_aime_voice_voicepage_PageShow | 元素埋点 | aime_Ainvest Aime_语音选择广场_音色选择_页面展示 | aime | 语音选择广场 | 音色选择 | 页面展示 | 2,0 | 1 | state | 0 | 0 |
| 15301 | aime_aime_voice_voicepage_langClick | 元素埋点 | aime_Ainvest Aime_语音选择广场_音色选择_对应语言选择 | aime | 语音选择广场 | 音色选择 | 对应语言选择 | 0 | 1 | itemId | 0 | 0 |
| 12657 | aime_aime_screenerPage | 页面埋点 | aime_Ainvest Aime_选股落地页 | aime | 选股落地页 | - | - | 0,2 | 0 | - | 0 | 0 |
| 5615 | aime_aime_screenerPage_ScreenPage_View | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_去查看 | aime | 选股落地页 | 选股落地页 | 去查看 | 0 | 0 | - | 0 | 0 |
| 5612 | aime_aime_screenerPage_ScreenPage_addWatch | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_加自选 | aime | 选股落地页 | 选股落地页 | 加自选 | 0 | 0 | - | 0 | 0 |
| 5613 | aime_aime_screenerPage_ScreenPage_addfollow | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_加关注 | aime | 选股落地页 | 选股落地页 | 加关注 | 0 | 1 | state | 0 | 0 |
| 5614 | aime_aime_screenerPage_ScreenPage_seceltWatchlist | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_选择自选列表 | aime | 选股落地页 | 选股落地页 | 选择自选列表 | 0 | 0 | - | 0 | 0 |
| 5611 | aime_aime_screenerPage_ScreenPage_share | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_分享 | aime | 选股落地页 | 选股落地页 | 分享 | 0 | 0 | - | 0 | 0 |
| 5610 | aime_aime_screenerPage_ScreenPage_tabcontent | 元素埋点 | aime_Ainvest Aime_选股落地页_选股落地页_tab选项 | aime | 选股落地页 | 选股落地页 | tab选项 | 0,2 | 1 | content | 0 | 0 |
| 11649 | aime_iwc_aimetalk_answerFinish_show | 元素埋点 | aime_iwencai_aime对话页_答案完全展示_显示 | iwc | aime对话页 | 答案完全展示 | 显示 | 2 | 2 | logId, stayLen | 0 | 0 |
| 11650 | aime_iwc_aimetalk_answerInterrupt_show | 元素埋点 | aime_iwencai_aime对话页_答案截断_显示 | iwc | aime对话页 | 答案截断 | 显示 | 2 | 3 | logId, stayLen, state | 0 | 0 |
| 11647 | aime_iwc_aimetalk_answerStart_show | 元素埋点 | aime_iwencai_aime对话页_答案内容展示_显示 | iwc | aime对话页 | 答案内容展示 | 显示 | 2 | 2 | logId, stayLen | 0 | 0 |
| 11648 | aime_iwc_aimetalk_answer_show | 元素埋点 | aime_iwencai_aime对话页_答案_显示 | iwc | aime对话页 | 答案 | 显示 | 2 | 2 | logId, stayLen | 0 | 0 |
| 11645 | aime_iwc_aimetalk_firstBubble_show | 元素埋点 | aime_iwencai_aime对话页_Thinking内容返回_显示 | iwc | aime对话页 | Thinking内容返回 | 显示 | 2 | 2 | logId, stayLen | 0 | 0 |
| 11646 | aime_iwc_aimetalk_thinkingPlan_show | 元素埋点 | aime_iwencai_aime对话页_Thinking规划返回_显示 | iwc | aime对话页 | Thinking规划返回 | 显示 | 2 | 2 | logId, stayLen | 0 | 0 |
| 10595 | aime_web_aimeweb_inputBox_sign | 元素埋点 | aime_Ainvest Web_aime网页对话_对话输入框(inputBox)_登录 | web | aime网页对话 | 对话输入框(inputBox) | 登录 | 0,2 | 0 | - | 0 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### aime_aime_aimePortconbottom_touchConsent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | 确认用户点击，并存储下来 | object | 0 |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### aime_aime_canvas

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | 不同的comefrom老远 | string | 0,1,2 |

### aime_aime_canvas_creat_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | - | string | 1,0,2 |

### aime_aime_canvas_detail_create

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 计算组件从确认创建到宣称完成的完整耗时 | int | 0,2 |

### aime_aime_canvas_list_detail

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 计算用户从点击查看看板详情到最终完全展示的时间 | int | 0,1,2 |

### aime_aime_canvas_navigation_create

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | 不同的用户来源 | string | 0,2,1 |
| 停留时长 | stayLen | 计算看板从确认创建到渲染完成的最终耗时 | int | 0,2 |

### aime_aime_explore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,1,2 |

### aime_aime_explore_Aimetab_more

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_Aimetab_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | - | int | 4 |
| 会话id | sessionId | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 携带跳哪个tab的字段 | string | 0,1 |

### aime_aime_explore_clickShared_askTopic

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |

### aime_aime_explore_clickShared_cancelUp

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_clickShared_closebutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0 |

### aime_aime_explore_clickShared_content

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 2,1,4 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 2,1 |

### aime_aime_explore_clickShared_portfolioshare

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 会话id | sessionId | - | string | 0 |

### aime_aime_explore_clickShared_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_contest_askquestions

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_latest

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_lottery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_more

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 0 |

### aime_aime_explore_contest_mostLikes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_mostShares

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_myPrompt

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_contest_queryList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为埋点 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_contest_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_contest_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的问句内容 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |

### aime_aime_explore_exploreTab_switch

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 点击按钮后，用户看到页面的状态是卡片还是列表 | enum | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | 当前问句所在tab | string | 0 |

### aime_aime_explore_exploreTab_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,1,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录点击tab选项时不同tab名称 | string | 0,1,2 |
| 停留时长 | stayLen | - | int | 4 |

### aime_aime_explore_explore_foruCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | state 表示用户在卡片上的点击状态， 需要根据用户点击行为传入想对应的枚举值： state = like 用户点赞 state = unlike 用户取消点赞 state = follow 用户关注 state = unfollow 用户取消关注 state = dislike 点踩 state = undislike 取消点踩 state = news_click 用户点击新闻跳转 state = send_query 用户发送问句 | enum | 0 |
| 描述推荐相关的参数 | recInfo | 卡片曝光和点击时都需要带上推荐相关字段，方便识别用户看过、点击过的物品 | string | 0,2 |

### aime_aime_explore_explorecategories_myFav

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 记录用户行为 | string | 0 |

### aime_aime_explore_inputBox_input

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_inputBox_sendQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_morefunction_AimeProfile

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_morefunction_allsetting

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_morefunction_broadcast

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 记录语音播报的开、关状态 | string | 0 |

### aime_aime_explore_morefunction_feedback

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 记录用户行为 | string | 0 |

### aime_aime_explore_morefunction_livsupport

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 记录用户信息 | string | 0 |

### aime_aime_explore_myfavor_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 记录用户行为 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录问句内容 | string | 0 |

### aime_aime_explore_myfavor_disCollect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_explore_pushShare_askquestions

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 运营平台对应的push id，content推送内容的title | pushId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | Push的问句名称等 | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_explore_pushShare_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 运营平台对应的push id，content推送内容的title | pushId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_explore_pushShare_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 运营平台对应的push id，content推送内容的title | pushId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_explore_pushShare_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 运营平台对应的push id，content推送内容的title | pushId | push对应的内容 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_explore_queryDetail_askquestions

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | 对应的tab页面 | string | 0 |

### aime_aime_explore_queryDetail_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 收藏的问句内容 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | - | string | 0 |

### aime_aime_explore_queryDetail_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 分享的问句详情 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | 对应的tab页面 | string | 0 |

### aime_aime_explore_queryDetail_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | 对应的tab页面 | string | 0 |

### aime_aime_explore_queryDetails_clickShared

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句点击详情 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 可点击的菜单表头名称 | tab | 对应的tab页面 | string | 0 |

### aime_aime_explore_queryList_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容记录 | string | 0 |

### aime_aime_explore_queryList_disCollect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录问句内容 | string | 0 |

### aime_aime_explore_queryList_queryCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句名称 | string | 0 |

### aime_aime_explore_share_sharecancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_share_shareface

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_share_sharelink

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_share_sharetwitter

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_explore_share_whatsApp

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句类型 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_webexplore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,1,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录用户点击的是explore还是aime对话按钮 | string | 0,1,2 |

### aime_aime_webexplore_clickShared_askTopic

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |

### aime_aime_webexplore_clickShared_portfolioshare

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 会话id | sessionId | - | string | 0 |

### aime_aime_webexplore_clickShared_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_webexplore_contest_askquestions

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_webexplore_contest_latest

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_webexplore_contest_mostLikes

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_webexplore_contest_mostShares

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_webexplore_contest_myPrompt

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_webexplore_contest_queryList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为埋点 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_webexplore_contest_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id，一次会话表示一次连接服务端 | session_id | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_webexplore_contest_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句的领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的问句内容 | string | 0 |

### aime_aime_webexplore_exploreTab_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,1,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录点击tab选项时不同tab名称 | string | 0,1,2 |
| 停留时长 | stayLen | - | int | 4 |

### aime_aime_webexplore_queryList_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容记录 | string | 0 |

### aime_aime_webexplore_queryList_disCollect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录问句内容 | string | 0 |

### aime_aime_webexplore_queryList_queryCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句名称 | string | 0 |

### aime_aime_aimeApp_Aimetab_userCenter

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_Googlelog_googLogIn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_IOSlog_appleLogIn

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_LS_emaPhone

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0 |

### aime_aime_aimeApp_emaiCreate_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_emailSignin_continueLogin

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_emailSignin_forPass

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_emailSignin_phoneSin

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_phoneSignin_continue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_phoneSignin_emailSin

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_rbtCen_ads

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | banner的内容，比如推广链接 | string | 0,2 |

### aime_aime_aimeApp_rbtCen_changePic

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_rbtCen_editName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_rbtCen_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | tab内可操作的项目：例如message、setting | string | 0 |

### aime_aime_aimeApp_setting_logout

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimeApp_setting_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | tab中选项的内容，如userID、Clear Cache、Notification、Language、About Aime、Update、Account&Security Privacy Agreement | string | 0,2 |
| 会话id | sessionId | - | string | 0,2 |

### aime_aime_aimeApp_sms_inputBox

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimetalk

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 4,2,1,8 |
| 停留时长 | stayLen | 用户停留时长或首屏加载时长 | int | 4,8 |

### aime_aime_aimetalk_Aimetab_moreFunction

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0,2 |

### aime_aime_aimetalk_DR_link

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | comefrom | string | 0,2 |

### aime_aime_aimetalk_DR_viewAll

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | comefrom | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0,2 |
| 答案的标识 | logId | 问句id | string | 0,2 |
| 描述推荐相关的参数 | recInfo | 推荐信息 | string | 2,0 |

### aime_aime_aimetalk_Inputlock_upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |

### aime_aime_aimetalk_Mulpoint_upgradeaime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |

### aime_aime_aimetalk_Taghint_taghint

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |

### aime_aime_aimetalk_Upgrade_Upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_activeRecom_aimeexplain

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 答案的标识 | logId | - | string | 0,2 |

### aime_aime_aimetalk_activeRecom_heatTopic

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 可点击的菜单表头名称 | tab | 记录用户点击的热点词 | string | 0,2 |
| 渠道,来源 | source | 用户进入的渠道来源， web还是app | string | 0,2 |

### aime_aime_aimetalk_activeRecom_heatTopicQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述推荐相关的参数 | recInfo | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 曝光的问句内容 | string | 0,2 |
| 可点击的菜单表头名称 | tab | 用户有滑动行为的tab | string | 1 |
| 渠道,来源 | source | 用户来的渠道来源，web 还是app | string | 0,2,1 |
| 标记列表行数 | num | 记录当前问句列表页面的位置 | int | 2,0 |
| 组件id，描述是什么组件 | groupId | 记录当前问句列表是第几页 | string | 0,2,1 |

### aime_aime_aimetalk_activeRecom_insightWatchlistAlrt

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | state=code 为点击股票，state=query 为点击问句 | enum | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户点击的内容， 用户点击代码时放入相关代码， 用户点击问句放入问句 | string | 0 |
| 描述推荐相关的参数 | recInfo | 推荐展示的字段 | string | 0,2 |
| 组件id，描述是什么组件 | groupId | 问句顺序， 最上面的气泡为1， 下面的气泡为2 | string | 0 |

### aime_aime_aimetalk_activeRecom_tkPanel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 标记列表行数 | num | 第几个问句 | int | 2,0 |
| 入口 | from | 用户来源渠道comefrom | string | 2,0 |
| 会话id | sessionId | - | string | 2,0 |
| 停留时长 | stayLen | 问句从用户进入到展示完成的耗时 | int | 2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 主动式推荐的问句内容 | string | 2,0 |
| 物品id | itemId | - | string | 2,0 |
| 描述推荐相关的参数 | recInfo | - | string | 2,0 |
| 类型 | type | 物品自身的投资标签 | string | 2,0 |
| 召回算法 | recallName | - | string | 2,0 |
| 功能类型 | function | 主动式分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 2,0 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 0,2 |
| 模式 | mode | 主动式的类别,目前分为文字类型的和页卡类型，用Text和Card区分 | string | 0,2 |

### aime_aime_aimetalk_activepage_activequery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击时触发的问句，需要包含技能名，问句 | string | 0 |
| 入口 | from | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_activepage_afterVotingQueries

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道,来源 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击问句之后，采集用户曝光和点击。 | string | 0,2 |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0,2 |
| 答案的标识 | logId | - | string | 0,2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0,2 |

### aime_aime_aimetalk_activepage_aimeprofile

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 答案的标识 | logId | - | string | 2 |

### aime_aime_aimetalk_activepage_insightForecastQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述推荐相关的参数 | recInfo | 推荐相关字段 | string | 0,2 |

### aime_aime_aimetalk_activepage_insightNewsQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | state = news 为 点击新闻，state = query 为点击问句 | enum | 0 |
| 描述推荐相关的参数 | recInfo | 推荐相关参数 | string | 0,2 |

### aime_aime_aimetalk_activepage_insightSwipe

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | state=analyze 用户点击现在分析 state=watchlist 用户点击加自选 | enum | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户滑动到股票代码，曝光的股票代码 | string | 2,0,1 |
| 描述推荐相关的参数 | recInfo | 推荐相关字段 | string | 2,0 |
| 渠道,来源 | source | source = recommend 为推荐透出结果页， source = chat 对话透出的高定结果页 | string | 0,2,1 |

### aime_aime_aimetalk_activepage_polling

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道,来源 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0,2 |
| 答案的标识 | logId | - | string | 0,2 |
| 扩展字段集合，用于承载业务相关字段 | logmap | - | object | 0,2 |

### aime_aime_aimetalk_addPanel_queryClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |
| 类型 | type | 反馈的问句领域 | string | 0 |

### aime_aime_aimetalk_aiChatArea_leaveTalk

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | 问句id、用户id以及回答时间 | string | 5,2 |

### aime_aime_aimetalk_aimeHome_more

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0,2 |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimetalk_aimeHome_newChat

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_aimeHome_recQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,1,2 |
| 入口 | from | - | string | 0,2 |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |
| 描述推荐相关的参数 | recInfo | - | string | 0,1 |

### aime_aime_aimetalk_aimeMemMsg_cancelbutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 被删除记忆的内容 | string | 0 |
| 答案的标识 | logId | 对话的traceId | string | 0 |
| 物品id | itemId | 被删除记忆的id | string | 0 |

### aime_aime_aimetalk_aimeMemMsg_functioncard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记忆的内容 | string | 2 |
| 答案的标识 | logId | 对话的traceId | string | 2 |
| 物品id | itemId | 记忆的id | string | 2 |

### aime_aime_aimetalk_aimeprofile_adjust

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_aimeprofile_livetv

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的内容名称positions或者orders | string | 0 |

### aime_aime_aimetalk_aimeprofile_tabSwift

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的物品类别，stock 或者crypto | string | 0 |

### aime_aime_aimetalk_answer_deepThought

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句 | string | 0 |

### aime_aime_aimetalk_bottomQuickInput_bottomButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 包含Pattern Screening、Trend Prediction、Select & Analyze、Feedback、Visualization、Document Q&A、Image Q&A | string | 0 |

### aime_aime_aimetalk_bottomQuickInput_subtab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用数字1-16从上到下从左往右表示各个子tab | string | 0 |

### aime_aime_aimetalk_bottomQuickInput_unlockPro

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimetalk_broadcastpodcast_broadcast1

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 枚举值为“broadcast”、“podcast”，分别代表播客和播报 | string | 2,0 |
| 标题 | title | - | string | 0,2 |

### aime_aime_aimetalk_collect_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |
| 答案的标识 | logId | 结果页收藏统计 | string | 0 |
| 渠道 | source | 渠道 | string | 0 |
| 入口 | from | comefrom | string | 0 |

### aime_aime_aimetalk_collect_disCollect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |

### aime_aime_aimetalk_diafufei_unlock

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 触发类型，问句输入：typewrite问句点击：click | string | 0,2 |
| 答案的标识 | logId | 问句id | string | 2,0 |
| 物品id | itemId | 付费产品id | string | 2,0 |
| 停留时长 | stayLen | - | int | 2,0 |
| 会话id | sessionId | - | string | 2,0 |

### aime_aime_aimetalk_diagRe_levelcard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 触发类型，问句输入：typewrite问句点击：click | string | 0,2 |
| 答案的标识 | logId | 问句id | string | 2,0 |
| 物品id | itemId | 付费产品id | string | 2,0 |
| 会话id | sessionId | - | string | 2,0 |

### aime_aime_aimetalk_diagRe_unlock

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 触发类型，问句输入：typewrite问句点击：click | string | 0,2 |
| 答案的标识 | logId | 问句id | string | 2,0 |
| 物品id | itemId | 付费产品id | string | 2,0 |
| 会话id | sessionId | - | string | 2,0 |

### aime_aime_aimetalk_diagRe_upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |

### aime_aime_aimetalk_explore_foruCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 描述推荐相关的参数 | recInfo | 卡片曝光和点击时都需要带上推荐相关字段，方便识别用户看过、点击过的物品 | string | 0,2 |
| 状态 | state | state 表示用户在卡片上的点击状态， 需要根据用户点击行为传入想对应的枚举值： state = like 用户点赞 state = unlike 用户取消点赞 state = follow 用户关注 state = unfollow 用户取消关注 state = dislike 点踩 state = undislike 取消点踩 state = news_click 用户点击新闻跳转 state = send_query 用户发送问句 | enum | 0 |

### aime_aime_aimetalk_fdPanel_cancel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |

### aime_aime_aimetalk_fdPanel_confirm

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 带上确认提交的反馈问题 | string | 0 |

### aime_aime_aimetalk_fdPanel_fdQues

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 带上确认提交的反馈问题 | string | 0 |

### aime_aime_aimetalk_feedbackDetails_feedbackContent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 类型 | type | 用户选择的反馈勾选的类型 | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 数值 | value | 用户反馈输入的内容 | string | 0 |

### aime_aime_aimetalk_feedback_down

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 2,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈问句的内容 | string | 0 |
| 类型 | type | 反馈问句的领域 | string | 0 |
| 答案的标识 | logId | 统计结果页点踩 | string | 0 |
| 渠道 | source | 渠道 | string | 0 |
| 入口 | from | comefrom | string | 0 |

### aime_aime_aimetalk_feedback_more

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 2,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈问句的内容 | string | 0 |
| 类型 | type | 反馈问句的领域 | string | 0 |

### aime_aime_aimetalk_feedback_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |
| 类型 | type | 反馈的问句领域 | string | 0 |
| 答案的标识 | logId | 统计结果页点赞 | string | 0 |
| 渠道 | source | 渠道 | string | 0 |
| 入口 | from | comefrom | string | 0 |

### aime_aime_aimetalk_fintuneAime_save

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_guide_queryClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句 | string | 0 |
| 会话id | sessionId | 用户行为记录 | string | 0,1 |

### aime_aime_aimetalk_history_disCollect

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |
| 类型 | type | 反馈的问句领域 | string | 0 |

### aime_aime_aimetalk_inputBox_addPanel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_aimetalk_inputBox_input

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_aimetalk_inputBox_openVoice

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_aimetalk_inputBox_sendQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 对话问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 发送的对话问句 | string | 0 |
| 类型，用于type的补充 | childType | 根据唤起的场景，如果是探索，增加探索{tab类别}_问句内容 ；如果是push 增加探索push_问句内容 | string | 0 |

### aime_aime_aimetalk_inputBox_tkPanel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 物品自身的投资标签 | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |
| 答案的标识 | logId | 当前问句的logid | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 会话id | sessionId | - | string | 0,2 |
| 描述推荐相关的参数 | recInfo | - | string | 0,2 |
| 召回算法 | recallName | - | string | 0,2 |
| 物品id | itemId | - | string | 0,2 |
| 功能类型 | function | 分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 0,2 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 0,2 |
| 状态 | state | 对话前active 或 对话后 after | enum | 0,2 |

### aime_aime_aimetalk_list_slide

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 滑动时长 | int | 1 |
| 答案的标识 | logId | 最新一条log_id | string | 1 |
| 方向 | direct | 滑动方向（上下） | string | 1 |

### aime_aime_aimetalk_lpFb_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### aime_aime_aimetalk_lpFb_contest

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为分析 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### aime_aime_aimetalk_lpFb_down

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句 | string | 0 |
| 类型 | type | 反馈的问句类型 | string | 0 |
| 答案的标识 | logId | 问句id | string | 0 |
| 渠道 | source | 渠道 | string | 0 |
| 入口 | from | comefrom | string | 0 |

### aime_aime_aimetalk_lpFb_feedback

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句 | string | 0 |
| 类型 | type | 反馈的问句类型 | string | 0 |

### aime_aime_aimetalk_lpFb_up

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句 | string | 0 |
| 类型 | type | 反馈的问句类型 | string | 0 |
| 答案的标识 | logId | 问句id | string | 0 |
| 渠道 | source | 渠道 | string | 0 |
| 入口 | from | comefrom | string | 0 |

### aime_aime_aimetalk_memoryToast_content

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |

### aime_aime_aimetalk_memorypage_remove

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### aime_aime_aimetalk_modelSwitch_buttons

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_modelSwitchmenu_Upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 模型使用次数用完后的升级按钮（目前有深度思考以及专业研究两个） | string | 0 |
| 渠道,来源 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_modelSwitchmenu_feedback

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_modelSwitchmenu_login

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_modelSwitchmenu_type

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 选择的模型类型 | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_more_agent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimetalk_more_aimeprofile

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_more_aimequestion

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击时的问句内容 | string | 0 |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimetalk_more_dna

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_more_explore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimetalk_more_newChat

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 2,0 |
| 入口 | from | - | string | 0,2 |
| 会话id | sessionId | - | string | 0,2 |

### aime_aime_aimetalk_more_setting

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimetalk_more_tab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | tab的名称，History或者Favorite | string | 0,2 |

### aime_aime_aimetalk_morefunction_AimeProfile

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0 |

### aime_aime_aimetalk_morefunction_clearthecontext

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | - | string | 0 |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### aime_aime_aimetalk_morefunction_feedback

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0 |

### aime_aime_aimetalk_morefunction_livesupport

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_aimetalk_morefunction_setting

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 行为记录 | string | 0 |

### aime_aime_aimetalk_morefunction_upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_multiModalInput_uploadFilePreview

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | URL、Image、file 三种类型 | string | 0 |

### aime_aime_aimetalk_naviBar_avatar

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_aimetalk_naviBar_quit

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |

### aime_aime_aimetalk_naviBar_voice

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 状态 | state | 描述喇叭状态，开启传1，关闭传0 | enum | 0 |

### aime_aime_aimetalk_regenerateFeedback_better

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 前一个问句的logid | preLogId | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_regenerateFeedback_same

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 前一个问句的logid | preLogId | - | string | 0 |

### aime_aime_aimetalk_regenerateFeedback_switchAnswer

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_regenerateFeedback_worse

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 前一个问句的logid | preLogId | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_screenResult_Rank

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |

### aime_aime_aimetalk_screenResult_source

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 对应用户问句 | string | 0 |
| 渠道 | source | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimetalk_screenResult_stockName

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 股票代码 | stock | 点击的股票名 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |

### aime_aime_aimetalk_searchresult_gomore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 答案的标识 | logId | - | string | 0,2 |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |

### aime_aime_aimetalk_shareContest_createCon

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为分析 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_aimetalk_skillpopup_skillchoosed

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 选择的那个skill | string | 0 |

### aime_aime_aimetalk_sourcePopUp_Traceable link 

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | 日志信息 | string | 0,2 |
| 描述ABtest实验id的字段，用逗号分隔 | experInfo | 实验 | string | 2,0 |
| 位置 | position | 序号 | string | 0 |
| 物品id | itemId | 文章ID | string | 0 |

### aime_aime_aimetalk_stateRemind_display

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | 停留时长 | int | 4 |

### aime_aime_aimetalk_stateRemind_leaveTalk

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 扩展字段集合，用于承载业务相关字段 | logmap | 点确认键退出 | object | 0 |

### aime_aime_aimetalk_tkPanel_ansBubble

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0,1,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回的答案 | string | 2,1,0 |
| 类型 | type | 对话问句领域 | string | 2,1,0 |
| 答案的标识 | logId | 调用总控的log_id | string | 2,1,0 |
| 类型，用于type的补充 | childType | 组件类型 | string | 2,1,0 |

### aime_aime_aimetalk_tkPanel_ansLoading

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户问句内容 | string | 2 |
| 答案的标识 | logId | 调用总控的log_id | string | 2 |
| 停留时长 | stayLen | loading状态的等待时长 | int | 2 |
| 状态 | state | 区分状态是否超时，超时=1，未超时=0 | enum | 2 |

### aime_aime_aimetalk_tkPanel_ansResp

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 返回的答案 | string | 2 |
| 类型 | type | 对话问句领域 | string | 2 |
| 答案的标识 | logId | 调用总控的log_id | string | 2 |

### aime_aime_aimetalk_tkPanel_bottomTag

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 物品自身的投资标签 | string | 0,2,1 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2,1 |
| 答案的标识 | logId | 前一个问句的prelogid | string | 0,2,1 |
| 标记列表行数 | num | - | int | 0,2,1 |
| 入口 | from | - | string | 0,2,1 |
| 会话id | sessionId | - | string | 0,2,1 |
| 描述推荐相关的参数 | recInfo | - | string | 2,0,1 |
| 物品id | itemId | - | string | 2,0,1 |
| 召回算法 | recallName | - | string | 2,0,1 |
| 功能类型 | function | 底部tag分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 2,0,1 |
| 透传id，用于关联股票、涨跌幅等信息，推荐业务使用 | impsId | 推荐唯一识别符，pageid+userid+时间戳 | string | 0,1,2 |

### aime_aime_aimetalk_tkPanel_contest

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_aimetalk_tkPanel_dialogCutOff

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id，一次会话表示一次连接服务端 | session_id | - | string | 2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 增加comefrom、source等附加信息 | string | 2 |

### aime_aime_aimetalk_tkPanel_firstBub

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户问句内容 | string | 2 |
| 答案的标识 | logId | 调用总控的log_id | string | 2 |
| 停留时长 | stayLen | 生成步骤的时长 | int | 2 |

### aime_aime_aimetalk_tkPanel_intradayChart

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 股票代码或公司名称 | string | 0,2 |
| 会话id | sessionId | 用户行为记录 | string | 0,2 |
| 页面业务来源 | from | 用户来源comefrom | string | 2,0 |

### aime_aime_aimetalk_tkPanel_lenovo

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 2,1,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 推荐问句的内容 | string | 2 |
| 页面业务来源 | from | comefrom | string | 2,1,0 |
| 标记列表行数 | num | lenovoId，输入联想的序号数，第几列联想 | int | 0 |

### aime_aime_aimetalk_tkPanel_linkTracing

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 溯源链接 | string | 0,2 |
| 入口 | from | 用户来源comefrom | string | 2,0 |
| 答案的标识 | logId | logId | string | 0,2 |
| 物品id | itemId | 文章信息 | string | 0 |
| 描述ABtest实验id的字段，用逗号分隔 | experInfo | 实验信息 | string | 0 |
| 位置 | position | 序号 | string | 0 |

### aime_aime_aimetalk_tkPanel_moreLinksButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0,2 |
| 页面业务来源 | from | 用户来源comefrom | string | 2,0 |

### aime_aime_aimetalk_tkPanel_moreTrace

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录问句 | string | 0 |

### aime_aime_aimetalk_tkPanel_regenerate

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | - | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |
| 入口 | from | - | string | 0 |
| 渠道 | source | - | string | 0 |
| 扩展字段集合，用于承载业务相关字段 | logmap | style | object | 0 |

### aime_aime_aimetalk_tkPanel_resultPage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 2,4 |
| 答案的标识 | logId | - | string | 2,4 |
| 停留时长 | stayLen | - | int | 4 |
| 类型 | type | 图表类型 | string | 2,4 |
| 页面业务来源 | from | - | string | 2,4 |
| 模式 | mode | 0:历史session, 1:当前session | string | 4,2 |

### aime_aime_aimetalk_tkPanel_resultPageGraph

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |
| 答案的标识 | logId | - | string | 0 |
| 类型 | type | 图表类型 | string | 0 |
| 页面业务来源 | from | - | string | 0 |

### aime_aime_aimetalk_tkPanel_role

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 人设字段，字段内容为【Aime、Ray Dalio、Bill Ackman、Warren Buffett】 | string | 0,2 |
| 会话id | sessionId | 用户行为id | string | 2,0 |
| 入口 | from | 用户来源comefrom | string | 2,0 |

### aime_aime_aimetalk_tkPanel_share

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 入口 | from | 说明用户从何种方式进入的 | string | 0 |
| 会话id | sessionId | - | string | 0 |
| 类型 | type | 对话的领域 | string | 0 |
| 答案的标识 | logId | 问句id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |
| 渠道 | source | 渠道 | string | 0 |

### aime_aime_aimetalk_tkPanel_shareform

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型，用于type的补充 | childType | 分享的形式，如Image、Link | string | 0 |
| 入口 | from | - | string | 0,2 |
| 会话id | sessionId | - | string | 0,2 |
| 答案的标识 | logId | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0,2 |
| 类型 | type | 对话的领域 | string | 0,2 |
| 渠道 | source | - | string | 2,0 |

### aime_aime_aimetalk_tkPanel_trace

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 要带上溯源链接 | string | 0,2 |
| 物品id | itemId | 文章id | string | 0,2 |
| 位置 | position | 序号位置 | string | 0 |
| 描述ABtest实验id的字段，用逗号分隔 | experInfo | AB实验 | string | 0 |
| 答案的标识 | logId | 用户信息 | string | 0 |

### aime_aime_aimetalk_tkPanel_tracePopUp

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 记录点击溯源的链接 | string | 0 |

### aime_aime_aimetalk_tkPanel_traceability

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 溯源链接 | string | 0,2 |
| 会话id | sessionId | 用户行为记录 | string | 0,2 |
| 入口 | from | 用户来源comefrom | string | 2,0 |
| 答案的标识 | logId | logId | string | 0,2 |
| 位置 | position | 序号位置 | string | 0 |
| 物品id | itemId | 文章的id | string | 0 |
| 描述ABtest实验id的字段，用逗号分隔 | experInfo | ab实验 | string | 0 |

### aime_aime_aimetalk_tkPanel_userQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 9,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 9,2 |
| 答案的标识 | logId | - | string | 0 |

### aime_aime_aimetalk_topbanner_unlock

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id（0；10012；10013） | string | 0,2 |

### aime_aime_aimetalk_voiInput_endVoice

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 反馈的问句内容 | string | 0 |
| 类型 | type | 反馈的问句领域 | string | 0 |

### aime_aime_aimetalk_voice_moreFunction

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句 | string | 0 |

### aime_aime_aimetalk_voice_switchLatestStatus

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 0关闭，1打开 | enum | 8 |

### aime_aime_chatTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 2 |

### aime_aime_chatTheme_Theme_huTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 0 |

### aime_aime_chatTheme_Theme_techTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 0 |

### aime_aime_chatTheme_Theme_tradTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 0 |

### aime_aime_chatTheme_naviBar_quit

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为 | string | 0 |

### aime_aime_aimemix_aimeEverywhere_aimeNewUserGuide

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 判断是否手动关闭相关新手引导弹窗，如果关闭枚举值为ManualClose，进入Aime 为 ButtonEntry | enum | 0,2 |
| 模式 | mode | 判断目前展示的是三行threeline 还是 四行fourline 样式 | string | 2,0 |

### aime_aime_aimeweb

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 停留时长 | stayLen | - | int | 4 |
| 入口 | from | 从插件、product、悬浮机器人等不同的渠道进入Aime web对话 | string | 0,2,4 |

### aime_aime_aimeweb_Inputlock_upgrade

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |
| 入口 | from | 判断进入机器人的来源：如快讯右边栏机器人 | string | 0,2 |

### aime_aime_aimeweb_Subplans_Aimepro

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |
| 类型 | type | 点击类型（月\|年、购买、底部信息） | string | 0,2 |
| 渠道 | source | web | string | 0,2 |
| 入口 | from | 判断进入机器人的来源：如快讯右边栏机器人 | string | 0,2 |

### aime_aime_aimeweb_Taghint_taghint

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |
| 入口 | from | 判断进入机器人的来源：如快讯右边栏机器人 | string | 0,2 |

### aime_aime_aimeweb_activeRecom_tkPanel

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 主动式推荐的问句内容 | string | 0,2 |
| 功能类型 | function | 主动式分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 0,2 |

### aime_aime_aimeweb_aimeHome_explore

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimeweb_aimeHome_history

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimeweb_aimeHome_newChat

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0 |
| 入口 | from | - | string | 0 |

### aime_aime_aimeweb_aimeHome_recquestions

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,2 |
| 会话id | sessionId | - | string | 0 |
| 描述推荐相关的参数 | recInfo | - | string | 0,2 |

### aime_aime_aimeweb_aimeHome_switchTab

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,1 |
| 入口 | from | - | string | 0,1 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,1 |

### aime_aime_aimeweb_dialogDetail_details

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | - | string | 4,2,0,1 |
| 请求地址 | url | - | string | 4,end,1,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 4,2,1,0 |
| 停留时长 | stayLen | - | int | 4 |

### aime_aime_aimeweb_function_subsCard

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |
| 入口 | from | 判断进入机器人的来源：如快讯右边栏机器人 | string | 0,2 |

### aime_aime_aimeweb_list_slide

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | log_id | string | 1 |
| 停留时长 | stayLen | 滑动时长 | int | 1 |
| 方向 | direct | 方向 | string | 1 |

### aime_aime_aimeweb_naviBar_askAime

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 页面业务来源 | from | 关注从哪个功能页进入对话 | string | 0 |

### aime_aime_aimeweb_naviBar_collectQue

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 能力类型 | string | 3,2,1,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 具体问句内容 | string | 3,2,1,0 |
| 答案的标识 | logId | 问句id | string | 0 |

### aime_aime_aimeweb_naviBar_recQuery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 物品自身的投资标签 | string | 3,2,1,0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 3,2,1,0 |
| 答案的标识 | logId | 前一个问句的prelogid | string | 2,1,0,3 |
| 标记列表行数 | num | - | int | 3,2,1,0 |
| 描述推荐相关的参数 | recInfo | - | string | 2,1,0 |
| 物品id | itemId | - | string | 2,1,0 |
| 召回算法 | recallName | - | string | 2,1,0 |
| 功能类型 | function | 底部tag分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 0,2,1 |
| 描述ABtest实验id的字段，用逗号分隔 | experInfo | 算法AB实验id | string | 2,0,1 |

### aime_aime_aimeweb_shareContest_createCon

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |

### aime_aime_aimeweb_tkPanel_activequery

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 渠道 | source | - | string | 0,2 |
| 入口 | from | - | string | 0,2 |

### aime_aime_aimeweb_tkPanel_bottomTag

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 类型 | type | 物品自身的投资标签 | string | 0,1,2 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0,1,2 |
| 答案的标识 | logId | 前一个问句的prelogid | string | 0,1,2 |
| 标记列表行数 | num | - | int | 0,1,2 |
| 入口 | from | - | string | 0,1,2 |
| 会话id | sessionId | - | string | 0,1,2 |
| 召回算法 | recallName | - | string | 0,1,2 |
| 功能类型 | function | 底部tag分发类型，枚举值：rec、basic、opera（推荐、兜底、运营） | string | 0,1,2 |
| 物品id | itemId | 推荐唯一识别符，pageid+userid+时间戳 | string | 2,1,0 |

### aime_aime_aimeweb_tkPanel_contest

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 问句内容 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |

### aime_aime_robotCenter

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id记录 | string | 2,4 |

### aime_aime_robotCenter_rbtCen_chatTheme

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id记录 | string | 2,4 |

### aime_aime_robotCenter_rbtCen_faq

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 触发携带的问句 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |

### aime_aime_robotCenter_rbtCen_research

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 触发携带的问句 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |

### aime_aime_robotCenter_rbtCen_screener

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | 用户行为id记录 | string | 0 |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 触发携带的问句 | string | 0 |
| 类型 | type | 问句领域 | string | 0 |

### aime_aime_robotCenter_setting_everywhereswitch

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 开关状态：on、off | enum | 0 |

### aime_aime_landingpage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 产品id | string | 0,2 |
| 类型 | type | 点击类型（月、年+购买信息+底部信息） | string | 0,2 |
| 渠道 | source | 来源渠道：ainvest、aime | string | 0,2 |

### aime_aime_roleplay_craeteCharacter_createButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 会话id | sessionId | - | string | 0 |

### aime_aime_roleplay_createCharacterlist_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 各个tab的内容，包含preofile、memory、knowledge、skill | string | 0 |

### aime_aime_roleplay_rateInterest_rate

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 数值 | value | 记录具体评分数值 | string | 0 |
| 类型 | type | 提交评分时归属的具体栏目：Memory、Knowledge、Skill | string | 0 |

### aime_aime_roleplay_selectGuru_guruList

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击的人设头像信息：比如aime、buffet、dalio\ackman等 | string | 0 |

### aime_aime_AgentStore_memorypage_forgot

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | - | string | 0 |

### aime_aime_socialLandingPage

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 页面是否打开 | enum | 2 |

### aime_aime_socialLandingPage_aimeQuestion_aimeQuestionBlock

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 问句是否被展示 | enum | 2 |
| 标记列表行数 | num | 问句是否被点击 | int | 0 |

### aime_aime_memory_aimeMemDisp_chatButton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 组件id，描述是什么组件 | groupId | 卡片的名称，例如analysis_approach | string | 0 |

### aime_aime_memory_aimeMemDisp_deletebutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 被删除记忆的内容 | string | 0 |
| 答案的标识 | logId | 被删除记忆的trace_id | string | 0 |

### aime_aime_memory_aimeMemDisp_savebutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 用户输入的内容 | string | 0 |

### aime_aime_voice_langpage_PageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 语言选择页曝光 | enum | 2 |

### aime_aime_voice_langpage_langClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 不用语种的选择次数 | string | 0 |

### aime_aime_voice_voicepage_PageShow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 音色选择页页面曝光 | enum | 2 |

### aime_aime_voice_voicepage_langClick

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 物品id | itemId | 音色选择点击量 | string | 0 |

### aime_aime_screenerPage_ScreenPage_addfollow

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 状态 | state | 点击后的状态，包含follow、unfollow | enum | 0 |

### aime_aime_screenerPage_ScreenPage_tabcontent

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 埋点触发时，携带的内容信息，如问句内容、发言 | content | 点击tab的类型，如：introduce、filters | string | 0,2 |

### aime_iwc_aimetalk_answerFinish_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |

### aime_iwc_aimetalk_answerInterrupt_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |
| 状态 | state | 0用户主动断开；1用户退出或者断网 | enum | 2 |

### aime_iwc_aimetalk_answerStart_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |

### aime_iwc_aimetalk_answer_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |

### aime_iwc_aimetalk_firstBubble_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |

### aime_iwc_aimetalk_thinkingPlan_show

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 答案的标识 | logId | logid | string | 2 |
| 停留时长 | stayLen | 耗时 | int | 2 |
