# Wave 2 routing fixtures

Each prompt has one primary owner. If intent is materially ambiguous, ask one clarification instead of invoking two owners for the same claim.

| Prompt class | Expected primary owner | Forbidden ambiguity |
|---|---|---|
| accounting close/reconciliation | `sk-accounting-pro` | generic finance prose |
| payment webhook/idempotency | `sk-fintech-integration-pro` | API design as business integration owner |
| Expo cache/cancellation | `sk-expo-data-fetching` | native UI/testing |
| native safe-area/accessibility | `sk-expo-native-ui` | data-fetching |
| GitHub workflow permissions/rollback | `sk-github-actions-templates` | generic CI prose |
| model drift/canary | `sk-mlops-pro` | generic ML only |
| reentrancy/storage collision | `sk-solidity-security` | generic security only |
| schema migration/restore | `sk-database-migration` | application framework |
| final claim evidence | `sk-verify-pro` | parallel `sk-verification` invocation |
