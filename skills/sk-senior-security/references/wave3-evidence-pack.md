# Authorized threat-model evidence

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A synthetic threat model identifies one blocker with asset, authorization scope, threat, severity and remediation.

## Negative, edge, or blocked case

A bounded residual-risk case is deferred with owner and verification request; no exploit is authorized.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** asset, scope, threat, severity, evidence, remediation, verification, residual risk.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-review -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
