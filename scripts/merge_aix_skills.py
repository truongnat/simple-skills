#!/usr/bin/env python3
"""Phase 1 merge: vendor aix skills into this repo as third-party skills.

Copies aix `content/skills/<name>` directories into `skills/`, normalizes their
SKILL.md frontmatter to the simple-skills format (name + description required),
adds `aliases:` for plain-name lookups (e.g. `docker` -> `docker-pro`), and
registers every copied skill in docs/conventions/THIRD_PARTY_SKILLS.md so the
repo validator accepts them as vendored third-party skills.

Skips:
  - planning-pro / business-analysis-pro  (simple-skills has its own step workflows)
  - CONTRIBUTING.md / _shared             (not skills)

Usage:
  python scripts/merge_aix_skills.py [--aix-root /path/to/aix] [--commit HASH]
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
THIRD_PARTY = ROOT / "docs" / "conventions" / "THIRD_PARTY_SKILLS.md"

SKIP = {"planning-pro", "business-analysis-pro", "CONTRIBUTING.md", "_shared"}
AIX_SOURCE_REL = "content/skills"
NAME_RE = re.compile(r"^name:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*\S+", re.MULTILINE)


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return None if end < 0 else text[4:end]


def add_alias(frontmatter_text: str, alias: str) -> str:
    """Insert `aliases: [alias]` before the closing --- if not already present."""
    if re.search(r"^aliases:", frontmatter_text, re.MULTILINE):
        return frontmatter_text
    return frontmatter_text.rstrip() + f"\naliases: [{alias}]\n"


def plain_alias(name: str, existing_dirs: set[str]) -> str | None:
    """docker-pro -> docker (only when docker is not already a skill dir)."""
    if not name.endswith("-pro"):
        return None
    plain = name[: -len("-pro")]
    if plain in existing_dirs or plain in SKIP:
        return None
    return plain


def copy_skill(src: Path, dst: Path, alias: str | None) -> tuple[bool, str]:
    if dst.exists():
        return False, f"skip (exists): {dst.name}"
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".venv", "__pycache__"))
    skill_md = dst / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        return False, f"FAIL (frontmatter): {dst.name}"
    name_m = NAME_RE.search(meta)
    if not name_m or name_m.group(1).strip() != dst.name:
        return False, f"FAIL (name mismatch): {dst.name}"
    if not DESC_RE.search(meta):
        return False, f"FAIL (missing description): {dst.name}"
    if alias:
        new_meta = add_alias(meta, alias)
        new_text = text.replace(meta, new_meta, 1)
        skill_md.write_text(new_text, encoding="utf-8")
        return True, f"copied +alias {alias}: {dst.name}"
    return True, f"copied: {dst.name}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aix-root", type=Path, default=Path("/tmp/aix-repo"))
    parser.add_argument("--commit", default="26381fc6b35fff7fcf312313649d7c379c97fc24")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    src_root = args.aix_root / AIX_SOURCE_REL
    if not src_root.is_dir():
        print(f"ERROR: {src_root} not found", file=sys.stderr)
        return 2

    existing_dirs = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    aix_names = sorted(p.name for p in src_root.iterdir() if p.is_dir())
    to_copy = [n for n in aix_names if n not in SKIP]
    copied: list[str] = []
    skipped: list[str] = []
    failed: list[str] = []

    for name in to_copy:
        dst = SKILLS / name
        alias = plain_alias(name, existing_dirs)
        if args.dry_run:
            copied.append(f"{name}" + (f" (+alias {alias})" if alias else ""))
            continue
        ok, msg = copy_skill(src_root / name, dst, alias)
        (copied if ok else (skipped if msg.startswith("skip") else failed)).append(msg)
        if not ok:
            existing_dirs.add(name)

    if not args.dry_run:
        # Register copied skills in THIRD_PARTY_SKILLS.md (validator requires `name`).
        registered = {n for n in to_copy if (SKILLS / n).is_dir()}
        update_third_party_doc(registered, args.commit)

    print(f"aix source: {src_root}")
    print(f"total aix skills: {len(aix_names)} | to copy: {len(to_copy)} | skipped by rule: {len(aix_names) - len(to_copy)}")
    print(f"copied: {len(copied)}")
    for line in copied:
        print(f"  + {line}")
    if skipped:
        print(f"skipped (already exist): {len(skipped)}")
        for line in skipped:
            print(f"  = {line}")
    if failed:
        print(f"FAILED: {len(failed)}", file=sys.stderr)
        for line in failed:
            print(f"  ! {line}", file=sys.stderr)
        return 1
    print("OK")
    return 0


def update_third_party_doc(skill_names: set[str], commit: str) -> None:
    """Add/refresh the aix section of THIRD_PARTY_SKILLS.md with `name` mentions."""
    text = THIRD_PARTY.read_text(encoding="utf-8")
    marker = "<!-- AIX_VENDORED_SKILLS -->"
    names = sorted(skill_names)
    # Chunk into rows of 12 for readability.
    rows = [", ".join(f"`{n}`" for n in names[i : i + 12]) for i in range(0, len(names), 12)]
    lines = [
        marker,
        "",
        "| Category | Skills | Source | Revision | License |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| AI engineering | {row} | [truongnat/aix](https://github.com/truongnat/aix) | `{commit}` | MIT |")
    lines.append("")
    block = "\n".join(lines)

    if marker in text:
        # Replace between the previous heading and the marker block end.
        start = text.find("### Vendored from aix")
        if start < 0:
            start = text.find(marker)
        end = text.find(marker, start) + len(marker)
        # extend to end of the table block
        tail = text[end:]
        next_heading = re.search(r"\n## ", tail)
        if next_heading:
            end += next_heading.start()
        else:
            end = len(text.rstrip())
        new_text = text[:start] + "### Vendored from aix\n\n" + block + "\n" + tail[next_heading.start() if next_heading else 0 :]
    else:
        new_text = text.rstrip() + "\n\n" + "### Vendored from aix\n\n" + block + "\n"
    THIRD_PARTY.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
