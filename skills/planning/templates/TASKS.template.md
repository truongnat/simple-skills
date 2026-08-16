# Tasks

> Filled by planning step-03. Work inventory first, then task cards.
> Each card is a self-contained context package for execution.
> Implement feature code before automated tests.
> Progress: planning seeds Status=`todo`; execution updates as work completes.

plan_ref: PLAN.md

## Work inventory

<!-- One row per implementable unit. -->

| Inv | Unit | Trace | Layer |
|-----|------|-------|-------|
| I-01 | _(e.g. Add SearchRequest fields: …)_ | _(doc §)_ | model |

## Progress board

| Done | ID | Title | Status |
|------|----|-------|--------|
| [ ] | T-001 | _(short title)_ | todo |

## Execution order

T-001 → _(extend)_

## Tasks

### T-001: _(short title — concrete unit)_

- Status: todo
- Work items:
  - [ ] 1. _(concrete step)_
  - [ ] 2. _(concrete step)_
- AC: _(observable outcome — WHO + WHAT; not "works" / "per spec")_
- Verify: _(command or check that falsifies this AC)_
- Files/scope: _(concrete path or `…/File.ext`)_

#### Dev context

<!-- IPO Input for this card. Extract ONLY from DISCUSSION / BA / design / PLAN / repo.
Every tech fact bullet must end with `[Source: path#§ or heading]`.
If no guidance, write: `No specific guidance found.` -->

- **Reuse:** _(existing symbols, helpers, patterns — or `No specific guidance found.`)_
- **Constraints:** _(auth, limits, ordering — or none)_
- **Gaps:** _(missing source detail; mark inferred vs unknown)_

<!-- Duplicate ### T-00x as needed. Map ~1 inventory row → 1 card. -->
<!-- Put automated tests AFTER implement cards. -->
<!-- Keep Progress board in sync with card Status. -->
