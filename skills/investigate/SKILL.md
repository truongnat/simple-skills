---
name: investigate
description: Investigate codebase, bugs, system behavior, or technical questions before implementing. Root-cause analysis, reproduction, impact mapping, and evidence-based recommendations.
---

# Investigate

## Purpose

Find technical truth before deciding to fix, plan, or implement.

## XML Contract

See [openai.yaml](./agents/openai.yaml)

## Quality Standards

- [ ] Status is one of the defined taxonomy values.
- [ ] Observed facts have explicit sources.
- [ ] Inferences are separated from observed facts with confidence levels.
- [ ] If root cause is claimed: evidence is sufficient to explain all observed symptoms.
- [ ] Recommendation distinguishes: fix / workaround / next investigation.
- [ ] Reproduction steps include environment, preconditions, and both expected and actual results.

## WRONG vs CORRECT

```markdown
// WRONG — no source, no confidence
The bug is probably in the export service.

// CORRECT — evidence-based
Observation: `GET /api/export` returns 500 when user 11716 is in the result set.
Stack trace: `DecryptInitialPassword()` throws on line 42 of `encryption.ts`.
Hypothesis H-001: The encrypted value for this user was set by Keycloak directly (plaintext).
Evidence: Keycloak audit log shows password was reset via admin console for user 11716.
Confidence: Medium.
```

```markdown
// WRONG — claiming root cause without evidence
Root cause: caching issue.

// CORRECT — qualified root cause
Root cause: Likely the encrypted attribute is plaintext, causing decryption to fail.
Confidence: Medium.
Alternative hypothesis: The encryption key changed between runs (low probability, no evidence).
Next step: Inspect the database value for user 11716's password attribute safely.
```

## Edge Cases

| Situation | Handling |
|---|---|
| Cannot reproduce the issue | Status = Not Reproduced. Document conditions tried and possible reasons. |
| Log is truncated or incomplete | Document as limitation. Do NOT over-claim from partial data. |
| Sensitive data in logs (PII, tokens) | Redact before quoting. Document as security risk if exposure is found. |
| Multiple root causes are possible | List as multiple hypotheses with confidence for each. Do NOT pick one arbitrarily. |
| Issue is environment-specific | Document environment differences. Recommend cross-env comparison. |

## Limitations

- Does NOT guarantee a fix exists.
- Does NOT replace planning or execution.
- Does NOT replace deep security audit.
