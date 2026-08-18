from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHECK = REPO_ROOT / "scripts" / "check_version.py"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )


def test_version_consistent() -> None:
    result = _run()
    assert result.returncode == 0, result.stderr
    assert "consistent" in result.stdout


def test_version_consistent_with_matching_tag() -> None:
    from simple_skills import __version__

    result = _run("--expect-tag", f"v{__version__}")
    assert result.returncode == 0, result.stderr


def test_version_mismatch_with_wrong_tag() -> None:
    from simple_skills import __version__

    wrong = "v0.0.0" if not __version__.startswith("0.0.0") else "v0.0.1"
    result = _run("--expect-tag", wrong)
    assert result.returncode == 1
    assert "!= pyproject.toml version" in result.stderr
