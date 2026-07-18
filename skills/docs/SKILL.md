---
name: docs
description: >-
  Maintain a wiki-style project documentation tree. Two modes: full (write the
  whole wiki in one pass) and sync (update only pages affected by a code
  change). Honors rules.docs in settings. (Hard contract in this SKILL.md —
  MUST follow.)
---

# Docs (project wiki)

## Language (do this first)

**Re-read `.agents/settings.yaml` now** — do not reuse a `language` value cached
earlier in this session. Write every wiki page and reply in that `language`
(`en` or `vi`); keep code, identifiers, paths, commands, and section keys
unchanged. A direct instruction in the current user request overrides the file.

## Memory (read first)

Before writing, read `.agents/memory/INDEX.md` and open entries whose hook
matches the area being documented; reuse recorded decisions/gotchas instead of
re-deriving them. If none apply, continue.

## Purpose

Keep a durable, human-facing **wiki** that explains the project — architecture,
each app/package, key flows, and setup — and keep it in step with the code.
Unlike `.agents/PRJ_REFERENCE.md` (agent-facing context) this wiki is for
people. Location, format, and sync strategy come from `rules.docs` in settings.

The **content** is the same across formats (the 80/20 knowledge below), but the
**organization and mechanism differ per output type** — a spreadsheet and a
Word doc are not a link tree. `rules.docs.format` is one of `markdown`, `html`,
`docx`, or `xlsx`; resolve it first and follow that format's mechanics
(**Output format** section below).

## Modes

| Mode | Use | Behavior |
|---|---|---|
| `full` | Wiki missing or a full rebuild is requested | Cover the whole repo and (re)write every unit. |
| `sync` | Code changed | Update only the units affected by the change; add/remove units for added/removed projects. |

## Output format (resolve first)

Read `rules.docs.format` and follow that type's organization. The **markdown
page tree is always the canonical source of truth**; `html`, `docx`, and `xlsx`
are **rendered from it** — this is what keeps `sync` incremental (diff the
source, re-render only affected units). Always keep `.docmap.md` regardless of
format.

| Format | Organization | Built with | Addressable unit (for sync) |
|---|---|---|---|
| `markdown` | Multi-file **page tree** with cross-links (`Home.md`, `architecture.md`, `workspaces/<name>.md`, `flows/`, `guides/`). The deliverable itself. | Write tool + `templates/WIKI_HOME`, `WIKI_PAGE` | page (`.md` file) |
| `html` | Same page tree rendered to **linked `.html` pages** + one shared `styles.css`; nav/link map on `index.html`. Enterprise theme with short `.ss-*` classes; Tailwind CDN. | Render per `.agents/DESIGN_SYSTEM.md` (self-contained, theme-aware) | page (`.html` file) |
| `docx` | **One linear Word document** with Heading styles + TOC (not a link tree). See `templates/DOCX_OUTLINE.template.md`. | The **`docx` skill** (office-common / python-docx) | section (H1/H2) |
| `xlsx` | **Workbook of sheets** (Overview, Workspaces, Architecture, APIs, Flows, Docmap) — tabular rows, not prose. See `templates/XLSX_STRUCTURE.template.md`. | The **`xlsx` skill** (office-common / openpyxl) | sheet / row |

Format-specific rules:

- **markdown / html:** one unit = one page. `sync` rewrites only changed pages;
  html additionally re-renders those pages and leaves `styles.css` untouched
  unless the theme changed. HTML must be self-contained and accessible per
  `.agents/DESIGN_SYSTEM.md`.
- **docx:** the document is monolithic, so `sync` regenerates the `.docx`, but
  uses the docmap to re-derive only the **sections** whose sources changed and
  carries unchanged section text over. Use built-in Heading styles so the TOC
  works; embed images (Mermaid → PNG); keep it self-contained.
- **xlsx:** content is **reshaped into rows/columns** — every content sheet has
  a `Source` column. `sync` touches only the affected **sheets/rows** (new app =
  new `Workspaces` row + per-app sheet; removed app = mark its row removed).
- All formats keep the **80/20 overview first** (top page / first H1 / `Overview`
  sheet) and a freshness record (page footer / appendix / `Docmap` sheet).

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | `rules.docs` (enabled, location, format, sync_strategy), `rules.branch`, repo source/config, `.agents/PRJ_REFERENCE.md` when present, the change set for `sync` (git diff or task scope), existing wiki + `.docmap.md`. |
| Outputs | Under `rules.docs.location` (default `.agents/wiki/`): the wiki in the resolved `rules.docs.format` (see **Output format**), plus `.docmap.md` (unit → source paths + last-synced commit). The markdown page tree is the canonical **source**; `html`/`docx`/`xlsx` are rendered from it so `sync` stays incremental. |
| Safety | Read-only against project code (never execute it) except running the bundled read-only scanner. Do NOT invent behavior — cite source files; mark unknowns. Never write secrets. Respect the branch gate below. Do NOT rewrite unaffected pages in `sync` mode. |

### Branch gate (mandatory, before writing)

Read `rules.docs.sync_strategy` and `rules.branch`:

- `main-only`: the wiki may be written **only** on the base/main branch. If the
  working tree is on a feature branch, **do not touch the wiki** — report that
  wiki updates are deferred to `main` and stop.
- `with-commit`: write the wiki on the current branch. When invoked from `done`,
  **stage the wiki changes into the same commit** as the task so docs travel
  through the PR.

### Required artifacts

#### Canonical source: markdown page tree (all formats)
Always author/keep the markdown tree under `rules.docs.location` — it is the
single source of truth that `html`/`docx`/`xlsx` render from:
- `Home.md` — landing page: 80/20 overview of the whole project + a link map to
  every page. First thing a reader opens.
- `architecture.md` — components, boundaries, data flow (diagram when useful).
- `workspaces/<name>.md` — one page per project surfaced by the scanner, each
  with its own stack, entry points, commands, and responsibilities.
- `flows/<name>.md`, `guides/<name>.md` — optional; only when they add value.
- Every page: an **Overview (80/20)** block at the top, then detail, then a
  footer: `Sources:` (the code paths it describes) and `Last-synced: <commit>`.

#### Rendered artifact (when `format` ≠ markdown)
- `html`: linked `.html` pages + shared `styles.css` per `.agents/DESIGN_SYSTEM.md`.
- `docx`: one `<Project>-wiki.docx` per `templates/DOCX_OUTLINE.template.md`,
  built with the **`docx`** skill.
- `xlsx`: one `<Project>-wiki.xlsx` per `templates/XLSX_STRUCTURE.template.md`,
  built with the **`xlsx`** skill.

#### `.docmap.md`
- Required: yes (every format). Maps each addressable unit (page / section /
  sheet-row) to the source paths/globs it documents, plus the repo commit the
  wiki was last synced to. Without it, `sync` cannot know what a diff affects.

## Workflow

### Common preflight
1. Read `rules.docs`. If `enabled: false`, stop (report disabled). Resolve
   `format` and follow the **Output format** mechanics for it.
2. Apply the **Branch gate** above; stop if it forbids writing here.
3. Resolve coverage deterministically — never enumerate from a workspace config:
   ```bash
   bash .agents/skills/init/scripts/scan_workspaces.sh
   ```
   Classify each surfaced directory's stack yourself (any ecosystem).

### Mode `full`
4. Build/refresh the **markdown source tree**: seed pages from `templates/` and
   fill from repo evidence (and `.agents/PRJ_REFERENCE.md` when present). One
   `workspaces/<name>.md` per surfaced project. Keep the 80/20 overview first.
5. **Render to `format`** if not markdown: html (per DESIGN_SYSTEM.md), docx
   (via the `docx` skill using `DOCX_OUTLINE`), or xlsx (via the `xlsx` skill
   using `XLSX_STRUCTURE`). Reshape content to that format's units.
6. Write `.docmap.md`: every unit → the source paths it covers; set
   `Last-synced` to the current commit (`git rev-parse --short HEAD`).
7. Cite sources; mark anything uncertain as `Unknown` rather than inventing it.

### Mode `sync`
4. Determine the change set: `git diff --name-only <Last-synced>..HEAD` (or the
   task's changed files when invoked from `done`).
5. Map changed paths → affected **units** via `.docmap.md`. Update **only**
   those in the markdown source. Re-run the scanner: add a unit for any new
   project, mark a removed project's unit as removed/stale.
6. **Re-render only the affected units** into `format` (markdown/html: rewrite
   those pages; docx: regenerate the doc, re-deriving changed sections only;
   xlsx: update the affected sheets/rows). Refresh each unit's freshness record
   and the top-level `Last-synced` in `.docmap.md`. Leave the rest untouched.
7. If `sync_strategy: with-commit` and invoked by `done`, stage the wiki changes
   so they are committed together with the task.

## Quality Standards

- [ ] `format` resolved from settings; the format's organization was followed
      (page tree / html pages / docx outline / xlsx sheets).
- [ ] The 80/20 overview comes first (top page / first H1 / `Overview` sheet).
- [ ] Every content unit records its source(s) and a `Last-synced` commit
      (page footer / appendix table / `Source` column / `Docmap` sheet).
- [ ] `full` covers every project the scanner surfaces (one unit per workspace).
- [ ] `sync` touched only the units the diff affects (via `.docmap.md`), plus
      add/remove for added/removed projects.
- [ ] docx/xlsx built via the `docx`/`xlsx` skills; html self-contained per
      `.agents/DESIGN_SYSTEM.md`.
- [ ] No invented behavior; unknowns are marked; no secrets in pages.
- [ ] Branch gate honored (no wiki writes off `main` when `main-only`).

## Reference

`agents/openai.yaml` mirrors this contract for tooling. This SKILL.md is authoritative.

## Limitations

- Does NOT implement or modify project code.
- Does NOT replace `.agents/PRJ_REFERENCE.md` (agent context) — this is the
  human wiki.
- `sync` is only as good as `.docmap.md`; if it is missing, run `full` first.
