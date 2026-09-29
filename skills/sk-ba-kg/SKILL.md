---
name: sk-ba-kg
description: >-
  BA knowledge graph: link IDs and artifacts across the task artifacts into a
  searchable graph (/kg). Writes KG.md with Mermaid graph + edge table.
  (Hard contract.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [knowledge-graph,requirements]
sk-roles: [researcher]
sk-compatible: [claude, cursor, codex, gemini]
---

# BA knowledge graph

## Shared preamble (do this first)

## Working principles

Use clear, concrete language. Cite paths and IDs, distinguish evidence from assumptions, and record open questions instead of inventing details.

## Purpose

Build a **trace graph** of entities (Epic/US/AC/FR/BR/API/Screen/Test) and
edges (implements, traces, tests, maps). For lookup, not a vector DB.

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
| Inputs | Task artifacts with IDs; optional focus question. |
| Outputs | `KG.md` from template. |
| Safety | Do NOT invent links without citing both ends. Orphan IDs stay listed as orphans. **Confirm-first** if corpus empty. |

### Required artifacts

#### `KG.md`
- Seed `templates/KG.template.md`
- executive_summary, nodes, edges, mermaid graph, orphans, query_answers, handoff

## Workflow (detailed mechanics — order enforced by the step files)

1. Scan the task artifacts for IDs and explicit mappings.
2. Build node + edge tables; draw Mermaid `flowchart` or `graph`.
3. List orphans (ID with no edge).
4. Answer focus question if provided.

## Quality Standards

- [ ] Every edge cites source artifact.
- [ ] Orphans visible.
- [ ] Work commit complete.

## Output

Produce a reusable ba kg artifact with the selected approach, relevant files or evidence, verification results, limitations or risks, and next steps.

## Boundary

**`sk-ba-kg`** owns **development lifecycle, requirements analysis, planning, specification, review, and delivery handoffs**. It does not own **product/domain-specialist implementation as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review and sk-verification for quality evidence.
