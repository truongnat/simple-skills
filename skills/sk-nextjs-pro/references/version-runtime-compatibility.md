# Next.js version and runtime compatibility

Record Next.js major, React version, router mode, rendering/runtime target, hosting adapter, and cache semantics before changing framework code.

| Change | Compatibility checks |
|---|---|
| Pages → App Router | Data fetching, layouts, loading/error boundaries, metadata, and client boundaries |
| Server → Client component | Bundle cost, serializable props, secrets, hydration, and browser-only APIs |
| Node → Edge runtime | Node API usage, package compatibility, crypto, filesystem, and latency region |
| Fetch/cache change | Revalidation tags/paths, stale data expectation, invalidation owner, and cost |
| Server Action/Route Handler | Auth, CSRF/origin policy, idempotency, error serialization, and progressive enhancement |
| Next major upgrade | Codemod output, removed APIs, build output, image/font behavior, and smoke routes |
| Self-host/Vercel change | Environment variables, headers, assets, ISR/cache persistence, and observability |

Required evidence: typecheck/build, representative server/client route tests, cache invalidation scenario, denied-auth scenario, production-like runtime smoke test, and documented rollback or forward-fix path.
