---
name: research
description: Research internal or external sources before making technical/product decisions. Source-backed findings, comparison matrix, recommendations with citations and caveats.
---

# Research

## Purpose

Collect, verify, and synthesize evidence to support technical, product, or operational decisions.

This skill focuses on:

- Identify the research question and the decision it supports.
- Define a source strategy.
- Distinguish local evidence, external evidence, facts, inference, and opinion.
- Prefer primary/official sources for technical/API/framework research.
- Check freshness for information that may change.
- Compare options with an evidence matrix.
- Provide a recommendation with confidence, caveats, and residual risks.
- Create `RESEARCH.md` for handoff to brainstorming, planning, technical design, or execution.

The goal: avoid decisions based on vague memory, weak sources, or stale information.

## When to Use

Use this skill when:

- User requests research before implementing.
- Need to find new or possibly changed information.
- Need to check official docs for API/framework/library/tool.
- Need to compare technical options.
- Need to compare products, tools, or platforms.
- Need to check compatibility, pricing, limits, licensing, support status, or new docs.
- Need product, market, or competitor research.
- Need source-backed recommendations.
- Need to create or update `RESEARCH.md`.
- Need to synthesize local docs/code with external sources.
- Need to assess caveats, residual risks, or uncertainty.
- Need to decide which direction to take based on evidence.

## When NOT to Use

Do NOT use this skill when:

- The answer is already clear in the repo and does not need freshness.
- Task only needs execution per plan.
- Task only needs a PR or diff review; use `review-pr`.
- Task is specific debugging based on logs/codebase; use `investigate`.
- User only needs a brainstorming session without sources.
- User only needs planning from clear requirements.
- User requests immediate implementation with clear sources and decisions.
- User explicitly says not to use external sources.
- Research requires professional legal/financial/medical advice.

## XML Contract

```xml
<Contract>
  <Inputs>Research question, decision context, local evidence, external source constraints, freshness requirement, quality bar, session path if available.</Inputs>
  <Outputs>RESEARCH.md or research report with source strategy, local evidence, external evidence, key findings, comparison, recommendation, confidence, caveats, residual risks, handoff.</Outputs>
  <Artifacts>RESEARCH.md in session path if applicable; otherwise, research report in response.</Artifacts>
  <Safety>Do NOT fabricate citations. Do NOT copy long source content. Do NOT use stale sources for decisions needing fresh information. Do NOT present inference as fact. Do NOT omit caveats or residual risks. Do NOT replace licensed professionals for legal/financial/medical matters.</Safety>
</Contract>
```

## Source Strategy

Prioritize sources in this order:
1. Official documentation / primary source.
2. Standards/specs/RFC if relevant.
3. Vendor docs or official release notes.
4. Source repository, changelog, official issue tracker.
5. Academic paper or credible technical publication.
6. Reputable engineering blog.
7. Reputable comparison/review source.
8. Community discussion (for context only, not single-source decisions).

For technical questions: prefer official docs. If a source is not official, note it as supporting only. Do NOT rely on old blogs if newer docs contradict them.

## Source Quality Levels

| Level | Source Type | Trust |
|---|---|---|
| Primary | Official docs, specs, release notes, source repo | Highest |
| Secondary | Reputable engineering articles, vendor-neutral guides | Medium |
| Community | GitHub issues, Stack Overflow, Reddit, forums | Context only |
| Marketing | Landing pages, sales pages | Use carefully |
| Unknown | Unclear author/date/source | Avoid or mark low confidence |

## Freshness Policy

Must check freshness when information can change: API/framework/library versions, pricing/limits/quota, product availability, cloud service behavior, legal/regulatory/compliance, security vulnerabilities, model/tool capabilities, SaaS features, app store policies, browser/platform support, performance benchmarks, current best practices, active project maintenance.

If freshness is unclear: document a caveat, lower confidence, and recommend verification before implementation.

## Workflow

1. Determine if research is needed.
2. Choose Lite Mode or Full Mode.
3. Identify the research question.
4. Identify the decision to support.
5. Identify constraints and freshness requirements.
6. Define a source strategy.
7. Read local evidence first if the research relates to the current repo/project.
8. Collect external evidence from appropriate sources.
9. Prefer primary/official sources.
10. Check freshness for information that may change.
11. Record sources reviewed.
12. Synthesize key findings — do NOT copy long content.
13. Separate facts, inference, and opinion/recommendation.
14. If multiple options, create a comparison matrix.
15. Provide recommendation with confidence.
16. Document caveats and residual risks.
17. Document open questions.
18. Handoff to planning/technical design/execution or continue research.
19. Save `RESEARCH.md` if Full Mode/session applicable.

## Limitations

- Research does NOT implement.
- Research does NOT replace planning.
- Research does NOT replace investigate when root cause is needed.
- Research does NOT replace review.
- Research does NOT guarantee external sources are always correct or unchanged.
- Research does NOT replace professional legal/financial/medical advice.
- If sources are missing, stale, or conflicting, document the limitation instead of over-confidently concluding.

<Contract>
  <Inputs>Research question, decision context, local evidence, external source constraints, freshness requirement, quality bar.</Inputs>
  <Outputs>RESEARCH.md with source strategy, evidence, findings, comparison matrix, recommendation, confidence, caveats, residual risks.</Outputs>
  <Artifacts>RESEARCH.md in session path.</Artifacts>
  <Safety>Do NOT fabricate citations. Do NOT copy long source content. Do NOT use stale sources for fresh decisions. Do NOT present inference as fact. Do NOT omit caveats.</Safety>
</Contract>
