from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATE = REPO_ROOT / "scripts" / "validate_skills.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_skills", VALIDATE)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _run() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE)],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )


def test_validator_passes_on_full_catalog() -> None:
    result = _run()
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SKILL_VALIDATION_OK" in result.stdout


def test_vendored_aix_skills_registered_in_third_party_doc() -> None:
    third_party = (REPO_ROOT / "docs" / "conventions" / "THIRD_PARTY_SKILLS.md").read_text(
        encoding="utf-8"
    )
    # Spot-check a few vendored aix skills are attributed.
    for name in ("docker-pro", "react-pro", "nestjs-pro", "postgresql-pro", "planning-pro"):
        if name == "planning-pro":
            continue  # deliberately not vendored (ss has its own planning)
        assert f"`{name}`" in third_party, f"{name} missing from THIRD_PARTY_SKILLS.md"


def test_x_schema_rejects_bad_kind() -> None:
    v = _load_validator()
    validate_x_schema = v.validate_x_schema

    errors: list[str] = []
    aliases: dict[str, str] = {}
    validate_x_schema("demo", "x-kind: madeup\n", errors, aliases)
    assert any("x-kind" in e for e in errors)


def test_x_schema_rejects_bad_version() -> None:
    v = _load_validator()
    validate_x_schema = v.validate_x_schema

    errors: list[str] = []
    aliases: dict[str, str] = {}
    validate_x_schema("demo", "x-version: v1\n", errors, aliases)
    assert any("x-version" in e for e in errors)


def test_x_schema_rejects_bad_provider() -> None:
    v = _load_validator()
    validate_x_schema = v.validate_x_schema

    errors: list[str] = []
    aliases: dict[str, str] = {}
    validate_x_schema("demo", "x-compatible: [claude, bing]\n", errors, aliases)
    assert any("x-compatible" in e for e in errors)


def test_x_schema_rejects_duplicate_alias() -> None:
    v = _load_validator()
    validate_x_schema = v.validate_x_schema

    errors: list[str] = []
    aliases: dict[str, str] = {"docker": "docker-pro"}
    validate_x_schema("other-pro", "aliases: [docker]\n", errors, aliases)
    assert any("already used" in e for e in errors)


def test_x_schema_accepts_block_style_compatible() -> None:
    v = _load_validator()
    validate_x_schema = v.validate_x_schema

    errors: list[str] = []
    aliases: dict[str, str] = {}
    fm = "x-compatible:\n  - claude\n  - cursor\n  - codex\n  - gemini\n"
    validate_x_schema("demo-pro", fm, errors, aliases)
    assert not errors, errors
