#!/usr/bin/env python3
"""Build CONTEXT.md and/or CONTEXT_PACK.md for handoff / sub-agent dispatch.

Usage:
  python tools/session/build_context.py
  python tools/session/build_context.py --skill execution
  python tools/session/build_context.py --skill planning --pack --check
  python tools/session/build_context.py --rules-only

--pack writes CONTEXT_PACK.md (Rules-first envelope for workers).
--check fails if Rules (mandatory) block is missing or incomplete.
Legacy default still writes CONTEXT.md for same-runtime execution handoff.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SOURCES = (
    "DISCUSSION.md",
    "QUICK.md",
    "BUSINESS_ANALYSIS.md",
    "BASIC_DESIGN.md",
    "DETAIL_DESIGN.md",
    "PLAN.md",
    "TASKS.md",
    "INVESTIGATE.md",
    "RESEARCH.md",
    "REVIEW.md",
    "SYNC.md",
)

SKILL_HEADINGS: dict[str, tuple[str, ...]] = {
    "default": (
        "executive summary",
        "developer overview",
        "goal",
        "recommendation",
        "handoff",
        "approach",
        "definition of done",
        "problem statement",
        "scope",
        "keywords",
    ),
    "planning": (
        "executive summary",
        "developer overview",
        "goal",
        "recommendation",
        "approach",
        "definition of done",
        "handoff",
    ),
    "execution": (
        "executive summary",
        "developer overview",
        "goal",
        "approach",
        "definition of done",
        "handoff",
    ),
    "investigate": (
        "executive summary",
        "developer overview",
        "question",
        "recommendation",
        "doc reality check",
        "keywords",
    ),
    "review": (
        "executive summary",
        "developer overview",
        "recommendation",
        "handoff",
    ),
    "brainstorming": (
        "executive summary",
        "developer overview",
        "goal",
        "recommendation",
        "keywords",
        "spec quality review",
    ),
    "basic-design": (
        "executive summary",
        "developer overview",
        "goal",
        "doc reality check",
        "handoff",
    ),
    "detail-design": (
        "executive summary",
        "developer overview",
        "goal",
        "doc reality check",
        "handoff",
    ),
    "research": (
        "executive summary",
        "developer overview",
        "question",
        "recommendation",
        "keywords",
    ),
}

OUTPUT_HINTS: dict[str, str] = {
    "planning": "Write/update `PLAN.md` + `TASKS.md` in the active session only.",
    "execution": "Implement in-repo per TASK card; update `EXECUTION.md` + TASKS progress.",
    "investigate": "Write/update `INVESTIGATE.md` in the active session only.",
    "review": "Write/update `REVIEW.md` in the active session only.",
    "brainstorming": "Write/update `DISCUSSION.md` in the active session only.",
    "basic-design": "Write/update `BASIC_DESIGN.md` in the active session only.",
    "detail-design": "Write/update `DETAIL_DESIGN.md` in the active session only.",
    "research": "Write/update `RESEARCH.md` in the active session only.",
    "default": "Write only the session artifacts named in Mission / Output contract.",
}

RULES_NEEDLES = (
    "## Rules (mandatory)",
    "## Language",
    "## Work layout",
    "## Confirm-first",
    "## Safety",
    "## Output contract",
    "Ask method",
    ".agent-work/",
)


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".agents").is_dir() or (candidate / ".agent-work").is_dir():
            return candidate
        if (candidate / "docs" / "artifact-schemas.json").is_file():
            return candidate
    return start.resolve()


def resolve_session(root: Path, explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit)
        if not path.is_absolute():
            path = root / path
        if not path.is_dir():
            raise SystemExit(f"Session dir not found: {path}")
        return path
    pointer = root / ".agent-work" / "sessions" / ".current"
    if not pointer.is_file():
        raise SystemExit("No active session. Pass --session or run session.sh new/set.")
    rel = pointer.read_text(encoding="utf-8").splitlines()[0].strip()
    path = root / rel
    if not path.is_dir():
        raise SystemExit(f"Active session missing: {rel}")
    return path


def rules_template_path(root: Path) -> Path:
    here = Path(__file__).resolve().parent
    for p in (
        root / ".agents" / "tools" / "session" / "RULES_BUNDLE.template.md",
        root / "tools" / "session" / "RULES_BUNDLE.template.md",
        here / "RULES_BUNDLE.template.md",
    ):
        if p.is_file():
            return p
    raise SystemExit("RULES_BUNDLE.template.md not found under tools/session/")


def load_rules_bundle(root: Path) -> str:
    text = rules_template_path(root).read_text(encoding="utf-8").strip()
    # Normalize title for pack heading
    if text.startswith("# Rules bundle"):
        body = text.split("\n", 1)[1].lstrip() if "\n" in text else ""
        return "## Rules (mandatory)\n\n" + body
    if text.startswith("## Rules"):
        return text
    return "## Rules (mandatory)\n\n" + text


def check_rules_block(text: str) -> list[str]:
    missing = [n for n in RULES_NEEDLES if n not in text]
    return missing


def extract_sections(text: str, headings: tuple[str, ...], limit: int = 80) -> str:
    lines = text.splitlines()
    want = {h.casefold() for h in headings}
    chunks: list[str] = []
    i = 0
    while i < len(lines):
        m = re.match(r"^##\s+(.+?)\s*$", lines[i])
        if not m:
            i += 1
            continue
        title = m.group(1).strip()
        key = title.casefold()
        matched = any(key == w or key.startswith(w) for w in want)
        i += 1
        body: list[str] = []
        while i < len(lines) and not re.match(r"^##\s+", lines[i]):
            body.append(lines[i])
            i += 1
        if matched:
            trimmed = "\n".join(body).strip()
            if trimmed:
                chunks.append(f"### {title}\n\n{trimmed}")
    out = "\n\n".join(chunks)
    out_lines = out.splitlines()
    if len(out_lines) > limit:
        out = "\n".join(out_lines[:limit]) + "\n\n…(truncated)"
    return out


def project_digest(root: Path, limit: int = 40) -> str:
    for rel in (".agents/PRJ_REFERENCE.md", "docs/PRJ_REFERENCE.md"):
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        block = extract_sections(
            text,
            (
                "executive summary",
                "technology stack",
                "key constraints",
                "verified commands",
                "agent clis",
            ),
            limit,
        )
        return block or f"_(see {rel})_"
    return "_(no PRJ_REFERENCE.md — run init / detect_agents)_"


def build_legacy_context(session: Path, skill: str) -> str:
    headings = SKILL_HEADINGS.get(skill, SKILL_HEADINGS["default"])
    parts = [
        "# CONTEXT (compact handoff pack)",
        "",
        "> Auto-built for execution. Prefer this + active TASK card Dev context.",
        "> Do not invent beyond Sources. Regenerate: "
        "`python .agents/tools/session/build_context.py`",
        f"> skill={skill}",
        "",
    ]
    found = 0
    for name in SOURCES:
        path = session / name
        if not path.is_file():
            continue
        found += 1
        text = path.read_text(encoding="utf-8")
        parts.append(f"## From {name}")
        parts.append("")
        if name == "TASKS.md":
            inv = extract_sections(text, ("Work inventory", "Execution order"), 40)
            parts.append(inv or "_(see TASKS.md)_")
        else:
            block = extract_sections(text, headings, 60)
            parts.append(block or "_(see source file)_")
        parts.append("")
    if found == 0:
        return ""
    return "\n".join(parts).rstrip() + "\n"


def build_pack(root: Path, session: Path, skill: str, mission: str) -> str:
    rules = load_rules_bundle(root)
    headings = SKILL_HEADINGS.get(skill, SKILL_HEADINGS["default"])
    hint = OUTPUT_HINTS.get(skill, OUTPUT_HINTS["default"])
    rel_session = str(session.relative_to(root)) if session.is_relative_to(root) else str(session)

    parts: list[str] = [
        "# CONTEXT_PACK (sub-agent envelope)",
        "",
        "> Built for worker CLIs. Obey **Rules (mandatory)** verbatim.",
        "> Main must refuse dispatch if `--check` fails. Sources only — do not invent.",
        f"> skill={skill} session={rel_session}",
        "",
        rules,
        "",
        "## Mission",
        "",
        mission.strip()
        or f"Run skill `{skill}` for session `{rel_session}`. Return artifacts per Output contract.",
        "",
        "## Constraints",
        "",
        "- Path scale: honor Quick/Lite/Full in Developer overview when present.",
        "- cwd: repository root (product). Artifacts only under the active session.",
        "- Do not modify `.agents/skills` or kit policy files.",
        "- If Blocking: stop and Ask-back to main (see Ask-back protocol).",
        "",
        "## Project digest",
        "",
        project_digest(root),
        "",
        "## Decision so far",
        "",
    ]

    decision_bits: list[str] = []
    for name in SOURCES:
        path = session / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if name == "TASKS.md":
            continue
        block = extract_sections(text, headings, 50)
        if block:
            decision_bits.append(f"### From {name}\n\n{block}")
    parts.append("\n\n".join(decision_bits) if decision_bits else "_(none yet)_")
    parts.append("")

    tasks = session / "TASKS.md"
    if tasks.is_file():
        parts.extend(
            [
                "## Task scope",
                "",
                extract_sections(
                    tasks.read_text(encoding="utf-8"),
                    ("Work inventory", "Execution order"),
                    50,
                )
                or "_(see TASKS.md)_",
                "",
            ]
        )

    parts.extend(
        [
            "## Output contract",
            "",
            hint,
            f"- Session dir: `{rel_session}`",
            "- Headings stay English; prose follows settings.language.",
            "",
            "## Ask-back protocol",
            "",
            "If Blocking clarity is missing, do **not** guess. Return to main:",
            "",
            "| Ask method | Question | Why blocking |",
            "|---|---|---|",
            "| confirm / choice / fact / table / diagram / html | _(one question)_ | _(one line)_ |",
            "",
            "Status for the skill: `blocked` until main confirms.",
            "",
        ]
    )
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", help="Session dir (default: .current)")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument(
        "--skill",
        default="default",
        help="Skill id for section selection / output hints (e.g. planning, execution)",
    )
    parser.add_argument(
        "--pack",
        action="store_true",
        help="Write CONTEXT_PACK.md (Rules-first worker envelope)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate Rules (mandatory) in pack text; exit 1 if incomplete",
    )
    parser.add_argument(
        "--rules-only",
        action="store_true",
        help="Print Rules bundle to stdout and exit",
    )
    parser.add_argument("--mission", default="", help="Override Mission paragraph")
    args = parser.parse_args()
    root = args.root.resolve() if args.root else find_root(Path.cwd())
    skill = args.skill.strip() or "default"

    if args.rules_only:
        print(load_rules_bundle(root))
        return 0

    session = resolve_session(root, args.session)

    if args.pack or args.check:
        pack = build_pack(root, session, skill, args.mission)
        missing = check_rules_block(pack)
        if missing:
            print("CONTEXT_PACK_RULES_FAIL missing=" + ",".join(missing), file=sys.stderr)
            if args.check:
                return 1
        if args.pack:
            out = session / "CONTEXT_PACK.md"
            out.write_text(pack, encoding="utf-8")
            print(f"CONTEXT_PACK_OK path={out}")
        if args.check and not missing:
            print("CONTEXT_PACK_CHECK_OK")
        if args.check and missing:
            return 1
        if args.pack or args.check:
            # Also refresh legacy CONTEXT when packing for convenience
            legacy = build_legacy_context(session, skill)
            if legacy:
                (session / "CONTEXT.md").write_text(legacy, encoding="utf-8")
            return 0

    legacy = build_legacy_context(session, skill)
    if not legacy:
        print("CONTEXT_BUILD_EMPTY", file=sys.stderr)
        return 1
    out = session / "CONTEXT.md"
    out.write_text(legacy, encoding="utf-8")
    print(f"CONTEXT_OK path={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
