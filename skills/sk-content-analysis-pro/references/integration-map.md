# Content analysis — integration map

| Skill | When |
|-------|------|
| **`sk-business-analysis`** | Requirements, BRD, decisions from extracted facts |
| **`sk-security-pro`** | PII/credentials in content; redaction policy; safe handling |
| **`sk-data-analysis-pro`** | Numeric profiling, pivots on **extracted** structured tables |
| **`sk-web-research-pro`** | External verification of claims not in provided corpus |
| **`sk-image-processing-pro`** | Crop/resize/enhance **before** semantic read when needed |
| **`sk-testing-pro`** | Golden-file regression for automated extraction pipelines (CI) |
| **`sk-repo-tooling-pro`** | Shared `scripts/` for repeatable FFmpeg/OCR steps |
| **`sk-seo-pro`** | Marketing/web asset angle (rare) |

**Boundary:** **`sk-content-analysis-pro`** owns **reading, structuring, and reporting** on user-supplied content; **`sk-business-analysis`** owns **business deliverable** packaging; **`sk-data-analysis-pro`** owns **quantitative** analysis of tabular **data** once correctly extracted.
