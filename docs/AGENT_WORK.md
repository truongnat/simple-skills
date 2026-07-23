# Agent Work layout

Simple Skills splits **Kit** and **Work** so installer files never share a
version history with feature artifacts.

## Kit — `.agents/`

Owned by the installer (`install.sh` / `install.ps1`):

- `skills/`, `tools/`
- `settings.yaml`, `SKILL_PREAMBLE.md`, `AGENT_POLICY.md`
- `DESIGN_SYSTEM.md`, `CODE_COMMENTS.md`, `THIRD_PARTY_SKILLS.md`
- optional `wiki/` (docs skill; location from `rules.docs`)

Reinstall may mirror/replace kit files. Do **not** put task artifacts here.

## Work — `.agent-work/`

Owned by the feature / team. Contains **sessions + memory together** (one
context when implementing a feature). Installer appends `.agent-work/` to the
host `.gitignore` so Work stays out of the product root history.

Progress lives in `TASKS.md` (cards include **Dev context** with `[Source:]`
cites). There is no separate `OVERVIEW.md`. Before execution, `sync` records
**Implementation readiness** `PASS` | `CONCERNS` | `FAIL`.

```text
.agent-work/
├── .git/                 # nested git (created by session.sh)
├── README.md
├── sessions/
│   ├── .current          # pointer to active Task-N-…
│   └── Task-N-<slug>/    # fixed artifact templates for one task
└── memory/
    ├── INDEX.md
    └── Task-N-<slug>.md  # durable lessons (vital few)
```

### Why a sibling folder (not inside `.agents`)?

Skills/tools are kit and change on reinstall. Sessions/memory are work and need
cheap checkout/diff over time. One nested git on `.agent-work` versions both
session and memory without bloating the product root git or colliding with the
installer.

### Host root `.gitignore` (required on install)

The installer appends (or creates) this entry in the **host project**
`.gitignore`:

```gitignore
.agent-work/
```

This kit repo also ignores `.agent-work/` in its own `.gitignore`. Work history
stays in the nested git under `.agent-work/`, not in the product root.

Track kit selectively if you want (for example commit `.agents/settings.yaml`
and `PRJ_REFERENCE.md`); leave Work out of the product history.

### Commands

```bash
bash .agents/tools/session/session.sh work-root   # ensure .agent-work + nested git
bash .agents/tools/session/session.sh new <slug>
bash .agents/tools/session/session.sh current
bash .agents/tools/session/session.sh status
```

Inside `.agent-work`, use normal git (`status`, `diff`, `log`, branches) to
compare artifact versions for the feature.
