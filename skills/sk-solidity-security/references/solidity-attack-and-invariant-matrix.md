# Solidity attack and invariant matrix

Use this matrix after the compact workflow when the task involves a high-risk claim. Fixtures must use synthetic identifiers and redacted values. The domain skill produces evidence; `sk-tester` executes tests, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` owns the final `pass`/`block`/`defer` decision.

| Scenario | Expected result | Evidence | Failure/limitation | Next owner |
|---|---|---|---|---|
| Reentrancy | A malicious callback cannot drain funds or violate accounting during an external call. | Adversarial test trace and invariant result. | A passing unit test without adversarial path is insufficient. | sk-tester -> sk-verify-pro |
| Access control | Unauthorized caller cannot invoke privileged state transitions; role changes are auditable. | Caller matrix, revert trace and event log. | Default admin assumptions must be explicit. | sk-review -> sk-verify-pro |
| Oracle manipulation | Stale/outlier oracle input is rejected or bounded before pricing-sensitive mutation. | Oracle fixture, freshness check and invariant output. | Economic assumptions require domain review. | sk-review -> sk-verify-pro |
| Upgrade/storage collision | Upgrade layout preserves storage slots and rejects incompatible implementation. | Storage layout diff and upgrade simulation. | Proxy admin key handling is out of scope and handed off. | sk-security-review -> sk-verify-pro |
| Integer/rounding | Boundary values and rounding direction preserve conservation and never create excess funds. | Fuzz/property test report and balance invariant. | Unchecked casts block pass. | sk-tester -> sk-verify-pro |
| Signature replay | A signature cannot be reused across chain, contract, nonce or deadline domains. | Domain-separator fixture and replay rejection trace. | Private keys remain synthetic. | sk-api-security-pro -> sk-verify-pro |
| Pause/emergency | Pause blocks defined risky operations while preserving documented recovery and withdrawal paths. | State-machine test and emergency runbook check. | Pause authority and unpause owner are named. | sk-review -> sk-verify-pro |
| Failure/limitation | Any unmodeled economic or governance assumption is recorded as defer with owner. | Assumption register and residual-risk decision. | Do not claim formal assurance from heuristic tests. | sk-verify-pro |

## Verification response shape

Return exactly:

- **Claim:** the bounded domain claim being assessed.
- **Criteria:** scenario rows and acceptance thresholds.
- **Evidence:** paths, commands, fixture IDs, timestamps and reviewer findings.
- **Limitations:** untested environments, assumptions, stale inputs or residual risk.
- **Next owner:** `sk-tester`, `sk-review`, `sk-review-pr`, the named domain owner, or `sk-verify-pro`.

Do not claim final release status from this matrix; hand the packet to `sk-verify-pro`.
