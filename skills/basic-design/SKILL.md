---
name: basic-design
description: Turn an approved DISCUSSION.md direction into system-level design — boundaries, components, flows, interfaces, and data ownership — before detail design or planning. Domain-agnostic; omit unused sections.
---

# Basic Design

## Purpose

Turn an approved direction into a system-level design: what is being built, where boundaries sit, and which parts own which data.

This skill focuses on:

- Capture the chosen recommendation from DISCUSSION.md as design context.
- Define architecture overview and major components.
- Describe main actor or system flows (happy paths only).
- Name external interfaces at purpose level (not full contracts).
- Assign logical data ownership (entities/stores, not full schemas).
- List logical data sources with access mode (read/write/both) when relevant.
- Note major entry points or surfaces in scope (omit if N/A).
- Note relevant NFRs only when they affect design.
- Prepare handoff to detail-design (or research/investigate if blocked).

The goal: lock boundaries before writing implementable contracts or task plans. Stay domain-agnostic — works for APIs, UIs, batches, libraries, CLIs, or mixed systems.

## Dynamic depth

- Include only sections that apply to the task.
- Omit unused optional sections (do not invent filler).
- Mark gaps as open questions instead of guessing.
- Lite Mode: short goal + components + flows + handoff (5–10 bullets).

## When to Use

Use this skill when:

- DISCUSSION.md has a clear recommendation and scope.
- Task needs architecture, module boundaries, or flow structure before coding.
- Multiple components or systems interact and ownership must be clear.
- Need BASIC_DESIGN.md before detail-design or planning.
- Business-analysis is done (or not needed) and technical shape is next.

## When NOT to Use

Do NOT use this skill when:

- Direction is still unclear — use brainstorming first.
- Business rules/AC are unclear and stakeholders must decide — use business-analysis.
- Task is small/clear (Lite skip) — handoff straight to planning or execution.
- User asks for full contracts, field lists, or query specs — use detail-design.
- User asks for task breakdown, DoD, or rollback — use planning.
- User needs code changes — use execution.
- Deep external comparison is needed first — use research.
- Root-cause debugging is needed — use investigate.

## XML Contract

See [openai.yaml](./agents/openai.yaml)

## Quality Standards

- [ ] Goal is one sentence aligned with DISCUSSION recommendation.
- [ ] Architecture overview is short; diagram only if it clarifies boundaries.
- [ ] Each component has a clear responsibility.
- [ ] Flows cover main paths only — no task IDs or full contracts.
- [ ] External interfaces are purpose-level only.
- [ ] Unused optional sections are omitted (not filled with N/A spam).
- [ ] Open questions mark blocking vs non-blocking.
- [ ] Handoff points to detail-design, or research/investigate if blocked.

## WRONG vs CORRECT

```markdown
// WRONG — detail dumped into basic design
POST /api/items body: { id: string, name: string, ... 20 fields }

// CORRECT — purpose-level boundary
External: Item Admin API — create/list items in tenant scope.
Ownership: Item Service owns Item; Tenant Master is read-only for this feature.
```

```markdown
// WRONG — forcing UI sections on a library change
Screens: N/A. Controls: N/A. Tabs: N/A.

// CORRECT — omit UI; keep what applies
Components: Parser module, Config loader.
Flows: Load config → parse input → emit result events.
```

## Edge Cases

| Situation | Handling |
|---|---|
| DISCUSSION conflicts with repo patterns | Prefer existing patterns. Document conflict as open question. |
| Blocking unknown | Stop short of fake design. Handoff to research or investigate. |
| Single-module change | Lite Mode — skip unused optional sections. |
| Multi-artifact pack (hub + children) | One BASIC_DESIGN with surfaces list; detail-design may split per surface later. |
| No BA notes but rules implied | Mark as assumptions; do not invent BR IDs. |

## Limitations

- Does NOT implement code.
- Does NOT replace brainstorming when direction is unclear.
- Does NOT replace business-analysis for requirements.
- Does NOT produce full contract/query/field detail (use detail-design).
- Does NOT produce PLAN.md task breakdown (use planning).
- Does NOT invent file paths without inspecting the codebase.
- Does NOT hardcode a product domain, screen type, or stack.
