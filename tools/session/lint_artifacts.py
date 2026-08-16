#!/usr/bin/env python3
"""Lint session artifacts for readable quality (beyond heading schemas).

Usage:
  python tools/session/lint_artifacts.py
  python tools/session/lint_artifacts.py --session .agent-work/sessions/Task-1-x
  python .agents/tools/session/lint_artifacts.py

Includes thinking-method anti-pattern detection:
  - Activity-only Goals (Outcome-first violation)
  - Weak ACs that cannot be falsified
  - Mega-batch cards (Small-batch violation)
  - Missing Dev context or Source cites
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _work_settings import work_dir_name


FILLER = re.compile(
    r"\b("
    r"leverage|holistic|synerg(?:y|ies)|ensure consistency|"
    r"optimize the flow|align(?:ing)? stakeholders|"
    r"as an AI|I will now analyze|this section (?:covers|discusses)"
    r")\b",
    re.I,
)
TODO_LEFT = re.compile(r"_\(TODO|_(\.\.\.|| short title|name)_\)|_\(TODO", re.I)
SOURCE = re.compile(r"\[Source:\s*[^\]]+\]|No specific guidance found", re.I)

# ---------------------------------------------------------------------------
# Thinking-method anti-pattern patterns
# ---------------------------------------------------------------------------

# Activity-only Goal patterns (Outcome-first violation).
# Detects Goals that start with effort verbs, not observable outcomes.
ACTIVITY_GOAL_START = re.compile(
    r"^##\s+Goal\s*\n+"
    r"(?:(?!^##\s)[^\n]*\n)*?"  # do not cross next ## heading
    r"^\s*(?:[-*]\s+)?"
    r"(write|implement|refactor|fix|add|create|build|develop|integrate|"
    r"set up|configure|design|update|modify|change|move|remove|delete)\b",
    re.I | re.M,
)

# Weak AC patterns — cannot be falsified (Outcome-first / Small-batch violation).
# Matches formats like:
#   - **AC:** works.
#   **AC:** works
#   - AC: works.
#   AC: works
WEAK_AC = re.compile(
    r"(?:^\s*-\s*\*\*AC:\*\*\s*|"  # - **AC:** 
    r"^\s*\*\*AC:\*\*\s*|"  # **AC:** 
    r"^\s*-\s*AC[:\s]+|"  # - AC: or - AC 
    r"^\s*AC[:\s]+)"  # AC: or AC 
    r"(works|correct|done|implemented|finished|complete|per spec|"
    r"as designed|as expected|properly|correctly|good|fine|ok)\.?\s*$",
    re.I | re.M,
)

# Vague Verify patterns — do not name concrete check.
VAGUE_VERIFY = re.compile(
    r"(?:^\s*\*\*Verify[:\*]\*?\s*|^-\s*\*\*Verify[:\*]\*?\s*|"
    r"^Verify[:\s]+)"
    r"(manual (?:qa|testing)|will test later|tbd|as needed|"
    r"test when done|verify later|check manually|somehow)\.?\s*$",
    re.I | re.M,
)

# Mega-batch indicators — multiple endpoints/screens in one card.
MEGA_BATCH = re.compile(
    r"^###\s+T-\d+[^\n]*\b"
    r"(all (?:endpoints|screens|apis|routes|controllers)|"
    r"entire (?:module|service|feature|page)|"
    r"complete (?:CRUD|implementation|feature)|"
    r"full (?:page|module|implementation|stack)|"
    r"\d+ (?:endpoints|screens|apis|routes))\b",
    re.I | re.M,
)

# Layer-only card titles — no named unit (Small-batch violation).
LAYER_TITLE = re.compile(
    r"^###\s+T-\d+[:\s]+"
    r"(BE|FE|API|UI|DB|backend|frontend|database|service|controller)"
    r"(?:\s+(?:search|form|page|list|detail|create|update|delete))?\s*$",
    re.I | re.M,
)

# Process-only DoD — only PR/lint/merge milestones, no consumer outcome.
PROCESS_DOD = re.compile(
    r"^##\s+Definition of done\s*\n+"
    r"(?:[^\n]*\n)*?"
    r"(?:^\s*-\s*\[\s*\]\s*(?:PR|lint|review|merge|commit|CI|pipeline|deploy)\b.*\n)+"
    r"(?!.*(?:test|verify|check|assert|returns|shows|200|201|400|401|endpoint|field|message))",
    re.I | re.M,
)

# ---------------------------------------------------------------------------
# Readability patterns
# ---------------------------------------------------------------------------

# Empty section: heading followed only by HTML comments, blank lines, or _(TODO)_
EMPTY_SECTION = re.compile(
    r"^##\s+(.+?)\s*\n+"
    r"(?:"
    r"\s*<!--[^>]*-->\s*\n|"  # HTML comments
    r"\s*\n|"  # blank lines
    r"\s*_\(TODO\)_?\s*\n|"  # _(TODO)_
    r"\s*_…_\s*\n|"  # _…_
    r"\s*[-*]\s+_(TODO|…)_\s*\n"  # - _(TODO)_
    r")+"
    r"(?=^##\s|\Z)",
    re.M,
)

# Excessive file length threshold
MAX_FILE_LINES = 300

# Filler ratio: lines that are only filler / total non-blank lines
FILLER_RATIO_THRESHOLD = 0.15  # 15% filler = warning

# Translated template headings (must stay English for shared form).
VI_HEADING = re.compile(
    r"^#{1,3}\s+("
    r"Tóm tắt(?:\s+điều hành)?|"
    r"Tổng quan(?:\s+developer|\s+lập trình)?|"
    r"Mục tiêu|"
    r"Bối cảnh|"
    r"Kiểm tra thực tế(?:\s+tài liệu)?|"
    r"Câu hỏi(?:\s+đang mở)?|"
    r"Bàn giao|"
    r"Giả định|"
    r"Kiến trúc|"
    r"Thành phần|"
    r"Luồng(?:\s+người dùng)?|"
    r"Sở hữu dữ liệu|"
    r"Chất lượng đặc tả|"
    r"Phạm vi|"
    r"Khuyến nghị"
    r")\b",
    re.I | re.M,
)
VI_CHAR = re.compile(
    r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡ"
    r"ùúụủũưừứựửữỳýỵỷỹđ"
    r"ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ"
    r"ÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ]"
)


def read_language(root: Path) -> str:
    settings = root / ".agents" / "settings.yaml"
    if not settings.is_file():
        settings = root / "docs" / "config" / "settings.yaml"
    if not settings.is_file():
        return "en"
    for line in settings.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("#") or not s.startswith("language:"):
            continue
        val = s.split(":", 1)[1].strip().strip("\"'")
        return val.lower() if val else "en"
    return "en"


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".agents").is_dir() or (candidate / ".agent-work").is_dir():
            return candidate
        if (candidate / "docs" / "config" / "artifact-schemas.json").is_file():
            return candidate
        if (candidate / "docs" / "AGENTS.md").is_file():
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
    pointer = root / work_dir_name(root) / "sessions" / ".current"
    if not pointer.is_file():
        raise SystemExit("No active session. Pass --session or run session.sh new/set.")
    rel = pointer.read_text(encoding="utf-8").splitlines()[0].strip()
    path = root / rel
    if not path.is_dir():
        raise SystemExit(f"Active session missing: {rel}")
    return path


def path_is_quick(session: Path) -> bool:
    for name in ("DISCUSSION.md", "PLAN.md", "QUICK.md", "SYNC.md"):
        p = session / name
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        if re.search(r"\|\s*Path\s*\|\s*`?Quick`?", text, re.I):
            return True
        if re.search(r"Path:\s*Quick\b", text, re.I):
            return True
    return False


def lint_file(
    path: Path,
    errors: list[str],
    warnings: list[str],
    *,
    language: str = "en",
    check_thinking: bool = True,
) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.name
    if TODO_LEFT.search(text):
        errors.append(f"{rel}: leftover template TODO / placeholder")
    for m in FILLER.finditer(text):
        warnings.append(f"{rel}: filler phrase '{m.group(0)}'")
    for m in VI_HEADING.finditer(text):
        errors.append(
            f"{rel}: heading must stay English (shared form), not '{m.group(1)}' "
            f"— translate prose only (language={language})"
        )
    if language == "vi":
        body = strip_fences(text)
        # Ignore heading lines for prose-language signal.
        prose = "\n".join(
            ln for ln in body.splitlines() if not ln.lstrip().startswith("#")
        )
        letters = sum(1 for ch in prose if ch.isalpha())
        vi_hits = len(VI_CHAR.findall(prose))
        if letters >= 120 and vi_hits < 8:
            warnings.append(
                f"{rel}: language=vi but little Vietnamese prose "
                f"(vi_chars={vi_hits}) — avoid English-only body"
            )
    
    # -----------------------------------------------------------------------
    # Thinking-method anti-pattern detection
    # -----------------------------------------------------------------------
    if check_thinking:
        # Outcome-first: activity-only Goal
        if path.name in ("DISCUSSION.md", "PLAN.md", "QUICK.md"):
            if ACTIVITY_GOAL_START.search(text):
                errors.append(
                    f"{rel}: Goal appears activity-only (Outcome-first violation). "
                    f"Goal must state WHO + WHAT + EVIDENCE, not start with "
                    f"'write/implement/refactor/fix/add/create/build...'"
                )
        
        # Outcome-first: weak ACs
        if path.name == "TASKS.md":
            for m in WEAK_AC.finditer(text):
                errors.append(
                    f"{rel}: weak AC '{m.group(1)}' cannot be falsified "
                    f"(Outcome-first violation). AC must state observable outcome."
                )
            
            # Evidence: vague Verify
            for m in VAGUE_VERIFY.finditer(text):
                errors.append(
                    f"{rel}: vague Verify '{m.group(1)}' does not name concrete check "
                    f"(Evidence-over-confidence violation). Verify must name "
                    f"command/test/curl/UI path."
                )
            
            # Small-batch: mega-batch cards
            for m in MEGA_BATCH.finditer(text):
                errors.append(
                    f"{rel}: mega-batch indicator '{m.group(1)}' in card title "
                    f"(Small-batch violation). Split into smaller cards."
                )
            
            # Small-batch: layer-only titles
            for m in LAYER_TITLE.finditer(text):
                warnings.append(
                    f"{rel}: layer-only card title '{m.group(0).strip()}' "
                    f"(Small-batch warning). Prefer naming concrete unit "
                    f"(endpoint, screen id, control IDs)."
                )
        
        # Outcome-first: process-only DoD
        if path.name == "PLAN.md":
            if PROCESS_DOD.search(text):
                errors.append(
                    f"{rel}: Definition of done has only process milestones "
                    f"(Outcome-first violation). DoD needs >=1 consumer/contract outcome."
                )
    
    if path.name == "TASKS.md":
        cards = list(re.finditer(r"^###\s+T-\d+", text, re.M))
        if cards and "#### Dev context" not in text:
            errors.append(f"{rel}: task cards require #### Dev context")
        elif cards:
            # Each card region should cite Source or explicit none
            parts = re.split(r"(?=^###\s+T-\d+)", text, flags=re.M)
            for part in parts:
                if not re.match(r"^###\s+T-\d+", part):
                    continue
                title = part.splitlines()[0]
                if "#### Dev context" not in part:
                    errors.append(f"{rel}: {title}: missing #### Dev context")
                elif not SOURCE.search(part):
                    errors.append(
                        f"{rel}: {title}: Dev context needs [Source: …] or "
                        "'No specific guidance found.'"
                    )
    if path.name in {"BUSINESS_ANALYSIS.md", "BASIC_DESIGN.md", "DETAIL_DESIGN.md"}:
        # checked at session level for Quick
        pass
    # -----------------------------------------------------------------------
    # Readability checks
    # -----------------------------------------------------------------------
    lines = text.count("\n") + 1
    # Excessive file length
    if lines > MAX_FILE_LINES and path.name.endswith(".md"):
        warnings.append(f"{rel}: very long ({lines} lines, max {MAX_FILE_LINES}) — cut empty sections")
    # Empty sections (heading + only comments/blanks/TODO)
    for m in EMPTY_SECTION.finditer(text):
        heading_name = m.group(1).strip()
        warnings.append(
            f"{rel}: empty section '## {heading_name}' — "
            f"delete if not needed, or fill with real content"
        )
    # Filler ratio
    non_blank = [ln for ln in text.splitlines() if ln.strip()]
    if non_blank:
        filler_hits = len(FILLER.findall(text))
        ratio = filler_hits / len(non_blank)
        if ratio > FILLER_RATIO_THRESHOLD:
            warnings.append(
                f"{rel}: high filler ratio ({filler_hits} phrases / "
                f"{len(non_blank)} lines = {ratio:.0%}) — rewrite with concrete content"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", help="Session dir (default: .current)")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument(
        "--no-thinking",
        action="store_true",
        help="Skip thinking-method anti-pattern detection",
    )
    args = parser.parse_args()
    root = args.root.resolve() if args.root else find_root(Path.cwd())
    session = resolve_session(root, args.session)
    language = read_language(root)
    errors: list[str] = []
    warnings: list[str] = []
    check_thinking = not args.no_thinking

    quick = path_is_quick(session)
    if quick:
        for banned in (
            "BUSINESS_ANALYSIS.md",
            "BASIC_DESIGN.md",
            "DETAIL_DESIGN.md",
        ):
            if (session / banned).is_file():
                errors.append(
                    f"Path=Quick forbids {banned} — use Lite/Full or delete and use quick-fix"
                )

    for path in sorted(session.glob("*.md")):
        if path.name.startswith("."):
            continue
        lint_file(path, errors, warnings, language=language, check_thinking=check_thinking)

    if not list(session.glob("*.md")):
        print(f"SESSION_LINT_EMPTY session={session}")
        return 0

    if warnings and not args.strict:
        print("SESSION_LINT_WARNINGS")
        for w in warnings:
            print(f"- {w}")
    if errors or (args.strict and warnings):
        print("SESSION_LINT_FAILED")
        print(f"session={session}")
        for err in errors:
            print(f"- {err}")
        if args.strict:
            for w in warnings:
                print(f"- {w}")
        return 1
    print(f"SESSION_LINT_OK session={session}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
