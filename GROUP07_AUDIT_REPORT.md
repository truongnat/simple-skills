# Audit & remediation — Nhóm 07: Cloud, infrastructure & deployment

**Ngày:** 2026-09-29
**Phạm vi:** 17 skill trong taxonomy Nhóm 07.

## Baseline findings

Baseline scanner ghi nhận 15 metadata field thiếu trên nhóm, 14/17 skill có `sk-tags` rỗng và 14/17 có `sk-roles` rỗng. Ba skill legacy/specialist thiếu boundary rõ ràng: `sk-deployment-pipeline-design`, `sk-github-actions-templates` và `sk-hybrid-cloud-networking`. Nhiều skill professional đã có boundary nhưng thiếu section `Required inputs` hoặc `Cross-skill handoffs` theo contract chung.

Scanner phát hiện **một execution candidate duy nhất**:

- `sk-vps-devops-pro:133` — wording `rsync` trong ví dụ offsite backup.

## Phân loại execution candidate

Đây là domain guidance hợp lệ về chiến lược disaster recovery, không phải repo tooling hay bundled automation. Tuy nhiên, vì repository áp dụng policy guidance-only và yêu cầu không còn execution residue, wording đã được chuyển từ:

> `rsync or S3 copy`

sang:

> `replicated backup or object-storage copy`

Giữ nguyên ý nghĩa kiến trúc backup/offsite recovery nhưng loại tên công cụ thực thi cụ thể khỏi hướng dẫn.

## Remediation đã triển khai

- Chuẩn hóa metadata cho cả 17 skill: `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`; giữ lại metadata chuyên biệt đã có khi phù hợp.
- Bổ sung boundary và canonical ownership cho ba skill legacy/specialist.
- Bổ sung `Required inputs` và `Cross-skill handoffs` cho toàn bộ nhóm.
- Làm rõ handoff giữa:
  - `sk-ci-cd-pro` và `sk-deployment-pro`.
  - `sk-deployment-pipeline-design` và `sk-github-actions-templates`.
  - `sk-infrastructure-as-code-pro` và provider/platform skills.
  - `sk-network-infra-pro`, `sk-hybrid-cloud-networking` và `sk-security-pro`.
  - `sk-docker-pro`, `sk-kubernetes-pro` và deployment runtime.
- Giữ nguyên fenced domain examples, YAML/HCL/Dockerfile snippets và reference assets.
- Không thêm repo script, automation hoặc bundled tooling.

## Verification

| Check | Result |
|---|---:|
| Skills kiểm tra | 17/17 |
| Contract errors | 0 |
| Empty routing metadata | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Execution-pattern hits ngoài fenced examples | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 07 đã đạt guidance-only: execution candidate duy nhất đã được phân loại, wording tooling đã được loại bỏ, và toàn bộ skill có metadata/routing contract nhất quán. Domain examples vẫn được giữ lại vì chúng mô tả kiến trúc cloud/deployment thay vì yêu cầu agent thực thi lệnh.
