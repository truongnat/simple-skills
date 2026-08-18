from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_catalog_builder_writes_all_skills() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "build_catalog.py"), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "catalog OK" in result.stdout


def test_catalog_json_matches_disk() -> None:
    catalog = json.loads((REPO_ROOT / "catalog.json").read_text(encoding="utf-8"))
    on_disk = {
        p.name for p in (REPO_ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    }
    catalog_ids = {s["id"] for s in catalog["skills"]}
    assert catalog_ids == on_disk, (
        f"catalog ids ({len(catalog_ids)}) != disk SKILL.md dirs ({len(on_disk)})\n"
        f"missing in catalog: {on_disk - catalog_ids}\n"
        f"missing on disk: {catalog_ids - on_disk}"
    )
    assert "init" in catalog_ids
    assert catalog["meta"]["skill_count"] == len(on_disk)
    # Every skill must have a raw URL under the repo.
    for skill in catalog["skills"]:
        assert skill["raw_skill"].endswith(f"/skills/{skill['id']}/SKILL.md")


def test_catalog_fits_groups_exist_in_catalog() -> None:
    catalog = json.loads((REPO_ROOT / "catalog.json").read_text(encoding="utf-8"))
    ids = {s["id"] for s in catalog["skills"]}
    for group, skill_ids in catalog["fits"].items():
        for sid in skill_ids:
            assert sid in ids, f"fits[{group}] references missing skill {sid}"


def _install_minimal(tmp_path: Path) -> Path:
    """Run install.sh from a synthetic source tree, return the .agents dir."""
    src = tmp_path / "src"
    shutil.copytree(REPO_ROOT / "docs", src / "docs")
    shutil.copytree(REPO_ROOT / "tools", src / "tools")
    shutil.copytree(REPO_ROOT / "skills" / "init", src / "skills" / "init")
    shutil.copy2(REPO_ROOT / "install.sh", src / "install.sh")
    shutil.copy2(REPO_ROOT / "catalog.json", src / "catalog.json")
    # is_simple_skills_source needs these markers.
    (src / "skills" / "planning").mkdir(parents=True)
    (src / "skills" / "planning" / "SKILL.md").write_text("# planning\n", encoding="utf-8")
    (src / "skills" / "execution").mkdir()
    (src / "skills" / "execution" / "SKILL.md").write_text("# execution\n", encoding="utf-8")

    target = tmp_path / "proj"
    target.mkdir()
    result = subprocess.run(
        ["bash", "install.sh", "install"],
        cwd=src,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    # install.sh resolves TARGET via cwd when running from the source tree.
    agents = src / ".agents"
    assert agents.is_dir(), result.stdout
    return agents


def test_install_is_minimal_only_init_skill(tmp_path: Path) -> None:
    agents = _install_minimal(tmp_path)
    skills = [p.name for p in (agents / "skills").iterdir()]
    assert skills == ["init"], f"minimal install should ship only init, got {skills}"
    assert (agents / "catalog.json").is_file()
    assert (agents / "settings.yaml").is_file()
    assert (agents / "tools" / "policy" / "redact.py").is_file()
    assert (agents / "tools" / "providers" / "compile.py").is_file()
    assert (agents / "tools" / "session" / "session.sh").is_file()


def test_status_reports_no_kit(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    result = subprocess.run(
        [sys.executable, "-m", "simple_skills", "status"],
        env={"PYTHONPATH": str(REPO_ROOT / "src")},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "no installed kit" in result.stdout


def test_validate_reports_ok_from_repo() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "simple_skills", "validate"],
        cwd=REPO_ROOT,
        env={"PYTHONPATH": str(REPO_ROOT / "src")},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "SKILL_VALIDATION_OK" in result.stdout
