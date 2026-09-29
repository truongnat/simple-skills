# Prompt Engineering Integration Map

## sk-ai-integration-pro

- **When**: The prompt is part of a broader agent with tools, RAG, or memory.
- **Ownership split**:
  - `sk-prompt-engineering-pro`: Prompt design, optimization, versioning.
  - `sk-ai-integration-pro`: Agent architecture, tool selection, RAG, memory, orchestration.

## sk-agent-evaluation-pro

- **When**: Measuring prompt quality with metrics and regression tests.
- **Ownership split**:
  - `sk-prompt-engineering-pro`: Designing prompt variants.
  - `sk-agent-evaluation-pro`: Measuring quality, building datasets, statistical testing.

## sk-testing-pro

- **When**: Integrating prompt tests into CI.
- **Ownership split**:
  - `sk-prompt-engineering-pro`: Prompt design and expected outputs.
  - `sk-testing-pro`: CI structure, test pyramid, flaky test management.
