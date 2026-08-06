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
PURGE_UNSELECTED=false
CONFLICT_MODE="${SIMPLE_SKILLS_CONFLICT_MODE:-prompt}"

usage() {
  cat <<'EOF'
Usage:
  install.sh [install] [--agents-mode prompt|replace|skip] [--conflict-mode prompt|replace|skip|rename] [--profile NAME[,NAME...]]
  install.sh uninstall [--yes] [--keep-settings] [--purge-work]
  install.sh doctor

Commands:
  install     Install/update the kit into .agents/ (default)
  uninstall   Remove the kit from this project
  doctor      Check whether this project looks healthy

Install options:
  --agents-mode     How to handle existing root AGENTS.md (prompt|replace|skip)
  --conflict-mode   How to handle existing skills (prompt|replace|skip|rename)
  --profile         core (default) | office | frontend | backend | all (comma-ok)
  --purge-unselected  Remove skills not in the selected profile

Uninstall options:
  --yes             Do not prompt
  --keep-settings   Keep .agents/settings.yaml after uninstall
  --purge-work      Also delete .agent-work/ (sessions + memory) — destructive

Env: SIMPLE_SKILLS_AGENTS_MODE, SIMPLE_SKILLS_PROFILE, SIMPLE_SKILLS_CONFLICT_MODE
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
    --conflict-mode)
      [ "$#" -ge 2 ] || { echo "Error: --conflict-mode requires a value." >&2; exit 2; }
      CONFLICT_MODE="$2"
      shift 2
      ;;
    --purge-unselected)
      PURGE_UNSELECTED=true
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

case "$CONFLICT_MODE" in
  prompt|replace|skip|rename) ;;
  *)
    echo "Error: conflict mode must be prompt, replace, skip, or rename." >&2
    exit 2
    ;;
esac

cleanup() {
  if [ -n "$TMP" ] && [ -d "$TMP" ]; then
    rm -rf "$TMP"
  fi
}
trap cleanup EXIT

get_unique_skill_name() {
  local base_name="$1"
  local skills_dir="$2"
  local name="$base_name"
  local counter=1
  while [ -d "${skills_dir}/${name}" ]; do
    name="${base_name}${counter}"
    counter=$((counter + 1))
  done
  printf '%s' "$name"
}

resolve_conflict_action() {
  local skill_name="$1"
  local mode="$2"
  
  case "$mode" in
    replace|skip|rename)
      printf '%s' "$mode"
      return
      ;;
  esac
  
  # prompt mode
  echo ""
  echo "Skill '${skill_name}' already exists." >&2
  if [ -c /dev/tty ] && tty -s < /dev/tty 2>/dev/null; then
    printf "[R]eplace / [S]kip / [C]opy to new name (skill-A1) / [A]bort? (R/S/C/A) " > /dev/tty
    read -r answer < /dev/tty
    case "$answer" in
      [rR]|[rR]eplace|[yY]|[yY]es) printf 'replace' ;;
      [sS]|[sS]kip|[nN]|[nN]o) printf 'skip' ;;
      [cC]|[cC]opy|[rR]ename) printf 'rename' ;;
      *) printf 'abort' ;;
    esac
  else
    echo "Non-interactive mode: use --conflict-mode to specify behavior." >&2
    printf 'abort'
  fi
}

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

# Flat kit docs: source-under-docs → basename under .agents/
KIT_FLAT_DOCS=(
  conventions/DESIGN_SYSTEM.md
  conventions/CODE_COMMENTS.md
  conventions/THIRD_PARTY_SKILLS.md
  policy/SKILL_PREAMBLE.md
  policy/AGENT_POLICY.md
  policy/AGENT_WORK.md
  guides/START_HERE.md
  guides/WHAT_NEXT.md
  guides/MIGRATION.md
  guides/BA_SKILLS.md
)

# Normative Thinking methods (+ README) under docs/thinking/ → .agents/thinking/
THINKING_DOCS=(
  outcome-first.md
  input-process-output.md
  make-implicit-explicit.md
  single-source-of-truth.md
  small-batch.md
  feedback-loop.md
  default-path-first.md
  reversible-decisions.md
  standardize-before-automate.md
  design-for-handoff.md
  evidence-over-confidence.md
  optimize-bottleneck.md
  README.md
)

doctor_file() {
  local label="$1" path="$2"
  if [ -f "$path" ]; then
    printf '%s=yes\n' "$label"
    return 0
  fi
  printf '%s=missing\n' "$label"
  return 1
}

# Resolve rules.agent_work.location from a settings.yaml (default .agent-work).
# Mirrors tools/session/_work_settings.py and session.sh's work_dir_rel() so
# install.sh, session.sh, and every tools/session/*.py tool agree.
work_dir_location() {
  local sf="$1"
  local loc=".agent-work"
  [ -f "$sf" ] || { printf '%s\n' "$loc"; return; }
  local val
  val="$(awk '
    /^rules:[[:space:]]*$/ { in_rules=1; next }
    in_rules && /^[^[:space:]]/ { in_rules=0 }
    in_rules && /^  agent_work:[[:space:]]*$/ { in_aw=1; next }
    in_aw && /^  [^[:space:]]/ { in_aw=0 }
    in_aw && /^    location:/ {
      v = $0
      sub(/^    location:[[:space:]]*/, "", v)
      gsub(/[[:space:]]+$/, "", v)
      print v
      exit
    }
  ' "$sf" 2>/dev/null)"
  val="${val%\"}"; val="${val#\"}"
  val="${val%\'}"; val="${val#\'}"
  [ -n "$val" ] && loc="${val%/}"
  printf '%s\n' "$loc"
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

  for f in START_HERE.md WHAT_NEXT.md SKILL_PREAMBLE.md AGENT_POLICY.md settings.yaml BA_SKILLS.md; do
    doctor_file "kit_${f}" "${TARGET}/.agents/${f}" || ok=1
  done

  for f in "${THINKING_DOCS[@]}"; do
    doctor_file "kit_thinking/${f}" "${TARGET}/.agents/thinking/${f}" || ok=1
  done

  doctor_file "root_AGENTS.md" "${TARGET}/AGENTS.md" || ok=1

  local work_loc
  work_loc="$(work_dir_location "${TARGET}/.agents/settings.yaml")"

  if [ -f "${TARGET}/.gitignore" ] && grep -Fqx -- "${work_loc}/" "${TARGET}/.gitignore"; then
    printf 'gitignore_agent_work=yes\n'
  else
    printf 'gitignore_agent_work=MISSING (%s/)\n' "$work_loc"
    ok=1
  fi

  if [ -d "${TARGET}/${work_loc}" ]; then
    printf 'work_dir=yes\n'
    if [ -d "${TARGET}/${work_loc}/.git" ]; then
      printf 'work_nested_git=yes\n'
    else
      printf 'work_nested_git=no\n'
    fi
  else
    printf 'work_dir=(none yet)\n'
  fi
  if [ "$work_loc" != ".agent-work" ] && [ -d "${TARGET}/.agent-work" ]; then
    printf 'orphaned_default_work_dir=yes — .agent-work/ exists but rules.agent_work.location=%s\n' "$work_loc"
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
    doctor_file "tool_${t}" "${TARGET}/.agents/tools/session/${t}" || ok=1
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

  # Resolve before .agents/ is removed below, so a customized location is
  # still honored for the --purge-work step and the closing message.
  work_loc="$(work_dir_location "${TARGET}/.agents/settings.yaml")"

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
    if [ -d "${TARGET}/${work_loc}" ]; then
      echo "Removing ${TARGET}/${work_loc} (--purge-work) ..."
      rm -rf "${TARGET}/${work_loc}"
    fi
  else
    echo "Keeping ${work_loc}/ (sessions/memory). Use --purge-work to delete."
  fi

  echo "Uninstall complete. (.gitignore ${work_loc}/ entry left in place if present.)"
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

  skills_dir="${TARGET}/.agents/skills"
  abort_install=false

  while IFS= read -r skill; do
    [ -n "$skill" ] || continue
    [ "$abort_install" = true ] && break
    
    skill_path="${SOURCE}/skills/${skill}"
    [ -d "$skill_path" ] || { echo "Error: missing skill source ${skill}" >&2; exit 1; }
    
    skill_dest="${skills_dir}/${skill}"
    skill_exists=false
    [ -d "$skill_dest" ] && skill_exists=true
    
    # Handle conflict if skill already exists
    if [ "$skill_exists" = true ]; then
      action="$(resolve_conflict_action "$skill" "$CONFLICT_MODE")"
      
      case "$action" in
        skip)
          echo "Skipping skill $skill (keeping existing)."
          continue
          ;;
        rename)
          new_name="$(get_unique_skill_name "$skill" "$skills_dir")"
          skill_dest="${skills_dir}/${new_name}"
          echo "Installing skill $skill as $new_name ..."
          ;;
        replace)
          echo "Replacing skill $skill ..."
          ;;
        abort)
          echo "Aborting install."
          abort_install=true
          continue
          ;;
      esac
    else
      echo "Installing skill ${skill} ..."
    fi
    
    [ "$abort_install" = true ] && continue
    
    mkdir -p "$skill_dest"
    
    # Only remove existing content if we're replacing the original skill
    if [ "$skill_exists" = true ] && [ "$skill_dest" = "${skills_dir}/${skill}" ]; then
      shopt -s dotglob nullglob
      for item in "${skill_dest}"/*; do
        [ "$(basename "$item")" = ".venv" ] && continue
        rm -rf "$item"
      done
      shopt -u dotglob nullglob
    fi
    
    shopt -s dotglob nullglob
    for item in "${skill_path}"/*; do
      [ "$(basename "$item")" = ".venv" ] && continue
      cp -R "$item" "${skill_dest}/"
    done
    shopt -u dotglob nullglob
  done < "${SKILLS_FILE}"

  if [ "$abort_install" = true ]; then
    rm -f "${SKILLS_FILE}"
    echo "Installation aborted by user." >&2
    exit 1
  fi

  if [ "$PURGE_UNSELECTED" = true ]; then
    shopt -s nullglob
    for installed in "${TARGET}/.agents/skills"/*/; do
      name="$(basename "$installed")"
      if ! grep -Fxq -- "$name" "${SKILLS_FILE}"; then
        echo "Removing skill not in profile: ${name} ..."
        rm -rf "$installed"
      fi
    done
    shopt -u nullglob
  else
    echo "Keeping existing skills not in profile (use --purge-unselected to remove)."
  fi
  rm -f "${SKILLS_FILE}"

  if [ -d "${TARGET}/.agents/skills/office-mcp" ]; then
    echo "Removing obsolete skill office-mcp ..."
    rm -rf "${TARGET}/.agents/skills/office-mcp"
  fi

  # Pre-taxonomy flat thinking doc (replaced by .agents/thinking/).
  rm -f "${TARGET}/.agents/THINKING_OUTCOME_FIRST.md"

  for rel in "${KIT_FLAT_DOCS[@]}"; do
    src="${SOURCE}/docs/${rel}"
    if [ ! -f "$src" ]; then
      # Pre-taxonomy flat layout fallback (docs/DESIGN_SYSTEM.md, …)
      flat="${SOURCE}/docs/$(basename "$rel")"
      if [ -f "$flat" ]; then
        src="$flat"
      else
        echo "Error: missing kit doc '${rel}' under ${SOURCE}/docs/" >&2
        echo "Also tried flat path: docs/$(basename "$rel")" >&2
        echo "Update installer (sk / curl install.sh from main) or set SIMPLE_SKILLS_BRANCH." >&2
        exit 1
      fi
    fi
    cp -f "$src" "${TARGET}/.agents/$(basename "$rel")"
  done

  rm -rf "${TARGET}/.agents/thinking"
  mkdir -p "${TARGET}/.agents/thinking"
  cp -R "${SOURCE}/docs/thinking/." "${TARGET}/.agents/thinking/"
  for f in "${THINKING_DOCS[@]}"; do
    if [ ! -f "${TARGET}/.agents/thinking/${f}" ]; then
      echo "Error: missing thinking doc after copy: ${f}" >&2
      exit 1
    fi
  done

  if [ -d "${SOURCE}/docs/examples" ]; then
    rm -rf "${TARGET}/.agents/examples"
    cp -R "${SOURCE}/docs/examples" "${TARGET}/.agents/examples"
  fi

  # Settings must land before we compute the gitignore marker below, so a
  # kept (already-customized) settings.yaml controls the Work dir name.
  if [ -f "${TARGET}/.agents/settings.yaml" ]; then
    echo "Keeping existing .agents/settings.yaml."
  else
    cp -f "${SOURCE}/docs/config/settings.yaml" "${TARGET}/.agents/settings.yaml"
  fi

  ensure_agent_work_gitignore() {
    local gi="${TARGET}/.gitignore"
    local marker
    marker="$(work_dir_location "${TARGET}/.agents/settings.yaml")/"
    if [ -f "$gi" ] && grep -Fqx -- "$marker" "$gi"; then
      echo "Keeping existing .gitignore entry for ${marker}."
      return
    fi
    if [ -f "$gi" ]; then
      printf '\n# Simple Skills — Work layer (sessions + memory; nested git)\n%s\n' "$marker" >> "$gi"
      echo "Appended ${marker} to existing .gitignore."
    elif [ "$marker" = ".agent-work/" ]; then
      cp -f "${SOURCE}/docs/config/gitignore.agent-work.snippet" "$gi"
      echo "Created .gitignore with .agent-work/ ignore rule."
    else
      printf '# Simple Skills — Work layer (sessions + memory; nested git)\n%s\n' "$marker" > "$gi"
      echo "Created .gitignore with ${marker} ignore rule."
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
  cp -f "${SOURCE}/docs/config/artifact-schemas.json" \
    "${TARGET}/.agents/tools/session/artifact-schemas.json"

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
