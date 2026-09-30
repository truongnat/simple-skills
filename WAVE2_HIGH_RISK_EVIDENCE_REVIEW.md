# Wave 2B — High-risk evidence review and cross-skill handoff

## Scope

Reviewed the nine P1 domain packs after Wave 2A. The review checks that each matrix has domain-specific expected evidence, failure/recovery and limitation handling, synthetic-fixture guidance, and a canonical downstream owner.

## Result

**PASS with one explicit plan correction:** the P1 packs contain eight baseline rows each (74 rows total after restoring the two GitHub Actions cases), and every pack delegates execution/findings/final decision to the owners below. The P2 table in `WAVE2_REMAINING_SKILLS_PLAN.md` lists **20** skills although its prose says 21; Wave 2C covers all 20 listed skills rather than inventing a 21st target.

| Domain skill | Evidence producer | Findings owner | Final decision owner | Adjacent review |
|---|---|---|---|---|
| `sk-accounting-pro` | `sk-tester` | `sk-review` | `sk-verify-pro` | ledger/audit trail, not generic finance prose |
| `sk-expo-data-fetching` | `sk-tester` | `sk-review` | `sk-verify-pro` | API security for token refresh; native UI excluded |
| `sk-expo-native-ui` | `sk-tester` | `sk-review` | `sk-verify-pro` | accessibility and JavaScript test owners remain distinct |
| `sk-financial-analysis-pro` | `sk-tester` | `sk-review` | `sk-verify-pro` | assumptions/units/periods are explicit |
| `sk-fintech-integration-pro` | `sk-tester` | `sk-review` | `sk-verify-pro` | API security owns signature controls; integration owns business state |
| `sk-github-actions-templates` | `sk-tester` | `sk-review-pr` | `sk-verify-pro` | deployment owns rollout mechanics; workflow owns permissions/rollback evidence |
| `sk-hybrid-cloud-networking` | `sk-tester` | `sk-review` | `sk-verify-pro` | provider/IaC/security owners are downstream specialists |
| `sk-mlops-pro` | `sk-tester` | `sk-review` | `sk-verify-pro` | data engineering owns freshness/schema; deployment owns canary execution |
| `sk-solidity-security` | `sk-tester` | `sk-review` | `sk-verify-pro` | security review and API security assist; no formal-assurance claim |

## Review findings closed

- No real secrets, tokens, PAN, PII, private keys, customer payloads, or machine-specific paths were added to fixtures.
- Every P1 matrix contains a recovery or rollback row and a limitation/defer path.
- Every matrix instructs the domain skill not to claim final release status.
- `sk-verification` is not used as a parallel final owner; `sk-verify-pro` is canonical.
- Hybrid networking related-skill bullets were normalized into valid, separate handoff bullets.
- Adjacent ownership is explicit for finance ↔ API security, MLOps ↔ data engineering, Expo ↔ UI/testing, and Actions ↔ deployment.

## Verification packet shape

A P1 domain pack emits `Claim`, `Criteria`, `Evidence`, `Limitations`, and `Next owner`. `sk-tester` executes fixtures, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` decides `pass`, `block`, or `defer`.
