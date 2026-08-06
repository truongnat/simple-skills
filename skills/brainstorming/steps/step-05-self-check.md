# Step 05 — Self-check and handoff

## Goal

Verify `DISCUSSION.md` against the contract. Fail closed.

## Precondition (fail closed)

- [ ] Step ledger 01–04 = `done` (or `blocked` with questions asked)
- [ ] Spec quality review sits **before** Scope in/out in the artifact
- [ ] Handoff names exactly one next skill

If precondition fails → return to the earliest incomplete step. Do **not** set
Ready=Yes.

## Checks (run all)

1. File exists and was seeded from template (has Step ledger + Spec quality review).
2. Step ledger is sequential: no later step `done` while an earlier step is `todo`.
3. Issue triage classifies every material issue by severity, blocking status,
   reversibility, and status.
4. Clarification checkpoint records the focused questions actually asked and
   the answers received — not left as unresolved placeholders while later
   steps are `done`.
5. Spec quality review has Feasibility, Correctness, and Capability gaps with
   clear verdicts (no leftover `_(TODO)_` unless blocked).
6. Visual triage matches what was actually created — no `html-recommended`
   row without either a confirmed skip or a linked `VISUAL_DECISION.html`.
7. Scope in and Scope out are both present and do not contradict each other.
8. Options matrix has ≥1 real option; Recommendation has Choose/Reason/Not
   choosing/Confidence.
9. No Ready=Yes / recommendation locked while a Critical issue, blocking
   Spec quality Fail/Unknown, or open Blocking=Yes capability gap remains.
10. Executive summary ≤5 bullets and mentions direction, top risk, and next action.
11. Developer overview Status/Path/Next action reflect the final state.
12. Handoff names exactly one next skill with blockers listed honestly (not
    hidden because the next skill is planning/execution).
13. No PLAN/TASKS/code invented by this skill.
14. Mark Step ledger 05 `done` or `blocked` with checklist evidence.

## Done when

- [ ] All checks pass **or** Handoff blockers are non-empty and honest.
- [ ] Step ledger 05 = `done` or `blocked`.
- [ ] User is told the next skill and path to `DISCUSSION.md`.

## Stop

Brainstorming ends here. Do **not** auto-run business-analysis/basic-design/
planning/research/execution unless the user asks.
