---
name: sk-xlsx
description: >-
  Create, inspect, edit, and validate Excel .sk-xlsx files with strict
  supported-lossless coverage manifests (Python/openpyxl). Use when the user
  mentions Excel, spreadsheet, .sk-xlsx, workbook, cells, or formulas.
---

# XLSX

## Purpose

Work with modern Excel `.sk-xlsx` files using the Python CLI. Every create/edit
must prove supported-lossless coverage (`coverage_ratio == 1.0`) before publish.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in ``artifacts/<task-id>/PROGRESS.md`` with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifact, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | [step-01-init.md](./steps/step-01-init.md) | Init (setup + ledger) |
| 02 | [step-02-build.md](./steps/step-02-build.md) | Build (inspect / create / edit) |
| 03 | [step-03-verify.md](./steps/step-03-verify.md) | Verify (coverage gate) |

## Contract (mandatory)

This skill is a **hard contract**. Obey it before any other action. Do NOT treat as optional. Do NOT skip required artifacts.

| Field | Requirement |
|-------|-------------|
| Inputs | .sk-xlsx path and/or JSON create/edit spec; optional manifest path. |
| Outputs | .sk-xlsx deliverable for create/edit plus coverage manifest JSON with coverage_ratio=1.0. |
| Safety | Do NOT publish when unsupported OOXML parts/macros/OLE/signatures exist. Do NOT claim full Excel format support. Do NOT silently drop sheets/cells. Use sk-office-common helpers beside this skill. |

### Required artifacts

#### `coverage.json`
- Required: yes
- **format** (required, string): Must be sk-xlsx.
- **operation** (required, string): inspect | create | edit | validate
- **coverage_ratio** (required, number): Must equal 1.0 before publish.
- **items** (required, array): Coverage inventory entries with status preserved/transformed/unsupported/skipped.

### Reference

## Workflow (detailed mechanics — order enforced by the step files)

   skill's `requirements.txt`. Do not install into global Python.
2. Prefer CLI over ad-hoc scripts.
3. For edits of unknown files: `inspect` first; stop if unsupported.
4. Write via `create`/`edit` (atomic temp → validate → publish).
5. Keep the coverage manifest with the deliverable.

## Commands

```bash
```

On Windows, replace `.venv/bin/python` with `.venv/Scripts/python.exe`.

### Create spec example

```json
{
  "properties": {"title": "Sales", "creator": "agent"},
  "sheets": [
    {"title": "Data", "rows": [["Name", "Qty"], ["A", 1], ["B", 2]]}
  ]
}
```

## Limitations

- `.xls` not supported.
- Macros/OLE/signatures block writes.
- Formula recalculation via LibreOffice is optional; absence is `skipped`, not a pass.

## Output

Produce a document/media artifact with input and output paths, coverage/quality checks, unsupported-content limitations, validation evidence, and delivery notes.
