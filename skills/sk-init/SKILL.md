---
name: sk-init
description: Initialize or refresh project context for an agent. Use at the start of a new project or when the project structure, conventions, or goals have changed.
sk-kind: process
sk-version: 0.1.0
sk-tags: [context,repository]
sk-roles: [researcher]
sk-compatible: [claude, cursor, codex, gemini]
---

# Initialize Project Context

Inspect the repository before making changes and create or refresh a concise project reference in the project’s normal documentation location. Do not install a custom runtime or modify agent configuration unless the user explicitly asks.

## Steps

1. Identify the repository root, primary language/framework, package manager, entry points, tests, and build commands.
2. Read the project README, contribution guidance, and relevant configuration files.
3. Record only verified facts: structure, commands, conventions, important constraints, and open questions.
4. Ask before changing project-wide settings, dependencies, authentication, or generated files.
5. Keep the reference short and update it when facts change; do not duplicate the whole README or source tree.

## Output

Return the files inspected, the verified project facts, the commands used to verify them, and any missing information that blocks the next task.
