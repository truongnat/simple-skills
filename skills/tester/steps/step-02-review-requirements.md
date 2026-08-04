# Step 02 — Review requirements

## Goal

Review BA artifacts (BUSINESS_ANALYSIS.md, PRD, USER_FLOW, etc.) for clarity, testability, and completeness. Produce `REQ_REVIEW.md` with assessment of every requirement.

## Precondition (fail closed)

- [ ] Step ledger 01 = `done` in all 5 artifacts
- [ ] `REQ_REVIEW.md` exists and contains headings `Step ledger` and `Requirement inventory`
- [ ] At least one upstream BA artifact exists (BUSINESS_ANALYSIS.md, PRD.md, BRD.md, URD.md, or equivalent requirements source)

If precondition fails → return to step-01. Do **not** continue.

## Rules

- Edit **only** `REQ_REVIEW.md` in this step.
- Do **not** write test cases yet — that is step-04.
- Do **not** write test plan yet — that is step-03.
- Do **not** accept requirements at face value — challenge every one.
- Do **not** proceed past this step with Blocking=Yes questions unanswered.
- Every requirement must be assessed for both **clarity** and **testability**.
- Separate confirmed facts from assumptions from open questions.

## Fill these sections in REQ_REVIEW.md

1. **Requirement inventory** — list every requirement from upstream artifacts with ID, source, title, type (FR/NFR/AC/US).
2. **Clarity assessment** — for each requirement:
   - Clarity: `Clear` / `Ambiguous` / `Missing`
   - Testability: `Yes` / `No` / `Partial`
   - Evidence: quote or section reference from source artifact
   - Notes: why ambiguous, what is missing, what assumption is needed
3. **Completeness check** — for each feature area, check 7 axes:
   - Happy path, error handling, boundary conditions, permissions/roles, data validation, concurrency, state transitions
4. **Feasibility assessment** — for technically risky requirements:
   - Technical risk, external dependencies, verdict (Pass/Fail/Unknown)
5. **Traceability matrix** — map Req ID → User Story → AC → Test Case ID (leave TC column empty for now)
6. **Q&A items** — every unclear requirement becomes a question with target (BA/PM/Dev), blocking flag
7. **Risk assessment** — risks from requirement gaps
8. Update Step ledger 02

## Mandatory stop gate

**STOP and wait for user answers when:**

- Any P0/P1 requirement has Clarity = `Ambiguous` or `Missing` AND is Blocking
- Testability = `No` for a critical requirement
- Feasibility = `Fail` or `Unknown` for a must-have requirement
- More than 30% of requirements are Ambiguous or Missing

Do not proceed to test planning with unresolved blocking questions.

## Spec quality enforcement

Every requirement from upstream artifacts must pass a quality check before test planning can use it:

- **Clarity:** is the requirement unambiguous? Can two engineers read it and implement the same thing?
- **Testability:** can a test be written that proves pass/fail? "Should work well" fails; "Response time < 2s under 100 concurrent users" passes.
- **Completeness:** are error handling, boundary conditions, and permissions specified?
- **Traceability:** does the requirement link to a user story or business objective?

If >30% of requirements fail clarity or testability, this is a **blocking spec quality issue** — stop and request BA/PM clarification before proceeding.

## Done when

- [ ] Every requirement from upstream artifacts has a row in Requirement inventory.
- [ ] Every requirement has Clarity and Testability assessed.
- [ ] Completeness check covers all feature areas with 7-axis analysis.
- [ ] Traceability matrix maps requirements to ACs (TC column can be empty).
- [ ] Blocking questions are in Q&A items with target and blocking flag.
- [ ] Step ledger 02 = `done` or `blocked` (with questions asked).
- [ ] No leftover `_(TODO)_` on Clarity/Testability verdicts unless blocked.

## Next

Only if Step ledger 02 = `done`: Read and follow `./step-03-create-test-plan.md`.
If `blocked`: stop for user answers.
