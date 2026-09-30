# Skill authoring checklist

## Metadata

- [ ] `name` matches the directory name and uses kebab-case.
- [ ] `description` states scope, use cases, and trigger keywords.
- [ ] `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, and `sk-compatible` are present and non-empty where required.

## Contract

- [ ] Boundary states ownership and exclusions.
- [ ] When-to-use and when-not-to-use signals are concrete.
- [ ] Required inputs and assumptions are explicit.
- [ ] Cross-skill handoffs identify adjacent owners.

## Content

- [ ] Workflow is actionable without hidden repository assumptions.
- [ ] Deep material is in focused `references/` files.
- [ ] Examples are adapted to the domain; no placeholder content remains.
- [ ] SKILL.md stays below the repository line limit.

## Verification

- [ ] Frontmatter parses as YAML.
- [ ] Local links and bundled resource paths resolve.
- [ ] Markdown fences are balanced.
- [ ] No secrets, conflict markers, or accidental machine paths are present.
