# Step 08 — Test summary & closure

## Goal

Compile the final test summary with metrics, coverage analysis, quality assessment, and go/no-go recommendation. Close the test cycle.

## Precondition (fail closed)

- [ ] Step ledger 01–07 = `done` in all artifacts
- [ ] `TESTCASES.md` has all test cases executed (Pass/Fail/Blocked/Skipped)
- [ ] `DEFECT_LOG.md` has all defects logged with severity and evidence

If precondition fails → return to the earliest incomplete step. Do **not** write summary with unexecuted test cases or unlogged defects.

## Rules

- Edit **only** `TEST_SUMMARY.md` in this step.
- All metrics must come from actual data in TESTCASES.md and DEFECT_LOG.md — no estimates or guesses.
- Go/No-Go recommendation must reference specific metrics and thresholds.
- Do **not** recommend Go while P0 bugs are open.
- Do **not** skip lessons learned — even one observation improves the next cycle.

## Actions

### A. Test metrics

1. Count from `TESTCASES.md`:
   - Total test cases, Passed, Failed, Blocked, Not run
   - Pass rate = Passed / (Passed + Failed) × 100%
2. Compare with planned counts from `TEST_PLAN.md` estimation.
3. Fill **Test metrics** table (planned vs actual vs variance).

### B. Coverage analysis

4. For each area/feature:
   - Count total cases, passed, failed, blocked
   - Calculate coverage % = (Passed + Failed) / Total × 100%
5. Fill **Coverage analysis** table.

### C. Defect analysis

6. Copy summary data from `DEFECT_LOG.md`:
   - By severity: counts per level
   - By area: counts per module
   - Defect density: bugs per feature or per 100 LOC (if LOC known)
   - Trend: describe discovery pattern (early spike, steady, late surge)
7. Fill **Defect analysis** section.

### D. Requirement coverage

8. For each requirement in `REQ_REVIEW.md` traceability matrix:
   - List test cases covering it
   - Report pass/fail status
   - Note gaps (requirement with no test case or all tests blocked)
9. Fill **Requirement coverage** table.

### E. Quality assessment

10. Define criteria and thresholds (from TEST_PLAN or standard):
    - Pass rate ≥ 95%
    - P0 bugs open = 0
    - P1 bugs open ≤ 2
    - Requirement coverage = 100%
    - Blocked test cases = 0
    - Regression pass rate = 100%
11. Compare actual values against thresholds.
12. Fill **Quality assessment** table (criteria, threshold, actual, verdict).

### F. Go / No-Go recommendation

13. Based on quality assessment:
    - **Go** — all criteria pass, no residual risk
    - **Conditional** — critical criteria pass, non-critical items need attention before release
    - **No-Go** — critical criteria fail (P0 bugs open, pass rate below threshold)
14. State rationale referencing specific metrics.
15. If Conditional: list conditions that must be met.
16. List residual risks accepted for release.

### G. Lessons learned

17. Identify ≥1 observation from this cycle:
    - What went well (keep doing)
    - What went wrong (stop doing)
    - What to improve next cycle
18. Fill **Lessons learned** table.

### H. Final checks

19. Fill **Handoff** — next step (release / next test cycle / stakeholder review).
20. Update Step ledger 08 in all artifacts.
21. Run `session.sh commit 'docs(tester): test cycle complete'`.

## Stop gate

**Must NOT recommend Go when:**

- Any P0 / Critical bug is still Open
- Pass rate is below threshold
- Requirement coverage has gaps for P0 requirements
- Blocked test cases > 0 for P0 features

In these cases, recommendation must be **No-Go** or **Conditional** with explicit fix conditions.

## Spec quality enforcement

The test summary is the final spec quality gate — it determines whether the product is ready for release:

- **Metrics accuracy:** every metric comes from actual TESTCASES.md and DEFECT_LOG.md data, not estimates or rounded numbers.
- **Go/No-Go objectivity:** the recommendation references specific metrics and thresholds, not gut feeling or schedule pressure.
- **Quality criteria completeness:** all criteria (pass rate, open bugs, coverage, blocked cases) are assessed against explicit thresholds.
- **Lessons learned honesty:** at least one observation is genuine — "everything was perfect" is rarely true and suggests the lesson section was skipped.

If metrics do not match execution data or Go recommendation has open P0 bugs, do not mark step-08 done.

## Done when

- [ ] Test metrics match actual TESTCASES.md execution data.
- [ ] Coverage analysis covers all areas from test scope.
- [ ] Defect analysis matches DEFECT_LOG.md data.
- [ ] Requirement coverage maps every requirement to test results.
- [ ] Quality assessment has explicit thresholds and verdicts.
- [ ] Go/No-Go recommendation references metrics (not gut feeling).
- [ ] Lessons learned has ≥1 observation.
- [ ] Step ledger 08 = `done` in all artifacts.
- [ ] All artifacts committed via `session.sh commit`.

## Stop

Tester cycle ends here. Report to user:

- Quality verdict (Go / No-Go / Conditional)
- Key metrics (pass rate, open bugs, coverage)
- Path to TEST_SUMMARY.md
- Recommended next action
