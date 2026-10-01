# System-design capacity and failure decision

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A selected topology meets stated load/failure assumptions with data flow, SLO and rollout/rollback.

## Negative, edge, or blocked case

A rejected design records trade-offs and blocks when capacity or failure evidence is unresolved.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** context, alternatives, data flow, SLO, observability, failure modes, capacity, rollout, evidence.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-system-design-pro -> sk-review -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
