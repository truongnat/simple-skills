# DOCX outline spec

> A Word document is **one linear file**, not a link tree. Organize the same
> wiki content as a single document with a heading hierarchy + table of
> contents. Build it with the `docx` skill (office-common / python-docx).
> Deliverable: `<location>/<Project>-wiki.docx` (+ the markdown source pages
> the docmap tracks, so `sync` stays incremental).

## Document structure (heading order)

1. **Title page** — project name, generated date, source commit.
2. **Table of contents** — generated from Heading 1/2 styles.
3. **H1 Overview (80/20)** — the vital 20%, as a short bulleted section.
4. **H1 Architecture** — components/boundaries/data flow; embed a diagram
   image (render Mermaid to PNG) or a component table.
5. **H1 Workspaces** — one **H2 per app/package** (surfaced by the scanner),
   each with stack, entry points, commands, responsibilities.
6. **H1 Flows** *(optional)* — one H2 per key flow.
7. **H1 Guides** *(optional)* — setup / how-to.
8. **Appendix: Sources & freshness** — a table of section → source paths →
   last-synced commit (mirrors `.docmap.md`).

## Formatting rules

- Use built-in styles (`Heading 1/2/3`, `Title`, `Normal`) so the TOC and
  navigation work — never fake headings with bold text.
- Tables for structured data (workspaces, commands, contracts).
- Each H1/H2 opens with its 80/20 overview line before detail.
- Keep images embedded (no external links; office files must be self-contained).

## Sync granularity

Word is monolithic: `sync` regenerates the `.docx` from the updated markdown
source, but uses the docmap to re-derive only the **sections** whose sources
changed; unchanged section text is carried over verbatim.
