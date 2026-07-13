---
name: brainstorming
description: Clarify goals, scope, constraints, options, trade-offs, risks, and recommendations before planning or implementation.
---

# Brainstorming

## Purpose

Turn an initial request into a clear direction before planning or implementing.

This skill focuses on:

- Clarify goals and expected outcomes.
- Separate facts, assumptions, and unknowns.
- Identify constraints, scope, out-of-scope, and non-goals.
- Analyze feasible solution directions.
- Compare trade-offs between options.
- Identify risks, uncertainties, and verification methods.
- Make a reasoned recommendation.
- Prepare handoff to planning, technical design, business analysis, or implementation.

The goal: help the team settle on the smallest, clearest, verifiable direction before investing larger effort.

## When to Use

Use this skill when:

- Starting a new task with unclear goals, scope, constraints, or solutions.
- User wants to discuss ideas before implementing.
- Multiple approaches exist and need trade-off analysis.
- Scope needs to be locked before planning.
- Need to define in-scope, out-of-scope, or non-goals.
- Need draft success criteria before moving to planning or business analysis.
- Need to create or update `DISCUSSION.md`.
- Need alignment on product, UX, technical direction, or workflow.
- Need to decide between MVP, prototype, proof of concept, or phased delivery.
- Need to clarify risks, assumptions, or unknowns before detailed work.

## When NOT to Use

Do NOT use this skill when:

- Task is small, scope is clear, and can be fixed directly without discussion.
- Task already has a complete `DISCUSSION.md` and the user requests execution.
- Task has clear requirements/specs and only needs detailed planning.
- User requests code review, debug, or a specific bug investigation.
- User requests a small fix: typo, copy, style, import, simple config.
- User requests immediate implementation with low ambiguity.
- User needs detailed business requirement analysis; use `business-analysis`.
- User needs detailed technical architecture; use `technical-design` if available.
- User needs deep external source research; use `research`.

## XML Contract

```xml
<Contract>
  <Inputs>Initial request, repo context, existing documents, constraints, current behavior, desired outcome, and stakeholder feedback if available.</Inputs>
  <Outputs>Light discussion or full DISCUSSION.md including goal, facts, assumptions, unknowns, constraints, scope, options, trade-offs, recommendation, risks, open questions, and handoff to planning.</Outputs>
  <Artifacts>DISCUSSION.md in the session path if applicable; otherwise, return a discussion artifact in the response.</Artifacts>
  <Safety>Do NOT implement code during brainstorming. Do NOT treat assumptions as facts. Do NOT create detailed planning before a clear recommendation. Do NOT create large extra artifacts unless requested.</Safety>
</Contract>
```

## Depth Modes

### Lite Mode

Use Lite Mode when:

- Task is small or medium.
- Ambiguity is low to medium.
- Only a quick direction lock is needed.
- No `DISCUSSION.md` is needed.
- No more than 2 significant options.

### Full Mode

Use Full Mode when:

- Task is large.
- Multiple solution directions exist.
- High risk.
- Multiple stakeholders or actors.
- Dependency on repo, data, workflow, or architecture.
- Need to save `DISCUSSION.md`.
- User requests thorough brainstorming, discussion, alignment, scope, or trade-off analysis.

Full Mode uses the `DISCUSSION.md` artifact template.

## Clarification Policy

- Ask the user when missing information would significantly change direction, scope, cost, risk, or architecture.
- Do NOT ask if a safe assumption can be made.
- If assuming, document the assumption clearly.
- Ask at most 1-3 critical questions.
- Do NOT ask a long list if a best-effort discussion is still possible.
- If the user says "just do it", create the best possible output and note unknowns.
- If an open question blocks planning/implementation, mark it `Blocking = Yes`.

## Operating Principles

- Do NOT jump to implementation when scope is unclear.
- Prefer the smallest direction that meets the goal.
- Recommendations must include reasoning, trade-offs, and verification method.
- Unknowns must be documented clearly, not hidden in assumptions.
- Facts, assumptions, and unknowns must be separated.
- Scope, out-of-scope, and non-goals must be separated.
- Do NOT over-engineer discussion for small tasks.
- Do NOT create a long `DISCUSSION.md` if Lite Mode is sufficient.
- If multiple options, use an option matrix.
- If uncertainty is high, prefer a direction that is easy to roll back or verify.
- Do NOT stray into detailed planning or implementation before the direction is locked.

## Workflow

1. Determine if the task needs brainstorming.
2. Choose Lite Mode or Full Mode.
3. Identify or create a session path if working in a repo/session.
4. Restate the request in specific language.
5. Identify goals and desired outcomes.
6. Separate confirmed facts, assumptions, and unknowns.
7. Identify constraints: time, platform, tech stack, budget, tools, artifacts, quality bar.
8. Identify in-scope, out-of-scope, and non-goals.
9. Identify success criteria or draft acceptance signals.
10. Identify decision criteria: simplicity, speed, maintainability, cost, UX, risk, reversibility, testability.
11. List feasible solution directions.
12. Compare trade-offs per decision criteria.
13. Choose the simplest verifiable recommendation.
14. Document why other options were not chosen if important.
15. Document risks and mitigation.
16. Document open questions.
17. Document conditions for moving to planning or the next skill.
18. Save `DISCUSSION.md` if Full Mode and in a suitable repo/session.

## Decision Criteria

| Criteria | Meaning |
|---|---|
| Simplicity | Is the option simple to understand, build, and maintain? |
| Speed | Can it be tried or delivered quickly? |
| User Value | Does it solve the main pain point? |
| Risk | Is there technical, product, data, or operational risk? |
| Cost | Does it cost in tools, infra, APIs, time, or people? |
| Maintainability | Is it easy to extend and maintain? |
| Reversibility | If wrong, is it easy to roll back or change direction? |
| Testability | Is it easy to verify via test, demo, metric, or stakeholder review? |
| Integration Impact | Does it heavily affect the existing system? |
| Dependency | Does it rely on third parties, other teams, or uncertain data? |

## Limitations

- This skill does NOT implement code.
- This skill does NOT replace detailed planning.
- This skill does NOT replace detailed business analysis.
- This skill does NOT replace detailed technical design.
- This skill does NOT replace research when deep external sources are needed.
- This skill does NOT auto-confirm assumptions.
- This skill does NOT decide for stakeholders when critical information is missing.
- This skill should NOT create long artifacts for small, clear-scope tasks.

## Artifact Template

See `DISCUSSION.md` template in AGENTS.md workflow section.

<Contract>
  <Inputs>Initial request, repo context, existing documents, constraints, current behavior, desired outcome.</Inputs>
  <Outputs>DISCUSSION.md or discussion artifact with goal, facts, assumptions, unknowns, scope, options, trade-offs, recommendation, risks, open questions.</Outputs>
  <Artifacts>DISCUSSION.md in session path if applicable.</Artifacts>
  <Safety>Do not implement code. Do not treat assumptions as facts. Do not create detailed planning without clear direction.</Safety>
</Contract>
