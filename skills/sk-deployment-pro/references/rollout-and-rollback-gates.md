# Deployment rollout and rollback gates

Record artifact digest, environment, traffic scope, schema coupling, SLO/error budget, health signals, approval owner, and rollback trigger before promotion.

| Stage | Gate evidence |
|---|---|
| Preflight | Artifact provenance, config diff, migration compatibility, backup/restore readiness |
| Canary | Small traffic slice, startup/readiness, error rate, latency tail, dependency health |
| Promotion | SLO within budget, logs/traces stable, no alert regression, owner acknowledges |
| Rollback | Known-good artifact/config, reverse-traffic or rollout action, data compatibility |
| Post-rollback | Service health, queued work, cache state, incident record, follow-up fix |

Prefer rollback when the previous version remains schema-compatible and the failure is isolated. Prefer forward-fix when an irreversible expand/contract migration has already made the old binary unsafe. Never claim zero downtime without measuring connection, queue, and data-layer behavior.
