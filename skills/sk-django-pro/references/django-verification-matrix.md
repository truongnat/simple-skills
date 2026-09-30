# Django and DRF verification matrix

| Layer | Scenario | Expected evidence |
|---|---|---|
| Model | Valid, invalid, uniqueness, relationship deletion | Constraint/validation behavior in a transactional test database |
| Migration | Forward apply, fresh install, data transform, rollback decision | Migration plan and post-migration invariant |
| API | Valid serializer, malformed input, permission denial, pagination | Status/body contract and query count/shape |
| Auth/CSRF | Anonymous, authenticated, wrong tenant, unsafe browser request | Explicit 401/403/CSRF behavior and no data leakage |
| Query | N+1, filtering, ordering, transaction boundary | `assertNumQueries` or measured query evidence |
| Admin | Allowed/denied actions and sensitive fields | Admin permission and audit behavior |
| Async/signals | Retry, duplicate delivery, side-effect failure | Idempotent handler and observable failure |
| Operations | Static assets, health, logging, secret/config separation | Deployment smoke check without secret exposure |

Use fixtures/factories with explicit tenant and timezone assumptions. Do not treat Django's built-in protections as proof that application-level authorization and object ownership are correct.
