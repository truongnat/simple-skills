#!/usr/bin/env python3
"""Validate the Group 01 skill contract without third-party dependencies."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DOCS = ROOT / "docs"
NAMES = """sk-api-ba sk-ba-dashboard sk-ba-handoff sk-ba-integrate sk-ba-kg sk-ba-test sk-basic-design sk-brainstorming sk-business-analysis sk-detail-design sk-discussing-pro sk-done sk-executing-pro sk-execution sk-gap-analysis sk-grill-me-pro sk-init sk-investigate sk-planning sk-quick-fix sk-review sk-review-pr sk-scaffold sk-specify sk-story-spec sk-sync sk-tester sk-to-issues-pro sk-to-prd-pro sk-user-flow sk-ux-wireframe sk-verification sk-verify-pro""".split()
REQUIRED = {"name", "description", "sk-kind", "sk-version", "sk-tags", "sk-roles", "sk-compatible"}
ALLOWED_KINDS = {"process", "domain"}
ALLOWED_STATES = {"todo", "in_progress", "blocked", "skipped", "complete", "partial"}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values


def check_markdown(name: str, text: str, errors: list[str]) -> None:
    if text.count("```") % 2:
        errors.append(f"{name}: unbalanced fenced code blocks")
    if "§ Gates C." in text or "git sk-init" in text:
        errors.append(f"{name}: known malformed contract text remains")


def main() -> int:
    errors: list[str] = []
    seen_aliases: dict[str, str] = {}
    for name in NAMES:
        path = SKILLS / name / "SKILL.md"
        if not path.exists():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            meta = frontmatter(text)
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
            continue
        missing = REQUIRED - meta.keys()
        if missing:
            errors.append(f"{name}: missing metadata {sorted(missing)}")
        if meta.get("sk-kind") not in ALLOWED_KINDS:
            errors.append(f"{name}: invalid sk-kind {meta.get('sk-kind')!r}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", meta.get("sk-version", "")):
            errors.append(f"{name}: sk-version must be semver")
        if not meta.get("sk-tags", "").startswith("["):
            errors.append(f"{name}: sk-tags must be a list")
        if not meta.get("sk-roles", "").startswith("["):
            errors.append(f"{name}: sk-roles must be a list")
        aliases = re.search(r"^aliases:\s*\[(.*?)\]", text, re.M)
        if aliases:
            for alias in (a.strip() for a in aliases.group(1).split(",")):
                if alias:
                    previous = seen_aliases.setdefault(alias, name)
                    if previous != name:
                        errors.append(f"duplicate alias {alias!r}: {previous}, {name}")
        check_markdown(name, text, errors)
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).resolve().exists():
                errors.append(f"{name}: broken local link {target!r}")

    for name in NAMES:
        for path in (SKILLS / name).rglob("*"):
            if not path.is_file():
                continue
            try:
                bundled_text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "planning-pro" in bundled_text or "git sk-init" in bundled_text:
                errors.append(f"{name}: stale reference in {path.relative_to(ROOT)}")

    required_docs = [DOCS / "GROUP01_SESSION_ARTIFACTS.md", DOCS / "GROUP01_ROUTING.md"]
    for path in required_docs:
        if not path.exists():
            errors.append(f"missing shared contract: {path.relative_to(ROOT)}")

    execution = (SKILLS / "sk-execution" / "SKILL.md").read_text(encoding="utf-8")
    executing_pro = (SKILLS / "sk-executing-pro" / "SKILL.md").read_text(encoding="utf-8")
    verification = (SKILLS / "sk-verification" / "SKILL.md").read_text(encoding="utf-8")
    verify_pro = (SKILLS / "sk-verify-pro" / "SKILL.md").read_text(encoding="utf-8")
    if "canonical execution owner" not in executing_pro:
        errors.append("sk-executing-pro: missing canonical owner declaration")
    if "Compatibility role" not in execution:
        errors.append("sk-execution: missing compatibility facade declaration")
    if "canonical verification owner" not in verify_pro:
        errors.append("sk-verify-pro: missing canonical owner declaration")
    if "Compatibility role" not in verification:
        errors.append("sk-verification: missing compatibility facade declaration")
    for name, text in (("sk-executing-pro", executing_pro), ("sk-to-prd-pro", (SKILLS / "sk-to-prd-pro" / "SKILL.md").read_text()), ("sk-to-issues-pro", (SKILLS / "sk-to-issues-pro" / "SKILL.md").read_text())):
        if "planning-pro" in text:
            errors.append(f"{name}: stale planning-pro reference")

    if errors:
        print("GROUP01 VALIDATION: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"GROUP01 VALIDATION: PASS ({len(NAMES)} skills, metadata/ownership/docs/references checked)")
    print(f"Allowed states: {', '.join(sorted(ALLOWED_STATES))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
