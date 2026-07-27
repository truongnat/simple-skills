# Simple Skills

<p align="center">
  <img src="docs/assets/banner.svg" alt="Simple Skills — Agent kit that ships" width="100%">
</p>

<p align="center">
  <a href="https://github.com/truongnat/simple-skills/actions/workflows/ci.yml"><img src="https://github.com/truongnat/simple-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  &nbsp;
  <a href="https://pypi.org/project/simple-skills/"><img src="https://img.shields.io/pypi/v/simple-skills.svg?style=flat&label=PyPI&color=10a37f" alt="PyPI"></a>
  &nbsp;
  <a href="https://pypi.org/project/simple-skills/"><img src="https://img.shields.io/pypi/pyversions/simple-skills.svg?style=flat" alt="Python"></a>
  &nbsp;
  <a href="https://pypi.org/project/simple-skills/"><img src="https://img.shields.io/pypi/dm/simple-skills.svg?style=flat&color=667085" alt="Downloads"></a>
  &nbsp;
  <img src="https://img.shields.io/badge/license-MIT-0d0d0d?style=flat&labelColor=f7f7f8" alt="MIT">
  &nbsp;
  <img src="https://img.shields.io/badge/status-active-10a37f?style=flat&labelColor=0d0d0d" alt="Active">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CLI-sk-10a37f?style=for-the-badge&labelColor=0d0d0d" alt="CLI">
  <img src="https://img.shields.io/badge/install-pipx%20%2B%20sk%20install-e7f6f1?style=for-the-badge&labelColor=0d0d0d&color=0f766e" alt="Install">
  <img src="https://img.shields.io/badge/paths-Quick%20·%20Lite%20·%20Full-f7f7f8?style=for-the-badge&labelColor=0d0d0d&color=10a37f" alt="Paths">
  <img src="https://img.shields.io/badge/thinking-12%20methods-e7f6f1?style=for-the-badge&labelColor=0d0d0d&color=0f766e" alt="Thinking">
  <img src="https://img.shields.io/badge/HTML-light%20only%20·%20.ss--*-ffffff?style=for-the-badge&labelColor=0d0d0d&color=667085" alt="HTML">
</p>

<p align="center">
  <b>Agent kit for work that ships</b><br>
  <code>think → design → plan → execute → review → done</code>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#mental-model">Model</a> ·
  <a href="#paths">Paths</a> ·
  <a href="#thinking-methods">Thinking</a> ·
  <a href="docs/guides/START_HERE.md">Start here</a> ·
  <a href="docs/guides/WHAT_NEXT.md">What next</a>
</p>

---

## Install

```bash
pipx install simple-skills
cd your-project && sk install
sk doctor
```

Also: `uv tool install simple-skills`.

| Profile | What you get |
| :-- | :-- |
| **`core`** (default) | Lifecycle skills + shared policy |
| `office` | Office file skills |
| `ba` | BA / specify / wireframe pack |
| `frontend` · `backend` · `all` | Domain skill sets |

```bash
sk install --profile ba
sk uninstall --yes
```

<details>
<summary><b>From git / curl</b></summary>

```bash
pipx install git+https://github.com/truongnat/simple-skills.git
curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/i | bash
```

</details>

Reinstall keeps `.agents/settings.yaml`. Then run skill **`init`** once.

---

## Mental model

<p align="center">
  <img src="https://img.shields.io/badge/.agents-Kit%20(installer)--0d0d0d?style=for-the-badge&labelColor=10a37f&color=0d0d0d" alt="Kit">
  <img src="https://img.shields.io/badge/-→-f7f7f8?style=for-the-badge&labelColor=f7f7f8&color=f7f7f8" alt="to">
  <img src="https://img.shields.io/badge/.agent--work-Work%20(sessions%20%2B%20memory)--0d0d0d?style=for-the-badge&labelColor=667085&color=0d0d0d" alt="Work">
</p>

```mermaid
flowchart LR
  K["Kit · .agents/"] --> W["Work · .agent-work/"]
  K --- S[skills · tools · policy · thinking]
  W --- T[sessions · memory · nested git]
```

| | Path | Owns |
| :-- | :-- | :-- |
| **Kit** | `.agents/` | Installer-owned rules & skills |
| **Work** | `.agent-work/` | Session truth (auto-gitignored) |
| **CLI** | `sk` | install · doctor · uninstall |

Progress = `TASKS.md` + `session.sh status`. Artifacts only under sessions. Blocking → **Confirm-first**.

---

## Paths

<p align="center">
  <img src="https://img.shields.io/badge/Quick-tiny%20fix-10a37f?style=for-the-badge&labelColor=0d0d0d" alt="Quick">
  <img src="https://img.shields.io/badge/Lite-small%20feature-0f766e?style=for-the-badge&labelColor=0d0d0d" alt="Lite">
  <img src="https://img.shields.io/badge/Full-unclear%20%2F%20multi--surface-667085?style=for-the-badge&labelColor=0d0d0d" alt="Full">
</p>

| | When | Flow |
| :-- | :-- | :-- |
| **Quick** | Tiny clear fix | `quick-fix` → execution → review → done |
| **Lite** | Small feature | brainstorming → planning → sync → … |
| **Full** | Unclear / multi-surface | Full lifecycle · `business-analysis` · design |

Lite/Full use **Step ledger** + **Spec quality** (not Quick).

```bash
bash .agents/tools/session/session.sh status
python .agents/tools/session/validate_artifacts.py
```

---

## Thinking methods

<p align="center">
  <img src="https://img.shields.io/badge/1-Outcome--first-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="1">
  <img src="https://img.shields.io/badge/2-IPO-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="2">
  <img src="https://img.shields.io/badge/3-Make--explicit-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="3">
  <img src="https://img.shields.io/badge/4-SSOT-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="4">
  <img src="https://img.shields.io/badge/5-Small--batch-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="5">
  <img src="https://img.shields.io/badge/6-Feedback-e7f6f1?style=flat-square&labelColor=10a37f&color=e7f6f1" alt="6">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/7-Default%20path-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="7">
  <img src="https://img.shields.io/badge/8-Reversible-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="8">
  <img src="https://img.shields.io/badge/9-Standardize-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="9">
  <img src="https://img.shields.io/badge/10-Handoff-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="10">
  <img src="https://img.shields.io/badge/11-Evidence-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="11">
  <img src="https://img.shields.io/badge/12-Bottleneck-f7f7f8?style=flat-square&labelColor=0d0d0d&color=f7f7f8" alt="12">
</p>

Session-wide — **not** report titles. Detail: [docs/thinking/README.md](docs/thinking/README.md)

```text
Outcome-first → IPO → Make-explicit → SSOT → Small-batch → Feedback loop
→ Default path first → Reversible → Standardize → Handoff → Evidence
→ Bottleneck → (5W1H) → Vital few
```

Fold into `Goal` / `Verify` / `Handoff`. No `OUTCOME.md` / `HANDOFF.md`.

---

## HTML · Docs · Develop

<p align="center">
  <img src="https://img.shields.io/badge/HTML-light%20only-10a37f?style=flat&labelColor=0d0d0d" alt="HTML">
  <img src="https://img.shields.io/badge/classes-.ss--*-667085?style=flat&labelColor=0d0d0d" alt="ss">
  <img src="https://img.shields.io/badge/theme-DESIGN__SYSTEM-e7f6f1?style=flat&labelColor=0f766e" alt="theme">
</p>

- Theme: [DESIGN_SYSTEM.md](docs/conventions/DESIGN_SYSTEM.md) · seed `VISUAL_DECISION.template.html`
- Docs map: [docs/README.md](docs/README.md)
- Start: [START_HERE.md](docs/guides/START_HERE.md)

```bash
pip install -e ".[dev]"
python scripts/validate_skills.py && pytest -q
```

Python ≥ 3.11 · MIT · [truongnat/simple-skills](https://github.com/truongnat/simple-skills)
