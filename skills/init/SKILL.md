---
name: init
description: >-
  Initializes or refreshes project knowledge for all other skills. Use first
  when entering a project, when .agents/PRJ_REFERENCE.md is missing or stale,
  or when the user asks to force-regenerate project context and rules. Stops
  to ask the user configuration questions (language, branch mode, report
  format, etc.) before scanning — never auto-fills settings silently.
---

# Project Init

## Shared preamble (do this first)

Read and follow `.agents/SKILL_PREAMBLE.md` now (Language + Work layout +
Memory + Thinking methods + **Readable writing**) before Purpose, Contract, or
steps. Do not skip it; do not reuse a cached `language`. Write so a teammate
understands on first pass — concrete paths/IDs, no filler, no method branding.
Artifacts go under `.agent-work/` (sessions + memory), not `.agents/`.
Source copy: `docs/policy/SKILL_PREAMBLE.md` / `docs/policy/AGENT_WORK.md`.

## Purpose

Build a reliable project reference before other lifecycle skills run. Collect
facts from the repository, record sources and confidence, and configure
project-specific behavior without inventing conventions.

## Contract (mandatory)

| Field | Requirement |
|---|---|
| Inputs | Repository root, existing `.agents/settings.yaml` and `.agents/PRJ_REFERENCE.md` when present, source/config/docs/tests, git metadata, **user-confirmed settings from the configuration dialog**. |
| Outputs | `.agents/PRJ_REFERENCE.md` and a merged `.agents/settings.yaml`. |
| Safety | Read-only discovery. Never read or record secret values. Never execute **project** code, install dependencies, or mutate source files. Running the bundled read-only `scripts/scan_workspaces.sh` (filesystem sweep only) is allowed. Preserve existing user settings unless explicitly replaced. Mark uncertain facts; do not invent business or workflow rules. |

### Required artifacts

#### `.agents/PRJ_REFERENCE.md`

- Required: yes.
- **executive_summary**: The most useful 20% of project context.
- **project_identity**: Purpose, users, domain, lifecycle status.
- **workspaces**: For a monorepo, one row per app/package/service with its
  path, type, and its **own** stack, entry point, and commands. Never collapse
  a multi-stack monorepo into a single root stack.
- **agent_clis**: Table from `detect_agents.py --write` (CLI id, status, path,
  auth probe) — never store tokens.
- **tech_stack**: Languages, frameworks, runtime, package/build tools. In a
  monorepo, record the stack **per workspace** (see `workspaces`), not only the
  root manifest.
- **architecture**: Components, boundaries, entry points, data flows.
- **business_rules**: Rule, source, affected area, confidence.
- **key_constraints**: Technical, business, compliance, compatibility.
- **commands**: Setup, build, test, lint, run, migration commands.
- **conventions**: Code, branch, commit, PR, reporting, decision-gate, and visual conventions.
- **security_notes**: Security boundaries and handling rules, without secrets.
- **references**: Authoritative file/path/URL references.
- **unknowns**: Missing or conflicting information requiring confirmation.
- **freshness**: Generated/updated time, source commit, mode.

#### `.agents/settings.yaml`

- Required: yes; merge in place. Keep the file **lean** (language,
  rules.code.comments.prose_language, branch, reports.output_format, docs,
  optional commit/PR).
- Preserve `language`, `rules.code.comments.prose_language`, and any
  user-authored values.
- Populate only repository-evidenced or user-confirmed project rules under the
  knobs above — do **not** dump decision/visual/report-style/code-comment
  matrices into settings (those defaults live in `AGENT_POLICY.md`).
- Do not copy descriptive project facts here; link to
  `.agents/PRJ_REFERENCE.md`.

## Modes

| Mode | Use | Behavior |
|---|---|---|
| `init` | Reference is missing | Create from the template. |
| `refresh` | Existing reference may be stale | Update changed facts and preserve confirmed content. |
| `force` | User explicitly requests regeneration | Re-scan all sources and rebuild the reference; merge settings without silently resetting user choices. |

## Configuration dialog (mandatory — STOP and ask)

After selecting the mode (step 2) and **before** scanning the repository (step 3),
**STOP and open a dialog** to collect settings from the user. Do not guess or
auto-fill these values silently — the user must confirm or choose.

### How to ask

1. **Read existing `.agents/settings.yaml`** (if any) to pre-fill defaults.
2. **Present each question** using the `choice` Ask method (from
   `SKILL_PREAMBLE.md` → Confirm-first). Show the current/default value first
   so the user can just confirm to skip.
3. **Wait for the user's answer** before proceeding. Do not continue the
   workflow until all questions are answered.
4. **Record answers** and use them when writing `settings.yaml` (step 8) and
   `PRJ_REFERENCE.md` (step 7).

### Questions to ask

| # | Setting | Ask method | Default (if no existing value) |
|---|---------|-----------|-------------------------------|
| 1 | `language` — prose language for all artifacts | `choice`: `en` / `vi` | `en` |
| 2 | `rules.branch.mode` — branching strategy | `choice`: `checkout` (safer) / `direct` | `checkout` |
| 3 | `rules.branch.base` — base branch name | `fact` (text) | auto-detect from git |
| 4 | `rules.reports.output_format` — report format | `choice`: `markdown` / `html` | `markdown` |
| 5 | `rules.docs.enabled` — enable wiki/docs skill | `confirm` (Yes/No) | `true` |
| 6 | `rules.code.comments.prose_language` — code comment language | `choice`: `repo-default` / `en` / `vi` | `repo-default` |

### Dialog rules

- **One round, up to 6 questions.** Present all questions in a single message
  (numbered). The user answers all at once or one by one — either is fine.
- **Show defaults clearly.** Format each question so the user can reply with
  just a number/letter or type a custom value. Example:

  ```
  Configure project settings (press Enter / reply "default" to accept defaults):

  1. Language (en | vi) [en]:
  2. Branch mode (checkout | direct) [checkout]:
  3. Base branch name [auto-detect]:
  4. Report format (markdown | html) [markdown]:
  5. Enable docs/wiki skill (yes | no) [yes]:
  6. Code comment language (repo-default | en | vi) [repo-default]:
  ```

- **Existing values win.** If `settings.yaml` already has a value, show it as
  the default. The user can keep it or change it.
- **Skip in `refresh` mode when user says so.** If the user invokes `refresh`
  and says "keep current settings", skip the dialog entirely.
- **Never invent values.** If the user does not answer a question, use the
  default — do not guess.

## Workflow (step by step)

1. Read `.agents/settings.yaml` and existing project reference, if any.
2. Select mode: `init`, `refresh`, or explicit `force`.
3. **Configuration dialog (STOP → ask → wait → record).** See above.
4. Inventory repository facts using read-only inspection:
   - git root, remotes (redact credentials), branches, default/base branch;
   - manifests, lockfiles, build/test/lint configs, CI, containers, migrations;
   - source layout, entry points, public interfaces, tests, documentation;
   - business rules and constraints evidenced by docs, tests, schemas, or code.
5. **Deep workspace scan (mandatory — do not scan only the root, and do not
   enumerate from the workspace config).** The scan has two responsibilities,
   split so that no stack is ever missed:

   **a. Coverage (deterministic) — run the bundled candidate surfacer.** It
   sweeps the **filesystem** (not the workspace config) and prints every
   plausible project-root directory, pruned of build/generated/platform noise:

   ```bash
   bash .agents/skills/init/scripts/scan_workspaces.sh
   ```

   Each row is `DIR<TAB>MARKER_HINTS`. The hints (e.g. `pubspec.yaml`,
   `package.json`, or `-` for none) are only clues; the script deliberately does
   **not** classify the stack.

   **b. Classification (yours) — you decide each stack.** For **every** row,
   open the directory and identify its stack from its actual manifest/tooling
   using your own knowledge — **any** ecosystem counts (Node/TS, Flutter/Dart,
   Go, Rust, Python, JVM, Kotlin, Swift, .NET, PHP, Ruby, Elixir, Deno, Zig, …).
   Do not limit yourself to a fixed list; a directory whose hint is `-` still
   gets inspected and classified.
   - **Record every candidate** in the `workspaces` table and give each its own
     `tech_stack`, entry point, and per-app commands. A directory of a different
     ecosystem is a distinct stack that MUST appear.
   - **Why the config is not enough:** a `pnpm-workspace.yaml` / `turbo.json` /
     root `package.json "workspaces"` lists only JS/TS members. A Flutter/Dart,
     Go, Rust, or Python app under `apps/` is typically **not** listed there, so
     enumerating from the config silently drops whole stacks. Filesystem
     coverage is the source of truth; the config is only supporting evidence.
   - The surfacer's hint list is best-effort, not exhaustive. If you know of a
     project directory it did not surface (unusual layout or ecosystem), add it
     — never treat the script's rows as the complete universe of stacks.
   - If the script cannot run (e.g. no Bash), fall back to a manual recursive
     directory sweep that prunes `node_modules`, build/generated, and native
     platform dirs, and classify every project root yourself — never bound the
     sweep by the workspace config.
6. **Agent CLI inventory (read-only):** detect installed worker CLIs (no secrets):

   ```bash
   python .agents/tools/session/detect_agents.py --write
   ```

   Upserts `## Agent CLIs` in `PRJ_REFERENCE.md`. Status values:
   `available` / `auth_unknown` / `missing`. Optional lean knobs:
   `rules.agents.routing` / `fallback` in settings (commented skeleton).
7. Classify every important statement:
   - `confirmed`: direct source or user confirmation;
   - `inferred`: evidence exists but is indirect;
   - `unknown`: unresolved or conflicting.
8. Seed from `templates/PRJ_REFERENCE.template.md`, fill all applicable
   sections, and keep source references close to each fact.
9. Merge confirmed project conventions into `.agents/settings.yaml`.
   Preserve `language`, security hard rules, and custom user values.
10. Validate:
    - no secret values or sensitive file contents;
    - executive summary appears first and is decision-oriented;
    - commands are sourced, not guessed;
    - every workspace member with its own manifest has its own stack recorded
      (no multi-stack monorepo collapsed to a single root stack);
    - unknowns and conflicts are visible.
11. Report created/updated files and the highest-priority unknowns.

## Discovery boundaries

Do not open `.env`, credential stores, private keys, production dumps, or
secret-manager payloads. File names may be listed when needed; values must
never be read or copied.

## Handoff

All subsequent skills must read `.agents/settings.yaml` and
`.agents/PRJ_REFERENCE.md` before making project-specific decisions. If the
reference is missing or materially stale, run this skill first.
