# Simple Skills

Skills + rules for AI agents: think → design → plan → execute → review → done.

- **Kit** `.agents/` — skills, tools, settings (installer)
- **Work** `.agent-work/` — sessions + memory (nested git; auto-gitignored)

Start with [docs/START_HERE.md](docs/START_HERE.md). Skill map: [docs/WHAT_NEXT.md](docs/WHAT_NEXT.md).

## Install

```bash
# Linux / macOS
curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/truongnat/simple-skills/main/install.ps1 | iex

# From clone
./install.sh --agents-mode replace
./install.sh --profile office          # core + office
./install.sh --profile all
```

Profiles: `core` (default) · `office` · `frontend` · `backend` · `all`  
Then run **`init`**. Reinstall keeps `settings.yaml`.

## After install

```bash
bash .agents/tools/session/session.sh help
bash .agents/tools/session/session.sh doctor
```

| Path | Skill |
| --- | --- |
| **Quick** (tiny fix) | `quick-fix` → sync → execution → review → done |
| **Lite** / **Full** | brainstorming → (business-analysis) → design → planning → … |

Step skills use a **Step ledger** and **Spec quality** gates (not on Quick).  
Lint: `python .agents/tools/session/lint_artifacts.py`  
Handoff pack: `python .agents/tools/session/build_context.py`

## Settings (keep small)

`language` · `rules.branch.mode` · `rules.reports.output_format` · `rules.docs.*`  
Defaults in `AGENT_POLICY.md`.

## Docs

| File | Role |
| --- | --- |
| [START_HERE](docs/START_HERE.md) | 2-minute start |
| [WHAT_NEXT](docs/WHAT_NEXT.md) | Situation → skill |
| [AGENTS](docs/AGENTS.md) | Entrypoint |
| [AGENT_POLICY](docs/AGENT_POLICY.md) | Full policy |
| [AGENT_WORK](docs/AGENT_WORK.md) | Kit vs Work + git ownership |
| [MIGRATION](docs/MIGRATION.md) | Host upgrade notes |
| [examples](docs/examples/README.md) | Good/bad session shapes |

## Dev checks

```bash
pip install -e ".[dev]"
python scripts/validate_skills.py
pytest -q
```
