# Audit & remediation — Nhóm 10: Git, tooling, platform & meta-skills

**Ngày:** 2026-09-29
**Phạm vi:** 26 skill trong taxonomy Nhóm 10.

## Baseline findings

- `sk-skills-self-review-pro` thiếu 5 metadata routing fields.
- 22 skill có `sk-tags` hoặc `sk-roles` rỗng.
- 7 skill thiếu explicit `Boundary`.
- 8 skill thiếu `Required inputs`.
- 20 skill thiếu `Cross-skill handoffs`.
- Không phát hiện repository-specific execution residue thuộc các pattern cần loại bỏ. Git/worktree/tooling vocabulary được giữ lại vì là domain content của chính Nhóm 10.

## Remediation đã triển khai

- Chuẩn hóa metadata cho toàn bộ 26 skill: `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`.
- Bổ sung tags/roles theo cluster: Git/repository, tooling/CLI, orchestration/routing, knowledge/memory, skill authoring và process/quality.
- Bổ sung ownership boundary cho các skill legacy:
  - code review và gatekeeper.
  - Git worktree isolation.
  - codebase mapping.
  - durable memory.
  - tool discovery.
  - harness/session usage.
  - TDD và AIX entry point.
- Bổ sung `When not to use`, `Required inputs` và `Cross-skill handoffs` cho các skill còn thiếu.
- Làm rõ canonical handoffs giữa `sk-git-operations-pro`, `sk-git-worktree-pro`, `sk-repo-tooling-pro`, `sk-using-harness`, `sk-router-pro`, `sk-gatekeeper` và các domain skills.
- Giữ lại Git/tooling commands chỉ khi chúng là domain examples; không thêm repo automation hoặc execution scripts.

## Verification toàn bộ repo

| Check | Result |
|---|---:|
| Nhóm 01–10 | 222/222 skills |
| Contract errors | 0 |
| Empty tags/roles | 0 |
| Broken local links | 0 |
| Unbalanced Markdown fences | 0 |
| Repository execution residue | 0 |
| `git diff --check` | PASS |

## Kết luận

Nhóm 10 đã dùng chung contract routing với Nhóm 01–09, đồng thời giữ đúng domain-specific nature của Git, tooling, platform và meta-skills. Toàn bộ 222 skill trong Nhóm 01–10 pass consistency scan.
