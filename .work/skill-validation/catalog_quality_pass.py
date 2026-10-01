#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
REPORT = ROOT / "PHASE10_CATALOG_QUALITY_REPORT.md"

# These are review leads from Wave 3, not a claim that every skill needs a runtime
# scenario. Keep policy here rather than inferring it from generic words such as
# "security", "data", or "release".
LEAD_LANES: dict[str, str] = {
    "sk-architecture-decision-records": "W3-P1",
    "sk-docs": "W3-P1",
    "sk-investigate": "W3-P1",
    "sk-reverse-doc": "W3-P1",
    "sk-review": "W3-P1",
    "sk-review-pr": "W3-P1",
    "sk-senior-security": "W3-P1",
    "sk-sync": "W3-P1",
    "sk-system-design-pro": "W3-P1",
    "sk-ba-integrate": "W3-P2",
    "sk-ba-kg": "W3-P2",
    "sk-detail-design": "W3-P2",
    "sk-excel-doc-convert": "W3-P2",
    "sk-quick-fix": "W3-P2",
    "sk-redesign-existing-projects": "W3-P2",
    "sk-research": "W3-P2",
    "sk-user-flow": "W3-P2",
    "sk-ux-wireframe": "W3-P2",
    "sk-high-end-visual-design": "W3-P2-visual",
    "sk-industrial-brutalist-ui": "W3-P2-visual",
    "sk-minimalist-ui": "W3-P2-visual",
    "sk-ba-dashboard": "W3-H",
    "sk-ba-handoff": "W3-H",
    "sk-basic-design": "W3-H",
    "sk-discussing-pro": "W3-H",
    "sk-done": "W3-H",
    "sk-executing-pro": "W3-H",
    "sk-init": "W3-H",
    "sk-planning": "W3-H",
    "sk-sync-custom-to-repo": "W3-H",
    "sk-using-aix": "W3-H",
    "sk-visual-design-foundations": "W3-H",
}

EXCEPTIONS: dict[str, str] = {
    "sk-ba-dashboard": "process/reporting artifact; telemetry or screenshots are not required",
    "sk-ba-handoff": "handoff contract is already deterministic; sample is training-only",
    "sk-basic-design": "existing WRONG/CORRECT and boundary guidance is sufficient",
    "sk-discussing-pro": "upstream clarification skill; follow references before adding evidence",
    "sk-done": "closeout guidance must not duplicate final verification ownership",
    "sk-executing-pro": "checkpoint guidance is progressive disclosure, not a domain test",
    "sk-init": "deterministic read-only preflight; scenario would duplicate the command contract",
    "sk-planning": "planning may stop on dependency failure but does not own execution evidence",
    "sk-sync-custom-to-repo": "explicit non-execution boundary; runtime Git evidence is inappropriate",
    "sk-using-aix": "router/capability guard; validate claims and fallback paths instead",
    "sk-visual-design-foundations": "visual guidance; text-only evidence is not a visual fixture",
}

TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
LINK_RE = re.compile(r"\]\(([^)]+)\)")


@dataclass(frozen=True)
class Signals:
    inline_scenario: bool
    inline_evidence: bool
    linked_scenario: bool
    linked_evidence: bool
    linked_files: tuple[str, ...]

    @property
    def scenario(self) -> bool:
        return self.inline_scenario or self.linked_scenario

    @property
    def evidence(self) -> bool:
        return self.inline_evidence or self.linked_evidence

    @property
    def complete(self) -> bool:
        return self.scenario and self.evidence



def body(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---\n") and "\n---" in text[4:]:
        return text[text.index("\n---", 4) + 4 :]
    return text


def section(text: str, heading: str) -> str:
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.I | re.M)
    if not m:
        return ""
    tail = text[m.end() :]
    nxt = re.search(r"^##\s+", tail, re.M)
    return tail[: nxt.start()] if nxt else tail


def tokens(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def referenced_local_files(path: Path, raw: str) -> tuple[list[Path], list[str]]:
    """Follow local markdown links from SKILL.md, including one hop in refs.

    One-hop traversal is deliberate: it captures the skill's contract fixtures
    without turning the catalog pass into an unbounded documentation crawler.
    """
    files: list[Path] = []
    broken: list[str] = []
    queue: list[tuple[Path, str]] = [(path, raw)]
    seen: set[Path] = set()
    while queue:
        source, text = queue.pop(0)
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists() or not resolved.is_file():
                broken.append(f"{source.relative_to(ROOT)} → `{target}`")
                continue
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(resolved)
            if len(files) <= 32 and resolved.suffix.lower() in {".md", ".markdown", ".txt"}:
                queue.append((resolved, resolved.read_text(encoding="utf-8", errors="replace")))
    return files, broken


def signal_text(text: str) -> tuple[bool, bool]:
    scenario = bool(re.search(r"(?i)(worked scenario|example|scenario|fixture|positive scenario|negative or edge)", text))
    evidence = bool(re.search(r"(?i)(expected output|evidence|verification|acceptance criteria|quality gate|test case|evidence packet)", text))
    return scenario, evidence


def classify(name: str, signals: Signals) -> tuple[str, str]:
    lane = LEAD_LANES.get(name)
    if lane == "W3-H":
        return "exception", EXCEPTIONS[name]
    if lane == "W3-P2-visual":
        return "visual-review", "visual evidence requires screenshot or visual-regression tooling, not prose alone"
    if lane:
        if signals.complete:
            return "covered", "positive and edge/scenario signals found in inline content or linked local references"
        return "action", "evidence-producing lead lacks a complete scenario-plus-evidence pair after linked-reference traversal"
    return "not-a-wave3-lead", "not part of the 32 Wave 3 review leads; generic vocabulary is not scored as a failure"


def main() -> int:
    dirs = sorted(p for p in SKILLS.glob("sk-*") if p.is_dir())
    findings: list[str] = []
    coverage: dict[str, list[str]] = defaultdict(list)
    reclassified: list[tuple[str, str, str, Signals]] = []
    reference_count = 0
    linked_reference_count = 0
    link_count = 0
    broken_links: list[str] = []
    unbalanced_fences: list[str] = []
    boundaries: dict[str, set[str]] = {}

    for d in dirs:
        p = d / "SKILL.md"
        if not p.is_file():
            findings.append(f"- **{d.name}** — missing `SKILL.md`.")
            continue
        raw = p.read_text(encoding="utf-8", errors="replace")
        text = body(p)
        refs = d / "references"
        reference_count += len(list(refs.glob("*"))) if refs.is_dir() else 0
        if raw.count("```") % 2:
            unbalanced_fences.append(str(p.relative_to(ROOT)))
        files, link_errors = referenced_local_files(p, raw)
        broken_links.extend(link_errors)
        link_count += len(LINK_RE.findall(raw))
        linked_reference_count += sum(1 for f in files if f.parent.name == "references")
        inline_scenario, inline_evidence = signal_text(text)
        linked_scenario = linked_evidence = False
        for f in files:
            s, e = signal_text(f.read_text(encoding="utf-8", errors="replace"))
            linked_scenario |= s
            linked_evidence |= e
        signals = Signals(inline_scenario, inline_evidence, linked_scenario, linked_evidence, tuple(str(f.relative_to(ROOT)) for f in files))
        if signals.complete:
            coverage["scenario_and_evidence"].append(d.name)
        elif signals.scenario:
            coverage["scenario_without_evidence"].append(d.name)
        elif signals.evidence:
            coverage["evidence_without_scenario"].append(d.name)
        else:
            coverage["neither_signal"].append(d.name)
        boundaries[d.name] = tokens(section(text, "Boundary"))
        if d.name in LEAD_LANES:
            classification, reason = classify(d.name, signals)
            reclassified.append((d.name, classification, reason, signals))
            if classification == "action":
                findings.append(f"- **{d.name}** — {reason}.")

    overlaps: list[tuple[float, str, str]] = []
    names = sorted(boundaries)
    for i, left in enumerate(names):
        if len(boundaries[left]) < 6:
            continue
        for right in names[i + 1 :]:
            if len(boundaries[right]) < 6:
                continue
            union = boundaries[left] | boundaries[right]
            score = len(boundaries[left] & boundaries[right]) / len(union) if union else 0
            if score >= 0.72:
                overlaps.append((score, left, right))
    overlaps.sort(reverse=True)

    status = "PASS" if not broken_links and not unbalanced_fences and not findings else "REVIEW"
    lines = [
        "# Phase 10 — Catalog-wide quality pass", "",
        "## Scope and method", "",
        f"- Catalog inventory: **{len(dirs)} skills**.",
        "- Deterministic checks: Markdown fences, local links, and reference inventory.",
        "- Coverage heuristic: scenario/worked-example plus evidence/verification signals from SKILL.md and linked local references.",
        "- Wave 3 policy: evidence-producing P1/P2 leads are scored; visual, guidance-only, process-artifact, and router skills use explicit dispositions.",
        "- Boundary heuristic: token Jaccard similarity; high overlap is a review lead, not proof of duplication.",
        "- This pass is guidance-only and does not execute skill scripts or alter user projects.", "",
        "## Result", "",
        f"**{status}** — local links: {len(broken_links)} broken / {link_count} scanned; unbalanced fences: {len(unbalanced_fences)}; references: {reference_count}; linked reference files inspected: {linked_reference_count}.", "",
        "## Coverage signals", "",
        "| Signal | Count | Interpretation |", "|---|---:|---|",
        f"| Scenario and evidence | {len(coverage['scenario_and_evidence'])} | Strong baseline; signal may be inline or linked |",
        f"| Scenario without evidence | {len(coverage['scenario_without_evidence'])} | Add expected result, proof or acceptance gate when the lane requires it |",
        f"| Evidence without scenario | {len(coverage['evidence_without_scenario'])} | Add one worked case when the lane requires it |",
        f"| Neither signal | {len(coverage['neither_signal'])} | Review only when policy classifies the skill as repeatable/evidence-producing |", "",
        "## Inline versus linked-reference coverage", "",
        "| Scope | Scenario | Evidence | Both |", "|---|---:|---:|---:|",
        f"| Inline SKILL.md | {sum(1 for _,_,_,s in reclassified if s.inline_scenario)} | {sum(1 for _,_,_,s in reclassified if s.inline_evidence)} | {sum(1 for _,_,_,s in reclassified if s.inline_scenario and s.inline_evidence)} |",
        f"| Linked local references | {sum(1 for _,_,_,s in reclassified if s.linked_scenario)} | {sum(1 for _,_,_,s in reclassified if s.linked_evidence)} | {sum(1 for _,_,_,s in reclassified if s.linked_scenario and s.linked_evidence)} |", "",
        "## Wave 3 lead reclassification", "",
        "| Skill | Lane | Classification | Explainable reason | Linked files |", "|---|---|---|---|---|",
    ]
    for name, classification, reason, signals in reclassified:
        lane = LEAD_LANES[name]
        linked = ", ".join(f"`{f}`" for f in signals.linked_files if "/references/" in f) or "—"
        lines.append(f"| `{name}` | {lane} | **{classification}** | {reason} | {linked} |")
    lines += ["", "## Boundary overlap review leads", ""]
    if overlaps:
        lines += ["| Similarity | Candidate pair | Action |", "|---:|---|---|"]
        for score, left, right in overlaps[:30]:
            lines.append(f"| {score:.2f} | `{left}` ↔ `{right}` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |")
    else:
        lines.append("No boundary pairs exceeded the review threshold (0.72 Jaccard).")
    lines += ["", "## Deterministic failures", ""]
    lines.extend([*(f"- Broken link: {x}" for x in broken_links), *(f"- Unbalanced fence: `{x}`" for x in unbalanced_fences)] or ["None."])
    lines += ["", "## Evidence-producing review leads requiring follow-up", ""]
    lines.extend(findings or ["None. All P1/P2 evidence-producing leads have scenario and evidence signals after reference traversal."])
    lines += ["", "## Explicit heuristic exceptions", "", "| Skill | Reason |", "|---|---|"]
    lines.extend(f"| `{name}` | {reason} |" for name, reason in EXCEPTIONS.items())
    lines += ["", "## Acceptance", "", "- Run `.work/skill-validation/validate_current_skills.py` separately for the catalog contract.", "- Treat overlap and coverage findings as review leads; domain owners decide whether content changes are warranted.", "- W3-H exceptions are policy decisions, not suppressed errors; keep their reasons reviewable.", "- Keep `.idea/` and unrelated historical summaries out of the commit.", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"CATALOG_QUALITY_PASS {status}")
    print(f"skills={len(dirs)} refs={reference_count} linked_refs={linked_reference_count} links={link_count} broken_links={len(broken_links)} fences={len(unbalanced_fences)} overlap_leads={len(overlaps)} follow_up={len(findings)} wave3_leads={len(reclassified)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
