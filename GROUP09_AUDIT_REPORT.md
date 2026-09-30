# Audit & remediation — Nhóm 09: Tài liệu, nghiên cứu & business

**Ngày:** 2026-09-29
**Phạm vi:** 24 skill trong taxonomy Nhóm 09.

## Baseline findings

Baseline ghi nhận 8 skill legacy thiếu metadata routing (`sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`), tương đương 40 field. 14/24 skill có tags/roles rỗng. Contract scan chi tiết cho thấy:

- 11 skill thiếu explicit `Boundary`.
- 17 skill thiếu `Required inputs`.
- 22 skill thiếu `Cross-skill handoffs`.
- Không có execution-pattern candidate ngoài code examples.

## Remediation đã triển khai

- Chuẩn hóa metadata cho toàn bộ 24 skill với tags/roles phù hợp documentation, research và business; giữ specialized metadata khi đã tồn tại.
- Bổ sung ownership boundary theo từng loại artifact:
  - Business/system diagrams.
  - Enterprise documentation và docs-as-code.
  - DOCX/XLSX/PDF/PPTX office artifacts.
  - Research/reverse-document workflows.
  - Reports, market research, finance/accounting và technical writing.
- Bổ sung `When not to use`, `Required inputs` và `Cross-skill handoffs` cho skill legacy.
- Làm rõ routing giữa `sk-research`, `sk-web-research-pro`, `sk-market-research-pro`, `sk-business-analysis`, `sk-docs`, `sk-technical-writing-pro` và format-specific skills.
- Giữ nguyên domain examples và format-specific references; không thêm repo script/tooling.

## Verification

| Check | Result |
|---|---:|
| Skills kiểm tra | 24/24 |
| Contract errors | 0 |
| Empty tags/roles | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Tooling hits ngoài fenced examples | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 09 đã đạt cùng contract routing với Nhóm 01–08: metadata đầy đủ, boundary rõ, inputs được khai báo, handoffs explicit và evidence/format limitations được định tuyến tới đúng specialist skill.
