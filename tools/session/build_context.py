#!/usr/bin/env python3
"""Build a compact CONTEXT.md from session artifacts (handoff pack).

Usage:
  python tools/session/build_context.py
  python .agents/tools/session/build_context.py --session .agent-work/sessions/Task-1-x
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
        # match startswith for "Executive summary" etc.
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", help="Session dir (default: .current)")
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve() if args.root else find_root(Path.cwd())
    session = resolve_session(root, args.session)

    parts = [
        "# CONTEXT (compact handoff pack)",
        "",
        "> Auto-built for execution. Prefer this + active TASK card Dev context.",
        "> Do not invent beyond Sources. Regenerate: "
        "`python .agents/tools/session/build_context.py`",
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
            # Keep inventory + first two cards lightly
            inv = extract_sections(text, ("Work inventory", "Execution order"), 40)
            parts.append(inv or "_(see TASKS.md)_")
        else:
            block = extract_sections(
                text,
                (
                    "executive summary",
                    "developer overview",
                    "goal",
                    "recommendation",
                    "handoff",
                    "approach",
                    "definition of done",
                    "problem statement",
                    "scope",
                ),
                60,
            )
            parts.append(block or "_(see source file)_")
        parts.append("")

    if found == 0:
        print("CONTEXT_BUILD_EMPTY", file=sys.stderr)
        return 1

    out = session / "CONTEXT.md"
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"CONTEXT_OK path={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
