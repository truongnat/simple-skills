# Phase 2 — Security, testing & reliability upgrade

## Scope

The 20 skills in Group 06 were reviewed. This phase adds focused verification packs to the highest-risk skills and preserves existing deep reference bundles for the remaining mature skills.

## New focused packs

| Skill | New material |
|---|---|
| `sk-ai-red-teaming-pro` | Prompt injection, jailbreak, tool misuse, exfiltration, over-refusal, regression matrix |
| `sk-api-security-pro` | AuthN/AuthZ, validation, replay, rate limits, CORS/CSRF, logging and transport cases |
| `sk-auth-implementation-patterns` | Login/session/MFA/reset/authorization/secrets regression cases |
| `sk-e2e-testing-patterns` | Isolation, async races, selectors, external dependencies, retries, parallelism and cleanup |
| `sk-security-review` | Review evidence contract and severity/triage guide |
| `sk-debugging-strategies` | Incident evidence from detection through learning |
| `sk-performance-tuning-pro` | Baseline, tail latency, capacity, cost, regression and recovery gates |
| `sk-testing-pro` | Behavior, isolation, observability, mutation, flake, contract, security and release gates |

## Existing skills covered by mature references

`sk-auth-pro`, `sk-bug-discovery-pro`, `sk-debugging-investigation`, `sk-distributed-tracing`, `sk-nextjs-security-scan`, `sk-sast-configuration`, `sk-security-pro`, `sk-senior-security`, `sk-solidity-security`, `sk-stride-analysis-patterns`, `sk-systematic-debugging-pro`, and `sk-test-driven-development-pro` already contain focused reference bundles or received one in Phase 1. They remain in the catalog-wide validation pass rather than receiving duplicate content.

## Acceptance evidence

Each new pack is linked from its owning skill, has scenario-based expected evidence, and is checked by the catalog validator, fence scanner, and local-path scanner.

## Validation run

| Check | Result |
|---|---|
| Legacy missing local reference paths | PASS — 0 |
| Internal Markdown links | PASS — 1,489 checked, 0 broken |
| Markdown fences | PASS — 1,425 files, 0 unbalanced |
| Catalog validator | PASS — 222 skills, 0 errors |
| JSON/YAML parse | PASS — 1 JSON and 3 YAML resources |
| Bundled JavaScript syntax | PASS — 24 files |
| Bundled shell syntax | PASS — 1 file |
| Existing JavaScript test suite | PASS — 10 tests, 0 failures |
| `git diff --check` | PASS |
