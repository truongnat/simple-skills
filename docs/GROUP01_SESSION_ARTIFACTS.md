# Group 01 Session Artifact Contract

This is the shared contract for the 33 skills in the development-process and requirements group.

## Canonical location

Each task uses:

```text
artifacts/<task-id>/
```

The task ID must be stable across resume, review, verification, and closure.

## Artifact ownership

| Artifact | Owner | Required when |
|---|---|---|
| `CONTEXT.md` | `sk-init` / `sk-sync` | repository facts or readiness are needed |
| `BUSINESS_ANALYSIS.md`, `PRD.md`, design files | discovery/design skill | that path is selected |
| `PLAN.md` | `sk-planning` | planned work |
| `TASKS.md` | `sk-planning`, then execution owner | planned work |
| `PROGRESS.md` | active workflow | any multi-step workflow |
| `state.json`, `checkpoint.log` | `sk-executing-pro` | canonical execution |
| `EXECUTION.md` | `sk-executing-pro` or legacy `sk-execution` | implementation work |
| `REVIEW.md` | `sk-review` | post-implementation review |
| `REVIEW_PR.md` | `sk-review-pr` | PR/MR/branch review |
| `VERIFY.md` | `sk-verify-pro` | full claim-to-evidence verification |
| `DONE.md` | `sk-done` | task closure |

A lightweight skill may return inline facts only, but it must explicitly report `artifact_mode: none` and must not imply that an artifact was written.

## State vocabulary

Use these values consistently:

- `todo` — not started
- `in_progress` — actively being worked
- `blocked` — cannot continue without a decision, dependency, or evidence
- `skipped` — intentionally not run, with reason and risk
- `complete` — acceptance criteria and required evidence passed
- `partial` — some scope complete; remaining scope is explicit

`sk-done` is a skill name, not a task status. Legacy `sk-execution` may read `sk-done` in existing task files, but new artifacts must use `complete`.

## Handoff minimum

Every handoff must state:

1. current status;
2. artifacts written and their paths;
3. evidence already collected;
4. blockers, skipped checks, and residual risk;
5. exact next skill and owner.

## Canonical lifecycle

```text
sk-init/sk-sync
  → discovery or BA/design path
  → sk-planning
  → sk-executing-pro
  → sk-review or sk-review-pr
  → sk-verify-pro
  → sk-done
```

Compatibility facades:

- `sk-execution` continues legacy `TASKS.md`/`EXECUTION.md` sessions only.
- `sk-verification` provides a lightweight summary only; full verification routes to `sk-verify-pro`.
