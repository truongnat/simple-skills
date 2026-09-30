# MLOps evaluation and release gates

Use this reference to turn an MLOps design into reproducible release evidence. Keep model quality, data quality, serving reliability, cost, and rollback criteria separate.

## Gate matrix

| Gate | Example check | Release evidence |
|---|---|---|
| Reproducibility | Same code/data/environment reproduces artifact within tolerance | Versioned run and artifact digest |
| Data contract | Schema, null rate, range, freshness, and category checks pass | Data-quality report |
| Model quality | Offline metrics meet baseline and slice thresholds | Evaluation report with dataset version |
| Bias/safety | Protected or high-impact slices meet policy thresholds | Slice report and reviewer sign-off |
| Serving SLO | Latency, error rate, availability, and resource limits pass | Load/Canary metrics |
| Drift | Feature/prediction drift stays below alert threshold | Monitoring baseline and alert test |
| Rollback | Previous model and configuration can be restored | Timed rollback rehearsal |
| Cost | Inference/training cost stays within budget | Cost estimate and observed usage |

## Release scenarios

Test canary success, quality regression, schema break, feature staleness, dependency failure, model-server timeout, alert firing, and rollback. A model should not advance solely because aggregate accuracy improves; inspect critical slices and operational metrics.

## Incident evidence

Record model/version, data snapshot, feature-store version, serving configuration, input/output sample hashes, alert timestamp, impact window, decision owner, mitigation, rollback result, and follow-up action. Never log sensitive raw inputs unless explicitly approved and protected.
