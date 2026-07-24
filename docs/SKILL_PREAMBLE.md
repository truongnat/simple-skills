# Shared skill preamble

First-party skills point here instead of pasting Language/Memory/Work blocks.
**Read this file fully** at the start of every first-party skill invocation —
before Purpose, Contract, or steps.

Installed path: `.agents/SKILL_PREAMBLE.md` (source: `docs/SKILL_PREAMBLE.md`).
Layout detail: `.agents/AGENT_WORK.md`.

## Language (do this first)

**Re-read `.agents/settings.yaml` now** — do not reuse a `language` value cached
earlier in this session. Values: `en` | `vi`. Mid-session edits win after
re-read. A direct instruction in the current user request overrides the file.

### What follows `language` (prose only)

Write **all narrative content** in that language: executive summary bullets,
paragraphs, table *cell values* that are sentences, questions to the user,
recommendations, handoff prose, Clarification checkpoint answers.

**One language per artifact.** Do not mix: a Vietnamese summary with an English
architecture paragraph, or half-translated tables. If unsure of a term, keep the
domain identifier raw and explain once in `language` — do not flip the whole
section to English.

### What stays English (shared form — never translate)

Keep the **template form** identical across projects so schemas/lint/tools work:

| Keep in English | Examples |
| --- | --- |
| Markdown `##` / `###` headings | `## Executive summary`, `## Doc reality check`, `## Goal` |
| Template section titles & Step ledger step names | `Frame + Spec quality`, Status column labels as in templates |
| Table **column headers** from templates | `Claim`, `Doc evidence`, `Verdict`, `Blocking`, `Ask user?` |
| Enum / machine values | `Quick`/`Lite`/`Full`, `PASS`/`FAIL`, `Match`/`Mismatch`, `todo`/`done`/`blocked`, `Confirmed?` Yes/No |
| Code, paths, commands, API routes, IDs | `FBD13001`, `lblBase`, `src/...` |

**Wrong (`language: vi`):** `## Tóm tắt điều hành` or `## Mục tiêu`  
**Right (`language: vi`):** `## Executive summary` with Vietnamese bullets underneath.

**Domain terms:** keep original product/spec identifiers (JP screen names, field
IDs, API paths) as-is. Do **not** invent bilingual ceremony (JP/EN/VN label
rows) unless the domain artifact itself requires it.

## Work layout (mandatory)

Simple Skills splits **Kit** and **Work**:

| Layer | Path | Contents |
| --- | --- | --- |
| Kit | `.agents/` | skills, tools, settings, policy (installer) |
| Work | `.agent-work/` | `sessions/` + `memory/` together (nested git) |

Rules:

1. Write lifecycle artifacts **only** under
   `.agent-work/sessions/<Task-N-…>/` — never under `.agents/`, temp, or cache.
2. Write durable lessons **only** under `.agent-work/memory/`.
3. Resolve the active session with:
   ```bash
   bash .agents/tools/session/session.sh current
   ```
   Create one with `session.sh new <slug>` (also ensures `.agent-work` + nested
   git). Progress: `session.sh status`.
4. Do **not** put task artifacts into `.agents/skills` or other kit paths.
5. Prefer the product root `.gitignore` to include `.agent-work/` so Work history
   stays in its nested git, not the product repo.

## Memory (read first)

Before framing, researching, deciding, designing, planning, investigating, or
writing durable docs, read `.agent-work/memory/INDEX.md` and open the entries
whose hook matches this task. Reuse prior decisions, gotchas, and conventions
instead of re-deriving them; if memory conflicts with current evidence, trust
current evidence and note the drift. If none apply, continue.
(Memory is written by `done` — the vital few only.)

Skills that only execute, sync, review, or test still obey Language and Work
layout. Memory is optional for those unless the task needs prior decisions.

## Thinking methods (session-wide — not titles)

**Vital few** and **5W1H** are methods for the whole session context. They are
**not** report section names.

- Use **vital few** to prioritize what actually changes the outcome (summaries,
  memory). Do not title anything `80/20` or brand the executive summary
  with a method suffix. Do not create a separate `OVERVIEW.md`.
- Use **5W1H** only when the problem is hard/unclear — apply it to the session
  goal and evidence, then fold answers into real sections. Do not stamp 5W1H
  tables, do not answer trivia, do not brand a heading `5W1H`.

Details: `.agents/AGENT_POLICY.md` → Thinking methods.

## Readable writing (mandatory — every artifact)

Readers must understand ~80%+ of the artifact on a **first pass** without
decoding jargon. If a teammate new to the task cannot act from it, rewrite.

**Do:**

1. Concrete names: file paths, API routes, table/field IDs, screen IDs,
   commands, ticket/AC IDs, exact error strings.
2. Short sentences. One claim per bullet. Tables for lists of facts.
3. Spec quality / Doc reality findings = **specific** finding + evidence path +
   verdict. Example: `FBD13001 Search ignores BaseCd — see api/… line 40 —
   Mismatch` — not “cần align architecture với domain”. When designing or
   investigating from docs: **ask** on Blocking mismatches (docs vs code /
   common vs 設計書 / stale wiki) before continuing.
4. Delete unused sections. Finished artifacts must not contain `_(TODO)_` or
   leftover template scaffolding.
5. Charts only when they change a decision; otherwise omit (no decorative
   placeholder Mermaid).
6. **Keywords** (discovery artifacts): when the report uses domain/opaque terms
   a busy teammate would not know, fill `## Keywords` — see below.

**Do not:**

1. Pad to fill the template. Empty honesty beats fake completeness.
2. Abstract filler: “leverage”, “align stakeholders”, “holistic approach”,
   “ensure consistency”, “optimize the flow” with no object.
3. Restate section titles as content (“This section covers feasibility…”).
4. Dump bilingual labels (JP/EN/VN) unless the **domain artifact** requires
   them; never invent translation noise for ceremony.
5. Answer method prompts (5W1H / vital-few) as trivia sections.
6. Narrate your process (“I will now analyze…”, “As an AI…”).

### Keywords (glossary for discovery reports)

Required on **brainstorming / investigate / research** artifacts when the body
uses terms a new teammate would not decode on first pass. Optional elsewhere
when the same problem appears. Heading stays English: `## Keywords`.

| Column | Content |
| --- | --- |
| Term | Exact string as used in the report (ID, JP name, acronym, module) |
| Meaning | One short line in `settings.language` |
| Where seen | Path / doc § / log / UI — evidence, not invention |

**Include a term when ≥1 is true:**

1. **Opaque ID / product name** — screen/form IDs (`FBD13001`, `RBD09002`), JP
   帳票/画面 names, internal service nicknames.
2. **Acronym or shorthand** used more than once, or once but critical to the
   recommendation (e.g. `WMS`, `指図`, `ExcelCreator`).
3. **Project-specific meaning** of a common word (e.g. “common” = shared print
   pipeline in *this* repo).
4. **Doc/code token** the reader must map (control IDs, table names, error
   codes) to follow evidence or Doc reality rows.

**Do not list:** everyday words; generic programming vocabulary (`HTTP`,
`JSON`, `null`) unless the project redefines them; every column of a wide
Excel; bilingual triple rows for ceremony.

**Cap:** vital few — typically **3–12** rows. Prefer linking Meaning to Where
seen over essays. If no opaque terms → `_(none — plain language)_` once.

Self-check before saving: *Would I paste this into a PR for a busy reviewer?*
If no → cut half, name concrete things, move guesses to Unknowns.

## Scale (Quick / Lite / Full)

At task start, pick a path (see `.agents/AGENT_POLICY.md` → Scale & Quick path):

- **Quick** — tiny clear fix; skip BA/design/Spec matrices; still use TASK Dev context.
- **Lite** — small feature; short sections; optional skip design.
- **Full** — unclear product or multi-surface; full lifecycle.

Record the choice in DISCUSSION/PLAN Developer overview (`Path:`).
