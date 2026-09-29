# Code packaging — integration map

| Skill | When |
|-------|------|
| **`sk-deployment-pro`** | Digest promotion, rollout, rollback, environments — **after** artifact exists |
| **`sk-testing-pro`** | What runs in CI; flaky gates; coverage |
| **`sk-security-pro`** | OIDC trust, SBOM/signing policy, fork PR workflows, secret scanning |
| **`sk-ci-cd-pro`** | Workflow graph, concurrency, reusable workflows across repos |
| **`sk-docker-pro`** | Dockerfile depth, BuildKit, layer/cache tuning beyond basics |
| **`sk-javascript-pro`** / **`sk-cli-pro`** | npm publish, `bin`/CLI entry when shipping JS tools |
| **`sk-nestjs-pro`** / **`sk-nextjs-pro`** | Framework-specific Docker or standalone bundles |

**Boundary:** **`sk-code-packaging-pro`** owns **build reproducibility**, **artifact shape**, **registry push mechanics** in CI; **`sk-deployment-pro`** owns **runtime** lifecycle and traffic.
