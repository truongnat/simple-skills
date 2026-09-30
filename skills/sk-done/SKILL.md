---
name: sk-done
description: "Close a task after canonical execution, review, and verification with DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, and optional RELEASE_NOTE.md. Use for final status and handoff. (Hard contract in this SKILL.md — MUST follow.)"
sk-kind: domain
sk-version: 0.1.0
sk-tags: [closure,release]
sk-roles: [main]
sk-compatible: [claude, cursor, codex, gemini]
---

# Done

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Close a task with clear, honest, reviewable artifacts.

Prefer inputs from `EXECUTION.md`, `REVIEW.md`, `VERIFY.md`, `PLAN.md` (DoD/rollback), and `TASKS.md` when present (task completion vs intended cards). Final status must consume the canonical `sk-verify-pro` result.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately after this Contract, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in DONE.md with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the closing artifacts, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | the detailed instructions in this skill | Inputs gathered + DONE.md opened (with progress checklist) |
| 02 | the detailed instructions in this skill | Memory entry + INDEX pointer |
| 03 | the detailed instructions in this skill | DONE.md filled + PR artifacts + wiki sk-sync |
| 04 | the detailed instructions in this skill | Gates + commit + archive |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|

### Required artifacts

Use `references/closure-and-decision-evidence.md` to consume canonical verification, record acceptance ownership, residual risk, follow-up, and an auditable closure decision.

#### `DONE.md`
- Required: yes
- **step_ledger** (required): `## progress checklist` table — Step \| Name \| Status \| Evidence for steps 01–04; statuses `todo`/`complete`/`blocked`, updated at the end of every step, never a later `complete` while an earlier row is `todo`/`blocked` (progress checklist).
- **executive_summary** (required, array): Maximum five bullets with final status, delivered value, verification, residual risk, and next action.
- **developer_overview** (required, object): Final status, verification summary, residual risks, next action.
- **charts** (optional, array): Mermaid delivery/verification chart when useful; otherwise N/A.
- **status** (required, string): Done / Done with risks / Needs fix / Blocked / Partial.
- **summary** (required, string): Outcome-focused summary (not file list).
- **scope_completed** (required, array): Scope item, status, evidence.
- **what_changed** (required, array): Area, change summary, reason.
- **files_changed** (required, array): File path, summary.
- **verification** (required, array): Check, command/method, result, evidence.
- **sk-review_result** (optional, string): Findings and resolution, or 'No findings.'
- **skipped_failed_checks** (optional, array): Check, status, reason, risk.
- **risks_followups** (optional, array): Item, type (risk/follow-up/blocker), impact, owner/next action.
- **handoff** (required, string): Next step, reviewer focus, QA focus, deployment notes.

#### Docs wiki sk-sync (per the project documentation settings)
- If the project documentation settings.enabled` is false, skip.
- If the project documentation settings.sk-sync_strategy: with-commit`: run the `sk-docs` skill in `sk-sync`
  mode for this task's change set and **stage the wiki changes so they land in
  the same commit** as the task (they travel through the PR).
- If the project documentation settings.sk-sync_strategy: main-only`: do **not** touch the wiki here on a
  feature branch — note in DONE.md that the wiki is refreshed on `main`.

- Required: yes. Persists **across tasks** (not per session) — sibling to
  `templates/MEMORY_ENTRY.template.md`, then add/refresh a one-line pointer in
  if missing; newest on top).
- **Vital few (mandatory):** capture only knowledge that will change future
  work — non-obvious decisions + why, gotchas, reusable conventions, pointers.
  It is **not** a changelog: omit anything reconstructable from git, `DONE.md`,
  or the code. If nothing durable was learned, still create the entry with
  `Outcome` filled and each section `None.` — do not pad. Do not title the
  supersedes or extends an existing entry, update that entry instead of adding
  a near-duplicate.

#### `PR_MESSAGE.md`
- Required: no
- Conventional commit format: feat/fix/refactor(scope): summary.

#### `PR_DESCRIPTION.md`
- Required: no
- Summary, Changes, Verification, Review Notes, Risks/Follow-ups.
- Must answer Design for handoff: what / why / how verified / next (reviewer focus).
- Verification must be evidence over confidence (named check + result — not a vague claim).

#### `RELEASE_NOTE.md`
- Required: no
- Only when change is user-facing or user requests it.

### Reference

## Quality Standards

- [ ] Final status is one of: Done / Done with risks / Needs fix / Blocked / Partial.
- [ ] Summary describes outcome, not a file list.
- [ ] Verification distinguishes: passed / failed / skipped / not run.
- [ ] No failed check is marked as passed.
- [ ] Review result is included.
- [ ] PR_MESSAGE.md follows Conventional Commits format.
- [ ] PR_DESCRIPTION.md answers: what changed, why, how verified, reviewer focus
- [ ] Verification is evidence-backed (passed/failed/skipped/not run) — not
- [ ] DONE handoff names next + risks; no chat-only material context.
- [ ] When TASKS.md exists, DONE summary reflects completed vs remaining task IDs honestly (use Progress board / Status / checkboxes; do not claim Done if open `todo`/`in_progress`/`blocked` IDs remain without documented blockers).

- [ ] First-pass readable: concrete names (paths/APIs/IDs); no abstract filler.
- [ ] No leftover `_(TODO)_` or placeholder Mermaid in finished sections.
- [ ] Spec/sk-review findings state finding + evidence + verdict (not essays).

## WRONG vs CORRECT

```markdown
// WRONG — file list instead of outcome
Changed: teacher-form.tsx, teacher-service.ts, teacher-test.ts

// CORRECT — outcome-focused
Summary: Preserved teacher list search state when navigating back from detail page,
including year filter restoration and search keyword persistence.
```

```markdown
// WRONG — hiding skipped checks
Verification: all passed.

// CORRECT — honest reporting
Verification:
- typecheck: passed
- lint: passed
- unit tests: skipped (test database not available)
- e2e: skipped (browser setup unavailable)
Residual risk: Main flow not verified by automated tests. Manual completion check.
```

## Edge Cases

| Situation | Handling |
|---|---|
| Task has blockers | Status = Blocked. DONE.md records blocker and suggested next action. Do NOT create PR artifacts. |
| No PR template found in repo | Use fallback template from this skill. Document in notes. |
| User only needs summary, no PR | Use Lite Mode. No file creation needed. |
| Review found issues that were fixed | Document finding → resolution → evidence in sk-review_result section. |
| Scope changed during sk-execution | Document deviation in DONE.md. Note whether deviation was reviewed. |

## Limitations

- Does NOT auto-fix code.
- Does NOT turn unverified tasks into complete.
- When TASKS.md exists, do not claim Done if open task IDs remain without documented blockers.
- If sk-review found blockers, return to sk-execution before complete.

## Output

Produce a reusable done artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-done`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.
