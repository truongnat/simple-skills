---
name: execution
description: Execute a plan or agreed scope: modify files, run verification, record EXECUTION.md, handle failures, and handoff to review.
---

# Execution

## Purpose

Execute a locked plan in a controlled, safe, and verifiable way.

This skill focuses on:

- Read and follow `PLAN.md` strictly.
- Execute each small task within scope.
- Modify workspace files with control.
- Do NOT break changes outside scope or belonging to others.
- Run appropriate verification after each step or phase.
- Record changed files, commands run, results, failures, and blockers.
- Update `EXECUTION.md` so a reviewer can understand exactly what was done.
- Prepare handoff to `review`, QA, or user verification.

The goal: complete the planned task with minimal, reviewable, verifiable, and rollback-able changes.

## When to Use

Use this skill when:

- `PLAN.md` exists.
- Scope is clear enough to execute safely.
- User requests implementation, file changes, test runs, or task completion.
- Need to create, modify, or delete workspace files.
- Need to run verification commands: lint, typecheck, test, build, or manual checks.
- Need to update artifacts after execution.
- Need to record `EXECUTION.md`.
- Need to handle each task in the implementation plan.
- Need to collect verification evidence before review.

## When NOT to Use

Do NOT use this skill when:

- Goals are unclear; use `brainstorming`.
- Business requirements are unclear; use `business-analysis`.
- No plan exists for a complex or high-risk task; use `planning`.
- Investigating root cause without knowing what to fix; use `investigate`.
- Only a review is needed after implementation; use `review`.
- A blocker from planning is unresolved.
- User has not approved execution for destructive, high-risk, or irreversible tasks.
- Deep external source research is needed first; use `research`.

## XML Contract

```xml
<Contract>
  <Inputs>PLAN.md, locked scope, repo context, affected files, constraints, verification commands, session path if available.</Inputs>
  <Outputs>Workspace changes within scope, EXECUTION.md or execution summary, files changed, commands run, verification evidence, issues/blockers, deviations, handoff to review.</Outputs>
  <Artifacts>EXECUTION.md in session path if applicable; otherwise, execution summary in response.</Artifacts>
  <Safety>Do NOT modify outside scope. Do NOT put secrets in files/logs. Do NOT delete sensitive files/config/migration/data without a plan or confirmation. Do NOT revert changes not belonging to you without permission. Do NOT claim completion without verification or documenting skipped checks.</Safety>
</Contract>
```

## Depth Modes

### Lite Mode

Use when: task is small, scope is very clear, few or no dependencies, no need to save `EXECUTION.md`, no high-risk/destructive changes, verification is simple.

### Full Mode

Use when: `PLAN.md` exists, task has multiple steps, many file changes, migration/config/infra/auth/permission/security/public API, need to save `EXECUTION.md`, need handoff to review or QA.

## Safety Rules

**Scope Safety**: Only modify what is in the plan/scope. If a change outside scope is needed to unblock, document it as a `Deviation` with reason. Do NOT expand features beyond the request.

**Workspace Safety**: Check working tree/diff before modifying if possible. Do NOT revert or overwrite changes not belonging to you. Do NOT delete files without knowing ownership and rollback. Do NOT format the entire repo for a small change.

**Secret Safety**: Do NOT hardcode secrets, credentials, tokens, API keys, private keys, or passwords. Do NOT print secrets into `EXECUTION.md`. If a secret is found in repo/log/output, stop and report the risk.

**Data/Migration Safety**: Do NOT run destructive migration without a plan, backup, or confirmation. Do NOT modify seed/production data without explicit permission. Do NOT change schema without a rollback/downgrade note.

**Dependency Safety**: Do NOT upgrade major dependencies outside scope. Do NOT modify lockfiles unnecessarily. If lockfile changes due to install/test, document it. Do NOT add new packages if an existing dependency can be used.

## Workflow

1. Determine if the task is ready for execution.
2. Choose Lite Mode or Full Mode.
3. Read `PLAN.md` if available.
4. Read context/session artifacts if needed.
5. Confirm the next task and its dependencies are satisfied.
6. Identify planned files/scope to modify.
7. Check safety before creating, modifying, or deleting files.
8. Check working tree/diff if possible.
9. Make small, in-scope changes.
10. Record changed files and rationale.
11. Run format/lint/typecheck/test/build/manual checks as appropriate.
12. Record commands, results, and evidence.
13. If a command fails, classify the failure type.
14. If failure is from your change, fix within scope and re-verify.
15. If failure is pre-existing or outside scope, document it clearly.
16. If the plan needs to change, stop and recommend returning to `planning`.
17. Update `EXECUTION.md` if Full Mode/session applicable.
18. Repeat until the task is complete or blocked.
19. Compile final execution summary.
20. Handoff to `review`, QA, or user verification.

## Failure Handling

Do NOT silently ignore verification failures.

Classify failures as: Introduced (fix within scope and re-run), Pre-existing (document evidence, do NOT claim as your issue), Environment (missing env/dependency/service/permission, document blocker), Flaky (re-run if reasonable, document both results), Out-of-Scope (document, do NOT expand scope without permission), Plan Failure (plan is wrong or missing steps, stop and return to planning).

## Verification Policy

- Do NOT claim "done", "fixed", "complete" without verification.
- If verification is not possible, document the reason clearly.
- If a command does not exist, document "command unknown" and how to find it.
- If only manual verification is possible, document the manual steps.
- If tests fail due to unrelated/pre-existing issues, document evidence.
- If a check is skipped due to time/tool/env, document the skipped check and risk.
- Prefer verification closest to the change: unit tests for logic, component/manual/e2e for UI, integration/API tests for API, typecheck for types, build for build behavior, format/lint for formatting, dry-run for config/infra.

## Limitations

- This skill does NOT do independent review; use `review` after execution.
- This skill does NOT replace planning for complex tasks.
- This skill does NOT replace investigate when root cause is unknown.
- This skill does NOT decide for stakeholders when blockers are business-related.
- This skill does NOT guarantee verification passes if the environment is missing dependencies/env/services.
- If the plan is wrong or scope changes significantly, stop and return to `planning`.

<Contract>
  <Inputs>PLAN.md, locked scope, repo context, affected files, constraints, verification commands.</Inputs>
  <Outputs>Workspace changes within scope, EXECUTION.md, files changed, commands run, verification evidence, blockers, deviations.</Outputs>
  <Artifacts>EXECUTION.md in session path.</Artifacts>
  <Safety>Do NOT modify outside scope. Do NOT put secrets in files/logs. Do NOT delete sensitive files without plan or confirmation.</Safety>
</Contract>
