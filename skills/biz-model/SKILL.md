---
name: biz-model
description: >-
  BA business diagrams in one skill: sequence, activity, swimlane, bpmn, state,
  erd, usecase-diagram. Default Mermaid; PlantUML for swimlanes. Use for /sequence
  /activity /bpmn /state /erd /usecase-diagram aliases. (Hard contract — MUST follow.)
---

# Biz model (BA diagrams)

## Shared preamble (do this first)

Read and follow `.agents/SKILL_PREAMBLE.md` now (Language + Work layout +
Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.
Artifacts go under `.agent-work/` (sessions + memory), not `.agents/`.
Source copy: `docs/SKILL_PREAMBLE.md` / `docs/AGENT_WORK.md`.
Aliases: `.agents/BA_SKILLS.md`.

## Purpose

Produce **one** diagram package for a business/system concern. Prefer diagrams
that trace to FR/US/AC IDs already in the session.

## Modes

| `diagram` | Alias | Default format |
| --- | --- | --- |
| `sequence` | `/sequence` | mermaid |
| `activity` | `/activity` | mermaid |
| `activity-swimlane` | `/activity-swimlane` | plantuml |
| `bpmn` | `/bpmn` | mermaid (BPMN-like) + notes for Camunda/Bizagi export limits |
| `state` | `/state` | mermaid |
| `erd` | `/erd` | mermaid |
| `usecase-diagram` | `/usecase-diagram` | mermaid |

`format`: `mermaid` (default) | `plantuml`.  
D2 / dbdiagram: record under **Limitations** as P1; do not claim live render unless tool exists.

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action.

| Field | Requirement |
|-------|-------------|
| preferred_role | `reasoner` |
| Inputs | `diagram` mode, subject (process/object/system), actors, related SPEC/BA/PRD IDs, format preference. |
| Outputs | Session `MODEL.md` seeded from template, with one primary diagram fenced block. |
| Safety | Do NOT invent systems/actors not evidenced. Do NOT omit alternate/exception paths when the subject has decisions. Do NOT claim BPMN XML/Camunda import unless actually produced. **Confirm-first** when subject or actors are Blocking-unknown. |

### Required artifacts

#### `MODEL.md`
- Required: yes — seed `templates/MODEL.template.md`
- **executive_summary**, **developer_overview**, **diagram**, **format**
- **subject**, **actors_or_entities**, **trace_refs**
- **diagram_source** (fenced mermaid/plantuml)
- **legend**, **open_questions**, **limitations**, **handoff**

## Workflow

1. Confirm `diagram` (+ format if needed).
2. Gather actors/entities from session artifacts; list `trace_refs`.
3. Seed `MODEL.md`; draw the diagram; note limitations (esp. BPMN/D2).
4. `session.sh commit 'docs(biz-model): <diagram> …'`.

## Quality Standards

- [ ] One primary diagram; headings English.
- [ ] Happy path + key decision/exception branches when applicable.
- [ ] Trace refs to FR/US/AC/BR when they exist.
- [ ] Limitations honest (no fake Camunda XML).
- [ ] Work nested git: ran `session.sh commit 'docs(biz-model): …'` after writing
      (or `WORK_COMMIT=clean`).
