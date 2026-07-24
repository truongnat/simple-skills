#!/usr/bin/env python3
"""Thin sub-agent dispatch helper (Phase 2 scaffold).

Enforces Rules gate before any worker spawn. Real CLI adapters are stubs:
prints a ready command template or refuses. Main brain remains authoritative.

Usage:
  python tools/session/delegate_worker.py --skill planning --cli codex --dry-run
  python tools/session/delegate_worker.py --skill execution --cli opencode --check-only
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
if str(SESSION_DIR) not in sys.path:
    sys.path.insert(0, str(SESSION_DIR))

from build_context import (  # noqa: E402
    build_pack,
    check_rules_block,
    find_root,
    resolve_session,
)

SUPPORTED = ("claude", "codex", "opencode", "cursor", "main")


def ensure_pack(root: Path, session: Path, skill: str, mission: str) -> Path:
    pack_text = build_pack(root, session, skill, mission)
    missing = check_rules_block(pack_text)
    if missing:
        raise SystemExit(
            "DELEGATE_REFUSED reason=rules_incomplete missing=" + ",".join(missing)
        )
    out = session / "CONTEXT_PACK.md"
    out.write_text(pack_text, encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--session", default=None)
    parser.add_argument("--skill", required=True)
    parser.add_argument(
        "--cli",
        default="main",
        help="Target worker id (claude|codex|opencode|cursor|main)",
    )
    parser.add_argument("--mission", default="")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build pack + print invoke template; do not spawn",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only validate/build pack with Rules gate",
    )
    args = parser.parse_args()
    root = args.root.resolve() if args.root else find_root(Path.cwd())
    session = resolve_session(root, args.session)
    cli = args.cli.strip().lower()
    if cli not in SUPPORTED:
        print(f"DELEGATE_REFUSED reason=unsupported_cli cli={cli}", file=sys.stderr)
        return 1

    try:
        pack_path = ensure_pack(root, session, args.skill, args.mission)
    except SystemExit as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"DELEGATE_PACK_OK path={pack_path}")

    if args.check_only or cli == "main":
        print("DELEGATE_FALLBACK_MAIN reason=check_only_or_cli_main")
        return 0

    binary = shutil.which(cli)
    if cli == "cursor" and not binary:
        binary = shutil.which("cursor-agent")
    if not binary:
        print(f"DELEGATE_REFUSED reason=cli_missing cli={cli} → fallback main")
        return 2

    rel_pack = pack_path.relative_to(root) if pack_path.is_relative_to(root) else pack_path
    template = (
        f"# Suggested invoke (human/main must approve)\n"
        f"# Attach CONTEXT_PACK and require Rules obedience.\n"
        f"{binary}  # open session with pack:\n"
        f"#   {rel_pack}\n"
        f"# After worker returns: validate_artifacts.py && lint_artifacts.py && "
        f"session.sh commit 'docs({args.skill}): worker {cli}'\n"
    )
    print("DELEGATE_READY")
    print(template)
    if args.dry_run:
        return 0

    print(
        "DELEGATE_SPAWN_SKIPPED reason=adapters_are_manual_approve_only "
        "(use --dry-run; main merges results)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
