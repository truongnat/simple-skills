#!/usr/bin/env bash
set -euo pipefail

OWNER="${SIMPLE_SKILLS_OWNER:-truongnat}"
REPO="${SIMPLE_SKILLS_REPO:-simple-skills}"
BRANCH="${SIMPLE_SKILLS_BRANCH:-main}"
GITHUB="${OWNER}/${REPO}"
AGENTS_MODE="${SIMPLE_SKILLS_AGENTS_MODE:-prompt}"
PROFILE="${SIMPLE_SKILLS_PROFILE:-core}"

TARGET="$(pwd)"
SOURCE=""
TMP=""
COMMAND="install"
UNINSTALL_YES=false
KEEP_SETTINGS=false
PURGE_WORK=false

usage() {
  cat <<'EOF'
Usage:
  install.sh [install] [--agents-mode prompt|replace|skip] [--profile NAME[,NAME...]]
  install.sh uninstall [--yes] [--keep-settings] [--purge-work]
  install.sh doctor

Commands:
  install     Install/update the kit into .agents/ (default)
  uninstall   Remove the kit from this project
  doctor      Check whether this project looks healthy

Install options:
  --agents-mode   How to handle existing root AGENTS.md (prompt|replace|skip)
  --profile       core (default) | office | frontend | backend | all (comma-ok)

Uninstall options:
  --yes             Do not prompt
  --keep-settings   Keep .agents/settings.yaml after uninstall
  --purge-work      Also delete .agent-work/ (sessions + memory) — destructive

Env: SIMPLE_SKILLS_AGENTS_MODE, SIMPLE_SKILLS_PROFILE
EOF
}

# First token may be a command (or long-flag aliases).
if [ "$#" -gt 0 ]; then
  case "$1" in
    install|uninstall|doctor)
      COMMAND="$1"
      shift
      ;;
    --uninstall)
      COMMAND="uninstall"
      shift
      ;;
    --doctor)
      COMMAND="doctor"
      shift
      ;;
  esac
fi

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agents-mode)
      [ "$#" -ge 2 ] || { echo "Error: --agents-mode requires a value." >&2; exit 2; }
      AGENTS_MODE="$2"
      shift 2
      ;;
    --profile)
      [ "$#" -ge 2 ] || { echo "Error: --profile requires a value." >&2; exit 2; }
      PROFILE="$2"
      shift 2
      ;;
    --yes|-y)
      UNINSTALL_YES=true
      shift
      ;;
    --keep-settings)
      KEEP_SETTINGS=true
      shift
      ;;
    --purge-work)
      PURGE_WORK=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Error: unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$AGENTS_MODE" in
  prompt|replace|skip) ;;
  *)
    echo "Error: agents mode must be prompt, replace, or skip." >&2
    exit 2
    ;;
esac

cleanup() {
  if [ -n "$TMP" ] && [ -d "$TMP" ]; then
    rm -rf "$TMP"
  fi
}
trap cleanup EXIT

fetch_source() {
  echo "Downloading ${GITHUB}@${BRANCH} ..."
  TMP="$(mktemp -d)"
  curl -fsSL "https://github.com/${GITHUB}/archive/refs/heads/${BRANCH}.tar.gz" \
    | tar -xz -C "$TMP" --strip-components=1
  SOURCE="$TMP"
}

is_simple_skills_source() {
  local root="$1"
  [ -f "${root}/docs/AGENTS.md" ] \
    && [ -f "${root}/skills/planning/SKILL.md" ] \
    && [ -f "${root}/skills/execution/SKILL.md" ]
}

cmd_doctor() {
  local ok=0
  printf 'DOCTOR project=%s\n' "$TARGET"

  if [ -d "${TARGET}/.agents" ]; then
    printf 'agents_dir=yes\n'
  else
    printf 'agents_dir=MISSING — run install.sh\n'
    ok=1
  fi

  for f in START_HERE.md WHAT_NEXT.md SKILL_PREAMBLE.md AGENT_POLICY.md settings.yaml; do
    if [ -f "${TARGET}/.agents/$f" ]; then
      printf 'kit_%s=yes\n' "$f"
    else
      printf 'kit_%s=missing\n' "$f"
      ok=1
    fi
  done

  if [ -f "${TARGET}/AGENTS.md" ]; then
    printf 'root_AGENTS.md=yes\n'
  else
    printf 'root_AGENTS.md=missing\n'
    ok=1
  fi

  if [ -f "${TARGET}/.gitignore" ] && grep -Fqx -- '.agent-work/' "${TARGET}/.gitignore"; then
    printf 'gitignore_agent_work=yes\n'
  else
    printf 'gitignore_agent_work=MISSING\n'
    ok=1
  fi

  if [ -d "${TARGET}/.agent-work" ]; then
    printf 'work_dir=yes\n'
    if [ -d "${TARGET}/.agent-work/.git" ]; then
      printf 'work_nested_git=yes\n'
    else
      printf 'work_nested_git=no\n'
    fi
  else
    printf 'work_dir=(none yet)\n'
  fi

  sess="${TARGET}/.agents/tools/session/session.sh"
  if [ -x "$sess" ] || [ -f "$sess" ]; then
    printf 'session_tool=yes\n'
    _ss_out="$(mktemp)"
    if bash "$sess" doctor >"$_ss_out" 2>/dev/null; then
      sed 's/^/session_/' "$_ss_out" || true
    else
      printf 'session_doctor=warn (could not run)\n'
    fi
    rm -f "$_ss_out"
  else
    printf 'session_tool=missing\n'
    ok=1
  fi

  for t in validate_artifacts.py lint_artifacts.py build_context.py; do
    if [ -f "${TARGET}/.agents/tools/session/$t" ]; then
      printf 'tool_%s=yes\n' "$t"
    else
      printf 'tool_%s=missing\n' "$t"
      ok=1
    fi
  done

  if [ "$ok" -eq 0 ]; then
    printf 'DOCTOR_OK\n'
    return 0
  fi
  printf 'DOCTOR_FAIL\n'
  return 1
}

cmd_uninstall() {
  if [ "$UNINSTALL_YES" != true ]; then
    if [ -c /dev/tty ] && tty -s < /dev/tty 2>/dev/null; then
      printf "Uninstall Simple Skills kit from %s? [y/N] " "$TARGET" > /dev/tty
      read -r answer < /dev/tty
      case "$answer" in
        y|Y|yes|YES|Yes) ;;
        *) echo "Aborted."; exit 0 ;;
      esac
    else
      echo "Error: uninstall needs --yes when no interactive terminal is available." >&2
      exit 2
    fi
  fi

  settings_backup=""
  if [ "$KEEP_SETTINGS" = true ] && [ -f "${TARGET}/.agents/settings.yaml" ]; then
    settings_backup="$(mktemp)"
    cp -f "${TARGET}/.agents/settings.yaml" "$settings_backup"
    echo "Backing up settings.yaml ..."
  fi

  if [ -d "${TARGET}/.agents" ]; then
    echo "Removing ${TARGET}/.agents ..."
    rm -rf "${TARGET}/.agents"
  else
    echo "No .agents/ directory to remove."
  fi

  if [ -f "${TARGET}/AGENTS.md" ]; then
    echo "Removing ${TARGET}/AGENTS.md ..."
    rm -f "${TARGET}/AGENTS.md"
  fi

  if [ -n "$settings_backup" ]; then
    mkdir -p "${TARGET}/.agents"
    cp -f "$settings_backup" "${TARGET}/.agents/settings.yaml"
    rm -f "$settings_backup"
    echo "Restored .agents/settings.yaml (--keep-settings)."
  fi

  if [ "$PURGE_WORK" = true ]; then
    if [ -d "${TARGET}/.agent-work" ]; then
      echo "Removing ${TARGET}/.agent-work (--purge-work) ..."
      rm -rf "${TARGET}/.agent-work"
    fi
  else
    echo "Keeping .agent-work/ (sessions/memory). Use --purge-work to delete."
  fi

  echo "Uninstall complete. (.gitignore .agent-work/ entry left in place if present.)"
}

cmd_install() {
  if is_simple_skills_source "$(pwd)"; then
    SOURCE="$(pwd)"
  else
    fetch_source
  fi

  resolve_skills() {
    if command -v python3 >/dev/null 2>&1; then
      python3 "${SOURCE}/scripts/resolve_install_profile.py" \
        --source "${SOURCE}" \
        --profile "${PROFILE}" \
        --check
      return
    fi
    if [ "${PROFILE}" = "all" ]; then
      for skill_path in "${SOURCE}"/skills/*/; do
        [ -d "$skill_path" ] || continue
        basename "$skill_path"
      done | sort
      return
    fi
    echo "Error: python3 is required to resolve install profile '${PROFILE}'." >&2
    echo "Install python3 or use --profile all." >&2
    exit 2
  }

  echo "Installing skills into ${TARGET}/.agents (profile: ${PROFILE}) ..."

  mkdir -p "${TARGET}/.agents/skills"

  SKILLS_FILE="$(mktemp)"
  resolve_skills > "${SKILLS_FILE}"
  skill_count="$(wc -l < "${SKILLS_FILE}" | tr -d ' ')"
  if [ "$skill_count" -eq 0 ]; then
    echo "Error: profile '${PROFILE}' resolved to zero skills." >&2
    exit 1
  fi

  echo "Installing ${skill_count} skills."

  while IFS= read -r skill; do
    [ -n "$skill" ] || continue
    skill_path="${SOURCE}/skills/${skill}"
    [ -d "$skill_path" ] || { echo "Error: missing skill source ${skill}" >&2; exit 1; }
    echo "Installing skill ${skill} ..."
    skill_dest="${TARGET}/.agents/skills/${skill}"
    mkdir -p "$skill_dest"
    shopt -s dotglob nullglob
    for item in "${skill_dest}"/*; do
      [ "$(basename "$item")" = ".venv" ] && continue
      rm -rf "$item"
    done
    for item in "${skill_path}"/*; do
      [ "$(basename "$item")" = ".venv" ] && continue
      cp -R "$item" "${skill_dest}/"
    done
    shopt -u dotglob nullglob
  done < "${SKILLS_FILE}"

  shopt -s nullglob
  for installed in "${TARGET}/.agents/skills"/*/; do
    name="$(basename "$installed")"
    if ! grep -Fxq -- "$name" "${SKILLS_FILE}"; then
      echo "Removing skill not in profile: ${name} ..."
      rm -rf "$installed"
    fi
  done
  shopt -u nullglob
  rm -f "${SKILLS_FILE}"

  if [ -d "${TARGET}/.agents/skills/office-mcp" ]; then
    echo "Removing obsolete skill office-mcp ..."
    rm -rf "${TARGET}/.agents/skills/office-mcp"
  fi

  cp -f "${SOURCE}/docs/DESIGN_SYSTEM.md" "${TARGET}/.agents/DESIGN_SYSTEM.md"
  cp -f "${SOURCE}/docs/CODE_COMMENTS.md" "${TARGET}/.agents/CODE_COMMENTS.md"
  cp -f "${SOURCE}/docs/THIRD_PARTY_SKILLS.md" "${TARGET}/.agents/THIRD_PARTY_SKILLS.md"
  cp -f "${SOURCE}/docs/SKILL_PREAMBLE.md" "${TARGET}/.agents/SKILL_PREAMBLE.md"
  cp -f "${SOURCE}/docs/AGENT_POLICY.md" "${TARGET}/.agents/AGENT_POLICY.md"
  cp -f "${SOURCE}/docs/AGENT_WORK.md" "${TARGET}/.agents/AGENT_WORK.md"
  cp -f "${SOURCE}/docs/START_HERE.md" "${TARGET}/.agents/START_HERE.md"
  cp -f "${SOURCE}/docs/WHAT_NEXT.md" "${TARGET}/.agents/WHAT_NEXT.md"
  cp -f "${SOURCE}/docs/MIGRATION.md" "${TARGET}/.agents/MIGRATION.md"
  if [ -d "${SOURCE}/docs/examples" ]; then
    rm -rf "${TARGET}/.agents/examples"
    cp -R "${SOURCE}/docs/examples" "${TARGET}/.agents/examples"
  fi

  ensure_agent_work_gitignore() {
    local gi="${TARGET}/.gitignore"
    local marker=".agent-work/"
    if [ -f "$gi" ] && grep -Fqx -- "$marker" "$gi"; then
      echo "Keeping existing .gitignore entry for .agent-work/."
      return
    fi
    if [ -f "$gi" ]; then
      printf '\n# Simple Skills — Work layer (sessions + memory; nested git)\n%s\n' "$marker" >> "$gi"
      echo "Appended .agent-work/ to existing .gitignore."
    else
      cp -f "${SOURCE}/docs/gitignore.agent-work.snippet" "$gi"
      echo "Created .gitignore with .agent-work/ ignore rule."
    fi
  }
  ensure_agent_work_gitignore

  if [ -d "${SOURCE}/tools" ]; then
    echo "Installing tools into ${TARGET}/.agents/tools ..."
    mkdir -p "${TARGET}/.agents/tools"
    shopt -s dotglob nullglob
    for item in "${TARGET}/.agents/tools"/*; do
      [ "$(basename "$item")" = "decision-logs" ] && continue
      rm -rf "$item"
    done
    for item in "${SOURCE}/tools"/*; do
      [ "$(basename "$item")" = "decision-logs" ] && continue
      cp -R "$item" "${TARGET}/.agents/tools/"
    done
    shopt -u dotglob nullglob
  fi

  mkdir -p "${TARGET}/.agents/tools/session"
  cp -f "${SOURCE}/docs/artifact-schemas.json" \
    "${TARGET}/.agents/tools/session/artifact-schemas.json"

  if [ -f "${TARGET}/.agents/settings.yaml" ]; then
    echo "Keeping existing .agents/settings.yaml."
  else
    cp -f "${SOURCE}/docs/settings.yaml" "${TARGET}/.agents/settings.yaml"
  fi

  install_agents_file=true
  if [ -f "${TARGET}/AGENTS.md" ]; then
    case "$AGENTS_MODE" in
      replace)
        echo "Replacing existing ${TARGET}/AGENTS.md ..."
        ;;
      skip)
        echo "Keeping existing ${TARGET}/AGENTS.md."
        install_agents_file=false
        ;;
      prompt)
        if [ -c /dev/tty ] && tty -s < /dev/tty 2>/dev/null; then
          printf "AGENTS.md already exists. Replace it? [y/N] " > /dev/tty
          read -r answer < /dev/tty
          case "$answer" in
            y|Y|yes|YES|Yes)
              echo "Replacing existing ${TARGET}/AGENTS.md ..."
              ;;
            *)
              echo "Keeping existing ${TARGET}/AGENTS.md."
              install_agents_file=false
              ;;
          esac
        else
          echo "AGENTS.md already exists; keeping it because no interactive terminal is available." >&2
          echo "Use --agents-mode replace or SIMPLE_SKILLS_AGENTS_MODE=replace to replace it." >&2
          install_agents_file=false
        fi
        ;;
    esac
  fi

  if [ "$install_agents_file" = true ]; then
    cp -f "${SOURCE}/docs/AGENTS.md" "${TARGET}/AGENTS.md"
  fi

  rm -f "${TARGET}/.agents/AGENTS.md"

  echo "Skills installed successfully (profile: ${PROFILE})."
  echo "Next: bash .agents/tools/session/session.sh doctor   # or: ./install.sh doctor"
}

case "$COMMAND" in
  doctor) cmd_doctor ;;
  uninstall) cmd_uninstall ;;
  install) cmd_install ;;
  *)
    echo "Error: unknown command: ${COMMAND}" >&2
    usage >&2
    exit 2
    ;;
esac
