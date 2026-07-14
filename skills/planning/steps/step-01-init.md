# Step 01 — Init (seed templates)

## Goal

Create session folder artifacts from templates **before** filling content.

## Rules

- Read this step fully. Do **not** skip to filling strategy or tasks yet.
- Do **not** invent PLAN/TASKS from scratch — copy templates.
- Do **not** proceed to step-02 until both template files exist on disk in the session folder.

## Actions

1. Resolve session dir: `.agents/sessions/<Task-N-short-description>/` (create if missing).
2. Locate skill templates:
   - `{skill-root}/templates/PLAN.template.md`
   - `{skill-root}/templates/TASKS.template.md`
3. Copy (Write tool) into the session dir as:
   - `PLAN.md` ← PLAN.template.md
   - `TASKS.md` ← TASKS.template.md
4. If `PLAN.md` / `TASKS.md` already exist and are non-template content:
   - Ask user: overwrite with fresh templates, or keep and continue from step-02/03.
   - Default if user says redo planning: overwrite with templates.
5. List the session directory and confirm both files exist.

## Done when

- [ ] `PLAN.md` exists in session (from template).
- [ ] `TASKS.md` exists in session (from template).
- [ ] Confirmed via directory listing.

## Next

Only after Done: Read and follow `./step-02-fill-plan.md`.
Do **not** fill TASKS yet.
