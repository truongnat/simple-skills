---
name: sk-reverse-doc
description: >-
  Reconstruct a coherent SPEC_SRS or requirements pack from scattered Word,
  PDF, images, Excel design sheets, or notes. Alias /sk-reverse-doc. Uses office
  / sk-excel-doc-convert when needed; never invent missing requirements.
  (Hard contract.)
---

# Reverse doc

## Shared preamble (do this first)

Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.

## Purpose

Rebuild a **traceable** requirements view from messy inputs. Prefer extracting
evidence first; mark gaps explicitly.

## Step contract (mandatory — invoke = execute ALL steps)

This skill runs as a **sequential step workflow** (`the skill-local `steps/` directory`).
Invoking it **is** executing every step below, in order, one at a time.

| Rule | Requirement |
| --- | --- |
| Invoke | Read `steps/step-01-init.md` immediately, finish it, then open the next step file. |
| Sequence | Finish each step, update the **progress checklist** in ``artifacts/<task-id>/PROGRESS.md`` with evidence, then read the next file. |
| No skipping | NEVER skip a step, never jump straight to the final artifact, never claim complete while any ledger row is `todo`/`blocked`. |
| Blocked | A `blocked` step stops the skill: ask (Confirm-first), resume from the earliest incomplete step. |

| Step | File | Output |
| --- | --- | --- |
| 01 | [step-01-init.md](./steps/step-01-init.md) | Init (mode + ledger) |
| 02 | [step-02-frame.md](./steps/step-02-frame.md) | Frame (inputs + scope) |
| 03 | [step-03-fill.md](./steps/step-03-fill.md) | Fill (produce artifact) |
| 04 | [step-04-self-check.md](./steps/step-04-self-check.md) | Self-check & handoff |

## Contract (mandatory)

| Field | Requirement |
|-------|-------------|
| preferred_role | `researcher` |
| Inputs | Source files (sk-docx/sk-pdf/images/sk-xlsx/md), target shape (`srs` default), optional glossary. |
| Outputs | `REVERSE_DOC.md` inventory + `SPEC_SRS.md` (or linked sk-specify artifact) under the session. |
| Safety | Do NOT invent FR/NFR not evidenced. Do NOT treat OCR guesses as facts — mark Confidence. Do NOT claim lossless layout recovery. Prefer `sk-excel-doc-convert` for 方眼紙 Excel. **Confirm-first** when sources conflict. |

### Required artifacts

#### `REVERSE_DOC.md`
- Seed `templates/REVERSE_DOC.template.md`
- Source inventory, extraction notes, conflicts, confidence, handoff

#### `SPEC_SRS.md` (or mode output)
- Prefer `sk-specify` `SPEC_SRS.template.md` structure when target=`srs`
- Every FR/NFR cites a source ID from `REVERSE_DOC.md`

## Workflow (detailed mechanics — order enforced by the step files)

1. Inventory sources; assign `S-001`…
2. For Excel design sk-docs: run/invoke `sk-excel-doc-convert` when available.
3. For sk-docx/sk-pdf/images: extract text via office skills or describe visible content; record limits.
4. Write `REVERSE_DOC.md` then fill `SPEC_SRS.md` with Source column filled.
5. List conflicts Blocking; Confirm-first.

## Quality Standards

- [ ] Every requirement cites a source ID or is Gap/Unknown.
- [ ] Conflicts listed, not silently merged.
- [ ] Work commit complete.

## Output

Produce a document/media artifact with input and output paths, coverage/quality checks, unsupported-content limitations, validation evidence, and delivery notes.
