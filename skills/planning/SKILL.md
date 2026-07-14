---
name: planning
description: "MUST write both PLAN.md and TASKS.md files to the session folder (not chat-only). Fine-grained micro-tasks from design; implement before tests. (Hard contract in this SKILL.md — MUST follow.)"
---

# Planning

## Purpose

Turn a clear goal into:

1. **PLAN.md** — strategy: scope, approach, verification, DoD, rollback, risks.
2. **TASKS.md** — **fine-grained micro-tasks** broken from DISCUSSION / BA / BASIC_DESIGN / DETAIL_DESIGN / PLAN so execution can implement step by step without guessing.

Prefer `DETAIL_DESIGN.md` as input when present (then `BASIC_DESIGN.md`, then `DISCUSSION.md`). Do not re-design architecture or invent contracts — use the design artifacts.

Do **not** put full task cards in PLAN.md. PLAN may only list a `task_index` (ordered IDs + short titles) pointing at TASKS.md.

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | DETAIL_DESIGN.md when present; else BASIC_DESIGN.md / DISCUSSION.md / requirement notes; user request; codebase mapping; affected systems; constraints. |
| Outputs | MUST write two session files on disk: PLAN.md and TASKS.md. Incomplete if only PLAN.md or only chat output. |
| Safety | Do NOT implement code during planning. Do NOT finish planning without writing BOTH PLAN.md and TASKS.md files to the session directory on disk. Do NOT put task bodies only in chat or only inside PLAN.md. Do NOT dump full task cards into PLAN.md — those belong in TASKS.md. Do NOT invent affected files without inspecting the codebase. Do NOT treat assumptions as confirmed. Do NOT skip rollback for destructive changes. Do NOT re-design architecture when design artifacts already exist. Do NOT put test-writing tasks before the feature code those tests would cover. Do NOT emit vague epic-level tasks when design detail exists. |

### Required artifacts

#### `PLAN.md`
- Required: yes
- **goal** (required, string): One sentence.
- **scope** (required, string): In scope summary.
- **non_goals** (optional, array): Explicitly excluded outcomes.
- **assumptions** (required, array): Assumptions with risk and confirmation status.
- **approach** (required, string): Phased strategy (how work will proceed). Not step-by-step file edits.
- **affected_areas** (optional, array): Systems/dirs to touch with confidence (known / inferred / unknown). High level only.
- **test_strategy** (optional, string): When/how to verify after code exists (frameworks in project). Not write-tests-first.
- **verification_strategy** (required, string): Automated and manual verification approach for the whole change.
- **definition_of_done** (required, array): Checklist of verifiable completion conditions.
- **rollback_strategy** (required, string): How to undo changes per type (code/config/data).
- **risks** (optional, array): Risks with impact and mitigation.
- **task_index** (required, array): Ordered task IDs summarizing TASKS.md (implement before tests), e.g. T-001 Model → T-002 Service → T-003 API → T-004 Tests.
- **handoff** (required, string): Ready for sync/execution? Blocking items? Review required?

#### `TASKS.md`
- Required: yes
- **plan_ref** (required, string): Reference to PLAN.md. MUST be a real file in the same session folder.
- **tasks** (required, array): Micro-task cards broken from design/docs: ID, title, description (steps + design trace), dependencies, acceptance_criteria, verification, files_or_scope, confidence, status.
- **execution_order** (required, array): Ordered task IDs. Feature implementation before automated tests for the same surface.
- **notes** (optional, array): Sequencing notes, blockers, or split-file references.

### Reference

`agents/openai.yaml` is a machine-readable duplicate for tooling. The Contract in this SKILL.md is authoritative for agents.

## Mandatory file writes

Planning is **incomplete** until **both** files exist on disk in the session folder (Write/Edit tools — chat-only does not count):

1. Write `PLAN.md` (strategy + `task_index` only).
2. Write `TASKS.md` (full micro-task cards) — **required every time, including Lite Mode**.
3. Confirm `PLAN.md` `task_index` IDs match `TASKS.md`.
4. Only then hand off to sync/execution.

Do **not** stop after `PLAN.md` alone. Do **not** put the full task list only in chat or only inside `PLAN.md`.

### TASKS.md template (required shape)

```markdown
# Tasks

plan_ref: PLAN.md

## Execution order
T-001 → T-002 → T-003 → …

## Tasks

### T-001: <short title>
- Status: todo
- Trace: <DESIGN/DOC section or ID>
- Depends: none | T-00x
- Description: <concrete steps>
- AC: <acceptance criterion>
- Verify: <how to check after this task>
- Files/scope: <paths or area> (confidence: known|inferred|unknown)

### T-002: …
```

## What a TASK is

A task is **not** a vague epic (“Build export”). It is a **smallest useful unit of work** derived from design/docs:

- Traceable to a specific design/plan/BA bullet (cite section or ID).
- One primary change concern (e.g. one endpoint handler, one model field set, one validation rule, one UI binding).
- Clear enough that execution does not invent missing design.
- Independently verifiable after it is done (or after its dependent implement tasks exist).

**Default order: implement feature code first, then add/verify tests.** Do not schedule “write automated tests” before the code under test exists. Optional early tasks may only clarify data/setup or manual checklists — not pretend to unit-test absent code.

## Dynamic depth

- Lite Mode: thin PLAN + short TASKS (still specific — not epics).
- Full Mode: many small cards from DETAIL_DESIGN surfaces (contracts, operations, client mapping, persistence).
- Split large epics until each card has a single outcome and clear files/scope.

## Quality Standards

### PLAN.md

- [ ] Goal is one sentence; scope and assumptions are clear.
- [ ] Approach is phased strategy — not a dump of file-level steps.
- [ ] Verification strategy and DoD are falsifiable.
- [ ] Rollback matches change scope (code/config/data as needed).
- [ ] `task_index` lists every TASKS.md ID in order (summary only).
- [ ] No full AC/verify/file lists inside PLAN task sections.
- [ ] **Both `PLAN.md` and `TASKS.md` files exist on disk** in the session folder.

### TASKS.md — granularity

- [ ] **`TASKS.md` file was written** (not only described in chat).
- [ ] Each task traces to a concrete design/doc source (section, BR/AC, contract, operation).
- [ ] Each task is a **micro-task**: one concern — not “implement whole feature”.
- [ ] Description includes enough steps that execution can follow without inventing design.
- [ ] Each task has ID, AC, verification method, and files_or_scope with confidence.
- [ ] Dependencies and `execution_order` are consistent.
- [ ] **Implementation / wiring tasks come before automated test tasks** for the same surface.
- [ ] Test tasks (if any) name the code/surfaces already created by prior tasks.
- [ ] Status starts as `todo` unless already agreed otherwise.

### Sequencing (implement → then test)

1. Models / contracts / persistence shapes needed by the feature.
2. Service/domain logic and operations from DETAIL_DESIGN.
3. API / CLI / entrypoints and client/UI wiring as in scope.
4. Manual smoke or project-framework tests **after** code under test exists.
5. Do NOT invent a test framework. Use what the project already has.

## WRONG vs CORRECT

```markdown
// WRONG — finished planning with only PLAN.md or chat bullet list
Created PLAN.md. Tasks: 1) … 2) … (no TASKS.md file)

// CORRECT — two files on disk
Wrote `.agents/sessions/.../PLAN.md`
Wrote `.agents/sessions/.../TASKS.md` with full T-00x cards matching task_index
```

```markdown
// WRONG — epic dumped as one task
T-001: Implement export feature.

// CORRECT — micro-tasks from DETAIL_DESIGN
T-001: Add ExportRequest/ExportResult fields per DETAIL_DESIGN contracts (trace: §contracts).
T-002: Implement permission check in export service (trace: §rules_and_validation).
T-003: Wire POST /api/export handler to service (trace: §contracts).
T-004: Add API test for 403 unauthorized — after T-002/T-003 exist.
```

```markdown
// WRONG — tests before code
T-001: Write all unit tests for export
T-002: Implement export

// CORRECT — code first, then tests
T-001–T-003: Implement model → service → endpoint
T-004: Add tests for T-001–T-003 using project test framework
```

```markdown
// WRONG — all task detail stuffed into PLAN.md
## Tasks
T-002: Edit FooService.cs line 40… AC: …

// CORRECT — PLAN stays strategic; detail in TASKS.md
## Approach
1. Follow DETAIL_DESIGN contracts
2. Implement model → service → API
3. Verify with project tests after code exists
## Task index
T-001 … T-004 (See TASKS.md)
```

```markdown
// WRONG — vague TASKS card
T-002: Update the export feature.

// CORRECT — verifiable micro-task
T-002: Add server-side permission check for export endpoint.
Trace: DETAIL_DESIGN §rules_and_validation + §contracts POST /api/export
Depends: T-001 (ExportRequest model)
AC: Unauthorized token on POST /api/export returns 403.
Verify: After T-003 wires the endpoint, curl with unauthorized token → 403.
Files: inferred export service/controller (confirm in sync).
Status: todo
```

## Edge Cases

| Situation | Handling |
|---|---|
| Design is thin | Still break into smallest clear steps; mark confidence unknown; add investigate if blocked. |
| Affected files unknown | Mark confidence unknown; do not invent paths. |
| Assumptions block execution | Mark blocking in PLAN; require confirmation before execution. |
| Single-file change | Lite Mode — still write both PLAN.md and TASKS.md (1–3 specific micro-tasks). |
| Agent produced PLAN only | Incomplete. Immediately write TASKS.md before handoff. |
| Large work | Many small TASKS cards (or TASKS-*.md sections); one PLAN. |
| Destructive change | Require user review of PLAN rollback before execution. |

## Limitations

- Does NOT implement code.
- Does NOT replace brainstorming when direction is unclear.
- Does NOT replace basic-design or detail-design when architecture or contracts are missing for a non-Lite task.
- Does NOT re-design architecture when design artifacts already exist.
- Does NOT replace investigate when codebase mapping is missing.
- Does NOT auto-confirm assumptions.
- Does NOT require TDD or tests-before-code.
- Does NOT complete without both `PLAN.md` and `TASKS.md` on disk.
