# Step 04 — Self-check and handoff

## Goal

Verify artifacts against the planning contract. Fail closed — do not hand off if checks fail.

## Checks (run all)

1. Session folder listing shows both `PLAN.md` and `TASKS.md`.
2. `PLAN.md` has **no** `### T-00x` sections with AC/Verify/Files/Status bodies.
3. `TASKS.md` has `plan_ref` and at least one real `### T-00x` card (not only empty template titles).
4. Every ID in PLAN Task index appears in TASKS.md Execution order and as a heading.
5. First implement-oriented task is **not** “write test cases / TC matrix / 6 dimensions” before feature code.
6. No single epic card for whole FE page or whole BE layer when design has more detail — split or flag FAIL.
7. Update PLAN Handoff: set Ready only if checks 1–6 pass; else list failures and return to step-02 or step-03.

## Done when

- [ ] All checks pass **or** blockers explicitly documented and Ready=No with next action.
- [ ] User is told: planning complete → next skill `sync` (only if Ready).

## Stop

Do **not** invent an extra step. Do **not** implement code here.
Planning skill ends when this step completes.
