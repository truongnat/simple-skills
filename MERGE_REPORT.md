# aix × simple-skills — Merge Report (simple-skills as the base)

> **Goal:** merge `truongnat/aix` into `truongnat/simple-skills`, **following
> simple-skills' architecture**: Python-first, `sk` CLI, `skills/` layout, profiles,
> zero-dependency installer, pytest, `docs/` map.
>
> aix contributes its **158 domain skills**, its **Zod-style skill schema**, its
> **security policy** (redaction + shell denylist), and its **multi-provider
> compilation** — all re-implemented in Python, not imported as a TypeScript monorepo.
>
> **Date:** 2025-08-17 · **Method:** direct source audit of both repos.

---

## 1. Executive summary

simple-skills is the base and keeps its identity: repo layout, CLI, installer, session
tooling, profiles, docs. aix is **folded in** as a content + ideas donor, with its
TypeScript packages **not** carried into the core (they were the platform layer we're
*not* adopting — the host agent is the runtime, per aix's own README).

**Result:** one Python repo with 222 Zod-validated skills, 5+ installable profiles,
provider compilation (claude/cursor/codex/gemini), secret redaction, step-ledger
sessions, and Windows/macOS/Linux one-command install — all under the `sk` CLI.

```
simple-skills (merged)
├── sk                    CLI (src/simple_skills/) — install/update/doctor/status/validate
├── install.sh / install.ps1 / install.cmd
├── skills/               222 skills (66 ss + 156 aix, deduped)
├── src/simple_skills/    Python CLI
├── tools/
│   ├── session/          step ledger + artifact validation + git   (ss, kept)
│   ├── policy/           NEW: secret/PII redaction + shell denylist (port of @x/policy)
│   ├── providers/        NEW: compile skills per provider          (port of @x/providers)
│   ├── decision-server/ choice-reader/ ba_report/ session-serve/ video-keyframes/
├── scripts/              validate_skills.py (extended schema), resolve_install_profile.py
├── docs/                 config (profiles.json …), guides, policy, thinking, conventions
├── tests/                pytest (14 ss + new)
└── LICENSE               ADD (MIT)
```

---

## 2. What each side contributes (framed for a simple-skills base)

### simple-skills (base — everything stays)
- **Architecture:** Python ≥3.11, zero runtime deps, `sk` CLI, hatchling build, PyPI package
- **Skills:** 66 lifecycle / BA / office / frontend / backend skills with step files
- **Workflow:** step ledger, `TASKS.md` + `PLAN.md`, spec-quality gates, session status, nested git
- **Install:** `install.sh` / `install.ps1` / `install.cmd`, conflict modes, profiles, `sk doctor`
- **Docs & tests:** `docs/` map (guides/policy/thinking/conventions), 14 pytest files, CI validates skills + runs tests

### aix (folded in)
| Asset | How it's adopted |
|---|---|
| 158 domain skills | Copied into `skills/`, migrated to simple-skills SKILL.md format **+ aix-style schema keys** |
| Skill schema (Zod) | Ported to `scripts/validate_skills.py` as a Python validator (`x-kind`, `x-version`, `x-tags`, `x-compatible`) |
| Multi-provider adapters | Ported to `tools/providers/` (Python) — compile/install skills for claude/cursor/codex/gemini |
| `@x/policy` (redaction, shell denylist) | Ported to `tools/policy/` (Python), wired into session tools |
| Budget hard-stop | Ported as a small `tools/policy/budget.py` guard for paid provider calls |
| Headless LangGraph engine | **NOT adopted** — conflicts with "host agent is the runtime". Optional `sk run` later |
| `services/kb-server` (NestJS+SQLite) | **NOT adopted** — Python tools write markdown sessions; KB is out of scope for now |
| `.aix/sessions` | Adopted as an alias under `.agent-work/` (session dir naming) |

---

## 3. Compatibility & dedupe

### 3.1 Skill overlap

Exact-name overlap: **0**. Near-duplicates (2):

| simple-skills | aix | Action |
|---|---|---|
| `planning` (step-ledger workflow) | `planning-pro` (spine phase 2) | Keep both; `planning-pro` references `planning` for the ledger |
| `business-analysis` (ss) | `business-analysis-pro` (aix) | Keep both (ss = step workflow, aix = domain depth); cross-link in frontmatter |

→ **222 unique skills** (66 + 156). No renames: aix's `-pro` names stay intact so
their internal cross-references ("combine with `ci-cd-pro`") keep working.

### 3.2 Skill format (follow simple-skills, extended)

simple-skills SKILL.md today:
```yaml
---
name: planning
description: >-
  Step workflow: …
---
```

Merged format (ss base + optional aix keys, all validated):
```yaml
---
name: docker-pro
description: >-
  …
x-kind: domain            # new, optional — process | domain | reference
x-version: 0.1.0          # new, optional — semver
x-tags: [docker, containers]      # new, optional
x-compatible: [claude, cursor, codex, gemini]   # new, optional
aliases: [docker]         # new, optional — maps plain names → -pro skills
---
```

`validate_skills.py` is extended to enforce: name pattern, description length,
`x-version` semver, valid `x-kind`, valid `x-compatible` providers, `aliases`
uniqueness. (This is the aiх Zod schema, ported to Python.)

### 3.3 Structural decisions

| Conflict | Resolution (follow simple-skills) |
|---|---|
| Two CLIs (`sk` vs `aix`) | **Keep `sk` only.** `aix` command not shipped |
| Two session dirs | Keep `.agent-work/`; accept `.aix/sessions` as a legacy alias for imported projects |
| Two skill dirs (`skills/` vs `content/skills/`) | **`skills/` only** (ss layout) |
| TS packages (13) | Dropped from core; only Python ports (tools/policy, tools/providers) are kept |
| Version drift (v0.4.0 tag reports 0.3.0) | Single-source from `pyproject.toml` via `importlib.metadata`; CI tag==version gate |
| License | Add `LICENSE` (MIT) |
| Tests | **pytest only** (ss runner); aix's 7 node tests are ported to pytest where they cover ported logic |
| Docs | Keep `docs/` map; aix root md files move under `docs/` |

---

## 4. Target architecture (simple-skills layout)

```
skills/
  66 ss skills (kept as-is) + 156 aix skills (migrated frontmatter)
  _shared/               session-artifacts-contract.md + step-ledger-contract.md
src/simple_skills/
  cli.py                 install / update / doctor / status / validate
  __init__.py            __version__ ← importlib.metadata (single source)
tools/
  policy/                redact.py, denylist.py, budget.py   (port of @x/policy)
  providers/             compile.py, adapters/{claude,cursor,codex,gemini}.py
  session/               session.sh, build_context, lint_artifacts, validate_artifacts
  decision-server/ choice-reader/ ba_report/ session-serve/ video-keyframes/
scripts/
  validate_skills.py     extended: full schema (name/x-kind/x-version/x-tags/x-compatible/aliases)
  resolve_install_profile.py   handles 222 skills across 5+ profiles
docs/config/
  install-profiles.json  extended: core/office/ba/frontend/backend + aix domains
  artifact-schemas.json  extended for new session artifacts
tests/                   test_validate_skills_schema.py, test_policy.py, test_providers.py, …
LICENSE                  MIT (added)
```

---

## 5. Phased roadmap

### Phase 0 — Hygiene (~half a day)
- [ ] Add `LICENSE` (MIT)
- [ ] Fix version drift: `__version__` from `pyproject.toml`; CI check `git tag == pyproject version`
- [ ] Port aix `PROJECT_OVERVIEW.md` corrections into `docs/` (kill Neo4j claims — it's SQLite)

### Phase 1 — Content merge (biggest value, ~2–3 days)
- [ ] Copy 156 aix skill dirs → `skills/` (skip `-pro` workflow skills already covered by ss)
- [ ] Write migration script: add `x-kind`/`x-version`/`x-tags`/`x-compatible` to each SKILL.md frontmatter
- [ ] Extend `validate_skills.py` with the full schema; run over all 222; fix failures
- [ ] Extend `docs/config/install-profiles.json`: add aix domains to backend (`nestjs-pro`, `postgresql-pro`, …), frontend (`react-pro`, `nextjs-pro`, …), ba (`business-analysis-pro`), all (222)
- [ ] Add `aliases` for ss plain names that map to `-pro` skills

### Phase 2 — Policy & providers (~3–4 days)
- [ ] `tools/policy/redact.py` — redact secrets/PII from session logs + artifacts (port of `@x/policy`)
- [ ] `tools/policy/denylist.py` — block dangerous shell commands in session tools
- [ ] `tools/policy/budget.py` — hard-stop guard for paid provider calls (port of aix budget tracker)
- [ ] `tools/providers/` — compile/install skills for claude/cursor/codex/gemini (port of `@x/providers`); wire into `sk install --provider <name>`

### Phase 3 — CLI & session (~2 days)
- [ ] `sk status` — expose step ledger + session + git (from `session.sh status`)
- [ ] `sk validate` — CLI wrapper for the extended `validate_skills.py`
- [ ] Spec-quality gates inside session tools (validate artifacts before advancing steps)

### Phase 4 — Tests, CI, docs, release (~2 days)
- [ ] pytest suites for schema validation, policy, providers
- [ ] CI: `validate_skills.py` over 222 + `pytest -q` + profile resolution + coverage floor
- [ ] Update `docs/` map + README (222 skills, 5+ profiles, provider install)
- [ ] Release 0.5.0: PyPI + changelog; note aix as the content source

---

## 6. Product after merge (`sk` CLI)

```bash
sk install                      # core profile (17 skills)
sk install --profile ba         # BA profile, now with aix BA depth
sk install --profile all        # all 222 skills
sk install --profile backend --provider cursor   # compile for Cursor
sk install --conflict-mode rename
sk update                       # update own skills without deleting custom ones
sk status                       # step ledger + session + git
sk validate                     # validate all 222 SKILL.md against the schema
sk doctor                       # env + config health
```

**Value vs. either repo alone:**

| Capability | aix alone | ss alone | Merged (ss base) |
|---|---|---|---|
| Skills | 158 domain | 66 lifecycle/office | **222, schema-validated** |
| Runtime | Node monorepo | Python, zero deps | **Python, zero deps** |
| Install | pnpm+node | any OS + conflict modes | **any OS + profiles + conflicts** |
| Provider compilation | TS adapters | none | **Python adapters (4 providers)** |
| Security | policy + budget | none | **policy + budget (Python)** |
| Workflow | spine phases | step ledger + gates | **ledger + gates (ss wins)** |
| Tests | 7 node tests | 14 pytest | **pytest, both suites** |
| Publishing | not ready | PyPI (drift bug fixed) | **PyPI, single-source version** |

---

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| 222 skills in one `skills/` dir feels big | Profiles + `x-tags` + `sk skills list/show` + progressive disclosure |
| Dropping TS packages loses headless engine + kb-server | Document as out-of-scope; keep `tools/session` markdown sessions; optional `sk run` later |
| aix skill cross-references break on rename | **No renames** — keep `-pro` names; `aliases` handle plain-name lookups |
| Migration script corrupts frontmatter | Validate each file after rewrite (`validate_skills.py`), git-diff reviewable |
| Existing ss users lose nothing | All ss skills/docs/tools stay in place; new content is additive |
| Provider compile quality | Port aix adapter logic faithfully; test each provider output in CI |

---

## 8. Recommendation

**Merge into simple-skills now, in this order:** Phase 0 (hygiene) → Phase 1 (content)
→ Phase 2 (policy/providers) → Phase 3 (CLI/session) → Phase 4 (release).

The content merge (Phase 1) delivers most of the value and is pure addition —
reversible, low-risk. Phases 2–3 are Python ports of aix's best ideas, keeping the
zero-dependency, host-agent-is-runtime philosophy. The merged repo stays
**simple-skills** in name and architecture, with aix as its largest content donor.
