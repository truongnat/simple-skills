# MLOps evaluation and release matrix

Use this matrix after the compact workflow when the task involves a high-risk claim. Fixtures must use synthetic identifiers and redacted values. The domain skill produces evidence; `sk-tester` executes tests, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` owns the final `pass`/`block`/`defer` decision.

| Scenario | Expected result | Evidence | Failure/limitation | Next owner |
|---|---|---|---|---|
| Reproducibility | The same code, data snapshot and config reproduce the control metric within tolerance. | Run manifest, hashes and metric comparison. | Unpinned data or dependency is a limitation. | sk-tester -> sk-verify-pro |
| Schema drift | Incoming schema changes are detected before serving and routed to a quarantine path. | Schema diff, alert and quarantine count. | Backward-compatible additions still require owner review. | sk-data-engineering-pro -> sk-verify-pro |
| Data drift | A declared drift threshold triggers investigation without automatic promotion. | Drift report, threshold config and decision. | Drift is a signal, not proof of model failure. | sk-review -> sk-verify-pro |
| Model regression | Candidate meets quality and slice-level guardrails against the frozen baseline. | Evaluation report and slice breakdown. | Aggregate improvement cannot mask a critical slice regression. | sk-tester -> sk-verify-pro |
| Canary rollback | A canary breach stops promotion and restores the prior model/version. | Canary metrics, rollback event and health check. | Rollback owner and trigger must be named. | sk-deployment-pro -> sk-verify-pro |
| Feature freshness | Feature age stays within SLA; stale features fail safe or are marked unavailable. | Freshness metrics and serving behavior. | Imputation policy must be explicit. | sk-data-engineering-pro -> sk-review |
| Serving SLO | Latency/error/throughput targets are measured under representative load. | Load report, percentile metrics and error budget. | Synthetic load does not prove peak production capacity. | sk-performance-tuning-pro -> sk-verify-pro |
| Alert thresholds | Alerts have threshold, owner, runbook and suppression policy; test firing is recorded. | Alert test event and runbook link. | Unowned alerts block release. | sk-review -> sk-verify-pro |

## Verification response shape

Return exactly:

- **Claim:** the bounded domain claim being assessed.
- **Criteria:** scenario rows and acceptance thresholds.
- **Evidence:** paths, commands, fixture IDs, timestamps and reviewer findings.
- **Limitations:** untested environments, assumptions, stale inputs or residual risk.
- **Next owner:** `sk-tester`, `sk-review`, `sk-review-pr`, the named domain owner, or `sk-verify-pro`.

Do not claim final release status from this matrix; hand the packet to `sk-verify-pro`.
