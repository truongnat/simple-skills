# Phase 3 — Data, AI & agent systems upgrade

## Scope

This phase adds scenario-based evaluation, grounding, lineage, reproducibility, and tool-failure guidance to the highest-impact Group 04 skills. Existing mature reference bundles are preserved; new content is not duplicated where a skill already owns the same evaluation concern.

## New focused packs

| Skill | New material |
|---|---|
| `sk-ai-agents-pro` | Tool misuse, prompt injection, retry loops, state recovery, memory leakage, multi-agent conflict, human handoff, cost/latency gates |
| `sk-fullstack-rag-pro` | Answerable/unanswerable, stale/conflicting corpus, ACL, hybrid retrieval, noisy context, malformed ingestion, groundedness and citation evidence |
| `sk-data-engineering-pro` | Idempotency, late events, schema evolution, quality drift, partial failure, backfill, PII, consumer lag, lineage evidence |
| `sk-data-science-pro` | Missingness, leakage, multiple comparisons, imbalance, A/B design, segments, outliers, reproducibility and uncertainty |
| `sk-machine-learning-pro` | Tiny-batch overfit, split integrity, baselines, robustness, fairness, reproducibility, export/runtime and MLOps handoff |
| `sk-agent-evaluation-pro` | Golden-set composition, correctness, groundedness, safety, tool behavior, robustness, latency/cost, regression gates |

`sk-ai-integration-pro`, `sk-ai-design-pro`, `sk-content-analysis-pro`, `sk-data-analysis-pro`, `sk-prompt-engineering-pro`, and `sk-mlops-pro` already contain mature reference bundles or were upgraded in previous phases; they remain covered by catalog validation without duplicate packs.

## Acceptance evidence

Every new pack is linked from its owning skill and defines inputs, expected evidence, failure cases, and a release or handoff boundary. Validation must pass catalog contracts, local links, Markdown fences, resource parsing, and relevant syntax/tests.
