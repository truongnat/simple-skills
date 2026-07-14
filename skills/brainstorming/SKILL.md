---
name: brainstorming
description: Clarify goals, scope, constraints, options, trade-offs, risks, and recommendations before planning or implementation.
---

# Brainstorming

## Purpose

Turn an initial request into a clear direction before planning or implementing.

This skill focuses on:

- Clarify goals and expected outcomes.
- Separate facts, assumptions, and unknowns.
- Identify constraints, scope, out-of-scope, and non-goals.
- Analyze feasible solution directions.
- Compare trade-offs between options.
- Identify risks, uncertainties, and verification methods.
- Make a reasoned recommendation.
- Prepare handoff to planning, technical design, business analysis, or implementation.

The goal: help the team settle on the smallest, clearest, verifiable direction before investing larger effort.

## When to Use

Use this skill when:

- Starting a new task with unclear goals, scope, constraints, or solutions.
- User wants to discuss ideas before implementing.
- Multiple approaches exist and need trade-off analysis.
- Scope needs to be locked before planning.
- Need to define in-scope, out-of-scope, or non-goals.
- Need draft success criteria before moving to planning or business analysis.
- Need to create or update DISCUSSION.md.
- Need alignment on product, UX, technical direction, or workflow.
- Need to decide between MVP, prototype, proof of concept, or phased delivery.
- Need to clarify risks, assumptions, or unknowns before detailed work.

## When NOT to Use

Do NOT use this skill when:

- Task is small, scope is clear, and can be fixed directly without discussion.
- Task already has a complete DISCUSSION.md and the user requests execution.
- Task has clear requirements/specs and only needs detailed planning.
- User requests code review, debug, or a specific bug investigation.
- User requests a small fix: typo, copy, style, import, simple config.
- User requests immediate implementation with low ambiguity.
- User needs detailed business requirement analysis; use business-analysis.
- User needs detailed technical architecture; use technical-design if available.
- User needs deep external source research; use research.

## XML Contract

See [openai.yaml](./agents/openai.yaml)

## Quality Standards

- [ ] Goal is one clear sentence, not a paragraph.
- [ ] Facts, assumptions, and unknowns are separated.
- [ ] Scope, out-of-scope, and non-goals are separated.
- [ ] At least one option is analyzed; if multiple, comparison matrix is used.
- [ ] Recommendation has a reason, trade-off summary, and confidence level.
- [ ] Risks have both impact and mitigation.
- [ ] Handoff to next skill is specified.

## WRONG vs CORRECT

```markdown
// WRONG — vague, no recommendation
We could use option A or B. Both have pros and cons.

// CORRECT — clear recommendation with trade-off
Recommend: Option B — minimal prototype first.
Reason: Lowest risk, fastest to validate UX assumption.
Not A: Requires full architecture before validating user flow.
Confidence: Medium.
```

```markdown
// WRONG — assumptions mixed with facts
The user needs authentication.

// CORRECT — separated
Fact: The current system uses Keycloak 26.
Assumption: We can reuse existing Keycloak config (risk: may need custom scopes).
```

## Edge Cases

| Situation | Handling |
|---|---|
| User says "just decide for me" | Make best-effort recommendation but mark confidence and open questions. |
| No options exist yet | Recommend investigate first, or research external solutions. |
| Task is too small for full DISCUSSION.md | Use Lite Mode — 5 bullets max. |
| User contradicts earlier statement | Document both positions as open question, flag to stakeholder. |

## Limitations

- This skill does NOT implement code.
- This skill does NOT replace detailed planning.
- This skill does NOT replace business analysis.
- This skill does NOT replace technical design.
- This skill does NOT auto-confirm assumptions.

## References

- [Decision Matrix](https://asana.com/resources/decision-matrix)
- [How Might We Questions](https://www.designkit.org/methods/how-might-we)
