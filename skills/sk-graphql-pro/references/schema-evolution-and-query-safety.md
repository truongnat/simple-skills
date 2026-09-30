# GraphQL schema evolution and query safety

| Concern | Expected evidence |
|---|---|
| Field addition | Existing operations remain valid; resolver has auth, nullability, and latency behavior |
| Field deprecation | Usage inventory, replacement guidance, owner, and removal date |
| Nullability change | Generated/client type impact and partial-data behavior are reviewed |
| Enum change | Unknown-value handling and client compatibility are tested |
| N+1 | Resolver trace or query count demonstrates batching/DataLoader behavior |
| Expensive query | Depth/complexity/cost limit, timeout, and rejection response are defined |
| Authorization | Field/object access is tested for allowed and denied identities |
| Federation change | Composition, ownership, entity references, and rollout order are verified |
| Mutation retry | Idempotency and duplicate side-effect behavior are explicit |

A schema check should include representative persisted operations, introspection policy, error shape, query budget, resolver metrics, and a rollback or forward-fix decision.
