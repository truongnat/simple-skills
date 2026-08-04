# Step 06 — Setup environment

## Goal

Prepare and verify the test environment before execution. Confirm every dependency from TEST_PLAN.md is ready. Run a smoke test to catch setup issues early.

## Precondition (fail closed)

- [ ] Step ledger 01–05 = `done` in all artifacts
- [ ] `TEST_PLAN.md` has environment requirements filled (not `_(TODO)_`)
- [ ] `TESTCASES.md` has test cases ready for execution

If precondition fails → return to the earliest incomplete step. Do **not** set up an environment for test cases that do not exist.

## Rules

- Edit **only** `TEST_PLAN.md` (environment status) in this step.
- Do **not** execute test cases yet — that is step-07.
- Do **not** skip the smoke test — it catches environment issues before full execution.
- Verify every environment item from TEST_PLAN, not just the obvious ones.
- If a critical environment component is unavailable, **stop and report** — do not proceed with partial setup.

## Actions

1. Read `TEST_PLAN.md` → Environment requirements section.
2. For each row, verify and update Status:
   - **Server / URL** — accessible, correct version deployed, no maintenance window
   - **Browsers** — installed, correct versions, cache cleared
   - **Mobile devices** — connected, OS version matches, app installed
   - **Test accounts** — created, credentials verified, correct roles/permissions
   - **Test data** — loaded, DB state matches prerequisites, no stale data from prior runs
   - **Third-party** — sandbox keys valid, mock services running, rate limits confirmed
3. Update Status column in TEST_PLAN.md environment table:
   - `Ready` — verified and working
   - `Blocked` — not available, with reason
   - `Partial` — available with limitations (note in comments)
4. Run **smoke test** — execute 1–2 P0 test cases from TESTCASES.md to confirm end-to-end path works:
   - If smoke test passes → proceed
   - If smoke test fails → document failure, do not proceed until fixed
5. Update Step ledger 06 in all artifacts.

## Spec quality enforcement

Environment setup is a spec for execution — if the setup is incomplete, execution results are unreliable:

- **Verification evidence:** every environment item has a Status based on actual verification, not assumption. "Should be fine" is not verification.
- **Smoke test validity:** the smoke test exercises the end-to-end path, not just "can I open the URL."
- **Blocker transparency:** if an environment component is unavailable, it is documented as Blocked with a reason — not silently skipped.

If any critical environment item is unverified or smoke test fails, do not mark step-06 done.

## Done when

- [ ] Every environment item has Status = `Ready` or `Blocked` (no `_(TODO)_`).
- [ ] Smoke test passes (or failure is documented with blocker).
- [ ] TEST_PLAN.md environment table is fully updated.
- [ ] Step ledger 06 = `done` or `blocked`.

## Next

Only if Step ledger 06 = `done`: Read and follow `./step-07-execute-and-log.md`.
If `blocked`: stop for environment resolution.
