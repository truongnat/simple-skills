#!/usr/bin/env python3
"""Validate the Wave 0/Wave 1 boundary contract for the lifecycle skill cluster."""

from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGETS = (
    "sk-ba-dashboard",
    "sk-ba-handoff",
    "sk-ba-integrate",
    "sk-ba-kg",
    "sk-ba-test",
    "sk-basic-design",
    "sk-brainstorming",
    "sk-detail-design",
    "sk-discussing-pro",
    "sk-gap-analysis",
    "sk-init",
    "sk-investigate",
    "sk-quick-fix",
)
LEGACY_TEMPLATE = re.compile(
    r"owns development lifecycle, requirements analysis, planning, specification, "
    r"review, and delivery handoffs",
    re.I,
)
STALE_GENERIC_HANDOFF = re.compile(
    r"sk-review and sk-verification for quality evidence",
    re.I,
)


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.I | re.M)
    if not match:
        return ""
    tail = text[match.end() :]
    next_heading = re.search(r"^##\s+", tail, re.M)
    return tail[: next_heading.start()] if next_heading else tail


def main() -> int:
    failures: list[str] = []
    boundaries: dict[str, str] = {}

    for name in TARGETS:
        path = ROOT / "skills" / name / "SKILL.md"
        if not path.is_file():
            failures.append(f"{name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        body = section(text, "Boundary")
        if not body:
            failures.append(f"{name}: missing ## Boundary section")
            continue
        boundaries[name] = " ".join(body.split())
        if LEGACY_TEMPLATE.search(body):
            failures.append(f"{name}: legacy generic lifecycle Boundary remains")
        for marker in ("Primary artifact:", "Handoff:"):
            if marker.lower() not in body.lower():
                failures.append(f"{name}: Boundary lacks {marker}")
        if not re.search(r"does\s+(?:\*\*)?not(?:\*\*)?\s+own|do\s+(?:\*\*)?not(?:\*\*)?\s+own|not\s+own", body, re.I):
            failures.append(f"{name}: Boundary lacks explicit non-ownership clause")

    for left, right in itertools.combinations(sorted(boundaries), 2):
        if boundaries[left] == boundaries[right]:
            failures.append(f"{left} and {right}: identical Boundary text")

    for path in sorted((ROOT / "skills").glob("sk-*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if STALE_GENERIC_HANDOFF.search(text):
            failures.append(f"{path.relative_to(ROOT)}: stale facade-as-owner handoff")

    verification = (ROOT / "skills" / "sk-verification" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    canonical = (ROOT / "skills" / "sk-verify-pro" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    if "sk-verify-pro" not in verification or "compatibility" not in verification.lower():
        failures.append("sk-verification: facade must delegate to sk-verify-pro")
    if "canonical verification owner" not in canonical.lower():
        failures.append("sk-verify-pro: canonical verification ownership is not explicit")

    if failures:
        print("Boundary contract validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Boundary contract validation: PASS ({len(TARGETS)} target skills)")
    print("- every target has artifact owner, non-ownership clause and canonical handoff")
    print("- no target retains the bulk-remediation lifecycle template")
    print("- target Boundaries are pairwise distinct")
    print("- no generic handoff treats sk-verification as a peer final owner")
    print("- sk-verification facade and sk-verify-pro canonical owner are explicit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
