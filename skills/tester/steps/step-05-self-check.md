# Step 05 — Self-check (planning gate)

## Goal

Verify planning artifacts (REQ_REVIEW, TEST_PLAN, TESTCASES) against the contract before entering execution phase. Fail closed. This is a **planning gate** — DEFECT_LOG and TEST_SUMMARY are checked for template integrity only, not content.

## Precondition (fail closed)

- [ ] Step ledger 01–04 = `done` in their respective artifacts
- [ ] All 5 artifacts exist in the session directory

If precondition fails → return to the earliest incomplete step.

## Checks (run all)

### Cross-artifact checks

1. All 5 files exist and were seeded from templates (each has Step ledger + Executive summary + Developer overview).
2. Step ledger is sequential across all artifacts: no later step `done` while an earlier step is `todo`.
3. Traceability is complete: REQ_REVIEW traceability matrix → TESTCASES IDs are filled.
4. TEST_PLAN scope matches REQ_REVIEW scope (no feature planned that was not reviewed).
5. TESTCASES requirement mapping references only IDs that exist in REQ_REVIEW inventory.

### REQ_REVIEW.md checks

6. Every requirement from upstream artifacts has a row in Requirement inventory.
7. Every requirement has Clarity and Testability assessed (no `_(TODO)_` on verdicts).
8. Blocking questions have target and blocking flag.
9. Completeness check covers all feature areas.

### TEST_PLAN.md checks

10. Test scope in/out both present.
11. Test strategy covers at least functional + regression.
12. Estimation has explicit numbers (not "TBD" or "it depends").
13. Risk assessment has ≥1 real risk or explicit "no material risks" with evidence.
14. Environment requirements list all dependencies.

### TESTCASES.md checks

15. Every P0 AC has ≥1 test case with Positive + Negative + Boundary.
16. Every test case has: ID, Priority, Type, Preconditions, Steps, Expected result, Requirement mapping.
17. API test cases (if in scope) have: endpoint, method, headers, payload, assertions.
18. Test data does not contain real PII.
19. Testing gaps are documented.
20. Manual steps are precise enough to repeat.

### DEFECT_LOG.md — template integrity only

21. Template structure is intact (step ledger, executive summary, defect list sections present).
22. No content expected — defect list is empty until step-07.

### TEST_SUMMARY.md — template integrity only

23. Template structure is intact (step ledger, metrics, quality assessment sections present).
24. No content expected — metrics are empty until step-08.

### Quality checks

25. No leftover `_(TODO)_` in filled sections (REQ_REVIEW, TEST_PLAN, TESTCASES).
26. Executive summaries are ≤5 bullets each.
27. First-pass readable: concrete names, no filler.
28. Work nested git: ran `session.sh commit 'docs(tester): planning complete'` after writing artifacts.

## Spec quality enforcement

The planning gate is the spec quality checkpoint for the entire planning phase:

- **REQ_REVIEW quality:** are clarity and testability verdicts backed by evidence (quotes, section references), not gut feeling?
- **TEST_PLAN quality:** does the strategy reference REQ_REVIEW findings? Does estimation use a named technique with numbers?
- **TESTCASES quality:** does every test case have reproducible steps and specific expected results? Is traceability complete?
- **Cross-artifact consistency:** do scope boundaries match between REQ_REVIEW and TEST_PLAN? Do requirement IDs in TESTCASES exist in REQ_REVIEW inventory?

If any artifact has `_(TODO)_` in required fields or fails cross-artifact consistency, the planning gate fails.

## Done when

- [ ] All checks pass **or** Ready=No with blockers listed.
- [ ] Step ledger 05 = `done` or `blocked` in all artifacts.
- [ ] User is told:
  - Planning phase complete — ready for execution
  - Next: step-06 (setup environment) → step-07 (execute) → step-08 (summary)
  - Path to each artifact
  - Any remaining blockers

## Handoff guidance

Planning gate passed. Enter execution phase:

1. **Step 06** — Setup environment, verify dependencies, run smoke test
2. **Step 07** — Execute test cases, log defects, identify patterns
3. **Step 08** — Compile test summary, metrics, go/no-go recommendation

## Stop

Planning phase ends here. Do **not** auto-start execution (step-06) unless asked.
