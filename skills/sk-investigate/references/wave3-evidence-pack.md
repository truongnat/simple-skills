# Investigation reproduction evidence

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A synthetic defect has observation, reproduction steps, competing root-cause candidates and confidence.

## Negative, edge, or blocked case

A non-reproducible case separates hypotheses from facts and defers remediation.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** observation, hypothesis, reproduction, candidates, confidence, evidence paths, limitations.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-investigate -> sk-review -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
