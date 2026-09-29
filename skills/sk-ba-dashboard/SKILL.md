---
name: sk-ba-dashboard
description: >-
  BA project dashboard: progress, coverage, and risks across task artifacts
  (/dashboard). Writes DASHBOARD.md with honest status — no fake green.
  (Hard contract.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [requirements,reporting]
sk-roles: [reasoner]
sk-compatible: [claude, cursor, codex, gemini]
---

# BA dashboard

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Single skim view of BA delivery health for the **current task workspace** (and optional

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
| preferred_role | `reasoner` |
| Inputs | Active task artifacts, optional TASKS/PLAN, memory INDEX. |
| Outputs | `DASHBOARD.md` from template. |
| Safety | Do NOT invent coverage %. Do NOT mark Ready while Blocking gaps remain. Prefer tool counts over hand-waved progress. **Confirm-first** if task artifact path unclear. |

### Required artifacts

#### `DASHBOARD.md`
- Seed `templates/DASHBOARD.template.md`
- executive_summary, developer_overview, artifact_inventory, coverage,
  risks, blockers, next_actions, handoff

## Workflow (detailed mechanics — order enforced by the step files)

1. Resolve the task artifact directory; inventory artifacts present/missing.
3. Coverage by area (spec/model/story/api/test/ux).
4. Top risks + blockers; next actions ordered.

## Quality Standards

- [ ] Inventory matches files on disk.
- [ ] No fake 100% / all-green without evidence.
- [ ] Work commit complete.

## Output

Produce a reusable ba dashboard artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.
