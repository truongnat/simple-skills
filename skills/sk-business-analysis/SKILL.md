---
name: sk-business-analysis
description: >-
  Step workflow: seed BUSINESS_ANALYSIS template then frame+Spec quality →
  stories/rules/AC → self-check. Clarify requirements before design/sk-planning.
  Challenge feasibility, correctness, and missing feature capabilities.
  (Hard contract in this SKILL.md — MUST follow.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [requirements,acceptance-criteria]
sk-roles: [reasoner]
sk-compatible: [claude, cursor, codex, gemini]
---

# Business Analysis

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Clarify business requirements before basic design, sk-planning, implementation, or testing via a **forced step sequence**:

1. Seed `BUSINESS_ANALYSIS.md` from template
2. Frame problem/stakeholders/scope + **Spec quality review**; **stop and ask** on blockers
3. User stories / business rules / acceptance criteria
4. Self-check

## Workflow architecture (mandatory)

- Read **one** step fully; finish it before the next.
- **NEVER** skip step-01 (template seed).
- **NEVER** write stories/AC before Spec quality review is complete.
- **NEVER** continue past step-02 while Feasibility/Correctness Fail/Unknown+blocking
  or Blocking=Yes capability gaps remain open.
- **NEVER** claim complete until step-04 passes (or Ready=No with blockers).
- Keep the **progress checklist** in the artifact updated every step.

| Path | Role |
|------|------|
| [templates/BUSINESS_ANALYSIS.template.md](./templates/BUSINESS_ANALYSIS.template.md) | Seed for task artifact |
| the detailed instructions in this skill | Copy template into the task artifact directory |
| the detailed instructions in this skill | Frame + Spec quality review |
| the detailed instructions in this skill | Stories, rules, AC |
| the detailed instructions in this skill | Verify + stop |

### Execution entry

**Start here:** Read and follow the detailed instructions in this skill immediately after this Contract.

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts or steps.

| Field | Requirement |
|-------|-------------|
| preferred_role | `reasoner` (routing hint for multi-CLI; fallback main). |
| Inputs | User request, business context, existing requirements, data samples (Excel, CSV, SQL, JSON, API response), screenshots or demo recordings, stakeholder feedback. |
| Outputs | Task artifact `BUSINESS_ANALYSIS.md` seeded from template and filled through the four local phases, including Spec quality review and progress checklist. |
| Safety | Do NOT treat assumptions as requirements. Do NOT accept specs as automatically correct or feasible. Do NOT decide for stakeholders. Do NOT write vague or untestable acceptance criteria. Do NOT omit capability gaps a feature of this type should normally have. Do NOT produce technical architecture — hand off to sk-basic-design. Do NOT skip Spec quality review. **Confirm-first:** STOP on Blocking Spec/Unknowns; classify Ask method; reuse prior answers; do not finish BA as an open-questions dump. If Path=`Quick`, **stop** and use `sk-quick-fix` (or upgrade Path). |

### Required artifacts

#### `BUSINESS_ANALYSIS.md`
- Required: yes.
- **step_ledger** (required, table): Steps 01–04 status; no later step complete while earlier is todo.
- **executive_summary** (required, array): Maximum five bullets with the problem, key rule/decision, top Spec quality finding, top risk, and next action.
- **developer_overview** (required, object): Status, Spec quality summary, open questions, next action.
- **charts** (optional, array): Mermaid process/actor flow when useful; otherwise N/A.
- **problem_statement** (required, string): One-sentence business problem.
- **stakeholders** (required, array): Actor, goal, pain point, authority.
- **scope** (required, object): In scope, out of scope, non-goals.
- **user_stories** (required, array): ID, actor, need, value.
- **business_rules** (required, array): BR ID, rule, source, confidence.
- **data_assumptions** (optional, array): Assumption, risk, confirmation owner.
- **acceptance_criteria** (required, array): AC ID, Given/When/Then, rule mapping.
- **spec_quality_review** (required, object): Feasibility, Correctness, Capability recommendations — challenge the request/specs before design.
- **open_questions** (required, array): Question, owner, blocking status.
- **handoff** (required, string): Recommended next skill and readiness.

### Reference

## Spec quality review (mandatory)

Do not only restate specs. Challenge them with three axes:

1. **Feasibility (tính khả thi)** — Can stakeholders, process, data, systems, and timeline actually support this?
2. **Correctness (tính đúng đắn)** — Are requirements consistent with current business/system reality, or are the specs (or the system) wrong?
3. **Capability recommendations (khả năng feature / gaps)** — What should a feature of this type normally include that the request omitted?
   Example: upload without max size, MIME allowlist, overwrite policy, progress, retry, audit, permission, or error messaging.

Write findings under `spec_quality_review` and promote Blocking=Yes gaps into `open_questions`.

## Forbidden outputs (reject / rewrite)

| Failure | Fix |
|---------|-----|
| No template seed / no progress checklist | Restart step-01 |
| progress checklist skipped / later step `complete` while earlier `todo`/`blocked` | Fix ledger; return to earliest incomplete step |
| Stories/AC before Spec quality complete | Return to step-02 |
| Specs restated without feasibility/correctness/capability challenge | Fill Spec quality review; ask blockers |
| Ready=Yes with open Blocking capability gaps | Set Ready=No; ask user |
| Vague AC (“works”, “per spec”) | Rewrite Given/When/Then |

## Quality Standards

- [ ] progress checklist sequential and complete (or blocked with questions).
- [ ] Problem statement is one sentence.
- [ ] Stakeholders/actors are listed with role and pain point.
- [ ] Business rules have IDs (BR-001, BR-002) for traceability.
- [ ] Acceptance criteria use Given/When/Then format.
- [ ] Assumptions are separated from confirmed requirements.
- [ ] Spec quality review covers Feasibility, Correctness, and Capability recommendations.
- [ ] Open questions have owners (if known) and blocking status; capability gaps are not silently dropped.
- [ ] Handoff to next skill is specified (usually sk-basic-design when technical work follows).
- [ ] When a demo recording is supplied, relevant sampled frames are cited as sources and interpretation gaps are kept as open questions.

- [ ] First-pass readable: concrete names (paths/APIs/IDs); no abstract filler.
- [ ] No leftover `_(TODO)_` or placeholder Mermaid in finished sections.
- [ ] Spec/review findings state finding + evidence + verdict (not essays).

- [ ] Confirm-first: on Blocking need, STOP immediately; classify Ask method (`confirm`/`choice`/`fact`/`table`/`diagram`/`html`); ask that way; finished artifact is not a quiz — residual Open questions non-blocking only (the skill instructions).

## WRONG vs CORRECT

```markdown
// WRONG — restates the request only
User wants an upload button. Proceed to design.

// CORRECT — challenges feasibility, correctness, and missing capabilities
Feasibility: Pass-with-gaps — storage API exists; async virus scan capacity unknown.
Correctness: Partial — current screen already has import; request conflicts with overwrite rule BR-002.
Capability gaps:
- CAP-001 max file size / MIME allowlist (Blocking=Yes)
- CAP-002 overwrite vs append policy (Blocking=Yes)
- CAP-003 progress + retry UX (Blocking=No)
Ask stakeholders before sk-basic-design.
```

```markdown
// WRONG — vague, untestable
The system should handle data well.

// CORRECT — specific, testable
BR-001: Admin users can create, update, deactivate, and export teacher accounts within their assigned school only.
AC-001: Given an admin user with school assignment X, when they open the teacher list, then only teachers in school X are shown.
```

```markdown
// WRONG — assumption presented as fact
Teacher ID is unique.

// CORRECT — assumption with caveat
ASM-001: We assume teacher ID is unique within a school year.
Risk if wrong: Import may merge wrong records.
Needs confirmation from: Product owner.
```

## Edge Cases

| Situation | Handling |
|---|---|
| Stakeholder feedback contradicts | Document both positions as open questions. Flag for resolution. |
| Requirement is too vague to write AC | Write best-effort AC. Mark as "needs clarification." |
| Data sample is inconsistent with description | Document the inconsistency. Recommend confirming which source is correct. |
| Business rules conflict with each other | Document the conflict. Flag to stakeholder for decision. |
| Specs conflict with existing system behavior | Record under Correctness; ask whether to change the system or fix the specs. |
| Specs omit common feature capabilities | List Capability recommendations; mark Blocking=Yes when implementation would invent policy. |

## Limitations

- Does NOT replace stakeholder decisions.
- Does NOT auto-implement.
- Does NOT auto-confirm business rules without a source.
- Does NOT produce technical architecture — hand off to sk-basic-design (then sk-detail-design) when technical work follows.
- Does NOT replace sk-planning.

## Output

Produce a reusable business analysis artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.
