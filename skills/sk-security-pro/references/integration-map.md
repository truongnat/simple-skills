# Integration map — sk-security-pro

| Combined skill | Why | `sk-security-pro` owns | Other skill owns |
|----------------|-----|----------------------|------------------|
| **`sk-nestjs-pro`** | HTTP API | Threats, authz rules, validation policy | Guards, pipes, filters, module wiring |
| **`sk-nextjs-pro`** | Web surface | CSP, cookie strategy, Server Action abuse, env leakage | Routing, cache, middleware mechanics |
| **`sk-postgresql-pro`** | Data layer | RLS intent, least privilege | SQL, migrations, query patterns |
| **`sk-api-design-pro`** | Public contracts | Abuse cases, versioning, idempotency for sensitive ops | OpenAPI shape, pagination ergonomics |
| **`sk-auth-pro`** | Identity protocols | Session/JWT/OAuth threat framing | Provider wiring, token lifetimes in code |
| **`sk-react-pro`** / **`sk-react-native-pro`** / **`sk-flutter-pro`** | Client surface | XSS, deep links, secure storage policy | UI implementation |
| **`sk-testing-pro`** | Assurance | Abuse cases, security regression tests | CI layout, runners |
| **`sk-ci-cd-pro`** | Pipelines | Secrets in CI, fork PR policy, action pinning | YAML structure, matrix |
| **`sk-deployment-pro`** | Runtime exposure | TLS termination, WAF hints, secret mounts | Infra topology, rollout |
| **`sk-network-infra-pro`** | Segmentation, DNS, TLS path | SSRF/lateral-movement narrative | VPC/firewall specifics |

**Handoff:** **`sk-security-pro`** states **invariants and threats**; stack skills implement **wiring** without duplicating threat rationale.
