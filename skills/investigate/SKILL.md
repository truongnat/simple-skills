---
name: investigate
description: Investigate codebase, bugs, system behavior, or technical questions before implementing. Root-cause analysis, reproduction, impact mapping, and evidence-based recommendations.
---

# Investigate

## Purpose

Find technical truth before deciding to fix, plan, or implement.

This skill focuses on:

- Identify the investigation question.
- Collect evidence from logs, errors, screenshots, reproduction, codebase, config, or test results.
- Reproduce the issue if possible.
- Trace related code paths.
- Separate observed facts from inferences/hypotheses.
- Identify root cause or remaining hypotheses.
- Assess impact, blast radius, and regression risk.
- Recommend a fix, workaround, or next investigation step.
- Save `INVESTIGATE.md` for handoff to planning/execution/review.

The goal: avoid fixing code based on guesses, while producing clear enough evidence for the team to decide next steps.

## When to Use

Use this skill when:

- User asks to investigate a bug.
- User provides logs/errors/screenshots and needs analysis.
- Need to understand code paths or system behavior.
- Need to reproduce an issue before fixing.
- Need root-cause analysis.
- Need impact analysis before changing code.
- Need to determine if the bug is FE, BE, DB, config, infra, auth, data, or external.
- Need to check for regression or behavior drift.
- Need to map affected modules before planning.
- Not sure if workspace changes are needed.
- Multiple hypotheses exist and evidence is needed to eliminate some.
- Need to create or update `INVESTIGATE.md`.

## When NOT to Use

Do NOT use this skill when:

- Root cause is already clear and only implementation is needed; use `execution`.
- Direction is clear and task breakdown is needed; use `planning`.
- Only product idea brainstorming is needed; use `brainstorming`.
- Business requirements are unclear; use `business-analysis`.
- Reviewing a PR; use `review-pr`.
- Reviewing changes after execution; use `review`.
- Only syncing repo state before execution is needed; use `sync`.
- Deep external source research is needed; use `research`.
- User needs a quick fix with an obvious root cause and clear scope.

## XML Contract

```xml
<Contract>
  <Inputs>Problem description, expected/actual behavior, logs/errors/reproduction, screenshots, test results, codebase context, config metadata, environment details, session path if available.</Inputs>
  <Outputs>INVESTIGATE.md or investigation report with question, status, evidence, reproduction, observed facts, hypotheses, code path, impact map, root cause, recommendation, open questions, handoff.</Outputs>
  <Artifacts>INVESTIGATE.md in session path if applicable; otherwise, investigation report in response.</Artifacts>
  <Safety>Read-only by default. Do NOT modify code unless requested. Do NOT run destructive commands. Do NOT read/copy secrets or sensitive data without a clear reason. Do NOT claim root cause when evidence is insufficient. Do NOT paste long logs or sensitive output into artifacts.</Safety>
</Contract>
```

## Investigation Status

| Status | Meaning |
|---|---|
| Root Cause Confirmed | Root cause has strong evidence. |
| Likely Root Cause | Root cause is highly probable but not fully verified. |
| Hypotheses Identified | Hypotheses exist but not enough evidence to conclude. |
| Reproduced, Not Root-Caused | Issue reproduced but cause not found. |
| Not Reproduced | Could not reproduce with attempted conditions. |
| Needs More Evidence | Missing logs/context/env/reproduction to conclude. |
| Blocked | Blocked by access/env/secret/tooling/missing data. |

## Workflow

1. Identify the investigation question.
2. Choose Lite Mode or Full Mode.
3. Identify session path if applicable.
4. Collect context provided by the user.
5. Check sensitive data boundaries.
6. Collect facts from artifacts/files/commands (read-only).
7. Reproduce if possible and safe.
8. Trace related code paths.
9. Separate observed facts from inferences.
10. List hypotheses.
11. Check supporting and counter-evidence for each hypothesis.
12. Determine root cause if enough evidence exists.
13. If insufficient, document remaining hypotheses and how to verify them.
14. Document impact and blast radius.
15. Document risks.
16. Provide recommendation: fix, workaround, or next investigation.
17. Document open questions.
18. Handoff to planning/execution/review or stop if blocked.
19. Save `INVESTIGATE.md` if Full Mode/session applicable.

## Evidence Policy

Good evidence has: clear source, timestamp if relevant, file/path/function/line if applicable, command run if applicable, input and output concisely, reproduction conditions, result (pass/fail/not reproduced).

Do NOT paste: overly long logs, secrets/tokens/passwords, full database dumps, unnecessary PII, command output not serving the conclusion.

## Observed vs Inferred

Observed facts = things directly seen from evidence. Example: "`GET /teachers` returns 500 when user 11716 is included."

Inferences = reasoning based on observed facts. Example: "The encrypted password attribute is likely plaintext for users updated directly in Keycloak." Must include confidence: High / Medium / Low.

## Command Safety

Investigate by default does NOT mutate workspace.

Allowed (read-only safe): `ls`, `find`, `grep`, `rg`, `git status`, `git diff --name-only`, reading source files (non-sensitive), running focused tests if they do not mutate external state, running build/typecheck/lint if they do not modify files.

NOT allowed by default: commands that write files/generate large artifacts, `npm install`/`pnpm install`, migrations/seeds, deploy, reset/clean/checkout/rebase, delete/rename/move, commands against production data/service, commands that may leak secrets.

## Limitations

- This skill does NOT guarantee a fix exists.
- This skill does NOT replace an execution plan if code changes are needed.
- This skill does NOT replace review after fixing.
- This skill does NOT replace a deep security audit.
- This skill does NOT conclude with certainty if evidence is insufficient.
- This skill does NOT auto-fix code without being requested.
- This skill does NOT read secrets/PII without a clear reason and appropriate approval.

<Contract>
  <Inputs>Problem description, expected/actual behavior, logs/errors/reproduction, codebase context, environment details.</Inputs>
  <Outputs>INVESTIGATE.md with question, status, evidence, reproduction, observed facts, hypotheses, code path, impact map, root cause, recommendation, open questions.</Outputs>
  <Artifacts>INVESTIGATE.md in session path.</Artifacts>
  <Safety>Read-only by default. Do NOT modify code unless requested. Do NOT run destructive commands. Do NOT read secrets without a clear reason. Do NOT claim root cause when evidence is insufficient.</Safety>
</Contract>
