# Step 02 — Fill PLAN.md (strategy only)

## Goal

Fill `PLAN.md` as **strategy only**. Full task cards stay empty in `TASKS.md` until step-03.

## Rules

- Edit **only** `PLAN.md` in this step.
- Prefer inputs: `DETAIL_DESIGN.md` → `BASIC_DESIGN.md` → `DISCUSSION.md` / BA notes.
- **Forbidden in PLAN.md:** `### T-00x` bodies with Description / AC / Verify / Files / Status.
- Task index = ordered **ID + short title** only (implement before tests).
- Do **not** put “write test cases / 6 dimensions matrix” as the first index item before feature work.
- Do **not** start step-03 until PLAN sections below are filled (no leftover `_(TODO)_` on required fields unless marked blocked).

## Fill these PLAN.md sections

1. Goal (one sentence)
2. Scope / Non-goals
3. Assumptions (risk + confirmed)
4. Approach (phases only)
5. Affected areas (high level + confidence)
6. Test strategy (optional — after-code)
7. Verification strategy
8. Definition of done
9. Rollback strategy
10. Risks
11. Task index (summary → points to TASKS.md)
12. Handoff (blockers; Ready stays No until step-04)

## Done when

- [ ] Required PLAN sections filled (or explicitly blocked with open questions).
- [ ] No full task cards inside PLAN.md.
- [ ] Task index lists intended IDs in implement-then-test order.

## Next

Read and follow `./step-03-fill-tasks.md`.
Do **not** claim planning complete yet.
