#!/usr/bin/env bash
# Short entrypoint for curl | bash (same CLI as install.sh).
set -euo pipefail

ROOT="$(CDPATH= cd -- "$(dirname "$0")" 2>/dev/null && pwd)" || ROOT=""
if [ -n "$ROOT" ] && [ -f "${ROOT}/install.sh" ]; then
  exec bash "${ROOT}/install.sh" "$@"
fi

OWNER="${SIMPLE_SKILLS_OWNER:-truongnat}"
REPO="${SIMPLE_SKILLS_REPO:-simple-skills}"
BRANCH="${SIMPLE_SKILLS_BRANCH:-main}"
curl -fsSL "https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/install.sh" \
  | bash -s -- "$@"
