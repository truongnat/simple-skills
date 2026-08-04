#!/usr/bin/env python3
"""Parse BA markdown artifacts into structured sections.

Stdlib only. Handles headings, tables, mermaid diagrams, and prose.
"""

from __future__ import annotations

import re
from typing import Any


def parse_ba_markdown(text: str) -> dict[str, Any]:
    """Parse BA markdown into structured sections.

    Args:
        text: Markdown content

    Returns:
        {
            "title": str,
            "sections": [
                {
                    "heading": str,
                    "level": int,
                    "type": str,  # "prose", "table", "mermaid"
                    "content": str,  # raw markdown
                    "data": any  # parsed data for tables/mermaid
                }
            ],
            "metadata": {
                "has_mermaid": bool,
                "tables": list[str]
            }
        }
    """
    title = extract_title(text)
    sections = extract_sections(text)

    has_mermaid = any(s["type"] == "mermaid" for s in sections)
    tables = [s["heading"] for s in sections if s["type"] == "table"]

    return {
        "title": title,
        "sections": sections,
        "metadata": {
            "has_mermaid": has_mermaid,
            "tables": tables,
        },
    }


def extract_title(text: str) -> str:
    """Extract first H1 heading as title."""
    match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"


def extract_sections(text: str) -> list[dict[str, Any]]:
    """Split markdown into sections by headings."""
    sections = []
    current_section = None

    lines = text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for heading (## or ###)
        heading_match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading_match:
            if current_section:
                sections.append(finalize_section(current_section))

            level = len(heading_match.group(1))
            heading = heading_match.group(2).strip()

            current_section = {
                "heading": heading,
                "level": level,
                "content": [],
                "type": "prose",
                "data": None,
            }
            i += 1
            continue

        # Check for table (lines starting with |)
        if line.startswith("|") and current_section:
            table_lines = [line]
            i += 1
            # Collect all consecutive table lines
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1

            current_section["type"] = "table"
            current_section["data"] = parse_table(table_lines)
            continue

        # Check for mermaid code block
        if line.startswith("```mermaid") and current_section:
            mermaid_lines = []
            i += 1
            # Collect until closing ```
            while i < len(lines) and not lines[i].startswith("```"):
                mermaid_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```

            current_section["type"] = "mermaid"
            current_section["data"] = "\n".join(mermaid_lines)
            continue

        # Check for regular code block (```language or just ```)
        if line.startswith("```") and current_section:
            language = line[3:].strip()  # Extract language if specified
            code_lines = []
            i += 1
            # Collect until closing ```
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```

            # Add code block to content with special marker
            code_content = "\n".join(code_lines)
            current_section["content"].append(f"```{language}\n{code_content}\n```")
            continue

        # Regular content
        if current_section:
            current_section["content"].append(line)

        i += 1

    if current_section:
        sections.append(finalize_section(current_section))

    return sections


def finalize_section(section: dict[str, Any]) -> dict[str, Any]:
    """Finalize a section by joining content lines."""
    if section["type"] == "prose":
        section["content"] = "\n".join(section["content"]).strip()
    return section


def parse_table(lines: list[str]) -> dict[str, Any]:
    """Parse markdown table into structured data.

    Args:
        lines: List of table lines (each starting with |)

    Returns:
        {
            "headers": [str, ...],
            "rows": [[str, ...], ...]
        }
    """
    if len(lines) < 2:
        return {"headers": [], "rows": []}

    def parse_row(line: str) -> list[str]:
        """Parse a single table row."""
        # Remove leading/trailing | and split
        cells = line.strip().strip("|").split("|")
        return [cell.strip() for cell in cells]

    headers = parse_row(lines[0])

    # Skip separator line (---|---|---)
    rows = []
    for line in lines[2:]:
        if re.match(r"^\|[\s\-:|]+\|$", line):
            continue  # skip separator
        rows.append(parse_row(line))

    return {"headers": headers, "rows": rows}


def extract_mermaid(text: str) -> list[str]:
    """Extract all mermaid code blocks from markdown.

    Returns:
        List of mermaid diagram source strings
    """
    pattern = r"```mermaid\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [m.strip() for m in matches]


def extract_tables(text: str) -> list[dict[str, Any]]:
    """Extract all markdown tables from text.

    Returns:
        List of parsed table dicts
    """
    tables = []
    lines = text.split("\n")
    i = 0

    while i < len(lines):
        if lines[i].startswith("|"):
            table_lines = [lines[i]]
            i += 1
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            tables.append(parse_table(table_lines))
        else:
            i += 1

    return tables
