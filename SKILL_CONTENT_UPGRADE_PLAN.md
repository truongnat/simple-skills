# Skill content upgrade plan

## Objective

Improve the usefulness of all 222 skills without flattening domain boundaries or adding generic filler. Each upgrade should add one or more of: decision guidance, worked scenarios, expected evidence, references, reusable templates, or domain-specific quality gates.

## Delivery policy

Work in phases, ordered by user impact and risk. Keep each skill self-contained, use progressive disclosure for long material, preserve existing handoffs, and validate links/fences/contracts after every phase. Do not mass-insert identical boilerplate into every `SKILL.md`.

## Cluster roadmap

| Phase | Cluster | Scope | Content to add | Status |
|---|---|---|---|---|
| 1 | High-risk integrations and runtime operations | fintech, finance, accounting, hybrid networking, Solidity, MLOps, Expo, GitHub Actions | Reference packs, scenario matrices, expected evidence, failure/rollback guidance | **Implemented in this pass** |
| 2 | Security, testing, and reliability | Group 06: auth, API security, SAST, E2E, debugging, performance, testing | Threat cases, invariants, regression fixtures, severity/triage tables, incident evidence | **Core high-risk packs implemented; mature-reference skills retained for catalog pass** |
| 3 | Data, AI, and agent systems | Group 04: RAG, agents, evaluation, data engineering, ML | Evaluation datasets, grounding/safety gates, drift/lineage, tool-failure cases | **Core evaluation and lineage packs implemented; mature-reference skills retained for catalog pass** |
| 4 | Cloud, deployment, and databases | Groups 07–08 | Provider decision tables, rollout/rollback cases, schema/migration checks, backup/restore evidence | **Core operational packs implemented; mature-reference skills retained for catalog pass** |
| 5 | Architecture, API, and frameworks | Groups 02–03 | Compatibility matrices, contract examples, failure modes, version migration notes | **Core compatibility and framework packs implemented; mature-reference skills retained for catalog pass** |
| 6 | Frontend, UI/UX, and accessibility | Group 05 | Interaction states, responsive/accessibility checks, visual and semantic evidence | **Core interaction and accessibility packs implemented; mature-reference skills retained for catalog pass** |
| 7 | Lifecycle and BA/product workflows | Group 01 | Worked artifacts, acceptance criteria, handoff evidence, decision records | **Core lifecycle evidence packs implemented; canonical ownership remains covered by catalog pass** |
| 8 | Documents, research, and business | Group 09 | Golden-output checks, source/evidence registers, reproducibility and citation guidance | **Core output/evidence packs implemented; mature-format references retained for catalog pass** |
| 9 | Git, tooling, platform, and meta-skills | Group 10 | Safe boundaries, review gates, reusable templates, tool capability matrices | **Core safety/capability packs implemented; mature references retained for catalog pass** |
| 10 | Catalog-wide quality pass | All groups | Router precedence, duplicate-boundary notes, reference link audit, coverage linter | **Quality pass implemented; deterministic gates pass and review leads recorded** |

## Phase 1 deliverables

Created reference packs for `sk-hybrid-cloud-networking`, `sk-solidity-security`, `sk-mlops-pro`, `sk-expo-data-fetching`, `sk-expo-native-ui`, and `sk-github-actions-templates`. Existing finance/accounting/fintech references were created in the previous pass. Fixed the unbalanced fence in `sk-biz-model/templates/MODEL.template.md`.

## Phase 2 deliverables

Created and linked focused verification packs for `sk-ai-red-teaming-pro`, `sk-api-security-pro`, `sk-auth-implementation-patterns`, `sk-e2e-testing-patterns`, `sk-security-review`, `sk-debugging-strategies`, `sk-performance-tuning-pro`, and `sk-testing-pro`. The remaining Group 06 skills already have mature references or received focused material in Phase 1; they are covered by the validation pass and are not duplicated.

## Per-skill upgrade contract

For each skill, add only the sections appropriate to its domain:

1. **Decision map:** when to choose this skill versus adjacent skills.
2. **Worked scenario:** a realistic input, approach, and expected output.
3. **Failure modes:** common invalid input, unsafe assumption, or boundary case.
4. **Verification evidence:** what must be checked and what counts as proof.
5. **Reference navigation:** when to load each bundled file.
6. **Handoff:** the next owner and the artifact passed forward.

## Acceptance criteria per phase

- No broken local links or unbalanced Markdown fences.
- Catalog validator passes with zero errors.
- New material is specific to the skill and avoids generic restatement.
- High-risk skills include scenario-based expected evidence, not only a checklist.
- Long content moves to focused references while `SKILL.md` remains navigable.
- Existing uncommitted user files and prior audit artifacts are not overwritten.

## Next execution order

1. Complete Group 06 security/testing/reliability reference packs.
2. Complete Group 04 AI/data evaluation packs.
3. Complete Groups 07–08 operational and persistence validation packs.
4. Upgrade one representative skill per remaining cluster, validate the pattern, then fan out only where the content is genuinely reusable.

## Phase 3 deliverables

Created and linked focused evaluation/lineage packs for `sk-ai-agents-pro`, `sk-fullstack-rag-pro`, `sk-data-engineering-pro`, `sk-data-science-pro`, `sk-machine-learning-pro`, and `sk-agent-evaluation-pro`. Existing mature Group 04 references remain authoritative for AI integration, content analysis, prompt engineering, data analysis, and MLOps.

## Phase 4 deliverables

Created and linked focused operational packs for `sk-deployment-pro`, `sk-database-migration`, `sk-postgresql-table-design`, `sk-redis-pro`, `sk-kubernetes-pro`, and `sk-aws-pro`. Existing CI/CD, Docker, networking, IaC, SQL, and PostgreSQL production references remain authoritative where they already cover the same concerns.

## Phase 5 deliverables

Created and linked focused compatibility/verification packs for `sk-api-design-pro`, `sk-microservices-pro`, `sk-graphql-pro`, `sk-spring-boot-pro`, `sk-django-pro`, and `sk-nextjs-pro`. Existing clean architecture, NestJS, React, TypeScript, and framework reference bundles remain authoritative where they already cover the same concerns.

## Phase 6 deliverables

Created and linked focused interaction/accessibility packs for `sk-frontend-design-pro`, `sk-mobile-design-pro`, `sk-a11y-design-pro`, `sk-design-system-pro`, `sk-react-pro`, and `sk-accessibility-compliance`. Existing React Native, Expo, motion, component, and visual-design references remain authoritative where they already cover the same concerns.

## Phase 7 deliverables

Created and linked focused lifecycle/BA/product packs for `sk-business-analysis`, `sk-specify`, `sk-planning`, `sk-quick-fix`, `sk-execution`, `sk-tester`, and `sk-done`. Existing Group 01 step templates, session-artifact contracts, and canonical `sk-executing-pro`/`sk-verify-pro` ownership remain authoritative where they already cover the same concerns.

## Phase 8 deliverables

Created and linked focused output/evidence packs for `sk-pdf-pro`, `sk-xlsx`, `sk-pptx`, `sk-docx`, `sk-research`, `sk-web-research-pro`, `sk-market-research-pro`, and `sk-docs`. Existing format-specific coverage manifests, research templates, and enterprise documentation standards remain authoritative where they already cover the same concerns.

## Phase 9 deliverables

Created and linked focused safety/capability packs for `sk-git-operations-pro`, `sk-git-worktree-pro`, `sk-repo-tooling-pro`, `sk-router-pro`, `sk-gatekeeper`, `sk-tool-discovery`, `sk-skill-authoring`, and `sk-skills-self-review-pro`. Existing Group 10 command references, routing tables and authoring rules remain authoritative where they already cover the same concerns.

## Phase 10 deliverables

Ran a catalog-wide quality pass over all 222 skills. Deterministic checks found 0 broken local links, 0 unbalanced fences, and 1,003 reference files. The reproducible linter records routing/ownership overlap leads and scenario-plus-evidence coverage leads for domain-owner review without treating heuristics as automatic defects.
