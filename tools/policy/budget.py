#!/usr/bin/env python3
"""tools/policy/budget.py — budget & context hard-stop guard.

Port of aix `@x/core/src/budget.ts`, dependency-free. Tracks USD spend and
context tokens across agent/provider calls and hard-stops before a paid loop
runs away.

Usage (CLI):
  python tools/policy/budget.py check --usd-spent 9.5 --usd-limit 10
  python tools/policy/budget.py check --tokens 180000 --token-limit 200000
  python tools/policy/budget.py add --usd-spent 9.5 --usd 0.5 --tokens 4000

Usage (import):
  from budget import BudgetTracker
  b = BudgetTracker(usd_limit=10, token_context_limit=200_000)
  b.add_usage(usd=0.5, tokens=4000)
  result = b.check_hard_stop()   # PolicyResult; ok=False -> stop the loop
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PolicyError:
    code: str
    message: str


@dataclass
class PolicyResult:
    ok: bool
    error: Optional[PolicyError] = None
    warnings: list[str] = field(default_factory=list)


@dataclass
class BudgetState:
    usd_spent: float = 0.0
    usd_limit: float = 10.0
    usd_warn_threshold: float = 0.8
    tokens_in_phase: int = 0
    token_context_limit: int = 200_000


class BudgetTracker:
    """Tracks USD + token spend and exposes hard-stop / warning checks."""

    def __init__(
        self,
        usd_limit: float = 10.0,
        token_context_limit: int = 200_000,
        usd_warn_threshold: float = 0.8,
    ) -> None:
        self.state = BudgetState(
            usd_limit=usd_limit,
            token_context_limit=token_context_limit,
            usd_warn_threshold=usd_warn_threshold,
        )

    def add_usage(
        self,
        usd: float,
        tokens: int,
        prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
    ) -> BudgetState:
        p_tokens = prompt_tokens if prompt_tokens is not None else round(tokens * 0.8)
        c_tokens = completion_tokens if completion_tokens is not None else tokens - p_tokens
        s = self.state
        s.usd_spent += usd
        s.tokens_in_phase += tokens
        return s

    def check_hard_stop(self) -> PolicyResult:
        """ok=False means the loop MUST stop (budget or context limit hit)."""
        s = self.state
        if s.usd_spent >= s.usd_limit:
            return PolicyResult(
                ok=False,
                error=PolicyError(
                    code="BUDGET",
                    message=(
                        f"Budget hard-stop: ${s.usd_spent:.2f} spent of "
                        f"${s.usd_limit:.2f} limit"
                    ),
                ),
            )
        if s.tokens_in_phase >= s.token_context_limit:
            return PolicyResult(
                ok=False,
                error=PolicyError(
                    code="CONTEXT",
                    message=(
                        f"Context hard-stop: {s.tokens_in_phase} tokens used of "
                        f"{s.token_context_limit} limit"
                    ),
                ),
            )
        return PolicyResult(ok=True)

    def check_before_call(self) -> PolicyResult:
        """Warn before a call; ok=False + recoverable=False means cannot continue."""
        s = self.state
        result = PolicyResult(ok=True)

        usd_ratio = s.usd_spent / s.usd_limit if s.usd_limit else 0.0
        if usd_ratio >= 1:
            result.ok = False
            result.warnings.append(
                f"Budget exhausted: ${s.usd_spent:.2f} of ${s.usd_limit:.2f}. Cannot continue without reset."
            )
        elif usd_ratio >= s.usd_warn_threshold:
            result.warnings.append(
                f"Budget near limit: ${s.usd_spent:.2f} of ${s.usd_limit:.2f} "
                f"({usd_ratio * 100:.0f}%). Consider confirming before proceeding."
            )

        ctx_ratio = s.tokens_in_phase / s.token_context_limit if s.token_context_limit else 0.0
        if ctx_ratio >= 1:
            result.ok = False
            result.warnings.append(
                f"Context full: {s.tokens_in_phase} of {s.token_context_limit} tokens. "
                "Must compact or clear before continuing."
            )
        elif ctx_ratio >= 0.8:
            result.warnings.append(
                f"Context nearly full: {s.tokens_in_phase} of {s.token_context_limit} tokens "
                f"({ctx_ratio * 100:.0f}%). Consider compacting."
            )

        if result.warnings:
            result.ok = result.ok and not any("exhausted" in w or "Context full" in w for w in result.warnings)
        return result

    def should_compact(self) -> bool:
        ratio = self.state.tokens_in_phase / self.state.token_context_limit if self.state.token_context_limit else 0.0
        return ratio >= 0.8

    def snapshot(self) -> dict:
        s = self.state
        return {
            "usd_spent": round(s.usd_spent, 4),
            "usd_limit": s.usd_limit,
            "tokens_in_phase": s.tokens_in_phase,
            "token_context_limit": s.token_context_limit,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Budget/context hard-stop guard.")
    sub = parser.add_subparsers(dest="cmd")

    p_check = sub.add_parser("check")
    p_check.add_argument("--usd-spent", type=float, default=0.0)
    p_check.add_argument("--usd-limit", type=float, default=10.0)
    p_check.add_argument("--tokens", type=int, default=0)
    p_check.add_argument("--token-limit", type=int, default=200_000)

    p_add = sub.add_parser("add")
    p_add.add_argument("--usd-spent", type=float, default=0.0)
    p_add.add_argument("--usd", type=float, required=True)
    p_add.add_argument("--tokens", type=int, default=0)
    p_add.add_argument("--usd-limit", type=float, default=10.0)
    p_add.add_argument("--token-limit", type=int, default=200_000)

    args = parser.parse_args()

    if args.cmd == "add":
        b = BudgetTracker(usd_limit=args.usd_limit, token_context_limit=args.token_limit)
        b.state.usd_spent = args.usd_spent
        b.add_usage(usd=args.usd, tokens=args.tokens)
        print(json.dumps(b.snapshot(), indent=2))
        return 0

    b = BudgetTracker(usd_limit=args.usd_limit, token_context_limit=args.token_limit)
    b.state.usd_spent = args.usd_spent
    b.state.tokens_in_phase = args.tokens
    result = b.check_hard_stop()
    print(json.dumps({"ok": result.ok, "error": result.error.message if result.error else None}, indent=2))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
