# Financial analysis reference

Use this reference for repeatable financial modeling, valuation, and statement-analysis work. The output is an analysis, not a guarantee of investment performance or a substitute for professional, legal, tax, or regulatory advice. Preserve source dates, fiscal periods, currencies, units, and assumptions so another analyst can reproduce the result.

## Evidence and period discipline

Create a source register before calculating:

| Field | Record |
|---|---|
| Source | Filing, company release, market-data provider, or management input |
| As-of date | Data availability date and market close convention |
| Fiscal period | FY/Q, trailing period, forecast period, and restatement status |
| Currency/unit | Currency, thousands/millions, nominal/real, per-share basis |
| Transformation | Mapping, normalization, sign convention, FX conversion, and rounding |
| Confidence | Directly reported, derived, estimated, or unavailable |

Do not mix fiscal periods, currencies, or continuing/discontinued operations without labeling the transformation. Keep historical actuals separate from forecasts and make the boundary visible in tables and charts.

## Statement analysis

Start with a normalized three-statement view. Confirm that the balance sheet balances, cash flow reconciles to cash movement, and non-GAAP adjustments are clearly separated from reported figures. Ratio results require a denominator definition and period convention.

Examples of explicit conventions:

- Current ratio = current assets / current liabilities.
- Gross margin = gross profit / revenue.
- ROE should state average or ending equity and treatment of preferred equity.
- Debt-to-equity should state whether lease liabilities and minority interest are included.
- Growth rates should state whether they are YoY, sequential, CAGR, or organic.

Use `N/M` for a non-meaningful ratio rather than hiding division by zero or a negative denominator. Explain material changes instead of inferring causality from a ratio alone.

## DCF model structure

A defensible DCF separates assumptions, forecast drivers, calculations, and outputs.

```text
Revenue -> operating assumptions -> EBIT -> taxes -> NOPAT
        -> D&A, capex, working capital -> free cash flow
        -> discount rate -> present value -> terminal value -> enterprise value
        -> net debt and dilution -> equity value -> value per share
```

Use a consistent convention for mid-year or end-year discounting. A common unlevered free cash flow form is:

```text
UFCF = EBIT × (1 − tax rate) + D&A − capex − change in NWC
Enterprise value = Σ(UFCF_t / (1 + WACC)^t) + PV(terminal value)
```

Terminal value must state the method. For perpetual growth:

```text
TV = UFCF_(n+1) / (WACC − g)
UFCF_(n+1) = UFCF_n × (1 + g)
```

Reject or flag assumptions where `WACC <= g`, terminal growth is unsupported by the business context, margins jump without a driver, or terminal value dominates without sensitivity disclosure.

## Comparable companies

Build a peer-selection rationale before calculating multiples. Record business model, geography, growth, margin, capital intensity, accounting differences, and size. Keep numerator and denominator periods aligned. Label whether multiples use LTM, NTM, or a specific fiscal year. Show median and dispersion; do not present a single peer multiple as certainty.

For EV/EBITDA, reconcile enterprise value to equity value using the same net debt, leases, non-controlling interests, and preferred claims convention across peers. For P/E, document treatment of loss-making companies and one-off items.

## Data quality and model controls

- Assert required columns and unique period keys.
- Check signs for expenses, cash flow, debt, and working capital.
- Check that units and currencies are consistent.
- Reconcile statement totals and cash movement.
- Detect missing, duplicated, restated, or stale data.
- Keep formulas deterministic and avoid hidden hard-coded overrides.
- Round only for presentation; calculate using full precision.
- Preserve input snapshots and model version.

## Sensitivity and uncertainty

At minimum, show a two-way sensitivity for the two assumptions that most affect value, commonly WACC and terminal growth or revenue growth and margin. Add scenario labels such as bear/base/bull, state which assumptions change together, and identify break-even conditions. Explain limitations such as cyclicality, sparse history, survivorship bias, market-data timing, and forecast uncertainty.

## Validation cases

| Case | Expected result | Evidence |
|---|---|---|
| Balance sheet inputs | Assets equal liabilities plus equity within stated rounding tolerance | Reconciliation check |
| Currency conversion | All converted values use one dated FX convention | Source register and conversion table |
| DCF base case | Present values, terminal value, enterprise value, and equity bridge reconcile | Calculation trace |
| DCF sensitivity | Increasing WACC lowers value; increasing terminal growth raises value within valid bounds | Sensitivity grid |
| Invalid WACC/growth | Model flags or rejects `WACC <= g` | Validation error |
| Comparable peer outlier | Outlier is shown and treatment is documented, not silently removed | Peer table and rationale |
| Missing period | Calculation stops or marks unavailable; no silent zero substitution | Data-quality report |
| Unit mismatch | Thousand/million or per-share mismatch is detected | Unit assertions |
| Restated financials | Restatement status and chosen version are disclosed | Source register |
| Reproducibility | Same inputs and model version produce the same outputs | Saved input snapshot and hash/version |

## Reporting template

Present the analysis in this order: objective and scope; sources and periods; assumptions; method; key calculations; results; sensitivity/scenarios; risks and limitations; conclusion; and next steps. Distinguish facts, derived metrics, estimates, and recommendations. Avoid language that implies certainty where the model is scenario-based.
