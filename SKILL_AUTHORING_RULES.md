# Skill authoring rules

Use these rules when creating or updating a skill in this repository.

1. Keep each skill self-contained under `skills/sk-<name>/`.
2. Use valid YAML frontmatter; `name` must match the directory.
3. Write a precise description with scope, use cases, and trigger keywords.
4. Include routing metadata: `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, and `sk-compatible`.
5. State the boundary, activation signals, exclusions, required inputs, workflow, verification, and cross-skill handoffs.
6. Keep `SKILL.md` concise; move deep material into focused `references/` files.
7. Keep templates and reusable output assets under the owning skill directory.
8. Resolve local links and bundled resource paths before marking the skill complete.
9. Do not include secrets, machine-specific paths, merge markers, or unverified claims.
10. Record assumptions and route adjacent concerns to their canonical specialist skill.
