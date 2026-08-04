#!/usr/bin/env python3
"""Render parsed BA markdown as styled HTML.

Uses the .ss-* design system from decision-server. Stdlib only.
"""

from __future__ import annotations

import html
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def render_report(
    artifacts: dict[str, dict[str, Any]],
    session_name: str,
    title: str = "Business Analysis Report",
) -> str:
    """Render full HTML report from multiple BA artifacts.

    Args:
        artifacts: {filename: parsed_data} mapping
        session_name: Session identifier
        title: Report title

    Returns:
        Complete HTML string
    """
    navigation = render_navigation(artifacts)
    artifact_sections = render_artifact_sections(artifacts)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!doctype html>
<html lang="en" data-ss-theme="enterprise">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} — {html.escape(session_name)}</title>
  <link rel="stylesheet" href="/ba-report.css">
</head>
<body class="ss-page ss-wide">
  <a class="ss-skip" href="#main">Skip to content</a>

  <header class="ss-header">
    <div class="ss-header-inner">
      <p class="ss-eyebrow">Session: {html.escape(session_name)}</p>
      <h1>{html.escape(title)}</h1>
      <p class="ss-prose">Generated from {len(artifacts)} artifact{"s" if len(artifacts) != 1 else ""}</p>
    </div>
  </header>

  <nav class="ss-nav ss-ba-nav" aria-label="Artifact navigation">
    <ul>
      {navigation}
    </ul>
  </nav>

  <main id="main" class="ss-main">
    {artifact_sections}
  </main>

  <footer class="ss-footer">
    <div class="ss-footer-inner">
      <p>BA Report · Generated {generated_at} · Tailwind + Mermaid CDN</p>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="/ba-report.js" defer></script>
</body>
</html>
"""


def render_navigation(artifacts: dict[str, dict[str, Any]]) -> str:
    """Render sidebar navigation for multiple artifacts."""
    links = []
    for filename, data in artifacts.items():
        artifact_id = filename_to_id(filename)
        title = data.get("title", filename)
        links.append(f'<li><a href="#{artifact_id}">{html.escape(title)}</a></li>')
    return "\n      ".join(links)


def render_artifact_sections(artifacts: dict[str, dict[str, Any]]) -> str:
    """Render all artifact sections."""
    sections = []
    for filename, data in artifacts.items():
        artifact_id = filename_to_id(filename)
        title = data.get("title", filename)

        section_html = f"""
    <section id="{artifact_id}" class="ss-ba-artifact">
      <div class="ss-card">
        <h2>{html.escape(title)}</h2>
        <p class="ss-prose ss-mute">Source: {html.escape(filename)}</p>
      </div>
"""
        for section in data.get("sections", []):
            section_html += render_section(section)

        section_html += "    </section>\n"
        sections.append(section_html)

    return "\n".join(sections)


def render_section(section: dict[str, Any]) -> str:
    """Render a single section to HTML."""
    heading = section.get("heading", "")
    level = section.get("level", 2)
    section_type = section.get("type", "prose")

    # Heading tag (h2, h3, h4)
    heading_tag = f"h{min(level + 1, 6)}"

    html_parts = [
        f'      <div class="ss-section-content">',
        f"        <{heading_tag}>{html.escape(heading)}</{heading_tag}>",
    ]

    if section_type == "table":
        html_parts.append(render_table(section.get("data", {})))
    elif section_type == "mermaid":
        html_parts.append(render_mermaid(section.get("data", "")))
    else:  # prose
        html_parts.append(render_prose(section.get("content", "")))

    html_parts.append("      </div>")

    return "\n".join(html_parts)


def render_table(table: dict[str, Any]) -> str:
    """Render markdown table as .ss-table."""
    headers = table.get("headers", [])
    rows = table.get("rows", [])

    if not headers:
        return "<p class='ss-prose ss-mute'>_(empty table)_</p>"

    html_parts = ['<div class="ss-table-wrap">']
    html_parts.append('<table class="ss-table">')

    # Header
    html_parts.append("  <thead><tr>")
    for h in headers:
        html_parts.append(f'    <th scope="col">{html.escape(h)}</th>')
    html_parts.append("  </tr></thead>")

    # Body
    html_parts.append("  <tbody>")
    for row in rows:
        html_parts.append("    <tr>")
        for i, cell in enumerate(row):
            # Add data-status for status columns
            attrs = ""
            if i < len(headers):
                header_lower = headers[i].lower()
                if header_lower in ["status", "verdict", "blocking", "confidence"]:
                    status = cell.lower()
                    if status in ["pass", "fail", "blocked", "yes", "no", "confirmed", "inferred", "unknown"]:
                        attrs = f' data-status="{status}"'
            html_parts.append(f"      <td{attrs}>{html.escape(cell)}</td>")
        html_parts.append("    </tr>")
    html_parts.append("  </tbody>")
    html_parts.append("</table>")
    html_parts.append("</div>")

    return "\n".join(html_parts)


def render_mermaid(code: str) -> str:
    """Render mermaid diagram placeholder."""
    if not code.strip():
        return "<p class='ss-prose ss-mute'>_(empty diagram)_</p>"

    return f'<div class="ss-mermaid"><div class="mermaid">{html.escape(code)}</div></div>'


def render_prose(text: str) -> str:
    """Render markdown prose as HTML.

    Handles paragraphs, lists, inline code, bold/italic, and code blocks.
    """
    if not text.strip():
        return ""

    lines = text.split("\n")
    html_parts = []
    in_list = False
    list_type = None  # "ul" or "ol"
    in_code_block = False
    code_language = ""
    code_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check for code block start
        if stripped.startswith("```") and not in_code_block:
            in_code_block = True
            code_language = stripped[3:].strip()
            code_lines = []
            i += 1
            continue

        # Check for code block end
        if stripped.startswith("```") and in_code_block:
            in_code_block = False
            # Render the code block
            code_content = "\n".join(code_lines)
            lang_class = f' class="language-{code_language}"' if code_language else ""
            html_parts.append(f"<pre><code{lang_class}>{html.escape(code_content)}</code></pre>")
            i += 1
            continue

        # If inside code block, collect lines
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Horizontal rule (---, ***, ___)
        if re.match(r"^[-*_]{3,}$", stripped):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
                list_type = None
            html_parts.append("<hr>")
            i += 1
            continue

        # Empty line
        if not stripped:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
                list_type = None
            i += 1
            continue

        # Unordered list item
        if re.match(r"^[-*]\s+", stripped):
            if not in_list or list_type != "ul":
                if in_list:
                    html_parts.append(f"</{list_type}>")
                html_parts.append("<ul>")
                in_list = True
                list_type = "ul"
            content = re.sub(r"^[-*]\s+", "", stripped)
            html_parts.append(f"  <li>{inline_format(content)}</li>")
            i += 1
            continue

        # Ordered list item
        if re.match(r"^\d+\.\s+", stripped):
            if not in_list or list_type != "ol":
                if in_list:
                    html_parts.append(f"</{list_type}>")
                html_parts.append("<ol>")
                in_list = True
                list_type = "ol"
            content = re.sub(r"^\d+\.\s+", "", stripped)
            html_parts.append(f"  <li>{inline_format(content)}</li>")
            i += 1
            continue

        # Regular paragraph
        if in_list:
            html_parts.append(f"</{list_type}>")
            in_list = False
            list_type = None
        html_parts.append(f"<p>{inline_format(stripped)}</p>")
        i += 1

    if in_list:
        html_parts.append(f"</{list_type}>")

    return "\n".join(html_parts)


def inline_format(text: str) -> str:
    """Apply inline markdown formatting."""
    # Escape HTML first
    text = html.escape(text)

    # Bold: **text** or __text__
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)

    # Italic: *text* or _text_
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"_(.+?)_", r"<em>\1</em>", text)

    # Inline code: `code`
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)

    # Links: [text](url)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)

    return text


def filename_to_id(filename: str) -> str:
    """Convert filename to HTML ID."""
    # Remove .md extension and replace non-alphanumeric with -
    name = Path(filename).stem
    return re.sub(r"[^a-zA-Z0-9]", "-", name).lower()


# Import re for inline_format
import re
