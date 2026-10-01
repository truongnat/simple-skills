# BA trace-graph integrity

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

Epic -> US -> AC -> API -> Test relations carry provenance and resolve cleanly.

## Negative, edge, or blocked case

Broken or unresolved links are surfaced; no graph database or vector-search implementation is claimed.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** relations, provenance, unresolved links, limitation, owner.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-ba-kg -> sk-review.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
