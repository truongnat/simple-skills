#!/usr/bin/env python3
"""Progressive disclosure loader for thinking methods.

Instead of loading all 12 thinking method files for every task, this module
provides path-based method selection — Quick path loads only essential methods,
Lite/Full load progressively more.

Usage:
  python tools/session/thinking_methods.py --path Quick
  python tools/session/thinking_methods.py --path Full --output bundle.md
  python .agents/tools/session/thinking_methods.py --path Lite
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


# Method definitions with path applicability and priority.
# Priority determines load order within a path level.
THINKING_METHODS = [
    {
        "name": "outcome-first",
        "title": "Outcome-first",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 1,
        "summary": "Lock WHO + WHAT + EVIDENCE before tasks. Goal must be observable outcome, not activity.",
        "key_rules": [
            "Every Goal/DoD/AC must pass three-axis: WHO (consumer), WHAT (observable change), EVIDENCE (how to verify)",
            "Reject activity-only Goals: 'write X', 'implement Y', 'refactor Z', 'fix the bug'",
            "Strength ladder: activity < artifact < contract < consumer < evidence-bound",
            "If Goal is activity-only → STOP, rewrite or Confirm-first",
        ],
        "file": "docs/thinking/outcome-first.md",
    },
    {
        "name": "input-process-output",
        "title": "Input → Process → Output",
        "paths": ["Lite", "Full"],
        "priority": 2,
        "summary": "Every unit needs Input (facts/constraints), Process (transformation), Output (observable result).",
        "key_rules": [
            "Input sufficient when: Blocking unknowns resolved, contracts cited, High-impact assumptions confirmed",
            "Process coherent when: each step advances Output, no ceremony-only steps",
            "Card-level IPO: Trace + Dev context → Work items → AC + Verify",
            "Blocking Input gap → Confirm-first, do not invent contracts",
        ],
        "file": "docs/thinking/input-process-output.md",
    },
    {
        "name": "make-implicit-explicit",
        "title": "Make implicit explicit",
        "paths": ["Lite", "Full"],
        "priority": 3,
        "summary": "Classify Facts vs Assumptions vs Unknowns vs Rules. Dual-interpretation → Confirm-first.",
        "key_rules": [
            "Taxonomy: Fact (sourced) ≠ Assumption (unconfirmed) ≠ Unknown ≠ Preference ≠ Rule",
            "Dual-interpretation test: if two readings change Output/Process → Blocking → Confirm-first",
            "High-impact Assumption with Confirmed?: No → Ready blocker",
            "Blocking Unknowns/Issues need Owner (who will answer?)",
        ],
        "file": "docs/thinking/make-implicit-explicit.md",
    },
    {
        "name": "small-batch",
        "title": "Small-batch",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 4,
        "summary": "small step → complete → check → continue. Each batch: one goal, one output, independent verify.",
        "key_rules": [
            "Four-property test: one goal, one output, independent verify, short feedback",
            "Quick ceiling: 1-3 cards max. More outputs → upgrade Path",
            "Execution rhythm: start card → work → Verify THIS card → done → next dependent card",
            "Forbidden: implement T-001..T-005 then run all Verifies",
        ],
        "file": "docs/thinking/small-batch.md",
    },
    {
        "name": "feedback-loop",
        "title": "Feedback loop",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 5,
        "summary": "Shortest useful signal by latency×risk. Example/See/Run/Spike/Ask/Compare modalities.",
        "key_rules": [
            "Latency × risk: higher rewind cost → earlier + stronger signal required",
            "Modalities: Example (Given→Expect), See (preview), Run (test), Spike (feasibility), Ask, Compare",
            "Requirement ambiguity → Example confirm before TASKS",
            "UI/layout Blocking → See before polish",
        ],
        "file": "docs/thinking/feedback-loop.md",
    },
    {
        "name": "default-path-first",
        "title": "Default path first",
        "paths": ["Lite", "Full"],
        "priority": 6,
        "summary": "L1 happy → L2 validation → L3 errors → L4 rare. Name edges early, implement rare late.",
        "key_rules": [
            "Order: happy path first, then validation, then errors, then rare edges",
            "Name material edges in Non-goals/CAP gaps — do not silent-drop",
            "Thin early guards only for Blocking security/money/data-loss",
            "Anti-pattern: Approach leads with exception encyclopedia while happy flow empty",
        ],
        "file": "docs/thinking/default-path-first.md",
    },
    {
        "name": "reversible-decisions",
        "title": "Reversible decisions",
        "paths": ["Full"],
        "priority": 7,
        "summary": "R (reversible) → fast try. H (hard-to-reverse) → options + Spike + ADR. U → treat as H.",
        "key_rules": [
            "Class R: decide fast → try → measure; no ADR spam",
            "Class H: options + Spike/POC + record why (ADR)",
            "Class U: treat as H until proven R",
            "Quick path forbids NEW Type H locks (public API / core schema / auth architecture)",
        ],
        "file": "docs/thinking/reversible-decisions.md",
    },
    {
        "name": "standardize-before-automate",
        "title": "Standardize before automate",
        "paths": ["Full"],
        "priority": 8,
        "summary": "manual → understand → standardize → template → automate. Don't CI/bot a process with no checklist.",
        "key_rules": [
            "Ladder: manual → understand → standardize → template → automate",
            "Do not add CI/bots/hooks/skills until checklist/template exists",
            "Map each automated check to a named standard row",
            "Org-wide automation is often Reversibility H",
        ],
        "file": "docs/thinking/standardize-before-automate.md",
    },
    {
        "name": "design-for-handoff",
        "title": "Design for handoff",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 9,
        "summary": "Successor continues from files alone. Six questions: what/why/run/check/risks/next.",
        "key_rules": [
            "Six questions: What is this? Why this way? How to run? How to check? What risks? What's next?",
            "No chat-only material context — everything in files",
            "Opaque green (tests pass, nobody understands) = fail",
            "Land in existing fields: Goal/Handoff/Dev context/Verify/Risks/PR",
        ],
        "file": "docs/thinking/design-for-handoff.md",
    },
    {
        "name": "evidence-over-confidence",
        "title": "Evidence over confidence",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 10,
        "summary": "Claim works/done/Ready only with recorded proof. AI confidence ≠ a run.",
        "key_rules": [
            "Evidence kinds: test result, screenshot, log, API response, metrics, link, confirmed checklist",
            "Do not claim works/done/Ready from fluency alone ('chắc chạy rồi', 'should be fine')",
            "Skip = risk + 'skipped'/'blocked', never fake pass",
            "Record evidence in Verify/EXECUTION/REVIEW/DONE/PR",
        ],
        "file": "docs/thinking/evidence-over-confidence.md",
    },
    {
        "name": "optimize-bottleneck",
        "title": "Optimize bottleneck",
        "paths": ["Full"],
        "priority": 11,
        "summary": "Name constraint stage (requirements/coding/review/deploy/decision-wait), relieve THAT first.",
        "key_rules": [
            "Name the constraint stage before improving",
            "Local speed-ups elsewhere often add inventory, not throughput",
            "Automate only after a checklist, prefer automating the bottleneck",
            "Constraint stages: requirements, coding, review, deployment, decision-wait",
        ],
        "file": "docs/thinking/optimize-bottleneck.md",
    },
    {
        "name": "single-source-of-truth",
        "title": "Single Source of Truth",
        "paths": ["Quick", "Lite", "Full"],
        "priority": 12,
        "summary": "One kind of truth → one official update place. Cite, don't fork.",
        "key_rules": [
            "One kind of truth → one official update place; everything else cites",
            "Progress truth = only TASKS.md + session.sh status (no OVERVIEW.md)",
            "Trace/[Source:]/ticket IDs beat restating AC in chat/docs/code",
            "Docs ↔ code conflict → do not silent-pick; classify + Confirm-first",
        ],
        "file": "docs/thinking/single-source-of-truth.md",
    },
]


def get_methods_for_path(path: str) -> list[dict]:
    """Return thinking methods applicable to the given path, sorted by priority."""
    path_normalized = path.capitalize()
    if path_normalized not in ("Quick", "Lite", "Full"):
        path_normalized = "Full"
    
    applicable = [m for m in THINKING_METHODS if path_normalized in m["paths"]]
    return sorted(applicable, key=lambda m: m["priority"])


def generate_bundle(path: str, include_full_text: bool = False, root: Path | None = None) -> str:
    """Generate a thinking methods bundle for the given path.
    
    Args:
        path: Quick, Lite, or Full
        include_full_text: If True, include full file contents (requires root)
        root: Repo root for reading full method files
    
    Returns:
        Markdown-formatted bundle string
    """
    methods = get_methods_for_path(path)
    
    lines = [
        f"# Thinking Methods Bundle — Path: {path}",
        "",
        f"> Auto-generated for {path} path. {len(methods)} methods loaded.",
        "> Apply these silently — do not create method-branded headings.",
        "",
        "## Framing Order",
        "",
        "```",
    ]
    
    for i, m in enumerate(methods, 1):
        lines.append(f"{i}. {m['title']}")
    
    lines.extend([
        "```",
        "",
        "---",
        "",
    ])
    
    for m in methods:
        lines.extend([
            f"## {m['title']}",
            "",
            f"**{m['summary']}**",
            "",
            "Key rules:",
            "",
        ])
        for rule in m["key_rules"]:
            lines.append(f"- {rule}")
        lines.extend(["", "---", ""])
    
    if include_full_text and root:
        lines.extend([
            "## Full Method Details",
            "",
        ])
        for m in methods:
            file_path = root / m["file"]
            if file_path.is_file():
                content = file_path.read_text(encoding="utf-8")
                lines.extend([
                    f"### {m['title']} (full)",
                    "",
                    content,
                    "",
                    "---",
                    "",
                ])
    
    return "\n".join(lines)


def find_agents_root(start: Path) -> Path:
    """Walk up to find agents root."""
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".agents").is_dir():
            return candidate
        if (candidate / "docs" / "thinking").is_dir():
            return candidate
    return start.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        choices=["Quick", "Lite", "Full"],
        default="Full",
        help="Execution path (determines which methods to load)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--full-text",
        action="store_true",
        help="Include full method file contents (requires repo root)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo root (for --full-text)",
    )
    args = parser.parse_args()
    
    root = args.root.resolve() if args.root else find_agents_root(Path.cwd())
    bundle = generate_bundle(args.path, include_full_text=args.full_text, root=root)
    
    if args.output:
        args.output.write_text(bundle, encoding="utf-8")
        print(f"Thinking bundle written to {args.output} ({args.path} path, {len(get_methods_for_path(args.path))} methods)")
    else:
        print(bundle)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
