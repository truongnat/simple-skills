# Caching — integration map

| Skill | When |
|-------|------|
| **`sk-deployment-pro`** | CDN deploy, cache purge, rollout, circuit breaker rollout. |
| **`sk-network-infra-pro`** | Edge, TLS, LB cache headers path, partition behavior. |
| **`sk-nextjs-pro`** / **`sk-react-pro`** | Data cache, SWR/React Query, RSC cache. |
| **`sk-postgresql-pro`** | Query shape, replicas, read-after-write vs replica lag. |
| **`sk-sql-data-access-pro`** | Fix queries before masking with cache. |
| **`sk-performance-tuning-pro`** | End-to-end latency and profiling. |
| **`sk-seo-pro`** | `Cache-Control` impact on crawl (stale content risk). |
| **`sk-api-design-pro`** | HTTP caching headers, cache-friendly contract semantics. |
| **`sk-security-pro`** | Cache poisoning, auth-aware keys, sensitive data — **`cache-security-and-isolation.md`**. |

**Boundary:** **`sk-caching-pro`** owns cache **architecture**, **consistency story**, **invalidation**, **failure degradation**, and **cost framing**; paired skills own framework/DB/security implementation details.
