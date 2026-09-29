---
name: sk-javascript-testing-patterns
description: Apply JavaScript testing patterns for unit, integration, async, mocking, and regression tests. Use when designing or reviewing tests for JavaScript applications.
sk-kind: domain
sk-version: 0.1.0
sk-tags: [language, framework, application]
sk-roles: [developer, engineer]
sk-compatible: [claude, cursor, codex, gemini]
---
# JavaScript Testing Patterns

## Use this skill when

Use this skill for the scenarios listed in the description. Keep the first pass focused on the smallest reproducible example and the requested scope.

## Workflow

1. Inspect the current project conventions and existing tests or diagnostics.
2. Reproduce the behavior or define the expected behavior with a minimal example.
3. Choose the narrowest useful technique and record the evidence.
4. Implement or recommend the smallest change that addresses the verified cause.
5. Run the relevant checks and report failures, residual risk, and next action.

## Output

Produce a test strategy, representative tests, verification output, and any coverage or fixture gaps.

## Detailed reference

Read `references/javascript-testing-patterns-reference.md` for Jest/Vitest/Testing Library setup and detailed pattern examples.
Do not load the reference wholesale when the compact workflow is sufficient.

## Boundary

**`sk-javascript-testing-patterns`** owns **named programming-language, framework, or engineering-domain guidance within its specialized scope**. It does not own **cross-domain architecture or product planning as the primary concern**; route those concerns to the appropriate specialist skill.

## Required inputs

- language/framework version, target behavior, existing code/context, constraints, and verification target.
- State assumptions explicitly when context, ownership, or evidence is incomplete.

## Cross-skill handoffs

- sk-testing-pro for test strategy; sk-systematic-debugging-pro for diagnosis; sk-clean-code or architecture skills for cross-cutting design; neighboring stack skill for integration.
