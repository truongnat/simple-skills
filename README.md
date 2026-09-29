# Simple Skills

> **222 reusable Agent Skills** for coding, architecture, product, design, security, data, and operations — installable with `npx skills`.

[Agent Skills](https://agentskills.io/) is an open format that lets coding agents use focused, reusable, and verifiable instruction sets. This repository follows one simple principle: **every skill should be independent, discoverable, easy to install, and explicit about its boundaries**.

---

## Why Simple Skills?

- **Portable** — works with agents that support the Agent Skills standard.
- **Composable** — install one skill, a focused set, or the entire collection.
- **Predictable** — every skill lives under `skills/sk-<name>/` and includes a `SKILL.md`.
- **Self-contained** — references, scripts, templates, and assets stay with the skill that uses them.
- **Tool-friendly** — the `sk-` prefix makes skills easy to search, route, and automate.

## Quick Start

### 1. Browse available skills

```bash
npx skills add truongnat/simple-skills --list
```

### 2. Install one skill

```bash
npx skills add truongnat/simple-skills --skill sk-planning
```

### 3. Install the entire collection

```bash
npx skills add truongnat/simple-skills --all
```

Depending on your agent setup, add `--agent` / `-a` to select a target agent and `--global` / `-g` to install at user scope.

## Explore by Use Case

| Use case | Suggested skills |
| --- | --- |
| **Planning & execution** | `sk-planning`, `sk-executing-pro`, `sk-execution`, `sk-verification` |
| **Architecture & systems** | `sk-clean-architecture`, `sk-system-design-pro`, `sk-microservices-pro`, `sk-api-design-pro` |
| **Code quality & debugging** | `sk-clean-code-architecture-pro`, `sk-review`, `sk-systematic-debugging-pro`, `sk-test-driven-development-pro` |
| **Frontend & UI/UX** | `sk-frontend-design-pro`, `sk-ui-ux-system-pro`, `sk-design-system-pro`, `sk-a11y-design-pro` |
| **Backend & frameworks** | `sk-nodejs-backend-patterns`, `sk-fastapi-pro`, `sk-nestjs-pro`, `sk-spring-boot-pro` |
| **Data & AI** | `sk-data-analysis-pro`, `sk-data-engineering-pro`, `sk-ai-agents-pro`, `sk-prompt-engineering-pro` |
| **Security & reliability** | `sk-security-pro`, `sk-api-security-pro`, `sk-nextjs-security-scan`, `sk-deployment-pro` |
| **Git & workflow** | `sk-git-operations-pro`, `sk-git-worktree-pro`, `sk-parallel-agents-pro`, `sk-router-pro` |

> These are only starting points. Browse the full collection in [`skills/`](./skills/).

## Repository Structure

```text
simple-skills/
├── skills/
│   ├── sk-<skill-name>/
│   │   ├── SKILL.md              # Main contract and agent instructions
│   │   ├── references/            # Deep-dive documentation, when needed
│   │   ├── scripts/               # Supporting scripts, when needed
│   │   ├── templates/             # Output templates, when needed
│   │   └── assets/                # Local assets, when needed
│   └── ...
├── README.md
└── .gitignore
```

Each skill should remain an independent unit. Avoid hidden dependencies between skill directories; when coordination is required, document it in the skill's boundary or workflow section.

## Skill Format

```yaml
---
name: sk-my-skill
description: What the skill does and when it should be used
sk-kind: domain
sk-version: 0.1.0
sk-tags: []
sk-roles: []
sk-compatible: [claude, cursor, codex, gemini]
aliases: []
---
```

The frontmatter is followed by the agent-facing instructions:

```markdown
# My Skill

## Boundary
State what this skill owns and what it does not own.

## When to use
Describe the signals or situations that should activate the skill.

## Workflow
Define the steps, required inputs, and verification criteria.
```

### Naming Conventions

- The directory name and the frontmatter `name` must match.
- Skill names use the `sk-` prefix, for example `sk-api-design-pro`.
- Internal resources use paths relative to the skill directory.
- Do not use legacy `x-*` metadata; current metadata keys use the `sk-*` prefix.

## Check Before Opening a Change

Review the changed files and run the checks available in your environment:

```bash
git diff --check
git status --short
find skills -mindepth 1 -maxdepth 1 -type d -name 'sk-*' | wc -l
```

## Contributing

1. Create or update a `skills/sk-<skill-name>/` directory.
2. Keep the `SKILL.md` contract concise; move deep-dive material into `references/` when appropriate.
3. Check all internal links and bundled resources.
4. Run the validator before committing.
5. In your pull request, explain the new skill or the behavior that changed.

## Safety Note

Read `SKILL.md` and review every script before installing or executing a skill from an external source. A skill may contain instructions that access files, run commands, or call tools — use only what is appropriate for your environment and trust level.

---

**Simple Skills** — small, clear, composable instructions for building reliable agent workflows.
