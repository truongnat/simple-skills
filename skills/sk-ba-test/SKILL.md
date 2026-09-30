---
name: sk-ba-test
description: >-
  BA testing prep: overview checklist (/test-checklist) then executable cases
  (/test-cases). Complements sk-tester; optional playwright-hint mode. Writes
  TEST_CHECKLIST.md or expands into TESTCASES.md. (Hard contract.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [test-design,requirements]
sk-roles: [critic]
sk-compatible: [claude, cursor, codex, gemini]
---

# BA test

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Prepare BA-facing test coverage **before** deep `sk-tester` runs:

| Mode | Alias | Output |
| --- | --- | --- |
| `checklist` | `/test-checklist` | `TEST_CHECKLIST.md` |
| `cases` | `/test-cases` | `TESTCASES.md` (same shape as `sk-tester` when possible) |
| `playwright-hint` | `/playwright-gen` | section in `TESTCASES.md` — **hints only**, not a runnable suite claim |

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (the skill-local `steps/` directory).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in ``artifacts/<task-id>/PROGRESS.md`` with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifact, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | [step-01-init.md](./steps/step-01-init.md) | Init (mode + ledger) |
| 02 | [step-02-frame.md](./steps/step-02-frame.md) | Frame (inputs + scope) |
| 03 | [step-03-fill.md](./steps/step-03-fill.md) | Fill (produce artifact) |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `critic` |
| Inputs | Mode; AC/US/FR; sk-user-flow/API maps when present. |
| Outputs | Mode artifact under `artifacts/<task-id>/`. |
| Safety | Do NOT claim pass without sk-execution. Do NOT use real PII as test data. Do NOT claim Playwright scripts are production-ready from hints alone. **Confirm-first** on untestable AC. |

### Required artifacts

- `checklist` → `templates/TEST_CHECKLIST.template.md`
- `cases` / `playwright-hint` → prefer `sk-tester` schema fields in `TESTCASES.md`; seed `templates/TESTCASES_BA.template.md` if starting fresh

## Workflow (detailed mechanics — order enforced by the step files)

1. Confirm mode.
2. `checklist`: scenario inventory by priority/type for review.
3. `cases`: expand checklist rows into executable cases (Given/When/Then or steps).
4. `playwright-hint`: add selector/flow hints only; hand off to engineering for real codegen.

## Quality Standards

- [ ] Cases map to AC/US/FR when available.
- [ ] No real personal data.
- [ ] Playwright mode labeled as hints.
- [ ] Work commit complete.
- [ ] Each case records evidence location, criteria mapping, freshness, limitation, result and next owner.
- [ ] Handoff packet contains Claim, Criteria, Evidence, Coverage map, Limitations, Decision and Next owner.
- [ ] Use `pass`, `block`, or `defer`; never treat a missing human/domain decision as `pass`.

## Output

Produce a reusable ba test artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-ba-test`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.

Hand off the completed packet to `sk-verify-pro`; `sk-done` or a release owner may consume it only after a canonical `pass`.
