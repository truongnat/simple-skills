# Changelog

All notable changes to **Simple Skills** are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.5.0] — 2025-08-18

### Added

- **Minimal install by design.** `sk install` now ships only the `init` skill
  plus tools, docs, settings, and the machine-readable `catalog.json` — no
  longer copies all 222 skills. `init` is the scaffold that builds the skill
  set for the project.
- **`catalog.json`** (built by `scripts/build_catalog.py`): 221 skills with
  full frontmatter metadata, raw GitHub URLs per skill, and 31 detect→skill
  `fits` groups. CI verifies the catalog is not stale.
- **`init` build-fit scaffold.** The init skill now asks which AI provider(s)
  you work on (`claude` / `cursor` / `codex` / `gemini`, multi-select) plus
  `enforce_one`, then asks "Build skills to fit this project?" — **Fit**
  (matches detected stack to catalog fits groups), **All**, or **Minimal** —
  and installs + compiles the chosen skills for your provider(s).
- **Provider compilation** (`tools/providers/`): compile the skill catalog for
  claude / cursor / codex / gemini layouts, exposed as `sk compile --provider X`
  and `sk install --provider X`.
- **Security policy** (`tools/policy/`): secret/PII redaction (`redact.py`),
  dangerous-shell-command guard (`denylist.py`), and budget/context hard-stop
  (`budget.py`). `session.sh commit` auto-redacts Work artifacts before the
  nested-git commit.
- **CLI commands** `sk status` (step ledger + session + git) and
  `sk validate` (schema-validate all SKILL.md files).
- **156 vendored skills from [aix](https://github.com/truongnat/aix)**
  (commit `26381fc`), bringing the catalog to 222 skills (66 first-party +
  156 vendored), all with `x-*` schema validation and plain-name aliases
  (e.g. `docker` → `docker-pro`).
- **`x-*` frontmatter schema validation** in `scripts/validate_skills.py`:
  `x-kind`, `x-version` (semver), `x-tags`, `x-compatible`, `aliases` —
  including block-style YAML lists.
- **Extended install profiles** with aix domain skills: `ba` 42, `frontend`
  65, `backend` 97, `all` 222.
- **Version-consistency guard** (`scripts/check_version.py`) + CI gate that
  fails a release when the git tag does not match `pyproject.toml`.
- **`LICENSE` (MIT)** added.

### Fixed

- **Version drift:** `v0.4.0` was released while `__version__` still reported
  `0.3.0`. Version is now single-sourced and CI-enforced.
- **aix doc drift:** `PROJECT_OVERVIEW.md` claimed Neo4j/Redis/Meili — the
  knowledge base is SQLite (`node:sqlite`); `doctor.ts` said "Neo4j".
- **aix SSH-key redaction regex** never matched `RSA PRIVATE KEY` PEM headers;
  the port now handles all common PEM variants.

## [0.4.0] — 2025-08-07

- SemVer 2.0.0 validation, slim artifacts, readability lint, simplified CLI
  (install / update / doctor), configurable Work layer location.

## [0.3.0]

- CLI simplification groundwork (install, update, doctor with `--agent`).

## [0.2.0]

- Initial PyPI release: installer CLI (`sk`), skills, profiles, session tools.
