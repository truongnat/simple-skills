# Spring Boot service verification matrix

| Layer | Scenario | Expected evidence |
|---|---|---|
| Controller | Valid request, validation error, unknown route | Status/body contract and stable error shape |
| Security | Missing, wrong, insufficient, and valid authority | 401/403 behavior and method-level authorization evidence |
| Service | Domain success and invariant violation | Unit test isolates rule and preserves transaction boundary |
| Repository | Query result, absent entity, constraint conflict | `@DataJpaTest` or equivalent fixture and SQL/index expectation |
| Transaction | Commit, rollback, timeout, duplicate request | Atomicity and idempotency evidence |
| Configuration | Test/profile/production property differences | Startup check and secret/config source review |
| Integration | Real HTTP + persistence + security path | `@SpringBootTest`/MockMvc fixture with cleanup |
| Operations | Health, readiness, metrics, structured error/logging | Actuator evidence without leaking secrets |

Prefer constructor injection and explicit transaction ownership. A green slice test is not proof that serialization, security filters, transactions, and database behavior work together.
