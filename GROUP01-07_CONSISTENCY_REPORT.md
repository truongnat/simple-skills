# Consistency audit — Nhóm 01–07

**Ngày:** 2026-09-29
**Phạm vi:** 162 skill thuộc Nhóm 01–07.

## Baseline

Consistency scan trước remediation cho thấy Nhóm 06–07 đã đạt contract mới, nhưng các nhóm legacy 01–05 còn thiếu nhiều section routing:

| Contract | Baseline issue |
|---|---:|
| Boundary thiếu | 35 skill |
| Required inputs thiếu | 70 skill |
| Cross-skill handoffs thiếu | 97 skill |
| Metadata routing rỗng | 0 skill |

Các gaps chủ yếu là khác biệt cấu trúc giữa skill legacy và các skill professional mới, không phải thiếu domain content.

## Remediation

- Bổ sung explicit `Boundary` cho skill chưa có ownership contract.
- Bổ sung `Required inputs` và assumption discipline cho các skill legacy.
- Bổ sung `Cross-skill handoffs` theo domain của từng nhóm:
  - Nhóm 01: lifecycle, BA/specification, review/verification.
  - Nhóm 02: architecture/API/backend, security, testing, deployment.
  - Nhóm 03: language/framework/domain implementation, debugging, testing.
  - Nhóm 04: AI/data/agent systems, evaluation, safety/privacy.
  - Nhóm 05: frontend/UI/UX, accessibility, testing, product handoff.
- Giữ nguyên nội dung domain và examples; chỉ bổ sung routing/contract metadata.

## Final verification

| Check | Result |
|---|---:|
| Skills kiểm tra | 162/162 |
| Contract errors | 0 |
| Empty tags/roles | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Repo-tooling hits ngoài fenced examples | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 01–07 hiện dùng cùng contract tối thiểu: metadata routing, ownership boundary, required inputs và specialist handoffs. Các skill cũ vẫn giữ domain guidance nhưng được định tuyến nhất quán với các skill professional đã chuẩn hóa.
