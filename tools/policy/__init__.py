#!/usr/bin/env python3
"""tools/policy/__init__.py — unified policy surface.

Port of aix `@x/policy` (redaction + shell denylist) and `@x/core` budget
tracker. Importable as a package when tools/ is on sys.path, or run each
module directly as a CLI.

  from policy import redact, check_shell, audit_skill_source, BudgetTracker
"""

from __future__ import annotations

from budget import BudgetTracker, BudgetState  # noqa: F401
from denylist import PolicyError, PolicyResult, audit_skill_source, check_shell  # noqa: F401
from redact import Finding, RedactResult, redact  # noqa: F401

__all__ = [
    "BudgetTracker",
    "BudgetState",
    "Finding",
    "PolicyError",
    "PolicyResult",
    "RedactResult",
    "audit_skill_source",
    "check_shell",
    "redact",
]
