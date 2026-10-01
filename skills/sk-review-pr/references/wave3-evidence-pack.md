# Pull-request review readiness packet

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A synthetic diff exposes a missing regression test or security check and receives an evidence-backed recommendation.

## Negative, edge, or blocked case

A clean diff still records changed files, scope and explicit verification limitations.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** diff summary, changed files, regression/test/security risk, recommendation, evidence paths.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-review-pr -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
