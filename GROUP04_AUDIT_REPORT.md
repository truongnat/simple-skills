# Audit & remediation — Nhóm 04: Data, AI & agent systems

**Ngày:** 2026-09-29
**Phạm vi:** 17 skills trong `SKILL_GROUPING_REPORT.md`.

## Phạm vi đã kiểm tra

- Metadata frontmatter: `name`, `description`, `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`.
- Boundary, when-to-use, required inputs, output contract và cross-skill handoff.
- Overlap giữa agent orchestration, LLM integration, prompt engineering, evaluation, RAG, data science, ML và MLOps.
- Local Markdown links, fenced-code balance và command/tooling remnants ngoài code examples.
- Reference/resource layout của các skill reference-heavy.

## Findings trước remediation

| Severity | Finding | Affected scope |
|---|---|---|
| High | `sk-gemini-api-dev` thiếu `description` bắt buộc trong frontmatter. | 1 skill |
| High | Gemini workflow đánh số sai, có SDK install command và boundary rỗng. | 1 skill |
| Medium | Description metadata của AI integration và Stream RTC bị truncate/khó routing. | 2 skills |
| Medium | Sáu skill nền tảng thiếu `When not to use`, `Required inputs` và handoff contract. | AI agents, data engineering, data science, fullstack RAG, ML, MLOps |
| Medium | `sk-tags` và `sk-roles` rỗng trên toàn nhóm, làm giảm khả năng routing. | 17 skills |
| Low | Một số skill generated có contract ngắn và overlap chưa được ghi rõ. | Các skill nền tảng |

## Remediation đã triển khai

- Chuẩn hóa tags/roles có ý nghĩa cho toàn bộ 17 skill.
- Sửa/hoàn thiện description frontmatter cho Gemini, AI integration và Stream RTC.
- Bổ sung Gemini boundary, required inputs, when-not-to-use, cross-skill handoffs và workflow numbering.
- Loại SDK install command khỏi Gemini, chuyển thành guidance về dependency declaration.
- Bổ sung routing/input/handoff contracts cho sáu skill nền tảng.
- Ghi rõ ownership giữa `sk-ai-integration-pro`, `sk-ai-agents-pro`, `sk-a2a-protocol-pro`, `sk-agent-evaluation-pro`, `sk-fullstack-rag-pro`, `sk-data-science-pro`, `sk-data-engineering-pro`, `sk-machine-learning-pro` và `sk-mlops-pro`.
- Giữ code examples domain trong fenced blocks; không thêm command execution mới.

## Verification

- Skills kiểm tra: **17/17**.
- Frontmatter errors: **0**.
- Execution references ngoài code fences: **0**.
- Stale patterns (`npm install`, `Install SDK`, `xcopy`, `rsync`, `git sk-*`, `scripts/`): **0**.
- Local links: **164**, broken links: **0**.
- Unbalanced Markdown fences: **0**.
- `git diff --check`: **PASS**.
- Thay đổi giới hạn trong `skills/`: **17 `SKILL.md` files**.
