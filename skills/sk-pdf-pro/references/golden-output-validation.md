# PDF golden-output validation

| Check | Expected evidence |
|---|---|
| Integrity | File opens, page count is expected, encryption/password state is known |
| Text/tables | Extracted text and table structure match the intended fixture |
| Visual layout | Representative pages render without clipping, overlap, blank-page drift or unreadable text |
| Metadata | Title/author/subject/producer and dates are intentional or explicitly N/A |
| Forms/OCR | Fields, coordinates, reading order and OCR confidence are verified where applicable |
| Round trip | Merge/split/rotate/watermark/encrypt output preserves required content and permissions |
| Limits | Unsupported features, lossy transforms and skipped checks are disclosed |

Keep a small golden fixture set: text-heavy, table-heavy, scanned/OCR, form, rotated and encrypted cases. Compare both machine-readable output and rendered pages; a successful file write is not proof of a correct PDF.
