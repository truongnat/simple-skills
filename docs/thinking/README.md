# Thinking methods

Session-wide ways of working — **not** report section titles. Never brand
headings or create method-named artifacts (`OUTCOME.md`, `IPO.md`,
`SMALL_BATCH.md`, `IMPLICIT.md`, `SSOT.md`, `FEEDBACK.md`, `HAPPY_PATH.md`,
`5W1H.md`, …).

Ops rules (short): `.agents/SKILL_PREAMBLE.md` → Thinking methods  
Policy summary: `.agents/AGENT_POLICY.md` → Thinking methods  
Source ops/policy: `docs/policy/SKILL_PREAMBLE.md`, `docs/policy/AGENT_POLICY.md`

## Framing order

```text
1. Outcome-first              → lock Output (WHO / WHAT / EVIDENCE)
2. Input → Process → Output   → bind Input + Process to that Output
3. Make implicit explicit     → classify & surface material implicits
4. Single Source of Truth     → cite canonical stores; no forks
5. Small-batch                → size completable units + coding Verify slots
6. Feedback loop              → modality + latency×risk (Example/See/Run/Spike)
7. Default path first         → L1 happy → L2 validation → L3 errors → L4 rare
8. 5W1H (if unclear)          → diagnose; fold into real sections
9. Vital few                  → prioritize in summaries / memory
```

## Methods in this folder

| Method | Normative file | Installed path |
| --- | --- | --- |
| **Outcome-first** | [outcome-first.md](./outcome-first.md) | `.agents/thinking/outcome-first.md` |
| **Input → Process → Output** | [input-process-output.md](./input-process-output.md) | `.agents/thinking/input-process-output.md` |
| **Make implicit explicit** | [make-implicit-explicit.md](./make-implicit-explicit.md) | `.agents/thinking/make-implicit-explicit.md` |
| **Single Source of Truth** | [single-source-of-truth.md](./single-source-of-truth.md) | `.agents/thinking/single-source-of-truth.md` |
| **Small-batch** | [small-batch.md](./small-batch.md) | `.agents/thinking/small-batch.md` |
| **Feedback loop** | [feedback-loop.md](./feedback-loop.md) | `.agents/thinking/feedback-loop.md` |
| **Default path first** | [default-path-first.md](./default-path-first.md) | `.agents/thinking/default-path-first.md` |

Vital few and 5W1H are fully specified in policy/preamble today (short methods).
When a method needs staff-engineer detail, add a file here and link it from
preamble + this index — do **not** invent a separate skill.

**Hybrid C:** Small-batch = unit size + coding Verify rhythm; Feedback loop =
when/which signal by latency×risk. **Default path first** = deepen L1→L2→L3→L4
(name edges early via Make-explicit; implement rare late). Coding-card hard
size stays in `planning/steps/step-03-fill-tasks.md` §B–§C. Confirm-first stays
in `SKILL_PREAMBLE.md`; SSOT owns canonical stores + visual docs↔code conflicts.
