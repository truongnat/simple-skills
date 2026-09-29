# SQL data access — integration map

| Skill | Combine when |
|-------|----------------|
| **`sk-postgresql-pro`** | Server Postgres, migrations, `EXPLAIN (ANALYZE)`, RLS, vacuum/replication, concurrency at scale. |
| **`sk-data-analysis-pro`** | Post-export pandas, charts, Parquet pipelines, statistical validation. |
| **`sk-security-pro`** | Injection in apps, credential handling, PII in exports, path trust. |
| **`sk-nestjs-pro`** / **`sk-nextjs-pro`** | ORM and app-layer connection lifecycle — this skill for **raw** SQLite in scripts/tests. |
| **`sk-performance-tuning-pro`** | Very large exports, memory pressure, batching I/O. |
| **`sk-content-analysis-pro`** | User attached `.db` without SQL goal — clarify schema vs narrative summary. |

**Boundary:** **`sk-sql-data-access-pro`** = **SQLite file workflows** + portable SQL habits; **`sk-postgresql-pro`** = **production server** Postgres.
