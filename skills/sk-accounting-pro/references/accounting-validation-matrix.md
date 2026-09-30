# Accounting validation matrix

Use this matrix after the compact workflow when the task involves a high-risk claim. Fixtures must use synthetic identifiers and redacted values. The domain skill produces evidence; `sk-tester` executes tests, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` owns the final `pass`/`block`/`defer` decision.

| Scenario | Expected result | Evidence | Failure/limitation | Next owner |
|---|---|---|---|---|
| Double-entry balance | Post a 1,250 expense with cash credit; debit and credit totals both equal 1,250. | Journal export, trial-balance totals, reviewer initials. | Unposted subledger or rounding mismatch blocks close. | sk-tester -> sk-verify-pro |
| Period close | Lock March only after accruals, cut-off and retained earnings roll-forward reconcile. | Close checklist, period-lock audit event, trial balance before/after. | Late March invoice remains in April queue and is disclosed. | sk-review -> sk-verify-pro |
| Reversal | Reverse an accrual in April with a linked original entry; never edit the posted March entry. | Original/reversal IDs, equal-and-opposite lines, timestamps. | Unlinked reversal blocks audit-trail acceptance. | sk-accounting-pro -> sk-review |
| FX | Revalue a EUR payable at the approved close rate and post realized/unrealized FX separately. | Rate source/date, calculation sheet, journal IDs. | Missing rate provenance or mixed currencies blocks posting. | sk-review -> sk-verify-pro |
| Reconciliation | Bank balance plus timing items equals the adjusted book balance; unexplained difference stays open. | Reconciliation statement, unmatched-item register, owner/date. | Do not force-balance with a suspense entry without approval. | sk-accounting-pro -> sk-planning |
| Audit trail | Every adjustment retains actor, reason, source document and approval chain. | Immutable event log and source-document links with redacted fixture IDs. | PII or secrets are never copied into fixtures. | sk-accounting-pro -> sk-review |
| Known-answer statement | A fixture trial balance produces assets = liabilities + equity and net income matches the control total. | Known-answer totals and comparison output. | Different accounting basis is a limitation, not a pass. | sk-verify-pro |
| Failure/recovery | If posting fails after validation, retry idempotently or quarantine the batch; do not duplicate entries. | Failure log, retry key, quarantine/replay result. | Named owner must approve replay and period impact. | sk-tester -> sk-verify-pro |

## Verification response shape

Return exactly:

- **Claim:** the bounded domain claim being assessed.
- **Criteria:** scenario rows and acceptance thresholds.
- **Evidence:** paths, commands, fixture IDs, timestamps and reviewer findings.
- **Limitations:** untested environments, assumptions, stale inputs or residual risk.
- **Next owner:** `sk-tester`, `sk-review`, `sk-review-pr`, the named domain owner, or `sk-verify-pro`.

Do not claim final release status from this matrix; hand the packet to `sk-verify-pro`.
