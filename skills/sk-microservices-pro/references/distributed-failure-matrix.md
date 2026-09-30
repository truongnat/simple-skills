# Distributed service failure matrix

Review topology and interactions as failure boundaries, not only as component diagrams. For each call or event record owner, timeout, retry, idempotency key, ordering, consistency, and operator evidence.

| Failure | Expected behavior/evidence |
|---|---|
| Slow dependency | Deadline is propagated; caller degrades or fails explicitly |
| Retry storm | Bounded exponential backoff, jitter, retry ownership, and load evidence |
| Duplicate event | Consumer is idempotent and reconciliation is observable |
| Out-of-order event | Version/sequence policy or compensating action is explicit |
| Partial saga | Durable state, compensation, operator resume, and stuck-state alert |
| Schema mismatch | Consumer-driven contract or compatibility gate blocks unsafe rollout |
| Network partition | Consistency trade-off and user-visible behavior are documented |
| Service overload | Admission control, queue/backpressure, and saturation signal exist |
| Correlation loss | Trace/context propagation allows end-to-end diagnosis |

Do not use distributed transactions by default. State the ownership boundary, consistency promise, recovery path, and evidence required before adding a broker, saga, or service split.
