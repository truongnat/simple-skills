# Security review evidence and severity

## Minimum evidence

Capture asset and trust boundary, attack precondition, affected principal/data, reproducible steps or reasoning, observed impact, control that should prevent it, remediation owner, and retest result. Redact secrets and use synthetic identifiers.

## Severity guide

| Severity | Typical impact | Required action |
|---|---|---|
| Critical | Remote compromise, broad secret/tenant exposure, unauthorized funds/control | Block release; contain and retest |
| High | Privilege escalation, material data exposure, reliable bypass | Owner and fix before release unless explicitly accepted |
| Medium | Limited scope or stronger preconditions | Fix in planned window with compensating control |
| Low | Defense-in-depth or low-impact disclosure | Track, explain, and monitor |

Do not downgrade solely because exploitation was not observed; document the missing precondition and confidence separately.
