---
name: done
description: Close a task after execution/review with DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, and optional RELEASE_NOTE.md.
---

# Done

## Purpose

Close a task with clear, honest, reviewable artifacts.

This skill focuses on:

- Summarize what was actually done against the real goal.
- Link changes to plan/execution/review if available.
- Record real verification evidence that was actually run.
- Record skipped checks, failed checks, or blockers.
- Record residual risks and follow-ups.
- Create `DONE.md`.
- Create a concise `PR_MESSAGE.md`.
- Create `PR_DESCRIPTION.md` following repo template if available.
- Create a short release note if the user or workflow requires it.
- Prepare handoff to reviewer, QA, user, or next agent.

The goal: help the reader quickly understand what was done, how it was verified, what risks remain, and whether it is ready for PR/done.

## When to Use

Use this skill when:

- After execution and review.
- Task has met acceptance criteria.
- Task has blockers but needs a clear handoff.
- User requests a summary.
- User requests PR/MR preparation.
- `DONE.md` is needed.
- `PR_MESSAGE.md` is needed.
- `PR_DESCRIPTION.md` is needed.
- A short release note is needed.
- A task needs to be closed or a final report produced.
- A summary of changed files, verification, risks, and follow-ups is needed.
- Handoff to reviewer/QA/user is needed.

## When NOT to Use

Do NOT use this skill when:

- No execution has happened and no real output exists.
- No review has been done for high-risk or significant changes.
- Verification is still missing and has not been documented.
- Scope is still changing.
- Review has blockers that need fixing before done.
- User is still requesting implementation/fixes; use `execution`.
- User is requesting review; use `review`.
- User is requesting planning or breakdown; use `planning`.
- User is requesting investigation or root cause; use `investigate`.

## XML Contract

```xml
<Contract>
  <Inputs>PLAN.md, EXECUTION.md, REVIEW.md, diff/file changes, verification evidence, skipped checks, blockers, risks, follow-ups, PR/MR template if available.</Inputs>
  <Outputs>DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, optional RELEASE_NOTE.md, or done summary in response.</Outputs>
  <Artifacts>DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, optional RELEASE_NOTE.md in session path if applicable; otherwise, artifact in response.</Artifacts>
  <Safety>Do NOT overclaim verification. Do NOT hide skipped/failed checks. Do NOT mark complete if blockers remain. Do NOT auto-fix code. Do NOT describe changes that were not made. Do NOT put secrets/diffs/sensitive output into final artifacts.</Safety>
</Contract>
```

## Final Status Taxonomy

| Status | Meaning | Can Mark Done? |
|---|---|---|
| Done | Scope complete, verification appropriate, no blockers. | Yes |
| Done with Risks | Scope complete but residual risks/skipped checks are documented. | Yes, if risks are accepted |
| Needs Fix | Review or verification found issues to fix. | No |
| Needs More Verification | Changes look complete but evidence is insufficient. | No or conditional |
| Blocked | External blocker prevents completion. | No |
| Partial | Only part of scope is complete. | No unless partial delivery is accepted |

## Workflow

1. Determine if the task has enough input for done.
2. Choose Lite Mode or Full Mode.
3. Read `PLAN.md` if available.
4. Read `EXECUTION.md` if available.
5. Read `REVIEW.md` if available.
6. Identify actual changes from diff/file changed if available.
7. Look for PR/MR template in the repo if PR artifacts are needed.
8. Determine final status.
9. Summarize by goal/outcome, not by mechanically listing files.
10. Summarize what changed by logical groups.
11. Record verification that was actually run.
12. Record skipped checks, failed checks, or blockers.
13. Record review findings and resolution if any.
14. Record residual risks and follow-ups.
15. Create `DONE.md`.
16. Create `PR_MESSAGE.md` per convention.
17. Create `PR_DESCRIPTION.md` per repo template or fallback.
18. Create `RELEASE_NOTE.md` if needed.
19. Provide clear handoff: ready for PR, ready for QA, needs fix, blocked, or needs verification.

## Template Lookup

When a PR/MR description is needed, check for templates in order:
1. `.github/PULL_REQUEST_TEMPLATE.md`
2. `.github/pull_request_template.md`
3. `.github/PULL_REQUEST_TEMPLATE/*`
4. `.gitlab/merge_request_templates/*`
5. `.gitea/pull_request_template.md`
6. `.forgejo/pull_request_template.md`
7. Built-in repo template if configured.
8. Fallback template from this skill.

## PR Message Guidelines

Use Conventional Commits format unless the repo has its own convention:
```
<type>(<scope>): <summary>
```

| Type | Use When |
|---|---|
| feat | New user-facing capability |
| fix | Bug fix |
| docs | Documentation-only change |
| refactor | Code restructuring without behavior change |
| test | Test-only change |
| chore | Tooling, config, maintenance |
| perf | Performance improvement |
| ci | CI/CD change |
| build | Build system/dependency change |

Rules: one line, imperative or outcome-focused, no period at the end, do not mention files unless necessary, do not overstate scope.

## Limitations

- This skill does NOT modify code.
- This skill does NOT replace execution.
- This skill does NOT replace review.
- This skill does NOT turn unverified tasks into done.
- This skill does NOT guarantee PR readiness if input is missing.
- If review found blockers, return to `execution` before done.
- If scope changed significantly, return to `planning` or `review`.

<Contract>
  <Inputs>PLAN.md, EXECUTION.md, REVIEW.md, diff/file changes, verification evidence, skipped checks, blockers, risks, PR/MR template.</Inputs>
  <Outputs>DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, optional RELEASE_NOTE.md.</Outputs>
  <Artifacts>DONE.md, PR_MESSAGE.md, PR_DESCRIPTION.md, optional RELEASE_NOTE.md in session path.</Artifacts>
  <Safety>Do NOT overclaim verification. Do NOT hide skipped/failed checks. Do NOT mark complete if blockers remain. Do NOT put secrets into artifacts.</Safety>
</Contract>
