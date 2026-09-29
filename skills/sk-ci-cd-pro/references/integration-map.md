# CI/CD — integration map

| Skill | When |
|-------|------|
| **`sk-docker-pro`** | Image build, layer cache, BuildKit, digest references in deploy. |
| **`sk-deployment-pro`** | Promotion stages, rollback, migration sequencing with releases. |
| **`sk-testing-pro`** | Job ordering, flakes, coverage gates, contract/e2e depth. |
| **`sk-security-pro`** | OIDC trust, fork policy, Sigstore/SBOM gates, secret scanning. |
| **`sk-git-operations-pro`** | Triggers, protected branches, tags, merge queue semantics. |
| **`sk-code-packaging-pro`** | Publish wheels/containers/npm from pipeline outputs. |
| **`sk-postgresql-pro`** | Migration jobs, backwards-compatible schema rollout. |
| **`business-analysis-pro`** | Rare: regulatory gates / approval RACI mapped to env protection. |

**Boundary:** **`sk-ci-cd-pro`** owns **workflow graph**, **runner execution model**, **secrets/OIDC wiring at YAML level**, **pipeline reliability patterns**, and **artifact handoff**; **`sk-deployment-pro`** owns **runtime rollout** beyond the workflow step.
