# Collaboration, PRs, and safety

## Pull requests

- **Small PRs** — easier review, less merge conflict; link **issue** or ticket.
- **Description** — **what**, **why**, **how to test**; screenshots for UI.
- **Draft PRs** — early feedback without merge pressure.

## Reviews

- **Approve** vs **comment** — blocking issues vs nits; use **CODEOWNERS** when the repo supports it.

## Hooks and CI

- **Pre-commit** / **husky** — format, lint, test fast feedback; keep **fast** or developers skip.
- **CI** — same commands as local when possible (**`sk-testing-pro`**, **`sk-code-packaging-pro`**).

## Secrets

- **Never** commit `.env`, API keys, or **private** deploy keys — use **`sk-security-pro`** patterns; rotate if leaked.

## Conflict with **`sk-deployment-pro`**

- **`sk-git-operations-pro`** = **VCS** workflow and hygiene.
- **`sk-deployment-pro`** = **runtime** promotion, K8s, rollback — orthogonal.
