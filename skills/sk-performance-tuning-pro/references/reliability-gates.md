# Performance reliability gates

| Gate | Evidence |
|---|---|
| Baseline | Workload, environment, version, p50/p95/p99, throughput, error rate |
| Bottleneck | Profile/trace or resource metric linking change to bottleneck |
| Capacity | Headroom at expected peak and degraded dependency behavior |
| Tail latency | p95/p99 and timeout/error behavior, not only average latency |
| Regression | Same benchmark before/after with variance and warm-up stated |
| Cost | CPU/memory/network/storage cost or operational trade-off |
| Recovery | Backpressure, timeout, circuit breaker, and rollback behavior |

Reject optimizations that improve a synthetic benchmark while degrading correctness, tail latency, cost, or operability.
