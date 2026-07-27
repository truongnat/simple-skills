# BA skills (consolidated)

Catalog of **51 BA slash-style capabilities** mapped onto a small set of
first-party skills. Prefer these consolidated skills over inventing 51 separate
folders.

Install profile: `--profile ba` (includes `core` + BA skills below).

## Flow

`Ý tưởng → tài liệu → sơ đồ → kiểm thử → bàn giao`

Use existing lifecycle skills where they already cover the step:

| Stage | Prefer |
| --- | --- |
| Unclear goals / options | `brainstorming` then `specify` / `discover` mode |
| Stories / rules / AC (lifecycle) | `business-analysis` |
| System design | `basic-design` → `detail-design` |
| Wiki SRS/Architecture | `docs` |
| Test cases | `tester` (+ `ba-test` later) |
| Worker split | `delegate_worker.py` (Rules pack) |

## Consolidated skills (P0 shipped)

| Skill | Modes (aliases) | Session artifact |
| --- | --- | --- |
| `specify` | `prd`, `roadmap`, `discover`, `urd`, `brd`, `prd-epic`, `srs` | `PRD.md` / `ROADMAP.md` / `DISCOVER.md` / `URD.md` / `BRD.md` / `PRD_EPIC.md` / `SPEC_SRS.md` |
| `biz-model` | `sequence`, `activity`, `activity-swimlane`, `bpmn`, `state`, `erd`, `usecase-diagram` (+ format `mermaid` \| `plantuml`) | `MODEL.md` |
| `story-spec` | `usecase`, `userstory`, `ac` | `USECASE.md` / `USER_STORIES.md` / `AC.md` |
| `gap-analysis` | `gap` | `GAP.md` |
| `user-flow` | `user-flow` | `USER_FLOW.md` |
| `api-ba` | `api-doc`, `api-map` (P0); `api-assess` / `api-design` stubs | `API_BA.md` |

## Full 51 → target map

### 1. Product planning (3)

| Alias | Target |
| --- | --- |
| `/prd` | `specify` mode=`prd` |
| `/roadmap` | `specify` mode=`roadmap` |
| `/discover` | `specify` mode=`discover` (or `research` when evidence-heavy) |

### 2. Elicitation & spec (6)

| Alias | Target |
| --- | --- |
| `/brainstorm` | `brainstorming` |
| `/urd` | `specify` mode=`urd` |
| `/brd` | `specify` mode=`brd` |
| `/prd-epic` | `specify` mode=`prd-epic` |
| `/srs` | `specify` mode=`srs` (session); `docs` for wiki SRS |
| `/reverse-doc` | **P1** — use `excel-doc-convert` / office skills until dedicated skill |

### 3. Business diagrams (11)

| Alias | Target |
| --- | --- |
| `/sequence` … `/usecase-diagram` | `biz-model` with matching `diagram` mode |
| `/d2-erd`, `/d2-activity`, `/d2-architect`, `/dbdiagram` | **P1** — note in `MODEL.md` Limitations; prefer Mermaid/PlantUML offline |

### 4. Use case & story (3)

| Alias | Target |
| --- | --- |
| `/usecase` | `story-spec` mode=`usecase` |
| `/userstory` | `story-spec` mode=`userstory` (or deepen via `business-analysis`) |
| `/ac` | `story-spec` mode=`ac` |

### 5. Screen design (5)

| Alias | Target |
| --- | --- |
| `/user-flow` | `user-flow` |
| `/wireframe-*`, `/prototype-html`, `/figma` | **P1/P2** |

### 6. API (7)

| Alias | Target |
| --- | --- |
| `/api-doc`, `/api-map` | `api-ba` |
| `/api-assess`, `/api-design`, `/api-checklist`, `/api-test`, `/api-readiness` | **P1** (extend `api-ba` modes) |

### 7. Testing (3)

| Alias | Target |
| --- | --- |
| `/test-cases` | `tester` |
| `/test-checklist`, `/playwright-gen` | **P1** |

### 8. Quality control (5)

| Alias | Target |
| --- | --- |
| `/gap` | `gap-analysis` |
| `/ask` | Confirm-first / Ask methods in `SKILL_PREAMBLE` (no separate skill) |
| `/cr` | **P1** — extend `gap-analysis` or new mode |
| `/dashboard`, `/kg` | **P2** |

### 9. Handoff & ops (8)

| Alias | Target |
| --- | --- |
| `/export`, `/preview` | `docs` + office skills (**P1** polish) |
| `/delegate` | `delegate_worker.py` |
| `/jira`, `/confluence`, `/meet`, `/userguide`, `/update-overview` | **P1/P2** |

## Rules

1. One **canonical** artifact per concern; link IDs (`FR-001`, `US-001`, `AC-001`, `BR-001`).
2. Headings English; prose follows `settings.language`.
3. Confirm-first on Blocking unknowns.
4. Commit Work with `session.sh commit` after writing session artifacts.
