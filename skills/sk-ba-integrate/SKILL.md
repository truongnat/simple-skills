---
name: sk-ba-integrate
description: >-
  BA tool sk-sync scaffolds: Jira Cloud (/jira) and Confluence (/confluence)
  bidirectional plans. Offline mapping first; live API only with explicit
  credentials and user confirmation. (Hard contract.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [requirements,integration]
sk-roles: [reasoner]
sk-compatible: [claude, cursor, codex, gemini]
---

# BA integrate (Jira / Confluence)

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Prepare **safe** sk-sync between task backlog/project documentation and Jira/Confluence.

## Modes

| Mode | Alias | Output |
| --- | --- | --- |
| `jira` | `/jira` | `INTEGRATE_JIRA.md` |
| `confluence` | `/confluence` | `INTEGRATE_CONFLUENCE.md` |

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
| preferred_role | `researcher` |
| Inputs | Mode; local stories/AC/project documentation; site URL; project/space keys; auth method. |
| Outputs | Integrate plan artifact; optional dry-run log. |
| Safety | Do NOT store API tokens in task artifacts. Do NOT live-push without explicit user confirmation. Do NOT overwrite remote blindly — prefer dry-run + field mapping. Secrets only via env/OS keychain, never committed. **Confirm-first**. |

### Required artifacts

- `jira` → `templates/INTEGRATE_JIRA.template.md`
- `confluence` → `templates/INTEGRATE_CONFLUENCE.template.md`

## Workflow (detailed mechanics — order enforced by the step files)

1. Build field/page mapping from local IDs ↔ remote keys.
2. Produce dry-run change list (create/update/skip).
3. If user confirms live sk-sync: use official CLI/API with env credentials; log results without secrets.

## Quality Standards

- [ ] Mapping table complete for in-scope items.
- [ ] Dry-run before live.
- [ ] No tokens in markdown.
- [ ] Work commit complete.

## Output

Produce a reusable ba integrate artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary


**`sk-ba-integrate`** owns the business integration map for Jira/Confluence and related project-system synchronization: actors, systems, exchanged information, ownership, lifecycle states, failure expectations, and synchronization intent.

It does **not** own API contract design, connector implementation, or external write execution without the required approval. Route API behavior to `sk-api-ba`/`sk-api-design-pro`, repository state to `sk-sync`, and evidence decisions to `sk-verify-pro`.

**Primary artifact:** an integration requirement map with ownership and failure expectations. **Handoff:** pass the business map to API/integration implementation owners and the refreshed state to `sk-sync`.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review for quality findings; sk-verify-pro for canonical claim-to-evidence decisions (sk-verification is a compatibility facade only).
