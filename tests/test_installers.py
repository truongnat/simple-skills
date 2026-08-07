from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]

# Flat docs: installer copies basename into .agents/.
INSTALLER_FLAT_DOCS = (
    "AGENTS.md",
    "conventions/DESIGN_SYSTEM.md",
    "conventions/CODE_COMMENTS.md",
    "conventions/THIRD_PARTY_SKILLS.md",
    "policy/SKILL_PREAMBLE.md",
    "policy/AGENT_POLICY.md",
    "policy/AGENT_WORK.md",
    "guides/START_HERE.md",
    "guides/WHAT_NEXT.md",
    "guides/MIGRATION.md",
    "guides/BA_SKILLS.md",
    "config/settings.yaml",
    "config/artifact-schemas.json",
    "config/gitignore.agent-work.snippet",
)

# Thinking methods: installer copies docs/thinking/ as a directory.
INSTALLER_THINKING = (
    "outcome-first.md",
    "input-process-output.md",
    "make-implicit-explicit.md",
    "single-source-of-truth.md",
    "small-batch.md",
    "feedback-loop.md",
    "default-path-first.md",
    "reversible-decisions.md",
    "standardize-before-automate.md",
    "design-for-handoff.md",
    "evidence-over-confidence.md",
    "optimize-bottleneck.md",
    "README.md",
)

# Back-compat for any helper that expects the combined list.
INSTALLER_DOCS = INSTALLER_FLAT_DOCS + tuple(
    f"thinking/{name}" for name in INSTALLER_THINKING
)


def make_source(tmp_path: Path) -> Path:
    shutil.copy2(REPO_ROOT / "install.sh", tmp_path / "install.sh")
    scripts = tmp_path / "scripts"
    scripts.mkdir(exist_ok=True)
    shutil.copy2(
        REPO_ROOT / "scripts" / "resolve_install_profile.py",
        scripts / "resolve_install_profile.py",
    )
    docs = tmp_path / "docs"
    guides = docs / "guides"
    policy = docs / "policy"
    thinking = docs / "thinking"
    conventions = docs / "conventions"
    config = docs / "config"
    for d in (guides, policy, thinking, conventions, config):
        d.mkdir(parents=True, exist_ok=True)

    (docs / "AGENTS.md").write_text("installed rules\n", encoding="utf-8")
    (conventions / "DESIGN_SYSTEM.md").write_text("design\n", encoding="utf-8")
    (conventions / "CODE_COMMENTS.md").write_text("comments\n", encoding="utf-8")
    (conventions / "THIRD_PARTY_SKILLS.md").write_text(
        "licenses\n`expo-native-ui`\nopenai.yaml\n",
        encoding="utf-8",
    )
    (policy / "SKILL_PREAMBLE.md").write_text("preamble\n", encoding="utf-8")
    (policy / "AGENT_POLICY.md").write_text("policy\n", encoding="utf-8")
    (policy / "AGENT_WORK.md").write_text("work layout\n", encoding="utf-8")
    (thinking / "outcome-first.md").write_text("outcome-first\n", encoding="utf-8")
    (thinking / "input-process-output.md").write_text("ipo\n", encoding="utf-8")
    (thinking / "make-implicit-explicit.md").write_text("explicit\n", encoding="utf-8")
    (thinking / "single-source-of-truth.md").write_text("ssot\n", encoding="utf-8")
    (thinking / "small-batch.md").write_text("small-batch\n", encoding="utf-8")
    (thinking / "feedback-loop.md").write_text("feedback-loop\n", encoding="utf-8")
    (thinking / "default-path-first.md").write_text("default-path-first\n", encoding="utf-8")
    (thinking / "reversible-decisions.md").write_text("reversible-decisions\n", encoding="utf-8")
    (thinking / "standardize-before-automate.md").write_text(
        "standardize-before-automate\n", encoding="utf-8"
    )
    (thinking / "design-for-handoff.md").write_text("design-for-handoff\n", encoding="utf-8")
    (thinking / "evidence-over-confidence.md").write_text(
        "evidence-over-confidence\n", encoding="utf-8"
    )
    (thinking / "optimize-bottleneck.md").write_text("optimize-bottleneck\n", encoding="utf-8")
    (thinking / "README.md").write_text("thinking index\n", encoding="utf-8")
    (guides / "START_HERE.md").write_text("start\n", encoding="utf-8")
    (guides / "WHAT_NEXT.md").write_text("what next\n", encoding="utf-8")
    (guides / "MIGRATION.md").write_text("migration\n", encoding="utf-8")
    (guides / "BA_SKILLS.md").write_text("ba skills map\n", encoding="utf-8")
    (config / "gitignore.agent-work.snippet").write_text(
        "# snippet\n.agent-work/\n", encoding="utf-8"
    )
    (config / "artifact-schemas.json").write_text(
        '{"version":1,"artifacts":{}}\n', encoding="utf-8"
    )
    (config / "settings.yaml").write_text("language: en\n", encoding="utf-8")
    (config / "install-profiles.json").write_text(
        """
{
  "version": 1,
  "default": "all",
  "profiles": {
    "core": {"skills": ["init", "planning", "execution"]},
    "office": {"includes": ["core"], "skills": ["xlsx"]},
    "frontend": {"includes": ["core"], "skills": ["web-component-design"]},
    "all": {"all_skills": true}
  }
}
""".strip()
        + "\n",
        encoding="utf-8",
    )
    tools = tmp_path / "tools"
    tools.mkdir()
    (tools / "README.md").write_text("tools\n", encoding="utf-8")
    decision_server = tools / "decision-server"
    decision_server.mkdir()
    (decision_server / "server.py").write_text("# decision server\n", encoding="utf-8")
    (decision_server / "client.js").write_text("// client\n", encoding="utf-8")
    (decision_server / "animate.js").write_text("// animate\n", encoding="utf-8")
    (decision_server / "styles.css").write_text("/* styles */\n", encoding="utf-8")
    (decision_server / "tailwind-theme.js").write_text("tailwind.config = {};\n", encoding="utf-8")
    (decision_server / "README.md").write_text("decision server\n", encoding="utf-8")
    choice_reader = tools / "choice-reader"
    choice_reader.mkdir()
    (choice_reader / "read.py").write_text("# choice reader\n", encoding="utf-8")
    session_serve = tools / "session-serve"
    session_serve.mkdir()
    (session_serve / "serve.py").write_text("# session serve\n", encoding="utf-8")
    video_keyframes = tools / "video-keyframes"
    video_keyframes.mkdir()
    (video_keyframes / "extract.py").write_text("# video keyframes\n", encoding="utf-8")
    session = tools / "session"
    session.mkdir()
    (session / "session.sh").write_text(
        "#!/usr/bin/env bash\ncase \"$1\" in doctor) echo DOCTOR_OK; exit 0;; *) exit 0;; esac\n",
        encoding="utf-8",
    )
    (session / "session.sh").chmod(0o755)
    for stub in (
        "validate_artifacts.py",
        "lint_artifacts.py",
        "build_context.py",
    ):
        (session / stub).write_text(f"# {stub}\n", encoding="utf-8")
    # Minimal skill set covering core + one third-party for profile pruning tests.
    for skill in ("planning", "execution", "init", "xlsx", "web-component-design"):
        root = tmp_path / "skills" / skill
        root.mkdir(parents=True)
        (root / "SKILL.md").write_text(f"# {skill}\n", encoding="utf-8")
    return tmp_path


def run_installer(
    root: Path,
    mode: str,
    profile: str = "all",
    purge_unselected: bool = False,
) -> subprocess.CompletedProcess[str]:
    argv = ["bash", "install.sh", "--agents-mode", mode, "--profile", profile]
    if purge_unselected:
        argv.append("--purge-unselected")
    return subprocess.run(
        argv,
        cwd=root,
        stdin=subprocess.DEVNULL,
        text=True,
        capture_output=True,
        check=True,
    )


