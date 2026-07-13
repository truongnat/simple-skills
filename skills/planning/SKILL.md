---
name: planning
description: Build an execution plan from DISCUSSION.md, requirements, or clear requests. Task breakdown, dependencies, acceptance criteria, DoD, verification, and rollback strategy.
---

# Planning

## Purpose

Turn a clear goal into a concrete execution plan with order, dependencies, acceptance criteria, verification, and rollback.

This skill focuses on:

- Lock goal and scope clearly enough to execute.
- Break work into small tasks with clear dependencies.
- Identify affected files, modules, systems, or artifacts if known.
- Write acceptance criteria for each task.
- Write verification strategy with commands or check methods.
- Write rollback strategy matching the change scope.
- Write a Definition of Done so review is objective.
- Prepare handoff to execution, implementation, or QA.

The goal: create a `PLAN.md` clear enough for an agent or developer to execute without guessing.

## When to Use

Use this skill when:

- `DISCUSSION.md` exists.
- Requirements or specs are clear enough.
- User requests a plan, task breakdown, or implementation plan.
- Need to create or update `PLAN.md`.
- Need to identify affected files or systems before modifying code.
- Need to break work into phases or small tasks.
- Need to identify dependencies between tasks.
- Need acceptance criteria for each task.
- Need verification strategy before execution.
- Need rollback strategy before changing workspace, codebase, database, infra, or config.
- Need a Definition of Done for review or verification.

## When NOT to Use

Do NOT use this skill when:

- Goals are still unclear; use `brainstorming` first.
- Business requirements lack rules, actors, data, or acceptance criteria; use `business-analysis`.
- Investigating root cause or mapping a system; use `investigate`.
- Reviewing results after implementation.
- User only needs a small fix with very clear scope.
- User wants to brainstorm solution directions rather than create an execution plan.
- User needs detailed technical architecture; use `technical-design` if available.
- User needs deep external source research; use `research`.

## XML Contract

```xml
<Contract>
  <Inputs>DISCUSSION.md, requirement notes, user request, codebase mapping, affected systems, constraints, and related context if available.</Inputs>
  <Outputs>Lite plan or full PLAN.md including goal, scope, assumptions, non-goals, affected files/systems, task breakdown, dependencies, acceptance criteria, verification strategy, Definition of Done, rollback strategy, risks, and handoff to execution.</Outputs>
  <Artifacts>PLAN.md in the session path if applicable; otherwise, return a plan artifact in the response.</Artifacts>
  <DefinitionOfDone>Specific, verifiable conditions for a task or plan to be considered complete.</DefinitionOfDone>
  <Gate>For large, destructive, irreversible, production/data/security-touching, or high-risk tasks, require user review and DoD confirmation before execution unless the user has already given clear permission to execute.</Gate>
  <Safety>Do NOT implement code during planning. Do NOT invent affected files without inspecting the codebase. Do NOT treat assumptions as confirmed requirements. Do NOT skip rollback when changing workspace, database, config, infra, or public behavior.</Safety>
</Contract>
```

## Depth Modes

### Lite Mode

Use Lite Mode when:

- Task is small or medium.
- Scope is clear.
- Few dependencies.
- No need to save `PLAN.md`.
- No migration, destructive changes, or high risk.
- User needs a quick plan before doing the work.

### Full Mode

Use Full Mode when:

- Task is large.
- Multiple steps or modules.
- Clear dependencies exist.
- Changes to database, config, infra, auth, payment, security, or public API.
- High regression risk.
- Need to save `PLAN.md`.
- User requests a thorough plan, implementation plan, breakdown, or DoD.

## Clarification Policy

- Ask the user when missing information significantly changes scope, execution order, risk, data, permission, or architecture.
- Do NOT ask if a safe assumption can be made.
- If assuming, document it in `Assumptions`.
- Ask at most 1-3 critical questions.
- Do NOT ask a long list if a best-effort plan is still possible.
- If the user says "just do it", create the best possible plan and mark blocking questions.
- If an open question blocks execution, mark it `Blocking = Yes`.

## Operating Principles

- Planning must be specific enough for another agent or developer to execute.
- Do NOT implement code during planning.
- Do NOT include out-of-scope work in the plan.
- Do NOT over-plan small tasks.
- Each task must have objective, scope/files, dependencies, acceptance criteria, and verification.
- Tasks must be small, ordered, and verifiable.
- Acceptance criteria must be testable.
- Verification strategy must include commands or specific check methods if possible.
- Rollback strategy must not be empty when changing workspace/codebase/database/config/infra.
- DoD must be specific enough for objective review.
- Do NOT invent affected files or systems without context or codebase inspection.
- If codebase context is missing, note it as unknown instead of guessing.
- If multiple phases, each phase must have exit criteria.

## Workflow

1. Determine if the task needs planning.
2. Choose Lite Mode or Full Mode.
3. Confirm session path if working in a repo/session.
4. Read `DISCUSSION.md`, requirement notes, or related context if available.
5. Restate goals, desired outcomes, and scope.
6. Document sources and context used for planning.
7. Document constraints, assumptions, and non-goals.
8. Identify affected files, systems, modules, or artifacts if known.
9. If codebase mapping is missing, note it as unknown or add an investigate task first.
10. Break down tasks in small, independent, verifiable order.
11. Document dependencies between tasks.
12. Document acceptance criteria for each task.
13. Document verification method for each task or phase.
14. Document execution order.
15. Document Definition of Done.
16. Document overall verification strategy.
17. Document rollback strategy.
18. Document risks and mitigation.
19. Document open questions and mark blocking if any.
20. For large/high-risk/destructive tasks, request user review/confirmation of the plan or DoD before execution unless the user has explicitly approved it.
21. Save `PLAN.md` if Full Mode and in a suitable repo/session.

## Limitations

- This skill does NOT implement code.
- This skill does NOT replace brainstorming when direction is unclear.
- This skill does NOT replace business analysis when business requirements are incomplete.
- This skill does NOT replace investigate when codebase or bug root cause is unknown.
- This skill does NOT replace detailed technical design.
- This skill does NOT auto-confirm assumptions.
- This skill does NOT invent affected files or systems without codebase context.
- This skill does NOT guarantee the plan is correct if inputs are missing or outdated.

## Artifact Template

See `PLAN.md` template in AGENTS.md workflow section.

<Contract>
  <Inputs>DISCUSSION.md, requirement notes, user request, codebase mapping, constraints, affected systems.</Inputs>
  <Outputs>PLAN.md with goal, scope, assumptions, non-goals, affected files, task breakdown, dependencies, acceptance criteria, verification, DoD, rollback, risks.</Outputs>
  <Artifacts>PLAN.md in session path.</Artifacts>
  <Safety>Do not implement code during planning. Do not invent affected files without inspection. Do not skip rollback for destructive changes.</Safety>
</Contract>
