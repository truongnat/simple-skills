---
name: sk-planning
description: >-
  Step workflow: seed PLAN/TASKS templates then fill (strategy then micro-tasks).
  MUST copy templates to session, fill PLAN slim then TASKS, self-check. Implement
  before tests. (Hard contract in this SKILL.md — MUST follow.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [planning,task-breakdown]
sk-roles: [reasoner]
sk-compatible: [claude, cursor, codex, gemini]
---

# Planning

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Produce **two task files on disk** via a **forced step sequence** (BMAD-style micro-file):

1. Seed templates → `PLAN.md` + `TASKS.md`
2. Run decision gate + **Spec quality sk-review**; **stop and ask** on unresolved Critical/blocking/visual/Spec-quality
   decisions; then fill **PLAN.md**
3. Fill **TASKS.md** (micro-tasks from design) — only after Spec quality gate passes
4. Self-check before handoff

Prefer `DETAIL_DESIGN.md` when present. Do not invent architecture or contracts. Use the shared artifact contract in `../../docs/GROUP01_SESSION_ARTIFACTS.md`.

## Workflow architecture (mandatory)

This skill uses **sequential step files**. Obey:

- Read **one** step file fully and finish it before opening the next.
- Keep the **progress checklist** in `PLAN.md` updated every step.
- **NEVER** skip step-01 (template seed).
- **NEVER** fill TASKS before PLAN step is sk-done.
- **NEVER** skip Spec quality sk-review (Feasibility / Correctness / Capability).
- **NEVER** fill strategy or TASKS while a Critical issue, blocking unknown,
  blocking Spec quality finding, or unconfirmed `html-recommended` item is open.
- **NEVER** claim complete until step-04 passes (or Ready=No with blockers).
- Do **not** dump full task cards into `PLAN.md`.
- Each step has a **Precondition**. If it fails, return to the previous step.

Skill root paths (relative to this skill):

| Path | Role |
|------|------|
| [templates/PLAN.template.md](./templates/PLAN.template.md) | Seed for session `PLAN.md` |
| [templates/TASKS.template.md](./templates/TASKS.template.md) | Seed for session `TASKS.md` |
| the detailed instructions in this skill | Copy templates into session |
| the detailed instructions in this skill | Fill PLAN strategy only |
| the detailed instructions in this skill | Fill TASKS micro-cards |
| the detailed instructions in this skill | Verify + handoff |

### Execution entry

**Start here:** Read and follow the detailed instructions in this skill immediately after this Contract.

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action.

| Field | Requirement |
|-------|-------------|
| preferred_role | `reasoner` (routing hint for multi-CLI; fallback main). |
| Inputs | DETAIL_DESIGN.md when present; else BASIC_DESIGN.md / DISCUSSION.md / BUSINESS_ANALYSIS.md; issue/visual triage and clarification answers; user request; codebase mapping; constraints. |
| Outputs | Session folder MUST contain filled `PLAN.md` + `TASKS.md` seeded from templates. `TASKS.md` MUST include Work inventory + specific micro-cards (not layer epithets only). Incomplete if PLAN-only, chat-only, tasks embedded in PLAN, empty template left, or vague epic cards. |
| Safety | Do NOT implement code. Do NOT skip steps. **Confirm-first:** STOP immediately on Blocking; classify Ask method before strategy/tasks — reuse Clarification/memory; do not finish PLAN/TASKS as a quiz. Do NOT silently choose defaults or invent omitted feature policy. Planning classifies visual need but does not create HTML itself; route confirmed HTML needs to sk-brainstorming/sk-basic-design and resume after the decision. Do NOT finish without both files, set Ready=Yes with blockers, invent paths, or treat assumptions/specs as confirmed. |

### Required artifacts

#### `PLAN.md` (from template)
Strategy only: executive_summary, developer_overview, charts (Mermaid when
useful), pre_sk-planning_decision_gate,
clarification_questions, visual_triage, spec_quality_sk-review (feasibility,
correctness, capability_recommendations), goal, scope, non_goals, assumptions,
approach, affected_areas, test_strategy (optional), verification_strategy,
definition_of_sk-done, rollback_strategy, risks, **task_index** (ID + title only),
handoff.

#### `TASKS.md` (from template)
Work inventory table, Progress board (Done checkbox + Status per ID), plan_ref, sk-execution_order, micro-task cards (Trace with §/AC, Status=`todo`, Work items ≥2 as `- [ ] N. …`, Description, AC observable, Verify, Flow/comment notes, Files/scope concrete, confidence, out-of-scope). Implement before automated tests. Planning seeds progress; sk-execution marks completion.

Use `references/planning-to-execution-handoff.md` to gate scope, decisions, task-card readiness, DoD, rollback, dependencies, and the next-owner handoff.

### Reference

## Forbidden outputs (reject / rewrite)

| Failure | Fix |
|---------|-----|
| No template seed (wrote files free-form only) | Restart at step-01 |
| progress checklist skipped / later step `sk-done` while earlier `todo`/`blocked` | Fix ledger; return to earliest incomplete step |
| Only `PLAN.md` / TASKS still template placeholders | Continue/finish step-03 |
| Full task cards inside `PLAN.md` | Move cards to `TASKS.md`; slim PLAN |
| T-001 = test matrix before code | Reorder: implement then tests |
| No Work inventory / one “implement feature” row | Build inventory per step-03 §A |
| Epic / vague layer titles / multi-endpoint card | Split + add Work items + Trace § per step-03 §B–C |
| Ready=Yes with open Blockers (or DISCUSSION blockers ignored) | Set Ready=No; copy blockers; re-run step-04 |
| Filled strategy/tasks before Critical/blocking clarification | Stop, ask, record answer, then resume |
| TASKS filled before Spec quality sk-review sk-done | Return to step-02; clear premature cards if needed |
| Specs/design accepted without feasibility/correctness/capability sk-review | Fill Spec quality sk-review; ask blocking gaps |
| Planning generated HTML without a visual decision handoff | Set Ready=No; route to sk-brainstorming/sk-basic-design |

## What a TASK is

- Traceable to a **design section / AC** (`Trace:` with § or id).
- One inventory unit (not entire screen/service/layer).
- Numbered **checkbox Work items** (`- [ ] 1. …`) an executor can follow and check off without re-reading the whole design.
- A **Progress board** row per card so status is visible at a glance.
- Independently verifiable after deps exist.
- Order: models → service → API → UI → **then** tests.

## Lite Mode

Still run **all four steps**. TASKS may have 1–3 cards; templates still required.

## Quality Standards

- [ ] Goal and approach are concrete (paths/phases), not abstract process talk.
- [ ] Spec quality findings are finding + evidence + verdict (not essays).
- [ ] Every TASK card has `#### Dev context` with Source cites or `No specific guidance found.`
- [ ] First-pass readable: concrete names (paths/APIs/IDs); no abstract filler.
- [ ] No leftover `_(TODO)_` or placeholder Mermaid in finished sections.
- [ ] Ready=Yes only when blockers are `none`.

- [ ] Confirm-first: on Blocking need, STOP immediately; classify Ask method (`confirm`/`choice`/`fact`/`table`/`diagram`/`html`); ask that way; finished artifact is not a quiz — residual Open questions non-blocking only (the skill instructions).

## Limitations

- Does NOT implement code.
- Does NOT replace design skills when contracts/architecture are missing (non-Lite).
- Does NOT require tests-before-code.
- Does NOT create visual HTML. It triages the need and blocks/hands off until
  the visual decision is resolved.

## Output

Produce a reusable planning artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-planning`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.
