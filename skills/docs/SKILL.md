---
name: docs
description: >-
  Build and maintain an enterprise documentation set (SRS, Architecture, HLD,
  LLD, ADRs, Reference, Operations, Guides) as a wiki. Two modes: full (author
  the whole set) and sync (update only what a code change affects). Honors
  rules.docs. (Hard contract in this SKILL.md — MUST follow.)
---

# Docs (enterprise documentation wiki)

## Language (do this first)

**Re-read `.agents/settings.yaml` now** — do not reuse a `language` value cached
earlier in this session. Write every document and reply in that `language`
(`en` or `vi`); keep code, identifiers, paths, commands, requirement IDs, and
section keys unchanged. A direct instruction in the current user request
overrides the file.

## Memory (read first)

Before writing, read `.agents/memory/INDEX.md` and open entries whose hook
matches the area; reuse recorded decisions/gotchas instead of re-deriving them.

## Purpose

Produce **real, standards-based documentation** for the project — not a thin
skim. This wiki is for humans (engineers, reviewers, new joiners, stakeholders)
and is distinct from `.agents/PRJ_REFERENCE.md` (agent context). It is built on
recognized standards so it holds up in an enterprise setting:

| Document | Standard it follows |
|---|---|
| SRS (requirements) | **ISO/IEC/IEEE 29148** (supersedes IEEE 830) |
| Architecture | **arc42** (12 sections) + **C4** diagrams + **4+1 views** |
| Architecture decisions | **ADR** (MADR/Nygard), one record per decision |
| High-Level Design (basic design) | fed by the `basic-design` skill / `BASIC_DESIGN.md` |
| Low-Level Design (detailed design) | fed by the `detail-design` skill / `DETAIL_DESIGN.md` |
| Guides (user-facing) | **Diátaxis** (tutorial / how-to / reference / explanation) |

## This is not a one-shot skim (depth gate — mandatory)

A credible doc set is authored **document-by-document**, each with its required
sections filled from real evidence. You MUST:

- Fill **every required section** of each in-scope document (list below). If a
  section does not apply, write `N/A` **with a one-line reason** — never delete
  it and never leave a heading empty.
- **Cite the source** (file/path/§) for each substantive claim. Where evidence
  is missing, write `Gap:` / `Unknown` and add it to the coverage matrix —
  **do not invent** behavior, requirements, or decisions.
- Assign stable IDs (`FR-001`, `NFR-001`, `ADR-001`, `BR-001`) and keep a
  **traceability** thread: requirement → design → code/test.
- Populate the **Documentation coverage matrix** in `Home.md` (each document:
  status `complete` / `partial` / `gap` / `N/A` + owner + last-synced). A wiki
  with everything `complete` on the first pass over a non-trivial repo is a red
  flag — be honest about `partial`/`gap`.

Scale rule: small projects may mark whole documents `N/A (reason)` — but that is
an explicit, visible decision, not a silent omission.

## Modes

| Mode | Use | Behavior |
|---|---|---|
| `full` | Doc set missing or a full rebuild is requested | Author every in-scope document to its standard. |
| `sync` | Code changed | Update only the documents/sections a change affects (via `.docmap.md`). |

## Information architecture (the doc set)

Author the **markdown source tree** under `rules.docs.location` (canonical
source; other formats render from it). Standard layout:

```
Home.md                         # landing: 80/20 + document map + coverage matrix
.docmap.md                      # source paths -> unit + last-synced commit
01-requirements/
  SRS.md                        # ISO/IEC/IEEE 29148
  glossary.md
02-architecture/
  architecture.md               # arc42 (12) + C4 (context/container/component) + 4+1
  decisions/ADR-index.md
  decisions/ADR-001-*.md        # one file per decision
03-design/
  HLD.md                        # High-Level / basic design  (<- BASIC_DESIGN.md)
  LLD.md                        # Low-Level / detailed design (<- DETAIL_DESIGN.md)
04-reference/
  api-reference.md
  data-model.md
  configuration.md
  workspaces/<name>.md          # per app/package surfaced by the scanner
05-operations/
  deployment.md
  runbook.md
  observability.md
  security.md
06-guides/                      # Diátaxis
  onboarding.md · tutorials.md · how-to.md · explanation.md
```

Templates in `templates/`: `SRS`, `ARCHITECTURE`, `HLD`, `LLD`, `ADR`,
`API_REFERENCE`, `DATA_MODEL`, `RUNBOOK`, `GUIDE`, `WIKI_HOME`, `WIKI_PAGE`,
`DOCMAP`, plus `DOCX_OUTLINE` / `XLSX_STRUCTURE` for those formats.

### Reuse existing artifacts (do not re-derive)

Aggregate what the lifecycle already produced instead of inventing:
- **SRS** ← `BUSINESS_ANALYSIS.md` + `DISCUSSION.md` (stories, rules, AC, scope).
- **HLD** ← `BASIC_DESIGN.md`; **LLD** ← `DETAIL_DESIGN.md`.
- **ADRs** ← decisions recorded in brainstorming/planning gates.
- **Reference/workspaces** ← the scanner + code; **memory** for prior gotchas.
If a source artifact is missing, note the `Gap` and document from code evidence.

## Output format (resolve first)

Read `rules.docs.format`; the **markdown tree is the canonical source**, the
others render from it (keeps `sync` incremental). Keep `.docmap.md` always.

| Format | Organization | Built with | Sync unit |
|---|---|---|---|
| `markdown` | The doc tree above; cross-linked `.md`. | Write tool | file/section |
| `html` | Same tree rendered to linked `.html` + shared `styles.css`; nav on `index.html`. Enterprise `.ss-*` theme, self-contained, accessible. | per `.agents/DESIGN_SYSTEM.md` | page |
| `docx` | **One controlled document** with a title page, TOC, and the doc set as parts (SRS, Architecture, HLD, LLD, ADRs, …) using Heading styles. | the **`docx`** skill; see `templates/DOCX_OUTLINE.template.md` | heading section |
| `xlsx` | **Workbook**: requirements register, traceability matrix, NFRs, ADR log, workspaces, data dictionary, coverage — tabular. | the **`xlsx`** skill; see `templates/XLSX_STRUCTURE.template.md` | sheet/row |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | `rules.docs` (enabled, location, format, sync_strategy), `rules.branch`, repo source/config, session artifacts (`BUSINESS_ANALYSIS.md`, `BASIC_DESIGN.md`, `DETAIL_DESIGN.md`, `DISCUSSION.md`), `.agents/PRJ_REFERENCE.md`, `.agents/memory/`, the change set for `sync`, existing wiki + `.docmap.md`. |
| Outputs | The enterprise doc set under `rules.docs.location` in the resolved `format`, with a coverage matrix in `Home.md`, ADRs, traceability IDs, and `.docmap.md`. |
| Safety | Read-only against project code (never execute it) except the bundled scanner. **Do NOT invent** requirements, behavior, or decisions — cite sources; mark `Gap`/`Unknown`. Never write secrets. Honor the branch gate. In `sync`, touch only affected documents/sections. |

### Branch gate (mandatory, before writing)

- `main-only`: write the wiki **only** on the base/main branch. On a feature
  branch, do not touch it — report that docs are refreshed on `main` and stop.
- `with-commit`: write on the current branch; when invoked from `done`, **stage
  the wiki changes into the same commit** so they travel through the PR.

### Required artifacts (per in-scope document)

Each document must contain its standard sections (see its template); the core:

- **SRS** — Introduction (purpose, scope, product overview, definitions);
  References; Specific requirements (external interfaces; functional `FR-*`;
  usability; performance; database/data; design constraints; software system
  attributes: reliability/availability/security/maintainability/portability);
  Verification; Appendices incl. **traceability**.
- **Architecture (arc42)** — 1 Introduction & Goals · 2 Constraints · 3 Context
  & Scope · 4 Solution Strategy · 5 Building Block View (C4) · 6 Runtime View ·
  7 Deployment View · 8 Crosscutting Concepts · 9 Architecture Decisions (link
  ADRs) · 10 Quality Requirements · 11 Risks & Technical Debt · 12 Glossary.
- **HLD** — components, boundaries, interfaces, data ownership, main flows.
- **LLD** — contracts, data model (fields/types), sequences, validation/rules,
  error/state handling, per-module detail.
- **ADR** — Context · Decision · Status · Consequences · Alternatives.
- **Reference/Operations/Guides** — per their templates.
- **`.docmap.md`** — required (every format): unit → source paths + last-synced.

## Workflow

### Common preflight
1. Read `rules.docs`. If `enabled: false`, stop. Resolve `format`.
2. Apply the **Branch gate**; stop if it forbids writing here.
3. Decide the in-scope doc set (mark out-of-scope docs `N/A` with reason).
4. Gather sources: session artifacts, `PRJ_REFERENCE.md`, memory, and coverage:
   ```bash
   bash .agents/skills/init/scripts/scan_workspaces.sh
   ```

### Mode `full`
5. Author the markdown source **document by document**, each to its template and
   standard, filling every required section, citing sources, and assigning IDs.
6. Build the **coverage matrix** in `Home.md` (status/owner/last-synced per doc)
   and the ADR index; thread traceability (req → design → code/test).
7. **Render to `format`** if not markdown (html per DESIGN_SYSTEM.md; docx via
   the `docx` skill; xlsx via the `xlsx` skill).
8. Write `.docmap.md` with the current commit (`git rev-parse --short HEAD`).

### Mode `sync`
5. Change set: `git diff --name-only <Last-synced>..HEAD` (or the task's files).
6. Map changed paths → affected documents/sections via `.docmap.md`; update
   **only** those, plus the coverage matrix and any new ADR the change implies.
   Re-run the scanner: add/remove workspace pages for added/removed projects.
7. Re-render only affected units; refresh `Last-synced`. Leave the rest intact.
8. If `sync_strategy: with-commit` and invoked by `done`, stage the changes.

## Quality Standards

- [ ] `format` resolved; the format's organization followed.
- [ ] Every in-scope document has all required sections (or `N/A` + reason).
- [ ] Requirements/decisions carry stable IDs; traceability thread present.
- [ ] Every substantive claim cites a source; gaps marked `Gap`/`Unknown`.
- [ ] `Home.md` has a coverage matrix reflecting real status (not all-green).
- [ ] `full` covers every project the scanner surfaces (per-workspace pages).
- [ ] `sync` touched only affected documents/sections via `.docmap.md`.
- [ ] docx/xlsx built via the `docx`/`xlsx` skills; html self-contained.

## Reference

`agents/openai.yaml` mirrors this contract for tooling. This SKILL.md is authoritative.

## Limitations

- Does NOT implement or modify project code.
- Does NOT replace `.agents/PRJ_REFERENCE.md` (agent context).
- Does NOT invent requirements/decisions to fill a template — gaps stay visible.
- `sync` is only as good as `.docmap.md`; run `full` first if it is missing.
