---
name: ux-wireframe
description: >-
  BA screen sketches: ASCII wireframe (/wireframe-ascii), static HTML
  wireframe (/wireframe-html), or simple interactive HTML prototype
  (/prototype-html). Not Figma. (Hard contract.)
---

# UX wireframe

## Shared preamble (do this first)

Read and follow `.agents/SKILL_PREAMBLE.md` now (Language + Work layout +
Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.
Artifacts go under `.agent-work/` (sessions + memory), not `.agents/`.
Aliases: `.agents/BA_SKILLS.md`.

## Purpose

Produce **low-fidelity** screen sketches for BA review. Figma (`/figma`) remains P2.

## Modes

| Mode | Alias | Output |
| --- | --- | --- |
| `ascii` | `/wireframe-ascii` | `WIREFRAME.md` (ASCII in markdown) |
| `html` | `/wireframe-html` | `wireframes/<screen>.html` + index note in `WIREFRAME.md` |
| `prototype` | `/prototype-html` | `prototypes/<flow>.html` with minimal interactivity |

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `reasoner` |
| Inputs | Mode, screens/flow from `user-flow`/US, content fields, constraints. |
| Outputs | `WIREFRAME.md` always; HTML files under session for html/prototype modes. |
| Safety | Do NOT present as final UI design. Do NOT embed secrets. Do NOT claim accessibility sign-off. Keep HTML offline-friendly (no build step). **Confirm-first** on unknown IA. |

### Required artifacts

#### `WIREFRAME.md`
- Seed `templates/WIREFRAME.template.md`
- executive_summary, mode, screens list, ascii or links to HTML, open_questions, handoff

## Workflow

1. Confirm mode + screen list (from user-flow when present).
2. `ascii`: boxes in markdown fences.
3. `html`: grayscale semantic HTML; link from `WIREFRAME.md`.
4. `prototype`: buttons/tabs that toggle sections; localStorage optional; document limits.
5. `session.sh commit 'docs(ux-wireframe): …'`.

## Quality Standards

- [ ] Screens trace to US/flow IDs when available.
- [ ] Labeled low-fidelity / not production UI.
- [ ] Work commit done.
