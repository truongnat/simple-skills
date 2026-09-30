# Audit & remediation — Nhóm 06: Security, testing & reliability

**Ngày:** 2026-09-29
**Phạm vi:** 20 skill trong taxonomy Nhóm 06.

## Baseline findings

Trước remediation, 14/20 skill có `sk-tags` rỗng và 14/20 có `sk-roles` rỗng. Scanner cũng phát hiện 31 metadata field thiếu trên nhóm, chủ yếu ở các skill legacy như auth implementation, debugging, tracing, E2E, SAST, senior security, Solidity security và STRIDE. Một số skill professional đã có boundary tốt nhưng thiếu section routing chuẩn `Required inputs` hoặc `Cross-skill handoffs`. `sk-nextjs-security-scan` thiếu description frontmatter và có boundary trống.

## Remediation đã triển khai

- Chuẩn hóa metadata cho cả 20 skill: `description`, `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`; giữ lại tags/roles chuyên biệt đã tồn tại khi có.
- Bổ sung description trigger-oriented cho `sk-nextjs-security-scan`.
- Bổ sung hoặc hoàn thiện boundary cho 10 skill legacy/specialist.
- Chuẩn hóa `When not to use`, `Required inputs` và `Cross-skill handoffs` cho các skill còn thiếu.
- Làm rõ canonical routing giữa:
  - `sk-security-pro` với API/auth/Next.js/SAST/security review.
  - `sk-testing-pro` với TDD, E2E, debugging và regression verification.
  - `sk-bug-discovery-pro` với systematic debugging và debugging investigation.
  - `sk-performance-tuning-pro` với distributed tracing và reliability diagnosis.
- Giữ nguyên code examples và reference assets domain; không thêm repo tooling hoặc script thực thi.

## Verification

| Check | Result |
|---|---:|
| Skills kiểm tra | 20/20 |
| Contract errors | 0 |
| Empty routing metadata | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Repo/CLI execution patterns ngoài code examples | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 06 hiện có cùng contract routing với các nhóm đã remediation trước: metadata đủ để định tuyến, ownership rõ, input boundary được nêu, handoff giữa security/testing/debugging/performance được ghi lại và output có thể kiểm chứng. Các ví dụ kỹ thuật trong fenced blocks được giữ lại để không làm mất giá trị domain.
