# Quick-fix upgrade trigger matrix

| Trigger found | Upgrade target | Required evidence before implementation |
|---|---|---|
| Public API, schema, migration or data-retention change | `sk-business-analysis` → `sk-specify`/`sk-planning` | Policy, compatibility rule, AC/Verify and rollback |
| Authentication, authorization or permission change | BA/security owner → `sk-planning` | Threat/permission decisions and negative AC |
| More than three independently verifiable outputs | `sk-planning` | Decomposed cards, dependency order and DoD |
| Product, UX or stakeholder behavior is ambiguous | `sk-business-analysis` or design owner | Decision owner, resolved assumptions and AC |
| No falsifiable AC + Verify pair | `sk-business-analysis` | Observable outcome and evidence source |
| Cross-service boundary or new dependency | Architecture/API owner → `sk-planning` | Contract, failure mode, rollout and rollback |

Record the trigger, target path, decision owner and artifact handoff in `QUICK.md`. Never keep a fuzzy Quick path after an upgrade trigger is discovered.
