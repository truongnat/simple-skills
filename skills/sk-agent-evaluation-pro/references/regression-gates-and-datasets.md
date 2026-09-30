# Agent evaluation regression gates and datasets

A golden set should mix normal, boundary, ambiguous, adversarial, tool-failure, and abstention cases. Each case needs an expected rubric, not necessarily one exact string.

## Gate design

| Dimension | Gate evidence |
|---|---|
| Correctness | Rubric score, reference/critic agreement, and critical-case minimum |
| Groundedness | Claim-to-source trace or explicit abstention |
| Safety | No critical policy bypass, secret leakage, or unauthorized action |
| Tool behavior | Correct tool, schema, arguments, ordering, and stop condition |
| Robustness | Paraphrase, noise, multilingual, and injection variants |
| Latency/cost | p50/p95 and token/tool budget against baseline |
| Regression | Versioned dataset, prompt/model/config diff, score delta, and reviewed failures |

Block release on critical-case failures even when aggregate score improves. Store evaluator version and sample-level results so a score can be audited.
