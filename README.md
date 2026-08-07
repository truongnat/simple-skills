<h1 align="center">Simple Skills</h1>

<div align="center">
<pre>
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ____  _                 _         ____  _    _ _       ║
║  / ___|(_)_ __ ___  _ __ | | ___   / ___|| | _(_) |___   ║
║  \___ \| | '_ ` _ \| '_ \| |/ _ \  \___ \| |/ / | / __|  ║
║   ___) | | | | | | | |_) | |  __/   ___) |   <| | \__ \  ║
║  |____/|_|_| |_| |_| .__/|_|\___|  |____/|_|\_\_|_|___/  ║
║                     |_|                                  ║
║                                                          ║
║     think → design → plan → execute → review → done      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
</pre>
</div>

<p align="center">
  <a href="https://github.com/truongnat/simple-skills/actions/workflows/ci.yml"><img src="https://github.com/truongnat/simple-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  &nbsp;
  <a href="https://pypi.org/project/simple-skills/"><img src="https://img.shields.io/pypi/v/simple-skills.svg?style=flat&label=PyPI&color=10a37f" alt="PyPI"></a>
  &nbsp;
  <img src="https://img.shields.io/badge/python-%3E%3D3.11-10a37f?style=flat&logo=python&logoColor=white" alt="Python >= 3.11">
  &nbsp;
  <a href="https://pypi.org/project/simple-skills/"><img src="https://img.shields.io/pypi/dm/simple-skills.svg?style=flat&color=667085" alt="Downloads"></a>
  &nbsp;
  <img src="https://img.shields.io/badge/license-MIT-0d0d0d?style=flat&labelColor=f7f7f8" alt="MIT">
  &nbsp;
  <img src="https://img.shields.io/badge/status-active-10a37f?style=flat&labelColor=0d0d0d" alt="Active">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CLI-sk-10a37f?style=for-the-badge&labelColor=0d0d0d" alt="CLI">
  <img src="https://img.shields.io/badge/skills-66%20skills-e7f6f1?style=for-the-badge&labelColor=0d0d0d&color=0f766e" alt="Skills">
  <img src="https://img.shields.io/badge/profiles-5%20profiles-f7f7f8?style=for-the-badge&labelColor=0d0d0d&color=10a37f" alt="Profiles">
  <img src="https://img.shields.io/badge/thinking-12%20methods-e7f6f1?style=for-the-badge&labelColor=0d0d0d&color=0f766e" alt="Thinking">
</p>

<p align="center">
  <b>Agent kit for work that ships</b><br>
  <code>think → design → plan → execute → review → done</code>
</p>

<p align="center">
  <a href="#what-is-this">What</a> ·
  <a href="#install">Install</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#profiles">Profiles</a> ·
  <a href="#mental-model">Model</a> ·
  <a href="#thinking-methods">Thinking</a> ·
  <a href="docs/guides/START_HERE.md">Start here</a>
</p>

---

## What is this?

**Simple Skills** is an agent kit that gives AI coding assistants structured workflows for real work. Instead of vague prompts, you get:

- **66 skills** across 5 profiles (core, office, BA, frontend, backend)
- **12 thinking methods** for better decision-making
- **Session management** with automatic git integration
- **Artifact validation** to ensure quality
- **Smart install** that handles conflicts gracefully

Perfect for teams who want AI assistance that actually ships.

---

## Install

The easiest way to install and manage Simple Skills across **all operating systems** (macOS, Linux, Windows) is using `pipx` or `uv`.

### 1. Install the global CLI tool
```bash
pipx install simple-skills
# or: uv tool install simple-skills
```

### 2. Install skills into your project
Navigate to your project directory and run:
```bash
cd your-project
sk install
```
*(Note: Use `sk install --agent claude` to install into `.claude` instead of the default `.agents` directory).*

### Available Commands
```bash
# Install everything (replaces existing directory)
sk install

# Update your skills from upstream (keeps your custom skills safe)
sk update

# Check if your project has all required configuration and docs
sk doctor
```

<details>
<summary><b>Fallback: Install without Python/pipx</b></summary>

If you don't have Python or pipx, you can download and run the installer script directly:

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/install.sh -o install.sh
bash install.sh install
```

**Windows:**
```powershell
iwr -useb https://raw.githubusercontent.com/truongnat/simple-skills/main/install.ps1 -OutFile install.ps1
.\install.ps1 install
```
</details>

---

## Quick start

After installation, run the **`init`** skill once to set up your project:

```bash
# In your AI assistant, say:
"Use the init skill to set up this project"
```

Then choose your path based on the task:

| Task size | When to use | Flow |
| :-- | :-- | :-- |
| **Quick** | Tiny clear fix | `quick-fix` → execution → review → done |
| **Lite** | Small feature | brainstorming → planning → sync → execute → review |
| **Full** | Unclear / multi-surface | Full lifecycle · business-analysis · design |

Lite/Full paths use **Step ledger** (track each workflow step) and **Spec quality** (validate artifacts before moving on) to ensure nothing falls through the cracks.

Check progress anytime:

```bash
bash .agents/tools/session/session.sh status
```

---

## CLI reference

The `sk` CLI is beautifully simple:

```bash
# Install everything into the default .agents folder
sk install

# Install for a specific agent provider (e.g. into .claude)
sk install --agent claude

# Update your skills from upstream (keeps your custom skills safe)
sk update --agent claude

# Check if your project has all required configuration and docs
sk doctor --agent claude
```

That's it. No complicated flags needed.

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

| | Path | Purpose |
| :-- | :-- | :-- |
| **Kit** | `.agents/` | Installer-owned: skills, tools, policy, thinking methods |
| **Work** | `.agent-work/` | Your session truth: tasks, memory, artifacts (auto-gitignored) |
| **CLI** | `sk` | Commands: `install`, `doctor`, `uninstall` |

**Key principle:** Progress lives in `TASKS.md` + `session.sh status`. Artifacts only under sessions. Blocking changes require confirmation.

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

These are session-wide principles, **not** report section titles. They guide every decision:

```text
Outcome-first → IPO → Make-explicit → SSOT → Small-batch → Feedback loop
→ Default path first → Reversible → Standardize → Handoff → Evidence
→ Bottleneck → (5W1H) → Vital few
```

**How to use:** Fold these into `Goal` / `Verify` / `Handoff` sections. No separate `OUTCOME.md` or `HANDOFF.md` files needed.

Full details: [docs/thinking/README.md](docs/thinking/README.md)

---



## HTML · Docs · Develop

<p align="center">
  <img src="https://img.shields.io/badge/HTML-light%20only-10a37f?style=flat&labelColor=0d0d0d" alt="HTML">
  <img src="https://img.shields.io/badge/classes-.ss--*-667085?style=flat&labelColor=0d0d0d" alt="ss">
  <img src="https://img.shields.io/badge/theme-DESIGN__SYSTEM-e7f6f1?style=flat&labelColor=0f766e" alt="theme">
</p>

- **Design system:** [DESIGN_SYSTEM.md](docs/conventions/DESIGN_SYSTEM.md) · seed `VISUAL_DECISION.template.html`
- **Docs map:** [docs/README.md](docs/README.md)
- **Getting started:** [START_HERE.md](docs/guides/START_HERE.md)
- **What's next:** [WHAT_NEXT.md](docs/guides/WHAT_NEXT.md)

### Development setup

```bash
pip install -e ".[dev]"
python scripts/validate_skills.py && pytest -q
```

---

<p align="center">
  <b>Python ≥ 3.11 · MIT License</b><br>
  <a href="https://github.com/truongnat/simple-skills">github.com/truongnat/simple-skills</a>
</p>
