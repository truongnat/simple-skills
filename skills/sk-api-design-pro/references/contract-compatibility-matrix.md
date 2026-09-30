# API contract compatibility matrix

Classify every proposed change against known consumers, compatibility window, and rollout order. Treat generated clients, mobile releases, webhooks, and third-party integrations as clients even when they are not in the same repository.

| Change | Compatibility risk | Required evidence |
|---|---|---|
| Add optional response field | Usually compatible | Consumer tolerance and contract test |
| Add required request field | Breaking | Versioned contract or staged default/backfill |
| Rename/remove field | Breaking | Usage inventory, deprecation window, absence proof |
| Narrow enum/value set | Breaking | Client value inventory and migration plan |
| Change error/status semantics | Often breaking | Error contract fixtures and retry/idempotency review |
| Change pagination/order | Behavior breaking | Stable cursor/order and consumer expectation |
| Change webhook payload | Breaking for signatures/parsers | Versioned schema, replay fixture, signature verification |
| Change timeout/retry | Operationally breaking | Client budget, idempotency, load and failure evidence |

Minimum contract evidence: example request/response, error cases, authentication scope, idempotency key behavior, compatibility window, consumer owner, deprecation date, and rollback/forward-fix plan.
