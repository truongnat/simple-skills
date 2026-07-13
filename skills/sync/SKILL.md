---
name: sync
description: Read-only sync of session artifacts, codebase context, git state, dirty changes, dependency/config drift, plan mismatch, and blockers before execution.
---

# Sync

## Purpose

Ensure the agent has the latest, reliable, and safe state before execution.

This skill focuses on:

- Sync session artifacts: `DISCUSSION.md`, `PLAN.md`, `EXECUTION.md`, `REVIEW.md`.
- Refresh codebase context at plan-relevant scope.
- Check workspace and git state.
- Detect drift between plan and current codebase.
- Detect dirty changes, conflicts, or out-of-scope modifications.
- Check dependency/config when the plan requires it.
- Check for missing or renamed files, and outdated assumptions.
- Identify blockers before modifying code.
- Record facts, risks, drift, and next steps.
- Maintain read-only mode by default.

The goal: avoid executing against stale context, wrong plans, dirty workspaces, drifted dependencies, or outdated assumptions.

## When to Use

Use this skill when:

- After `planning` and before `execution`.
- Session is old or context may be stale.
- User returns to a task after some time.
- Need to refresh context before modifying code.
- Need to check workspace state.
- Need to check git state.
- Need to check dirty changes or conflicts.
- Need to read existing session artifacts.
- Need to map codebase at plan-relevant scope.
- Need to verify the plan still matches the codebase.
- Need to check dependency/config at read-only level.
- Need to identify blockers before execution.
- Need to avoid overwriting changes that are not yours.

## When NOT to Use

Do NOT use this skill when:

- Task is only brainstorming.
- Task is only planning and does not need deep repo reading.
- User explicitly says not to check repo/workspace.
- No workspace, repo, or artifact to sync.
- User is only asking general knowledge.
- User requires a review of diff after execution; use `review`.
- User requires immediate implementation of a small, clear-scope task with fresh context.
- User requires external source research; use `research`.
- User provides full context for a specific file change in the prompt.

## Sync Readiness Gate

Before moving to execution, verify:

- Session path or task context exists.
- `PLAN.md` or scope is clear.
- Workspace exists and is readable.
- Git repo is initialized if needed.
- No dirty changes outside scope.
- No conflict markers or merge/rebase state.
- Files in the plan still exist.
- Affected files have not changed significantly vs the plan.
- Dependency/config assumptions still hold if the plan depends on them.
- No sensitive files need special handling.
- Any blockers require returning to planning or asking the user.

If readiness is not met: do NOT move to execution. Document blockers and recommend the next step.

## Inputs

- Session path.
- `DISCUSSION.md`.
- `PLAN.md`.
- `EXECUTION.md` if the task is resuming.
- `REVIEW.md` if returning after review.
- Current workspace.
- User constraints.
- Known affected files.
- Known verification commands.
- Git state if available.
- Dependency files: `package.json`, lockfile, `pyproject.toml`, `go.mod`, etc.
- Config metadata if relevant and safe to read.
- Previous assumptions or open questions.

## Outputs

- Sync summary.
- Observed facts.
- Inferred context.
- Drift detected.
- Dirty changes / conflict state.
- Dependency/config notes.
- Sensitive file handling notes.
- Risks.
- Blockers.
- Recommendation / next step.
- Optional short update to `EXECUTION.md` if the workflow requires it.

## XML Contract

```xml
<Contract>
  <Inputs>Session path, PLAN.md, workspace state, git state, dependency/config metadata, known affected files, user constraints.</Inputs>
  <Outputs>Sync summary, observed facts, inferred context, drift, dirty changes, risks, blockers, recommended next step.</Outputs>
  <Artifacts>Short update in EXECUTION.md if workflow requires; no separate file required.</Artifacts>
  <Safety>Read-only by default. Do NOT mutate workspace. Do NOT read secrets or sensitive files without a clear reason. Do NOT run destructive commands. Do NOT auto-resolve conflicts or unrelated dirty changes. Do NOT move to execution when plan is stale or blockers are unhandled.</Safety>
</Contract>
```

## Depth Modes

### Lite Mode

Use when: task is small, session is fresh, only a quick workspace/git/artifact check is needed, no deep codebase mapping needed, few affected files.

### Full Mode

Use when: session is old or context may be stale, many affected files, dirty changes, dependency/config drift, complex plan, migration/config/auth/security/data risk, thorough preparation is needed.

## Read-only Policy

Sync is read-only by default.

Allowed: list relevant files/paths, read session artifacts, read source files relevant to the plan, read metadata files, read git status/diff summary, read dependency manifest at needed scope, read non-sensitive config at needed scope, run read-only commands (status/list/grep/test discovery) if safe.

NOT allowed by default: modify files, format files, install/update dependencies, generate files, delete files, rename files, run migrations, run seeds, change env/config, resolve merge conflicts, checkout/reset/rebase/merge branches, modify lockfiles. If an action may mutate workspace, move to `execution` or ask the user.

## Sensitive File Policy

Do NOT read contents of: `.env`, `.env.*`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, private keys, certificates, credentials, tokens, cloud credential files, SSH keys, database dumps, backup files, production config with secrets, files containing PII or customer data.

Safe to read: file existence, file name, file size, modified time, tracked/ignored status. Do NOT copy sensitive content into artifacts or responses.

## Git State Checks

Check at needed scope: current branch, working tree dirty/clean, staged changes, untracked files, merge/rebase/cherry-pick state, conflict markers, diff summary, changes outside plan scope.

Read-only commands: `git status --short`, `git branch --show-current`, `git diff --name-only`, `git diff --stat`, `git diff --cached --name-only`.

Do NOT auto-run: `git reset`, `git checkout`, `git clean`, `git merge`, `git rebase`, `git stash`, `git add`, `git commit`.

## Dirty Changes Policy

If dirty changes exist:
1. Classify: in-scope changes, out-of-scope changes, unknown ownership, generated/lockfile changes, conflict-related changes.
2. If out-of-scope or unknown ownership: do NOT overwrite. Do NOT auto-revert. Document blocker/risk. Ask user or recommend resolution before execution.
3. If in-scope and belongs to current task: document as observed fact. May continue if no conflict.
4. If merge conflict: do NOT resolve during sync. Document blocker. Recommend conflict resolution.

## Drift Detection

Drift types: File Drift (plan file renamed/deleted/moved), API Drift (function/interface changed), Dependency Drift (package/runtime version different), Config Drift (config path/key different), Test Drift (test command missing/renamed), Artifact Drift (PLAN.md older than changes), Scope Drift (codebase shows wider/different scope), Data Drift (schema/sample data different), Branch Drift (on wrong branch).

Serious drift must block execution until resolved.

## Workflow

1. Determine if sync is needed.
2. Choose Lite Mode or Full Mode.
3. Confirm workspace and session path.
4. Read relevant session artifacts in order.
5. Check sensitive file boundaries before reading files.
6. Check git repo and working tree if applicable.
7. Check dirty changes, untracked files, conflict state.
8. Check plan files/systems exist.
9. Map codebase at plan-relevant scope.
10. Check dependency/config/tooling if plan needs it.
11. Compare plan with actual state.
12. Document observed facts.
13. Document inferred context separately from observed facts.
14. Document drift, risks, and blockers.
15. Recommend next step.
16. Only move to execution if state is reliable enough.

## Limitations

- This skill does NOT replace execution.
- This skill does NOT replace planning when the plan is stale.
- This skill does NOT replace investigate when the root cause is unknown.
- This skill does NOT write tools or automation.
- This skill does NOT auto-handle conflicts or unrelated dirty changes.
- This skill does NOT guarantee detecting all drift if context is missing.
- This skill does NOT read secrets or sensitive data without a clear reason and user permission.

<Contract>
  <Inputs>Session path, PLAN.md, workspace state, git state, dependency/config metadata, known affected files, user constraints.</Inputs>
  <Outputs>Sync summary: observed facts, inferred context, drift, dirty changes, risks, blockers, recommended next step.</Outputs>
  <Artifacts>Short update in EXECUTION.md if workflow requires.</Artifacts>
  <Safety>Read-only by default. Do NOT mutate workspace. Do NOT read secrets. Do NOT run destructive commands. Do NOT auto-resolve conflicts.</Safety>
</Contract>
