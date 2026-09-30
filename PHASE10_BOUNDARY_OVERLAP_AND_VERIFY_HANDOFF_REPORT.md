# Phase 10 — Detailed boundary overlap and `sk-verify-pro` handoff report

## Executive summary

The current catalog-wide heuristic produces **0 boundary overlap leads** at Jaccard ≥ 0.72.

| Classification | Count | Interpretation | Recommended treatment |
|---|---:|---|---|
| Lifecycle/BA generic-boundary cluster | 0 | Shared lifecycle vocabulary still creates pairwise similarity; not proof of duplicate skills | No remaining lifecycle/BA generic-boundary leads; keep the artifact-owner contracts and routing guardrail |
| Expo/JavaScript adjacency | 0 | UI, data-fetching and testing concerns share state/testing vocabulary | No remaining Expo/JavaScript adjacency leads at this threshold |
| Direct `sk-verify-pro` overlap | 0 | The P0 verification boundary rewrite removed direct heuristic collisions | Keep the handoff matrix below as the routing contract |

The score is a **review signal**, not a duplicate verdict. The linter compares tokens inside `Boundary`; it does not inspect triggers, artifacts, workflow steps, or user intent.

## 1. Complete list of 0 leads

### 1.1 Lifecycle/BA generic-boundary cluster — 0 pairs

All pairs in this table are combinations among the following 13 skills:

`sk-ba-dashboard`, `sk-ba-handoff`, `sk-ba-integrate`, `sk-ba-kg`, `sk-ba-test`, `sk-basic-design`, `sk-brainstorming`, `sk-detail-design`, `sk-discussing-pro`, `sk-gap-analysis`, `sk-init`, `sk-investigate`, `sk-quick-fix`.

| Similarity | Pair | Current interpretation | Next action |
|---:|---|---|---|

### 1.2 Expo/JavaScript adjacency — 0 pairs

| Similarity | Pair | Likely distinction | Next action |
|---:|---|---|---|

## 2. Recommended treatment of the 13-skill cluster

The 0 lifecycle/BA pairs are review signals, not duplicate verdicts. Do not merge these skills. Keep one-sentence primary artifacts, non-ownership clauses, and next-owner handoffs:

| Skill | Recommended canonical artifact/decision | Must not own | Canonical next handoff |
|---|---|---|---|
| `sk-ba-dashboard` | BA dashboard/reporting requirements, metrics, dimensions and decision questions | Data-pipeline implementation or visual frontend implementation | `sk-business-analysis` / analytics or frontend owner |
| `sk-ba-handoff` | BA-to-implementation handoff with assumptions, decisions, open questions and acceptance context | Implementation or final verification | `sk-planning` / `sk-executing-pro` |
| `sk-ba-integrate` | Integration requirement map: actors, systems, exchange, ownership and failure expectations | API technical design or integration coding | `sk-api-ba` / `sk-api-design-pro` |
| `sk-ba-kg` | Knowledge-graph requirements, entities, relations, provenance and query outcomes | Graph database implementation or generic BA | graph/data implementation owner |
| `sk-ba-test` | BA-level acceptance scenarios and business-readable expected outcomes | Test framework execution or release gate | `sk-tester` → `sk-verify-pro` |
| `sk-basic-design` | Early design direction, goals, constraints, references and visual hypotheses | Detailed UI layout or frontend code | `sk-detail-design` / `sk-ux-wireframe` |
| `sk-brainstorming` | Option set, divergent ideas, assumptions and selection criteria | Final requirements or implementation plan | `sk-business-analysis` / `sk-specify` |
| `sk-detail-design` | Detailed design specification with states, components and implementation constraints | Product discovery or code implementation | `sk-ux-wireframe` / relevant frontend skill |
| `sk-discussing-pro` | Clarified problem statement, goals, constraints and unresolved decisions | Planning or implementation before scope is stable | `sk-business-analysis` / `sk-planning` |
| `sk-gap-analysis` | Current-versus-target capability/evidence gap register and remediation priorities | Fix execution or final acceptance | `sk-planning` / domain owner |
| `sk-init` | Initial task/workspace context, scope, inputs, constraints and artifact location | Feature design or implementation | `sk-discussing-pro`, `sk-planning` or direct specialist |
| `sk-investigate` | Evidence-backed investigation record: observations, hypotheses, reproduction and findings | Permanent fix implementation or release approval | domain owner / `sk-quick-fix` / `sk-verify-pro` |
| `sk-quick-fix` | Small, bounded remediation with changed files, checks and rollback note | Broad refactor, discovery or unverified release decision | `sk-tester` → `sk-verify-pro` |

## 3. `sk-verify-pro` canonical handoff model

### 3.1 Ownership rule

`sk-verify-pro` is the final **claim-to-evidence decision owner**. It does not produce every type of evidence and does not replace domain expertise. Upstream skills produce requirements, implementation, tests, review findings or state; `sk-verify-pro` evaluates whether those inputs prove the stated claim.

```text
requirements / plan / domain constraints
        ↓
implementation + tests + review evidence
        ↓
sk-verify-pro: trace claim → criteria → evidence → status
        ↓
pass → sk-done / release owner
block → implementation owner / sk-planning
defer → named human or domain owner with explicit gap
```

### 3.2 Handoff matrix

| Neighbor | Role relative to `sk-verify-pro` | Required input to verification | Verification output/decision |
|---|---|---|---|
| `sk-verification` | Compatibility facade | Delegates directly to `sk-verify-pro`; preserve target, criteria and evidence location. | `VERIFY.md` produced by the canonical owner. |
| `sk-tester` | Evidence producer | Runs tests and supplies test matrix, expected results, logs, fixtures and limitations. | Verification record maps each acceptance criterion to test evidence. |
| `sk-review` | Quality findings producer | Returns severity-ranked findings and resolved review evidence; does not decide final pass alone. | `sk-verify-pro` classifies unresolved findings as pass/block/defer. |
| `sk-review-pr` | Diff/merge review producer | Supplies diff-anchored findings, changed-file scope, merge risks and residual concerns. | Verification checks claim scope plus resolved PR evidence. |
| `sk-planning` | Acceptance source | Supplies approved scope, milestones, acceptance checkpoints and stop conditions. | Every planned outcome has a verification criterion or explicit limitation. |
| `sk-executing-pro` | Execution coordinator | Supplies changed artifacts, execution log, blockers, decisions and next owner. | Verification confirms the execution claim against fresh artifacts. |
| `sk-execution` | Standard execution workflow | Supplies concise scope, actions, changed artifacts and checks. | Verification decides whether the prepared handoff is sufficient. |
| `sk-done` | Closeout consumer | Consumes the accepted verification record; returns blocked closeout when evidence is missing. | Completion record links to `VERIFY.md` and residual risks. |
| `sk-story-spec` | Behavior criteria source | Supplies story acceptance criteria, examples and story-level edge cases. | Verification maps implementation/test evidence to each story criterion. |
| `sk-specify` | Normative criteria source | Supplies formal requirements, constraints, invariants, exclusions and acceptance rules. | Verification traces each normative requirement to evidence or a gap. |
| `sk-business-analysis` | Business outcome source | Supplies stakeholder goals, business rules, assumptions and measurable outcomes. | Verification checks that the claimed outcome has supporting evidence, not just implementation proof. |
| `sk-api-ba` | API behavior source | Supplies API workflows, states, errors, permissions assumptions and acceptance scenarios. | Verification checks API evidence against the business contract; technical API design remains separate. |
| `sk-clean-architecture` | Architecture evidence source | Supplies module/dependency decisions and architecture constraints; does not ask verification to judge architecture expertise. | Verification checks that the implementation claim includes the agreed architecture artifact and relevant checks. |
| `sk-system-design-pro` | System-design evidence source | Supplies topology, flow, failure-mode and capacity decisions; domain owner remains responsible for technical correctness. | Verification checks claim-to-evidence coverage for the selected system design. |
| `sk-sync` | State/provenance source | Supplies refreshed repository/workspace state, drift findings and preserved user-change notes. | Verification uses the synchronized state as provenance and blocks stale claims. |
| `sk-scaffold` | Structural artifact source | Supplies generated paths, configuration assumptions and TODOs. | Verification checks scaffold completeness/consistency; implementation correctness remains with the stack owner. |

### 3.3 Required verification packet

Every handoff into `sk-verify-pro` should contain:

1. **Claim** — exactly what is being declared complete, mergeable, releasable or accepted.
2. **Criteria** — acceptance criteria, plan checkpoints, review policy or domain invariants.
3. **Evidence** — commands/results, test reports, review findings, artifact links or human checks with freshness.
4. **Coverage map** — which criterion each evidence item proves; mark uncovered criteria explicitly.
5. **Limitations** — stale evidence, unavailable environment, deferred visual/manual checks or domain uncertainty.
6. **Decision** — `pass`, `block`, or `defer`, with the next owner and unblock condition.

### 3.4 Status semantics

| Status | Meaning | Downstream action |
|---|---|---|
| `pass` | The stated claim is covered by fresh, sufficient evidence; known limitations do not invalidate it | `sk-done` or release owner may consume the verification record |
| `block` | A required criterion is unmet, evidence is missing/stale, or a blocker remains | Return to implementation/planning/domain owner; do not close task |
| `defer` | A named human/domain decision is still required and cannot be inferred safely | Record owner, exact question, deadline/condition and do not represent as pass |

## 4. Recommended next actions

### P0 — no further `sk-verify-pro` Boundary change required

- Keep `sk-verify-pro` as the sole final verification owner.
- Keep `sk-verification` as the compatibility facade and prevent invoking both for one task.
- Update generic Cross-skill handoff lists that still mention `sk-verification` as a peer quality owner; they should distinguish facade versus canonical owner.

### P1 — no remaining generic-boundary leads

- Keep the 13 rewritten Boundary contracts and guardrail.
- Add one explicit adjacent-skill comparison to each Boundary.
- Add `sk-tester → sk-verify-pro` and `sk-done ← sk-verify-pro` wording where the skill produces or consumes evidence.
- Rerun the linter on each catalog change; treat any new pair as a review lead only.

### P2 — no remaining Expo/JavaScript adjacency leads

- Keep the existing Expo data/UI/testing ownership contracts.
- Monitor Expo routing through regression fixtures.
- Do not reopen this adjacency without new evidence.

## Method limitations

- The 0 pairs are generated from current `Boundary` token sets at threshold 0.72.
- Similarity cannot determine whether two skills produce the same artifact.
- A pair may be intentionally adjacent and still require a handoff, not a merge.
- Domain correctness, trigger ranking and user-intent routing require manual or fixture-based review.
