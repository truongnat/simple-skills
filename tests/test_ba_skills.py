from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

BA_SKILLS = (
    "specify",
    "biz-model",
    "story-spec",
    "gap-analysis",
    "user-flow",
    "api-ba",
    "ba-test",
    "reverse-doc",
    "ux-wireframe",
)


def test_ba_profile_includes_consolidated_skills() -> None:
    profiles = json.loads(
        (REPO_ROOT / "docs" / "install-profiles.json").read_text(encoding="utf-8")
    )
    assert "ba" in profiles["profiles"]
    ba = profiles["profiles"]["ba"]
    assert ba.get("includes") == ["core"]
    assert set(ba["skills"]) == set(BA_SKILLS)


def test_ba_skills_registered_and_have_contract() -> None:
    manifest = json.loads(
        (REPO_ROOT / "docs" / "first-party-skills.json").read_text(encoding="utf-8")
    )
    names = {e["name"] for e in manifest["skills"]}
    for skill in BA_SKILLS:
        assert skill in names
        assert skill in manifest["preamble_required_for"]
        assert skill in manifest["report_skills"]
        text = (REPO_ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
        assert "## Contract (mandatory)" in text
        assert "### Required artifacts" in text
        assert "session.sh commit" in text
        assert (REPO_ROOT / "skills" / skill / "agents" / "openai.yaml").is_file()


def test_ba_skills_map_doc_lists_aliases() -> None:
    doc = (REPO_ROOT / "docs" / "BA_SKILLS.md").read_text(encoding="utf-8")
    for alias in (
        "/prd",
        "/sequence",
        "/usecase",
        "/gap",
        "/cr",
        "/user-flow",
        "/api-doc",
        "/api-readiness",
        "/test-checklist",
        "/reverse-doc",
        "/wireframe-ascii",
        "/prototype-html",
    ):
        assert alias in doc


def test_gap_analysis_has_cr_template() -> None:
    assert (
        REPO_ROOT / "skills" / "gap-analysis" / "templates" / "CR.template.md"
    ).is_file()
