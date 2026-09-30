# Git safe-change and review gates

| Gate | Evidence before proceeding |
|---|---|
| Scope | Current branch, base branch, clean/dirty state, intended files and user-owned changes recorded |
| History risk | Shared branch status, protection rules, merge strategy and force-push policy known |
| Change | `diff`, staged file list, diff check and secret scan reviewed; unrelated files excluded |
| Review | Required reviewers/owners, test evidence, conflict status and risk summary documented |
| Recovery | Revert/reset choice, backup/ref, rollback owner and expected blast radius stated |
| Publish | Exact remote/ref, commit trailer/policy, push result and post-push status captured |

Prefer the least destructive operation. A green local test does not authorize a history rewrite or deployment; authorization and repository state are separate gates.
