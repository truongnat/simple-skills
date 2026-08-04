#!/usr/bin/env python3
"""Find a BA session and launch the BA report server."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


BA_ARTIFACTS = [
    "BUSINESS_ANALYSIS.md",
    "USER_FLOW.md",
    "PRD.md",
    "BRD.md",
    "URD.md",
    "SPEC_SRS.md",
    "MODEL.md",
    "DISCOVER.md",
    "ROADMAP.md",
    "PRD_EPIC.md",
    "REQ_REVIEW.md",
    "TEST_PLAN.md",
    "TESTCASES.md",
    "DEFECT_LOG.md",
    "TEST_SUMMARY.md",
]


def latest_ba_session(sessions_dir: Path) -> Path | None:
    """Find most recent session with BA artifacts."""
    candidates = []
    for session in sessions_dir.iterdir():
        if not session.is_dir():
            continue
        if session.name.startswith("."):
            continue
        if any((session / artifact).is_file() for artifact in BA_ARTIFACTS):
            candidates.append(session)

    if not candidates:
        return None

    return max(candidates, key=lambda s: s.stat().st_mtime)


def resolve_session(
    value: Path | None,
    sessions_dir: Path,
) -> Path:
    """Resolve session path."""
    sessions_dir = sessions_dir.expanduser().resolve()

    if value is None:
        session = latest_ba_session(sessions_dir)
        if session is None:
            raise FileNotFoundError(
                f"no BA artifacts found under {sessions_dir}/<session>"
            )
        return session

    candidate = value.expanduser()
    if not candidate.exists() and len(candidate.parts) == 1:
        candidate = sessions_dir / candidate
    candidate = candidate.resolve()

    if not candidate.is_dir():
        raise FileNotFoundError(f"session does not exist: {candidate}")

    return candidate


def ba_report_server_path() -> Path:
    """Find server.py."""
    return Path(__file__).resolve().parent / "server.py"


def build_command(
    server: Path,
    sessions_dir: Path,
    host: str,
    port: int,
    open_browser: bool,
) -> list[str]:
    """Build server command."""
    command = [
        sys.executable,
        str(server),
        "--sessions-dir",
        str(sessions_dir),
        "--host",
        host,
        "--port",
        str(port),
    ]
    if open_browser:
        command.append("--open")
    return command


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser."""
    parser = argparse.ArgumentParser(
        description="Serve BA reports with minimal path typing."
    )
    parser.add_argument(
        "session",
        nargs="?",
        type=Path,
        help="Session directory or name. Defaults to latest with BA artifacts.",
    )
    parser.add_argument(
        "--sessions-dir",
        type=Path,
        default=Path(".agent-work/sessions"),
        help="Session parent used for lookup (default: .agent-work/sessions).",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Do not open the page in the default browser.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    args = build_parser().parse_args(argv)

    try:
        session = resolve_session(args.session, args.sessions_dir)
    except (FileNotFoundError, OSError) as exc:
        print(f"ba-report-serve: {exc}", file=sys.stderr)
        return 1

    server = ba_report_server_path()
    if not server.is_file():
        print(f"ba-report-serve: server not found: {server}", file=sys.stderr)
        return 1

    command = build_command(
        server=server,
        sessions_dir=args.sessions_dir.expanduser().resolve(),
        host=args.host,
        port=args.port,
        open_browser=not args.no_open,
    )

    print(f"Session  {session}", flush=True)
    try:
        return subprocess.call(command)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
