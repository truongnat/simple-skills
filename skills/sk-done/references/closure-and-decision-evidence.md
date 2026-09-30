# Closure and decision evidence

Close a task only after consuming the canonical verification result and recording what remains true after delivery.

| Closure field | Expected evidence |
|---|---|
| Status | Done, Done with risks, Needs fix, Blocked or Partial; never ambiguous “complete” |
| Scope | Completed items, intentionally skipped items and out-of-scope work |
| Verification | Claims mapped to `VERIFY.md`/test summary/review evidence |
| Decision | Release/acceptance owner, date, rationale and residual-risk disposition |
| Change record | Files/artifacts, migration or rollout notes, rollback status |
| Handoff | Next owner, follow-up issue, monitoring period and review date |

If verification is missing or blocked, close as `Done with risks`, `Partial`, or `Blocked` with the exact evidence gap. `DONE.md` should make a reviewer able to reconstruct the decision without relying on chat history.
