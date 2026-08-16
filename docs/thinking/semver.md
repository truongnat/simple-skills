# SemVer 2.0.0 convention

This project follows [Semantic Versioning 2.0.0](https://semver.org/) for
machine-readable config files.

## Versioned files

| File | Current | What it controls |
|------|---------|------------------|
| `artifact-schemas.json` | `2.0.0` | Required headings for session artifacts |
| `first-party-skills.json` | `1.0.0` | Skill inventory, step definitions, profiles |

## Rules

1. **MAJOR** — breaking change (removing required headings, renaming keys,
   changing validation logic). Bump when existing sessions would fail.
2. **MINOR** — backward-compatible addition (new optional heading, new skill
   entry). Old validators still work.
3. **PATCH** — fix or clarification (description typo, reordering entries).

## Validator enforcement

`validate_artifacts.py` reads the `version` field from `artifact-schemas.json`
and rejects schemas that don't meet `MIN_SCHEMA_VERSION`:

```
Schema version 1.0.0 is incompatible — validator requires >= 2.0.0
```

- Invalid SemVer strings (e.g. bare integers like `2`) → incompatible.
- Major version `0.x.y` → always accepted (initial development).
- Same or higher major version with `>= MIN_SCHEMA_VERSION` → accepted.

## When to bump

| Change | Bump |
|--------|------|
| Remove a required heading | MAJOR |
| Rename a key in `artifact-schemas.json` | MAJOR |
| Add a new artifact type | MINOR |
| Add an optional heading | MINOR |
| Add a new skill to inventory | MINOR |
| Fix a description or reorder entries | PATCH |
