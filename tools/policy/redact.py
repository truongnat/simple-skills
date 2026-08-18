#!/usr/bin/env python3
"""tools/policy/redact.py — secret/PII redaction at the boundary.

Port of aix `@x/policy/src/redact.ts`, dependency-free. Redacts secrets and PII
from arbitrary text (session logs, artifacts, provider error bodies) BEFORE they
hit disk or leave the machine.

Usage (CLI):
  python tools/policy/redact.py < file.txt
  echo "key=abc123... token=..." | python tools/policy/redact.py

Usage (import):
  from redact import redact
  result = redact(text)
  result.clean      # redacted text (secrets replaced with '••••')
  result.findings   # list of Finding(type, subtype, span)
"""

from __future__ import annotations

import re
from dataclasses import dataclass

REDACT_REPLACEMENT = "••••"


@dataclass(frozen=True)
class Finding:
    type: str  # 'secret' | 'pii'
    subtype: str
    span: tuple[int, int]


@dataclass(frozen=True)
class RedactResult:
    clean: str
    findings: list[Finding]


# (type, subtype, regex) — ordered; later patterns run on already-redacted text.
PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    ("secret", "api-key", re.compile(r"(?:api[_-]?key|apikey|api[_-]?secret)[=:]\s*['\"]?([a-zA-Z0-9_\-]{16,64})['\"]?", re.I)),
    ("secret", "bearer-token", re.compile(r"(?:Bearer\s+)([a-zA-Z0-9_\-.\+=]{20,2048})")),
    ("secret", "jwt", re.compile(r"eyJ[a-zA-Z0-9_\-]+\.eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+")),
    ("secret", "aws-key", re.compile(r"(?:AKIA|ASIA)[a-zA-Z0-9_\-]{16,}")),
    ("secret", "github-token", re.compile(r"gh[pousr]_[a-zA-Z0-9_\-]{36,}")),
    ("secret", "npm-token", re.compile(r"npm_[a-zA-Z0-9_\-]{36,}")),
    ("secret", "slack-token", re.compile(r"xox[baprs]-[0-9a-zA-Z\-]{10,}")),
    ("secret", "ssh-key", re.compile(r"-----BEGIN\s+(?:(?:RSA|DSA|EC|OPENSSH|PGP)\s+)?PRIVATE\s+KEY(?:-----| BLOCK-----)[\s\S]+?-----END\s+(?:(?:RSA|DSA|EC|OPENSSH|PGP)\s+)?PRIVATE\s+KEY(?:-----| BLOCK-----)")),
    ("secret", "pg-connection", re.compile(r"postgres(?:ql)?://[^:]+:[^@]+@[^\s]+")),
    ("secret", "redis-connection", re.compile(r"redis://[^:]+:[^@]+@[^\s]+")),
    ("secret", "mongo-connection", re.compile(r"mongodb(?:\+srv)?://[^:]+:[^@]+@[^\s]+")),
    ("secret", "generic-password", re.compile(r"password[=:]\s*['\"]?([^'\"\s]{6,})['\"]?", re.I)),
    ("secret", "generic-token", re.compile(r"token[=:]\s*['\"]?([a-zA-Z0-9_\-\.]{16,})['\"]?", re.I)),
    ("secret", "private-key", re.compile(r"private[_-]?key[=:]\s*['\"]?([a-zA-Z0-9_\-+\/=]{16,})['\"]?", re.I)),
    ("pii", "email", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("pii", "ip-address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("pii", "phone", re.compile(r"\b\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b")),
    ("pii", "ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("pii", "credit-card", re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b")),
]


def redact(input_text: str) -> RedactResult:
    """Return text with secrets/PII replaced by '••••' plus all findings."""
    clean = input_text
    all_findings: list[Finding] = []

    for ftype, subtype, pattern in PATTERNS:
        matches: list[Finding] = []
        for m in pattern.finditer(clean):
            matches.append(Finding(ftype, subtype, (m.start(), m.end())))
        all_findings.extend(matches)
        clean = pattern.sub(REDACT_REPLACEMENT, clean)

    return RedactResult(clean=clean, findings=all_findings)


def redact_file(path: str | None = None, text: str | None = None) -> RedactResult:
    """Convenience: redact a file's contents (in place only if --write given)."""
    if text is None and path is not None:
        text = open(path, encoding="utf-8", errors="replace").read()
    if text is None:
        text = ""
    return redact(text)


def main() -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Redact secrets/PII from stdin or a file.")
    parser.add_argument("file", nargs="?", help="Input file (default: stdin)")
    parser.add_argument("--write", action="store_true", help="Overwrite the input file with the redacted text")
    parser.add_argument("--report", action="store_true", help="Print findings summary to stderr")
    args = parser.parse_args()

    text = open(args.file, encoding="utf-8", errors="replace").read() if args.file else sys.stdin.read()
    result = redact(text)

    if args.file and args.write:
        with open(args.file, "w", encoding="utf-8") as f:
            f.write(result.clean)

    sys.stdout.write(result.clean)
    if args.report:
        counts: dict[tuple[str, str], int] = {}
        for f in result.findings:
            counts[(f.type, f.subtype)] = counts.get((f.type, f.subtype), 0) + 1
        for (ftype, subtype), n in sorted(counts.items()):
            print(f"[{ftype}/{subtype}] {n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
