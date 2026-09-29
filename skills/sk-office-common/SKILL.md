---
name: sk-office-common
description: Shared Python helpers for office document skills. Use when working with the bundled XLSX, DOCX, PPTX, or PDF helper modules and their validation/publish utilities.
---

# Office Common

Use the bundled  package as shared implementation support for the office skills in this repository.

## Available helpers

- Coverage manifests and validation errors
- Semantic fingerprints
- Atomic publish (temporary output, validate, then replace)
- OOXML ZIP inventory helpers
- Optional tool detection for LibreOffice, Tesseract, and Poppler

Import from the package rather than duplicating these helpers in an individual office skill.

## Output

Produce a document/media artifact with input and output paths, coverage/quality checks, unsupported-content limitations, validation evidence, and delivery notes.
