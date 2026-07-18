# XLSX workbook spec

> A spreadsheet is **tabular, sheet-organized** — not prose pages. Reshape the
> wiki content into sheets of rows/columns. Build it with the `xlsx` skill
> (office-common / openpyxl). Deliverable: `<location>/<Project>-wiki.xlsx`
> (+ the markdown source the docmap tracks, so `sync` stays incremental).

## Sheets (one concern per sheet)

| Sheet | Purpose | Columns |
|---|---|---|
| `Overview` | 80/20 summary | Aspect, Summary, Source |
| `Workspaces` | one row per app/package | Path, Type, Stack, Entry point, Commands, Responsibility, Source |
| `Architecture` | components & boundaries | Component, Responsibility, Depends on, Entry/boundary, Source |
| `APIs` *(optional)* | contracts/endpoints | Surface, Operation, Input, Output, Auth, Source |
| `Flows` *(optional)* | key flows as steps | Flow, Step #, Actor, Action, Result, Source |
| `Docmap` | freshness/index | Wiki unit, Sheet, Source paths, Last-synced |

## Formatting rules

- Row 1 = bold header; freeze the header row; set sensible column widths.
- One fact per row; no merged narrative cells. Put prose in `Summary`/
  `Responsibility` columns, kept short.
- Every content sheet has a `Source` column citing the code path — same honesty
  rule as the other formats (no invented behavior; mark `Unknown`).
- Keep a `Docmap` sheet mirroring `.docmap.md` for freshness tracking.

## Sync granularity

`sync` updates only the **rows/sheets** whose source paths changed (a new app =
a new `Workspaces` row + any per-app sheet; a removed app = mark its row
removed). Re-write the `Docmap` sheet's Last-synced.
