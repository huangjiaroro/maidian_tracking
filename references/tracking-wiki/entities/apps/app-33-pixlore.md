---
title: 应用 - Pixlore
type: entity
created: 2026-05-11
updated: 2026-05-11
sources:
  - raw/tracking/export-metadata.json
  - raw/tracking/overview.md
tags:
  - tracking
  - app
  - pixlore
  - ainvest
---

# Pixlore

## 概览

| 字段 | 值 |
| --- | --- |
| appId | 33 |
| appSign | Pixlore |
| appKey | 1c8ed5fc5b |
| creator | liugengyu@myhexin.com |
| createTime | 2025-09-23 19:49:52 |
| topicName | - |
| payloadStatus | 0 |
| pageCount(snapshot) | 2 |
| trackCount(snapshot) | 9 |
| relationTrackCount | 0 |
| tracksWithActionFields | 1 |

## 业务线汇总

| 业务线编码 | 页面数 | 埋点数 |
| --- | --- | --- |
| web | 2 | 9 |

## 页面清单

| pageId | pageShort | pageName | 截图数 | 埋点数 |
| --- | --- | --- | --- | --- |
| 1340 | pixlorechat | pixlorechat | 0 | 2 |
| 1339 | pixlorehomepage | pixlorehomepage | 0 | 7 |

## 关系枢纽埋点

暂无关系覆盖。

## 埋点清单

| trackId | trackKey | 埋点类型 | trackName | businessLine | 页面 | 区块 | 元素 | allowAction | 参数字段数 | 参数字段 | 前序数 | 后序数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13430 | Pixlore_web_pixlorechat_aiChatbox_inputBox | 元素埋点 | Pixlore_Ainvest Web_pixlorechat_AI对话框_输入框 | web | pixlorechat | AI对话框 | 输入框 | 0 | 0 | - | 0 | 0 |
| 13431 | Pixlore_web_pixlorechat_send_sendQuery | 元素埋点 | Pixlore_Ainvest Web_pixlorechat_发送_发送问句 | web | pixlorechat | 发送 | 发送问句 | 0 | 0 | - | 0 | 0 |
| 13421 | Pixlore_web_pixlorehomepage | 页面埋点 | Pixlore_Ainvest Web_pixlorehomepage | web | pixlorehomepage | - | - | 2 | 0 | - | 0 | 0 |
| 13425 | Pixlore_web_pixlorehomepage_Upgrade_paidUpgrade | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_升级_付费升级 | web | pixlorehomepage | 升级 | 付费升级 | 0 | 0 | - | 0 | 0 |
| 13422 | Pixlore_web_pixlorehomepage_button_generatebutton | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_按钮_生成按钮 | web | pixlorehomepage | 按钮 | 生成按钮 | 0 | 1 | url | 0 | 0 |
| 13423 | Pixlore_web_pixlorehomepage_install_chromeplugin | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_安装_chrome插件 | web | pixlorehomepage | 安装 | chrome插件 | 0 | 0 | - | 0 | 0 |
| 13427 | Pixlore_web_pixlorehomepage_navigation_chatButton | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_导航栏_开始对话 | web | pixlorehomepage | 导航栏 | 开始对话 | 0 | 0 | - | 0 | 0 |
| 13424 | Pixlore_web_pixlorehomepage_textinput_eventswitcharea | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_输入框_事件切换栏 | web | pixlorehomepage | 输入框 | 事件切换栏 | 0 | 0 | - | 0 | 0 |
| 13426 | Pixlore_web_pixlorehomepage_textinput_input | 元素埋点 | Pixlore_Ainvest Web_pixlorehomepage_输入框_输入框 | web | pixlorehomepage | 输入框 | 输入框 | 0 | 0 | - | 0 | 0 |

## 埋点字段明细

仅展开 `action_fields` 非空的埋点；字段来自 `track_info.csv`。

### Pixlore_web_pixlorehomepage_button_generatebutton

| 字段中文名 | 字段英文名 | 备注 | dataType | 适用动作 |
| --- | --- | --- | --- | --- |
| 请求地址 | url | 用户都转了哪些网站 UI | string | 0 |
