"""sk — Simple Skills installer CLI.

Usage:
  sk install [--agent NAME] [--provider NAME]
  sk update [--agent NAME] [--provider NAME]
  sk compile --provider NAME [--skills-root DIR] [--target DIR]
  sk status [--agent NAME]
  sk validate [--agent NAME]
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

COMMANDS = ("install", "update", "compile", "status", "validate", "doctor")
PROVIDERS = ("claude", "cursor", "codex", "gemini")

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

def find_provider_compiler() -> Path | None:
    """Locate tools/providers/compile.py: repo checkout, cwd, or installed kit."""
    candidates = [
        Path(__file__).resolve().parents[2] / "tools" / "providers" / "compile.py",
        Path.cwd().resolve() / "tools" / "providers" / "compile.py",
        Path.cwd().resolve() / ".agents" / "tools" / "providers" / "compile.py",
    ]
    for cand in candidates:
        if cand.is_file():
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
  \033[92msk\033[0m \033[96minstall\033[0m [--agent NAME] [--provider NAME]
  \033[92msk\033[0m \033[96mupdate\033[0m [--agent NAME] [--provider NAME]
  \033[92msk\033[0m \033[96mcompile\033[0m --provider NAME [--skills-root DIR] [--target DIR]
  \033[92msk\033[0m \033[96mstatus\033[0m [--agent NAME]
  \033[92msk\033[0m \033[96mvalidate\033[0m [--agent NAME]
  \033[92msk\033[0m \033[96mdoctor\033[0m [--agent NAME]

\033[1m\033[93mCOMMANDS\033[0m
  \033[96minstall\033[0m     Install minimal kit (init skill + tools + catalog)
  \033[96mupdate\033[0m      Update kit without deleting custom/built skills
  \033[96mcompile\033[0m     Compile skills for a provider (claude|cursor|codex|gemini)
  \033[96mstatus\033[0m     Show step ledger + session + git status
  \033[96mvalidate\033[0m     Validate all SKILL.md against the schema
  \033[96mdoctor\033[0m      Check whether this project looks healthy

\033[1m\033[93mOPTIONS\033[0m
  \033[92m--agent\033[0m     Agent name to install/update into (e.g. \033[96mclaude\033[0m -> \033[90m.claude\033[0m)
              [default: \033[1magents\033[0m]
  \033[92m--provider\033[0m  Provider to compile skills for: \033[96m{', '.join(PROVIDERS)}\033[0m or \033[96mall\033[0m
  \033[92m--skills-root\033[0m  Skills directory to compile from (default: installed agent skills)
  \033[92m--target\033[0m     Output directory for compiled files (default: agent dir)
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
    p_install.add_argument("--provider", choices=[*PROVIDERS, "all"], default=None)

    p_update = sub.add_parser("update")
    p_update.add_argument("--agent", default="agents")
    p_update.add_argument("--provider", choices=[*PROVIDERS, "all"], default=None)

    p_compile = sub.add_parser("compile")
    p_compile.add_argument("--provider", choices=[*PROVIDERS, "all"], required=True)
    p_compile.add_argument("--agent", default="agents")
    p_compile.add_argument("--skills-root", default=None)
    p_compile.add_argument("--target", default=None)

    p_status = sub.add_parser("status")
    p_status.add_argument("--agent", default="agents")

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("--agent", default="agents")

    p_doctor = sub.add_parser("doctor")
    p_doctor.add_argument("--agent", default="agents")
    return parser

def _rest_from_namespace(command: str, ns: argparse.Namespace) -> list[str]:
    rest: list[str] = []
    if getattr(ns, "agent", None):
        rest.extend(["--agent", ns.agent])
    if getattr(ns, "provider", None) and command in ("install", "update"):
        rest.extend(["--provider", ns.provider])
    return rest

def run_compile(provider: str, agent: str, skills_root: str | None, target: str | None) -> int:
    compiler = find_provider_compiler()
    if compiler is None:
        raise SystemExit("Error: tools/providers/compile.py not found (run from repo checkout or after install)")

    agent_dir = f".{agent}" if not agent.startswith(".") else agent
    if skills_root is None:
        skills_root = str(Path(agent_dir) / "skills")
    if target is None:
        target = agent_dir

    skills_path = Path(skills_root)
    if not skills_path.is_dir():
        raise SystemExit(f"Error: skills root not found: {skills_root}")

    argv = [
        sys.executable,
        str(compiler),
        "--provider", provider,
        "--skills-root", str(skills_path),
        "--target", target,
    ]
    return subprocess.call(argv)

def _agent_dir(agent: str) -> Path:
    return Path(agent if agent.startswith(".") else f".{agent}")

def find_session_sh(agent: str) -> Path | None:
    """Locate .agents/tools/session/session.sh in cwd (installed kit)."""
    cand = _agent_dir(agent) / "tools" / "session" / "session.sh"
    return cand if cand.is_file() else None

def run_status(agent: str) -> int:
    session_sh = find_session_sh(agent)
    if session_sh is None:
        print("Status: no installed kit found (run `sk install` first).")
        return 0
    return subprocess.call(["bash", str(session_sh), "status"])

def find_validator() -> Path | None:
    candidates = [
        Path(__file__).resolve().parents[2] / "scripts" / "validate_skills.py",
        Path.cwd().resolve() / "scripts" / "validate_skills.py",
        Path.cwd().resolve() / ".agents" / "tools" / "session" / "validate_artifacts.py",
    ]
    for cand in candidates:
        if cand.is_file():
            return cand
    return None

def run_validate(agent: str) -> int:
    validator = find_validator()
    if validator is None:
        print("Error: no validator found (run from repo checkout or after install).")
        return 2
    if validator.name == "validate_artifacts.py":
        session_sh = find_session_sh(agent)
        if session_sh is None:
            print("Error: no installed kit found (run `sk install` first).")
            return 2
        return subprocess.call(["python", str(validator)], cwd=Path.cwd())
    return subprocess.call([sys.executable, str(validator)])

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

    if command == "compile":
        return run_compile(ns.provider, ns.agent, ns.skills_root, ns.target)
    if command == "status":
        return run_status(ns.agent)
    if command == "validate":
        return run_validate(ns.agent)

    provider = getattr(ns, "provider", None)
    result = run_installer(command, _rest_from_namespace(command, ns))
    if result != 0:
        return result
    if provider:
        print(f"\n⤓ Compiling skills for provider '{provider}' ...")
        return run_compile(provider, ns.agent, None, None)
    return result

if __name__ == "__main__":
    raise SystemExit(main())
