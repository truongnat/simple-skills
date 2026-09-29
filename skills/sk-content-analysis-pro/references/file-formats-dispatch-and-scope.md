# Scope: analysis vs authoring; file-format dispatch

## Single skill, clear boundary (avoid “pdf vs pdf-reading” duplication)

This repo uses **one** multimodal skill — **`sk-content-analysis-pro`** — for **reading, inspecting, and reporting** on user-provided content. It does **not** own **authoring** or **mutating** files (writing PDFs, building slide decks, filling Excel templates).

| If the user wants… | Primary skill |
|---------------------|---------------|
| Summarize, extract, compare, OCR, scene breakdown, evidence report | **`sk-content-analysis-pro`** |
| Turn findings into BRD / requirements / decisions | **`sk-business-analysis`** |
| **Create** or **edit** spreadsheets, charts, pivot tables programmatically | **`sk-data-analysis-pro`** |
| Resize, convert, composite **images** as artifacts (not semantic “what’s in this image?”) | **`sk-image-processing-pro`** |
| Numeric EDA on CSV / Parquet / DB exports | **`sk-data-analysis-pro`** |
| **Query** local `.db` / **SQL** (schema, safe `SELECT`) | **`sk-sql-data-access-pro`** |
| **PostgreSQL** server, migrations, RLS, tuning | **`sk-postgresql-pro`** |

## Quick dispatch: extra formats (attach / path)

| Format | Read / analyze | Typical libraries / notes |
|--------|----------------|---------------------------|
| **SQLite** (`.sqlite`, `.db`) | Schema discovery, row sampling, aggregate questions | `sqlite3` (stdlib), **never** execute untrusted SQL from users without review |
| **Parquet** / **Feather** | Column stats, head, dtypes | `pandas`, `pyarrow` |
| **Password-protected Office** (`.docx`, `.xlsx`, `.pptx`) | Do not guess passwords; ask user to unlock or export; analysis only **after** decryption |
| **CSV** / TSV | Preview, dtypes, missingness | `pandas` — deep statistics → **`sk-data-analysis-pro`** |
| **PDF** | Text vs scan vs mixed; OCR limits | Same skill; choose extraction path per file; MarkItDown is optional but recommended as a first-pass converter when available (no separate “pdf-only” skill in this repo) |
| **Office docs** (`.docx`, `.xlsx`, `.pptx`) | Convert to Markdown before summary/extraction | Prefer bundled `analyze-doc` / MarkItDown when available; ask before installing optional tooling; hand structured tables to **`sk-data-analysis-pro`** when math matters |
| **Jupyter** (`.ipynb`) | JSON structure — cells, outputs; “what did this notebook do?” | Parse as JSON or `nbformat`; large outputs → **sample** cells; execution **order** matters |
| **YAML** / **TOML** | Config / infra as text | Parse with `yaml` / `tomllib` (Py 3.11+) — **secrets** often here → **`sk-security-pro`** |
| **OCR** (pytesseract) | Image text extraction | **Python** `pytesseract` requires **system** Tesseract (`apt`/`brew` **install** `tesseract-ocr`) — **pip alone is not enough** |

## Why this table exists

Agents can land on the right **workflow** without two overlapping skills for “read PDF.” **Manipulation** (merge PDFs, redact, build workbooks) belongs in implementation skills or **`sk-data-analysis-pro`** / **`sk-image-processing-pro`**, not in **`sk-content-analysis-pro`**.
