# Simple Skills

A portable [Agent Skills](https://agentskills.io/) pack for use with the [`npx skills`](https://github.com/vercel-labs/skills) CLI.

## Layout

```text
skills/sk-<skill-name>/SKILL.md
```

This repository contains **222 independent skills**. Every skill uses the shared `sk-` prefix, and every `SKILL.md` has `name` and `description` frontmatter. Optional `references/`, `scripts/`, `templates/`, and `assets/` remain inside the skill that uses them.

## Install

```bash
# Browse
npx skills add truongnat/simple-skills --list

# Install one
npx skills add truongnat/simple-skills --skill sk-planning

# Install all
npx skills add truongnat/simple-skills --all
```

Use `--agent`/`-a` and `--global`/`-g` when the CLI target requires it. The repository contains no custom installer, runtime, profile system, session engine, or framework outside the standard skill directories.

## Skill format

```yaml
---
name: sk-my-skill
description: What the skill does and when to use it
---

# My Skill

Instructions for the agent, with optional skill-local resources.
```

Review skills before installing them, especially when a skill includes executable scripts.
