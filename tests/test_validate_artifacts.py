from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "tools" / "session" / "validate_artifacts.py"


# ---------------------------------------------------------------------------
# SemVer 2.0.0 unit tests
# ---------------------------------------------------------------------------

def _import_semver_helpers():
    """Import SemVer helpers from the validator module."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "validate_artifacts", VALIDATOR
    )
    mod = importlib.util.module_from_spec(spec)
    # Stub the _work_settings import so the module loads standalone
    import types
    mod_ws = types.ModuleType("_work_settings")
    mod_ws.work_dir_name = lambda root: ".agent-work"
    import sys
    sys.modules["_work_settings"] = mod_ws
    spec.loader.exec_module(mod)
    return mod


def test_parse_semver_valid() -> None:
    mod = _import_semver_helpers()
    assert mod.parse_semver("1.0.0") == (1, 0, 0)
    assert mod.parse_semver("2.3.4") == (2, 3, 4)
    assert mod.parse_semver("0.1.0") == (0, 1, 0)
    assert mod.parse_semver("10.20.30") == (10, 20, 30)
    # Pre-release and build metadata are valid but parse returns M.m.p
    assert mod.parse_semver("1.0.0-alpha.1") == (1, 0, 0)
    assert mod.parse_semver("1.0.0+build.123") == (1, 0, 0)


def test_parse_semver_invalid() -> None:
    mod = _import_semver_helpers()
    assert mod.parse_semver("1") is None
    assert mod.parse_semver("1.0") is None
    assert mod.parse_semver("abc") is None
    assert mod.parse_semver("") is None
    assert mod.parse_semver("01.0.0") is None  # leading zero


def test_is_semver_compatible() -> None:
    mod = _import_semver_helpers()
    # Same major = compatible
    assert mod.is_semver_compatible("2.0.0", (2, 0, 0)) is True
    assert mod.is_semver_compatible("2.1.0", (2, 0, 0)) is True
    assert mod.is_semver_compatible("2.99.99", (2, 0, 0)) is True
    # Lower major = incompatible
    assert mod.is_semver_compatible("1.99.99", (2, 0, 0)) is False
    # Major 0 = anything goes
    assert mod.is_semver_compatible("0.1.0", (2, 0, 0)) is True
    assert mod.is_semver_compatible("0.0.1", (2, 0, 0)) is True
    # Invalid = incompatible
    assert mod.is_semver_compatible("abc", (2, 0, 0)) is False
    assert mod.is_semver_compatible("2", (2, 0, 0)) is False


def test_validate_rejects_old_schema_version(tmp_path: Path) -> None:
    """Validator should fail when schema has a non-SemVer version (e.g. integer 2)."""
    session = tmp_path / ".agent-work" / "sessions" / "Task-1-oldver"
    session.mkdir(parents=True)
    (tmp_path / ".agent-work" / "sessions" / ".current").write_text(
        ".agent-work/sessions/Task-1-oldver\n", encoding="utf-8"
    )
    # Write a schema with old integer version
    schema_dir = tmp_path / ".agents" / "tools" / "session"
    schema_dir.mkdir(parents=True)
    (schema_dir / "artifact-schemas.json").write_text(
        '{"version": 2, "artifacts": {}}', encoding="utf-8"
    )
    result = subprocess.run(
        ["python3", str(VALIDATOR), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "incompatible" in result.stdout


def test_validate_artifacts_accepts_seeded_discussion(tmp_path: Path) -> None:
    session = tmp_path / ".agent-work" / "sessions" / "Task-1-demo"
    session.mkdir(parents=True)
    (tmp_path / ".agent-work" / "sessions" / ".current").write_text(
        ".agent-work/sessions/Task-1-demo\n", encoding="utf-8"
    )
    template = (
        REPO_ROOT / "skills" / "brainstorming" / "templates" / "DISCUSSION.template.md"
    ).read_text(encoding="utf-8")
    (session / "DISCUSSION.md").write_text(template, encoding="utf-8")

    result = subprocess.run(
        ["python3", str(VALIDATOR), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SESSION_ARTIFACTS_OK" in result.stdout


def test_validate_artifacts_fails_on_missing_heading(tmp_path: Path) -> None:
    session = tmp_path / ".agent-work" / "sessions" / "Task-1-bad"
    session.mkdir(parents=True)
    (tmp_path / ".agent-work" / "sessions" / ".current").write_text(
        ".agent-work/sessions/Task-1-bad\n", encoding="utf-8"
    )
    (session / "REVIEW.md").write_text("# Review\n\n## Executive summary\n\n- x\n", encoding="utf-8")

    result = subprocess.run(
        ["python3", str(VALIDATOR), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "SESSION_ARTIFACTS_FAILED" in result.stdout
    assert "Developer overview" in result.stdout


def test_validate_artifacts_accepts_underscore_headings(tmp_path: Path) -> None:
    """YAML keys use underscores (developer_overview) — agent may generate
    headings with underscores. Validator should accept both forms."""
    session = tmp_path / ".agent-work" / "sessions" / "Task-1-underscore"
    session.mkdir(parents=True)
    (tmp_path / ".agent-work" / "sessions" / ".current").write_text(
        ".agent-work/sessions/Task-1-underscore\n", encoding="utf-8"
    )
    # Agent generates headings with underscores from YAML keys
    content = """# Review

## Executive_summary

- Summary here.

## Developer_overview

| Field | Value |
|---|---|
| Status | ready |

## Findings

| ID | Severity | Location | Evidence | Impact | Recommendation |
|---|---|---|---|---|---|
| F-001 | Low | src/x.ts | line 10 | minor | fix later |

## Recommendation

- Ship it.

## Handoff

- Next: deploy
"""
    (session / "REVIEW.md").write_text(content, encoding="utf-8")

    result = subprocess.run(
        ["python3", str(VALIDATOR), "--root", str(tmp_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SESSION_ARTIFACTS_OK" in result.stdout
