# Machine learning training and evaluation gates

Record data snapshot, split policy, code/dependency versions, seed, compute, baseline, metrics, and artifact digest. A model is not ready because training loss decreases.

| Gate | Expected evidence |
|---|---|
| Tiny-batch overfit | Model can learn a small known batch; failure is diagnosed before long training |
| Split integrity | No entity/time leakage across train/validation/test |
| Baseline | Simple baseline and confidence interval are reported |
| Quality | Primary and slice metrics meet decision thresholds |
| Robustness | Perturbation, missing input, distribution shift, or adversarial cases are assessed |
| Fairness/safety | Relevant subgroup and harmful-error analysis is documented |
| Reproducibility | Rerun stays within declared tolerance |
| Export/runtime | Serialized artifact matches serving runtime and latency contract |
| Rollback handoff | Registry/version/monitoring owner is explicit; defer operations to MLOps |

Keep training, evaluation, and deployment evidence separate so an offline score cannot mask serving or data-quality risk.
