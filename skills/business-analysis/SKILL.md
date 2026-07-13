---
name: business-analysis
description: Clarify business problems, stakeholder needs, scope, processes, user stories, business rules, data sources, assumptions, acceptance criteria, and functional specs.
---

# Business Analysis

## Purpose

Clarify business requirements before planning, technical design, implementation, or testing.

This skill focuses on:

- Business problem.
- Stakeholders and actors.
- Current state and desired state.
- Scope, out-of-scope, and non-goals.
- User stories and use cases.
- Business rules.
- Data sources and data assumptions.
- Verifiable acceptance criteria.
- Open questions requiring stakeholder confirmation.

The goal: turn vague input into clear, traceable requirement notes good enough to hand off to planning or implementation.

## When to Use

Use this skill when:

- Business requirements are unclear.
- User only describes an idea, pain point, or problem.
- Need to analyze requirements before starting technical work.
- Need to write user stories, use cases, or functional specs.
- Need to define scope, non-goals, or feature boundaries.
- Need to identify business rules.
- Need to write acceptance criteria.
- Need to analyze current and desired processes.
- Need to analyze data sources: Excel, CSV, SQL, API response, or business docs.
- Need to prepare documentation for stakeholders, PM, dev, or QA.

## When NOT to Use

Do NOT use this skill when:

- Task is purely technical with a clear spec.
- User only needs code review, debug, or implementation.
- User needs detailed technical architecture; use technical design or planning.
- User needs deep external source research; use `research`.
- User needs UI style, visual concept, or product brainstorming; use the appropriate skill.
- Input is already a complete requirement and only needs to be turned into implementation tasks.

## XML Contract

```xml
<Contract>
  <Inputs>User request, business context, existing requirement documents, data samples (Excel, CSV, SQL, JSON, API response), screenshots, bug reports with business factors, stakeholder feedback.</Inputs>
  <Outputs>Requirement notes: problem statement, stakeholders, current/desired state, scope, non-goals, user stories/use cases, business rules, data assumptions, acceptance criteria, assumptions, open questions, recommended next step.</Outputs>
  <Safety>Do NOT treat assumptions as requirements. Do NOT decide for stakeholders. Do NOT hide unclear points. Do NOT write vague or untestable acceptance criteria.</Safety>
</Contract>
```

## Operating Principles

- Do NOT treat assumptions as requirements.
- Do NOT decide for stakeholders when information is missing.
- If information is missing, record it in `Assumptions` or `Open Questions`.
- Requirements must clearly state actor, behavior, condition, and expected outcome.
- Acceptance criteria must be verifiable.
- Business rules should have IDs for traceability to tasks, test cases, or implementation.
- Scope and non-goals must be separated to prevent scope creep.
- Data assumptions must document source, owner, validation, and freshness.
- Do NOT turn BA docs into long essays; prefer bullets, tables, and scannable formats.

## Workflow

1. Restate the business problem.
2. Identify goals and expected outcomes.
3. Identify stakeholders and actors.
4. Identify current state.
5. Identify desired state.
6. Identify in-scope, out-of-scope, and non-goals.
7. Identify user stories or use cases.
8. Identify business rules.
9. Identify data sources, required fields, validation, and assumptions.
10. Write verifiable acceptance criteria.
11. Separate assumptions from confirmed requirements.
12. Record open questions for stakeholders.
13. Recommend next step: brainstorming, planning, technical design, implementation, or QA test design.

## Limitations

- This skill does NOT replace stakeholder decisions.
- This skill does NOT auto-implement.
- This skill does NOT auto-confirm business rules without a source.
- This skill does NOT replace research when deep external sources are needed.
- This skill does NOT guarantee correct requirements if input is missing or stakeholders have not confirmed.
- This skill should NOT produce detailed technical architecture; recommend moving to technical design if needed.

<Contract>
  <Inputs>User request, business context, existing requirements, data samples, screenshots, stakeholder feedback.</Inputs>
  <Outputs>Requirement notes: problem statement, stakeholders, scope, user stories/use cases, business rules, data assumptions, acceptance criteria, open questions.</Outputs>
  <Safety>Do NOT treat assumptions as requirements. Do NOT decide for stakeholders. Do NOT write vague or untestable acceptance criteria.</Safety>
</Contract>
