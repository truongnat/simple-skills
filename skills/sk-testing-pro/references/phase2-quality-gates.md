# Testing quality gates

Use these gates to evaluate a test suite beyond pass/fail and line coverage.

- **Behavior:** critical business rules have positive, negative, boundary, and authorization cases.
- **Isolation:** tests are repeatable in random order and parallel execution where supported.
- **Observability:** failures retain assertion context, logs/traces, fixture/version, and cleanup result.
- **Mutation/value:** survived mutations are reviewed by business impact; coverage is not treated as proof.
- **Flake control:** retries are measured, quarantined tests have owners, and retries do not convert failure to silent success.
- **Contract:** integration boundaries validate schema, error shape, idempotency, and compatibility.
- **Security:** fixtures contain no real secrets or personal data; auth and tenant boundaries are explicit.
- **Release evidence:** record suite scope, environment, test version, pass-on-first-attempt rate, known exclusions, and sign-off.
