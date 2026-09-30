# Consistency audit — Nhóm 01–04

**Ngày:** 2026-09-29
**Phạm vi:** 96 skill thuộc Nhóm 01, 02, 03 và 04.

## Kết quả audit

| Contract | Kết quả |
|---|---:|
| Skill được kiểm tra | 96 |
| `name` khớp thư mục | 96/96 |
| Frontmatter có `name`, `description`, `sk-kind`, `sk-version` | 96/96 |
| Có `sk-tags`, `sk-roles`, `sk-compatible` và không rỗng | 96/96 |
| Broken local links | 0 |
| Markdown fence lệch | 0 |
| Execution/repo command pattern ngoài code examples | 0 |

## Cải tiến đã áp dụng

- Chuẩn hóa metadata routing cho các skill legacy còn thiếu, ưu tiên giữ tags/roles chuyên biệt đã tồn tại.
- Bổ sung description còn thiếu cho `sk-javascript-testing-patterns`.
- Sửa các tham chiếu GitHub CLI/repo execution còn sót trong `sk-to-issues-pro` và `sk-to-prd-pro` thành guidance tạo artifact, không tự submit/publish.
- Loại wording source-control execution không cần thiết khỏi `sk-sync` và sửa checkpoint example của `sk-executing-pro`.
- Thay broken link tới tài liệu audit đã bị xóa trong `sk-verify-pro` bằng contract mô tả ổn định.
- Giữ nguyên domain code examples trong fenced blocks và không đưa tooling mới vào repo.

## Kết luận

Nhóm 01–04 hiện dùng chung một metadata/routing contract tối thiểu và không còn repo/CLI execution guidance ngoài code examples trong phạm vi đã kiểm tra. Các khác biệt về body workflow vẫn được giữ theo domain; consistency được áp dụng ở các điểm routing, ownership, artifact boundary và verification có tính toàn cục.
