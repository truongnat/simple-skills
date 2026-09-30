---
name: sk-quick-fix
description: >-
  Tiny clear fix path (Path=Quick): create a short session note + 1–3 TASK cards
  with Dev context, then hand off to sk-sync/sk-executing-pro. No BA, design, or Spec
  matrices. Use for one-line bugs and obvious small changes.
sk-kind: domain
sk-version: 0.1.0
sk-tags: [execution,small-change]
sk-roles: [coder]
sk-compatible: [claude, cursor, codex, gemini]
---

# Quick Fix

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing** + Scale) before Purpose,
Contract, or steps. Path must be **Quick**. If the change is unclear or needs
product/design decisions, stop and upgrade to Lite/Full (`sk-brainstorming` /
`sk-planning`).

## Purpose

Ship a **small, clear** change without Full lifecycle ceremony.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in QUICK.md with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifacts, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | the detailed instructions in this skill | Session + seeded QUICK.md with Outcome-first Goal |
| 02 | the detailed instructions in this skill | Slim TASKS.md (1–3 cards with Dev context) |
| 03 | the detailed instructions in this skill | Gates + commit + handoff to sk-sync |

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `coder` (routing hint for multi-CLI; fallback main). |
| Outputs | Session with `QUICK.md` + `TASKS.md` (1–3 cards with Dev context) + `CONTEXT.md` via the project context; Path=`Quick` recorded |
| Safety | **Forbidden on Quick:** `BUSINESS_ANALYSIS.md`, `BASIC_DESIGN.md`, `DETAIL_DESIGN.md`, Spec quality matrices, inventing product rules. Do NOT implement until sk-sync readiness allows. If unknowns block → upgrade Path. |

### Upgrade triggers

Use `references/upgrade-trigger-matrix.md` to record the trigger, target path, decision owner, and required evidence whenever Quick must upgrade to BA, design, architecture, security, or planning.

Upgrade to `sk-business-analysis`, a design skill, or `sk-planning` before implementation when any condition holds:

- the change touches a public API, schema, migration, authentication, authorization, or data retention;
- there are more than three independently verifiable outputs;
- product, UX, stakeholder policy, or expected behavior is ambiguous;
- no falsifiable AC and Verify pair can be written;
- the change crosses a service boundary or adds a dependency.

Record the trigger and target path in `QUICK.md`; do not keep a fuzzy Quick path after an upgrade trigger is found.

### Required artifacts

#### `QUICK.md`
- Path: Quick
- **Goal** (one sentence, Outcome-first: WHO + WHAT + EVIDENCE — not
  activity-only), facts, out of scope, handoff (`sk-sync` then `sk-executing-pro`)
- If rewriting the ask into an outcome surfaces product/design ambiguity →
  **upgrade Path** (do not keep fuzzy Goal on Quick)
- **Small-batch ceiling:** 1–3 cards; more independently verifiable Outputs →

#### `TASKS.md`
- 1–3 cards only; each with Work items, **AC** (observable slice of Goal),
  **Verify** (can falsify AC), Files/scope, **Dev context** + `[Source:]` or
  `No specific guidance found.`

## Workflow (start here)

Start at `steps/step-01-init.md` — the step files are authoritative for
ordering (see Step contract above). Handoff after step-03:
`sk-sync` → need `PASS` (or `CONCERNS` + user OK) → `sk-executing-pro` → `sk-review` → `sk-verify-pro` → `sk-done`.

## Quality Standards

- [ ] Path=Quick recorded; no BA/design files created.
- [ ] Goal passes Outcome-first three-axis (not “fix X” / “add null check” alone).
- [ ] ≤3 TASK cards (Small-batch ceiling); each AC is falsifiable via Verify; each has Dev context with Source or explicit none.
- [ ] First-pass readable; no leftover `_(TODO)_`.
- [ ] Lint OK.

## Limitations

- Does NOT replace sk-brainstorming/sk-planning for unclear work.
- Does NOT skip sk-review/sk-done for merge hygiene.

## Output

Produce a reusable quick fix artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-quick-fix`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.
