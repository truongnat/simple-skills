# Phase 8 — Documents, research and business upgrade

## Scope

This phase adds output-level validation and evidence discipline to representative Group 09 skills: golden fixtures, structural/rendered checks, source registers, citation freshness, reproducibility, market assumptions and documentation traceability.

## New focused packs

| Skill | New material |
|---|---|
| `sk-pdf-pro` | PDF integrity, text/table, visual, metadata, forms/OCR, round-trip and limitation checks |
| `sk-xlsx` | Coverage manifest, workbook structure, formulas, styles, data integrity, unsupported OOXML and reopen checks |
| `sk-pptx` | Slide coverage, narrative/layout, content, theme, export and limitation evidence |
| `sk-docx` | Text structure, pagination, tables/media, metadata, round-trip and unsupported-content checks |
| `sk-research` | Source/evidence register, method reproducibility, claim confidence, conflicts and handoff |
| `sk-web-research-pro` | Claim-to-source hierarchy, version/freshness, provenance and fact/inference labeling |
| `sk-market-research-pro` | Decision boundary, TAM/SAM/SOM assumptions, competitor framing, sensitivity and confidence |
| `sk-docs` | Standards, source traceability, stable IDs, coverage matrix, freshness and rendered-output review |

## Acceptance evidence

Each pack is linked from its owning skill and defines concrete golden-output or evidence-register checks. Existing format-specific templates, coverage manifests, research steps and documentation standards remain authoritative; these packs add reviewable acceptance evidence without claiming unsupported format guarantees.

## Validation run

| Check | Result |
|---|---|
| Catalog validator | PASS — 222 skills, 0 errors |
| Markdown fences | PASS — 0 unbalanced |
| Internal Markdown links | PASS — 0 broken |
| Local reference paths | PASS — 0 missing |
| Phase 8 focused packs | PASS — 8/8 linked and non-empty |
| JSON/YAML parse | PASS — 1 JSON and 3 YAML resources |
| Bundled JavaScript syntax | PASS — 24 files |
| Bundled shell syntax | PASS — 1 file |
| Existing Node test suite | PASS — 10 tests |
| `git diff --check` | PASS |
