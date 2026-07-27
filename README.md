# Simple Skills

Agent kit for shipping work with structure: **think → design → plan → execute → review → done**.

Install once into a project. Agents get skills, shared policy, session tools, and
session-wide Thinking methods — without inventing ceremony per chat.

| | |
| --- | --- |
| **CLI** | `sk` (`pipx install simple-skills`) |
| **Kit** | `.agents/` — skills, tools, settings, policy (installer-owned) |
| **Work** | `.agent-work/` — sessions + memory (nested git; auto-gitignored) |
| **Repo** | [truongnat/simple-skills](https://github.com/truongnat/simple-skills) |

**Start:** [docs/guides/START_HERE.md](docs/guides/START_HERE.md) ·
**Route a task:** [docs/guides/WHAT_NEXT.md](docs/guides/WHAT_NEXT.md) ·
**Docs map:** [docs/README.md](docs/README.md)

---

## Install

```bash
pipx install simple-skills    # once
cd your-project && sk install
sk doctor
```

Also: `uv tool install simple-skills`.

| Profile | Adds |
| --- | --- |
| `core` (default) | Lifecycle + shared policy |
| `office` | Office file skills |
| `ba` | BA / specify / wireframe pack |
| `frontend` / `backend` / `all` | Domain skill sets |

```bash
sk install --profile ba
sk uninstall --yes            # keeps .agent-work/; add --purge-work to delete
```

Until PyPI (or for a fork):

```bash
pipx install git+https://github.com/truongnat/simple-skills.git
# or: curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/i | bash
```

Reinstall merges kit files and **keeps** `.agents/settings.yaml`. After install,
run skill **`init`** once.

---

## Mental model

```text
┌─────────────────────────────────────────────────────────┐
│  Kit (.agents/)          installer-owned, shared rules  │
│  skills · tools · policy · thinking · DESIGN_SYSTEM     │
└────────────────────────────┬────────────────────────────┘
                             │ agents read
┌────────────────────────────▼────────────────────────────┐
│  Work (.agent-work/)     per-task truth + durable memory│
│  sessions/<Task-…>/ · memory/ · nested git via session.sh│
└─────────────────────────────────────────────────────────┘
```

- **Progress truth** = `TASKS.md` + `session.sh status` (no `OVERVIEW.md`).
- **Artifacts** live only under `.agent-work/sessions/…`, never under `.agents/`.
- **Confirm-first** on Blocking gaps: stop → Ask method → then finish the doc.

---

## Paths (pick the smallest that fits)

| Path | When | Flow |
| --- | --- | --- |
| **Quick** | Tiny clear fix (≈1–3 cards) | `quick-fix` → execution → review → done |
| **Lite** | Small feature, mostly clear | Short brainstorming → planning → sync → … |
| **Full** | Unclear / multi-surface | Full lifecycle (+ BA/design as needed) |

Stuck? Say the situation out loud and open [WHAT_NEXT.md](docs/guides/WHAT_NEXT.md).

```bash
bash .agents/tools/session/session.sh help
bash .agents/tools/session/session.sh status
python .agents/tools/session/validate_artifacts.py
python .agents/tools/session/lint_artifacts.py
```

---

## Thinking methods

Session-wide ways of working — **not** report section titles. Ops live in
`.agents/SKILL_PREAMBLE.md`; normative detail in `.agents/thinking/`
([source index](docs/thinking/README.md)).

```text
Outcome-first → IPO → Make-explicit → SSOT → Small-batch → Feedback loop
→ Default path first → Reversible decisions → Standardize before automate
→ Design for handoff → Evidence over confidence → Optimize bottleneck
→ (5W1H if unclear) → Vital few
```

Fold results into real fields (`Goal`, `Verify`, `Handoff`, …). Do not create
method-branded files (`OUTCOME.md`, `HANDOFF.md`, …).

---

## HTML decisions

Visual Ask method (`html`) uses the enterprise **light-only** theme:

- Classes: `.ss-*` per [DESIGN_SYSTEM.md](docs/conventions/DESIGN_SYSTEM.md)
- Template: `skills/brainstorming/templates/VISUAL_DECISION.template.html`
- Serve to record choices: `python .agents/tools/session-serve/serve.py <session>`

No `dark:` utilities; use `ss-btn` / `ss-input` / `ss-check` — not bare native
controls.

---

## Docs layout (source → install)

Source under `docs/`; install **flattens** most files into `.agents/` (Thinking
stays nested).

| Folder | Role |
| --- | --- |
| [guides/](docs/guides/) | Start, routing, migration, BA aliases |
| [policy/](docs/policy/) | Preamble, full policy, Kit vs Work |
| [thinking/](docs/thinking/) | Thinking methods (normative) |
| [conventions/](docs/conventions/) | Code comments, design system, third-party |
| [config/](docs/config/) | settings, schemas, install profiles |
| [examples/](docs/examples/) | Good/bad session shapes |
| [AGENTS.md](docs/AGENTS.md) | Host entrypoint → project root |

Settings you might edit: `language` · `rules.code.comments.prose_language` ·
`rules.branch.mode` · `rules.reports.output_format` · `rules.docs.*`  
Defaults: [AGENT_POLICY.md](docs/policy/AGENT_POLICY.md).

---

## Develop

```bash
pip install -e ".[dev]"
python scripts/validate_skills.py
pytest -q
sk --help
```

Python ≥ 3.11. Optional office extras: `pip install -e ".[office]"`.

---

## Publish (maintainers)

PyPI name: **`simple-skills`** (`v0.2.0`). Trusted Publisher once:

1. PyPI → pending publisher for `simple-skills`, repo `truongnat/simple-skills`,
   workflow `publish.yml`, environment `pypi`
2. GitHub Environment `pypi`
3. Release tag `v0.2.0` → workflow publishes the wheel

Users then: `pipx install simple-skills` → `sk install`.

---

## License

MIT — see `pyproject.toml`.
