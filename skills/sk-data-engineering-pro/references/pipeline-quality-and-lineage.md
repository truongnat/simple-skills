# Data pipeline quality and lineage matrix

Treat each dataset as a contract with owner, grain, schema, privacy class, freshness SLA, retention, and downstream consumers. Store run/version identifiers with quality results.

| Failure | Expected behavior/evidence |
|---|---|
| Duplicate delivery | Idempotent key or deduplication prevents double counting |
| Late/out-of-order event | Watermark policy is explicit; replay/backfill is safe |
| Schema change | Compatibility check blocks or versions the change |
| Null/range/category drift | Quality gate reports affected partitions and owner |
| Partial batch failure | Checkpoint/resume or atomic publish prevents partial truth |
| Backfill | Historical run is isolated, auditable, and does not corrupt current data |
| PII exposure | Classification, masking, access policy, and audit evidence exist |
| Consumer lag | Lag/SLA alert and capacity response are defined |

Minimum output: lineage from source to published table/topic, run status, row/volume deltas, quality results, freshness, incident owner, and rollback/rebuild path.
