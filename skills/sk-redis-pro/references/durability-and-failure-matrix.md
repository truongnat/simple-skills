# Redis durability and failure matrix

Choose Redis as cache, coordination store, stream, or primary data store explicitly. The required durability and recovery evidence differs by role.

| Scenario | Expected evidence |
|---|---|
| Cache miss/stampede | Bounded recomputation, jittered TTL/lock, origin protection |
| Eviction/memory pressure | Policy, key-size budget, hit-rate impact, alert and degraded behavior |
| Primary failover | Client reconnect, replica promotion, acceptable data-loss window |
| AOF/RDB recovery | Restore rehearsal, corruption/partial-write behavior, recovery time |
| Duplicate stream delivery | Consumer idempotency, pending-entry recovery, ack policy |
| Lock expiry/process pause | Fencing or ownership check prevents stale holder side effects |
| Pub/Sub disconnect | Message-loss expectation is explicit; durable stream used when required |
| Hot key/slow command | Key distribution, command complexity, latency and mitigation evidence |

Record persistence mode, replication, backup retention, recovery owner, key namespace, TTL semantics, and whether loss is acceptable.
