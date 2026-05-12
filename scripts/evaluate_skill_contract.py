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
    check(isinstance(routing_cases, list) and len(routing_cases) >= 6, "routing evals must include at least 6 cases.")
    check(any(case.get("expect_load") is False for case in routing_cases), "routing evals must include negative cases.")
    check(any("references/data-query.md" in case.get("expected_file_reads", []) for case in routing_cases), "routing evals must require data-query progressive loading.")
    check(isinstance(progressive_cases, list) and progressive_cases, "progressive_loading evals must be present.")

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
