# Audit & remediation — các nhóm skill còn lại

**Ngày:** 2026-09-29
**Phạm vi:** 171 skill ngoài Nhóm 01 và Nhóm 02.

## Kết quả audit ban đầu

| Hạng mục | Kết quả |
|---|---:|
| Skills được quét | 171 |
| Command/tool references trong `SKILL.md` | 184 |
| Bundled paths được phát hiện | 49 |
| Nhóm có nhiều command nhất | deploy, CI/CD, Docker/Kubernetes, CLI, document helpers, security scan |

## Chính sách áp dụng

Áp dụng chế độ **skill guidance-only**: loại repo/tool execution instructions, command snippets dùng để chạy workflow, và hướng dẫn invocation cụ thể; giữ code/config examples trong code fences khi chúng là kiến thức domain, cùng bundled assets phục vụ trực tiếp cho domain như PDF/DOCX/XLSX, accessibility, security scanning, motion và office processing.

## Remediation

- Xóa fenced `bash`/`sh`/`shell` khỏi 171 `SKILL.md` khi chúng chỉ là lệnh thực thi.
- Loại các inline command và command-first workflow cho Git, package manager, Docker/Kubernetes, cloud CLI, deployment, repo tooling và skill validation.
- Chuyển Quick Start/Development Workflow/Commands thành orientation hoặc workflow guidance không phụ thuộc invocation.
- Viết lại deploy workflow thành pre-check, rollout strategy, verification evidence, rollback reasoning và anti-pattern guidance.
- Giữ code examples domain trong fenced TypeScript/JavaScript/Python/TSX/YAML khi chúng giải thích behavior hoặc output, không phải lệnh shell.
- Không xóa bundled domain assets; chúng vẫn là tài nguyên của skill, không phải instruction bắt agent chạy lệnh repo.

## Verification sau remediation

- **Skills quét:** 171.
- **Execution references ngoài code fences:** 0.
- **Domain command examples trong non-shell code fences:** được giữ theo chính sách guidance-only.
- **Markdown fences:** cân bằng toàn repo.
- **`git diff --check`:** pass.
- **File `SKILL.md` đã cải thiện:** 74.
- **Bundled domain assets:** giữ nguyên có chủ đích.

## Ghi chú

Các skill có bản chất domain/tool integration vẫn mô tả concepts, APIs, configuration shape và examples cần thiết; chúng không còn yêu cầu agent thực thi command cụ thể trong `SKILL.md`.
