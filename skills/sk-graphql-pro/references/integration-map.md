# GraphQL — integration map

| Skill | Combine when |
|-------|----------------|
| **`sk-api-design-pro`** | REST coexistence, versioning, error semantics alignment. |
| **`sk-security-pro`** | Introspection abuse, authZ gaps, query cost attacks. |
| **`sk-nestjs-pro`** | Code-first vs schema-first; guards on resolvers. |
| **`sk-postgresql-pro`** | SQL performance, RLS — not in GraphQL layer alone. |
| **`sk-testing-pro`** | Operation tests, snapshot SDL, integration against test DB. |
| **`sk-caching-pro`** | APQ, CDN edge caching for GET queries, Redis response cache semantics. |

**Boundary:** **`sk-graphql-pro`** owns schema/resolver contract; DB and HTTP gateway details split per sibling skills.
