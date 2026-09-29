# NestJS — integration map

When you use **`sk-nestjs-pro`**, you often need these skills together. Clarify **who owns what** to avoid duplicated or conflicting advice.

| Combined skill | Why | `sk-nestjs-pro` owns | Other skill owns |
|----------------|-----|-------------------|------------------|
| **`sk-postgresql-pro`** | Migrations, RLS, indexes, SQL policies | ORM wiring, transactions, `SET LOCAL` in request path | `CREATE POLICY`, `EXPLAIN`, pool/session semantics |
| **`sk-auth-pro`** | JWT/session/OAuth models | Guards, Passport strategies, `ExecutionContext` | Protocol choice, token lifecycle, threat framing |
| **`sk-security-pro`** | Threat model, OWASP-style review | Input validation surface, error leakage, secure defaults | End-to-end abuse cases, infra secrets |
| **`sk-testing-pro`** | Unit/e2e structure | `TestingModule`, mocking providers, e2e app bootstrap | Assertion style, coverage strategy |
| **`sk-api-design-pro`** | REST/GraphQL contract shape | Controllers, DTOs, OpenAPI decorators | Resource modeling, versioning narrative |
| **`sk-deployment-pro`** | Rollout and rollback | Health checks, graceful shutdown hooks | Runtime topology, traffic switching |
| **`sk-ci-cd-pro`** | Pipeline YAML | Build/test commands for Nest apps | Workflow structure, secrets in CI |
| **`sk-caching-pro`** | Redis/CDN | Interceptor-level caching, cache keys per route | Invalidation policy, stampede protection |
| **`sk-microservices-pro`** | Multi-service boundaries | Nest microservice module patterns | Broader distributed design |
| **`sk-graphql-pro`** | GraphQL schema/resolvers | `@nestjs/graphql` wiring, resolver DI | Federation and domain schema depth |

**Handoff hint:** After Nest-specific wiring is settled, name the **next** skill for SQL (`sk-postgresql-pro`) or auth protocol (`sk-auth-pro`) before deep implementation.
