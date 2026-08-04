# Step 01 — Init (seed all templates)

## Goal

Create session artifacts from templates **before** filling content.

## Precondition (fail closed)

- [ ] Tester `SKILL.md` contract was read fully
- [ ] Session path is known or can be created safely
- [ ] All 5 templates exist in `skills/tester/templates/`

If any template is missing, stop and report it. Do **not** invent a replacement.

## Rules

- Read this step fully. Do **not** jump to reviewing requirements yet.
- Do **not** invent artifacts free-form — copy templates.
- Do **not** proceed to step-02 until all files exist on disk.
- Do **not** create PLAN/TASKS/design docs in this skill.

## Actions

1. Resolve the active session dir (do **not** invent a folder name):
   `bash .agents/tools/session/session.sh current` — reuse that path as
   `{session}` below. If none is active yet, create one with
   `session.sh new <short-slug>`. Never write to a temp/cache/scratchpad path.
2. Locate skill templates:
   - `{skill-root}/templates/TEST_PLAN.template.md`
   - `{skill-root}/templates/REQ_REVIEW.template.md`
   - `{skill-root}/templates/TESTCASES.template.md`
   - `{skill-root}/templates/DEFECT_LOG.template.md`
   - `{skill-root}/templates/TEST_SUMMARY.template.md`
3. Copy (Write tool) each template into the session dir:
   - `TEST_PLAN.md` ← TEST_PLAN.template.md
   - `REQ_REVIEW.md` ← REQ_REVIEW.template.md
   - `TESTCASES.md` ← TESTCASES.template.md
   - `DEFECT_LOG.md` ← DEFECT_LOG.template.md
   - `TEST_SUMMARY.md` ← TEST_SUMMARY.template.md
4. If any file already exists with real content:
   - Ask user: overwrite with fresh template, or keep and continue from the appropriate step.
5. Set Step ledger row 01 to `done` with evidence = paths in all 5 files.
6. List the session directory and confirm all 5 files exist.

## Done when

- [ ] All 5 `.md` files exist in session (from templates).
- [ ] Step ledger 01 = `done` in all 5 files.
- [ ] Confirmed via directory listing.

## Next

Only after Done: Read and follow `./step-02-review-requirements.md`.
