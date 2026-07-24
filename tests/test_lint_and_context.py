from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LINT = REPO_ROOT / "tools" / "session" / "lint_artifacts.py"
BUILD = REPO_ROOT / "tools" / "session" / "build_context.py"


def _session(tmp_path: Path) -> Path:
    session = tmp_path / ".agent-work" / "sessions" / "Task-1-demo"
    session.mkdir(parents=True)
    (tmp_path / ".agent-work" / "sessions" / ".current").write_text(
        ".agent-work/sessions/Task-1-demo\n", encoding="utf-8"
    )
    return session


def test_lint_ok_on_quick_tasks(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (session / "QUICK.md").write_text(
        "## Developer overview\n| Path | `Quick` |\n\n## Goal\nFix null.\n",
        encoding="utf-8",
    )
    (session / "TASKS.md").write_text(
        """# Tasks
### T-001: Guard null
- Status: todo
- Trace: src/a.ts
- Work items:
  - [ ] 1. return null
  - [ ] 2. test
- AC: returns null
- Verify: pnpm test
- Files/scope: src/a.ts
#### Dev context
- **Reuse:** helper `[Source: src/a.ts]`
- **Contracts / data:** No specific guidance found.
- **Constraints:** No specific guidance found.
- **Guardrails:** No specific guidance found.
- **Gaps:** none
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        ["python3", str(LINT), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SESSION_LINT_OK" in result.stdout


def test_lint_fails_quick_with_ba(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (session / "QUICK.md").write_text("Path: Quick\n", encoding="utf-8")
    (session / "BUSINESS_ANALYSIS.md").write_text("# BA\n", encoding="utf-8")
    result = subprocess.run(
        ["python3", str(LINT), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "Path=Quick forbids" in result.stdout


def test_lint_fails_translated_vietnamese_headings(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (tmp_path / ".agents").mkdir()
    (tmp_path / ".agents" / "settings.yaml").write_text("language: vi\n", encoding="utf-8")
    (session / "BASIC_DESIGN.md").write_text(
        "## Tóm tắt điều hành\n\n- hướng đi\n\n## Mục tiêu\n\nMột câu.\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        ["python3", str(LINT), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "heading must stay English" in result.stdout


def test_lint_warns_vi_settings_with_english_only_body(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (tmp_path / ".agents").mkdir()
    (tmp_path / ".agents" / "settings.yaml").write_text("language: vi\n", encoding="utf-8")
    (session / "DISCUSSION.md").write_text(
        "## Executive summary\n\n"
        + ("- The system should process every request correctly.\n" * 12)
        + "\n## Goal\n\nDeliver a robust architecture for the platform.\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        ["python3", str(LINT), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "SESSION_LINT_WARNINGS" in result.stdout
    assert "little Vietnamese prose" in result.stdout


def test_build_context_writes_file(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (session / "QUICK.md").write_text(
        "## Executive summary\n\n- fix null\n\n## Goal\n\nNull guard.\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        ["python3", str(BUILD), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert (session / "CONTEXT.md").is_file()
    assert "CONTEXT (compact" in (session / "CONTEXT.md").read_text(encoding="utf-8")


def test_build_context_pack_includes_rules_and_check(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (tmp_path / ".agents").mkdir()
    (session / "DISCUSSION.md").write_text(
        "## Executive summary\n\n- go\n\n## Goal\n\nShip.\n"
        "\n## Recommendation\n\nOption A.\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            "python3",
            str(BUILD),
            "--root",
            str(tmp_path),
            "--skill",
            "planning",
            "--pack",
            "--check",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    pack = (session / "CONTEXT_PACK.md").read_text(encoding="utf-8")
    assert "## Rules (mandatory)" in pack
    assert "Ask method" in pack
    assert ".agent-work/" in pack
    assert "CONTEXT_PACK_CHECK_OK" in result.stdout


def test_detect_agents_write_creates_section(tmp_path: Path) -> None:
    detect = REPO_ROOT / "tools" / "session" / "detect_agents.py"
    (tmp_path / ".agents").mkdir()
    result = subprocess.run(
        ["python3", str(detect), "--root", str(tmp_path), "--write"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    prj = tmp_path / ".agents" / "PRJ_REFERENCE.md"
    assert prj.is_file()
    assert "## Agent CLIs" in prj.read_text(encoding="utf-8")


def test_delegate_worker_rules_gate(tmp_path: Path) -> None:
    session = _session(tmp_path)
    (tmp_path / ".agents").mkdir()
    (session / "PLAN.md").write_text(
        "## Executive summary\n\n- plan\n\n## Goal\n\nDo it.\n",
        encoding="utf-8",
    )
    delegate = REPO_ROOT / "tools" / "session" / "delegate_worker.py"
    result = subprocess.run(
        [
            "python3",
            str(delegate),
            "--root",
            str(tmp_path),
            "--skill",
            "planning",
            "--cli",
            "main",
            "--check-only",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "DELEGATE_PACK_OK" in result.stdout
    assert (session / "CONTEXT_PACK.md").is_file()
    assert "## Rules (mandatory)" in (session / "CONTEXT_PACK.md").read_text(
        encoding="utf-8"
    )
