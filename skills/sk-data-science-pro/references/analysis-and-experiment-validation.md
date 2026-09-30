# Data science analysis and experiment validation

Start with a decision, estimand, population, unit of analysis, sampling frame, and baseline. Preserve notebook/code version, dataset snapshot, exclusions, transformations, and random seeds.

| Case | Expected evidence |
|---|---|
| Missingness | Mechanism and imputation/exclusion impact are reported |
| Leakage | Features unavailable at decision time are excluded or flagged |
| Multiple comparisons | Correction or pre-registered primary metric is stated |
| Imbalanced target | Stratified metrics and baseline comparison are shown |
| A/B test | Randomization, sample ratio, power/uncertainty, and stopping rule are documented |
| Segment effect | Important slices and interaction uncertainty are reported |
| Outlier | Rule is justified; robust and unfiltered sensitivity are compared |
| Reproduction | Independent rerun reaches expected tolerance |

Do not present a p-value without effect size and uncertainty. Separate exploratory findings from confirmatory claims and record decisions made from the analysis.
