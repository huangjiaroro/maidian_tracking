#!/usr/bin/env python3
"""Validate the tracking-query skill contract and eval fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def parse_frontmatter(markdown: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", markdown, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML-style frontmatter.")

    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")
    return frontmatter


def iter_expected_file_reads(evals: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for section_name in ("routing", "progressive_loading"):
        for case in evals.get(section_name, []):
            for key in ("expected_file_reads", "forbidden_file_reads"):
                value = case.get(key, [])
                if isinstance(value, list):
                    paths.extend(str(item) for item in value)
    return paths


def iter_cases(evals: dict[str, Any]) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for section_name in ("routing", "progressive_loading"):
        section = evals.get(section_name, [])
        if isinstance(section, list):
            cases.extend(case for case in section if isinstance(case, dict))
    return cases


def case_has_nonempty_list(case: dict[str, Any], field: str) -> bool:
    value = case.get(field)
    return isinstance(value, list) and len(value) > 0


def main() -> int:
    failures: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    skill_md = read_text("SKILL.md")
    frontmatter = parse_frontmatter(skill_md)
    description = frontmatter.get("description", "")

    check(frontmatter.get("name") == "tracking-query", "SKILL.md name must be tracking-query.")
    check(len(description) <= 180, "description must stay concise; keep it at or below 180 characters.")
    check("明确提及" in description and "时触发" in description, "description must explain the explicit trigger condition.")
    check("用户行为埋点的定义" in description and "明细数据" in description, "description must cover tracking definitions and detail data.")
    check("统计数据" in description and "UV" in description and "PV" in description, "description must cover PV/UV-style tracking stats.")
    check("## 技能作用与触发" not in skill_md, "Do not duplicate trigger guidance in the loaded body.")
    check("references/data-query.md" in skill_md, "SKILL.md must point data queries to references/data-query.md.")
    check("wiki 知识库优先" in skill_md and "wiki 查不到" in skill_md, "SKILL.md must enforce wiki-first lookup with CLI fallback only when wiki misses.")
    check("list` 都是分页列表" in skill_md, "SKILL.md must warn that list commands are paginated and not preferred for candidate confirmation.")
    check("## 查询状态机" in skill_md, "SKILL.md must define an explicit query state machine.")
    for stage in ("`INIT`", "`LOOKUP`", "`APP_CONFIRM`", "`CLI_FALLBACK`", "`FOLLOWUP`", "`ERROR_RECOVERY`"):
        check(stage in skill_md, f"SKILL.md state machine missing stage {stage}.")
    check("状态转移规则" in skill_md, "SKILL.md must define stage transition rules.")
    check("多轮 continuation 约束" in skill_md and "继续上一个问题" in skill_md, "SKILL.md must describe continuation behavior for follow-up turns.")
    check("工具路径纪律" in skill_md and "references/tracking-wiki/entities/lookups/page-lookup.md" in skill_md, "SKILL.md must require full linked-file paths for skill_view lookups.")
    check("工具使用策略" in skill_md and "search_files` / `read_file" in skill_md, "SKILL.md must define tool-selection guidance for search_files/read_file when available.")
    check("不要重复调用 `skill_view(name=\"tracking-query\")`" in skill_md, "SKILL.md must prevent redundant skill reloads within the same question.")
    check("路径报错后，不要重新加载 skill" in skill_md and "修正成完整路径后继续当前查询" in skill_md, "SKILL.md must define recovery behavior for linked-file path errors.")
    check("track search <keyword>" in skill_md and "track get-by-key --key <trackKey>" in skill_md, "SKILL.md must prefer precise CLI fallback commands when wiki misses.")
    check("工具预算与禁用模式" in skill_md and "每个问题最多 1 次" in skill_md, "SKILL.md must define tool budgets for state-machine execution.")
    check("先运行 `tracking-query <entity> --help`" in skill_md, "SKILL.md must require help-first CLI probing when parameters are uncertain.")
    check("先查看原始输出" in skill_md and "合法 JSON" in skill_md, "SKILL.md must guard JSON parsing with raw-output inspection.")
    check("只读知识库" in skill_md and "不要修改其中任何文件" in skill_md, "SKILL.md must treat references/tracking-wiki as read-only.")
    check("FROM hx_dwd.dwd_log_mob_unified_track_hs" not in skill_md, "Heavy SQL templates must not live in SKILL.md.")

    data_query = read_text("references/data-query.md")
    check("FROM hx_dwd.dwd_log_mob_unified_track_hs" in data_query, "data-query reference must contain SQL templates.")
    check("必须生成 `p_date` 分区条件" in data_query, "data-query reference must preserve the p_date gotcha.")

    query_playbook = read_text("references/tracking-wiki/concepts/query-playbook.md")
    check("wiki 知识库优先" in query_playbook and "不要分页扫描 CLI" in query_playbook, "query playbook must preserve wiki-first behavior and avoid CLI pagination when wiki hits.")
    check("track search <keyword>" in query_playbook and "`list` 命令都是分页列表" in query_playbook, "query playbook must prefer precise CLI fallback over paginated list commands.")

    evals = json.loads(read_text("evals/skill-evals.json"))
    routing_cases = evals.get("routing", [])
    progressive_cases = evals.get("progressive_loading", [])
    all_cases = iter_cases(evals)
    check(isinstance(routing_cases, list) and len(routing_cases) >= 6, "routing evals must include at least 6 cases.")
    check(any(case.get("expect_load") is False for case in routing_cases), "routing evals must include negative cases.")
    check(any("references/data-query.md" in case.get("expected_file_reads", []) for case in routing_cases), "routing evals must require data-query progressive loading.")
    check(isinstance(progressive_cases, list) and progressive_cases, "progressive_loading evals must be present.")
    check(any(case.get("id") == "tracking-continuation-no-reload" for case in all_cases), "evals must include a continuation case that avoids reloading entry documents.")
    check(any(case.get("id") == "tracking-path-error-recovery" for case in all_cases), "evals must include a path-recovery case for linked-file lookup failures.")
    check(any(case.get("id") == "positive-wiki-miss-cli-fallback" for case in all_cases), "evals must include a precise CLI fallback case for wiki misses.")
    check(any(case.get("id") == "cli-help-first-before-element-list" for case in all_cases), "evals must include a help-first CLI case for uncertain element commands.")
    check(
        any(
            set(case.get("expected_answer_fields", [])) >= {"track_key", "app", "page", "section", "element"}
            for case in all_cases
        ),
        "evals must require answer-field coverage for natural-language tracking lookups.",
    )
    check(any(case_has_nonempty_list(case, "expected_stages") for case in all_cases), "evals must annotate expected state-machine stages.")
    check(any(case_has_nonempty_list(case, "expected_tool_order") for case in all_cases), "evals must annotate expected tool order.")
    check(any(case_has_nonempty_list(case, "forbidden_tools") for case in all_cases), "evals must annotate forbidden tools.")
    check(any(isinstance(case.get("max_tool_calls"), int) and case["max_tool_calls"] > 0 for case in all_cases), "evals must cap tool-call budgets for at least one case.")
    check(any(case_has_nonempty_list(case, "expected_recovery_behavior") for case in all_cases), "evals must describe expected recovery behavior for failure cases.")
    check(
        any(
            "references/tracking-wiki/index.md" in case.get("forbidden_file_reads", [])
            and "references/tracking-wiki/concepts/query-playbook.md" in case.get("forbidden_file_reads", [])
            for case in all_cases
        ),
        "evals must forbid re-reading index and query-playbook on continuation turns.",
    )
    check(
        any(
            "tracking-query track search <keyword>" in case.get("expected_cli_commands", [])
            and "tracking-query --json track get-by-key --key <trackKey>" in case.get("expected_cli_commands", [])
            for case in all_cases
        ),
        "evals must require precise CLI fallback commands for wiki misses.",
    )
    check(
        any(
            "tracking-query track list" in case.get("forbidden_cli_commands", [])
            for case in all_cases
        ),
        "evals must forbid paginated track list scans in CLI fallback cases.",
    )
    check(
        any(
            "tracking-query --json element get --element-id <elementId>" in case.get("forbidden_cli_commands", [])
            for case in all_cases
        ),
        "evals must forbid unsupported element get guesses in help-first CLI cases.",
    )

    for relative_path in iter_expected_file_reads(evals):
        check((ROOT / relative_path).exists(), f"Eval references missing file: {relative_path}")

    gitignore_lines = set(read_text(".gitignore").splitlines())
    ignored_reference_lines = {
        "references/",
        "references/tracking-wiki/",
    }
    check(not (gitignore_lines & ignored_reference_lines), "Do not ignore bundled tracking wiki references.")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Skill contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
