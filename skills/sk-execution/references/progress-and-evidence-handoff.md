# Execution progress and evidence handoff

Legacy execution sessions must preserve the task ledger while remaining compatible with the canonical `sk-executing-pro` owner for new work.

| Execution event | Update required |
|---|---|
| Start card | Set status `in_progress`, record task ID, scope and precondition |
| Complete work item | Check the item, record changed surface and evidence |
| Verify card | Record AC/Verify result, test command or manual evidence and residual risk |
| Block | Set `blocked`, record exact cause, owner/question and resume point |
| Skip | Set `skipped` with reason and impact; do not imply completion |
| Handoff | Update `TASKS.md`, `EXECUTION.md`, artifact paths, next owner and open risks |

Worked scenario: when implementation passes local checks but a required integration environment is unavailable, keep the card partial/blocked and hand off the missing evidence. Never convert an unverified card to done merely because code changed.
