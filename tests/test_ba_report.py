"""Tests for BA report HTML generator tool."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.ba_report.parser import (
    extract_mermaid,
    extract_tables,
    parse_ba_markdown,
    parse_table,
)
from tools.ba_report.renderer import (
    filename_to_id,
    inline_format,
    render_mermaid,
    render_prose,
    render_report,
    render_table,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class TestParser:
    """Test markdown parser."""

    def test_parse_business_analysis_template(self):
        """Parse BUSINESS_ANALYSIS.template.md correctly."""
        template_path = (
            REPO_ROOT
            / "skills/business-analysis/templates/BUSINESS_ANALYSIS.template.md"
        )
        if not template_path.exists():
            pytest.skip("BUSINESS_ANALYSIS.template.md not found")

        text = template_path.read_text(encoding="utf-8")
        result = parse_ba_markdown(text)

        assert result["title"] == "Business Analysis"
        assert len(result["sections"]) > 0
        assert any(s["heading"] == "Executive summary" for s in result["sections"])
        assert any("User stories" in s["heading"] for s in result["sections"])

    def test_parse_table(self):
        """Parse markdown table into structured data."""
        table_md = [
            "| ID | Rule | Confidence |",
            "|---|---|---|",
            "| BR-001 | Test rule | Confirmed |",
            "| BR-002 | Another rule | Inferred |",
        ]
        result = parse_table(table_md)

        assert result["headers"] == ["ID", "Rule", "Confidence"]
        assert len(result["rows"]) == 2
        assert result["rows"][0] == ["BR-001", "Test rule", "Confirmed"]
        assert result["rows"][1] == ["BR-002", "Another rule", "Inferred"]

    def test_parse_empty_table(self):
        """Parse empty table."""
        result = parse_table([])
        assert result["headers"] == []
        assert result["rows"] == []

    def test_extract_mermaid(self):
        """Extract mermaid code blocks."""
        text = """
# Title

Some prose.

```mermaid
flowchart TD
  A-->B
  B-->C
```

More prose.

```mermaid
sequenceDiagram
  Alice->>Bob: Hello
```
"""
        diagrams = extract_mermaid(text)
        assert len(diagrams) == 2
        assert "flowchart TD" in diagrams[0]
        assert "sequenceDiagram" in diagrams[1]

    def test_extract_tables(self):
        """Extract all tables from markdown."""
        text = """
# Title

| ID | Name |
|---|---|
| 1 | Test |

Some prose.

| Col1 | Col2 |
|---|---|
| A | B |
"""
        tables = extract_tables(text)
        assert len(tables) == 2
        assert tables[0]["headers"] == ["ID", "Name"]
        assert tables[1]["headers"] == ["Col1", "Col2"]

    def test_parse_sections_with_mermaid(self):
        """Parse sections including mermaid diagrams."""
        text = """
# Title

## Section 1

Some prose.

## Section 2

```mermaid
flowchart TD
  A-->B
```
"""
        result = parse_ba_markdown(text)
        assert result["metadata"]["has_mermaid"] is True
        assert any(s["type"] == "mermaid" for s in result["sections"])


class TestRenderer:
    """Test HTML renderer."""

    def test_render_table_html(self):
        """Render table with .ss-table classes."""
        table = {
            "headers": ["ID", "Status"],
            "rows": [["BR-001", "Pass"], ["BR-002", "Fail"]],
        }
        html = render_table(table)

        assert 'class="ss-table"' in html
        assert 'data-status="pass"' in html
        assert 'data-status="fail"' in html
        assert "<th" in html
        assert "<td" in html

    def test_render_empty_table(self):
        """Render empty table."""
        html = render_table({"headers": [], "rows": []})
        assert "empty table" in html

    def test_render_mermaid(self):
        """Render mermaid diagram placeholder."""
        html = render_mermaid("flowchart TD\n  A-->B")
        assert 'class="ss-mermaid"' in html
        assert 'class="mermaid"' in html
        assert "flowchart TD" in html

    def test_render_empty_mermaid(self):
        """Render empty mermaid."""
        html = render_mermaid("")
        assert "empty diagram" in html

    def test_render_prose(self):
        """Render markdown prose."""
        text = """
This is a paragraph.

- List item 1
- List item 2

1. Ordered 1
2. Ordered 2
"""
        html = render_prose(text)
        assert "<p>" in html
        assert "<ul>" in html
        assert "<ol>" in html
        assert "<li>" in html

    def test_inline_format(self):
        """Test inline markdown formatting."""
        assert "<strong>bold</strong>" in inline_format("**bold**")
        assert "<em>italic</em>" in inline_format("*italic*")
        assert "<code>code</code>" in inline_format("`code`")
        assert '<a href="url">' in inline_format("[text](url)")

    def test_filename_to_id(self):
        """Convert filename to HTML ID."""
        assert filename_to_id("BUSINESS_ANALYSIS.md") == "business-analysis"
        assert filename_to_id("USER_FLOW.md") == "user-flow"
        assert filename_to_id("PRD.md") == "prd"

    def test_render_report(self):
        """Render full report from artifacts."""
        artifacts = {
            "BUSINESS_ANALYSIS.md": {
                "title": "Business Analysis",
                "sections": [
                    {
                        "heading": "Executive summary",
                        "level": 2,
                        "type": "prose",
                        "content": "Test summary.",
                        "data": None,
                    }
                ],
            }
        }
        html = render_report(artifacts, "Task-1-test")

        assert "<!doctype html>" in html
        assert "Task-1-test" in html
        assert "Business Analysis" in html
        assert 'class="ss-page' in html
        assert "mermaid.min.js" in html
        assert "ba-report.css" in html


class TestIntegration:
    """Integration tests."""

    def test_full_report_generation(self):
        """Generate complete report from sample BA artifacts."""
        # Create sample artifact
        sample_md = """
# Business Analysis

## Executive summary

- Test point 1
- Test point 2

## User stories

| ID | Actor | Need | Value |
|---|---|---|---|
| US-001 | User | Test need | Test value |

## Flow diagram

```mermaid
flowchart TD
  A[Start] --> B[Process]
  B --> C[End]
```
"""
        parsed = parse_ba_markdown(sample_md)
        artifacts = {"TEST.md": parsed}
        html = render_report(artifacts, "Task-1-test")

        # Verify structure
        assert "<!doctype html>" in html
        assert "Business Analysis" in html
        assert "ss-table" in html
        assert "mermaid" in html
        assert "US-001" in html

    def test_multiple_artifacts(self):
        """Render report with multiple artifacts."""
        artifacts = {
            "BUSINESS_ANALYSIS.md": {
                "title": "BA",
                "sections": [],
            },
            "USER_FLOW.md": {
                "title": "User Flow",
                "sections": [],
            },
        }
        html = render_report(artifacts, "Task-1-multi")

        assert "BA" in html
        assert "User Flow" in html
        assert "2 artifacts" in html
