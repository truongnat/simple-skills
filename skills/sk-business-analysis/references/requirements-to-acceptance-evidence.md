# Requirements-to-acceptance evidence

Use this pack to turn a business problem into testable, traceable decisions without inventing stakeholder policy.

| Artifact element | Required evidence |
|---|---|
| Problem | One-sentence problem, affected actor, measurable consequence |
| Stakeholders | Actor, goal, pain, authority and unresolved decision owner |
| Scope | In-scope, out-of-scope, non-goals and capability gaps |
| Business rule | Stable `BR-*` ID, rule statement, source/owner and exception |
| User story | Stable `US-*` ID, actor, intent, value and assumptions |
| Acceptance criterion | Stable `AC-*` ID, Given/When/Then or equivalent falsifiable result |
| Risk/unknown | Impact, blocking status, resolution question and decision owner |
| Handoff | Next skill, artifact path, trace IDs and readiness status |

Worked scenario: if a refund policy is unclear, stop before writing final AC; record the policy question, affected flows, provisional assumption, and owner. When resolved, update the same trace IDs and show which AC changed. A complete BA handoff is not a list of open questions: it is a decision-ready artifact with explicit blockers or a justified Ready status.
