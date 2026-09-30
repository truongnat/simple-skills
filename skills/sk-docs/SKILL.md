---
name: sk-docs
description: >-
  Build and maintain an enterprise documentation set (SRS, Architecture, HLD,
  LLD, ADRs, Reference, Operations, Guides) as a wiki. Two modes: full (author
  the whole set) and sk-sync (update only what a code change affects). Honors
  the project documentation settings. (Hard contract in this SKILL.md — MUST follow.)
sk-kind: domain
sk-version: 0.1.0
sk-tags: [documentation, research, business]
sk-roles: [writer, analyst, product-manager]
sk-compatible: [claude, cursor, codex, gemini]
---

# Docs (enterprise documentation wiki)

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

**Where this skill writes (exception to session-only Work layout):**

| Output | Location |
| --- | --- |

Do **not** treat the shared preamble line “not `agent configuration/`” as a ban on the
configured wiki path — that rule targets lifecycle reports (DISCUSSION/PLAN/…),
not the project documentation settings.location`.

## Purpose

Produce **real, standards-based documentation** for the project — not a thin
skim. This wiki is for humans (engineers, reviewers, new joiners, stakeholders)
recognized standards so it holds up in an enterprise setting:

| Document | Standard it follows |
|---|---|
| SRS (requirements) | **ISO/IEC/IEEE 29148** (supersedes IEEE 830) |
| Architecture | **arc42** (12 sections) + **C4** diagrams + **ISO/IEC/IEEE 42010** viewpoints + **4+1 views** |
| Architecture decisions | **ADR** (MADR/Nygard), one record per decision |
| Design descriptions (HLD/LLD) | **IEEE 1016-2009** design viewpoints; fed by `sk-basic-design`/`sk-detail-design` (`BASIC_DESIGN.md` / `DETAIL_DESIGN.md`) |
| API reference | **OpenAPI**/AsyncAPI when a spec exists (derive from it) |
| Guides (user-facing) | **Diátaxis** (tutorial / how-to / reference / explanation) |

### Documentation principles (apply throughout)

- **Docs-as-code:** the wiki lives in the repo, is versioned with the code,
  reviewed in the same PR, and rendered from a single markdown source of truth.
- **Address stakeholder concerns (ISO/IEC/IEEE 42010 / IEEE 1016):** organize
  architecture and design as **views** that answer specific **concerns** of
  named **stakeholders** — not a data dump. State stakeholders + concerns first.
- **Diátaxis separation:** never blend the four guide types; a tutorial is not a
  reference. Pick one purpose per page.
- **Single source, cite everything, no invention:** every claim traces to code
  or a session artifact; gaps are visible, not filled with plausible fiction.

## This is not a one-shot skim (depth gate — mandatory)

A credible doc set is authored **document-by-document**, each with its required
sections filled from real evidence. You MUST:

- Fill **every required section** of each in-scope document (list below). If a
  section does not apply, write `N/A` **with a one-line reason** — never delete
  it and never leave a heading empty.
- **Cite the source** (file/path/§) for each substantive claim. Where evidence
  is missing, write `Gap:` / `Unknown` and add it to the coverage matrix —
  **do not invent** behavior, requirements, or decisions.
- Assign stable IDs (`FR-001`, `NFR-001`, , `BR-001`) and keep a
  **traceability** thread: requirement → design → code/test.
- Populate the **Documentation coverage matrix** in `Home.md` (each document:
  status `complete` / `partial` / `gap` / `N/A` + owner + last-synced). A wiki
  with everything `complete` on the first pass over a non-trivial repo is a red
  flag — be honest about `partial`/`gap`.

Scale rule: small projects may mark whole documents `N/A (reason)` — but that is
an explicit, visible decision, not a silent omission.

Use `references/documentation-coverage-and-traceability.md` to record claim sources, stable IDs, stakeholder viewpoints, coverage status, freshness, rendered-output review, and next-owner handoff.

## Modes

| Mode | Use | Behavior |
|---|---|---|
| `full` | Doc set missing or a full rebuild is requested | Author every in-scope document to its standard. |
| `sk-sync` | Code changed | Update only the documents/sections a change affects (via `.docmap.md`). |

## Information architecture (the doc set)

Author the **markdown source tree** under the project documentation settings.location` (canonical
source; other formats render from it). Standard layout:

```
Home.md                         # landing: overview + document map + coverage matrix
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

Templates in `templates/`: `SRS`, `ARCHITECTURE`, `HLD`, `LLD`, ,
`API_REFERENCE`, `DATA_MODEL`, `RUNBOOK`, `GUIDE`, `WIKI_HOME`, `WIKI_PAGE`,
`DOCMAP`, plus `DOCX_OUTLINE` / `XLSX_STRUCTURE` for those formats.

### Reuse existing artifacts (do not re-derive)

Aggregate what the lifecycle already produced instead of inventing:
- **SRS** ← `BUSINESS_ANALYSIS.md` + `DISCUSSION.md` (stories, rules, AC, scope).
- **HLD** ← `BASIC_DESIGN.md`; **LLD** ← `DETAIL_DESIGN.md`.
- **ADRs** ← decisions recorded in sk-brainstorming/sk-planning gates.
- **Reference/workspaces** ← the scanner + code; **memory** for prior gotchas.
If a source artifact is missing, note the `Gap` and document from code evidence.

## Output format (resolve first)

Read the project documentation settings.format`; the **markdown tree is the canonical source**, the
others render from it (keeps `sk-sync` incremental). Keep `.docmap.md` always.

| Format | Organization | Built with | Sync unit |
|---|---|---|---|
| `markdown` | The doc tree above; cross-linked `.md`. | Write tool | file/section |
| `sk-docx` | **One controlled document** with a title page, TOC, and the doc set as parts (SRS, Architecture, HLD, LLD, ADRs, …) using Heading styles. | the **`sk-docx`** skill; see `templates/DOCX_OUTLINE.template.md` | heading section |
| `sk-xlsx` | **Workbook**: requirements register, traceability matrix, NFRs, ADR log, workspaces, data dictionary, coverage — tabular. | the **`sk-xlsx`** skill; see `templates/XLSX_STRUCTURE.template.md` | sheet/row |

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-preflight.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in ``artifacts/<task-id>/PROGRESS.md`` with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifact, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | [step-01-preflight.md](./steps/step-01-preflight.md) | Preflight (the project documentation settings + branch gate) |
| 02 | [step-02-author.md](./steps/step-02-author.md) | Author (full or sk-sync) |
| 03 | [step-03-render.md](./steps/step-03-render.md) | Render + docmap |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Outputs | The enterprise doc set under the project documentation settings.location` in the resolved `format`, with a coverage matrix in `Home.md`, ADRs, traceability IDs, and `.docmap.md`. |
| Safety | Read-only against project code (never execute it) except the bundled scanner. **Do NOT invent** requirements, behavior, or decisions — cite sources; mark `Gap`/`Unknown`. Never write secrets. Honor the branch gate. In `sk-sync`, touch only affected documents/sections. |

### Branch gate (mandatory, before writing)

- `main-only`: write the wiki **only** on the base/main branch. On a feature
  branch, do not touch it — report that sk-docs are refreshed on `main` and stop.
- `with-commit`: write on the current branch; when invoked from `complete`, **stage
  the wiki changes into the same commit** so they travel through the PR.

### Required artifacts (per in-scope document)

Each document must contain its standard sections (see its template); the core:

- **SRS** — Introduction (purpose, scope, product overview, definitions);
  References; Specific requirements (external interfaces; functional `FR-*`;
  usability; performance; database/data; design constraints; software system
  attributes: reliability/availability/security/maintainability/portability);
  Verification; Appendices incl. **traceability**.
- **Architecture (arc42 + ISO/IEC/IEEE 42010)** — 1 Introduction & Goals
  (**stakeholders + concerns**) · 2 Constraints · 3 Context & Scope · 4 Solution
  Strategy · 5 Building Block View (C4) · 6 Runtime View · 7 Deployment View ·
  8 Crosscutting Concepts · 9 Architecture Decisions (link ADRs) · 10 Quality
  Requirements · 11 Risks & Technical Debt · 12 Glossary.
- **HLD (IEEE 1016 high-level views)** — stakeholders/concerns; context,
  composition, logical, dependency, interface, information; data ownership.
- **LLD (IEEE 1016 detailed views)** — interface contracts, structure, data
  model (fields/types), interaction (sequences), validation/rules, state
  dynamics, algorithm, resource/concurrency, error handling.
- **ADR** — Context · Decision · Status · Consequences · Alternatives.
- **Reference/Operations/Guides** — per their templates.
- **`.docmap.md`** — required (every format): unit → source paths + last-synced.

## Workflow (detailed mechanics — order enforced by the step files)

### Common preflight
1. Read the project documentation settings. If `enabled: false`, stop. Resolve `format`.
2. Apply the **Branch gate**; stop if it forbids writing here.
3. Decide the in-scope doc set (mark out-of-scope documentation `N/A` with reason).

### Mode `full`
5. Author the markdown source **document by document**, each to its template and
   standard, filling every required section, citing sources, and assigning IDs.
6. Build the **coverage matrix** in `Home.md` (status/owner/last-synced per doc)
   and the ADR index; thread traceability (req → design → code/test).
7. **Render to `format`** if not markdown (html per DESIGN_SYSTEM.md; sk-docx via
   the `sk-docx` skill; sk-xlsx via the `sk-xlsx` skill).
8. Write `.docmap.md` with the current commit ().

### Mode `sk-sync`
5. Change set:  (or the task's files).
6. Map changed paths → affected documents/sections via `.docmap.md`; update
   **only** those, plus the coverage matrix and any new ADR the change implies.
   Re-run the scanner: add/remove workspace pages for added/removed projects.
7. Re-render only affected units; refresh `Last-synced`. Leave the rest intact.
8. If `sk-sync_strategy: with-commit` and invoked by `complete`, stage the changes.

## Quality Standards

- [ ] `format` resolved; the format's organization followed.
- [ ] Every in-scope document has all required sections (or `N/A` + reason).
- [ ] Requirements/decisions carry stable IDs; traceability thread present.
- [ ] Every substantive claim cites a source; gaps marked `Gap`/`Unknown`.
- [ ] `Home.md` has a coverage matrix reflecting real status (not all-green).
- [ ] `full` covers every project the scanner surfaces (per-workspace pages).
- [ ] `sk-sync` touched only affected documents/sections via `.docmap.md`.
- [ ] sk-docx/sk-xlsx built via the `sk-docx`/`sk-xlsx` skills; html self-contained.

## Reference

## Limitations

- Does NOT implement or modify project code.
- Does NOT invent requirements/decisions to fill a template — gaps stay visible.
- `sk-sync` is only as good as `.docmap.md`; run `full` first if it is missing.

## Boundary

**`sk-docs`** owns **enterprise documentation information architecture, standards-based document sets, traceability, and docs synchronization**. It does not own **code implementation, product requirements ownership, or unsupported publishing claims**; route those concerns to the appropriate specialist skill.

## When not to use

- When the request is outside `sk-docs`'s documented scope or another specialist is the primary owner.
- When the requested result would require unsupported format guarantees, fabricated evidence, or an unverified external claim.

## Required inputs

- documentation scope, stakeholders/concerns, source artifacts, standards, project documentation settings, freshness, and coverage expectations.
- State assumptions, evidence gaps, confidence, and limitations explicitly.

## Cross-skill handoffs

- sk-technical-writing-pro for editorial quality; sk-specify/sk-business-analysis for requirements; sk-architecture-patterns for architecture views; format skills for DOCX/PDF/XLSX outputs.
