---
name: sk-review-pr
description: "Review pull requests, merge requests, or branch diffs as a responsible code reviewer. Quality gate before merge. (Hard contract in this SKILL.md — MUST follow.)"
sk-kind: domain
sk-version: 0.1.0
sk-tags: [quality-gate,pr-review]
sk-roles: [critic]
sk-compatible: [claude, cursor, codex, gemini]
---

# Review PR

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Review a PR/MR or branch diff as a quality-responsible reviewer before merge.

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
| 01 | [step-01-init.md](./steps/step-01-init.md) | Init (base/head) |
| 02 | [step-02-diff.md](./steps/step-02-diff.md) | Get the diff |
| 03 | [step-03-findings.md](./steps/step-03-findings.md) | Findings + recommendation |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | Base ref, head ref (branch/PR/commit), PR description when available, changed files, test/CI results, codebase context. Head may differ from the currently checked-out branch. |
| Outputs | REVIEW_PR.md with sk-review mode, base/head, findings, testing gaps, residual risks, PR description coverage, merge recommendation. |
| Safety | Do NOT `checkout`, `stash`, reset, edit `.gitignore`, or otherwise change the current branch or working tree. Do NOT auto-fix the PR if the user only requested sk-review. Do NOT approve on behalf of the user. Do NOT create findings without evidence. Do NOT claim merge-safe if verification is missing. Do NOT ignore security/data risks. Create sk-review worktrees outside the repository, or use an existing ignored location. Never force-remove a dirty worktree. |

### Required artifacts

#### `REVIEW_PR.md`
- Required: yes
- **executive_summary** (required, array): Maximum five bullets with merge recommendation, top findings/risks, verification status, and next action.
- **developer_overview** (required, object): Merge recommendation, finding counts, verification status, next action.
- **charts** (optional, array): Mermaid finding/coverage chart when useful; otherwise N/A.
- **sk-review_mode** (required, string): remote-diff / worktree / current-branch.
- **base** (required, string): Base branch or commit (e.g. `origin/develop`).
- **head** (required, string): Head branch or commit being reviewed (e.g. `origin/A`).
- **pr_description_accuracy** (required, string): Does the diff match the description? yes/partial/no.
- **changed_areas** (required, array): Area, files, risk level, notes.
- **findings** (optional, array): Finding ID, severity, category, location, evidence, impact, recommendation, confidence.
- **verification_reviewed** (required, array): Check, result (pass/fail/skipped/missing), evidence, concern.
- **testing_gaps** (optional, array): Gap, risk, suggested follow-up.
- **residual_risks** (optional, array): Risk, impact, acceptance/mitigation.
- **merge_recommendation** (required, string): Approve / Approve with comments / Request changes / Needs more info / Needs more verification / Blocked. A merge-ready handoff routes to `sk-verify-pro` when the claim still needs final evidence.

### Reference

## Workflow

Review a pull request without disturbing the current branch or uncommitted work.

1. **Resolve base and head** — identify the pull request target and proposed change set; ask when either ref is ambiguous.
2. **Choose review mode** — use a read-only remote diff by default; use an isolated worktree only when full source or runtime evidence is genuinely required; use the current branch only when it is already the reviewed head and clean.
3. **Inspect the change set** — compare the merge-base range, changed files, tests, documentation, and stated scope. Record the review mode and refs in `REVIEW_PR.md`.
4. **Assess evidence** — distinguish CI/PR evidence from locally observed evidence; mark unavailable checks as skipped or missing rather than assuming success.
5. **Write and clean up** — produce findings with severity, location, evidence, impact, and recommendation; leave the current branch, worktree, and uncommitted changes unchanged.

## Quality Standards

- [ ] Review mode (remote-diff / worktree / current-branch) is recorded with base and head.
- [ ] Base is the PR target ref, not assumed from the current branch.
- [ ] Current branch and uncommitted work are untouched; any worktree is outside the repo (or already ignored) and safely removed.
- [ ] PR description is checked against actual diff (coverage column).
- [ ] Each finding has severity, file/location, evidence, and recommendation.
- [ ] Finding severity is one of: Critical / High / Medium / Low / Info.
- [ ] Merge recommendation is one of the defined taxonomy.
- [ ] Security/auth/permission is reviewed if changes touch those areas.
- [ ] Testing gaps are documented even when no blocker findings exist.
      `REVIEW_PR.md` (or `a clean working tree`).

## WRONG vs CORRECT

```markdown
// WRONG — no severity, no location
LGTM but there's a minor issue with the naming.

// CORRECT — structured finding
Finding PR-001: Medium — Export button text is misleading for unauthorized users.
Location: `src/features/export/export-button.tsx`, line 15.
Evidence: Button reads "Export All" but the endpoint rejects the request for unauthorized users.
Impact: UX confusion — users see an enabled button that will fail.
Recommendation: Disable the button text to "Export (not available)" for unauthorized roles.
Confidence: High.
```

```markdown
// WRONG — ignoring missing tests
No tests changed, but that's fine.

// CORRECT — calling out testing gaps
Testing gap: No new tests for the export permission check.
Risk: Regression may not be caught.
Follow-up: Add a negative API permission test.
```

## Edge Cases

| Situation | Handling |
|---|---|
| PR has no description | Document as an issue. PR description should explain what and why. |
| Diff is very large (>20 files) | Group by area. Note the size risk. Flag if changes are too broad. |
| Lockfile changes without manifest changes | Flag as potential unintended dependency change. |
| Binary files in the diff | Note they cannot be code-reviewed. Flag if large or unexpected. |
| CI evidence is missing | Note as testing gap. If changes are high-risk, recommend Needs more verification. |
| Head is a different branch while current branch has WIP | Use `remote-diff`, or a detached external worktree. Never checkout/stash/edit `.gitignore`. |
| Runtime verification needed but sandbox blocks worktree | Fall back to `remote-diff`, mark runtime checks `skipped`, and say so. |

## Limitations

- Does NOT auto-fix the PR.
- Does NOT replace deep security audit.
- Does NOT guarantee finding all bugs if evidence is insufficient.

## Output

Produce a reusable review pr artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.
