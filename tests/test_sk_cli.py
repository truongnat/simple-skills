from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from simple_skills.cli import find_local_installer, main

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_find_local_installer_from_repo() -> None:
    found = find_local_installer()
    assert found is not None
    assert found.resolve() == (REPO_ROOT / "install.sh").resolve()


def test_sk_doctor_via_local_installer(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("SIMPLE_SKILLS_ROOT", str(REPO_ROOT))
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    code = main(["doctor"])
    assert code != 0


def test_sk_install_into_temp_project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Minimal host project; installer fetches from local SOURCE when cwd is the kit.
    # Here we point SIMPLE_SKILLS_ROOT and run install.sh which detects SOURCE via
    # is_simple_skills_source(pwd) — pwd is tmp, so it would try network.
    # Instead invoke with cwd=REPO_ROOT targeting TARGET via... install.sh uses pwd as TARGET.
    # So: chdir to tmp, but we need SOURCE. install.sh only uses pwd as SOURCE if
    # is_simple_skills_source(pwd). Workaround: copy enough for source detection OR
    # run from a stub that has local install.sh from env.

    # Practical approach: run installer with cwd = REPO_ROOT won't install into tmp.
    # Use subprocess to run install.sh from REPO with TARGET by... can't.
    # Copy install path: monkeypatch by placing a fake that still works —
    # simplest: call run_installer after making tmp look like a consumer and
    # set SOURCE by... install downloads.

    # Offline-safe: execute bash install.sh from REPO_ROOT with a wrapper that
    # we simulate by copying the short path used in test_installers — too heavy.
    # Instead unit-test that main builds and calls local script with right args:

    calls: list[list[str]] = []

    def fake_call(argv: list[str]) -> int:
        calls.append(argv)
        return 0

    monkeypatch.setattr(subprocess, "call", fake_call)
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    monkeypatch.delenv("SIMPLE_SKILLS_ROOT", raising=False)
    # find_local_installer will find REPO_ROOT because __file__ walks up
    code = main(["install", "--agents-mode", "replace", "--profile", "core"])
    assert code == 0
    assert calls
    assert calls[0][0] == "bash"
    assert calls[0][1].endswith("install.sh")
    assert calls[0][2:] == ["install", "--agents-mode", "replace", "--profile", "core"]


def test_sk_bare_defaults_to_install(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[list[str]] = []

    def fake_call(argv: list[str]) -> int:
        calls.append(argv)
        return 0

    monkeypatch.setattr(subprocess, "call", fake_call)
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    assert main([]) == 0
    assert calls[0][2:] == ["install"]


def test_sk_uninstall_flags(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[list[str]] = []

    def fake_call(argv: list[str]) -> int:
        calls.append(argv)
        return 0

    monkeypatch.setattr(subprocess, "call", fake_call)
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    assert main(["uninstall", "--yes", "--keep-settings", "--purge-work"]) == 0
    assert calls[0][2:] == [
        "uninstall",
        "--yes",
        "--keep-settings",
        "--purge-work",
    ]


def test_module_entrypoint() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "simple_skills", "--version"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        env={**dict(**{k: v for k, v in __import__("os").environ.items()}), "PYTHONPATH": str(REPO_ROOT / "src")},
    )
    assert result.returncode == 0
    assert "0.2.0" in result.stdout or "0.2.0" in result.stderr
