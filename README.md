# Simple Skills

Skills + rules for AI agents: think → design → plan → execute → review → done.

- **Kit** `.agents/` — skills, tools, settings, policy (installer)
- **Work** `.agent-work/` — sessions + memory (nested git; `session.sh commit` / `archive`; auto-gitignored)

Start with [docs/guides/START_HERE.md](docs/guides/START_HERE.md). Skill map: [docs/guides/WHAT_NEXT.md](docs/guides/WHAT_NEXT.md). Docs catalog: [docs/README.md](docs/README.md).

## Install

```bash
pipx install simple-skills    # once (PyPI)
sk install                    # in your project
sk doctor
sk uninstall --yes
```

Also: `uv tool install simple-skills`.  
Profiles: `sk install --profile office` · `ba` · `frontend` · `backend` · `all` (default `core`).  
Then run **`init`**. Reinstall keeps `settings.yaml`.

Until the package is on PyPI (or for a fork):

```bash
pipx install git+https://github.com/truongnat/simple-skills.git
# or: curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/i | bash
```

## After install

```bash
sk doctor
bash .agents/tools/session/session.sh help
```

| Path | Skill |
| --- | --- |
| **Quick** (tiny fix) | `quick-fix` → sync → execution → review → done |
| **Lite** / **Full** | brainstorming → (business-analysis) → design → planning → … |

Step skills use a **Step ledger** and **Spec quality** gates (not on Quick).  
Lint: `python .agents/tools/session/lint_artifacts.py`  
Handoff pack: `python .agents/tools/session/build_context.py`

Session framing uses **Thinking methods** (Outcome-first → 5W1H if unclear → vital few). Ops in `.agents/SKILL_PREAMBLE.md`; Outcome-first detail in `.agents/thinking/outcome-first.md`.

## Settings (keep small)

`language` · `rules.code.comments.prose_language` · `rules.branch.mode` ·
`rules.reports.output_format` · `rules.docs.*`  
Defaults in [docs/policy/AGENT_POLICY.md](docs/policy/AGENT_POLICY.md).

## Docs layout

Source tree is classified; install flattens most files into `.agents/` (Thinking stays nested).

| Folder | Role | Installed |
| --- | --- | --- |
| [guides/](docs/guides/) | Start, routing, migration, BA aliases | `.agents/<file>` |
| [policy/](docs/policy/) | Preamble, full policy, Kit vs Work | `.agents/<file>` |
| [thinking/](docs/thinking/) | Thinking methods (Outcome-first, …) | `.agents/thinking/` |
| [conventions/](docs/conventions/) | Code comments, design system, third-party | `.agents/<file>` |
| [config/](docs/config/) | settings, schemas, install profiles | `.agents/settings.yaml`, tools schemas |
| [examples/](docs/examples/) | Good/bad session shapes | `.agents/examples/` |
| [AGENTS.md](docs/AGENTS.md) | Host entrypoint | project root `AGENTS.md` |

Full map: [docs/README.md](docs/README.md).

## Dev checks

```bash
pip install -e ".[dev]"
python scripts/validate_skills.py
pytest -q
sk --help
```

## Publish (maintainers)

Name on PyPI: **`simple-skills`** (available). After one Trusted Publisher setup:

1. https://pypi.org/manage/account/publishing/ → pending publisher for `simple-skills`, repo `truongnat/simple-skills`, workflow `publish.yml`, environment `pypi`
2. Create GitHub Environment `pypi` (optional protection rules)
3. GitHub → Release (tag `v0.2.0`) → workflow publishes the wheel

Then users only need `pipx install simple-skills` → `sk install`.
