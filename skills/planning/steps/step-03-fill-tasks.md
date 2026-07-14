# Step 03 — Fill TASKS.md (micro-tasks)

## Goal

Fill `TASKS.md` with **fine-grained micro-tasks** broken from design/docs. Match `PLAN.md` Task index.

## Rules

- Edit **TASKS.md** (and only adjust PLAN Task index if IDs must stay aligned).
- Each task = one concern; include `Trace:` to design/spec/BA.
- **Order:** models/contracts → service/ops → API/entrypoints → UI/client → **then** automated tests.
- Do **not** make T-001 (or first task) a test-case document / coverage matrix before code exists.
- Do **not** use epic cards (“Build entire FE page”, “Implement whole service”).
- Duplicate `### T-00x` template blocks as needed; delete unused placeholders.
- Lite Mode: still fill TASKS.md (1–3 specific cards).

## Fill

1. `plan_ref: PLAN.md`
2. Execution order (same IDs as PLAN Task index)
3. Notes (optional)
4. Full cards: Status, Trace, Depends, Description, AC, Verify, Files/scope + confidence

## Done when

- [ ] Every Task index ID has a `### T-00x` card in TASKS.md.
- [ ] Cards are micro-tasks with Trace + AC + Verify.
- [ ] Automated test tasks (if any) come after implement tasks for those surfaces.
- [ ] No leftover empty placeholder titles like `_(short title)_` on kept cards.

## Next

Read and follow `./step-04-self-check.md`.
