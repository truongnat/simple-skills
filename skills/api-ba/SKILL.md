---
name: api-ba
description: >-
  BA API work: summarize partner API docs (api-doc) or map API↔system↔screen
  (api-map). P0 modes; assess/design noted as follow-ons. Aliases /api-doc
  /api-map. (Hard contract.)
---

# API BA

## Shared preamble (do this first)

Read and follow `.agents/SKILL_PREAMBLE.md` now (Language + Work layout +
Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.
Artifacts go under `.agent-work/` (sessions + memory), not `.agents/`.
Aliases: `.agents/BA_SKILLS.md`.

## Purpose

Produce a **business-facing** API artifact — not a full OpenAPI rewrite unless
asked. Prefer citing partner docs; never invent endpoints.

## Modes

| Mode | Alias | Focus |
| --- | --- | --- |
| `api-doc` | `/api-doc` | Business summary of partner/external API |
| `api-map` | `/api-map` | Mapping API ↔ system data ↔ screen |
| `api-assess` | `/api-assess` | Build vs buy/integrate lean (short) |
| `api-design` | `/api-design` | Integration collaboration sketch (short) |

P0 depth is on `api-doc` and `api-map`. Other modes may be shorter sections in
the same `API_BA.md` when requested.

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `researcher` |
| Inputs | Mode, API docs/URL/spec, consumer screens/flows, system entities, auth constraints. |
| Outputs | `API_BA.md` from template. |
| Safety | Do NOT invent endpoints/fields. Do NOT copy secrets. Do NOT claim production readiness without evidence. **Confirm-first** when docs missing. |

### Required artifacts

#### `API_BA.md`
- Seed `templates/API_BA.template.md`
- executive_summary, developer_overview, mode, sources, summary or mapping tables,
  risks, open_questions, handoff

## Workflow

1. Confirm mode + source docs.
2. For `api-doc`: capabilities, auth, limits, business caveats.
3. For `api-map`: three-layer table API field ↔ system ↔ UI.
4. Commit Work.

## Quality Standards

- [ ] Sources cited; invented bits marked Assumption.
- [ ] Mapping rows have all three layers when mode=`api-map`.
- [ ] Work nested git: ran `session.sh commit 'docs(api-ba): …'` after writing
      (or `WORK_COMMIT=clean`).
