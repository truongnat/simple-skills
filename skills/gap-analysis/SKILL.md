---
name: gap-analysis
description: >-
  BA gap analysis: find missing business flows, rules, AC, or capabilities
  versus a feature/spec. Alias /gap. Writes GAP.md. (Hard contract.)
---

# Gap analysis

## Shared preamble (do this first)

Read and follow `.agents/SKILL_PREAMBLE.md` now (Language + Work layout +
Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.
Artifacts go under `.agent-work/` (sessions + memory), not `.agents/`.
Aliases: `.agents/BA_SKILLS.md`.

## Purpose

Compare **expected** capability for a feature type against **documented /
observed** coverage. Promote Blocking gaps into questions; do not silently fix
product decisions.

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `critic` |
| Inputs | Feature/epic under review, BA/PRD/SRS/stories/AC/models, optional code/UI evidence. |
| Outputs | Session `GAP.md` from template. |
| Safety | Do NOT invent gaps without stating the expectation source. Do NOT close Blocking gaps without user confirmation. **Confirm-first**. |

### Required artifacts

#### `GAP.md`
- Seed `templates/GAP.template.md`
- executive_summary, developer_overview, subject, expected_capabilities,
  gaps (ID, area, severity, evidence, recommendation), open_questions, handoff

## Workflow

1. State subject + expectation baseline (industry norm / prior BR / sibling feature).
2. Inventory covered flows/rules/AC/UI/API.
3. List gaps with severity Critical/High/Medium/Low.
4. Ask Blocking questions; commit Work.

## Quality Standards

- [ ] Each gap has evidence + recommendation.
- [ ] Severity taxonomy used.
- [ ] Work nested git: ran `session.sh commit 'docs(gap-analysis): …'` after writing
      (or `WORK_COMMIT=clean`).
