# Session-artifacts contract

This skill stores generated workflow artifacts under `artifacts/<task-id>/` in the current project workspace. Create the directory only when an artifact is required.

## Rules

- Use a stable task id such as `task-001-slug`; do not use an opaque hidden runtime path.
- Keep source evidence, decisions, status, and handoff artifacts in the same task directory.
- Name artifacts exactly as the calling skill specifies (`REVIEW.md`, `VERIFY.md`, `DISCUSSION.md`, or a debug note).
- Never claim completion while a required artifact is missing, stale, or unverified.
- If the workspace is read-only, report the intended path and continue with an explicit blocked status.
