# Fintech integration validation matrix

Use this matrix after the compact workflow when the task involves a high-risk claim. Fixtures must use synthetic identifiers and redacted values. The domain skill produces evidence; `sk-tester` executes tests, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` owns the final `pass`/`block`/`defer` decision.

| Scenario | Expected result | Evidence | Failure/limitation | Next owner |
|---|---|---|---|---|
| Idempotency | A repeated payment request with the same key creates one business effect and one ledger reference. | Replay trace, idempotency record, reconciliation result. | Key reuse across different payloads blocks processing. | sk-tester -> sk-verify-pro |
| Webhook signature | Valid signatures are accepted; invalid, missing and stale signatures are rejected before mutation. | Signed fixtures, verification result, no-mutation assertion. | Never use production secrets in fixtures. | sk-api-security-pro -> sk-verify-pro |
| Webhook replay | A delivered event ID is acknowledged safely on replay without duplicate fulfillment. | Event ledger and replay response trace. | Retention window must be explicit. | sk-review -> sk-verify-pro |
| Timeout/retry | Bounded retries use backoff and preserve the same idempotency key. | Retry schedule, attempt count, final state. | Do not retry unknown side effects blindly. | sk-tester -> sk-verify-pro |
| Refund/chargeback | Refund and chargeback states are modeled separately and reconcile to the processor report. | State transition log and reconciliation fixture. | Manual exception owner is named. | sk-fintech-integration-pro -> sk-review |
| Rate limits | Provider throttling produces bounded backoff and customer-safe status without request storms. | 429 fixture, rate-limit headers, metrics trace. | Backoff exhaustion is an explicit failure. | sk-tester -> sk-verify-pro |
| Token leakage | Logs, errors and analytics contain redacted tokens, PAN and PII. | Redaction test output and log scan. | Synthetic values only; no real payment data. | sk-security-review -> sk-verify-pro |
| Reconciliation | Internal transactions, provider events and settlement totals agree or produce a named exception. | Three-way reconciliation report and exception queue. | Unresolved variance blocks final claim. | sk-review -> sk-verify-pro |

## Verification response shape

Return exactly:

- **Claim:** the bounded domain claim being assessed.
- **Criteria:** scenario rows and acceptance thresholds.
- **Evidence:** paths, commands, fixture IDs, timestamps and reviewer findings.
- **Limitations:** untested environments, assumptions, stale inputs or residual risk.
- **Next owner:** `sk-tester`, `sk-review`, `sk-review-pr`, the named domain owner, or `sk-verify-pro`.

Do not claim final release status from this matrix; hand the packet to `sk-verify-pro`.
