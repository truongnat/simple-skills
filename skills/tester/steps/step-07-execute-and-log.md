# Step 07 — Execute tests & log defects

## Goal

Execute all test cases from TESTCASES.md in priority order. Log every failure as a defect in DEFECT_LOG.md. Update test case statuses. Identify defect patterns.

## Precondition (fail closed)

- [ ] Step ledger 01–06 = `done` in all artifacts
- [ ] `TEST_PLAN.md` environment Status is `Ready` (not `Blocked`)
- [ ] `TESTCASES.md` has test cases with steps and expected results filled
- [ ] Smoke test passed in step-06

If precondition fails → return to step-06. Do **not** execute tests in an unverified environment.

## Rules

- Edit `TESTCASES.md` (execution status) and `DEFECT_LOG.md` (defect entries).
- Execute in **priority order**: P0 first → P1 → P2.
- Every failure **must** get a BUG-XXX entry — no verbal-only or chat-only bugs.
- Severity follows standard classification:
  - **Critical** — system crash, data loss, security breach, core feature completely broken
  - **High** — major feature broken, no workaround
  - **Medium** — feature degraded, workaround exists
  - **Low** — cosmetic, minor UX issue, typo
- Evidence required for every defect: screenshot path, log excerpt, or detailed reproduction steps.
- Do **not** skip re-testing of fixed defects if time allows within the cycle.
- Do **not** mark step-07 `done` while any test case is unexecuted (unless explicitly Blocked by environment).

## Actions

### A. Execute test cases

1. Open `TESTCASES.md` — sort by Priority (P0 first).
2. For each test case:
   - Execute the steps as written.
   - Compare actual result to expected result.
   - Record status: `Pass` / `Fail` / `Blocked` (with reason) / `Skipped` (with reason).
   - If `Fail` → go to B (defect logging).
   - If `Blocked` → document blocker (environment issue, dependency not ready).
3. After all P0 cases → move to P1 → then P2.

### B. Log defects

4. For each failure, create a new BUG-XXX entry in `DEFECT_LOG.md`:
   - **BUG-ID**: sequential (BUG-001, BUG-002, …)
   - **Title**: one-sentence summary
   - **Severity**: Critical / High / Medium / Low (follow classification above)
   - **Priority**: P0 (fix immediately) / P1 (fix before release) / P2 (fix when possible)
   - **Area / module**: which feature/component
   - **Status**: Open
   - **Found in**: TC-XXX or API-XXX that triggered the defect
   - **Environment**: browser, OS, device, URL
   - **Steps to reproduce**: numbered, exact steps
   - **Expected result**: what should happen
   - **Actual result**: what actually happened
   - **Evidence**: screenshot path, log excerpt, or video timestamp

### C. Summarize

5. Update `DEFECT_LOG.md` summary tables:
   - Defect summary by severity (counts per severity level)
   - Defect summary by area (counts per module)
6. Look for **patterns** across defects:
   - Same root cause appearing in multiple bugs?
   - One module producing disproportionate defects?
   - Same type (boundary, permission, validation) repeating?
7. Fill **Patterns & root causes** section in DEFECT_LOG.md.
8. Update Step ledger 07 in all artifacts.

## Defect lifecycle

```
Open → In Progress → Fixed → Verified → Closed
                  ↘ Deferred (accepted risk)
                  ↘ Duplicate (reference original BUG-ID)
```

## Spec quality enforcement

Defect logs are specs for fixes — a poorly logged defect wastes developer time and may never get fixed:

- **Reproducibility:** can a developer who was not present reproduce the bug from the steps alone? If steps are vague, the defect is not actionable.
- **Evidence requirement:** every defect has evidence (screenshot, log, or detailed steps). "It broke" is not evidence.
- **Severity discipline:** severity follows the classification (Critical/High/Medium/Low), not emotional reaction. "Everything is Critical" means nothing is.
- **Expected vs actual:** both are stated explicitly. The delta between them is the bug.

If any defect entry is missing steps, evidence, or expected/actual comparison, do not mark step-07 done.

## Done when

- [ ] All test cases in TESTCASES.md have execution status (Pass/Fail/Blocked/Skipped).
- [ ] Every failure has a corresponding BUG-XXX entry in DEFECT_LOG.md.
- [ ] Each defect has: severity, steps to reproduce, expected vs actual, evidence.
- [ ] Defect summary tables are updated with accurate counts.
- [ ] Patterns section identifies recurring root causes (or explicit "no patterns detected").
- [ ] Step ledger 07 = `done`.
- [ ] No leftover `_(TODO)_` on executed test cases or defect fields.

## Next

Read and follow `./step-08-test-summary.md`.
