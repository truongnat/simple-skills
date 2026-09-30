# Git worktree isolation lifecycle

| Stage | Evidence |
|---|---|
| Assess | Current branch/status, dirty files, concurrency risk and whether isolation materially helps |
| Choose | In-place, new branch, or worktree decision with least-disruptive rationale |
| Create | Worktree path, branch/ref, base commit and repository identity recorded |
| Execute | Scope stays inside the selected worktree; no hidden stash, reset or checkout of user changes |
| Verify | Tests/diff run in the intended worktree; HEAD and status are captured |
| Handoff | Commit/ref, worktree path, cleanup owner and unresolved changes are explicit |
| Cleanup | Remove only after confirming no needed uncommitted files or active work depend on it |

If the workspace is dirty and a modifying isolation action is needed, summarize the changes and obtain confirmation before stash, switch, reset, checkout or cleanup.
