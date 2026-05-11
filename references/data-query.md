# 埋点数据查询

当前 skill 的埋点数据查询采用“agent 生成 SQL，CLI 只执行 SQL”的模式。CLI 不负责拼 SQL，不做表检索，也不做字段元数据检索。

## CLI 能力

- `data preview`：调用 EasyFetch `/v2/tool/data/fetch` 预览 SQL 结果
- `data download`：调用 EasyFetch `/v2/tool/data/fetch_presto_download` 下载 CSV 到本地
- `data explain`：对 SQL 执行 `EXPLAIN`
- `data config`：查看 EasyFetch 连接配置，不输出证书密码

## 边界

可以做：

- 根据用户问句和知识库定位候选埋点 `trackKey` / `stat_id`
- 生成并执行简单 SQL，返回埋点明细、埋点列表、UV、PV 等查询结果
- 按时间、应用、页面、区块、元素、`stat_id` 等字段做基础筛选、分组和排序
- 下载查询结果到本地 CSV

不做：

- 不解释指标上涨、下降、波动的业务原因
- 不做漏斗、留存、转化、归因、异常检测、趋势诊断或人群洞察
- 不基于查询结果给产品、运营或业务策略建议
- 不把多个指标拼成结论性分析报告

当用户提出“为什么下降”“原因是什么”“帮我分析”“给建议”等分析型问题时，先明确当前 skill 只能查询埋点数据；可以继续帮助用户把问题拆成可查询的 UV、PV、明细或埋点列表 SQL，并返回原始查询结果。

## 固定查询表

- 数据源：`presto-hive`
- 数据库：`hx_dwd`
- 表名：`dwd_log_mob_unified_track_hs`
- 完整表名：`hx_dwd.dwd_log_mob_unified_track_hs`
- 表中文名：统一版SDK埋点明细数据
- 时间字段：`log_time`
- 日期分区：`p_date`
- 小时分区：`p_hour`
- 埋点字段：`stat_id`
- UV 口径字段：`user_id`
- PV 口径：`COUNT(*)`

可用字段：

```text
user_id, log_time, stat_id, action_id, app_version, device_id, platform,
platform_version, log_version, from_stat_id, from_page_id, logmap, ip,
send_time, recv_time, id, app_cold_start_id, seq_id, host_app, pod_ip,
is_new_user, is_inner_user, app_name, p_date, p_hour
```

## SQL 生成规则

1. 判断查询类型：埋点明细、埋点列表、UV、PV。
2. 如果用户给的是自然语言埋点描述，先用知识库定位候选 `trackKey`，确认后作为 `stat_id`；如果用户直接给 `stat_id`，直接使用。
3. 解析时间范围，必须生成 `p_date` 分区条件；小时级查询再补 `p_hour` 条件；明细查询可同时加 `log_time` 范围。
4. Agent 自己生成完整 SQL，不调用脚本拼 SQL。
5. 先执行 `data explain`，再执行 `data preview`；用户需要全量数据时再执行 `data download`。

## SQL 模板

PV 查询：

```sql
SELECT
  COUNT(*) AS pv
FROM hx_dwd.dwd_log_mob_unified_track_hs
WHERE p_date >= '20260501'
  AND p_date <= '20260507'
  AND stat_id = 'ths_demo_click';
```

UV 查询：

```sql
SELECT
  COUNT(DISTINCT NULLIF(user_id, '')) AS uv
FROM hx_dwd.dwd_log_mob_unified_track_hs
WHERE p_date >= '20260501'
  AND p_date <= '20260507'
  AND stat_id = 'ths_demo_click';
```

明细查询：

```sql
SELECT
  log_time,
  stat_id,
  action_id,
  user_id,
  device_id,
  platform,
  app_version,
  from_stat_id,
  from_page_id,
  logmap,
  id,
  p_date,
  p_hour
FROM hx_dwd.dwd_log_mob_unified_track_hs
WHERE p_date >= '20260501'
  AND p_date <= '20260507'
  AND stat_id = 'ths_demo_click'
ORDER BY log_time DESC
LIMIT 100;
```

埋点列表查询：

```sql
SELECT
  stat_id,
  COUNT(*) AS pv,
  COUNT(DISTINCT NULLIF(user_id, '')) AS uv
FROM hx_dwd.dwd_log_mob_unified_track_hs
WHERE p_date >= '20260501'
  AND p_date <= '20260507'
GROUP BY stat_id
ORDER BY pv DESC
LIMIT 1000;
```

## 执行 SQL

Agent 生成 SQL 后，将完整 SQL 作为参数传给 CLI：

```sh
manage-tracking --json data explain --datasource-name presto-hive --sql "<SQL>"
manage-tracking --json data preview --datasource-name presto-hive --sql "<SQL>"
manage-tracking --json data download --datasource-name presto-hive --sql "<SQL>" --project-path .
```

也可以把 SQL 写入临时 `.sql` 文件后执行：

```sh
manage-tracking --json data preview --datasource-name presto-hive --sql-file query.sql
```

下载文件会保存到：

```text
data_file/intermediate/tracking_query_result_<timestamp>.csv
```

EasyFetch 配置读取顺序：

- `--easy-fetch-url`，或 `MANAGE_TRACKING_EASY_FETCH_BASE_URL` / `EASY_FETCH_BASE_URL`
- 若未显式传 EasyFetch URL，会按 SQL 环境选择默认地址：`ainvest` 使用 `https://cbas-gateway.ainvest.com:1443/sdmp/easyfetch`，`prod` / `dev` / `test` / `dreamface` 使用 `https://phonestat.hexin.cn/sdmp/easyfetch`
- SQL 环境读取顺序：`--sql-env` > 顶层 `--env` > `THS_TIER` > 当前 session 环境
- SQL 环境也用于将 `starrocks` 映射为 `starrocks-claude`；固定埋点明细表是 Hive 表，默认使用 `presto-hive`
- `CBAS_EMAIL` / `MANAGE_TRACKING_EMAIL` / SkillHub 共享配置中的 `user_email`
- `SSL_CERT_FILE` / `SSL_CERT_PASSWORD` 或 SkillHub 共享证书配置
