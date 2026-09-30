# Audit & remediation — Nhóm 08: Databases & data access

**Ngày:** 2026-09-29
**Phạm vi:** 10 skill trong taxonomy Nhóm 08.

## Baseline findings

Baseline scanner ghi nhận 15 metadata field thiếu, 7/10 skill có `sk-tags` rỗng và 7/10 có `sk-roles` rỗng. Ba skill legacy cần boundary/canonical ownership rõ hơn:

- `sk-database-migration`
- `sk-postgresql-table-design`
- `sk-sql-optimization-patterns`

Một số database specialist đã có boundary tốt nhưng thiếu `Required inputs` hoặc `Cross-skill handoffs` theo contract chung.

## Remediation đã triển khai

- Chuẩn hóa metadata toàn bộ 10 skill: `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`.
- Bổ sung ownership boundary cho migration, PostgreSQL table design và SQL optimization.
- Bổ sung `When not to use`, `Required inputs` và `Cross-skill handoffs` cho các skill legacy.
- Làm rõ canonical handoff giữa:
  - `sk-postgresql-pro` và `sk-postgres-patterns`.
  - `sk-sql-data-access-pro` cho SQLite/local access.
  - `sk-database-migration` và `sk-deployment-pro`.
  - `sk-sql-optimization-patterns` và `sk-performance-tuning-pro`.
  - `sk-prisma-postgres` với PostgreSQL/ORM/provider boundaries.
  - MongoDB, Elasticsearch và Redis specialists với SQL/database-general guidance.
- Giữ nguyên SQL, MQL, Redis, Prisma và migration code examples vì đây là domain artifacts, không phải repo tooling.

## Verification

| Check | Result |
|---|---:|
| Skills kiểm tra | 10/10 |
| Contract errors | 0 |
| Empty tags/roles | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Repo-tooling hits ngoài fenced examples | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 08 đã đạt contract chung với Nhóm 06–07: metadata đủ để routing, database ownership rõ, inputs và handoffs được nêu, còn domain examples được giữ lại để bảo toàn giá trị hướng dẫn.
