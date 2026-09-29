---
name: sk-investigate
description: "Investigate codebase, bugs, system behavior, or technical questions before implementing. Root-cause analysis, reproduction, impact mapping, and evidence-based recommendations. (Hard contract in this SKILL.md — MUST follow.)"
sk-kind: domain
sk-version: 0.1.0
sk-tags: [investigation,debugging]
sk-roles: [researcher]
sk-compatible: [claude, cursor, codex, gemini]
---

# Investigate

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Find technical truth before deciding to fix, plan, or implement.

When the question involves **sk-docs/specs** (設計書, wiki, README-as-spec, “expected
per document”): run **Doc reality check** — sk-docs ↔ code/runtime — and **ask**
before treating either side as the sole root cause.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately after this Contract, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in INVESTIGATE.md with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final report, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | the detailed instructions in this skill | Session + seeded INVESTIGATE.md + Question |
| 02 | the detailed instructions in this skill | Evidence, reproduction, Doc reality check |
| 03 | the detailed instructions in this skill | Hypotheses, root cause, recommendation |
| 04 | the detailed instructions in this skill | Quality gate + commit + handoff |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| preferred_role | `researcher` (routing hint for multi-CLI; fallback main). |
| Inputs | Problem description, expected/actual behavior, logs/errors/reproduction, screenshots or recordings, codebase context, environment details; **sk-docs/specs when cited or implied**. |
| Outputs | `INVESTIGATE.md` (prefer template) with question, status, evidence, reproduction, observed facts, hypotheses, code path, impact, root cause, recommendation, open questions; **Doc reality check** when sk-docs are in play (or N/A + reason). |

### Required artifacts

#### `INVESTIGATE.md`
- Required: yes
- Prefer seed: `templates/INVESTIGATE.template.md`
- **executive_summary** (required, array): Maximum five bullets with status, likely/confirmed cause, strongest evidence, impact, and next action (include top Doc mismatch if any).
- **developer_overview** (required, object): Investigation status, Doc reality blockers or n/a, strongest hypothesis, evidence gap, next action.
- **doc_reality_check** (required, object): Table of doc claims vs code/runtime with verdict and Blocking; or explicit N/A with reason when no sk-docs/specs are involved. Clarification checkpoint when Blocking=`Yes`.
- **charts** (optional, array): Mermaid cause/flow chart when useful; otherwise N/A.
- **question** (required, string): The investigation question.
- **status** (required, string): Root Cause Confirmed / Likely Root Cause / Hypotheses Identified / Needs More Evidence / Blocked.
- **context** (optional, string): Environment, version, related setup.
- **evidence** (required, array): Evidence ID, source, observation, supports hypothesis?, confidence.
- **reproduction** (optional, array): Step, action, expected, actual, result.
- **observed_facts** (required, array): Fact with source.
- **hypotheses** (optional, array): Hypothesis, supporting evidence, counter evidence, verification method, confidence.
- **code_path** (optional, array): Layer, file/component, role, observation.
- **root_cause** (optional, string): Confirmed or likely root cause.
- **impact** (required, array): Area affected, impact, confidence.
- **recommendation** (required, string): Fix recommendation / workaround / next investigation / sk-docs refresh.
- **open_questions** (optional, array): Question, owner, blocking status.
- **handoff** (required, string): Ready for sk-planning? Ready for sk-execution? Suggested next skill (`sk-docs`, `sk-detail-design`, `sk-execution`, …).

### Reference

## Doc reality check (when sk-docs/specs matter)

| Check | Rule |
|---|---|
| Trigger | User cites 設計書/wiki/spec, or “expected” comes from documents, or bug is “differs from design”. |
| Table | Claim \| Doc evidence \| Code/runtime evidence \| Verdict \| Blocking \| Ask? |
| Verdicts | `Match` / `Mismatch` / `Missing-in-docs` / `Missing-in-code` / `Stale` / `Unknown` |
| Stop | Blocking=`Yes` → Confirm-first; prefer `diagram`/`table`/`html` so the user sees sk-docs vs code/runtime (SSOT); ask which source wins or what to verify next; do not close as Confirmed on doc alone. |
| N/A | Pure runtime/infra with no doc claim → section N/A + one-line reason. |
| Fold | Record Accepted source of truth; update or queue the canonical store. |

## Quality Standards

- [ ] Status is one of the defined taxonomy values.
- [ ] Keywords filled (or none) so a new teammate can read evidence without guessing jargon.
- [ ] Observed facts have explicit sources.
- [ ] Inferences are separated from observed facts with confidence levels.
- [ ] Doc reality filled or N/A with reason; Blocking items asked.
- [ ] If root cause is claimed: evidence is sufficient to explain all observed symptoms.
- [ ] Recommendation distinguishes: fix / workaround / next investigation / sk-docs update.
- [ ] Reproduction steps include environment, preconditions, and both expected and actual results.
- [ ] When video evidence is supplied, keyframes and timestamps are cited; unsampled transitions and audio are documented as limitations.

- [ ] Confirm-first: on Blocking need, STOP immediately; classify Ask method (`confirm`/`choice`/`fact`/`table`/`diagram`/`html`); ask that way; finished artifact is not a quiz — residual Open questions non-blocking only (the skill instructions).

## WRONG vs CORRECT

```markdown
// WRONG — “design says X so code is wrong” with no code cite
Root cause: implementation ignores 画面設計書.

// CORRECT
Doc: FBD13001 §イベント F10 → search all tabs.
Code: Handler only refreshes active tab (path/…).
Verdict: Mismatch. Ask method=diagram (or table for fields): show sk-docs path vs
code path; ask: bug vs intentional? update doc or code?
```

```markdown
// WRONG — no source, no confidence
The bug is probably in the export service.

// CORRECT — evidence-based
Observation: `GET /api/export` returns 500 when user 11716 is in the result set.
Stack trace: `DecryptInitialPassword()` throws on line 42 of `encryption.ts`.
Hypothesis H-001: The encrypted value for this user was set by Keycloak directly (plaintext).
Evidence: Keycloak audit log shows password was reset via admin console for user 11716.
Confidence: Medium.
```

```markdown
// WRONG — claiming root cause without evidence
Root cause: caching issue.

// CORRECT — qualified root cause
Root cause: Likely the encrypted attribute is plaintext, causing decryption to fail.
Confidence: Medium.
Alternative hypothesis: The encryption key changed between runs (low probability, no evidence).
Next step: Inspect the database value for user 11716's password attribute safely.
```

## Edge Cases

| Situation | Handling |
|---|---|
| Cannot reproduce the issue | Status = Needs More Evidence / Not Reproduced. Document conditions tried. |
| Log is truncated or incomplete | Document as limitation. Do NOT over-claim from partial data. |
| Sensitive data in logs (PII, tokens) | Redact before quoting. Document as security risk if exposure is found. |
| Multiple root causes are possible | List as multiple hypotheses with confidence for each. Do NOT pick one arbitrarily. |
| Issue is environment-specific | Document environment differences. Recommend cross-env comparison. |
| Docs stale vs code | Doc reality `Stale`/`Mismatch`; ask refresh sk-docs vs fix code vs accept drift. |

## Limitations

- Does NOT guarantee a fix exists.
- Does NOT replace sk-planning or sk-execution.
- Does NOT replace deep security audit.
- Does NOT treat documentation as authoritative without code/runtime evidence.

## Output

Produce a reusable investigate artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.
