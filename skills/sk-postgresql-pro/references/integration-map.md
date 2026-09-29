# PostgreSQL — integration map

| Combined skill | Why | `sk-postgresql-pro` owns | Other skill owns |
|----------------|-----|----------------------|------------------|
| **`sk-nestjs-pro`** / **`sk-nextjs-pro`** | App talks to Postgres | Policies, migrations, query plans | ORM APIs, connection in request, serverless pool quirks |
| **`sk-sql-data-access-pro`** | SQLite locally vs Postgres; portable SQL | MVCC/types/portability gaps vs server Postgres | Embedded file DB scripts |
| **`sk-deployment-pro`** | Migrations in prod | Ordering, locks, `CONCURRENTLY`, rollback SQL | Pipeline gates, secrets for DB URLs |
| **`sk-security-pro`** | Data protection | Least privilege roles, RLS, encryption at rest awareness | App-level authz, logging policy |
| **`sk-auth-pro`** | Identity | RLS with `current_setting` / JWT claims mapped to DB | Token validation outside DB |
| **`sk-caching-pro`** | Reduce DB load | Query correctness, invalidation boundaries | Cache keys, TTL, Redis |
| **`sk-testing-pro`** | CI databases | Fixtures, transactions per test, templates | Test runner config |
| **`sk-data-analysis-pro`** | Analytics export | `COPY`, read-only replicas for heavy SELECT | pandas / notebooks |
| **`sk-performance-tuning-pro`** | End-to-end latency | Query shape, N+1, pool saturation narrative | Flame graphs outside DB |

**Handoff:** After schema and policies are clear, **`sk-deployment-pro`** owns *when* migrations run; **`sk-postgresql-pro`** owns *what* SQL runs safely.
