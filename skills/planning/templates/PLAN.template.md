# Plan

> Filled by planning step-02. Strategy only — **no** full task cards
> (`### T-00x` with AC/Verify/Files) in this file. See `TASKS.md` for work.
> Write for a busy teammate: concrete paths/phases — no filler.
> Obey `.agents/SKILL_PREAMBLE.md` Readable writing.

## Step ledger (mandatory — update every step)

| Step | Name | Status | Evidence |
|---|---|---|---|
| 01 | Init templates | `todo` / `done` | PLAN.md + TASKS.md exist |
| 02 | Fill PLAN + Spec quality | `todo` / `done` / `blocked` | Feasibility/Correctness/Capability filled |
| 03 | Fill TASKS inventory/cards | `todo` / `done` / `blocked` | Work inventory + cards |
| 04 | Self-check | `todo` / `done` / `blocked` | Ready Yes/No with evidence |

> **Hard rule:** Do not mark a later step `done` while an earlier step is still
> `todo`/`blocked`. Do not fill TASKS before Spec quality review is done.

## Executive summary

<!-- ≤5 concrete bullets. Fill last, keep first. -->

- _(TODO)_

## Developer overview

| Field | Value |
|---|---|
| Status | `needs_info` / `planning` / `ready_for_sync` / `blocked` |
| Cards drafted | `0` |
| Critical open decisions | `0` |
| Next action | _(ask user / fill tasks / sync)_ |

## Charts (optional)

<!-- Omit unless useful. No placeholder Mermaid. -->

## Pre-planning decision gate

<!-- Inherit unresolved items from DISCUSSION/BA/design. Do not fill strategy
while a blocking row is open. -->

| Issue ID/source | Issue / decision | Severity | Clarity | Blocking? | Visual need/format | Resolution evidence | Status |
|---|---|---|---|---|---|---|---|
| _(TODO)_ | _(TODO — one concrete decision)_ | Critical / High / Medium / Low | Clear / Partial / Unknown | Yes / No | none / text / table / diagram / html-recommended | _(user answer/path)_ | Open / Resolved |

### Questions requiring user input

| Issue | Focused question | Why the plan changes | Answer |
|---|---|---|---|
| _(TODO)_ | _(TODO)_ | _(TODO)_ | _(wait for user)_ |

> **STOP gate:** Strategy and TASKS stay unfilled while any Critical issue,
> blocking unknown, or unconfirmed `html-recommended` item is open.

## Spec quality review

<!-- Concrete finding + evidence + verdict. No abstract essays. -->

### 1. Feasibility

| Finding (concrete) | Evidence | Verdict |
|---|---|---|
| _(TODO)_ | _(repo / design / ops)_ | Pass / Pass-with-gaps / Fail / Unknown |

### 2. Correctness

| Finding (concrete) | Evidence | Verdict |
|---|---|---|
| _(TODO)_ | _(repo / API / DB / screen)_ | Pass / Pass-with-gaps / Fail / Unknown |

### 3. Capability gaps

| Gap ID | Missing capability | Ask or default | Blocking? | Status |
|---|---|---|---|---|
| CAP-001 | _(TODO)_ | _(ask / propose)_ | Yes / No | Open / Deferred / Resolved |

## Goal

<!-- One sentence. -->

_(TODO)_

## Scope

- _(TODO)_

## Non-goals

- _(TODO)_

## Assumptions

| Assumption | Risk | Confirmed |
|------------|------|-----------|
| _(TODO)_ | Low / Medium / High | No / Yes |

## Approach

<!-- Phased strategy only — not per-task AC/Verify/Files. -->

1. _(TODO — phase with concrete deliverable)_
2. _(TODO — phase)_
3. _(TODO — phase: implement feature before automated tests)_

## Affected areas

| Area / path | Expected change | Confidence |
|-------------|-----------------|------------|
| _(TODO — real path)_ | _(TODO)_ | known / inferred / unknown |

## Test strategy

<!-- Optional. How to verify **after** code exists. -->

- _(TODO or N/A)_

## Verification strategy

- _(TODO — automated command)_
- _(TODO — manual check)_

## Definition of done

- [ ] _(TODO — observable)_
- [ ] `TASKS.md` complete and matches Task index below

## Rollback strategy

- **Code:** _(TODO)_
- **Config:** _(TODO)_
- **Data:** _(TODO or N/A)_

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| _(TODO)_ | _(TODO)_ | _(TODO)_ |

## Task index

<!-- Draft OK in step-02. Step-03 replaces with fine-grained IDs. ID + title only. -->

T-001 _(title)_ → T-002 _(title)_ → … → T-00N _(tests after code)_ (see TASKS.md)

## Handoff

<!-- Ready=Yes ONLY if blockers is `none`. Never Yes + open blockers. -->

- Ready for sync/execution? **No**
- Blockers: _(list unresolved items, or `none`)_
