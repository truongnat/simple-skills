from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from simple_skills.cli import find_local_installer, main

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_find_local_installer_from_repo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(REPO_ROOT)
    monkeypatch.delenv("SIMPLE_SKILLS_ROOT", raising=False)
    found = find_local_installer()
    assert found is not None
    assert found.resolve() == (REPO_ROOT / "install.sh").resolve()


def test_find_local_installer_ignores_package_parents(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SIMPLE_SKILLS_ROOT", raising=False)
    assert find_local_installer() is None


def test_sk_doctor_via_local_installer(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("SIMPLE_SKILLS_ROOT", str(REPO_ROOT))
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    code = main(["doctor"])
    assert code != 0


def test_sk_install_into_temp_project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[list[str]] = []

    def fake_call(argv: list[str]) -> int:
        calls.append(argv)
        return 0

    monkeypatch.setattr(subprocess, "call", fake_call)
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    monkeypatch.delenv("SIMPLE_SKILLS_ROOT", raising=False)
    monkeypatch.chdir(REPO_ROOT)
    code = main(["install", "--agents-mode", "replace", "--profile", "core"])
    assert code == 0
    assert calls
    assert calls[0][0] == "bash"
    assert calls[0][1].endswith("install.sh")
    assert calls[0][2:] == ["install", "--agents-mode", "replace", "--profile", "core"]


def test_sk_install_downloads_installer_outside_kit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[list[str]] = []
    downloaded: list[str] = []
    file_existed_during_call: list[bool] = []

    def fake_call(argv: list[str]) -> int:
        calls.append(argv)
        file_existed_during_call.append(Path(argv[1]).is_file())
        return 0

    def fake_download(url: str, dest: Path) -> None:
        downloaded.append(url)
        dest.write_text("#!/usr/bin/env bash\n", encoding="utf-8")

    monkeypatch.setattr(subprocess, "call", fake_call)
    monkeypatch.setattr("simple_skills.cli._download", fake_download)
    monkeypatch.setenv("SIMPLE_SKILLS_SHELL", "bash")
    monkeypatch.delenv("SIMPLE_SKILLS_ROOT", raising=False)
    monkeypatch.chdir(tmp_path)
    assert main(["install", "--profile", "core"]) == 0
    assert downloaded
    assert downloaded[0].endswith("/install.sh")
    assert calls[0][1].endswith("install.sh")
    assert file_existed_during_call == [True]

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
