---
name: planning
description: "MUST write both PLAN.md and TASKS.md on disk. PLAN = strategy only (no ## Tasks body). TASKS = micro-tasks from design; implement before tests. (Hard contract in this SKILL.md — MUST follow.)"
---

# Planning

## Purpose

Turn a clear goal into **two session files on disk**:

1. **PLAN.md** — strategy only: goal, scope, approach, DoD, rollback, risks, **task_index**.
2. **TASKS.md** — fine-grained micro-tasks broken from DISCUSSION / BA / BASIC_DESIGN / DETAIL_DESIGN.

Prefer `DETAIL_DESIGN.md` when present. Do not invent architecture or contracts.

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | DETAIL_DESIGN.md when present; else BASIC_DESIGN.md / DISCUSSION.md / requirement notes; user request; codebase mapping; affected systems; constraints. |
| Outputs | MUST write two session files on disk: PLAN.md (strategy + task_index only) and TASKS.md (full micro-task cards). Incomplete if only PLAN.md, only chat, or full task bodies embedded in PLAN.md. |
| Safety | Do NOT implement code during planning. Do NOT finish without BOTH PLAN.md and TASKS.md on disk. Do NOT put ### T-00x bodies / AC / Verify / Files inside PLAN.md. Do NOT make the first task a test-case document or 6-dimension coverage matrix before feature code. Do NOT emit epic-level tasks when design detail exists. Do NOT invent affected files without inspecting the codebase. Do NOT treat assumptions as confirmed. Do NOT skip rollback for destructive changes. Do NOT re-design architecture when design artifacts already exist. |

### Required artifacts

#### `PLAN.md`
- Required: yes
- **goal** (required, string): One sentence.
- **scope** (required, string): In scope summary.
- **non_goals** (optional, array): Explicitly excluded outcomes.
- **assumptions** (required, array): Assumptions with risk and confirmation status.
- **approach** (required, string): Phased strategy only. No per-task AC/Verify/Files.
- **affected_areas** (optional, array): Systems/dirs at high level with confidence (known / inferred / unknown).
- **test_strategy** (optional, string): How to verify after code exists. Not write-tests-first.
- **verification_strategy** (required, string): Automated and manual verification for the whole change.
- **definition_of_done** (required, array): Falsifiable completion checklist.
- **rollback_strategy** (required, string): Undo strategy per code/config/data.
- **risks** (optional, array): Risks with impact and mitigation.
- **task_index** (required, array): Ordered ID + short title only (implement before tests). No full cards.
- **handoff** (required, string): Ready for sync/execution? Blocking items?

#### `TASKS.md`
- Required: yes
- **plan_ref** (required, string): PLAN.md in the same session folder.
- **tasks** (required, array): Micro-task cards: ID, title, Trace, Description, Depends, AC, Verify, Files/scope, confidence, status. Not epics.
- **execution_order** (required, array): Ordered IDs. Feature implementation before automated tests.
- **notes** (optional, array): Sequencing notes or blockers.

### Reference

`agents/openai.yaml` is a machine-readable duplicate for tooling. The Contract in this SKILL.md is authoritative for agents.

## Forbidden outputs (reject / rewrite)

If any of these happen, planning is **FAILED** — fix before handoff:

| Failure | Why |
|---------|-----|
| Only `PLAN.md` written (no `TASKS.md` file) | Contract requires both files on disk |
| Task cards only in chat | Chat does not count |
| `PLAN.md` contains `## Tasks` with AC / Verify / Files / Status per T-00x | Full cards belong only in `TASKS.md` |
| T-001 (or first task) is “write test cases / TC matrix / 6 dimensions” before feature code | Implement feature first; tests after code exists |
| One task = whole FE page or whole service layer | Must split into micro-tasks |
| Invented Dimension Coverage Formula / Pattern Catalog as required planning ritual | Not part of this skill |

## Mandatory file writes

1. Write `PLAN.md` (strategy + `task_index` only).
2. Write `TASKS.md` (full cards) in the **same session folder**.
3. Verify with a directory listing that **both files exist**.
4. Confirm every `task_index` ID exists in `TASKS.md`.
5. Only then report handoff.

### PLAN.md template (slim)

```markdown
# Plan

## Goal
<one sentence>

## Scope
- …

## Non-goals
- …

## Assumptions
| Assumption | Risk | Confirmed |
|---|---|---|

## Approach
1. …
2. …
(phases only — not full task cards)

## Affected areas
- … (confidence: known|inferred|unknown)

## Verification strategy
- …

## Definition of done
- [ ] …

## Rollback strategy
- …

## Risks
| Risk | Impact | Mitigation |
|---|---|---|

## Task index
T-001 <title> → T-002 <title> → … → T-00N <tests after code> (see TASKS.md)

## Handoff
Ready? Blockers?
```

### TASKS.md template (required)

```markdown
# Tasks

plan_ref: PLAN.md

## Execution order
T-001 → T-002 → T-003 → …

## Tasks

### T-001: <short title>
- Status: todo
- Trace: <DESIGN/DOC § or ID>
- Depends: none | T-00x
- Description: <concrete steps>
- AC: <acceptance criterion>
- Verify: <how to check>
- Files/scope: <path or area> (confidence: known|inferred|unknown)

### T-002: …
```

## What a TASK is

A **micro-task** derived from design/docs:

- Traces to a specific design/BA/spec bullet (`Trace:` required).
- One primary concern (one DTO set, one endpoint, one validation cluster, one UI binding — **not** entire screen).
- Enough steps that execution does not invent design.
- Independently verifiable (or after its implement deps exist).

**Order:** models/contracts → service/ops → API/entrypoints → UI/client → **then** automated tests for those surfaces.

Do **not** schedule “write test case document / coverage matrix” as T-001 before code.

## Dynamic depth

- Lite: both files; 1–3 specific micro-tasks in TASKS.md.
- Full: many cards from DETAIL_DESIGN (contracts, operations, client mapping, persistence).
- Split epics (e.g. “Build FE component”) until each card has one outcome.

## Quality Standards

### PLAN.md

- [ ] No `### T-00x` bodies / no AC+Verify+Files inside PLAN.
- [ ] `task_index` is summary-only; points to TASKS.md.
- [ ] Approach is phases, not file-edit steps.
- [ ] DoD, verification, rollback present.
- [ ] `PLAN.md` and `TASKS.md` both exist on disk.

### TASKS.md

- [ ] File written (not chat-only).
- [ ] Each card has Trace, AC, Verify, Files/scope + confidence.
- [ ] Micro-task size (one concern).
- [ ] Implement tasks before automated test tasks.
- [ ] execution_order matches task_index.

### Self-check before handoff

- [ ] `ls` session folder shows `PLAN.md` and `TASKS.md`.
- [ ] PLAN has **no** full Tasks section.
- [ ] First implement task is **not** “write test cases”.
- [ ] No epic FE/BE “build whole layer” single card when design has more detail.

## WRONG vs CORRECT

```markdown
// WRONG — PLAN.md contains ## Tasks with full T-001…T-007 cards (AC, Verify, Files)
// CORRECT — PLAN.md only has ## Task index: T-001 Models → … → T-00N Tests (see TASKS.md)
```

```markdown
// WRONG — only PLAN.md in session folder
// CORRECT — PLAN.md + TASKS.md both written with Write tool
```

```markdown
 // WRONG — T-001 Viết test case + 6 dimensions formula; then implement
 // CORRECT — T-001 DTOs → … → implement FE/BE → last tasks: automated tests
```

```markdown
// WRONG — T-006 Build entire FE page (form + F-keys + children + validation)
 // CORRECT — separate cards: master-config fields; F3 export wire; F8 print; one child screen; …
```

## Edge Cases

| Situation | Handling |
|---|---|
| Design thin | Smallest clear steps; unknown confidence; investigate if blocked. |
| Files unknown | confidence unknown — do not invent paths. |
| Blocking assumptions | Mark in PLAN; confirm before execution. |
| PLAN-only already exists | Incomplete — write/replace with slim PLAN + new TASKS.md. |
| Destructive change | User must review rollback in PLAN first. |

## Limitations

- Does NOT implement code.
- Does NOT complete without both files on disk.
- Does NOT allow full task cards inside PLAN.md.
- Does NOT require tests-before-code or Dimension Coverage formulas.
- Does NOT replace design skills when architecture/contracts are missing (non-Lite).
