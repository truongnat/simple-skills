# Phase 7 — Lifecycle and BA/product workflows upgrade

## Scope

This phase adds worked artifact, acceptance-criteria, decision-record, progress-ledger, QA traceability, upgrade-trigger, and closure evidence to representative Group 01 lifecycle skills. Existing step templates remain authoritative and are not duplicated.

## New focused packs

| Skill | New material |
|---|---|
| `sk-business-analysis` | Requirements-to-acceptance evidence, business rules, trace IDs, blockers and handoff readiness |
| `sk-specify` | Single-mode selection, stable IDs, decision records and artifact-specific evidence |
| `sk-planning` | Plan-to-execution gates, task-card readiness, DoD, rollback and handoff |
| `sk-quick-fix` | Upgrade triggers for API/schema/auth/ambiguity/scale/dependency changes |
| `sk-execution` | Progress status, evidence, blocked/skipped semantics and legacy-to-canonical handoff |
| `sk-tester` | Requirement → AC → test case → execution → defect → test summary traceability |
| `sk-done` | Closure status, verification consumption, acceptance decision, residual risk and follow-up |

## Acceptance evidence

Each pack is linked from its owning skill and describes a realistic lifecycle scenario, explicit artifact fields, failure/blocked behavior, expected evidence, and next-owner handoff. The packs preserve the existing Group 01 step contracts and distinguish `sk-tester` QA/STLC ownership from per-task execution verification.

## Validation run

| Check | Result |
|---|---|
| Catalog validator | PASS — 222 skills, 0 errors |
| Markdown fences | PASS — 0 unbalanced |
| Internal Markdown links | PASS — 0 broken |
| Local reference paths | PASS — 0 missing |
| Phase 7 focused packs | PASS — 7/7 linked and non-empty |
| JSON/YAML parse | PASS — 1 JSON and 3 YAML resources |
| Bundled JavaScript syntax | PASS — 24 files |
| Bundled shell syntax | PASS — 1 file |
| Existing Node test suite | PASS — 10 tests |
| `git diff --check` | PASS |
