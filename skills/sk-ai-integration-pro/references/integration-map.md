# AI integration — integration map

| Combined skill | Why | `sk-ai-integration-pro` owns | Other skill owns |
|----------------|-----|----------------------------|------------------|
| **`sk-security-pro`** | Abuse, data exfiltration | Prompt boundaries, tool validation, logging hygiene | Threat model, infra hardening |
| **`sk-testing-pro`** | Quality gates | Eval datasets, mock LLM, contract tests on structured output | Broader CI strategy |
| **`sk-caching-pro`** | Cost/latency | Prompt/embedding cache policies | Invalidation, Redis |
| **`sk-api-design-pro`** | External API | AI feature endpoints, SSE/WebSocket | REST semantics, versioning |
| **`sk-postgresql-pro`** | pgvector | Schema for vectors, ANN indexes | SQL tuning |
| **`sk-deployment-pro`** | Rollout | Feature flags for model swaps | Traffic management |
| **`sk-ci-cd-pro`** | Pipelines | Secret scanning, no keys in logs | Workflow YAML |

**Handoff:** After integration patterns are set, **`sk-security-pro`** should review data flows for PII and injection before production enablement.
