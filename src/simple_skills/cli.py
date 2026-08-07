"""sk — Simple Skills installer CLI.

Usage:
  sk install [--agent NAME]
  sk update [--agent NAME]
  sk doctor [--agent NAME]
  sk --help
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

from simple_skills import __version__

DEFAULT_OWNER = "truongnat"
DEFAULT_REPO = "simple-skills"
DEFAULT_BRANCH = "main"
INSTALL_SH = "install.sh"
INSTALL_PS1 = "install.ps1"

COMMANDS = ("install", "update", "doctor")

def _repo_meta() -> tuple[str, str, str]:
    return (
        os.environ.get("SIMPLE_SKILLS_OWNER", DEFAULT_OWNER),
        os.environ.get("SIMPLE_SKILLS_REPO", DEFAULT_REPO),
        os.environ.get("SIMPLE_SKILLS_BRANCH", DEFAULT_BRANCH),
    )

def _raw_url(filename: str) -> str:
    owner, repo, branch = _repo_meta()
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filename}"

def find_local_installer() -> Path | None:
    env = os.environ.get("SIMPLE_SKILLS_ROOT")
    if env:
        root = Path(env).expanduser().resolve()
        cand = root / INSTALL_SH
        if cand.is_file() and (root / "docs" / "AGENTS.md").is_file():
            return cand
        raise SystemExit(f"Error: SIMPLE_SKILLS_ROOT={root} missing {INSTALL_SH} or docs/AGENTS.md")

    cwd = Path.cwd().resolve()
    cand = cwd / INSTALL_SH
    if cand.is_file() and (cwd / "docs" / "AGENTS.md").is_file():
        return cand
    return None

def _download(url: str, dest: Path) -> None:
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            dest.write_bytes(resp.read())
    except urllib.error.URLError as exc:
        raise SystemExit(f"Error: failed to download {url}: {exc}") from exc

def _prefer_powershell() -> bool:
    if os.environ.get("SIMPLE_SKILLS_SHELL", "").lower() == "bash":
        return False
    if os.environ.get("SIMPLE_SKILLS_SHELL", "").lower() == "powershell":
        return True
    return sys.platform == "win32" and shutil.which("powershell") is not None

def _bash_argv(command: str, rest: list[str]) -> list[str]:
    return [command, *rest]

def _powershell_argv(command: str, rest: list[str]) -> list[str]:
    out: list[str] = ["-Command", command]
    i = 0
    while i < len(rest):
        arg = rest[i]
        if arg == "--agent" and i + 1 < len(rest):
            out.extend(["-AgentName", rest[i + 1]])
            i += 2
            continue
        if arg in ("-h", "--help"):
            out.append("-?")
            i += 1
            continue
        raise SystemExit(f"Error: unsupported option for PowerShell path: {arg}")
    return out

def run_installer(command: str, rest: list[str]) -> int:
    local = find_local_installer()

    if _prefer_powershell():
        ps1: Path | None = None
        if local is not None:
            cand = local.parent / INSTALL_PS1
            if cand.is_file():
                ps1 = cand
        if ps1 is not None:
            argv = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ps1), *_powershell_argv(command, rest)]
            return subprocess.call(argv)
        with tempfile.TemporaryDirectory(prefix="simple-skills-") as tmp:
            ps1 = Path(tmp) / INSTALL_PS1
            _download(_raw_url(INSTALL_PS1), ps1)
            argv = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ps1), *_powershell_argv(command, rest)]
            return subprocess.call(argv)

    if local is not None:
        return subprocess.call(["bash", str(local), *_bash_argv(command, rest)])

    bash = shutil.which("bash")
    if not bash:
        raise SystemExit("Error: bash not found. Install Git Bash/WSL, or set SIMPLE_SKILLS_SHELL=powershell.")

    with tempfile.TemporaryDirectory(prefix="simple-skills-") as tmp:
        script = Path(tmp) / INSTALL_SH
        _download(_raw_url(INSTALL_SH), script)
        return subprocess.call([bash, str(script), *_bash_argv(command, rest)])

def print_help():
    help_text = f"""
\033[1m\033[96msk\033[0m — \033[1mSimple Skills\033[0m installer CLI.
\033[90mVersion: {__version__}\033[0m

\033[1m\033[93mUSAGE\033[0m
  \033[92msk\033[0m \033[96minstall\033[0m [--agent NAME]
  \033[92msk\033[0m \033[96mupdate\033[0m [--agent NAME]
  \033[92msk\033[0m \033[96mdoctor\033[0m [--agent NAME]

\033[1m\033[93mCOMMANDS\033[0m
  \033[96minstall\033[0m     Install all skills (replaces existing directory)
  \033[96mupdate\033[0m      Update own skills without deleting custom ones
  \033[96mdoctor\033[0m      Check whether this project looks healthy

\033[1m\033[93mOPTIONS\033[0m
  \033[92m--agent\033[0m     Agent name to install/update into (e.g. \033[96mclaude\033[0m -> \033[90m.claude\033[0m)
              [default: \033[1magents\033[0m]
  \033[92m-h, --help\033[0m  Show this help message and exit
  \033[92m-V, --version\033[0m Show version
"""
    print(help_text)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-V", "--version", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    sub = parser.add_subparsers(dest="command")

    p_install = sub.add_parser("install")
    p_install.add_argument("--agent", default="agents")

    p_update = sub.add_parser("update")
    p_update.add_argument("--agent", default="agents")

    p_doctor = sub.add_parser("doctor")
    p_doctor.add_argument("--agent", default="agents")
    return parser

def _rest_from_namespace(command: str, ns: argparse.Namespace) -> list[str]:
    rest: list[str] = []
    if getattr(ns, "agent", None):
        rest.extend(["--agent", ns.agent])
    return rest

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return run_installer("install", [])

    if argv[0] in ("-V", "--version"):
        print(f"sk {__version__}")
        return 0
    if argv[0] in ("-h", "--help") or (len(argv) > 1 and argv[1] in ("-h", "--help")):
        print_help()
        return 0

    parser = build_parser()
    if argv[0] not in COMMANDS and not argv[0].startswith("-"):
        print(f"\033[91mError: unknown command: {argv[0]}\033[0m")
        print_help()
        return 2

    if argv[0] not in COMMANDS:
        ns = parser.parse_args(["install", *argv])
    else:
        ns = parser.parse_args(argv)

    command = ns.command or "install"
    return run_installer(command, _rest_from_namespace(command, ns))

if __name__ == "__main__":
    raise SystemExit(main())
