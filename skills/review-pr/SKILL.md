---
name: review-pr
description: Review pull requests, merge requests, or branch diffs as a responsible code reviewer. Quality gate before merge.
---

# Review PR

## Purpose

Review a PR/MR or branch diff as a quality-responsible reviewer before merge.

This skill focuses on:

- Identify base/head or diff scope under review.
- Read the PR/MR description if available.
- Map affected files and impacted code paths.
- Review correctness, edge cases, and regression risk.
- Review security, privacy, and data risks when changes touch input, auth, permission, network, files, secrets, DB, or infra.
- Review test coverage and verification evidence.
- Check if the PR description accurately reflects the changes.
- Document findings by severity, with evidence and recommendations.
- Document testing gaps and residual risks.
- Provide a clear merge recommendation: approve, approve with comments, request changes, needs more info, or blocked.

The goal: help the merge decision-maker understand if the PR is safe to merge, what needs fixing, and what risks remain.

## When to Use

Use this skill when:

- User requests a PR/MR review.
- Need to review the current branch against its base.
- Need to review a provided diff.
- Need to create `REVIEW_PR.md`.
- Need to identify blockers before merge.
- Need to check readiness before merge.
- Need to review PR description, test results, or CI evidence.
- Need to assess bugs, regression, security, missing tests, or maintainability risk.
- Need to request changes or provide an approve recommendation.
- Need a reviewer-facing report independent of internal execution.

## When NOT to Use

Do NOT use this skill when:

- Reviewing internal changes after execution in the same workflow; use `review`.
- Only a PR summary is needed without risk review; use `done` or an appropriate summary skill.
- No diff, branch, changed files, or artifacts exist to review.
- User requests immediate code fixes; use `execution` after findings or a mini-plan.
- User requests a fix plan; use `planning`.
- User requests root cause investigation before a diff exists; use `investigate`.
- User requests review of documentation/copywriting not related to code risk.

## XML Contract

```xml
<Contract>
  <Inputs>PR diff, branch diff, base/head, PR description, changed files, test/CI result, relevant codebase context.</Inputs>
  <Outputs>REVIEW_PR.md or review artifact with scope, findings, open questions, testing gaps, residual risks, PR description coverage, merge recommendation.</Outputs>
  <Artifacts>REVIEW_PR.md in session path if applicable; otherwise, review artifact in response.</Arti facts>
  <Safety>Do NOT auto-fix the PR if the user only requested review. Do NOT approve on behalf of the user in a remote system. Do NOT create findings without evidence. Do NOT claim merge-safe if verification is missing. Do NOT ignore security/data risks when changes touch input, auth, permission, secrets, files, networks, DB, migration, or infra.</Safety>
</Contract>
```

## Severity Taxonomy

| Severity | Meaning | Merge Impact |
|---|---|---|
| Critical | Data loss, secret leak, auth bypass, production outage, severe vulnerability, irreversible damage. | Block merge. |
| High | Serious bug/regression, wrong permission, broken main flow, risky migration, missing verification for high-risk area. | Request changes before merge. |
| Medium | Real bug/risk with narrow scope or workaround. | Usually fix before merge or explicitly accept. |
| Low | Minor bug/risk, maintainability issue with real impact, minor edge case. | Optional fix or follow-up. |
| Info | Non-blocking note, improvement suggestion, reviewer observation. | No merge block. |

## Merge Recommendation

| Recommendation | Meaning |
|---|---|
| Approve | No blockers, verification appropriate for risk level. |
| Approve with Comments | No blockers but Low/Info comments or accepted residual risks. |
| Request Changes | Critical/High or important Medium findings need fixing before merge. |
| Needs More Info | Missing context, PR description, diff, test result, or requirement to conclude. |
| Needs More Verification | Code looks OK but evidence is insufficient for the risk level. |
| Blocked | External blocker or branch/CI/conflict state prevents review/merge decision. |

## Workflow

1. Determine if review has enough input.
2. Choose Lite Mode or Full Mode.
3. Identify base/head or diff source.
4. Read the PR/MR description if available.
5. Identify changed files and affected paths.
6. Map relevant code paths at a needed scope.
7. Check if PR scope matches the description.
8. Review correctness and edge cases.
9. Review regression risk.
10. Review security/privacy if changes touch input, auth, permission, network, files, secrets, DB, or infra.
11. Review data/migration/API compatibility if relevant.
12. Review tests, CI, and verification evidence.
13. Review maintainability risk with real impact.
14. Document findings by severity.
15. If no findings, explicitly state "No findings found."
16. Document testing gaps and residual risks.
17. Document open questions.
18. Provide a merge recommendation.
19. Save `REVIEW_PR.md` if Full Mode/session applicable.

## Limitations

- Does NOT auto-fix the PR if the user only requested review.
- Does NOT approve on behalf of the user in a remote PR system.
- Does NOT replace a deep security audit.
- Does NOT guarantee finding all bugs if diff/context/test evidence is missing.
- If fixes are needed, move to `planning` or `execution`.
- If root cause understanding is needed before review, use `investigate`.

<Contract>
  <Inputs>PR diff, branch diff, base/head, PR description, changed files, test/CI results, codebase context.</Inputs>
  <Outputs>REVIEW_PR.md with scope, findings, testing gaps, residual risks, PR description coverage, merge recommendation.</Outputs>
  <Artifacts>REVIEW_PR.md in session path.</Artifacts>
  <Safety>Do NOT auto-fix PR if user only requested review. Do NOT approve for user in remote system. Do NOT create findings without evidence. Do NOT ignore security/data risks.</Safety>
</Contract>
