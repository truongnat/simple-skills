---
name: detail-design
description: Produce implementable design from BASIC_DESIGN.md — contracts, data model, sequences, rules, operations, client mapping when needed — before planning. Domain-agnostic; omit unused sections.
---

# Detail Design

## Purpose

Turn BASIC_DESIGN.md into implementable specs: how in-scope parts fulfill the approved boundaries.

This skill focuses on:

- Contracts for in-scope surfaces (HTTP, RPC, events, CLI, library APIs — whichever applies).
- Data model at key-field level with known/inferred confidence.
- Sequences for the main happy path plus 1–2 error paths when errors matter.
- Validation and rules at design level.
- Structured operations/queries when data access matters (base source, joins/links, filters with operators, sort/group).
- Client or presentation mapping when a consumer UI/CLI/SDK is in scope.
- Error and state handling for callers.
- Optional persistence write-spec and field provenance when outputs or stores need them.
- Traceability to BR/AC when business-analysis exists.
- Explicit gaps when sources are incomplete.
- Handoff to planning (not execution).

The goal: give planning enough precision without inventing architecture or a fixed product domain.

## Dynamic depth

- Include only sections that apply; omit the rest (no forced N/A blocks).
- Prefer structured lists/tables over prose for contracts, operations, and rules.
- Mark every uncertain field or join as inferred (never as known fact).
- If a needed input is missing, list it under `gaps` and do not invent.
- Multi-surface work: one DETAIL_DESIGN with sections per surface, or linked child notes — stay consistent with BASIC surfaces.

## When to Use

Use this skill when:

- BASIC_DESIGN.md exists and boundaries are agreed.
- Need implementable contracts, models, sequences, or rules before planning or coding.
- Need DETAIL_DESIGN.md for handoff to planning.
- Need BR/AC → design section traceability.

## When NOT to Use

Do NOT use this skill when:

- BASIC_DESIGN.md is missing or still blocked — use basic-design (or research/investigate).
- Direction is unclear — use brainstorming.
- Business requirements are unresolved — use business-analysis.
- Task is small/clear (Lite skip from brainstorming) — planning or execution is enough.
- User wants task IDs, DoD, verification commands, or rollback — use planning.
- User wants code changes — use execution.

## XML Contract

See [openai.yaml](./agents/openai.yaml)

## Quality Standards

- [ ] Goal links to basic-design decisions; no new architecture invented.
- [ ] Only in-scope surfaces get contracts and operations.
- [ ] Data fields and relations mark confidence (known / inferred).
- [ ] Sequences cover main path; error paths when failures matter.
- [ ] Unused optional sections are omitted.
- [ ] Gaps are listed when sources lack detail — not invented away.
- [ ] Handoff is to planning (blocking items called out).

## WRONG vs CORRECT

```markdown
// WRONG — inventing schema as fact
Item.code is VARCHAR(20) NOT NULL unique globally.

// CORRECT — confidence labeled
Item.code (inferred): string, unique within tenant — confirm with data owner.
Item.tenantId (known): FK from existing schema.
```

```markdown
// WRONG — forcing UI matrix on a pure API job
Controls / Screens / Tabs: all N/A...

 // CORRECT — omit client mapping; detail the API surface
Contracts: POST /items — 422 on missing required fields.
Operations: base Item; filter tenantId = :id; sort createdAt desc.
```

```markdown
// WRONG — planning dumped into detail design
T-001: Implement. DoD: PR merged.

// CORRECT — design only
Sequence: Client → API → Service → Store; on scope miss return SCOPE_DENIED.
Handoff: planning.
```

## Edge Cases

| Situation | Handling |
|---|---|
| Basic design still blocked | Do not guess. Flag and recommend research/investigate or stakeholder decision. |
| No UI/client in scope | Omit client_mapping. |
| No persistence | Omit data_model / persistence_spec or keep ephemeral structures only. |
| Existing contracts reused | Prefer inspect-repo facts; mark new contracts as proposed. |
| Source incomplete | Record gaps; partial design is OK if handoff states blockers. |
| BA missing | Trace to DISCUSSION; do not invent BR IDs. |

## Limitations

- Does NOT implement code.
- Does NOT expand scope beyond BASIC_DESIGN.md.
- Does NOT replace planning (no task IDs, DoD, rollback).
- Does NOT treat inferred details as confirmed facts.
- Does NOT re-open architecture without an open question.
- Does NOT hardcode a product domain, UI toolkit, or stack.
