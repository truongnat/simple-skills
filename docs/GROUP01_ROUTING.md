# Group 01 Routing Matrix

Choose one primary owner. Supporting skills may be invoked only when the primary owner explicitly hands off to them.

| User intent / condition | Primary skill | Supporting / next | Do not select as primary |
|---|---|---|---|
| Empty directory / greenfield | `sk-scaffold` | `sk-init` | `sk-init` before greenfield guard |
| Existing repo context | `sk-init` | `sk-sync` if stale/drifted | `sk-scaffold` |
| Unknown root cause | `sk-investigate` | `sk-sync`, domain debugger | implementation skill first |
| Idea is unclear | `sk-brainstorming` or `sk-discussing-pro` | `sk-business-analysis` | `sk-planning` |
| Need US/BR/AC and feasibility challenge | `sk-business-analysis` | design skills | `sk-specify` as a replacement |
| Need one document by mode (PRD/BRD/URD/SRS/roadmap) | `sk-specify` | `sk-business-analysis` when lifecycle AC is needed | `sk-to-prd-pro` |
| Already agreed context; create PRD GitHub issue without re-interview | `sk-to-prd-pro` | `sk-to-issues-pro` | `sk-specify` for GitHub submission |
| Existing PRD/epic; make vertical backlog slices | `sk-to-issues-pro` | `sk-planning` | `sk-to-prd-pro` |
| User journey | `sk-user-flow` | `sk-basic-design` | full wireframe skill |
| Visual / technical design | `sk-basic-design` → `sk-detail-design` | `sk-planning` | planning before design decision |
| Clear small change, ≤3 independently verifiable cards | `sk-quick-fix` | `sk-sync` → `sk-executing-pro` | full BA/design path |
| New planned implementation | `sk-executing-pro` | `sk-review` | `sk-execution` |
| Legacy TASKS/EXECUTION session | `sk-execution` | `sk-review` | `sk-executing-pro` simultaneously |
| Post-implementation code review | `sk-review` | `sk-verify-pro` → `sk-done` | `sk-review-pr` unless a PR/diff is the object |
| PR/MR/branch diff review | `sk-review-pr` | `sk-verify-pro` → `sk-done` | `sk-review` as a duplicate review |
| Full completion proof | `sk-verify-pro` | `sk-done` | `sk-verification` simultaneously |
| Lightweight proof summary with no full artifact | `sk-verification` | `sk-done` if applicable | `sk-verify-pro` unless full proof is needed |
| Close a verified task | `sk-done` | documentation sync | closure before verification |

## Upgrade triggers for `sk-quick-fix`

Upgrade to `sk-business-analysis` / design / `sk-planning` when any condition holds:

- public API, schema, migration, authentication, authorization, or data retention changes;
- more than three independently verifiable outputs;
- product, UX, or stakeholder policy is ambiguous;
- no falsifiable acceptance criterion and verification method can be written;
- change crosses a service boundary or introduces a new dependency.

## Routing invariants

- Never invoke both owners in an overlap pair for one task.
- A supporting skill must receive the primary artifact and stable trace IDs.
- External side effects (`gh issue create`, commits, releases) require the owning skill's explicit contract and user-visible result.
- A completion claim is invalid until `sk-verify-pro` or an explicitly declared lightweight verification result has recorded evidence.
