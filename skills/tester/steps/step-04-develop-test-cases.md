# Step 04 — Develop test cases

## Goal

Write test cases covering all acceptance criteria, user stories, and functional requirements. Produce `TESTCASES.md` with full traceability. Includes API test cases when endpoints are in scope.

## Precondition (fail closed)

- [ ] Step ledger 01–03 = `done`
- [ ] `TEST_PLAN.md` has test strategy and scope filled
- [ ] `REQ_REVIEW.md` has traceability matrix (Req → AC mapping)
- [ ] No open Blocking=Yes questions from step-02

If precondition fails → return to the earliest incomplete step. Do **not** write test cases over unresolved blockers.

## Rules

- Edit **only** `TESTCASES.md` in this step.
- Every test case must map to at least one requirement ID from REQ_REVIEW.
- Every AC must have at least one test case covering it.
- Cover three categories per requirement (when applicable):
  - **Positive** — happy path, valid input
  - **Negative** — invalid input, error conditions, unauthorized access
  - **Boundary** — min/max, empty, overflow, edge values
- API test cases must specify: endpoint, method, headers, payload, expected status code, assertions.
- Test data must NOT contain real personal information.
- Steps must be precise enough to repeat.
- Do **not** mark step-04 `done` while any P0 AC has zero test cases.

## Fill these sections in TESTCASES.md

1. **Test cases** — for each case:
   - ID (TC-001, TC-002, …), Priority (P0/P1/P2), Type (Positive/Negative/Boundary/Security/Concurrency)
   - Requirement mapping (REQ-ID, AC-ID)
   - Preconditions, Steps, Test data, Expected result, Verification method
2. **API test cases** — for each API endpoint test:
   - ID (API-001, API-002, …), Priority, Type
   - Endpoint (method + path), Headers, Request payload
   - Expected response (status code, body fields, headers)
   - Assertions (specific, measurable)
3. **Regression checklist** — areas and scenarios to re-verify after fixes.
4. **Test data** — all test data with purpose, source/setup, notes.
5. **Testing gaps** — uncovered areas with risk and suggested follow-up.
6. Fill **Traceability matrix** in `REQ_REVIEW.md` — update TC ID column with the test cases that cover each requirement.
7. Update Step ledger 04

## Coverage rules

| Priority | Minimum coverage                                    |
|----------|-----------------------------------------------------|
| P0       | Positive + Negative + Boundary (all ACs covered)    |
| P1       | Positive + Negative (all ACs; boundary when applicable) |
| P2       | Positive (happy path for all ACs)                   |

## API test case format

```
API-001 | POST /api/users | P0 | Positive
Headers: Content-Type: application/json, Authorization: Bearer {token}
Payload: {"name": "Test User", "email": "test@example.com"}
Assert: status = 201, response.id != null, response.email = "test@example.com"
```

## Spec quality enforcement

Test cases are executable specs — poor test cases create false confidence:

- **Step precision:** can a tester who has never seen this feature execute the steps and get the expected result? If steps say "enter valid data," that is not precise.
- **Traceability:** every test case maps to a requirement ID. Orphan test cases are waste.
- **Coverage discipline:** P0 requirements have positive + negative + boundary. If a P0 AC has only happy-path tests, coverage is insufficient.
- **Expected result specificity:** "Should work" is not an expected result. "Redirect to /dashboard, user name visible in header" is.

If any P0 AC has zero test cases or only positive tests, do not mark step-04 done.

## Done when

- [ ] Every P0/P1 AC has ≥1 test case.
- [ ] Test cases cover positive, negative, and boundary scenarios.
- [ ] API test cases (if in scope) have endpoint, payload, assertions.
- [ ] Every test case maps to a requirement ID.
- [ ] Traceability matrix in REQ_REVIEW.md is updated with TC IDs.
- [ ] Test data does not contain real PII.
- [ ] Testing gaps are documented (not silently ignored).
- [ ] Step ledger 04 = `done`.
- [ ] No leftover `_(TODO)_` on test case fields.

## Next

Read and follow `./step-05-self-check.md`.
