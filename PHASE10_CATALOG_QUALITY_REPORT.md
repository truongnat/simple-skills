# Phase 10 — Catalog-wide quality pass

## Scope and method

- Catalog inventory: **222 skills**.
- Deterministic checks: Markdown fences, local links, and reference inventory.
- Coverage heuristic: scenario/worked-example plus evidence/verification signals from SKILL.md and linked local references.
- Wave 3 policy: evidence-producing P1/P2 leads are scored; visual, guidance-only, process-artifact, and router skills use explicit dispositions.
- Boundary heuristic: token Jaccard similarity; high overlap is a review lead, not proof of duplication.
- This pass is guidance-only and does not execute skill scripts or alter user projects.

## Result

**PASS** — local links: 0 broken / 1671 scanned; unbalanced fences: 0; references: 1053; linked reference files inspected: 759.

## Coverage signals

| Signal | Count | Interpretation |
|---|---:|---|
| Scenario and evidence | 212 | Strong baseline; signal may be inline or linked |
| Scenario without evidence | 0 | Add expected result, proof or acceptance gate when the lane requires it |
| Evidence without scenario | 10 | Add one worked case when the lane requires it |
| Neither signal | 0 | Review only when policy classifies the skill as repeatable/evidence-producing |

## Inline versus linked-reference coverage

| Scope | Scenario | Evidence | Both |
|---|---:|---:|---:|
| Inline SKILL.md | 21 | 32 | 21 |
| Linked local references | 24 | 27 | 24 |

## Wave 3 lead reclassification

| Skill | Lane | Classification | Explainable reason | Linked files |
|---|---|---|---|---|
| `sk-architecture-decision-records` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-architecture-decision-records/references/wave3-evidence-pack.md` |
| `sk-ba-dashboard` | W3-H | **exception** | process/reporting artifact; telemetry or screenshots are not required | — |
| `sk-ba-handoff` | W3-H | **exception** | handoff contract is already deterministic; sample is training-only | — |
| `sk-ba-integrate` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-ba-integrate/references/wave3-evidence-pack.md` |
| `sk-ba-kg` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-ba-kg/references/wave3-evidence-pack.md` |
| `sk-basic-design` | W3-H | **exception** | existing WRONG/CORRECT and boundary guidance is sufficient | — |
| `sk-detail-design` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-detail-design/references/wave3-evidence-pack.md` |
| `sk-discussing-pro` | W3-H | **exception** | upstream clarification skill; follow references before adding evidence | `skills/sk-discussing-pro/references/socratic-techniques.md`, `skills/sk-discussing-pro/references/ideation-system-model.md`, `skills/sk-discussing-pro/references/session-artifacts-contract.md`, `skills/sk-discussing-pro/references/failure-modes.md` |
| `sk-docs` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-docs/references/wave3-evidence-pack.md` |
| `sk-done` | W3-H | **exception** | closeout guidance must not duplicate final verification ownership | — |
| `sk-excel-doc-convert` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-excel-doc-convert/references/wave3-evidence-pack.md` |
| `sk-executing-pro` | W3-H | **exception** | checkpoint guidance is progressive disclosure, not a domain test | `skills/sk-executing-pro/references/execution-cycle.md`, `skills/sk-executing-pro/references/dependency-aware-execution.md`, `skills/sk-executing-pro/references/checkpoint-discipline.md`, `skills/sk-executing-pro/references/completion-verification.md`, `skills/sk-executing-pro/references/adaptive-replanning.md`, `skills/sk-executing-pro/references/progress-tracking.md`, `skills/sk-executing-pro/references/execution-documentation.md`, `skills/sk-executing-pro/references/decision-framework.md`, `skills/sk-executing-pro/references/decision-tree.md`, `skills/sk-executing-pro/references/anti-patterns.md`, `skills/sk-executing-pro/references/failure-modes.md`, `skills/sk-executing-pro/references/integration-map.md` |
| `sk-high-end-visual-design` | W3-P2-visual | **visual-review** | visual evidence requires screenshot or visual-regression tooling, not prose alone | `skills/sk-high-end-visual-design/references/visual-qa-fixture.md` |
| `sk-industrial-brutalist-ui` | W3-P2-visual | **visual-review** | visual evidence requires screenshot or visual-regression tooling, not prose alone | `skills/sk-industrial-brutalist-ui/references/visual-qa-fixture.md` |
| `sk-init` | W3-H | **exception** | deterministic read-only preflight; scenario would duplicate the command contract | — |
| `sk-investigate` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-investigate/references/wave3-evidence-pack.md` |
| `sk-minimalist-ui` | W3-P2-visual | **visual-review** | visual evidence requires screenshot or visual-regression tooling, not prose alone | `skills/sk-minimalist-ui/references/visual-qa-fixture.md` |
| `sk-planning` | W3-H | **exception** | planning may stop on dependency failure but does not own execution evidence | — |
| `sk-quick-fix` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-quick-fix/references/wave3-evidence-pack.md` |
| `sk-redesign-existing-projects` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-redesign-existing-projects/references/wave3-evidence-pack.md` |
| `sk-research` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-research/references/wave3-evidence-pack.md` |
| `sk-reverse-doc` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-reverse-doc/references/wave3-evidence-pack.md` |
| `sk-review` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-review/references/wave3-evidence-pack.md` |
| `sk-review-pr` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-review-pr/references/wave3-evidence-pack.md` |
| `sk-senior-security` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-senior-security/references/wave3-evidence-pack.md` |
| `sk-sync` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-sync/references/wave3-evidence-pack.md` |
| `sk-sync-custom-to-repo` | W3-H | **exception** | explicit non-execution boundary; runtime Git evidence is inappropriate | — |
| `sk-system-design-pro` | W3-P1 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-system-design-pro/references/wave3-evidence-pack.md` |
| `sk-user-flow` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-user-flow/references/wave3-evidence-pack.md` |
| `sk-using-aix` | W3-H | **exception** | router/capability guard; validate claims and fallback paths instead | — |
| `sk-ux-wireframe` | W3-P2 | **covered** | positive and edge/scenario signals found in inline content or linked local references | `skills/sk-ux-wireframe/references/wave3-evidence-pack.md` |
| `sk-visual-design-foundations` | W3-H | **exception** | visual guidance; text-only evidence is not a visual fixture | — |

## Boundary overlap review leads

No boundary pairs exceeded the review threshold (0.72 Jaccard).

## Deterministic failures

None.

## Evidence-producing review leads requiring follow-up

None. All P1/P2 evidence-producing leads have scenario and evidence signals after reference traversal.

## Explicit heuristic exceptions

| Skill | Reason |
|---|---|
| `sk-ba-dashboard` | process/reporting artifact; telemetry or screenshots are not required |
| `sk-ba-handoff` | handoff contract is already deterministic; sample is training-only |
| `sk-basic-design` | existing WRONG/CORRECT and boundary guidance is sufficient |
| `sk-discussing-pro` | upstream clarification skill; follow references before adding evidence |
| `sk-done` | closeout guidance must not duplicate final verification ownership |
| `sk-executing-pro` | checkpoint guidance is progressive disclosure, not a domain test |
| `sk-init` | deterministic read-only preflight; scenario would duplicate the command contract |
| `sk-planning` | planning may stop on dependency failure but does not own execution evidence |
| `sk-sync-custom-to-repo` | explicit non-execution boundary; runtime Git evidence is inappropriate |
| `sk-using-aix` | router/capability guard; validate claims and fallback paths instead |
| `sk-visual-design-foundations` | visual guidance; text-only evidence is not a visual fixture |

## Acceptance

- Run `.work/skill-validation/validate_current_skills.py` separately for the catalog contract.
- Treat overlap and coverage findings as review leads; domain owners decide whether content changes are warranted.
- W3-H exceptions are policy decisions, not suppressed errors; keep their reasons reviewable.
- Keep `.idea/` and unrelated historical summaries out of the commit.
