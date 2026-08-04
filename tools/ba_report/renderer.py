#!/usr/bin/env python3
"""Render parsed BA markdown as styled HTML.

Uses the .ss-* design system from decision-server. Stdlib only.
"""

from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ARTIFACT_RELATIONSHIPS: dict[str, list[str]] = {
    "DISCUSSION.md": ["BUSINESS_ANALYSIS.md"],
    "BUSINESS_ANALYSIS.md": ["USER_FLOW.md", "PRD.md", "BRD.md", "URD.md", "SPEC_SRS.md", "REQ_REVIEW.md", "TEST_PLAN.md"],
    "USER_FLOW.md": ["PRD.md", "SPEC_SRS.md", "REQ_REVIEW.md"],
    "PRD.md": ["SPEC_SRS.md", "MODEL.md", "REQ_REVIEW.md", "TEST_PLAN.md"],
    "BRD.md": ["PRD.md", "REQ_REVIEW.md"],
    "URD.md": ["USER_FLOW.md", "PRD.md", "REQ_REVIEW.md"],
    "SPEC_SRS.md": ["MODEL.md", "PRD_EPIC.md", "REQ_REVIEW.md"],
    "MODEL.md": ["SPEC_SRS.md"],
    "DISCOVER.md": ["ROADMAP.md"],
    "ROADMAP.md": ["PRD_EPIC.md"],
    "PRD_EPIC.md": [],
    "REQ_REVIEW.md": ["TEST_PLAN.md", "TESTCASES.md"],
    "TEST_PLAN.md": ["TESTCASES.md"],
    "TESTCASES.md": ["DEFECT_LOG.md", "TEST_SUMMARY.md"],
    "DEFECT_LOG.md": ["TEST_SUMMARY.md"],
    "TEST_SUMMARY.md": [],
}

RELATIONSHIP_LABELS: dict[str, str] = {
    "DISCUSSION.md": "Discussion",
    "BUSINESS_ANALYSIS.md": "Business Analysis",
    "USER_FLOW.md": "User Flow",
    "PRD.md": "PRD",
    "BRD.md": "BRD",
    "URD.md": "URD",
    "SPEC_SRS.md": "SRS",
    "MODEL.md": "Data Model",
    "DISCOVER.md": "Discovery",
    "ROADMAP.md": "Roadmap",
    "PRD_EPIC.md": "Epics",
    "REQ_REVIEW.md": "Requirement Review",
    "TEST_PLAN.md": "Test Plan",
    "TESTCASES.md": "Test Cases",
    "DEFECT_LOG.md": "Defect Log",
    "TEST_SUMMARY.md": "Test Summary",
}


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
    toc = render_toc(artifacts)
    artifact_graph = render_artifact_graph(artifacts)
    artifact_sections = render_artifact_sections(artifacts)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!doctype html>
<html lang="en">
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
    <div class="nav-title">Artifacts</div>
    <ul>
      {navigation}
    </ul>
  </nav>

  <aside class="ss-toc" aria-label="Table of contents">
    <div class="toc-title">On this page</div>
    <ul>
      {toc}
    </ul>
  </aside>

  <main id="main" class="ss-main">
    {artifact_graph}
    {artifact_sections}
  </main>

  <footer class="ss-footer">
    <div class="ss-footer-inner">
      <p>BA Report · Generated {generated_at} · Mermaid CDN</p>
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


def render_toc(artifacts: dict[str, dict[str, Any]]) -> str:
    """Render right-sidebar table of contents from artifact sections."""
    entries = []
    for filename, data in artifacts.items():
        artifact_id = filename_to_id(filename)
        title = data.get("title", filename)
        entries.append(f'<li class="toc-h2"><a href="#{artifact_id}">{html.escape(title)}</a></li>')
        for section in data.get("sections", []):
            section_id = section_to_id(section.get("heading", ""), artifact_id)
            entries.append(f'<li class="toc-h3"><a href="#{section_id}">{html.escape(section["heading"])}</a></li>')
    return "\n      ".join(entries)


def render_artifact_graph(artifacts: dict[str, dict[str, Any]]) -> str:
    """Render Mermaid diagram showing relationships between artifacts."""
    if len(artifacts) < 2:
        return ""

    available = set(artifacts.keys())
    edges = []
    for filename in artifacts:
        targets = ARTIFACT_RELATIONSHIPS.get(filename, [])
        for target in targets:
            if target in available:
                src_label = RELATIONSHIP_LABELS.get(filename, Path(filename).stem)
                tgt_label = RELATIONSHIP_LABELS.get(target, Path(target).stem)
                src_id = filename_to_id(filename)
                tgt_id = filename_to_id(target)
                edges.append(f'  {src_id}["{src_label}"] --> {tgt_id}["{tgt_label}"]')

    if not edges:
        return ""

    mermaid_code = "graph LR\n" + "\n".join(edges)

    return f"""
    <div class="ss-ba-graph ss-card">
      <h2>Artifact Relationships</h2>
      <p class="ss-prose ss-mute">How artifacts in this session connect to each other</p>
      <div class="ss-mermaid">
        <div class="mermaid">{html.escape(mermaid_code)}</div>
      </div>
    </div>
"""


def render_artifact_sections(artifacts: dict[str, dict[str, Any]]) -> str:
    """Render all artifact sections."""
    sections = []
    available = set(artifacts.keys())
    for filename, data in artifacts.items():
        artifact_id = filename_to_id(filename)
        title = data.get("title", filename)
        related = render_related_artifacts(filename, available)

        section_html = f"""
    <section id="{artifact_id}" class="ss-ba-artifact">
      <div class="ss-card">
        <h2>{html.escape(title)}</h2>
        <p class="ss-prose ss-mute">Source: {html.escape(filename)}</p>
        {related}
      </div>
"""
        for section in data.get("sections", []):
            section_html += render_section(section, artifact_id)

        section_html += "    </section>\n"
        sections.append(section_html)

    return "\n".join(sections)


def render_related_artifacts(filename: str, available: set[str]) -> str:
    """Render related artifacts badges for a given artifact."""
    related_filenames = ARTIFACT_RELATIONSHIPS.get(filename, [])
    related_available = [f for f in related_filenames if f in available]

    if not related_available:
        return ""

    badges = []
    for rel_file in related_available:
        rel_id = filename_to_id(rel_file)
        rel_label = RELATIONSHIP_LABELS.get(rel_file, Path(rel_file).stem)
        badges.append(f'<a class="ss-ba-related" href="#{rel_id}">{html.escape(rel_label)}</a>')

    return f'\n        <div class="ss-ba-related-group"><span class="ss-ba-related-label">Related:</span>{"".join(badges)}</div>'


def render_section(section: dict[str, Any], artifact_id: str = "") -> str:
    """Render a single section to HTML."""
    heading = section.get("heading", "")
    level = section.get("level", 2)
    section_type = section.get("type", "prose")
    section_id = section_to_id(heading, artifact_id)

    heading_tag = f"h{min(level + 1, 6)}"

    html_parts = [
        f'      <div id="{section_id}" class="ss-section-content">',
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
                    if status in ["pass", "fail", "blocked", "yes", "no", "confirmed", "inferred", "unknown", "done", "todo"]:
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

    # Links: [text](url) — rewrite artifact filenames to anchors
    def rewrite_link(m: re.Match) -> str:
        link_text = m.group(1)
        url = m.group(2)
        # Check if URL points to a known BA artifact
        url_clean = url.split("#")[0].split("?")[0]
        artifact_id = _filename_to_anchor(url_clean)
        if artifact_id:
            fragment = url.split("#")[1] if "#" in url else ""
            anchor = f"#{artifact_id}"
            if fragment:
                anchor = f"#{fragment}"
            return f'<a href="{anchor}">{link_text}</a>'
        return f'<a href="{url}">{link_text}</a>'

    text = re.sub(r"\[(.+?)\]\((.+?)\)", rewrite_link, text)

    return text


def _filename_to_anchor(url: str) -> str | None:
    """If url matches a known BA artifact filename, return its anchor ID."""
    for artifact_name in ARTIFACT_RELATIONSHIPS:
        if url == artifact_name or url == f"./{artifact_name}" or url.endswith(f"/{artifact_name}"):
            return filename_to_id(artifact_name)
    return None


def filename_to_id(filename: str) -> str:
    """Convert filename to HTML ID."""
    name = Path(filename).stem
    return re.sub(r"[^a-zA-Z0-9]", "-", name).lower()


def section_to_id(heading: str, artifact_id: str = "") -> str:
    """Convert section heading to HTML ID, prefixed by artifact."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", heading).strip("-").lower()
    if artifact_id:
        return f"{artifact_id}-{slug}"
    return slug
