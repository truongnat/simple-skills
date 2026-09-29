# Deployment — integration map

| Skill | When |
|-------|------|
| **`sk-testing-pro`** | CI gates, test layers, flaky policy — quality pre-promote |
| **`sk-security-pro`** | OIDC deploy, secrets, signing, fork PR pipelines, SBOM admission |
| **`sk-postgresql-pro`** | Migration ordering, expand/contract, locking under deploy |
| **`sk-code-packaging-pro`** | Immutable image/wheel build before promotion |
| **`sk-git-operations-pro`** | Tags, release branches, merge hygiene |
| **`sk-ci-cd-pro`** | Workflow graph, concurrency, reusable deploy jobs |
| **`sk-network-infra-pro`** | LB, DNS, TLS, topology for traffic shift / multi-region |
| **`sk-nextjs-pro`** / **`sk-nestjs-pro`** | Framework-specific deploy targets (Vercel, Node containers) |
| **`sk-electron-pro`** / **`sk-tauri-pro`** | Desktop release channels and auto-update |
| **`sk-caching-pro`** | CDN cache invalidation, rollout interaction with edge cache |
| **`sk-api-design-pro`** | Contract compatibility across rolling deploys |

**Boundary:** **`sk-deployment-pro`** owns **promotion topology**, **release strategies**, **runtime rollout**, and **operational rollback narrative**; **`sk-ci-cd-pro`** focuses **pipeline YAML mechanics** when not strategy-specific.
