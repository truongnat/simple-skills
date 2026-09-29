---
name: sk-ba-handoff
description: >-
  BA handoff/ops: meeting minutes (/meet), userguide, export pack, HTML preview,
  update-overview. Offline-first artifacts in the task artifact directory; office skills for
  PDF/Word when needed. (Hard contract.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [handoff,documentation]
sk-roles: [reasoner]
sk-compatible: [claude, cursor, codex, gemini]
---

# BA handoff

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Produce stakeholder-facing handoff artifacts without inventing decisions.

## Modes

| Mode | Alias | Output |
| --- | --- | --- |
| `meet` | `/meet` | `MEETING.md` |
| `userguide` | `/userguide` | `USERGUIDE.md` |
| `export` | `/export` | `EXPORT.md` + optional office renders |
| `preview` | `/preview` | `preview/index.html` + `PREVIEW.md` |
| `update-overview` | `/update-overview` | `OVERVIEW_SHARED.md` (project shared note — not lifecycle OVERVIEW.md) |

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
| Inputs | Mode; notes/transcript/sources; audience; format targets. |
| Outputs | Mode artifact(s) under `artifacts/<task-id>/`. |
| Safety | Do NOT invent meeting decisions. Do NOT put secrets in export/preview. Do NOT create retired lifecycle `OVERVIEW.md` progress page — use `update-overview` shared note only. **Confirm-first** on ambiguous owners/dates. |

### Required artifacts

Templates under `templates/` for each mode file listed above.

## Workflow (detailed mechanics — order enforced by the step files)

1. Confirm mode + audience.
2. Seed template; cite sources.
3. `export`/`preview`: list included artifacts; render via `sk-docx`/`sk-pdf`/`html` skills when requested.

## Quality Standards

- [ ] Decisions vs actions separated in `meet`.
- [ ] Userguide roles clear (admin/CS/…).
- [ ] Export/preview inventory honest.
- [ ] Work commit complete.

## Output

Produce a reusable ba handoff artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-ba-handoff`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.
