---
name: sk-tool-discovery
description: >-
  Capability-first discovery of available local tools, connectors, and runtime
  affordances. Use before verification, review, or automation when tool choice
  must be based on actual availability rather than remembered names.
sk-kind: process
sk-version: 0.1.0
sk-roles: [developer, maintainer]
sk-tags: [tooling, cli, routing]
sk-compatible: [claude, cursor, codex, gemini]
---


# tool-discovery

## Purpose

Detect available local tools and route work by capability instead of tool-name memory.

## When To Use

- before verification or review when tool choice matters
- when `.harness/TOOL_CONTEXT.md` is missing or stale
- at the start of a composed review-and-verify workflow

## When Not To Use

- when `.harness/TOOL_CONTEXT.md` is already current for this session
- when the task needs no external tooling

## Inputs

- active session context
- optional existing `TOOL_CONTEXT.md`

## Procedure

1. Read `.harness/TOOL_CONTEXT.md` if present.
3. Update or create `.harness/TOOL_CONTEXT.md`.
4. Route by capability, not by guessed tool names.

## Reasoning Procedure

1. Restate the tool capability that is needed.
2. Check the current tool context or discover it fresh.
3. Derive the safest route by capability, not by memory.
4. Stop and report blocked if a required capability has no safe fallback.

## Action Loop

- Thought: identify the next tool or routing question.
- Action: inspect the context or run the discovery command.
- Observation: record the real tool availability and routing result.
- Repeat until the tool context is ready.

## Examples

### Example 1

Input: The repository needs a fresh .harness/TOOL_CONTEXT.md.

Output:
- Refreshed tool context: detected git, rg, and repository-local scripts.
- Routing guidance: use code search first, then git diff/history as needed.
- Notes: prefer safe fallbacks when a preferred tool is absent.

### Example 2

Input: A required capability has no safe fallback.

Output:
- Blocked: missing capability for the next step.
- Needed next step: choose a safe fallback or install the missing tool.
## Output Contract

Produce or refresh `.harness/TOOL_CONTEXT.md` with detected tools and routing guidance.

## Blocking Conditions

Return blocked when a required capability has no safe fallback and the next step depends on it.

## Common Failure Modes

- assuming a tool exists without detection
- treating missing optional tools as hard failure by default

## References

- `references/routing-table.md`
- `prompt.md`

## Boundary

**`sk-tool-discovery`** owns **capability-based discovery and routing of available tools without assuming tool names**. It does not own **performing the task itself or treating optional tooling as a hard dependency**; route those concerns to the appropriate specialist skill.

## When not to use

- When the request is outside `sk-tool-discovery`'s named capability or another specialist is the primary owner.
- When the requested result depends on unverified permissions, unsupported platform claims, or unsafe/destructive action.

## Required inputs

- required capability, active environment, current tool context, safe fallback, and routing goal.
- State assumptions, permissions, blockers, and verification evidence explicitly.

## Cross-skill handoffs

- sk-using-harness for active context; sk-repo-tooling-pro for repository CLI; relevant domain skill for the actual work.
