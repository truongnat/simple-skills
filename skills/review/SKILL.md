---
name: review
description: Review changes after execution: bugs, regression, missing tests, security/data risks, maintainability, and readiness before done/PR.
---

# Review

## Purpose

Evaluate changes after execution before marking done, creating a PR, or handing off.

This skill focuses on:

- Verify changes match goal/scope in the plan.
- Find actual bugs, regression risks, and missed edge cases.
- Check missing tests or verification gaps.
- Check security, auth, permission, secrets, data, and migration risks.
- Check maintainability, readability, and consistency if there is real impact.
- Document findings with severity, evidence, and clear recommendations.
- Document residual risks and testing gaps even when no findings exist.
- Provide a clear recommendation: ready, ready with risks, or needs fix.

The goal: produce a review with real value, helping decide if changes are safe for done/merge/deploy or need to return to execution.

## When to Use

Use this skill when:

- After execution.
- Before creating a done report.
- Before creating a PR message.
- Before merging or handing off to QA/user.
- When reviewing a diff, changed files, or artifacts.
- When `REVIEW.md` is needed.
- When a quality gate is needed before done.
- When assessing testing gaps, residual risks, or missed requirements.
- When the user requests code review without asking you to fix it.

## When NOT to Use

Do NOT use this skill when:

- No changes, diff, or artifacts exist to review.
- User only needs brainstorming or research.
- Requirements are unclear and no execution has happened.
- Immediate implementation/fix is needed; use `execution`.
- Planning a fix is needed; use `planning`.
- Reviewing an external pull request under a separate workflow; use `review-pr` if available.
- User only needs pure style/lint formatting without risk review.

## XML Contract

```xml
<Contract>
  <Inputs>Diff/file changes, PLAN.md, EXECUTION.md, test/check results, verification evidence, scope/context if available.</Inputs>
  <Outputs>REVIEW.md or review artifact with scope reviewed, findings, testing gaps, residual risks, open questions, recommendation, handoff.</Outputs>
  <Artifacts>REVIEW.md in session path if applicable; otherwise, review artifact in response.</Artifacts>
  <Safety>Do NOT auto-fix code if user only requested review. Do NOT create findings without evidence. Do NOT claim safe if verification is missing. Do NOT ignore security/data risks when changes touch input, auth, permission, secrets, files, network, DB, or infra.</Safety>
</Contract>
```

## Severity Taxonomy

| Severity | Meaning | Typical Action |
|---|---|---|
| Critical | Data loss, secret leak, auth bypass, severe crash, production outage, or security breach. | Must fix before done/merge/deploy. |
| High | Serious bug, major regression, wrong logic, wrong permission, dangerous migration, missing verification for a high-risk area. | Should fix before done/merge. |
| Medium | Real bug or risk with narrow scope or a workaround. | Fix soon or explicitly accept risk. |
| Low | Minor issue that may cause confusion or have a minor maintainability impact. | Fix if cheap or track follow-up. |
| Info | Non-blocking observation, improvement suggestion, note for reviewer. | Optional follow-up. |

## Finding Categories

| Category | Examples |
|---|---|
| Correctness | Wrong logic, wrong edge case, wrong state, wrong validation. |
| Regression | Change breaks existing behavior. |
| Requirement Gap | Does not meet plan, AC, or user request. |
| Missing Test | No test/verification for critical logic. |
| Security | Auth, permission, injection, XSS, CSRF, secrets, unsafe file/network. |
| Data/Migration | Data loss, invalid migration, backward compatibility, wrong mapping. |
| API/Contract | Breaking API, response shape changes, missing error handling. |
| UX/Accessibility | Poor flow, wrong error state, accessibility issue with impact. |
| Performance | Slow query, large bundle increase, unnecessary loop/re-render. |
| Maintainability | Duplication or overly complex code that creates real bug risk. |

## Workflow

1. Determine if review has enough input.
2. Choose Lite Mode or Full Mode.
3. Read `PLAN.md` if available.
4. Read `EXECUTION.md` if available.
5. Identify goals/scopes and expected outcomes.
6. Identify actual changed files/diff/artifacts.
7. Compare changes against plan and acceptance criteria.
8. Check correctness and edge cases.
9. Check regression risk.
10. Check missing tests and verification gaps.
11. Check security if changes touch input, auth, secrets, files, network, DB, or infra.
12. Check data/migration/API compatibility if relevant.
13. Check maintainability risk with real impact.
14. Document findings by severity.
15. If no findings, explicitly state "No findings found."
16. Document testing gaps.
17. Document residual risks.
18. Provide a recommendation: ready, ready with risks, needs fix, or blocked.
19. Save `REVIEW.md` if Full Mode/session applicable.

## Limitations

- Review does NOT auto-fix code if the user only requested review.
- Review does NOT replace execution.
- Review does NOT replace full QA or deep security audit.
- Review cannot guarantee no remaining bugs if diffs, tests, or context are missing.
- If fixes are needed, return to `planning` or `execution`.
- If review input is insufficient, document the limitation instead of over-confidently concluding.

<Contract>
  <Inputs>Diff/file changes, PLAN.md, EXECUTION.md, test/check result, verification evidence, scope/context.</Inputs>
  <Outputs>REVIEW.md with scope reviewed, findings, testing gaps, residual risks, recommendation, handoff.</Outputs>
  <Artifacts>REVIEW.md in session path.</Artifacts>
  <Safety>Do NOT auto-fix code if user only requested review. Do NOT create findings without evidence. Do NOT ignore security/data risks.</Safety>
</Contract>
