---
name: review-pr
description: Review pull requests, merge requests, or branch diffs as a responsible code reviewer. Quality gate before merge.
---

# Review PR

## Purpose

Review a PR/MR or branch diff as a quality-responsible reviewer before merge.

## XML Contract

See [openai.yaml](./agents/openai.yaml)

## Quality Standards

- [ ] PR description is checked against actual diff (coverage column).
- [ ] Each finding has severity, file/location, evidence, and recommendation.
- [ ] Finding severity is one of: Critical / High / Medium / Low / Info.
- [ ] Merge recommendation is one of the defined taxonomy.
- [ ] Security/auth/permission is reviewed if changes touch those areas.
- [ ] Testing gaps are documented even when no blocker findings exist.

## WRONG vs CORRECT

```markdown
// WRONG — no severity, no location
LGTM but there's a minor issue with the naming.

// CORRECT — structured finding
Finding PR-001: Medium — Export button text is misleading for unauthorized users.
Location: `src/features/export/export-button.tsx`, line 15.
Evidence: Button reads "Export All" but the endpoint rejects the request for unauthorized users.
Impact: UX confusion — users see an enabled button that will fail.
Recommendation: Disable the button text to "Export (not available)" for unauthorized roles.
Confidence: High.
```

```markdown
// WRONG — ignoring missing tests
No tests changed, but that's fine.

// CORRECT — calling out testing gaps
Testing gap: No new tests for the export permission check.
Risk: Regression may not be caught.
Follow-up: Add a negative API permission test.
```

## Edge Cases

| Situation | Handling |
|---|---|
| PR has no description | Document as an issue. PR description should explain what and why. |
| Diff is very large (>20 files) | Group by area. Note the size risk. Flag if changes are too broad. |
| Lockfile changes without manifest changes | Flag as potential unintended dependency change. |
| Binary files in the diff | Note they cannot be code-reviewed. Flag if large or unexpected. |
| CI evidence is missing | Note as testing gap. If changes are high-risk, recommend Needs more verification. |

## Limitations

- Does NOT auto-fix the PR.
- Does NOT replace deep security audit.
- Does NOT guarantee finding all bugs if evidence is insufficient.
