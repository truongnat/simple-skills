# Phase 5 — Architecture, API & frameworks upgrade

## Scope

This phase adds compatibility, distributed-failure, schema-evolution, and framework verification packs to representative Group 02–03 skills. Existing mature references remain authoritative where they already cover the same concern.

## New focused packs

| Skill | New material |
|---|---|
| `sk-api-design-pro` | Breaking-change classification, consumer inventory, contract fixtures, idempotency, deprecation and rollback evidence |
| `sk-microservices-pro` | Timeouts, retry storms, duplicate/out-of-order events, sagas, schema mismatch, partitions, overload and tracing |
| `sk-graphql-pro` | Schema evolution, deprecation, nullability/enums, N+1, query budgets, authZ and federation evidence |
| `sk-spring-boot-pro` | Controller, security, service, repository, transaction, configuration, integration and actuator checks |
| `sk-django-pro` | Model/migration, DRF, auth/CSRF, query count, admin, async/signals and operations checks |
| `sk-nextjs-pro` | Router/runtime/version compatibility, server/client boundaries, cache invalidation and hosting smoke tests |

## Acceptance evidence

Each new pack is linked from its owning skill and describes a realistic scenario, failure boundary, expected evidence, and handoff to adjacent ownership such as security, testing, deployment, database, or networking.

## Validation run

| Check | Result |
|---|---|
| Catalog validator | PASS — 222 skills, 0 errors |
| Markdown fences | PASS — 0 unbalanced |
| Internal Markdown links | PASS — 0 broken |
| Local reference paths | PASS — 0 missing |
| JSON/YAML parse | PASS — 1 JSON and 3 YAML resources |
| Bundled JavaScript syntax | PASS — 24 files |
| Bundled shell syntax | PASS — 1 file |
| `git diff --check` | PASS |
