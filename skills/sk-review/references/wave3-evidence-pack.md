# General review finding packet

This Wave 3 fixture is synthetic and illustrative. It records a bounded claim; it does not execute connectors, tests, deployments, exploit activity, or release approval.

## Positive or selected case

A review criterion identifies a severity-graded finding at a stable evidence location.

## Negative, edge, or blocked case

A clean or insufficient-evidence review cannot invent a finding or release decision.

## Evidence packet

- **Claim:** one bounded domain/artifact claim only.
- **Acceptance evidence:** criterion, finding, severity, confidence, evidence location, limitation, remediation owner.
- **Limitations:** assumptions, unsupported features, stale inputs, unverified environments, and residual risk are listed explicitly.
- **Next owner:** sk-tester -> sk-verify-pro.
- **Final decision:** `sk-verify-pro` owns `pass`, `block`, or `defer`; this fixture never makes that decision.
