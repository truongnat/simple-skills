#!/usr/bin/env python3
"""Validate session lifecycle artifacts against docs/config/artifact-schemas.json.

Usage (from repo root or any subdir):
  python tools/session/validate_artifacts.py
  python tools/session/validate_artifacts.py --session .agent-work/sessions/Task-1-demo
  python .agents/tools/session/validate_artifacts.py   # after install

Only artifacts that exist are checked. Missing optional artifacts are skipped.
Fails if a present artifact is missing a required heading (Markdown ## or HTML h2).
Fails if content rules detect thinking-method violations (activity-only Goals, etc).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from _work_settings import work_dir_name

# ---------------------------------------------------------------------------
# SemVer 2.0.0 validation (https://semver.org/)
# ---------------------------------------------------------------------------

SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


def parse_semver(version: str) -> tuple[int, int, int] | None:
    """Parse a SemVer string into (major, minor, patch) or None if invalid."""
    m = SEMVER_RE.match(str(version).strip())
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


# Minimum schema version this validator requires.
MIN_SCHEMA_VERSION = (2, 0, 0)


def is_semver_compatible(schema_version: str, min_version: tuple[int, int, int]) -> bool:
    """Check if schema_version meets the minimum required version.
    
    SemVer 2.0.0 rules (https://semver.org/):
    - MAJOR version bump = breaking changes
    - MINOR/PATCH bumps are backward-compatible
    - Major 0 = initial development, anything goes
    - Invalid versions = assume incompatible
    """
    sv = parse_semver(schema_version)
    if sv is None:
        return False
    # Major 0: anything goes (initial development)
    if sv[0] == 0:
        return True
    return sv >= min_version

# ---------------------------------------------------------------------------
# Thinking-method content validation patterns
# ---------------------------------------------------------------------------

# Activity-only Goal patterns (Outcome-first enforcement).
# These detect Goals that describe effort, not observable outcomes.
ACTIVITY_GOAL_PATTERNS = re.compile(
    r"^(" 
    r"write\s+(the\s+)?(a\s+)?\w+|"
    r"implement\s+(the\s+)?(a\s+)?\w+|"
    r"refactor\s+(the\s+)?\w+|"
    r"fix\s+(the\s+)?(bug|issue|problem)|"
    r"add\s+(the\s+)?(a\s+)?\w+\s+(support|feature|functionality)|"
    r"create\s+(the\s+)?(a\s+)?\w+\s+(endpoint|service|module|component)|"
    r"build\s+(the\s+)?(a\s+)?\w+|"
    r"develop\s+(the\s+)?(a\s+)?\w+|"
    r"integrate\s+\w+|"
    r"set\s+up\s+\w+|"
    r"configure\s+\w+"
    r")\b",
    re.I,
)

# Weak AC patterns — cannot be falsified.
WEAK_AC_PATTERNS = re.compile(
    r"^(works|correct|done|implemented|finished|complete|per spec|"
    r"as designed|as expected|properly|correctly)\.?$",
    re.I,
)

# Filler phrases that indicate activity, not outcome.
ACTIVITY_FILLER = re.compile(
    r"\b(implement|write|create|build|develop|refactor|fix|add|set up|configure)\b.*"
    r"\b(per spec|as designed|as expected|correctly|properly)\b",
    re.I,
)


def find_agents_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".agents").is_dir() or (candidate / ".agent-work").is_dir():
            return candidate
        if (candidate / "docs" / "config" / "artifact-schemas.json").is_file():
            return candidate
        if (candidate / "docs" / "AGENTS.md").is_file():
            return candidate
    return start.resolve()


def load_schema(root: Path) -> dict:
    candidates = [
        root / ".agents" / "tools" / "session" / "artifact-schemas.json",
        root / "docs" / "config" / "artifact-schemas.json",
        Path(__file__).resolve().parent / "artifact-schemas.json",
    ]
    for path in candidates:
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    raise SystemExit("artifact-schemas.json not found")


def resolve_session(root: Path, explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit)
        if not path.is_absolute():
            path = root / path
        if not path.is_dir():
            raise SystemExit(f"Session dir not found: {path}")
        return path
    work_dir = work_dir_name(root)
    pointer = root / work_dir / "sessions" / ".current"
    if not pointer.is_file():
        raise SystemExit(
            f"No active session ({work_dir}/sessions/.current). "
            "Pass --session or run session.sh new/set first."
        )
    rel = pointer.read_text(encoding="utf-8").splitlines()[0].strip()
    path = root / rel
    if not path.is_dir():
        raise SystemExit(f"Active session missing: {rel}")
    return path


def resolve_artifact_file(session: Path, basename: str) -> Path | None:
    for ext in (".md", ".html"):
        path = session / f"{basename}{ext}"
        if path.is_file():
            return path
    return None


def headings(text: str, suffix: str) -> list[str]:
    if suffix == ".html":
        found = re.findall(
            r"<h2[^>]*>\s*(.*?)\s*</h2>",
            text,
            flags=re.I | re.S,
        )
        cleaned: list[str] = []
        for raw in found:
            plain = re.sub(r"<[^>]+>", "", raw)
            plain = re.sub(r"\s+", " ", plain).strip()
            cleaned.append(plain)
        return cleaned
    return [
        m.group(1).strip()
        for m in re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.M)
    ]


def heading_matches(required: str, present: list[str]) -> bool:
    req = required.casefold()
    for heading in present:
        # Normalize underscores to spaces so YAML keys (developer_overview)
        # match Markdown headings (Developer overview).
        h = heading.replace("_", " ").casefold()
        if h == req or h.startswith(req + " ") or h.startswith(req + " ("):
            return True
        # Allow "Executive summary — …" style suffixes; prefer plain titles.
        if req in h:
            return True
    return False


def extract_section(text: str, heading: str) -> str | None:
    """Extract content under a ## heading until the next ## heading.
    
    Normalizes underscores to spaces so YAML keys (developer_overview)
    match Markdown headings (Developer overview).
    """
    # Build pattern that matches heading with underscores or spaces
    heading_escaped = re.escape(heading)
    # Also allow underscores in place of spaces
    heading_with_underscores = heading_escaped.replace(r"\ ", r"[\s_]+")
    pattern = rf"^##\s+{heading_with_underscores}\s*$"
    match = re.search(pattern, text, flags=re.M | re.I)
    if not match:
        return None
    start = match.end()
    # Find next ## heading
    next_heading = re.search(r"^##\s+", text[start:], flags=re.M)
    if next_heading:
        return text[start : start + next_heading.start()]
    return text[start:]


def extract_goal_section(text: str) -> str | None:
    """Extract the Goal section content."""
    return extract_section(text, "Goal")


def check_goal_not_activity(text: str, artifact_name: str) -> list[str]:
    """Check that Goal is not activity-only (Outcome-first enforcement)."""
    errors: list[str] = []
    goal_content = extract_goal_section(text)
    if not goal_content:
        return errors  # Heading check handles missing heading
    
    # Get first meaningful line (the Goal sentence)
    lines = [
        ln.strip() for ln in goal_content.splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    if not lines:
        return errors
    
    goal_sentence = lines[0]
    if ACTIVITY_GOAL_PATTERNS.match(goal_sentence):
        errors.append(
            f"{artifact_name}.md: Goal is activity-only — must state WHO + WHAT + EVIDENCE "
            f"(Outcome-first). Got: '{goal_sentence[:80]}...'"
        )
    return errors


def check_dod_has_outcome(text: str, artifact_name: str) -> list[str]:
    """Check that Definition of done has at least one consumer/contract outcome."""
    errors: list[str] = []
    dod_content = extract_section(text, "Definition of done")
    if not dod_content:
        return errors
    
    # Look for outcome indicators: test, verify, check, API, endpoint, returns, shows
    outcome_indicators = re.compile(
        r"\b(test|verify|check|assert|returns|shows|displays|receives|"
        r"201|200|400|401|404|contract|consumer|endpoint|API|field|message|"
        r"response|request|screen|form|button)\b",
        re.I,
    )
    # Look for process-only indicators (bad if no outcome)
    process_only = re.compile(
        r"^\s*-\s*\[\s*\]\s*(PR|lint|review|merge|commit|CI|pipeline|deploy)\b",
        re.I | re.M,
    )
    
    dod_lines = dod_content.strip().splitlines()
    has_outcome = any(outcome_indicators.search(ln) for ln in dod_lines)
    process_lines = process_only.findall(dod_content)
    
    if not has_outcome and process_lines:
        errors.append(
            f"{artifact_name}.md: Definition of done has only process milestones "
            f"({', '.join(process_lines[:3])}) — needs >=1 consumer/contract outcome "
            f"(Outcome-first)"
        )
    return errors


def check_ac_not_activity(text: str, artifact_name: str) -> list[str]:
    """Check that task card ACs are not activity-only or weak."""
    errors: list[str] = []
    # Split by task card headings
    cards = re.split(r"^###\s+T-\d+", text, flags=re.M)
    for i, card in enumerate(cards[1:], 1):  # Skip first split (before any card)
        # Find AC line
        ac_match = re.search(r"^-\s*\*\*AC[:\*]\*?\s*(.+?)$", card, re.M | re.I)
        if not ac_match:
            ac_match = re.search(r"^AC[:\s]+(.+?)$", card, re.M | re.I)
        if not ac_match:
            continue
        
        ac_text = ac_match.group(1).strip()
        if WEAK_AC_PATTERNS.match(ac_text):
            # Extract card title for error message
            title_match = re.search(r"^###\s+(T-\d+[^\n]*)", text, re.M)
            card_id = f"T-{i:03d}"
            errors.append(
                f"{artifact_name}.md: {card_id} AC is weak/unfalsifiable — "
                f"must state observable outcome. Got: '{ac_text[:60]}'"
            )
    return errors


def check_verify_falsifiable(text: str, artifact_name: str) -> list[str]:
    """Check that Verify lines name concrete checks (not vague)."""
    errors: list[str] = []
    cards = re.split(r"^###\s+T-\d+", text, flags=re.M)
    for i, card in enumerate(cards[1:], 1):
        verify_match = re.search(r"^-\s*\*\*Verify[:\*]\*?\s*(.+?)$", card, re.M | re.I)
        if not verify_match:
            verify_match = re.search(r"^Verify[:\s]+(.+?)$", card, re.M | re.I)
        if not verify_match:
            continue
        
        verify_text = verify_match.group(1).strip().lower()
        vague_patterns = [
            r"^(manual\s+)?(qa|testing|check|verify|test)\s*(only)?$",
            r"^will\s+test\s+later",
            r"^tbd",
            r"^as\s+needed",
        ]
        for pattern in vague_patterns:
            if re.match(pattern, verify_text, re.I):
                card_id = f"T-{i:03d}"
                errors.append(
                    f"{artifact_name}.md: {card_id} Verify is vague — "
                    f"must name concrete check (command, test, curl, UI path). "
                    f"Got: '{verify_text[:60]}'"
                )
                break
    return errors


def check_max_task_cards(text: str, artifact_name: str, max_cards: int = 3) -> list[str]:
    """Check Quick path ceiling: max N task cards."""
    errors: list[str] = []
    # Count cards in TASKS.md when QUICK.md exists (Quick path)
    card_count = len(re.findall(r"^###\s+T-\d+", text, re.M))
    if card_count > max_cards:
        errors.append(
            f"{artifact_name}.md: Quick path ceiling violated — found {card_count} "
            f"task cards, max is {max_cards}. Upgrade to Lite/Full or reduce cards."
        )
    return errors


def run_content_rules(
    text: str, artifact_name: str, rules: dict
) -> list[str]:
    """Run content validation rules on artifact text."""
    errors: list[str] = []
    
    if rules.get("goal_not_activity"):
        errors.extend(check_goal_not_activity(text, artifact_name))
    
    if rules.get("dod_has_outcome"):
        errors.extend(check_dod_has_outcome(text, artifact_name))
    
    if rules.get("ac_not_activity"):
        errors.extend(check_ac_not_activity(text, artifact_name))
    
    if rules.get("verify_falsifiable"):
        errors.extend(check_verify_falsifiable(text, artifact_name))
    
    if rules.get("max_task_cards"):
        errors.extend(check_max_task_cards(text, artifact_name, rules["max_task_cards"]))
    
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", help="Session dir (default: .current)")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo / project root (default: walk up from cwd)",
    )
    parser.add_argument(
        "--no-content-rules",
        action="store_true",
        help="Skip thinking-method content validation (heading checks only)",
    )
    args = parser.parse_args()
    root = args.root.resolve() if args.root else find_agents_root(Path.cwd())
    schema = load_schema(root)

    # SemVer 2.0.0 version check
    raw_version = schema.get("version")
    if raw_version is not None:
        version_str = str(raw_version)
        if not is_semver_compatible(version_str, MIN_SCHEMA_VERSION):
            print("SESSION_ARTIFACTS_FAILED")
            print(f"Schema version {version_str} is incompatible — "
                  f"validator requires >= {'.'.join(str(v) for v in MIN_SCHEMA_VERSION)}")
            return 1

    session = resolve_session(root, args.session)
    errors: list[str] = []
    content_warnings: list[str] = []
    checked = 0

    # Check if this is a Quick path session (for TASKS card ceiling)
    is_quick = False
    quick_path = session / "QUICK.md"
    if quick_path.is_file():
        quick_text = quick_path.read_text(encoding="utf-8")
        if re.search(r"Path:\s*Quick", quick_text, re.I):
            is_quick = True

    for basename, rules in (schema.get("artifacts") or {}).items():
        path = resolve_artifact_file(session, basename)
        if path is None:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8")
        present = headings(text, path.suffix.lower())
        for required in rules.get("required_headings") or []:
            if not heading_matches(required, present):
                errors.append(f"{path.name}: missing required heading '{required}'")
        
        # Run content rules (thinking-method enforcement)
        if not args.no_content_rules:
            content_rules = rules.get("content_rules") or {}
            # Special handling: max_task_cards only applies to TASKS.md on Quick path
            if "max_task_cards" in content_rules and not is_quick:
                content_rules = {k: v for k, v in content_rules.items() if k != "max_task_cards"}
            if content_rules:
                content_errors = run_content_rules(text, basename, content_rules)
                errors.extend(content_errors)

    if checked == 0:
        print(f"SESSION_ARTIFACTS_EMPTY session={session}")
        return 0
    if errors:
        print("SESSION_ARTIFACTS_FAILED")
        print(f"session={session}")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"SESSION_ARTIFACTS_OK session={session} checked={checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
