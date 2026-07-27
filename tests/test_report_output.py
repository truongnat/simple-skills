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
    ipo = (REPO_ROOT / "docs" / "thinking" / "input-process-output.md").read_text(
        encoding="utf-8"
    )
    small_batch = (REPO_ROOT / "docs" / "thinking" / "small-batch.md").read_text(
        encoding="utf-8"
    )
    explicit = (
        REPO_ROOT / "docs" / "thinking" / "make-implicit-explicit.md"
    ).read_text(encoding="utf-8")
    ssot = (
        REPO_ROOT / "docs" / "thinking" / "single-source-of-truth.md"
    ).read_text(encoding="utf-8")
    feedback = (
        REPO_ROOT / "docs" / "thinking" / "feedback-loop.md"
    ).read_text(encoding="utf-8")
    default_path = (
        REPO_ROOT / "docs" / "thinking" / "default-path-first.md"
    ).read_text(encoding="utf-8")
    reversible = (
        REPO_ROOT / "docs" / "thinking" / "reversible-decisions.md"
    ).read_text(encoding="utf-8")
    standardize = (
        REPO_ROOT / "docs" / "thinking" / "standardize-before-automate.md"
    ).read_text(encoding="utf-8")
    index = (REPO_ROOT / "docs" / "thinking" / "README.md").read_text(encoding="utf-8")
    catalog = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
    assert "Outcome-first" in preamble
    assert "three-axis" in preamble
    assert "thinking/outcome-first.md" in preamble
    assert "Input → Process → Output" in preamble
    assert "thinking/input-process-output.md" in preamble
    assert "Make implicit explicit" in preamble
    assert "thinking/make-implicit-explicit.md" in preamble
    assert "Single Source of Truth" in preamble
    assert "thinking/single-source-of-truth.md" in preamble
    assert "Small-batch" in preamble
    assert "thinking/small-batch.md" in preamble
    assert "Feedback loop" in preamble
    assert "thinking/feedback-loop.md" in preamble
    assert "Default path first" in preamble
    assert "thinking/default-path-first.md" in preamble
    assert "Reversible decisions" in preamble
    assert "thinking/reversible-decisions.md" in preamble
    assert "Standardize before automate" in preamble
    assert "thinking/standardize-before-automate.md" in preamble
    assert "Outcome-first" in policy
    assert "Input → Process → Output" in policy
    assert "Make implicit explicit" in policy
    assert "Single Source of Truth" in policy
    assert "Small-batch" in policy
    assert "Feedback loop" in policy
    assert "Default path first" in policy
    assert "Reversible decisions" in policy
    assert "Standardize before automate" in policy
    assert "WHO" in detail and "WHAT" in detail and "EVIDENCE" in detail
    assert "OUTCOME.md" in detail and "forbidden" in detail.lower()
    assert "Input" in ipo and "Process" in ipo and "Output" in ipo
    assert "IPO.md" in ipo
    assert "four-property" in small_batch or "Four-property" in small_batch
    assert "SMALL_BATCH.md" in small_batch
    assert "Dual-interpretation" in explicit or "dual-interpretation" in explicit
    assert "IMPLICIT.md" in explicit
    assert "Cite" in ssot and "fork" in ssot.lower()
    assert "SSOT.md" in ssot
    assert "diagram" in ssot and "Doc reality" in ssot
    assert "latency" in feedback.lower() and "modality" in feedback.lower()
    assert "FEEDBACK.md" in feedback
    assert "Given" in feedback and "Expect" in feedback
    assert "Hybrid C" in feedback or "hybrid" in feedback.lower()
    assert "L1" in default_path and "happy" in default_path.lower()
    assert "HAPPY_PATH.md" in default_path
    assert "name early" in default_path.lower() or "Name early" in default_path
    assert "reverse-cost" in reversible.lower() or "Hard-to-reverse" in reversible
    assert "REVERSIBLE.md" in reversible
    assert "High-impact" in reversible and "hard-to-reverse" in reversible.lower()
    assert "manual" in standardize.lower() and "template" in standardize.lower()
    assert "AUTOMATE.md" in standardize
    assert "accelerated mess" in standardize.lower() or "messy process" in standardize.lower()
    assert "outcome-first.md" in index and "input-process-output.md" in index
    assert "make-implicit-explicit.md" in index and "single-source-of-truth.md" in index
    assert "small-batch.md" in index and "feedback-loop.md" in index
    assert "default-path-first.md" in index and "reversible-decisions.md" in index
    assert "standardize-before-automate.md" in index
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
