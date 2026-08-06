#!/usr/bin/env python3
"""Shared, dependency-free settings.yaml reader for session tooling.

Single source of truth for resolving the Work layer directory name
(``rules.agent_work.location``, default ``.agent-work``) so every tool under
tools/session/ (and the installed .agents/tools/session/ copy) agrees with
session.sh on where sessions/memory live. Existing session data is never
moved automatically when the setting changes — see docs/policy/AGENT_WORK.md.
"""

from __future__ import annotations

from pathlib import Path

DEFAULT_WORK_DIR = ".agent-work"


def settings_path(root: Path) -> Path | None:
    for rel in (".agents/settings.yaml", "docs/config/settings.yaml"):
        path = root / rel
        if path.is_file():
            return path
    return None


def yaml_get(text: str, dotted: str, default: str) -> str:
    """Read a nested scalar from lean settings.yaml without a YAML dependency."""
    parts = dotted.split(".")
    lines = text.splitlines()
    if len(parts) == 1:
        key = parts[0]
        for line in lines:
            if line.startswith((" ", "\t")) or line.lstrip().startswith("#"):
                continue
            if ":" not in line:
                continue
            k, _, rest = line.partition(":")
            if k.strip() == key:
                val = rest.strip().strip("\"'")
                return val if val else default
        return default

    # Walk nested mapping by indentation (expects parts like rules.branch.mode).
    want = list(parts)
    idx = 0
    parent_indent = -1
    for line in lines:
        raw = line.rstrip()
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent < parent_indent and idx > 0:
            # Left the current parent block without finding the leaf.
            return default
        if ":" not in raw:
            continue
        key, _, rest = raw.lstrip().partition(":")
        key = key.strip()
        rest = rest.strip().strip("\"'")
        if idx < len(want) and key == want[idx]:
            if idx == len(want) - 1:
                return rest if rest else default
            # Enter child block
            parent_indent = indent
            idx += 1
            continue
        if idx > 0 and indent <= parent_indent and key != want[idx]:
            # Sibling at/above parent — stop if we already entered this level
            if indent < parent_indent or (indent == parent_indent and idx > 0):
                # Only reset when we've left the branch entirely
                if indent < parent_indent:
                    return default
    return default


def work_dir_name(root: Path) -> str:
    """Resolve rules.agent_work.location (default .agent-work), no trailing slash."""
    path = settings_path(root)
    text = path.read_text(encoding="utf-8") if path else ""
    return yaml_get(text, "rules.agent_work.location", DEFAULT_WORK_DIR).rstrip("/") or DEFAULT_WORK_DIR
