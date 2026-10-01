---
name: sk-sync
description: "Read-only sk-sync of task artifacts, codebase context, git state, dirty changes, dependency/config drift, plan mismatch, and blockers before sk-execution. (Hard contract in this SKILL.md — MUST follow.)"
sk-kind: domain
sk-version: 0.1.0
sk-tags: [context,readiness]
sk-roles: [researcher]
sk-compatible: [claude, cursor, codex, gemini]
---

# Sync

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Ensure the agent has the latest, reliable, and safe state before sk-execution.

This skill focuses on:

- Sync task artifacts: DISCUSSION.md, PLAN.md, TASKS.md, EXECUTION.md, REVIEW.md.
- Refresh codebase context at plan-relevant scope.
- Check workspace and git state.
- Detect drift between PLAN/TASKS and current codebase.
- Detect dirty changes, conflicts, or out-of-scope modifications.
- Check dependency/config when the plan requires it.
- Check for missing or renamed files, and outdated assumptions.
- Identify blockers before modifying code.
- Record facts, risks, drift, and next steps.
- Maintain read-only mode by default.

The goal: avoid executing against stale context, wrong plans, dirty workspaces, drifted dependencies, or outdated assumptions.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in ``artifacts/<task-id>/PROGRESS.md`` with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifact, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | [step-01-init.md](./steps/step-01-init.md) | Init (inputs) |
| 02 | [step-02-scan.md](./steps/step-02-scan.md) | Scan (workspace + git) |
| 03 | [step-03-readiness.md](./steps/step-03-readiness.md) | Readiness verdict |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| preferred_role | `researcher` (routing hint for multi-CLI; fallback main). |
| Inputs | Session path, PLAN.md, TASKS.md (including Progress board/Status/checkboxes when present), workspace state, git state, dependency/config metadata, known affected files, user constraints. |
| Outputs | Sync summary with observed facts (include TASKS resume point / in_progress|blocked IDs), inferred context, drift, dirty changes, risks, blockers, recommended next step;. |
| Safety | Read-only by default. Do NOT mutate TASKS progress during sk-sync. Prefer scope from PLAN/TASKS affected areas. Do NOT read secrets or sensitive files without a clear reason. Do NOT run destructive commands. Do NOT auto-resolve conflicts or unrelated dirty changes. Do NOT move to sk-execution when PLAN Ready=No, blockers open, PLAN.md/TASKS.md stale, or SYNC.md older than PLAN/TASKS. |

### Required artifacts

#### `EXECUTION.md`
- Required: no
- Append sk-sync summary if workflow requires it. Not required for Lite Mode.

#### `SYNC.md`
- Required: yes in Full Mode; optional in Lite Mode when the summary is appended to `EXECUTION.md`.
- **executive_summary** (required, array): Maximum five bullets with readiness, drift, blockers, and next action.
- **developer_overview** (required, object): Status, resume task IDs, blocker count, next action.
- **charts** (optional, array): Mermaid readiness/drift chart when useful; otherwise N/A.
- **scope** (required, string): What was synced (artifacts, workspace, git, dependencies).
- **observed_facts** (required, array): List of observed facts with source for each.
- **inferred_context** (optional, array): Inferences with basis and confidence level.
- **drift_detected** (optional, array): Drift items with type, impact, suggested action.
- **dirty_changes** (optional, array): Classified dirty changes with scope check (in-scope/out-of-scope/unknown).
- **risks_blockers** (required, array): Blockers with type, impact, next action.
- **recommendation** (required, string): Suggested next step.
- **implementation_readiness** (required, object): Verdict `PASS` | `CONCERNS` | `FAIL` plus one-line reason. Execution only after `PASS`, or `CONCERNS` with explicit user accept.

### Reference

## When to Use

Use this skill when:

- After `sk-planning` and before `sk-execution`.
- Session is old or context may be stale.
- User returns to a task after some time.
- Need to refresh context before modifying code.
- Need to check workspace state.
- Need to check git state.
- Need to check dirty changes or conflicts.
- Need to read existing task artifacts.
- Need to map codebase at plan-relevant scope.
- Need to verify the plan still matches the codebase.
- Need to check dependency/config at read-only level.
- Need to identify blockers before sk-execution.
- Need to avoid overwriting changes that are not yours.

## When NOT to Use

Do NOT use this skill when:

- Task is only sk-brainstorming.
- Task is only sk-planning and does not need deep repo reading.
- User explicitly says not to check repo/workspace.
- No workspace, repo, or artifact to sk-sync.
- User is only asking general knowledge.
- User requires a sk-review of diff after sk-execution; use `sk-review`.
- User requires immediate implementation of a small, clear-scope task with fresh context.
- User requires external source sk-research; use `sk-research`.
- User provides full context for a specific file change in the prompt.

## Sync Readiness Gate

Before moving to sk-execution, verify the checklist below, then set an explicit
**Implementation readiness** verdict (BMAD-inspired):

| Verdict | Meaning | Next |
| --- | --- | --- |
| `PASS` | Safe to execute | `sk-execution` |
| `CONCERNS` | Proceed only with documented risks the user accepts | Ask user, then maybe execute |
| `FAIL` | Must not execute | Return to sk-planning / sk-investigate / ask user |

Checklist:

- Session path or task context exists.
- PLAN.md and TASKS.md are present and aligned (both required before sk-execution).
- **Every TASK card has `#### Dev context`** with Source cites or explicit
  `No specific guidance found.` Missing Dev context → **FAIL** (return to sk-planning).
- **PLAN.md Handoff Ready = Yes** and PLAN Handoff blockers are empty/`none`. If Ready=No or open blockers exist → **FAIL**.
- If `SYNC.md` exists but is **older** than PLAN.md or TASKS.md (mtime or version/date) → treat prior SYNC as **stale**; rewrite SYNC.md this run.
- Code workspace exists and is readable — prefer paths from PLAN/TASKS affected areas.
- Repository context and source-control state are documented when relevant.
- No dirty changes outside scope.
- No conflict markers or merge/rebase state.
- Files referenced in TASKS.md still exist (or confidence unknown is documented).
- TASKS.md Progress board / Status / Work item checkboxes are readable; note resume point (first non-`sk-done` ID) and any `in_progress`/`blocked` cards as observed facts (do not mutate progress during sk-sync).
- Affected areas have not drifted significantly vs PLAN/TASKS.
- Dependency/config assumptions still hold if the plan depends on them.
- No sensitive files need special handling.
- Any blockers require returning to sk-planning or asking the user.

Map to verdict:

- Any hard blocker (Ready=No, missing Dev context, conflict markers, out-of-scope dirty unknown ownership, stale PLAN/TASKS mismatch) → **FAIL**.
- Soft risks only (minor drift with clear action, partial progress, inferred paths) → **CONCERNS** (list them).
- Otherwise → **PASS**.

If verdict is not `PASS` (unless user explicitly accepts `CONCERNS`): do NOT move
to sk-execution. Document blockers and recommend the next step.

**Full Mode:** write/update `SYNC.md` every sk-sync run after sk-planning changes — do not leave a pre-planning SYNC as the latest gate.

`SYNC.md` must include heading **Implementation readiness** with verdict
`PASS` | `CONCERNS` | `FAIL` and a one-line reason.

## Quality Standards

Sync output must pass these checks:

- [ ] **Implementation readiness** verdict is `PASS` / `CONCERNS` / `FAIL` with reason.
- [ ] Observed facts have clear sources (file path, command output, user statement).
- [ ] Inferred context is explicitly separated from observed facts.
- [ ] Confidence levels (High/Medium/Low) are stated for each inference.
- [ ] Drift items include type (File/API/Dependency/Config/Test/Scope/Data/Branch).
- [ ] Dirty changes are classified: in-scope, out-of-scope, unknown ownership.
- [ ] Blockers state why they block sk-execution and what the next action is.
- [ ] Recommendation matches the verdict (PASS→sk-execution; FAIL→not sk-execution).
- [ ] First-pass readable: concrete names (paths/APIs/IDs); no abstract filler.
- [ ] No leftover `_(TODO)_` or placeholder Mermaid in finished sections.
- [ ] Spec/sk-review findings state finding + evidence + verdict (not essays).

## WRONG vs CORRECT

```markdown
// WRONG — no source, no confidence, vague
Inferred: The task touches auth.

// CORRECT — has source, confidence, and basis
Inferred: The task touches auth login flow (confidence: High).
Basis: Both PLAN.md and dirty file `src/auth/login.ts` reference the same feature code `RAB07001`.
```

```markdown
// WRONG — single line, no classification
Drift: File was renamed.

// CORRECT — typed, with impact and action
Drift Type: File Drift
Impact: Plan references `src/old.ts` but file is now `src/new.ts`. Execution would fail at verification step.
Action: Update plan file paths or inspect new location before sk-execution.
```

## Edge Cases

| Situation | Handling |
|---|---|
| No git repo in workspace | Skip git checks, document "not a git repo" as observed fact. |
| .env file exists but not in plan scope | Do NOT read contents. Note existence as metadata only. |
| PLAN.md or TASKS.md missing | Block sk-execution. Return to sk-planning — both files are required (do not fold tasks into PLAN.md). |
| PLAN Handoff Ready=No or open blockers | **FAIL** readiness. Resolve blockers or return to sk-planning/ask user. |
| TASK card missing `#### Dev context` | **FAIL** readiness. Return to sk-planning step-03. |
| SYNC.md older than PLAN.md/TASKS.md | Stale sk-sync — rewrite SYNC.md this run before any PASS recommendation. |
| Soft drift with clear mitigation | **CONCERNS** — list risks; ask user before sk-execution. |
| TASKS.md stale vs PLAN task_index | Block sk-execution. Return to sk-planning to realign. |
| TASKS.md missing Progress board / Status / checkboxes | Do not block if cards are clear; recommend sk-execution add Progress board + checkboxes before/while running. Note as drift/risk. |
| Partial progress (`in_progress` / some `[x]`) | Ready may still be Yes; recommend resume at first non-`sk-done` ID. |
| Dirty changes with unknown ownership | Block sk-execution. Ask user to confirm ownership or commit/stash first. |
| Merge conflict markers detected | Block sk-execution. Recommend conflict resolution before proceeding. |
| Workspace directory does not exist | Block. Cannot proceed without a valid workspace. |
| User says "skip sk-sync, just do it" | Skip sk-sync, but note the risk of stale context in sk-execution artifact. |

## Workflow (detailed mechanics — order enforced by the step files)

1. Determine if sk-sync is needed.
2. Choose Lite Mode or Full Mode.
3. Confirm workspace and session path.
4. Read relevant task artifacts in order.
5. Check sensitive file boundaries before reading files.
6. Check git repo and working tree if applicable.
7. Check dirty changes, untracked files, conflict state, and **current branch vs
   the project branch settings.mode`**: for `checkout`, flag as a blocker if the tree is on the
   base branch (sk-execution must branch first); for `direct`, confirm the base
   branch is the intended target.
8. Check plan files/systems exist.
9. Map codebase at plan-relevant scope.
10. Check dependency/config/tooling if plan needs it.
11. Compare plan with actual state.
12. Document observed facts with sources.
13. Document inferred context separately from observed facts.
14. Document drift, risks, and blockers.
15. Set **Implementation readiness** (`PASS` / `CONCERNS` / `FAIL`) with reason.
16. Recommend next step matching the verdict.
17. Only move to sk-execution on `PASS`, or on `CONCERNS` after explicit user accept.

## Limitations

- This skill does NOT replace sk-execution.
- This skill does NOT replace sk-planning when PLAN.md or TASKS.md is stale.
- This skill does NOT replace sk-investigate when the root cause is unknown.
- This skill does NOT write tools or automation.
- This skill does NOT auto-handle conflicts or unrelated dirty changes.
- This skill does NOT guarantee detecting all drift if context is missing.
- This skill does NOT read secrets or sensitive data without a clear reason and user permission.

## References

- [Git Status Documentation](https://git-scm.com/sk-docs/git-status)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

## Output

Produce a reusable sync artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary


**`sk-sync`** owns workspace and artifact synchronization: read current repository state, reconcile task notes with files and branches, detect drift, and refresh context before execution or handoff.

It does **not** own requirements authoring, implementation, test execution, external research, or final review. Route planning to `sk-planning`, implementation to the domain owner, repository safety to `sk-git-operations-pro`, and verification to `sk-verify-pro`.

**Primary artifact:** a synchronization report naming inspected state, detected drift, preserved user changes, and the next safe action. **Handoff:** pass refreshed context and provenance to the next workflow owner; do not silently rewrite unrelated artifacts.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review for quality findings; sk-verify-pro for canonical claim-to-evidence decisions (sk-verification is a compatibility facade only).

## Wave 3 evidence pack

Read [`references/wave3-evidence-pack.md`](./references/wave3-evidence-pack.md) when the task requires the Wave 3 positive/negative fixture and evidence packet. The skill prepares bounded evidence; `sk-verify-pro` owns the final claim-to-evidence decision.
