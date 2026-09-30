# GitHub Actions workflow validation matrix

Use this reference before adopting a workflow template. Validate syntax and policy in a safe branch; do not test against production deployment targets without the required approvals.

## Validation cases

| Case | Expected result |
|---|---|
| YAML parse and expression expansion | Workflow loads without syntax or unresolved-expression errors |
| Pull request from fork | Secrets are unavailable by default; workflow does not expose privileged actions |
| Permissions review | `contents` and package/deploy permissions are least-privilege and job-scoped |
| Matrix failure | One failed combination produces a visible failed check; unrelated jobs behave as intended |
| Concurrency | Superseded runs cancel only where safe; production deploys are serialized |
| Cache miss/corruption | Job rebuilds safely without trusting unverified cache content |
| Artifact retention | Required artifacts are uploaded with bounded retention and sensitive files excluded |
| Action pinning | Actions use approved tags/SHAs and are reviewed on update |
| Deployment approval | Environment protection blocks unapproved production promotion |
| Rollback | Failed rollout has a documented, tested recovery path |
| Reusable workflow inputs | Required inputs, secrets, and outputs are type-correct and documented |

## Review evidence

Keep the rendered workflow, permission table, event/branch matrix, secret assumptions, action versions, sample logs, failure behavior, and rollback owner with the change. Treat a green test job as insufficient evidence for deployment safety.
