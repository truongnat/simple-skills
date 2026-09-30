# Planning-to-execution handoff contract

A plan is ready for execution only when strategy, scope, dependencies, DoD, rollback and task cards agree.

| Gate | Expected evidence |
|---|---|
| Scope | In/out/non-goals, assumptions and trace IDs are explicit |
| Design decision | Relevant BA/spec/design review is complete; unresolved blockers are recorded |
| Task decomposition | Each card has owner, dependency, input/output, AC and Verify pair |
| Order | Dependency order is justified; feature work is separated from test work where required |
| DoD | Observable success, test evidence, review gate and documentation updates are named |
| Rollback | Reversible boundary, trigger, owner and recovery artifact are defined |
| Handoff | `PLAN.md`, `TASKS.md`, source artifacts, status and next skill are linked |

Worked scenario: if an API migration has an unconfirmed compatibility policy, mark the plan blocked rather than creating implementation cards. Once resolved, update the decision record and regenerate only the affected cards, preserving trace IDs and prior evidence.
