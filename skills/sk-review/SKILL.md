---
name: sk-review
description: "Review changes after sk-execution: bugs, regression, missing tests, security/data risks, maintainability, and readiness before sk-done/PR. (Hard contract in this SKILL.md — MUST follow.)"
sk-kind: process
sk-version: 0.1.0
sk-tags: [quality-gate,code-review]
sk-roles: [critic]
sk-compatible: [claude, cursor, codex, gemini]
---

# Review

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Evaluate changes after sk-execution before marking sk-done, creating a PR, or handing off.

Compare the diff and `EXECUTION.md` against `PLAN.md` (DoD/scope) and
`TASKS.md` when present (per-task AC and intended files).

**Outcome-first:** Ready / Ready-with-risks requires evidence that maps to DoD
and AC (commands, responses, screenshots, test names) — not “files look clean.”

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
| 02 | [step-02-findings.md](./steps/step-02-findings.md) | Findings |
| 03 | [step-03-report.md](./steps/step-03-report.md) | Report + recommendation |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| preferred_role | `critic` (routing hint for multi-CLI; fallback main). |
| Inputs | Diff/file changes, PLAN.md, TASKS.md when present, EXECUTION.md, test/check results, verification evidence, scope/context. |
| Outputs | REVIEW.md with scope reviewed, findings, testing gaps, residual risks, recommendation, handoff. |

### Required artifacts

#### `REVIEW.md`
- Required: yes
- **executive_summary** (required, array): Maximum five bullets with recommendation, top findings/risks, verification status, and next action.
- **developer_overview** (required, object): Recommendation, finding counts by severity, verification gaps, next action.
- **charts** (optional, array): Mermaid finding-severity or coverage chart when useful; otherwise N/A.
- **scope_reviewed** (required, string): What changes were reviewed.
- **inputs** (required, array): What was read: PLAN.md, TASKS.md, EXECUTION.md, diff, test results.
- **findings** (optional, array): Finding ID, severity, category, location, evidence, impact, recommendation, confidence.
- **requirement_coverage** (required, array): Requirement/task, covered by change? evidence, notes.
- **verification_reviewed** (required, array): Check, result, evidence, concern.
- **testing_gaps** (optional, array): Gap, risk, suggested follow-up.
- **residual_risks** (optional, array): Risk, impact, acceptance/mitigation.
- **recommendation** (required, string): Ready / Ready with risks / Needs fix / Blocked / Needs more verification.
- **handoff** (required, string): Next action/skill, owner, and blocking status. A review-ready handoff normally routes to `sk-verify-pro` before `sk-done`.

### Reference

## Quality Standards

- [ ] Every finding has severity (Critical/High/Medium/Low/Info).
- [ ] Every finding has evidence (file path, line, or diff context).
- [ ] No findings → explicitly state "No findings found" + document residual risks.
- [ ] Security/data/migration risks checked if changes touch those areas.
      (CODE_COMMENTS.md / project policy defaults): public/exported symbols have doc comments;
      comment prose language matches `rules.code.comments.prose_language` (not
      `the user-requested language`); non-obvious/multi-stage logic has a numbered flow +
      `Step N:` markers;
      business rules/security noted; markers owned; **no stale comment
      contradicting the code** and no obvious-narration/commented-out noise.
- [ ] Recommendation uses one of: Ready / Ready with risks / Needs fix / Blocked / Needs more verification.
- [ ] When TASKS.md exists, check unfinished or unverified task IDs against EXECUTION evidence (Progress board Status / Done / Work item checkboxes must match claimed completion).

- [ ] First-pass readable: concrete names (paths/APIs/IDs); no abstract filler.
- [ ] No leftover `_(TODO)_` or placeholder Mermaid in finished sections.
- [ ] Spec/sk-review findings state finding + evidence + verdict (not essays).

## WRONG vs CORRECT

```markdown
// WRONG — vague, no evidence
Code could be cleaner.

// CORRECT — specific, evidence-based
Finding H-001: Missing server-side permission check.
Location: `src/export/export-handler.ts`, no guard before processing request.
Evidence: UI hides export button, but API endpoint still accepts direct requests.
Impact: Unauthorized users can export data by calling the endpoint directly.
Recommendation: Add server-side permission check + negative API test.
Severity: High
```

```markdown
// WRONG — claiming safe without checking
No security issues found.

// CORRECT — qualified statement
Security check:
- Auth: no changes touched auth middleware.
- Permission: server-side guard not added (Finding H-001).
- Input: existing validation still in place.
- Secrets: no new secrets introduced.
Residual risk: Missing permission check needs to be addressed before merge.
```

## Edge Cases

| Situation | Handling |
|---|---|
| No sk-review findings | State "No findings found" explicitly. Document residual risks. |
| User only asks "is this ready?" | Answer with recommendation status — if blocked, explain why. |
| Review input is incomplete (no diff) | Document limitation in scope. Do NOT claim full sk-review. |
| Pre-existing issue found during sk-review | Document as info finding. Note it's pre-existing, not introduced. |
| Security sk-review without enough context | Document as testing gap. Do NOT claim security is safe. |

## Limitations

- Does NOT auto-fix code.
- Does NOT replace full QA or deep security audit.
- If fixes are needed, return to sk-planning (update PLAN/TASKS) or sk-execution.

## Output

Produce a reusable review artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.
