# Integration map — sk-clean-code-architecture-pro

| Combined skill | Why | This skill owns | Other skill owns |
|----------------|-----|-----------------|------------------|
| **`sk-testing-pro`** | Safe refactors | Boundary-level tests; characterization plan | Runners, CI, pyramid, flake policy |
| **`sk-git-operations-pro`** | Reviewable diffs | Commit granularity for mechanical moves | Git mechanics |
| **`sk-nestjs-pro`** / **`sk-react-pro`** / **`sk-nextjs-pro`** | Framework wiring | Keep domain free of framework leakage | Module/DI/API specifics |
| **`sk-typescript-pro`** | Types at boundaries | Ports/adapters typing patterns | Compiler/tsconfig details |
| **`sk-postgresql-pro`** / **`sk-sql-data-access-pro`** | Persistence | Repository boundaries; no ORM in domain rules | SQL tuning, migrations |
| **`sk-api-design-pro`** | Contracts | DTO vs domain mapping at HTTP boundary | OpenAPI, versioning |
| **`sk-deployment-pro`** | Release | N/A for pure structure | Rollout when architecture implies service split |
| **`sk-feedback-pro`** | Review output | Structure of architecture review | Severity / people framing |
| **`sk-business-analysis`** | Rare | Align module boundaries with domain language | Requirements ownership |

**Boundary:** **`sk-clean-code-architecture-pro`** owns **dependency direction**, **module semantics**, **refactor sequencing**, and **structural trade-offs**; framework and infra skills own **tool-specific** implementation truth.
