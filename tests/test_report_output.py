from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_default_report_output_format_is_markdown() -> None:
    settings = (REPO_ROOT / "docs" / "settings.yaml").read_text(encoding="utf-8")
    assert "output_format: markdown" in settings
    assert "prose_language: repo-default" in settings


def test_comment_language_is_separate_from_thread_language() -> None:
    policy = (REPO_ROOT / "docs" / "AGENT_POLICY.md").read_text(encoding="utf-8")
    preamble = (REPO_ROOT / "docs" / "SKILL_PREAMBLE.md").read_text(encoding="utf-8")
    comments = (REPO_ROOT / "docs" / "CODE_COMMENTS.md").read_text(encoding="utf-8")
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


def test_agent_rules_define_html_artifact_compatibility() -> None:
    rules = (REPO_ROOT / "docs" / "AGENT_POLICY.md").read_text(encoding="utf-8")
    assert "## Artifact format resolution" in rules
    assert "then fall back to the" in rules
    assert "alternate extension" in rules
    assert "session-serve/serve.py" in rules
    assert "choice-reader" in rules


def test_entrypoint_points_at_policy() -> None:
    agents = (REPO_ROOT / "docs" / "AGENTS.md").read_text(encoding="utf-8")
    assert "AGENT_POLICY.md" in agents
    assert len(agents.splitlines()) <= 120
