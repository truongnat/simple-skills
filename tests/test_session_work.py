from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SESSION_SH = REPO_ROOT / "tools" / "session" / "session.sh"


def test_session_new_uses_agent_work_and_nested_git(tmp_path: Path) -> None:
    (tmp_path / ".agents").mkdir()
    result = subprocess.run(
        ["bash", str(SESSION_SH), "new", "demo-feature"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    rel = result.stdout.strip()
    assert rel.startswith(".agent-work/sessions/Task-1-demo-feature")
    assert (tmp_path / rel).is_dir()
    assert (tmp_path / ".agent-work" / "memory").is_dir()
    assert (tmp_path / ".agent-work" / ".git").is_dir()
    assert (tmp_path / ".agent-work" / "sessions" / ".current").read_text(
        encoding="utf-8"
    ).strip() == rel

    current = subprocess.run(
        ["bash", str(SESSION_SH), "current"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    assert current.stdout.strip() == rel

    work_root = subprocess.run(
        ["bash", str(SESSION_SH), "work-root"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    assert work_root.stdout.strip() == ".agent-work"
