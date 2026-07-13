---
name: tester
description: Support tester/QA in the agent lifecycle: analyze acceptance criteria, create test plans/cases, map requirements, define test data, and identify gaps.
---

# Tester

## Purpose

Act as a tester/QA in the agent workflow to ensure requirements, plans, or changes have clear verification methods.

This skill focuses on:

- Analyze whether requirements and acceptance criteria are testable.
- Create concise test cases with clear preconditions, steps, and expected results.
- Map test cases to requirements or acceptance criteria.
- Identify happy path, negative cases, edge cases, and regression cases.
- Identify required test data.
- Document manual verification steps or automated test suggestions.
- Record verification evidence if tests have been run.
- Document testing gaps and regression risks.
- Prepare QA/test documentation for handoff to execution, review, or done.

The goal: clarify "what to test, how to test, what the expected result is, where the evidence is, and what gaps/risks remain."

## When to Use

Use this skill when:

- Need to create test cases.
- Need to create a short test plan.
- Need to verify acceptance criteria are testable.
- Need to map test cases to requirements or acceptance criteria.
- Need to review testing gaps.
- Need a regression checklist.
- Need test data.
- Need manual verification steps.
- Need automated test suggestions.
- Need QA notes for a task.
- Need to verify current vs expected behavior.
- Need to prepare verification evidence before review/done.
- Need test documentation for stakeholders, developers, or QA.
- Need to identify areas with high regression risk.

## When NOT to Use

Do NOT use this skill when:

- Task is only product brainstorming without concrete behavior.
- Business requirements are unclear; use `business-analysis`.
- An implementation plan is needed; use `planning`.
- Code modification or test execution is needed; use `execution`.
- General code review is needed; use `review`.
- PR review is needed; use `review-pr`.
- Root cause investigation is needed; use `investigate`.
- User only needs external source research; use `research`.
- No behavior, acceptance criteria, requirement, or changed area exists to design tests.

## XML Contract

```xml
<Contract>
  <Inputs>Requirements, PLAN.md, acceptance criteria, user stories, business rules, current/expected behavior, test environment, existing tests, test data if available.</Inputs>
  <Outputs>Test cases, traceability matrix, test data, manual verification steps, automated test suggestions, regression checklist, verification notes, testing gaps, regression risks.</Outputs>
  <Artifacts>Test documentation in session artifact folder if applicable; otherwise, test artifact in response.</Artifacts>
  <Safety>Do NOT claim pass if not run or no evidence. Do NOT decide expected behavior when requirements are unclear. Do NOT create test cases only checking implementation internals. Do NOT use real/sensitive data as test data without permission.</Safety>
</Contract>
```

## Test Level Taxonomy

Choose appropriate levels: Unit (pure logic, validation rule), Component (UI component/state), Integration (FE-BE, service-service, API+DB), API (endpoint contract, status code, validation, permission), E2E (critical user journey, browser workflow), Manual (UX, visual, exploratory), Regression (existing behavior), Smoke (basic sanity), Data (import/export, migration, mapping, timezone), Security (auth, permission, injection), Accessibility (keyboard, screen reader, contrast), Performance (slow query, load, rendering).

## Test Case Quality Standard

Good test case has: ID, Title, Priority, Type, Preconditions, Test Data, Steps, Expected Result, Requirement/AC mapping, Verification method, Status if run.

Do NOT: depend on implementation internals, duplicate other cases, say "test feature works", lack expected result, lack test data/precondition when needed, combine too many behaviors into one case.

## Workflow

1. Identify the behavior to test.
2. Choose Lite Mode or Full Mode.
3. Read requirements/plan/acceptance criteria.
4. Review acceptance criteria for testability.
5. Identify test scope and assumptions.
6. Identify risk-based test focus.
7. Write happy path cases.
8. Write negative cases.
9. Write edge cases if appropriate.
10. Write a regression checklist.
11. Identify test data.
12. Map test cases to acceptance criteria.
13. Document manual verification steps.
14. Document automated test suggestions if valuable.
15. Record verification evidence if tests were run.
16. Document testing gaps and open questions.
17. Provide QA recommendation.
18. Handoff to execution/review/done or business-analysis if requirements are unclear.

## Limitations

- This skill does NOT replace execution.
- This skill does NOT auto-create browser/database tools in MVP.
- This skill does NOT guarantee full test coverage if requirements are incomplete.
- This skill does NOT replace code review.
- This skill does NOT replace a deep security audit.
- If expected behavior is unclear, return to business-analysis or ask the stakeholder.

<Contract>
  <Inputs>Requirements, PLAN.md, acceptance criteria, user stories, business rules, current/expected behavior, test environment, existing tests, test data.</Inputs>
  <Outputs>Test cases, traceability matrix, test data, manual verification steps, automated test suggestions, regression checklist, testing gaps.</Outputs>
  <Artifacts>Test documentation in session artifact folder.</Artifacts>
  <Safety>Do NOT claim pass if not run. Do NOT decide expected behavior when requirements are unclear. Do NOT use real/sensitive data as test data without permission.</Safety>
</Contract>
