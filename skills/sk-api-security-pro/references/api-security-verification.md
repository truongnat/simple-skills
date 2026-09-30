# API security verification matrix

| Boundary | Case | Expected evidence |
|---|---|---|
| Authentication | Missing, expired, malformed, and wrong-audience token | Correct denial status; no sensitive detail in response |
| Authorization | Horizontal and vertical privilege escalation | Access is denied across tenant/user/role boundaries |
| Input validation | Type confusion, oversized payload, injection strings, unknown fields | Typed validation and bounded resource use |
| Replay/idempotency | Same request or signed webhook repeated | One effect or explicit safe duplicate behavior |
| Rate limiting | Burst, distributed client, and expensive endpoint | Limit is enforced and recovery is observable |
| CORS/CSRF | Untrusted origin and browser credential flow | Policy matches intended clients; unsafe origin blocked |
| Error handling | Dependency/database failure | Stable public error shape; internals excluded |
| Logging | Auth headers, tokens, personal data, payloads | Redaction and correlation without secret leakage |
| Transport | HTTP downgrade or weak TLS configuration | Secure transport enforced in supported environments |

For each case retain request shape, identity/tenant, expected status, response redaction check, audit event, and rollback/mitigation owner.
