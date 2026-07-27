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
    "ba-dashboard",
    "ba-kg",
    "ba-handoff",
    "ba-integrate",
)


def test_ba_profile_includes_consolidated_skills() -> None:
    profiles = json.loads(
        (REPO_ROOT / "docs" / "config" / "install-profiles.json").read_text(
            encoding="utf-8"
        )
    )
    assert "ba" in profiles["profiles"]
    ba = profiles["profiles"]["ba"]
    assert ba.get("includes") == ["core"]
    assert set(ba["skills"]) == set(BA_SKILLS)


def test_ba_skills_registered_and_have_contract() -> None:
    manifest = json.loads(
        (REPO_ROOT / "docs" / "config" / "first-party-skills.json").read_text(
            encoding="utf-8"
        )
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
    doc = (REPO_ROOT / "docs" / "guides" / "BA_SKILLS.md").read_text(encoding="utf-8")
    for alias in (
        "/prd",
        "/sequence",
        "/d2-erd",
        "/dbdiagram",
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
        "/figma",
        "/dashboard",
        "/kg",
        "/meet",
        "/jira",
        "/confluence",
        "/delegate",
    ):
        assert alias in doc


def test_gap_analysis_has_cr_template() -> None:
    assert (
        REPO_ROOT / "skills" / "gap-analysis" / "templates" / "CR.template.md"
    ).is_file()


def test_p2_templates_exist() -> None:
    assert (REPO_ROOT / "skills" / "ux-wireframe" / "templates" / "FIGMA_BRIEF.template.md").is_file()
    assert (REPO_ROOT / "skills" / "ba-dashboard" / "templates" / "DASHBOARD.template.md").is_file()
    assert (REPO_ROOT / "skills" / "ba-kg" / "templates" / "KG.template.md").is_file()
    assert (REPO_ROOT / "skills" / "ba-integrate" / "templates" / "INTEGRATE_JIRA.template.md").is_file()
