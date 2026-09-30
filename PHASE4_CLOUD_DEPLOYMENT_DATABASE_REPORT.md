# Phase 4 — Cloud, deployment & databases upgrade

## Scope

This phase adds operational gates for rollout/rollback, schema migration, PostgreSQL design, Redis durability, Kubernetes reliability, and AWS readiness. Existing detailed references in CI/CD, Docker, networking, infrastructure-as-code, and SQL skills remain authoritative and are not duplicated.

## New focused packs

| Skill | New material |
|---|---|
| `sk-deployment-pro` | Preflight, canary, promotion, rollback, forward-fix and post-rollback evidence |
| `sk-database-migration` | Expand/contract, online indexes, backfill, locks, compatibility, restore and invariant checks |
| `sk-postgresql-table-design` | Grain, constraints, access paths, concurrency, growth, privacy and migration review |
| `sk-redis-pro` | Cache stampede, eviction, failover, persistence, streams, locks, Pub/Sub and hot keys |
| `sk-kubernetes-pro` | Scheduling, probes, rollout, traffic draining, security, state, observability and failure gates |
| `sk-aws-pro` | Security, reliability, performance, cost, operations and sustainability readiness evidence |

## Acceptance evidence

Each pack is linked from its owning skill. The material separates design intent from operational proof and states when to hand off to testing, security, networking, infrastructure-as-code, or MLOps specialists.
