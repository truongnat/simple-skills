# Phase 10 — Catalog-wide quality pass

## Scope and method

- Catalog inventory: **222 skills**.
- Deterministic checks: Markdown fences, local links, and reference inventory.
- Coverage heuristic: scenario/worked-example signal plus evidence/verification signal.
- Boundary heuristic: token Jaccard similarity; high overlap is a review lead, not proof of duplication.
- This pass is guidance-only and does not execute skill scripts or alter user projects.

## Result

**REVIEW** — local links: 0 broken / 1621 scanned; unbalanced fences: 0; references: 1003.

## Coverage signals

| Signal | Count | Interpretation |
|---|---:|---|
| Scenario and evidence | 181 | Strong baseline for repeatable decisions |
| Scenario without evidence | 0 | Add expected result, proof or acceptance gate |
| Evidence without scenario | 41 | Add one worked case or decision example |
| Neither signal | 0 | Review only when the domain is repeatable/high-risk |

## Boundary overlap review leads

| Similarity | Candidate pair | Action |
|---:|---|---|
| 0.94 | `sk-clean-architecture` ↔ `sk-system-design-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-verification` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-ux-wireframe` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-ux-wireframe` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-user-flow` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-user-flow` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-user-flow` ↔ `sk-ux-wireframe` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-tester` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-tester` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-tester` ↔ `sk-ux-wireframe` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-tester` ↔ `sk-user-flow` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-sync` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-sync` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-sync` ↔ `sk-ux-wireframe` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-sync` ↔ `sk-user-flow` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-sync` ↔ `sk-tester` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-ux-wireframe` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-user-flow` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-tester` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-story-spec` ↔ `sk-sync` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-verification` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-ux-wireframe` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-user-flow` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-tester` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-sync` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-specify` ↔ `sk-story-spec` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |
| 0.93 | `sk-scaffold` ↔ `sk-verify-pro` | Confirm ownership and canonical handoff; do not merge by heuristic alone. |

## Deterministic failures

None.

## High-risk coverage review leads

- **sk-api-ba** — high-risk topics `delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-architecture-decision-records** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-ba-dashboard** — high-risk topics `delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-ba-handoff** — high-risk topics `data, delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-ba-integrate** — high-risk topics `delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-ba-kg** — high-risk topics `delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-basic-design** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-biz-model** — high-risk topics `data, delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-detail-design** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-discussing-pro** — high-risk topics `data, delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-docs** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-docx** — high-risk topics `data, delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-done** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-excel-doc-convert** — high-risk topics `data, delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-executing-pro** — high-risk topics `delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-expo-native-ui** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-high-end-visual-design** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-hybrid-cloud-networking** — high-risk topics `data, delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-industrial-brutalist-ui** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-init** — high-risk topics `delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-investigate** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-minimalist-ui** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-office-common** — high-risk topics `data, delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-pdf** — high-risk topics `delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-planning** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-pptx** — high-risk topics `data, delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-quick-fix** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-redesign-existing-projects** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-research** — high-risk topics `data, delivery, platform` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-reverse-doc** — high-risk topics `delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-review** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-review-pr** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-senior-security** — high-risk topics `delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-story-spec** — high-risk topics `delivery` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-sync** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-sync-custom-to-repo** — high-risk topics `delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-system-design-pro** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-user-flow** — high-risk topics `delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-using-aix** — high-risk topics `delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-ux-wireframe** — high-risk topics `data, delivery, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.
- **sk-visual-design-foundations** — high-risk topics `data, delivery, platform, security` lack a complete scenario-plus-evidence pair; review whether the domain needs one.

## Acceptance

- Run `.work/skill-validation/validate_current_skills.py` separately for the catalog contract.
- Treat overlap and coverage findings as review leads; domain owners decide whether content changes are warranted.
- Keep `.idea/` and unrelated historical summaries out of the commit.
