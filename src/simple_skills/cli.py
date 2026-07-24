"""sk — Simple Skills installer CLI.

Usage:
  sk install [--agents-mode MODE] [--profile NAME]
  sk uninstall [--yes] [--keep-settings] [--purge-work]
  sk doctor
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

COMMANDS = ("install", "uninstall", "doctor")


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
    """Prefer a checkout that contains install.sh + docs/AGENTS.md."""
    env = os.environ.get("SIMPLE_SKILLS_ROOT")
    if env:
        root = Path(env).expanduser().resolve()
        cand = root / INSTALL_SH
        if cand.is_file() and (root / "docs" / "AGENTS.md").is_file():
            return cand

    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        cand = parent / INSTALL_SH
        if cand.is_file() and (parent / "docs" / "AGENTS.md").is_file():
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
    """Map sk flags to install.ps1 parameters."""
    out: list[str] = ["-Command", command]
    i = 0
    while i < len(rest):
        arg = rest[i]
        if arg in ("--agents-mode",) and i + 1 < len(rest):
            out.extend(["-AgentsMode", rest[i + 1]])
            i += 2
            continue
        if arg in ("--profile",) and i + 1 < len(rest):
            out.extend(["-Profile", rest[i + 1]])
            i += 2
            continue
        if arg in ("--yes", "-y"):
            out.append("-Yes")
            i += 1
            continue
        if arg == "--keep-settings":
            out.append("-KeepSettings")
            i += 1
            continue
        if arg == "--purge-work":
            out.append("-PurgeWork")
            i += 1
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
        if ps1 is None:
            tmp = Path(tempfile.mkdtemp(prefix="simple-skills-"))
            ps1 = tmp / INSTALL_PS1
            _download(_raw_url(INSTALL_PS1), ps1)
        argv = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ps1),
            *_powershell_argv(command, rest),
        ]
        return subprocess.call(argv)

    if local is not None:
        return subprocess.call(["bash", str(local), *_bash_argv(command, rest)])

    bash = shutil.which("bash")
    if not bash:
        raise SystemExit(
            "Error: bash not found. Install Git Bash/WSL, or set SIMPLE_SKILLS_SHELL=powershell."
        )

    tmp = Path(tempfile.mkdtemp(prefix="simple-skills-"))
    script = tmp / INSTALL_SH
    _download(_raw_url(INSTALL_SH), script)
    return subprocess.call([bash, str(script), *_bash_argv(command, rest)])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sk",
        description="Simple Skills — install and manage the agent kit in the current project.",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"sk {__version__}",
    )
    sub = parser.add_subparsers(dest="command")

    p_install = sub.add_parser("install", help="Install/update the kit into .agents/")
    p_install.add_argument(
        "--agents-mode",
        choices=("prompt", "replace", "skip"),
        default=None,
        help="How to handle existing root AGENTS.md",
    )
    p_install.add_argument(
        "--profile",
        default=None,
        help="core (default) | office | frontend | backend | all",
    )

    p_uninstall = sub.add_parser("uninstall", help="Remove the kit from this project")
    p_uninstall.add_argument("--yes", "-y", action="store_true", help="Do not prompt")
    p_uninstall.add_argument(
        "--keep-settings",
        action="store_true",
        help="Keep .agents/settings.yaml",
    )
    p_uninstall.add_argument(
        "--purge-work",
        action="store_true",
        help="Also delete .agent-work/",
    )

    sub.add_parser("doctor", help="Check whether this project looks healthy")
    return parser


def _rest_from_namespace(command: str, ns: argparse.Namespace) -> list[str]:
    rest: list[str] = []
    if command == "install":
        if ns.agents_mode:
            rest.extend(["--agents-mode", ns.agents_mode])
        if ns.profile:
            rest.extend(["--profile", ns.profile])
    elif command == "uninstall":
        if ns.yes:
            rest.append("--yes")
        if ns.keep_settings:
            rest.append("--keep-settings")
        if ns.purge_work:
            rest.append("--purge-work")
    return rest


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Bare `sk` → install (same as curl | bash default).
    if not argv:
        return run_installer("install", [])

    if argv[0] in ("-V", "--version"):
        print(f"sk {__version__}")
        return 0
    if argv[0] in ("-h", "--help"):
        build_parser().print_help()
        return 0

    parser = build_parser()
    if argv[0] not in COMMANDS and not argv[0].startswith("-"):
        parser.error(f"unknown command: {argv[0]}")

    if argv[0] not in COMMANDS:
        ns = parser.parse_args(["install", *argv])
    else:
        ns = parser.parse_args(argv)

    command = ns.command or "install"
    return run_installer(command, _rest_from_namespace(command, ns))


if __name__ == "__main__":
    raise SystemExit(main())
