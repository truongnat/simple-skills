#!/usr/bin/env python3
"""Check version consistency across the repo.

Verifies that:
  1. pyproject.toml version == src/simple_skills/__init__.py __version__
  2. (optional) git tag == pyproject version, when --expect-tag is given

Usage:
  python scripts/check_version.py [--expect-tag v0.4.0]

Exit code 0 on success, 1 on mismatch.
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
INIT = ROOT / "src" / "simple_skills" / "__init__.py"

VERSION_RE = re.compile(r"__version__\s*=\s*['\"]([^'\"]+)['\"]")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect-tag", help="Expected git tag (e.g. v0.4.0)")
    args = parser.parse_args()

    with PYPROJECT.open("rb") as f:
        pyproject_version = tomllib.load(f)["project"]["version"]

    init_text = INIT.read_text()
    m = VERSION_RE.search(init_text)
    if not m:
        print(f"ERROR: cannot find __version__ in {INIT}", file=sys.stderr)
        return 1
    init_version = m.group(1)

    errors: list[str] = []

    if pyproject_version != init_version:
        errors.append(
            f"pyproject.toml version {pyproject_version!r} != __init__.py version {init_version!r}"
        )

    if args.expect_tag:
        tag_version = args.expect_tag.lstrip("v")
        if tag_version != pyproject_version:
            errors.append(
                f"git tag {args.expect_tag!r} != pyproject.toml version {pyproject_version!r}"
            )

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(
            "Fix: bump pyproject.toml [project].version, src/simple_skills/__init__.py, and the git tag together.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: version {pyproject_version} consistent (pyproject == __init__"
          + (f" == tag {args.expect_tag}" if args.expect_tag else "") + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
