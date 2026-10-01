# Quick-fix scope gate

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A bounded one-file remediation has scope proof, focused checks, residual risk and rollback.

## Negative, edge, or blocked case

Broad or unclear refactoring is rejected and redirected to planning; no test or release claim is made.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** selected change, scope proof, checks, residual risk, rollback, owner.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-quick-fix -> sk-planning -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
