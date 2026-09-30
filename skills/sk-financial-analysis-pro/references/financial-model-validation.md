# Financial model validation matrix

Use this matrix after the compact workflow when the task involves a high-risk claim. Fixtures must use synthetic identifiers and redacted values. The domain skill produces evidence; `sk-tester` executes tests, `sk-review`/`sk-review-pr` records findings, and `sk-verify-pro` owns the final `pass`/`block`/`defer` decision.

| Scenario | Expected result | Evidence | Failure/limitation | Next owner |
|---|---|---|---|---|
| DCF | A known-answer DCF with explicit forecast, terminal value and discount-rate inputs reproduces the control valuation. | Model output, formula trace, control total. | Unsupported terminal assumptions remain disclosed. | sk-review -> sk-verify-pro |
| Comps | Comparable-company multiples use a dated, labeled peer set and consistent numerator/denominator. | Peer list, source timestamps, normalized multiple table. | Do not mix LTM and NTM without labeling. | sk-review -> sk-verify-pro |
| Assumptions | Every material assumption has owner, source, date, unit and rationale. | Assumption register and change log. | Unowned assumptions block decision use. | sk-planning -> sk-verify-pro |
| Sensitivity | Changing WACC and terminal growth updates the valuation table monotonically within bounds. | Sensitivity grid and monotonicity check. | Nonlinear behavior is investigated, not averaged away. | sk-tester -> sk-verify-pro |
| Units | Currency, scale, percentages and per-share units remain consistent across tabs and outputs. | Unit metadata and dimensional checks. | Mixed thousands/millions blocks pass. | sk-review -> sk-verify-pro |
| Periods | Historical, forecast and stub periods have explicit dates and no double-counted partial year. | Period map and row-level date checks. | Missing fiscal calendar is a limitation. | sk-financial-analysis-pro -> sk-planning |
| Known answer | The fixture model matches published control outputs within declared tolerance. | Control workbook/output and tolerance report. | Tolerance must be stated before comparison. | sk-tester -> sk-verify-pro |
| Failure/rollback | If a source refresh changes a key assumption, preserve the prior version and require review before republishing. | Version diff, rollback pointer, review decision. | Do not overwrite the last approved model. | sk-review -> sk-verify-pro |

## Verification response shape

Return exactly:

- **Claim:** the bounded domain claim being assessed.
- **Criteria:** scenario rows and acceptance thresholds.
- **Evidence:** paths, commands, fixture IDs, timestamps and reviewer findings.
- **Limitations:** untested environments, assumptions, stale inputs or residual risk.
- **Next owner:** `sk-tester`, `sk-review`, `sk-review-pr`, the named domain owner, or `sk-verify-pro`.

Do not claim final release status from this matrix; hand the packet to `sk-verify-pro`.
