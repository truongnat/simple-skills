from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_default_report_output_format_is_markdown() -> None:
    settings = (REPO_ROOT / "docs" / "config" / "settings.yaml").read_text(
        encoding="utf-8"
    )
    assert "output_format: markdown" in settings
    assert "prose_language: repo-default" in settings


def test_comment_language_is_separate_from_thread_language() -> None:
    policy = (REPO_ROOT / "docs" / "policy" / "AGENT_POLICY.md").read_text(
        encoding="utf-8"
    )
    preamble = (REPO_ROOT / "docs" / "policy" / "SKILL_PREAMBLE.md").read_text(
        encoding="utf-8"
    )
    comments = (REPO_ROOT / "docs" / "conventions" / "CODE_COMMENTS.md").read_text(
        encoding="utf-8"
    )
    rules = (REPO_ROOT / "tools" / "session" / "RULES_BUNDLE.template.md").read_text(
        encoding="utf-8"
    )
    execution = (REPO_ROOT / "skills" / "execution" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "rules.code.comments.prose_language" in policy
    assert "Never infer" in policy and "settings.language" in policy
    assert "prose_language" in preamble
    assert "not** `settings.language`" in comments
    assert "rules.code.comments.prose_language" in execution
    assert "**not**" in execution and "`settings.language`" in execution
    assert "prose_language" in rules
    assert "**not**" in rules and "`settings.language`" in rules


def test_contract_schema_documents_artifacts_subsection() -> None:
    policy = (REPO_ROOT / "docs" / "policy" / "AGENT_POLICY.md").read_text(
        encoding="utf-8"
    )
    manifest = (REPO_ROOT / "docs" / "config" / "first-party-skills.json").read_text(
        encoding="utf-8"
    )
    assert "Contract table" in policy
    assert "### Required artifacts" in policy
    assert '"Inputs"' in manifest and '"Safety"' in manifest
    assert "contract_requires_artifacts_section" in manifest


def test_outcome_first_thinking_method_is_wired() -> None:
    preamble = (REPO_ROOT / "docs" / "policy" / "SKILL_PREAMBLE.md").read_text(
        encoding="utf-8"
    )
    policy = (REPO_ROOT / "docs" / "policy" / "AGENT_POLICY.md").read_text(
        encoding="utf-8"
    )
    detail = (REPO_ROOT / "docs" / "thinking" / "outcome-first.md").read_text(
        encoding="utf-8"
    )
    index = (REPO_ROOT / "docs" / "thinking" / "README.md").read_text(encoding="utf-8")
    catalog = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
    assert "Outcome-first" in preamble
    assert "three-axis" in preamble
    assert "thinking/outcome-first.md" in preamble
    assert "Outcome-first" in policy
    assert "WHO" in detail and "WHAT" in detail and "EVIDENCE" in detail
    assert "OUTCOME.md" in detail and "forbidden" in detail.lower()
    assert "outcome-first.md" in index
    assert "thinking/" in catalog


def test_validate_skills_script_passes() -> None:
    import subprocess

    result = subprocess.run(
        ["python3", str(REPO_ROOT / "scripts" / "validate_skills.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SKILL_VALIDATION_OK" in result.stdout


def test_agent_rules_define_html_artifact_compatibility() -> None:
    rules = (REPO_ROOT / "docs" / "policy" / "AGENT_POLICY.md").read_text(
        encoding="utf-8"
    )
    assert "## Artifact format resolution" in rules
    assert "then fall back to the" in rules
    assert "alternate extension" in rules
    assert "session-serve/serve.py" in rules
    assert "choice-reader" in rules


def test_entrypoint_points_at_policy() -> None:
    agents = (REPO_ROOT / "docs" / "AGENTS.md").read_text(encoding="utf-8")
    assert "AGENT_POLICY.md" in agents
    assert len(agents.splitlines()) <= 120
