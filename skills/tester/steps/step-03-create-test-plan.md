# Step 03 — Create test plan

## Goal

Define test strategy, scope, estimation, environment needs, and risk mitigation. Produce `TEST_PLAN.md`.

## Precondition (fail closed)

- [ ] Step ledger 01 = `done`
- [ ] Step ledger 02 = `done` (not `todo` / `blocked`)
- [ ] `REQ_REVIEW.md` has Clarity assessment filled (no `_(TODO)_` on verdicts)
- [ ] No open Blocking=Yes questions in REQ_REVIEW.md

If precondition fails → return to step-02. Do **not** plan over unresolved requirement blockers.

## Rules

- Edit **only** `TEST_PLAN.md` in this step.
- Do **not** write test cases yet — that is step-04.
- Strategy must be informed by REQ_REVIEW findings (reference specific gaps/risks).
- Estimation must be explicit (numbers, not "it depends").
- Do **not** skip risk assessment — every plan has risks.
- Test types should match the project context (web vs mobile vs API vs embedded).

## Fill these sections in TEST_PLAN.md

1. **Test scope** — in scope, out of scope, assumptions (reference REQ_REVIEW for scope boundaries).
2. **Test strategy** — approach by level (unit → integration → E2E → manual), test types included/excluded with rationale.
3. **Test estimation** — technique used, effort breakdown by phase with hours/days.
4. **Environment requirements** — servers, browsers, devices, test accounts, test data, third-party dependencies.
5. **Risk assessment** — risks with impact, likelihood, mitigation, priority.
6. **Schedule & milestones** — phases with start/end dates, entry/exit criteria.
7. **Deliverables** — list of artifacts this cycle produces.
8. Update Step ledger 03

## Estimation guidance

Choose one technique and apply consistently:

- **Test-point analysis:** Count ACs per feature, weight by complexity (1-3), sum = test points. 1 test point ≈ 2-4 hours.
- **Story-point mapping:** Map dev story points to test effort ratio (typically 20-30% of dev effort).
- **AC-based counting:** Count acceptance criteria, estimate cases per AC (happy + negative + boundary ≈ 3-5 cases per AC).

## Spec quality enforcement

The test plan itself is a spec — it must be reviewable and auditable:

- **Strategy clarity:** can a new tester read the strategy and know what to test, what to skip, and why?
- **Estimation honesty:** every estimate has a technique and numbers. "It depends" is not an estimate.
- **Risk specificity:** every risk has a concrete mitigation, not "we'll deal with it."
- **Environment completeness:** every dependency is listed — if it is not in the plan, it will bite during execution.

If the plan has TBD sections or vague strategy, fix before marking step-03 done.

## Done when

- [ ] Test scope references REQ_REVIEW findings.
- [ ] Strategy covers at least functional + regression testing.
- [ ] Estimation has explicit numbers per phase.
- [ ] Environment requirements list all dependencies.
- [ ] Risk assessment has ≥1 real risk (or explicit "no material risks" with evidence).
- [ ] Schedule has entry/exit criteria per phase.
- [ ] Step ledger 03 = `done`.
- [ ] No leftover `_(TODO)_` on required fields.

## Next

Only if Step ledger 03 = `done`: Read and follow `./step-04-develop-test-cases.md`.
