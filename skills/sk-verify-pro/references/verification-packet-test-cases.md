# Verification packet test cases

Use this reference when an upstream skill hands evidence to `sk-verify-pro`. The examples are fixtures for the contract, not claims that a domain check was run.

## Required packet fields

| Field | Requirement |
|---|---|
| Claim | One precise completion, merge, release, or acceptance claim |
| Criteria | Acceptance criteria, plan checkpoint, review policy, or domain invariant |
| Evidence | Fresh command output, test report, artifact link, screenshot plus semantic check, or named human check |
| Coverage map | Criterion-to-evidence mapping; uncovered criteria are explicit |
| Limitations | Staleness, unavailable environment, deferred manual review, or domain uncertainty |
| Decision | Exactly `pass`, `block`, or `defer` |
| Next owner | Owner and unblock condition when not `pass` |

## Status semantics

- **`pass`** — every required criterion is covered by fresh, sufficient evidence; known limitations do not invalidate the claim.
- **`block`** — a required criterion is unmet, evidence is missing/stale, or a blocker remains. Do not close or publish.
- **`defer`** — a named human or domain owner must decide something that cannot be inferred safely. Record the exact question and do not describe it as passed.

## Canonical lifecycle cases

### VP-LIFE-001 — Complete handoff — `pass`

- **Claim:** The prepared artifact is ready for final verification.
- **Criteria:** Scope and acceptance criteria are approved; artifact path is stable; checks are complete.
- **Evidence:** Handoff packet links the artifact, test/review results, freshness, and coverage map.
- **Coverage map:** Every acceptance criterion maps to at least one evidence item.
- **Limitations:** None material.
- **Decision:** `pass`.
- **Next owner:** `sk-verify-pro` records `VERIFY.md`; `sk-done` may consume it.

### VP-LIFE-002 — Missing acceptance mapping — `block`

- **Claim:** The implementation is complete.
- **Criteria:** Story/specification includes AC-001 through AC-004.
- **Evidence:** Tests exist, but AC-003 and AC-004 have no result or artifact link.
- **Coverage map:** AC-001/002 covered; AC-003/004 uncovered.
- **Limitations:** Evidence is incomplete.
- **Decision:** `block`.
- **Next owner:** `sk-tester` or implementation owner adds evidence for AC-003/004.

### VP-LIFE-003 — Human/domain decision pending — `defer`

- **Claim:** The design is acceptable for release.
- **Criteria:** Accessibility, legal, security, or product-owner approval is required.
- **Evidence:** Automated checks pass; the required named approver has not reviewed the artifact.
- **Coverage map:** Automated criteria covered; approval criterion pending.
- **Limitations:** Human decision is unavailable.
- **Decision:** `defer`.
- **Next owner:** Named approver answers the exact open question; no release claim until then.

## Expo data-fetching cases

### VP-EXPO-DATA-001 — Valid response and cache — `pass`

- **Claim:** The screen loads and caches valid API data safely.
- **Criteria:** 2xx parsing, intended query key, rendered state, and no secret in client output.
- **Evidence:** Deterministic mocked response, query-key assertion, rendered-state assertion, and bundle/env inspection.
- **Coverage map:** Each criterion points to a test result or captured artifact.
- **Limitations:** Real network performance is out of scope.
- **Decision:** `pass` only when all mapped checks are fresh.

### VP-EXPO-DATA-002 — Invalid schema cached — `block`

- **Claim:** The data-fetching implementation is production-ready.
- **Criteria:** Malformed payload must surface a typed error and must not enter cache.
- **Evidence:** Fixture shows parse error, but cache inspection shows invalid data retained.
- **Coverage map:** Error rendering covered; cache safety failed.
- **Limitations:** None required to classify the failure.
- **Decision:** `block`.
- **Next owner:** Expo data-fetching implementation owner fixes validation/invalidation and reruns the case.

### VP-EXPO-DATA-003 — Offline/device behavior pending — `defer`

- **Claim:** Offline launch and token refresh are safe on supported devices.
- **Criteria:** Offline cache behavior, cancellation, refresh concurrency, and logout during refresh.
- **Evidence:** Unit fixtures pass; supported-device/network transition test has not run.
- **Coverage map:** Unit criteria covered; device/network criterion pending.
- **Limitations:** No fresh device/network evidence.
- **Decision:** `defer`.
- **Next owner:** `sk-expo-data-fetching` owner or named device tester runs the missing matrix.

## Expo native UI cases

### VP-EXPO-UI-001 — Accessible responsive state set — `pass`

- **Claim:** The component is ready for supported iOS, Android, and web targets.
- **Criteria:** Safe area/keyboard, dynamic type, screen reader semantics, touch targets, reduced motion, loading/error/empty states, and responsive layout.
- **Evidence:** Device matrix with SDK/size/font-scale/accessibility settings, semantic assertions, and approved visual comparisons.
- **Coverage map:** Every platform/state criterion maps to evidence; screenshots alone are insufficient.
- **Limitations:** Intentional platform deviations are documented.
- **Decision:** `pass` only after deviations are accepted.

### VP-EXPO-UI-002 — Keyboard or focus failure — `block`

- **Claim:** The form is accessible and usable.
- **Criteria:** Focus order, keyboard reachability, error announcement, and touch target size.
- **Evidence:** Screenshot looks correct, but keyboard covers the submit control and error is not announced.
- **Coverage map:** Visual layout covered; semantic/keyboard criteria failed.
- **Limitations:** None material.
- **Decision:** `block`.
- **Next owner:** Native UI implementation owner fixes the state and reruns semantic/device checks.

### VP-EXPO-UI-003 — Manual visual approval pending — `defer`

- **Claim:** The visual interaction states match the approved design.
- **Criteria:** Loading, error, empty, pressed, dark-mode and reduced-motion states.
- **Evidence:** Automated semantic checks pass; final product/design review is pending.
- **Coverage map:** Semantic criteria covered; visual approval criterion pending.
- **Limitations:** Automated tests cannot authorize subjective visual approval.
- **Decision:** `defer`.
- **Next owner:** Named design/product reviewer.

## JavaScript testing-pattern cases

### VP-JS-TEST-001 — Deterministic test suite — `pass`

- **Claim:** The test suite provides reliable evidence for the target behavior.
- **Criteria:** User-observable assertion, deterministic fixture, explicit rejected-promise handling, and restored timers/mocks.
- **Evidence:** Fresh test output, fixture description, coverage map, and teardown result.
- **Coverage map:** Target behavior and failure path each have an assertion.
- **Limitations:** External service behavior is covered by contract/integration tests separately.
- **Decision:** `pass`.

### VP-JS-TEST-002 — Flaky or leaking test — `block`

- **Claim:** The suite is safe to use as release evidence.
- **Criteria:** Tests are isolated and restore fake timers/mocks after each case.
- **Evidence:** Intermittent failure or leaked mock changes the result of a later test.
- **Coverage map:** Target assertion exists; isolation criterion fails.
- **Limitations:** A green rerun does not erase the leak.
- **Decision:** `block`.
- **Next owner:** Test owner fixes isolation and supplies a repeatable run.

### VP-JS-TEST-003 — External integration environment unavailable — `defer`

- **Claim:** The HTTP/persistence boundary is verified end-to-end.
- **Criteria:** Disposable integration environment and real boundary behavior.
- **Evidence:** Unit/component tests pass; integration environment is unavailable.
- **Coverage map:** Local behavior covered; boundary criterion pending.
- **Limitations:** No fresh integration evidence.
- **Decision:** `defer`.
- **Next owner:** Named integration-test owner provisions the environment and reruns the boundary case.

## Handoff rule

Upstream skills produce domain evidence; `sk-verify-pro` decides claim sufficiency. `sk-done` or a release owner may consume only a `pass`. `block` returns to the producing owner. `defer` records a named decision owner and must never be summarized as complete.
