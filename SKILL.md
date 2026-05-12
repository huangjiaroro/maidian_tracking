---
name: tracking-query
name_zh: 用户行为埋点查询
description: 当明确提及需要查询用户行为埋点的定义，明细数据和统计数据(如埋点的UV，PV)时触发
artifact_type: cli
runtime: python
python_version: 3.12.10
offline_install: true
entrypoint: tracking-query
---

# tracking-query

Use this skill for AInvest tracking questions:

- look up a `trackKey`
- reverse-search tracking candidates from page / section / element / button / scenario names
- confirm which app/page a candidate belongs to
- inspect relation coverage in the bundled wiki snapshot
- query PV / UV / detail data with SQL through the CLI

## First checks

- If you only need to confirm the wrapper works, run `tracking-query --json ping` once.
- Use `tracking-query --json config show` only when you need local config debugging.
- `--json` must appear immediately after `tracking-query`.
- Default to read-only commands. Only use `create` / `delete` when the user explicitly asks.

## Sources

Prefer the bundled wiki snapshot first. The fixed root is:

- `references/tracking-wiki/index.md`

Do not invent other roots or add `prod` / `ainvest` path variants.

Useful references:

- `references/tracking-wiki/concepts/query-playbook.md`
- `references/tracking-wiki/concepts/relation-model.md`
- `references/tracking-wiki/concepts/snapshot-sync.md`
- `references/data-query.md`

Key lookup files:

- `references/tracking-wiki/entities/lookups/page-lookup.md`
- `references/tracking-wiki/entities/lookups/section-lookup.md`
- `references/tracking-wiki/entities/lookups/element-lookup.md`
- `references/tracking-wiki/entities/apps/app-*.md`
- `references/tracking-wiki/entities/relations/`

Use full skill-relative paths when opening wiki files.

## Route The Query

Pick the first lookup by the clue type, not by the product name:

| User clue | Check first |
| --- | --- |
| 页面名 / “xx页” / 页面自然语言描述 | `page-lookup.md` |
| 区块、功能区、tab、模块 | `section-lookup.md` |
| 按钮、卡片、控件、CTA、列表项 | `element-lookup.md` |
| 直接给了 `trackKey` | CLI `track get-by-key` or exact wiki hit |
| PV / UV / 明细 / 埋点列表数据 | `references/data-query.md` |

Important:

- A page, section, or element may exist in multiple apps. Keep all candidates until the user explicitly narrows scope.
- Do not lock onto a single app just because the user said a product word like `aime` or `选股`.
- If wiki already gives an exact hit, answer from wiki first instead of paging through CLI lists.

## Default Workflow

### Natural-language reverse lookup

When the user did not provide a `trackKey`:

1. Read `references/tracking-wiki/concepts/query-playbook.md` if you need the detailed wiki workflow.
2. Search the correct lookup file first:
   - page name -> `page-lookup.md`
   - section name -> `section-lookup.md`
   - element / button name -> `element-lookup.md`
3. Keep cross-app candidates.
4. Open only the matching `entities/apps/app-*.md` files to confirm page name, `trackKey`, fields, and hierarchy.
5. If the wiki answer is precise enough, stop there and answer.
6. Use CLI only if wiki is insufficient or the user explicitly asks for a realtime check.

### Direct `trackKey` lookup

When the user already gave a `trackKey`:

1. Use `tracking-query --json track get-by-key --key <trackKey>`.
2. If you need wiki context such as app/page ownership or field notes, search the matching `app-*.md` file.

### Data queries

For PV, UV, detail rows, or track-list data:

1. Read `references/data-query.md`.
2. The agent writes SQL; the CLI only executes it.
3. Always include `p_date`; add `p_hour` for hourly queries.
4. Run `data explain` before `data preview`.
5. Run `data download` only when the user wants full data.

## Tool Rules

- Prefer `search_files` / `read_file` for wiki lookups.
- Open only the relevant snippets; avoid scanning whole app docs unless necessary.
- Use `execute_code` only for multi-step aggregation or de-duplication, not for a single keyword check.
- If a CLI subcommand or flag is uncertain, run the matching `--help` first.
- Do not assume CLI output is JSON unless the raw output is actually valid JSON.

Preferred precise CLI commands:

```sh
tracking-query track search <keyword>
tracking-query --json track get-by-key --key <trackKey>
```

Avoid unfiltered pagination as a discovery strategy:

- do not start with `app/page/section/element/track list`
- use `list` only when the user explicitly wants a list, or when you already have filters like `--app-id`, `--page-id`, or `--function-id`

## Answer Requirements

- Return `trackKey`, app, page, and section / element ownership when available.
- If there are multiple app candidates, list all of them and explain the difference.
- If you only found a page-level hit, do not invent section-level or element-level tracks.
- For relation questions, only describe relations present in the exported snapshot.
- If CLI and wiki disagree, state that clearly as realtime result vs snapshot result.
- In follow-up turns, continue from the current candidate instead of restarting the whole lookup flow.

## Implementation Notes

- `section` corresponds to backend `functionInfo`.
- `element` corresponds to backend `controlInfo`.
- If you need implementation details, inspect:
  - `tracking_query/cli.py`
  - `tracking_query/skillhub_entry.py`
  - `tracking_query/core/config.py`
  - `tracking_query/core/client.py`
  - `tracking_query/core/api.py`
