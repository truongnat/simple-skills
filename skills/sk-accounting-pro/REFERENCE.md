# Accounting reference

Use this reference for bookkeeping, journal entries, reconciliations, and statement preparation. Confirm the applicable jurisdiction, accounting basis, period, chart of accounts, approval authority, and source-document quality before posting or interpreting transactions. This guidance does not replace a qualified accountant or local tax/regulatory advice.

## Accounting control contract

Record these inputs before processing:

| Area | Required detail |
|---|---|
| Basis | GAAP/IFRS or the organization’s approved policy |
| Period | Posting date, accounting period, close status, and time zone |
| Accounts | Chart-of-accounts version and normal debit/credit balance |
| Source | Invoice, receipt, bank record, contract, payroll, or adjustment support |
| Authority | Preparer, reviewer, approver, and segregation-of-duties rule |
| Currency | Transaction currency, functional currency, FX rate date, and rounding |
| Evidence | Journal ID, attachments, audit trail, and reversal/adjustment link |

Never invent missing source documents or silently overwrite a posted entry. Use an explicit adjusting or reversing entry with reason, approver, and linkage.

## Double-entry workflow

1. Identify the economic event and posting period.
2. Determine affected accounts and whether each has a debit or credit normal balance.
3. Measure the amount and currency using the approved policy.
4. Draft balanced journal lines with date, description, source ID, and preparer.
5. Validate total debits equal total credits and accounts are active/postable.
6. Obtain required approval before posting.
7. Post to the ledger and retain an immutable audit trail.
8. Reconcile subledger, control account, and supporting document.

For a simple cash purchase of supplies:

```text
Debit  Office Supplies Expense   250.00
Credit Cash                      250.00
```

The entry is balanced, but classification still requires policy review: capitalization threshold, prepaid treatment, tax, and cost center may change the correct accounts.

## Period close and adjustments

Use a close checklist covering cutoff, accruals, prepaids, depreciation, inventory, payroll, intercompany balances, FX revaluation, bank reconciliation, control-account reconciliation, and review sign-off. Mark late adjustments explicitly and preserve the original period decision.

A reversal should reference the original journal ID, preserve the original amount and accounts unless policy requires otherwise, and specify its effective date. Do not use a reversal to hide an error; document the correction reason.

## Reconciliation

Reconcile from independent sources, not by forcing balances to agree. Match on stable identifiers where available and classify unmatched items:

- timing difference;
- missing ledger entry;
- missing bank/subledger item;
- duplicate;
- amount or currency mismatch;
- invalid account classification;
- unauthorized or suspicious transaction.

Every reconciling item needs owner, age, explanation, expected resolution date, and escalation threshold. Automatic matching must be deterministic, reviewable, and safe against duplicate settlement.

## Financial statements

Build statements from a trial balance and a documented mapping from accounts to statement lines. Validate:

- balance sheet equation: assets = liabilities + equity;
- retained earnings roll-forward and current-period profit linkage;
- cash flow reconciliation to opening and closing cash;
- comparative periods and consistent classifications;
- elimination of intercompany balances where applicable;
- notes for material estimates, policy changes, restatements, and contingencies.

Do not treat a balanced trial balance as proof that transactions are correctly classified or complete.

## Receivables, payables, and controls

For accounts receivable, track invoice, due date, customer, currency, collection status, credit note, and expected-loss policy. For accounts payable, match invoice, purchase order, receipt, approval, duplicate status, and payment. Separate vendor creation, invoice approval, payment release, and bank reconciliation where possible.

Protect personally identifiable and banking data. Restrict access by role, redact sensitive exports, retain evidence according to policy, and review unusual manual journals, after-hours postings, round-dollar entries, and rapid reversals.

## FX and rounding

Store transaction currency and functional-currency values together with the rate source/date and rounding policy. Post realized and unrealized FX differences to the approved accounts. Apply rounding consistently and reconcile residual cents rather than distributing unexplained differences.

## Validation cases

| Case | Expected result | Evidence |
|---|---|---|
| Balanced journal | Total debits equal total credits; entry can proceed to approval | Journal control total |
| Unbalanced journal | Posting blocked with actionable error | Validation result; no ledger mutation |
| Inactive or wrong-period account | Posting blocked or routed to approved adjustment flow | Account/period error |
| Duplicate invoice | Duplicate detected using configured matching keys; no second payment | Duplicate report |
| Bank reconciliation match | Matched item is linked to bank and ledger records | Reconciliation link |
| Reconciling difference | Difference remains visible with owner and age; no forced balancing | Open-items report |
| Reversal | Original entry remains; reversal references it and balances | Journal lineage |
| FX transaction | Rate source/date and both currency values are retained | FX audit fields |
| Trial balance | Debits and credits balance, with account mapping review | Trial-balance report |
| Statement preparation | Assets = liabilities + equity and cash flow ties to cash | Statement controls |
| Unauthorized manual journal | Approval or segregation-of-duties control blocks posting | Approval/audit log |
| Period close | Required close controls complete before period is locked | Close checklist and sign-off |

## Minimum audit trail

Retain immutable journal ID, source-document ID, posting timestamp, effective date, account and amount before/after correction, preparer, approver, reason, reversal/correction links, and system correlation ID. Make exports reproducible from a named ledger snapshot and chart-of-accounts version.

## Delivery checklist

Before calling the task complete, confirm the accounting basis and period, source documents, chart of accounts, balanced entries, reconciliation status, statement controls, approvals, audit trail, sensitive-data handling, unresolved differences, and the exact output format. State assumptions and route tax/legal judgments to the appropriate qualified owner.
