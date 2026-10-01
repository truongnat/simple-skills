# BA integration map failure boundary

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A synthetic Jira/Confluence map records actors, exchanged information and lifecycle state.

## Negative, edge, or blocked case

Permission failure or external write requires explicit approval and next owner; no connector is executed.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** actors, systems, information, lifecycle, failure, approval, owner.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-ba-integrate -> sk-review.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
