# Fintech integration reference

Use this reference after the core workflow identifies the provider, integration mode, authentication model, and assurance level. Treat provider documentation and sandbox behavior as authoritative; examples below are provider-neutral patterns, not a substitute for current API documentation.

## Integration contract

Before implementing, record:

| Area | Required decision |
|---|---|
| Provider and environment | Provider, API version, sandbox/live mode, supported regions and currencies |
| Authentication | API key, OAuth, mTLS, signed request, token rotation and storage owner |
| Data contract | Request/response schema, idempotency key, pagination, timestamps, currency units |
| Reliability | Timeout, retry policy, rate-limit handling, deduplication, circuit breaking |
| Events | Webhook events, signature verification, replay window, ordering, dead-letter handling |
| Operations | Logging redaction, metrics, alerts, reconciliation, support and rollback owner |

Never put live credentials, card data, bank credentials, or personally identifiable financial data in source code, fixtures, logs, or examples.

## Payment flow pattern

A payment integration should separate intent creation, customer confirmation, asynchronous event processing, and internal order state. Do not mark an order paid solely because a client request returned successfully.

```text
client -> create payment intent -> provider
provider -> confirmation/webhook -> verified webhook endpoint
verified event -> idempotent event handler -> order ledger
order ledger -> fulfillment and customer notification
```

Recommended internal states are `created`, `requires_action`, `processing`, `succeeded`, `failed`, `refunded`, and `disputed`. Map provider-specific states explicitly and preserve the original provider event ID.

### Idempotency

Generate an idempotency key from the business operation, not from an arbitrary retry counter. Persist the key, request fingerprint, provider response, and final internal state. A retry with the same key must return the original result; a reused key with a different payload must fail safely and be investigated.

### Amounts and currency

Represent money as integer minor units plus an explicit ISO currency code. Validate currency precision and rounding rules before sending the request. Never calculate payment amounts with binary floating point when exact decimal arithmetic is available.

## Webhook handling

1. Read the raw request body before JSON parsing.
2. Verify the provider signature using the configured secret and a bounded timestamp tolerance.
3. Reject malformed, unsigned, stale, or unverifiable events.
4. Persist the provider event ID before performing side effects.
5. Return a fast acknowledgement only after durable receipt, then process asynchronously when provider guidance allows it.
6. Make the handler idempotent and tolerate duplicate delivery.
7. Record ordering assumptions; do not assume events arrive in business order.
8. Send poison events to a reviewable dead-letter path with redacted diagnostics.

Do not trust a customer ID, amount, currency, or status supplied by the browser. Load authoritative values from the verified provider event and compare them with the internal order.

## Authentication and secrets

Keep credentials in a secret manager or platform secret store. Separate sandbox and production credentials, restrict scopes, rotate on a defined schedule, and make the owner and expiry visible. OAuth integrations should validate state, redirect URI, token audience, expiry, and refresh failure behavior. mTLS integrations need certificate rotation, clock synchronization, and a tested fallback/rollback plan.

## Reliability and rate limits

Use bounded timeouts and retry only transient failures. Do not retry validation errors, declined payments, authentication failures, or non-idempotent writes without a provider-supported idempotency key. Apply exponential backoff with jitter, respect `Retry-After`, and expose rate-limit metrics. A circuit breaker should fail with a user-safe state and preserve reconciliation work for later recovery.

## Reconciliation

Run reconciliation independently of webhook delivery. Compare internal records with provider reports using provider IDs, amount, currency, status, and settlement date. Classify differences as missing internal record, missing provider record, amount mismatch, currency mismatch, status mismatch, duplicate, or timing difference. Every automatic repair must be idempotent and auditable; ambiguous differences require review rather than silent correction.

## Security and observability checklist

- Redact credentials, authorization headers, full account numbers, and sensitive payload fields.
- Log correlation ID, provider request ID, event ID, endpoint, latency, outcome, and safe error class.
- Alert on signature failures, duplicate-event spikes, retry exhaustion, reconciliation drift, and unusual decline rates.
- Keep sandbox/live endpoints and secrets visibly distinct.
- Review PCI, privacy, retention, and regional obligations with the responsible compliance owner.

## Verification matrix

| Scenario | Expected result | Evidence |
|---|---|---|
| Same payment request retried with same idempotency key | One provider operation and one internal payment | Stored key, provider ID, event log |
| Same key reused with changed amount | Request rejected; original operation unchanged | Validation error and audit record |
| Invalid webhook signature | 4xx response; no state change or side effect | Redacted security log |
| Duplicate webhook event | 2xx/replay-safe handling; one fulfillment | Event deduplication record |
| Webhook arrives out of order | State transition follows explicit policy; no downgrade from terminal state | Transition log |
| Provider timeout after accepted write | Safe retry/reconciliation path; no duplicate charge | Retry trace and reconciliation result |
| Rate limit response | Bounded backoff; no hot loop; alert if exhausted | Retry-After handling and metric |
| Refund/chargeback event | Internal state and ledger updated exactly once | Event ID, ledger entry, notification status |
| Credential appears in error payload | Secret and sensitive fields redacted | Log inspection |
| Reconciliation amount mismatch | No silent repair; discrepancy classified and queued | Reconciliation report |

## Delivery checklist

Before production, verify sandbox tests, provider version, secret rotation, webhook replay handling, idempotency, rate-limit behavior, reconciliation, monitoring, runbook, rollback, and ownership. Record evidence and unresolved provider-specific assumptions in the final artifact.
