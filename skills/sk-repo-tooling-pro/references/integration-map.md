# Repo tooling — integration map

| Skill | When |
|-------|------|
| **`sk-skills-self-review-pro`** | Full bundle audit, authoring checklist, narrative on top of **`analyze-skills --markdown`**. |
| **`sk-web-research-pro`** | External facts — not replaceable by `query-kb`. |
| **`sk-ci-cd-pro`** | Wiring **`validate-skills`**, **`build`**, **`verify-kb`** into pipelines, matrix Node, caches. |
| **`sk-deployment-pro`** | Runner sizing, secrets, cross-repo promotion of KB artifacts. |
| **`sk-security-pro`** | API keys for embeddings / external search; log redaction. |
| **`documentation-persistence`** rule | When KB docs added — INDEX + **build-kb** / **verify-kb** per repo policy. |

**Handoff:** **`sk-repo-tooling-pro`** defines **which CLI steps** apply; **`sk-ci-cd-pro`** implements **YAML and runner** policy for your organization.
