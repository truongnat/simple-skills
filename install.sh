#!/usr/bin/env bash
set -euo pipefail

OWNER="${SIMPLE_SKILLS_OWNER:-truongnat}"
REPO="${SIMPLE_SKILLS_REPO:-simple-skills}"
BRANCH="${SIMPLE_SKILLS_BRANCH:-main}"
GITHUB="${OWNER}/${REPO}"

AGENT_NAME="agents"

TARGET="$(pwd)"
SOURCE=""
TMP=""
COMMAND="install"

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

usage() {
  cat <<EOH
${BOLD}Usage:${NC}
  ${GREEN}install.sh${NC} ${CYAN}[install]${NC} [--agent NAME]
  ${GREEN}install.sh${NC} ${CYAN}update${NC} [--agent NAME]
  ${GREEN}install.sh${NC} ${CYAN}doctor${NC} [--agent NAME]

${BOLD}Commands:${NC}
  ${CYAN}install${NC}     Install all skills (replaces existing directory)
  ${CYAN}update${NC}      Update own skills without deleting custom ones
  ${CYAN}doctor${NC}      Check whether this project looks healthy

${BOLD}Options:${NC}
  ${GREEN}--agent NAME${NC}   Agent name to install/update into (e.g. ${CYAN}claude${NC} -> ${NC}.claude${NC}). Default: ${BOLD}agents${NC}
EOH
}

if [ "$#" -gt 0 ]; then
  case "$1" in
    install|update|doctor)
      COMMAND="$1"
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
    --agent)
      [ "$#" -ge 2 ] || { echo "Error: --agent requires a value." >&2; exit 2; }
      AGENT_NAME="$2"
      shift 2
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

AGENT_DIR=".${AGENT_NAME}"

cleanup() {
  if [ -n "$TMP" ] && [ -d "$TMP" ]; then
    rm -rf "$TMP"
  fi
}
trap cleanup EXIT

fetch_source() {
  echo -e "${CYAN}⤓ Downloading source...${NC}"
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
    return 0
  fi
  echo -e "${RED}✖  Missing:${NC} $label"
  return 1
}

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
  echo -e "${BOLD}⚙  DOCTOR${NC} Checking ${CYAN}${AGENT_DIR}${NC} ..."
  
  if [ ! -d "${TARGET}/${AGENT_DIR}" ]; then
    echo -e "${RED}✖  ERROR:${NC} Directory ${AGENT_DIR} is missing."
    return 1
  fi

  for f in START_HERE.md WHAT_NEXT.md SKILL_PREAMBLE.md AGENT_POLICY.md settings.yaml BA_SKILLS.md; do
    doctor_file "kit_${f}" "${TARGET}/${AGENT_DIR}/${f}" || ok=1
  done

  for f in "${THINKING_DOCS[@]}"; do
    doctor_file "kit_thinking/${f}" "${TARGET}/${AGENT_DIR}/thinking/${f}" || ok=1
  done

  doctor_file "root_AGENTS.md" "${TARGET}/AGENTS.md" || ok=1

  local work_loc
  work_loc="$(work_dir_location "${TARGET}/${AGENT_DIR}/settings.yaml")"

  if [ -f "${TARGET}/.gitignore" ] && grep -Fqx -- "${work_loc}/" "${TARGET}/.gitignore"; then
    :
  else
    echo -e "${YELLOW}⚠  WARNING:${NC} gitignore_agent_work is missing (${work_loc}/)"
  fi

  sess="${TARGET}/${AGENT_DIR}/tools/session/session.sh"
  if [ ! -x "$sess" ] && [ ! -f "$sess" ]; then
    echo -e "${RED}✖  ERROR:${NC} session_tool=missing"
    ok=1
  fi

  for t in validate_artifacts.py lint_artifacts.py build_context.py; do
    doctor_file "tool_${t}" "${TARGET}/${AGENT_DIR}/tools/session/${t}" || ok=1
  done

  if [ "$ok" -eq 0 ]; then
    echo -e "${GREEN}✔  Everything looks good!${NC}"
    return 0
  else
    echo -e "${YELLOW}⚠  Found missing files. Run update or install.${NC}"
    return 1
  fi
}

copy_docs_and_tools() {
  # Pre-taxonomy flat thinking doc
  rm -f "${TARGET}/${AGENT_DIR}/THINKING_OUTCOME_FIRST.md"

  for rel in "${KIT_FLAT_DOCS[@]}"; do
    src="${SOURCE}/docs/${rel}"
    if [ ! -f "$src" ]; then
      flat="${SOURCE}/docs/$(basename "$rel")"
      if [ -f "$flat" ]; then
        src="$flat"
      fi
    fi
    if [ -f "$src" ]; then
      cp -f "$src" "${TARGET}/${AGENT_DIR}/$(basename "$rel")"
    fi
  done

  rm -rf "${TARGET}/${AGENT_DIR}/thinking"
  mkdir -p "${TARGET}/${AGENT_DIR}/thinking"
  cp -R "${SOURCE}/docs/thinking/." "${TARGET}/${AGENT_DIR}/thinking/"

  if [ -d "${SOURCE}/docs/examples" ]; then
    rm -rf "${TARGET}/${AGENT_DIR}/examples"
    cp -R "${SOURCE}/docs/examples" "${TARGET}/${AGENT_DIR}/examples"
  fi

  if [ ! -f "${TARGET}/${AGENT_DIR}/settings.yaml" ]; then
    cp -f "${SOURCE}/docs/config/settings.yaml" "${TARGET}/${AGENT_DIR}/settings.yaml"
  fi

  local gi="${TARGET}/.gitignore"
  local marker
  marker="$(work_dir_location "${TARGET}/${AGENT_DIR}/settings.yaml")/"
  if [ -f "$gi" ] && ! grep -Fqx -- "$marker" "$gi"; then
    printf '\n# Simple Skills — Work layer\n%s\n' "$marker" >> "$gi"
  elif [ ! -f "$gi" ]; then
    printf '# Simple Skills — Work layer\n%s\n' "$marker" > "$gi"
  fi

  if [ -d "${SOURCE}/tools" ]; then
    mkdir -p "${TARGET}/${AGENT_DIR}/tools"
    shopt -s dotglob nullglob
    for item in "${TARGET}/${AGENT_DIR}/tools"/*; do
      [ "$(basename "$item")" = "decision-logs" ] && continue
      rm -rf "$item"
    done
    for item in "${SOURCE}/tools"/*; do
      [ "$(basename "$item")" = "decision-logs" ] && continue
      cp -R "$item" "${TARGET}/${AGENT_DIR}/tools/"
    done
    shopt -u dotglob nullglob
  fi

  mkdir -p "${TARGET}/${AGENT_DIR}/tools/session"
  cp -f "${SOURCE}/docs/config/artifact-schemas.json" \
    "${TARGET}/${AGENT_DIR}/tools/session/artifact-schemas.json"

  cp -f "${SOURCE}/docs/AGENTS.md" "${TARGET}/AGENTS.md"
  rm -f "${TARGET}/${AGENT_DIR}/AGENTS.md"
}

cmd_install() {
  if is_simple_skills_source "$(pwd)"; then
    SOURCE="$(pwd)"
  else
    fetch_source
  fi

  echo -e "${CYAN}▶ Installing skills into ${GREEN}${AGENT_DIR}${NC} ..."

  if [ -d "${TARGET}/${AGENT_DIR}" ]; then
    echo -e "${YELLOW}  ↺ Cleaning old directory...${NC}"
    rm -rf "${TARGET}/${AGENT_DIR}"
  fi
  mkdir -p "${TARGET}/${AGENT_DIR}/skills"

  for skill_path in "${SOURCE}"/skills/*/; do
    [ -d "$skill_path" ] || continue
    skill="$(basename "$skill_path")"
    skill_dest="${TARGET}/${AGENT_DIR}/skills/${skill}"
    
    mkdir -p "$skill_dest"
    shopt -s dotglob nullglob
    for item in "${skill_path}"/*; do
      [ "$(basename "$item")" = ".venv" ] && continue
      cp -R "$item" "${skill_dest}/"
    done
    shopt -u dotglob nullglob
  done

  copy_docs_and_tools
  echo -e "${GREEN}✨ Installation complete.${NC}"
}

cmd_update() {
  if is_simple_skills_source "$(pwd)"; then
    SOURCE="$(pwd)"
  else
    fetch_source
  fi

  echo -e "${CYAN}▶ Updating own skills in ${GREEN}${AGENT_DIR}${NC} ..."

  mkdir -p "${TARGET}/${AGENT_DIR}/skills"

  for skill_path in "${SOURCE}"/skills/*/; do
    [ -d "$skill_path" ] || continue
    skill="$(basename "$skill_path")"
    skill_dest="${TARGET}/${AGENT_DIR}/skills/${skill}"
    
    # Update with force
    if [ -d "$skill_dest" ]; then
      shopt -s dotglob nullglob
      for item in "${skill_dest}"/*; do
        [ "$(basename "$item")" = ".venv" ] && continue
        rm -rf "$item"
      done
      shopt -u dotglob nullglob
    fi
    
    mkdir -p "$skill_dest"
    shopt -s dotglob nullglob
    for item in "${skill_path}"/*; do
      [ "$(basename "$item")" = ".venv" ] && continue
      cp -R "$item" "${skill_dest}/"
    done
    shopt -u dotglob nullglob
  done

  copy_docs_and_tools
  echo -e "${GREEN}✨ Update complete.${NC}"
}

case "$COMMAND" in
  doctor) cmd_doctor ;;
  install) cmd_install ;;
  update) cmd_update ;;
  *)
    echo "Error: unknown command: ${COMMAND}" >&2
    usage >&2
    exit 2
    ;;
esac
