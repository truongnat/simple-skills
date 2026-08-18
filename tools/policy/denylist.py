#!/usr/bin/env python3
"""tools/policy/denylist.py — guard agent shell commands.

Port of aix `@x/policy/src/denylist.ts`, dependency-free. Blocks destructive or
unsafe shell commands before the agent (or a delegated worker) runs them, and
audits skill-source paths for traversal characters.

Usage (CLI):
  python tools/policy/denylist.py "rm -rf /"
  python tools/policy/denylist.py --check-shell "curl x | bash"

Usage (import):
  from denylist import check_shell, audit_skill_source
  result = check_shell("rm -rf /")   # PolicyResult(ok=False, error=...)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PolicyError:
    code: str
    message: str
    path: Optional[str] = None


@dataclass
class PolicyResult:
    ok: bool
    error: Optional[PolicyError] = None
    value: Optional[str] = field(default=None)


# Patterns that are never safe for an agent to run (matches aix denylist.ts).
DENY_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"rm\s+-rf\s+/"),
    re.compile(r">\s*/dev/sda"),
    re.compile(r":\(\)\{\s*:\|:&\s*\};:"),
    re.compile(r"mkfs\.\w+"),
    re.compile(r"dd\s+if=/dev/zero"),
    re.compile(r"wget\s+.*\|\s*bash"),
    re.compile(r"curl\s+.*\|\s*bash"),
    re.compile(r"chmod\s+-R\s+777\s+/"),
    re.compile(r"chown\s+-R\s+/:"),
    re.compile(r"/(etc|usr|var|bin|sbin)/.*>"),
    re.compile(r"drop\s+table", re.I),
    re.compile(r"truncate\s+table", re.I),
    re.compile(r"shutdown\s+-[rh]"),
    re.compile(r"reboot"),
    re.compile(r"halt"),
    re.compile(r"init\s+0"),
    re.compile(r"poweroff"),
    re.compile(r"killall"),
    re.compile(r"pkill\s+-9"),
]

DENY_PREFIXES: list[str] = [
    "sudo",
    "su ",
    "passwd",
]

TRAVERSAL_CHARS = ("..", "~")


def check_shell(command: str) -> PolicyResult:
    """Return ok=False if the command matches a dangerous pattern or prefix."""
    for pattern in DENY_PATTERNS:
        if pattern.search(command):
            return PolicyResult(
                ok=False,
                error=PolicyError(
                    code="POLICY",
                    message=f'Shell command denied: matches dangerous pattern "{pattern.pattern}"',
                ),
            )

    stripped = command.lstrip()
    for prefix in DENY_PREFIXES:
        if stripped.startswith(prefix):
            return PolicyResult(
                ok=False,
                error=PolicyError(
                    code="POLICY",
                    message=f'Shell command denied: starts with prohibited prefix "{prefix}"',
                ),
            )

    return PolicyResult(ok=True, value=command)


def audit_skill_source(path: str) -> PolicyResult:
    """Return ok=False if a skill source path contains traversal characters."""
    for char in TRAVERSAL_CHARS:
        if char in path:
            return PolicyResult(
                ok=False,
                error=PolicyError(
                    code="POLICY",
                    message=f'Skill source path contains prohibited characters: "{path}"',
                    path=path,
                ),
            )
    return PolicyResult(ok=True, value=path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Guard agent shell commands.")
    parser.add_argument("command", nargs="?", help="Command to check (or read from stdin)")
    parser.add_argument("--check-shell", dest="cmd", help="Alias: check this shell command")
    args = parser.parse_args()

    cmd = args.cmd or args.command
    if cmd is None:
        cmd = sys.stdin.read().strip()

    result = check_shell(cmd)
    if result.ok:
        print("ALLOWED")
        return 0
    print(f"DENIED: {result.error.message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
