# Full skill coverage audit — test cases & detailed documentation

**Date:** 2026-09-30
**Scope:** all 222 `skills/sk-*/SKILL.md` packages and their bundled resources.
**Status:** audit only; no skill content was modified in this pass.

## Executive summary

- Catalog inventory: **222/222 skills**; no directory was omitted.
- Explicit test-case/invariant signal: **103 skills**. This is a heuristic signal, not a quality verdict; many process/document skills use checklists instead of tests.
- Verification/checklist signal: **212 skills**.
- Skills with bundled `references/`: **126**; with executable/config/resource files: **162**.
- High-priority follow-up: **9 P1 skills**; medium follow-up: **21 P2 skills**; optional maintenance: **0 P3 skills**.
- Core repository validation remains separate: the catalog validator passed in the previous pass; this report evaluates content coverage, not runtime correctness.

## P1 — should be improved before calling the catalog production-ready

| Skill | Evidence | Recommended additions |
|---|---|---|
| `sk-accounting-pro` | The skill references a missing `REFERENCE.md` and lacks explicit accounting test cases. Add double-entry balance, period close, reversal, FX, reconciliation, and audit-trail scenarios with expected outputs. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-expo-data-fetching` | The skill covers loading/error/cache/offline/auth/cancellation and even promises tests in its output, but has no explicit test section. Add a state matrix for HTTP errors, malformed payload, timeout, offline queue, cancellation, token refresh concurrency, cache invalidation, and environment leakage. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-expo-native-ui` | The skill has extensive platform/UI guidance but no explicit verification section. Add iOS/Android/web compatibility, safe-area, dynamic type, accessibility labels/focus, dark mode, reduced motion, keyboard, touch target, and visual regression cases. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-financial-analysis-pro` | The skill references a missing `REFERENCE.md` and lacks explicit model-validation cases. Add a DCF/comps case with assumptions, sensitivity, unit checks, period discipline, and a known-answer output. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-fintech-integration-pro` | The skill explicitly promises payment, banking, webhook, retry and security guidance, but has no `REFERENCE.md` despite referencing it at lines 78, 111 and 372, and no explicit test matrix. Add cases for idempotency, webhook replay/signature failure, duplicate events, timeout/retry, refund/chargeback, rate limits, token leakage, and reconciliation. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-github-actions-templates` | Templates/assets now exist, but there is no validation matrix. Add cases for YAML parse, least-privilege permissions, fork PR secrets, concurrency/cancel-in-progress, matrix failure, artifact retention, pinning, deployment approval, rollback, and reusable workflow inputs. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-hybrid-cloud-networking` | `Monitoring and Troubleshooting` is empty; the related-skills table contains malformed `-  - For IaC implementation`. Add BGP convergence, dual-tunnel failover, asymmetric routing, MTU/fragmentation, packet loss, DNS, and rollback scenarios. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-mlops-pro` | It has a verification response shape but no bundled references or concrete evaluation matrix. Add reproducibility, data/schema drift, model-quality regression, canary rollback, feature freshness, serving SLO, and alert-threshold cases. | Add explicit expected result/evidence, not only prose or a generic checklist. |
| `sk-solidity-security` | It delegates invariant/fuzz/regression strategy to `sk-testing-pro` but provides no concrete attack scenario matrix. Add reentrancy, access control, oracle manipulation, upgrade/storage collision, integer/rounding, signature replay, and pause/emergency invariants. | Add explicit expected result/evidence, not only prose or a generic checklist. |

## P2 — useful documentation/test-case additions in the next pass

| Skill(s) | Why | Suggested addition |
|---|---|---|
| `sk-spring-boot-pro` | No reference bundle or explicit test matrix despite framework-specific production guidance. | Add a minimal REST/service example with unit, integration, security, transaction, profile, and migration checks. |
| `sk-biz-model`, `sk-engineering-management-pro` | Business/process guidance is mostly conceptual and lacks observable examples. | Add 2–4 worked scenarios with assumptions, decision criteria, expected artifact, and failure/uncertainty handling. |
| `sk-fullstack-rag-pro`, `sk-ai-agents-pro`, `sk-ai-red-teaming-pro` | AI/agent output quality is high variance; generic checklists are not enough. | Add evaluation datasets, groundedness/safety cases, tool failure, prompt injection, latency/cost, and regression gates. |
| `sk-django-pro`, `sk-data-science-pro`, `sk-data-engineering-pro`, `sk-machine-learning-pro` | Framework/data guidance has examples but limited explicit expected results. | Add representative fixtures, schema/data assumptions, and verification outputs for the primary workflow. |
| `sk-office-common`, `sk-pdf`, `sk-pptx`, `sk-xlsx`, `sk-docx` | Artifact skills need output-level validation more than prose tests. | Add golden-output checks for layout, metadata, formulas, pagination, accessibility, and round-trip conversion. |
| `sk-clean-architecture`, `sk-debugging-strategies`, `sk-javascript-testing-patterns`, `sk-microservices-patterns`, `sk-stride-analysis-patterns` | These skills are concise and structurally sound but thin on observable worked cases. | Add at least one positive and one negative scenario with expected routing/decision/evidence. |

## P3 — maintenance opportunities

- **60 skills** have neither an example heading nor a reference bundle nor a code fence. Most are lifecycle/process skills, so this is not automatically a defect; add examples only where the skill makes a repeatable decision or produces a structured artifact.
- **19 skills** exceed 300 lines and **22 skills** exceed 180 lines without a `references/` directory. Consider progressive disclosure, but do not split merely to satisfy a number.
- The test-heading heuristic found only 15 explicit test headings; this is expected for many design, research, and documentation skills. Prefer “worked scenario + expected evidence” for those domains.
- External handoffs such as `sk-clean-code`, `sk-slides`, and `sk-gitnexus-exploring` are not counted as local documentation gaps.

## What is already working

- All 222 skills were inventoried; no skill directory was silently skipped.
- Most skills have boundary, inputs, handoff, checklist, output, or verification language after the previous contract remediation.
- Security, API, database, caching, debugging, and many document skills already have substantial reference bundles; the main gap is often explicit scenario coverage, not total absence of content.
- Existing bundled scripts and assets were inventoried but not executed in this audit because they may require external runtimes or user projects.

## Recommended order

1. Add missing `REFERENCE.md` files and high-risk scenario matrices for fintech, finance, and accounting.
2. Fill hybrid networking troubleshooting and repair its malformed handoff.
3. Add security/ML/mobile/CI validation matrices for Solidity, MLOps, Expo, and GitHub Actions.
4. Add worked examples and expected evidence to the P2 group.
5. Re-run catalog validation and add a lightweight coverage linter that checks for at least one scenario/verification block per high-risk domain skill.

## Method and limitations

The scan uses headings, keywords, code fences, reference paths, bundled resources, and targeted manual review. “No test signal” means no explicit terms such as test case, invariant, fuzz, assertion, expected result, or verification evidence were found; it does **not** prove that the skill has no useful checklist. Runtime correctness, current third-party API accuracy, and generated artifact quality require separate fixture-based or live validation.

## Appendix — all 222 skills

| Skill | Lines | Refs | Resources | Test signal | Verify signal | Examples | Code fences | Priority | Action |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `sk-3d-motion-pro` | 195 | 5 | 8 | 1 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-a11y-design-pro` | 192 | 5 | 8 | 1 | 7 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-a2a-protocol-pro` | 203 | 6 | 6 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-accessibility-compliance` | 82 | 4 | 4 | 1 | 1 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-accounting-pro` | 347 | 0 | 0 | 0 | 3 | 2 | 11 | P1 | Add missing REFERENCE.md plus domain-specific scenario/case matrix and evidence-based validation.; REFERENCE.md |
| `sk-ag-ui-pro` | 201 | 6 | 6 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-agent-evaluation-pro` | 218 | 7 | 7 | 0 | 7 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ai-agents-pro` | 119 | 0 | 0 | 0 | 1 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-ai-design-pro` | 195 | 5 | 8 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ai-integration-pro` | 304 | 20 | 20 | 0 | 20 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ai-red-teaming-pro` | 109 | 0 | 0 | 0 | 1 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-algorithm-pro` | 245 | 16 | 16 | 0 | 12 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-android-pro` | 116 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-angular-pro` | 122 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-api-ba` | 103 | 0 | 5 | 0 | 7 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-api-design-principles` | 132 | 3 | 5 | 0 | 2 | 1 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-api-design-pro` | 268 | 17 | 17 | 0 | 16 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-api-security-pro` | 119 | 0 | 0 | 0 | 4 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-architecture-decision-records` | 445 | 0 | 4 | 0 | 2 | 0 | 10 | OK | Adequate baseline; maintain examples and verification. |
| `sk-architecture-patterns` | 183 | 2 | 2 | 6 | 0 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-auth-implementation-patterns` | 110 | 1 | 1 | 0 | 1 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-auth-pro` | 336 | 26 | 26 | 0 | 18 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-aws-pro` | 119 | 0 | 0 | 3 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-azure-storage` | 199 | 13 | 13 | 2 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ba-dashboard` | 88 | 0 | 5 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ba-handoff` | 96 | 0 | 9 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ba-integrate` | 94 | 0 | 6 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ba-kg` | 89 | 0 | 5 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ba-test` | 94 | 0 | 6 | 0 | 9 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-basic-design` | 233 | 0 | 5 | 0 | 2 | 0 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-biz-model` | 121 | 0 | 5 | 0 | 1 | 0 | 0 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-blockchain-pro` | 118 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-brainstorming` | 188 | 0 | 2 | 0 | 6 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-bug-discovery-pro` | 289 | 20 | 20 | 1 | 12 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-bun-cli-pro` | 259 | 7 | 7 | 1 | 7 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-business-analysis` | 196 | 0 | 5 | 0 | 11 | 0 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-caching-pro` | 296 | 21 | 21 | 0 | 13 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ci-cd-pro` | 256 | 17 | 17 | 2 | 12 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-claude-code-pro` | 111 | 0 | 0 | 1 | 1 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-clean-architecture` | 43 | 3 | 3 | 0 | 0 | 0 | 0 | P2 | Add representative cases and expected decision/output examples; current workflow is useful but thin on observable evidence. |
| `sk-clean-code-architecture-pro` | 219 | 11 | 11 | 0 | 13 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-cli-pro` | 225 | 12 | 12 | 1 | 13 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-cloud-native-agent-pro` | 205 | 6 | 6 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-cloudflare-pro` | 120 | 0 | 0 | 3 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-code-packaging-pro` | 236 | 14 | 14 | 0 | 14 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-code-review-pro` | 137 | 2 | 3 | 3 | 6 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-content-analysis-pro` | 237 | 14 | 14 | 0 | 17 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-cpp-pro` | 124 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-data-analysis-pro` | 204 | 13 | 13 | 0 | 19 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-data-engineering-pro` | 129 | 0 | 0 | 0 | 3 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-data-science-pro` | 135 | 0 | 0 | 0 | 3 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-database-migration` | 359 | 1 | 1 | 1 | 1 | 0 | 9 | OK | Adequate baseline; maintain examples and verification. |
| `sk-debugging-investigation` | 138 | 1 | 1 | 0 | 2 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-debugging-strategies` | 49 | 1 | 1 | 0 | 3 | 0 | 0 | P2 | Add representative cases and expected decision/output examples; current workflow is useful but thin on observable evidence. |
| `sk-deploy-workflow` | 146 | 5 | 5 | 2 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-deployment-pipeline-design` | 128 | 2 | 2 | 1 | 0 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-deployment-pro` | 200 | 12 | 12 | 2 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-design-system-patterns` | 146 | 4 | 4 | 1 | 3 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-design-system-pro` | 217 | 18 | 18 | 1 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-design-taste-frontend` | 51 | 1 | 2 | 2 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-detail-design` | 238 | 0 | 5 | 0 | 4 | 0 | 4 | OK | Adequate baseline; maintain examples and verification. |
| `sk-devrel-pro` | 112 | 0 | 0 | 0 | 1 | 1 | 1 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-discussing-pro` | 211 | 4 | 4 | 0 | 8 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-distributed-tracing` | 105 | 1 | 1 | 0 | 1 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-django-pro` | 116 | 0 | 0 | 0 | 1 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-docker-compose-pro` | 189 | 7 | 7 | 2 | 5 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-docker-pro` | 207 | 13 | 13 | 2 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-docs` | 260 | 0 | 18 | 0 | 2 | 0 | 1 | OK | Adequate baseline; maintain examples and verification.; reference.md |
| `sk-docx` | 85 | 1 | 7 | 0 | 7 | 0 | 0 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-done` | 178 | 0 | 2 | 1 | 9 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-e2e-testing-patterns` | 151 | 1 | 1 | 13 | 2 | 1 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-elasticsearch-pro` | 119 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-electron-pro` | 193 | 11 | 11 | 1 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-engineering-management-pro` | 112 | 0 | 0 | 0 | 1 | 1 | 1 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-excel-doc-convert` | 131 | 2 | 8 | 0 | 5 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-executing-pro` | 182 | 12 | 12 | 0 | 14 | 0 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-execution` | 239 | 0 | 4 | 1 | 16 | 0 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-expo-data-fetching` | 470 | 2 | 2 | 0 | 0 | 1 | 19 | P1 | Add explicit test/evaluation matrix covering the skill’s highest-risk paths; link fixtures or executable validation where appropriate. |
| `sk-expo-native-ui` | 201 | 8 | 8 | 0 | 0 | 0 | 4 | P1 | Add explicit test/evaluation matrix covering the skill’s highest-risk paths; link fixtures or executable validation where appropriate. |
| `sk-fastapi-pro` | 121 | 0 | 0 | 0 | 7 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-feedback-pro` | 194 | 13 | 13 | 0 | 15 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-figma-mcp-pro` | 329 | 5 | 5 | 0 | 13 | 4 | 9 | OK | Adequate baseline; maintain examples and verification. |
| `sk-financial-analysis-pro` | 316 | 0 | 0 | 0 | 1 | 1 | 13 | P1 | Add missing REFERENCE.md plus domain-specific scenario/case matrix and evidence-based validation.; REFERENCE.md |
| `sk-fintech-integration-pro` | 392 | 0 | 0 | 0 | 1 | 1 | 15 | P1 | Add missing REFERENCE.md plus domain-specific scenario/case matrix and evidence-based validation.; REFERENCE.md |
| `sk-flutter-pro` | 198 | 12 | 12 | 1 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-frontend-design` | 86 | 0 | 1 | 2 | 1 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-frontend-design-pro` | 293 | 8 | 8 | 1 | 7 | 4 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-frontend-patterns` | 52 | 1 | 1 | 2 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-fullstack-pro` | 129 | 0 | 0 | 0 | 4 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-fullstack-rag-pro` | 123 | 0 | 0 | 0 | 1 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-game-dev-pro` | 120 | 0 | 0 | 1 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-gap-analysis` | 100 | 0 | 6 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-gatekeeper` | 112 | 1 | 2 | 1 | 5 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-gemini-api-dev` | 281 | 0 | 0 | 0 | 2 | 1 | 8 | OK | Adequate baseline; maintain examples and verification. |
| `sk-git-operations-pro` | 197 | 12 | 12 | 0 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-git-worktree-pro` | 137 | 0 | 0 | 1 | 2 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-github-actions-templates` | 353 | 0 | 3 | 0 | 2 | 0 | 8 | P1 | Add explicit test/evaluation matrix covering the skill’s highest-risk paths; link fixtures or executable validation where appropriate. |
| `sk-go-pro` | 133 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-graphql-pro` | 189 | 10 | 10 | 0 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-grill-me-pro` | 157 | 0 | 0 | 0 | 3 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-high-end-visual-design` | 129 | 0 | 0 | 2 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-hybrid-cloud-networking` | 268 | 1 | 1 | 0 | 0 | 0 | 7 | P1 | Fill troubleshooting/monitoring content, add failover/BGP/packet-loss scenarios, and repair malformed IaC handoff. |
| `sk-image-processing-pro` | 191 | 11 | 11 | 0 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-industrial-brutalist-ui` | 123 | 0 | 0 | 2 | 1 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-infrastructure-as-code-pro` | 168 | 4 | 4 | 3 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-init` | 38 | 0 | 1 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-investigate` | 175 | 0 | 1 | 0 | 9 | 0 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ios-pro` | 122 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-java-pro` | 116 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-javascript-pro` | 187 | 10 | 10 | 1 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-javascript-testing-patterns` | 44 | 2 | 2 | 0 | 2 | 0 | 0 | P2 | Add representative cases and expected decision/output examples; current workflow is useful but thin on observable evidence. |
| `sk-karpathy-coding-pro` | 170 | 1 | 1 | 0 | 14 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-kb-workflow` | 157 | 4 | 4 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-kubernetes-pro` | 130 | 0 | 0 | 3 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-machine-learning-pro` | 129 | 0 | 0 | 0 | 4 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-mapping-codebase` | 127 | 0 | 0 | 1 | 1 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-market-research-pro` | 197 | 14 | 14 | 0 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-mcp-server-pro` | 215 | 7 | 7 | 1 | 15 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-microservices-patterns` | 111 | 1 | 1 | 0 | 0 | 1 | 0 | P2 | Add representative cases and expected decision/output examples; current workflow is useful but thin on observable evidence. |
| `sk-microservices-pro` | 194 | 10 | 10 | 0 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-minimalist-ui` | 116 | 0 | 0 | 1 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-mlops-pro` | 121 | 0 | 0 | 0 | 1 | 1 | 2 | P1 | Add explicit test/evaluation matrix covering the skill’s highest-risk paths; link fixtures or executable validation where appropriate. |
| `sk-mobile-design-pro` | 197 | 12 | 12 | 1 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-mongodb-pro` | 116 | 0 | 0 | 1 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-motion-design-pro` | 301 | 8 | 8 | 1 | 5 | 4 | 5 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nestjs-neo4j-pro` | 185 | 7 | 7 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nestjs-pro` | 202 | 12 | 12 | 0 | 19 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-network-infra-pro` | 209 | 13 | 13 | 2 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nextjs-15-pro` | 112 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nextjs-pro` | 175 | 12 | 12 | 1 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nextjs-security-scan` | 254 | 5 | 9 | 0 | 5 | 1 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-nodejs-backend-patterns` | 67 | 2 | 2 | 1 | 0 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ocr-pro` | 191 | 11 | 11 | 0 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-office-common` | 45 | 0 | 6 | 0 | 4 | 0 | 0 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-parallel-agents-pro` | 196 | 12 | 12 | 0 | 7 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-pdf` | 86 | 1 | 7 | 0 | 6 | 0 | 0 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-pdf-pro` | 387 | 0 | 12 | 0 | 2 | 1 | 16 | OK | Adequate baseline; maintain examples and verification. |
| `sk-performance-tuning-pro` | 193 | 10 | 10 | 0 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-planning` | 155 | 0 | 2 | 0 | 6 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-platform-design-pro` | 279 | 10 | 10 | 1 | 6 | 4 | 6 | OK | Adequate baseline; maintain examples and verification. |
| `sk-postgres-patterns` | 251 | 0 | 0 | 1 | 1 | 1 | 11 | OK | Adequate baseline; maintain examples and verification. |
| `sk-postgresql-pro` | 202 | 12 | 12 | 1 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-postgresql-table-design` | 229 | 0 | 0 | 1 | 2 | 1 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-pptx` | 85 | 1 | 7 | 0 | 6 | 0 | 0 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-prisma-postgres` | 201 | 4 | 4 | 1 | 1 | 1 | 4 | OK | Adequate baseline; maintain examples and verification. |
| `sk-product-management-pro` | 118 | 0 | 0 | 0 | 4 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-prompt-engineering-pro` | 208 | 7 | 7 | 0 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-python-pro` | 120 | 0 | 0 | 1 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-quick-fix` | 114 | 0 | 1 | 0 | 7 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-react-native-pro` | 196 | 11 | 11 | 1 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-react-pro` | 166 | 12 | 12 | 1 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-redesign-existing-projects` | 209 | 0 | 0 | 2 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-redis-pro` | 115 | 0 | 0 | 1 | 2 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-remember-pro` | 130 | 0 | 0 | 1 | 3 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-repo-tooling-pro` | 186 | 12 | 12 | 0 | 16 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-report-writer` | 137 | 3 | 4 | 1 | 2 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-research` | 152 | 0 | 5 | 0 | 2 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-reverse-doc` | 100 | 0 | 5 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-review` | 155 | 0 | 4 | 1 | 6 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-review-pr` | 153 | 0 | 4 | 0 | 5 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-router-pro` | 232 | 4 | 4 | 0 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-rust-pro` | 119 | 0 | 0 | 1 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-sast-configuration` | 192 | 1 | 1 | 0 | 3 | 2 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-scaffold` | 139 | 0 | 5 | 0 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-security-pro` | 217 | 14 | 14 | 2 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-security-review` | 407 | 0 | 0 | 0 | 15 | 2 | 7 | OK | Adequate baseline; maintain examples and verification. |
| `sk-self-improve-agent-pro` | 130 | 14 | 14 | 0 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-senior-architect` | 116 | 3 | 3 | 0 | 1 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-senior-backend` | 116 | 3 | 3 | 0 | 4 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-senior-frontend` | 52 | 4 | 7 | 2 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-senior-security` | 48 | 4 | 6 | 0 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-seo-pro` | 127 | 12 | 12 | 1 | 5 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-shadcn-mastery-pro` | 311 | 7 | 7 | 1 | 5 | 3 | 8 | OK | Adequate baseline; maintain examples and verification. |
| `sk-skill-authoring` | 172 | 5 | 7 | 0 | 13 | 1 | 1 | OK | Adequate baseline; maintain examples and verification.; references/file.md |
| `sk-skill-creator-pro` | 188 | 0 | 0 | 2 | 7 | 1 | 2 | OK | Adequate baseline; maintain examples and verification.; references/decision-framework-and-trade-offs.md; references/failure-modes-detection-mitigation.md; references/quality-validation-and-guardrails.md; references/system-model.md |
| `sk-skills-self-review-pro` | 175 | 13 | 13 | 0 | 14 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-solidity-security` | 48 | 1 | 1 | 2 | 3 | 0 | 0 | P1 | Add explicit test/evaluation matrix covering the skill’s highest-risk paths; link fixtures or executable validation where appropriate. |
| `sk-specify` | 130 | 0 | 11 | 0 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-spring-boot-pro` | 124 | 0 | 0 | 0 | 1 | 1 | 2 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
| `sk-sql-data-access-pro` | 198 | 12 | 12 | 1 | 9 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-sql-optimization-patterns` | 241 | 1 | 1 | 1 | 0 | 1 | 7 | OK | Adequate baseline; maintain examples and verification. |
| `sk-story-spec` | 97 | 0 | 7 | 0 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-strategic-consulting-pro` | 201 | 14 | 14 | 0 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-stream-rtc-pro` | 125 | 10 | 10 | 0 | 5 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-stride-analysis-patterns` | 93 | 1 | 1 | 0 | 0 | 1 | 1 | P2 | Add representative cases and expected decision/output examples; current workflow is useful but thin on observable evidence. |
| `sk-sustainable-design-pro` | 194 | 5 | 8 | 1 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-sync` | 275 | 0 | 4 | 0 | 6 | 0 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-sync-custom-to-repo` | 101 | 1 | 1 | 1 | 5 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-system-design` | 213 | 0 | 26 | 1 | 2 | 1 | 5 | OK | Adequate baseline; maintain examples and verification. |
| `sk-system-design-pro` | 123 | 26 | 26 | 1 | 1 | 0 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-systematic-debugging-pro` | 168 | 3 | 3 | 1 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-tauri-pro` | 131 | 11 | 11 | 3 | 6 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-technical-writing-pro` | 113 | 0 | 0 | 0 | 2 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-test-driven-development-pro` | 132 | 3 | 3 | 0 | 3 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-tester` | 363 | 0 | 5 | 15 | 31 | 0 | 5 | OK | Adequate baseline; maintain examples and verification. |
| `sk-testing-pro` | 203 | 12 | 12 | 11 | 10 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-to-issues-pro` | 182 | 0 | 0 | 0 | 6 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-to-prd-pro` | 175 | 0 | 0 | 1 | 4 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-tool-discovery` | 109 | 1 | 2 | 1 | 1 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ttd-pro` | 131 | 0 | 0 | 1 | 5 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-typescript-pro` | 171 | 12 | 12 | 1 | 11 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ui-design-brain-pro` | 230 | 6 | 6 | 1 | 10 | 4 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ui-reverse-engineer-pro` | 154 | 9 | 9 | 1 | 4 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ui-stack-pro` | 350 | 9 | 9 | 1 | 7 | 4 | 11 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ui-ux-system-pro` | 347 | 5 | 5 | 1 | 7 | 5 | 5 | OK | Adequate baseline; maintain examples and verification. |
| `sk-user-flow` | 90 | 0 | 5 | 0 | 2 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-using-aix` | 99 | 0 | 0 | 1 | 4 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-using-harness` | 129 | 0 | 0 | 1 | 3 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ux-design-pro` | 108 | 0 | 0 | 0 | 2 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-ux-wireframe` | 96 | 0 | 6 | 1 | 3 | 0 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-vercel-deployment-pro` | 124 | 0 | 0 | 3 | 1 | 1 | 3 | OK | Adequate baseline; maintain examples and verification. |
| `sk-verification` | 132 | 1 | 2 | 0 | 6 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-verify-pro` | 127 | 1 | 1 | 0 | 8 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-vibe-coding-pro` | 108 | 0 | 0 | 1 | 4 | 1 | 1 | OK | Adequate baseline; maintain examples and verification. |
| `sk-visual-design-foundations` | 349 | 3 | 3 | 2 | 2 | 0 | 12 | OK | Adequate baseline; maintain examples and verification. |
| `sk-vps-devops-pro` | 202 | 8 | 8 | 2 | 8 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-vue-pro` | 119 | 0 | 0 | 2 | 1 | 1 | 2 | OK | Adequate baseline; maintain examples and verification. |
| `sk-web-component-design` | 302 | 3 | 3 | 1 | 1 | 0 | 8 | OK | Adequate baseline; maintain examples and verification. |
| `sk-web-research-pro` | 195 | 12 | 12 | 0 | 12 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-websocket-pro` | 128 | 10 | 10 | 0 | 5 | 1 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-writing-skills` | 150 | 0 | 0 | 0 | 4 | 3 | 0 | OK | Adequate baseline; maintain examples and verification. |
| `sk-xlsx` | 108 | 1 | 7 | 0 | 6 | 1 | 1 | P2 | Add 2–4 worked scenarios, expected outputs, and a compact verification checklist; add references if the topic has substantial variants. |
