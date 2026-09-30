---
name: sk-init
description: Initialize or refresh project context for an agent. Use at the start of a new project or when the project structure, conventions, or goals have changed.
sk-kind: domain
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

## Boundary


**`sk-init`** owns verified project/workspace context at task entry: inspected files, repository state, constraints, inputs, artifact location, assumptions, and blockers that affect the next safe action.

It does **not** own product discovery, architecture design, diagnosis, implementation, or acceptance decisions. Route unclear direction to `sk-discussing-pro`, execution sequencing to `sk-planning`, and domain work to the direct specialist.

**Primary artifact:** an initialization record listing verified facts, commands/evidence, missing information, and the proposed next owner. **Handoff:** pass the factual context to `sk-discussing-pro`, `sk-planning`, or the direct specialist without silently changing scope.

## Required inputs

- request, objective, constraints, current artifact, stakeholders, acceptance criteria, and desired output.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-planning or sk-executing-pro for lifecycle orchestration; sk-specify or BA skills for requirements artifacts; sk-review for quality findings; sk-verify-pro for canonical claim-to-evidence decisions (sk-verification is a compatibility facade only).
