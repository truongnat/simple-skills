#!/usr/bin/env python3
"""Local BA report server: serve HTML reports from session artifacts.

Stdlib only. Serves parsed BA markdown as styled HTML.
"""

from __future__ import annotations

import argparse
import json
import sys
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

# Support both package import and direct execution
try:
    from .parser import parse_ba_markdown
    from .renderer import render_report
except ImportError:
    # Direct execution
    sys.path.insert(0, str(Path(__file__).parent))
    from parser import parse_ba_markdown
    from renderer import render_report


BA_REPORT_CSS = "ba-report.css"
BA_REPORT_JS = "ba-report.js"
MAX_BODY_BYTES = 64 * 1024

BA_ARTIFACTS = [
    "DISCUSSION.md",
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
]


class BAReportHandler(BaseHTTPRequestHandler):
    """HTTP handler for BA reports."""

    def __init__(
        self,
        *args,
        sessions_dir: Path,
        tool_dir: Path,
        **kwargs,
    ):
        self.sessions_dir = sessions_dir
        self.tool_dir = tool_dir
        super().__init__(*args, **kwargs)

    def do_GET(self) -> None:
        """Route GET requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        # API endpoints
        if path == "/api/health":
            self._send_json({"status": "ok", "tool": "ba-report"})
            return

        if path == "/api/sessions":
            sessions = self._find_sessions()
            self._send_json({"sessions": [s.name for s in sessions]})
            return

        # Static assets
        if path == f"/{BA_REPORT_CSS}":
            self._serve_file(self.tool_dir / BA_REPORT_CSS, "text/css")
            return

        if path == f"/{BA_REPORT_JS}":
            self._serve_file(self.tool_dir / BA_REPORT_JS, "application/javascript")
            return

        # Session list (root)
        if path == "/" or path == "":
            self._serve_session_list()
            return

        # Session report
        if path.startswith("/"):
            session_name = path.strip("/")
            session_path = self.sessions_dir / session_name
            if session_path.is_dir():
                self._serve_session_report(session_path)
                return

        self._send_error(HTTPStatus.NOT_FOUND, "Not found")

    def _find_sessions(self) -> list[Path]:
        """Find all sessions with BA artifacts."""
        sessions = []
        if not self.sessions_dir.is_dir():
            return sessions

        for session in self.sessions_dir.iterdir():
            if not session.is_dir():
                continue
            if session.name.startswith("."):
                continue
            # Check if session has any BA artifacts
            if any((session / artifact).is_file() for artifact in BA_ARTIFACTS):
                sessions.append(session)

        return sorted(sessions, key=lambda s: s.stat().st_mtime, reverse=True)

    def _serve_session_list(self) -> None:
        """Serve HTML page listing all sessions."""
        sessions = self._find_sessions()

        if not sessions:
            html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>BA Reports</title>
  <link rel="stylesheet" href="/ba-report.css">
</head>
<body class="ss-page">
  <a class="ss-skip" href="#main">Skip to content</a>
  <header class="ss-header">
    <div class="ss-header-inner">
      <p class="ss-eyebrow">Simple Skills</p>
      <h1>BA Reports</h1>
    </div>
  </header>
  <main id="main" class="ss-main">
    <div class="ss-card">
      <h2>No sessions found</h2>
      <p class="ss-prose">No sessions with BA artifacts found. Create a session and run BA skills to generate artifacts.</p>
    </div>
  </main>
  <footer class="ss-footer">
    <div class="ss-footer-inner"><p>BA Report</p></div>
  </footer>
</body>
</html>"""
            self._send_html(html)
            return

        links = "\n".join(
            f'      <li><a href="/{s.name}">{s.name}</a></li>' for s in sessions
        )
        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>BA Reports</title>
  <link rel="stylesheet" href="/ba-report.css">
</head>
<body class="ss-page">
  <a class="ss-skip" href="#main">Skip to content</a>
  <header class="ss-header">
    <div class="ss-header-inner">
      <p class="ss-eyebrow">Simple Skills</p>
      <h1>BA Reports</h1>
      <p class="ss-prose">Sessions with BA artifacts:</p>
    </div>
  </header>
  <main id="main" class="ss-main">
    <div class="ss-card">
      <h2>Sessions</h2>
      <ul>
{links}
      </ul>
    </div>
  </main>
  <footer class="ss-footer">
    <div class="ss-footer-inner"><p>BA Report</p></div>
  </footer>
</body>
</html>"""
        self._send_html(html)

    def _serve_session_report(self, session: Path) -> None:
        """Serve full BA report for a session."""
        artifacts = {}

        for artifact_name in BA_ARTIFACTS:
            artifact_path = session / artifact_name
            if not artifact_path.is_file():
                continue

            text = artifact_path.read_text(encoding="utf-8")
            parsed = parse_ba_markdown(text)
            artifacts[artifact_name] = parsed

        if not artifacts:
            self._send_error(HTTPStatus.NOT_FOUND, "No BA artifacts in session")
            return

        html = render_report(artifacts, session.name)
        self._send_html(html)

    def _serve_file(self, path: Path, content_type: str) -> None:
        """Serve a static file."""
        if not path.is_file():
            self._send_error(HTTPStatus.NOT_FOUND, f"File not found: {path.name}")
            return

        content = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_html(self, html: str) -> None:
        """Send HTML response."""
        content = html.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_json(self, data: dict) -> None:
        """Send JSON response."""
        content = json.dumps(data).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_error(self, code: HTTPStatus, message: str) -> None:
        """Send error response."""
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format: str, *args) -> None:
        """Suppress default logging."""
        pass


def run_server(
    sessions_dir: Path,
    tool_dir: Path,
    host: str = "127.0.0.1",
    port: int = 8766,
    open_browser: bool = False,
) -> None:
    """Run the BA report server."""
    handler = lambda *args, **kwargs: BAReportHandler(
        *args,
        sessions_dir=sessions_dir,
        tool_dir=tool_dir,
        **kwargs,
    )

    server = ThreadingHTTPServer((host, port), handler)
    url = f"http://{host}:{port}"
    print(f"BA Report Server: {url}")

    if open_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser."""
    parser = argparse.ArgumentParser(
        description="Serve BA reports from session artifacts."
    )
    parser.add_argument(
        "--sessions-dir",
        type=Path,
        default=Path(".agent-work/sessions"),
        help="Session parent directory (default: .agent-work/sessions).",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1).")
    parser.add_argument("--port", type=int, default=8766, help="Port to bind (default: 8766).")
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open browser automatically.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    args = build_parser().parse_args(argv)

    sessions_dir = args.sessions_dir.expanduser().resolve()
    if not sessions_dir.is_dir():
        print(f"ba-report: sessions directory not found: {sessions_dir}", file=sys.stderr)
        return 1

    tool_dir = Path(__file__).resolve().parent

    try:
        run_server(
            sessions_dir=sessions_dir,
            tool_dir=tool_dir,
            host=args.host,
            port=args.port,
            open_browser=args.open,
        )
        return 0
    except Exception as exc:
        print(f"ba-report: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
