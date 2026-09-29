# Quick fix

> Path=**Quick**. Tiny clear change only. No BA/design/Spec matrices.
> Obey the skill instructions Readable writing.

## Step ledger (mandatory — update every step)

| Step | Name | Status | Evidence |
|---|---|---|---|
| 01 | Init | `todo` / `sk-done` | QUICK.md seeded + Goal set |
| 02 | Task cards | `todo` / `sk-done` / `blocked` | TASKS.md with 1–3 cards + AC/Verify/Dev context |
| 03 | Self-check | `todo` / `sk-done` / `blocked` | Gates pass + committed |

> **Hard rule:** never mark a later step `sk-done` while an earlier step is
> `todo`/`blocked`. `blocked` → stop and ask (Confirm-first).

## Developer overview

| Field | Value |
|---|---|
| Path | `Quick` |
| Status | `ready_for_tasks` / `ready_for_sk-sync` / `blocked` |
| Cards | `0` |
| Next action | _(fill TASKS / sk-sync / upgrade to Lite)_ |

## Goal

<!-- Outcome-first. One sentence. WHO + WHAT + EVIDENCE.
     BAD: "Fix parseDate" / "Add null check"
     GOOD: "parseDate(\"\") returns null (no throw); non-empty parsing unchanged;
            proven by pnpm test -- date."
     If rewrite needs product/design choice → upgrade Path (not Quick).
     See the relevant thinking method -->

_(one sentence)_

## Facts

<!-- IPO Input: from user / repo — paths/IDs. Blocking gaps → upgrade Path. -->

- _(from user / repo — paths/IDs)_

## Out of scope

<!-- Protect the Goal; name what this Quick fix will not change. -->

- _(what this Quick fix will not touch)_

## Unknowns

| Unknown | Blocking? |
|---------|-----------|
| _(none or list — if Blocking=Yes, upgrade Path)_ | Yes / No |

## Handoff

- **Next:** `sk-sync` → `sk-execution` (after PASS)
- **Upgrade instead if:** product/design unknown appears
