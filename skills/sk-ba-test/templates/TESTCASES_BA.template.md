# Test cases (BA)

> Seeded by `sk-ba-test` mode=`cases`. Headings English; prose = `the user-requested language`.
> Prefer aligning with `sk-tester` TESTCASES.md when both exist.

## Executive summary

- _(TODO)_

## Developer overview

| Field | Value |
|---|---|
| Mode | `cases` |
| Status | Draft / Ready / Blocked / Deferred |
| P0 coverage | _(TODO)_ |
| Next action | _(TODO)_ |

## Mode

`cases`

## Test scope

_(in / out / assumptions)_

## Test cases

### TC-001 — _(title)_ — P0 — Positive — maps AC-___

| Field | Value |
|---|---|
| Preconditions |  |
| Steps | 1. … |
| Test data | _(fake only)_ |
| Expected |  |
| Verification method | manual / automated / integration / human approval |
| Evidence location | `artifacts/<task-id>/...` or test report |
| Criteria mapping | AC-___ / invariant / plan checkpoint |
| Freshness | timestamp, commit, build, device or environment |
| Case result | pass / block / defer |
| Limitation or gap | _(none / describe explicitly)_ |
| Next owner | _(required for block/defer)_ |

### Verification packet handoff

Before handing cases to `sk-verify-pro`, include one packet per claim with:

| Packet field | Value |
|---|---|
| Claim | _(one precise completion or acceptance claim)_ |
| Criteria | _(acceptance criteria, invariant, review policy or checkpoint)_ |
| Evidence | _(fresh results and artifact links)_ |
| Coverage map | _(criterion → evidence; uncovered criteria explicit)_ |
| Limitations | _(stale, unavailable, manual or domain uncertainty)_ |
| Decision | `pass` / `block` / `defer` |
| Next owner | _(required unless `pass` is consumed by `sk-done`)_ |

### Verification status examples

| Case | Evidence state | Decision | Next owner |
|---|---|---|---|
| Complete acceptance mapping | Every AC maps to fresh test/review evidence; no material limitation | `pass` | `sk-done` or release owner consumes `VERIFY.md` |
| Missing acceptance evidence | One or more required ACs have no result, stale result, or unresolved blocker | `block` | `sk-tester` or implementation owner closes the gap |
| Human/domain decision pending | Automated evidence is complete but named approval or device/domain check is outstanding | `defer` | Named approver/test owner records the missing decision |

## Playwright hints (optional)

> Hints only — not a claim of a runnable suite.

| Case | URL / route | Key selectors (guess) | Assert |
|---|---|---|---|
| TC-001 |  |  |  |

## Open questions

| Question | Owner | Blocking |
|---|---|---|
|  |  | Yes/No |

## Handoff

`sk-tester` / sk-execution / engineering automation

Final claim-to-evidence decision: `sk-verify-pro` → `sk-done` or release owner.
