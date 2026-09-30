# Audit & remediation Group 02 — Kiến trúc, API & backend

**Phạm vi:** 18 skill trong taxonomy Group 02 của `simple-skills`.
**Ngày:** 2026-09-29
**Nguyên tắc:** chỉ thay đổi nội dung/resource thuộc `skills/`; không đưa `docs/`, `tools/`, `tests/` hoặc report vào commit/push.

## 1. Kết luận

Group 02 có nền tảng tốt ở các skill `*-pro`, nhưng trước remediation có ba vấn đề hệ thống:

1. **Boundary và routing không đồng nhất:** các skill legacy (API principles, architecture patterns, microservices patterns, Node backend) cạnh tranh phạm vi với các canonical `*-pro` skill.
2. **Metadata không đầy đủ:** 5 skill legacy thiếu `sk-kind`, `sk-version`, `sk-compatible`; tags/roles còn rỗng hoặc không có.
3. **Nội dung/code mẫu hỏng:** token `••••`, `__sk-init__`, `__post_sk-init__`, lệnh `adr sk-init`, và lệnh Python trỏ tới script không tồn tại trong 2 senior skill.

## 2. Gaps theo severity

### P0 — Đã sửa

- **Ví dụ Python không chạy được:** `__sk-init__` và `__post_sk-init__` xuất hiện trong các reference của architecture/microservices/API; đã chuẩn hóa thành `__init__` và `__post_init__`.
- **Thông tin chuẩn bị bị hỏng:** `RFC ••••` trong WebSocket và các benchmark `••••×` trong system design; đã thay bằng RFC 6455 và các tỷ lệ có ý nghĩa.
- **CORS template không an toàn:** wildcard origins/hosts trong `rest-api-template.py`; đã đổi thành domain placeholder cụ thể và giữ credentials tắt mặc định.

### P1 — Đã sửa

- **Canonical ownership:** xác lập owner cho API contract, clean architecture, microservices, system design và NestJS trong các skill `*-pro`.
- **Legacy facade routing:** thêm Boundary để route từ baseline skill sang canonical owner, giảm overlap và tránh chọn nhầm skill.
- **Script references sai:** senior architect/backend dùng tên file Python/snake_case không tồn tại; đã khớp với các script JavaScript/kebab-case thật trong thư mục `scripts/`.

### P2 — Đã sửa

- Chuẩn hóa `sk-tags`, `sk-roles`, `sk-kind`, `sk-version`, `sk-compatible` cho toàn bộ 18 skill.
- Sửa fullstack description/title bị token placeholder, giữ rõ stack Next.js/TypeScript hiện có.
- Sửa lệnh ADR thành `adr init docs/adr`.

## 3. Canonical routing sau remediation

```text
API principles ───────┐
GraphQL ──────────────┼──> sk-api-design-pro (contract owner)
NestJS / Node backend ┘

Architecture patterns / Clean Architecture ──> sk-clean-code-architecture-pro
Microservices patterns ──────────────────────> sk-microservices-pro
Senior Architect / System Design baseline ──> sk-system-design-pro
NestJS + Neo4j ──────────────────────────────> sk-nestjs-pro + graph specialization
ADR records ─────────────────────────────────> record lifecycle after design decision
```

## 4. Verification

- Metadata, semver, local links, malformed-token scan và canonical-owner scan: **PASS (18 skills)**.
- JavaScript scripts của `sk-senior-architect` và `sk-senior-backend`: `node --check`: **PASS**.
- `git diff --check`: **PASS**.
- Thay đổi chỉ nằm trong `skills/`; các file local `GROUP02_AUDIT_REPORT.md`, `docs/`, `tools/`, `tests/` không thuộc commit Group 02.

## 5. Remaining follow-up

- Các skill legacy `sk-senior-architect` và `sk-senior-backend` vẫn chứa toolkit rộng; nên tách thành facade + chuyên môn canonical ở đợt refactor lớn hơn nếu muốn giảm kích thước context.
- Nên thêm CI validator riêng cho Group 02 ở cấp repo nếu sau này repo muốn enforce metadata/broken-link/code-token guardrails tự động; hiện validator được chạy inline để không đưa tooling ngoài `skills/` vào commit.

## 6. Skill-only cleanup — 2026-09-29

Theo yêu cầu cập nhật, Group 02 không còn hướng dẫn thực thi command/tooling:

- Loại các section Quick Start, Development Workflow, Common Commands và Automation khỏi `sk-senior-architect`, `sk-senior-backend` và ADR skill.
- Xóa bundled `scripts/` của hai senior skill vì không còn thuộc scope skill-only.
- Xóa bytecode `__pycache__` phát sinh từ asset template.
- Giữ lại reference/checklist/code examples có giá trị hướng dẫn; chúng không được trình bày như lệnh cần chạy.
