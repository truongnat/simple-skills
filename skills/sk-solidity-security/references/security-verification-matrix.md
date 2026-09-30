# Solidity security verification matrix

Use this reference with the pattern library when reviewing a contract. State chain/runtime, compiler, trust boundaries, privileged roles, upgrade model, oracle assumptions, and whether the review is static, dynamic, fuzz, or adversarial.

## Attack and invariant cases

| Area | Adversarial case | Expected invariant/evidence |
|---|---|---|
| Reentrancy | Callback re-enters before state update | State transition is safe; guarded or checks-effects-interactions evidence |
| Access control | Untrusted caller invokes privileged function | Call reverts and role/admin event is auditable |
| Funds accounting | Deposit, withdrawal, fee, and rounding sequence | Sum of liabilities and balances remains conserved within explicit dust policy |
| Oracle | Stale, manipulated, zero, or extreme price | Freshness/bounds checks reject unsafe price |
| Signature replay | Same signed payload reused across chain, contract, or nonce | Domain separator, nonce, expiry, and chain binding prevent replay |
| Upgradeability | Storage layout change or unauthorized implementation change | Layout compatibility and upgrade authorization are verified |
| Pausing | Emergency pause/unpause and privileged bypass | Pause blocks intended actions without locking recovery path |
| Denial of service | Unbounded loop or hostile callback | Gas and liveness bounds are documented and tested |
| Integer/rounding | Boundary values, zero, max uint, fee rounding | No unexpected overflow, underflow, or value creation |

## Review evidence

Require source/bytecode correspondence, compiler settings, dependency versions, role inventory, event coverage, static-analysis findings, unit tests, fuzz properties, and unresolved assumptions. Treat a passing static scan as evidence for the scanned rules only, not as proof of absence of vulnerabilities.

## Minimum regression suite

Include happy path, unauthorized caller, malformed input, boundary amount, duplicate operation, stale oracle, paused state, upgrade authorization, and failure during external call. For each case record pre-state, action, expected revert/state/event, and post-state invariant.
