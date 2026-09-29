# Agent Evaluation Integration Map

## sk-ai-integration-pro

- **When**: The evaluation is part of building or iterating the agent itself.
- **Ownership split**:
  - `sk-agent-evaluation-pro`: Metric design, dataset, statistical testing.
  - `sk-ai-integration-pro`: Agent architecture, tool selection, RAG, memory.

## sk-prompt-engineering-pro

- **When**: Comparing prompt variants or designing templates for eval.
- **Ownership split**:
  - `sk-agent-evaluation-pro`: Measuring prompt quality with metrics.
  - `sk-prompt-engineering-pro`: Designing the prompt variants themselves.

## sk-testing-pro

- **When**: General software testing strategy and CI structure.
- **Ownership split**:
  - `sk-agent-evaluation-pro`: LLM-specific evals (metrics, datasets, tracing).
  - `sk-testing-pro`: Unit tests, integration tests for non-LLM code, test pyramid.

## sk-security-pro

- **When**: Safety red-teaming beyond agent output evaluation.
- **Ownership split**:
  - `sk-agent-evaluation-pro`: Automated red-team scoring, safety metrics.
  - `sk-security-pro`: Infrastructure hardening, threat modeling, pentesting.

## sk-ci-cd-pro

- **When**: Pipeline design, deployment gates, artifact management.
- **Ownership split**:
  - `sk-agent-evaluation-pro`: What to evaluate and how to score.
  - `sk-ci-cd-pro`: Pipeline structure, gating logic, artifact publishing.
