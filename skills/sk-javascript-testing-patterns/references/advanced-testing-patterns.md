# Advanced JavaScript Testing Patterns

Use this reference when the task needs examples beyond the compact workflow.

## Integration tests

Use a real boundary where it proves behavior: HTTP handlers, persistence adapters, queues, and serialization. Keep setup deterministic and isolate external services behind test fixtures or disposable environments.

## React and component tests

Test user-observable behavior with Testing Library. Prefer accessible queries, explicit state transitions, and minimal mocking of browser or network boundaries.

## Snapshots, timers, and promises

Use snapshots only for stable, reviewable structures. Restore fake timers and mocks after each test. Assert rejected promises explicitly and keep timeout behavior deterministic.
