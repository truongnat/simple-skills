# Integration map — sk-performance-tuning-pro

| Combined skill | Why | This skill owns | Other skill owns |
|----------------|-----|-----------------|------------------|
| **`sk-postgresql-pro`** | Query latency | When to index, batch, paginate, paginate shapes | SQL, plans, migrations, RLS |
| **`sk-caching-pro`** | Hit rate / stampede | Cache layer choice, TTL vs staleness narrative | Redis/CDN ops, eviction policy detail |
| **`sk-network-infra-pro`** | Tail at edge | CDN/cache headers awareness, latency vs hops | VPC, firewall rules, capacity planning |
| **`sk-algorithm-pro`** | Complexity | Picking lower-complexity structures after profiling | Formal proofs |
| **`sk-testing-pro`** | Regressions | Perf budgets, regression scenarios | Test layout, fixtures |
| **`sk-repo-tooling-pro`** | Repeatability | Scripted benchmarks / CI hooks | Pipeline wiring |
| **`sk-nestjs-pro`** / **`sk-nextjs-pro`** | Framework hot paths | Measurement placement, tracing hooks | Framework APIs, RSC/server split |
| **`sk-websocket-pro`** / **`sk-stream-rtc-pro`** | Real-time backpressure | Latency under sustained streams | Protocol semantics |
| **`sk-docker-pro`** / **`sk-deployment-pro`** | Runtime limits | CPU/mem impact on tail latency | Orchestration, rollout |

**Handoff:** When bottleneck is purely **business rules** or **requirements**, route to **`business-analysis-pro`** for trade-offs — **`sk-performance-tuning-pro`** stays on measurable system behavior.
