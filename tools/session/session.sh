#!/usr/bin/env bash
# Active-session helper for the agent lifecycle. Gives every skill/provider ONE
# deterministic answer to "which session am I in?" and "what is the real
# progress?" — so artifacts are never written to a cache/temp path and progress
# is never hand-guessed.
#
# Kit vs Work:
#   .agents/       installer kit (skills, tools, settings, policy)
#   .agent-work/   feature work (sessions + memory), optional nested git
#
# The active session is recorded in .agent-work/sessions/.current (one line: the
# repo-relative session dir). Read-only except `set`/`new`, which only touch
# that pointer and the session dir.
#
# Usage (run from the repo root, or any subdir — walks up to find .agents or
# .agent-work):
#   session.sh help                 Show commands + related tools
#   session.sh doctor               Check Work layout / gitignore / tools
#   session.sh current              Print the active session dir (exit 1 if unset)
#   session.sh set <dir|slug>       Point .current at an existing session dir
#   session.sh new <slug>           Create .agent-work/sessions/Task-N-<slug>, set current
#   session.sh status [dir]         Compute real task progress from <dir>/TASKS.md
#   session.sh work-root            Print .agent-work path (creates + ensures git)
#
# `status` prints a summary, a COMPLETE flag, and a corrected mermaid pie to
# paste into TASKS.md. COMPLETE=yes only when every card is done/skipped with
# nothing blocked or in any other state (e.g. in_progress, review). Never
# report 100%/done while COMPLETE=no. Do not maintain a separate OVERVIEW.md —
# TASKS.md + this command are the status source of truth.
set -eu

find_root() {
  d="$(pwd)"
  while [ "$d" != "/" ]; do
    if [ -d "$d/.agents" ] || [ -d "$d/.agent-work" ]; then
      printf '%s\n' "$d"
      return 0
    fi
    d="$(dirname "$d")"
  done
  pwd
}

ROOT="$(find_root)"
WORK_DIR="$ROOT/.agent-work"
SESS_DIR="$WORK_DIR/sessions"
MEM_DIR="$WORK_DIR/memory"
POINTER="$SESS_DIR/.current"

die() { printf '%s\n' "$*" >&2; exit 1; }

# Ensure Work tree exists. Init a nested git repo once so session+memory history
# stays out of the product root git and can be branched/diffed cheaply.
ensure_work() {
  mkdir -p "$SESS_DIR" "$MEM_DIR"
  if [ ! -d "$WORK_DIR/.git" ]; then
    if command -v git >/dev/null 2>&1; then
      git -C "$WORK_DIR" init -q
      # Keep nested repo self-contained; ignore OS junk only.
      if [ ! -f "$WORK_DIR/.gitignore" ]; then
        printf '%s\n' '.DS_Store' 'Thumbs.db' '*.tmp' > "$WORK_DIR/.gitignore"
      fi
      # Seed README so first commit has structure (optional, quiet).
      if [ ! -f "$WORK_DIR/README.md" ]; then
        cat > "$WORK_DIR/README.md" <<'EOF'
# Agent work (sessions + memory)

This directory is the **Work** layer for Simple Skills:

- `sessions/` — per-task artifacts (fixed templates)
- `memory/` — durable lessons (vital few) across tasks

It is intentionally separate from `.agents/` (the installer **Kit**: skills,
tools, settings, policy). Version this tree with its own git; keep the product
root git focused on source code.
EOF
      fi
      git -C "$WORK_DIR" add -A
      git -C "$WORK_DIR" -c user.email="agent-work@localhost" -c user.name="agent-work" \
        commit -q -m "chore: initialize agent-work" 2>/dev/null || true
    fi
  fi
}

cmd_work_root() {
  ensure_work
  printf '%s\n' ".agent-work"
}

cmd_current() {
  ensure_work
  [ -f "$POINTER" ] || die "No active session. A lifecycle skill must run 'session.sh set/new' first (or create .agent-work/sessions/<Task-N-slug>/ and point .current at it)."
  rel="$(head -n1 "$POINTER" | tr -d '\r\n')"
  [ -n "$rel" ] || die "Active-session pointer is empty: $POINTER"
  # Migrate legacy pointers written under .agents/sessions/…
  case "$rel" in
    .agents/sessions/*)
      base="$(basename "$rel")"
      if [ -d "$SESS_DIR/$base" ]; then
        rel=".agent-work/sessions/$base"
        printf '%s\n' "$rel" > "$POINTER"
      elif [ -d "$ROOT/$rel" ]; then
        die "Legacy session path '$rel' found. Move it to .agent-work/sessions/$base then re-run."
      fi
      ;;
  esac
  [ -d "$ROOT/$rel" ] || die "Active session '$rel' recorded in .current does not exist. Re-set it with 'session.sh set <dir>'."
  printf '%s\n' "$rel"
}

cmd_set() {
  ensure_work
  [ "$#" -ge 1 ] || die "Usage: session.sh set <dir|slug>"
  arg="$1"; base="$(basename "$arg")"
  target="$SESS_DIR/$base"
  [ -d "$target" ] || die "Session dir does not exist: .agent-work/sessions/$base (use 'session.sh new <slug>' to create it)."
  printf '%s\n' ".agent-work/sessions/$base" > "$POINTER"
  printf '%s\n' ".agent-work/sessions/$base"
}

cmd_new() {
  ensure_work
  [ "$#" -ge 1 ] || die "Usage: session.sh new <slug>"
  slug="$(printf '%s' "$1" | tr ' /' '--' | tr -cd 'A-Za-z0-9._-')"
  # Next Task-N number across existing Task-* dirs.
  n=1
  for d in "$SESS_DIR"/Task-*/; do
    [ -d "$d" ] || continue
    num="$(basename "$d" | sed -n 's/^Task-\([0-9]\{1,\}\)-.*/\1/p')"
    [ -n "$num" ] && [ "$num" -ge "$n" ] && n=$((num + 1))
  done
  name="Task-${n}-${slug}"
  mkdir -p "$SESS_DIR/$name"
  printf '%s\n' ".agent-work/sessions/$name" > "$POINTER"
  printf '%s\n' ".agent-work/sessions/$name"
}

cmd_status() {
  ensure_work
  rel="${1:-}"
  [ -n "$rel" ] || rel="$(cmd_current)"
  tasks="$ROOT/$rel/TASKS.md"
  [ -f "$tasks" ] || die "No TASKS.md in $rel — nothing to measure."

  # Parse the Progress board: rows like "| [ ] | T-001 | title | todo |".
  # Status is the last table cell; Done is the [ ]/[x] checkbox.
  awk -F'|' '
    /^[[:space:]]*\|[[:space:]]*\[[ xX]\][[:space:]]*\|/ {
      done_cell=$2; status=$(NF-1)
      gsub(/[[:space:]]/,"",done_cell)
      gsub(/^[[:space:]]+|[[:space:]]+$/,"",status)
      status=tolower(status)
      total++
      c[status]++
    }
    END{
      todo=c["todo"]+0; ip=c["in_progress"]+0; dn=c["done"]+0
      bl=c["blocked"]+0; sk=c["skipped"]+0
      other=total-todo-ip-dn-bl-sk
      pct=(total>0)?int(dn*100/total):0
      complete=(total>0 && (dn+sk)==total && bl==0 && other==0)?"yes":"no"
      printf "SESSION_TASKS_TOTAL: %d\n", total
      printf "done:%d in_progress:%d todo:%d blocked:%d skipped:%d other:%d\n", dn,ip,todo,bl,sk,other
      printf "PERCENT_DONE: %d%%\n", pct
      printf "COMPLETE: %s\n", complete
      if (checked!=dn) printf "WARNING: %d Done-checkboxes [x] but %d status=done rows — reconcile TASKS.md.\n", checked, dn
      if (other>0) printf "WARNING: %d card(s) in a non-terminal state (e.g. in_progress/review) — cannot be done.\n", other
      print  "--- paste into TASKS.md Progress board ---"
      print  "```mermaid"
      print  "pie title Task status"
      printf "  \"done\" : %d\n", dn
      printf "  \"in_progress\" : %d\n", ip
      printf "  \"todo\" : %d\n", todo
      printf "  \"blocked\" : %d\n", bl
      if (sk>0)    printf "  \"skipped\" : %d\n", sk
      if (other>0) printf "  \"other\" : %d\n", other
      print  "```"
    }
  ' "$tasks"
}

cmd_help() {
  cat <<'EOF'
Simple Skills — session helper

  session.sh help                 This text
  session.sh doctor               Check Work layout + pointer + tools
  session.sh work-root            Ensure .agent-work (+ nested git)
  session.sh new <slug>           Create Task-N-<slug> and set current
  session.sh set <dir|slug>       Point .current at an existing session
  session.sh current              Print active session path
  session.sh status [dir]         Progress from TASKS.md (source of truth)

Related (from repo / host root):
  python .agents/tools/session/validate_artifacts.py
  python .agents/tools/session/lint_artifacts.py
  python .agents/tools/session/build_context.py

Docs: .agents/START_HERE.md · .agents/WHAT_NEXT.md · .agents/MIGRATION.md
EOF
}

cmd_doctor() {
  ensure_work
  printf 'DOCTOR root=%s\n' "$ROOT"
  printf 'work=%s\n' "$WORK_DIR"
  if [ -d "$WORK_DIR/.git" ]; then
    printf 'nested_git=yes\n'
  else
    printf 'nested_git=no (run work-root / new to init)\n'
  fi
  if [ -f "$POINTER" ]; then
    rel="$(head -n1 "$POINTER" | tr -d '\r\n')"
    printf 'current=%s\n' "$rel"
    if [ -d "$ROOT/$rel" ]; then
      printf 'current_exists=yes\n'
    else
      printf 'current_exists=NO\n'
    fi
  else
    printf 'current=(unset)\n'
  fi
  gi="$ROOT/.gitignore"
  if [ -f "$gi" ] && grep -Fqx -- '.agent-work/' "$gi"; then
    printf 'gitignore_agent_work=yes\n'
  else
    printf 'gitignore_agent_work=MISSING — product git may track Work\n'
  fi
  for f in START_HERE.md WHAT_NEXT.md SKILL_PREAMBLE.md AGENT_POLICY.md; do
    if [ -f "$ROOT/.agents/$f" ] || [ -f "$ROOT/docs/$f" ]; then
      printf 'doc_%s=yes\n' "$f"
    else
      printf 'doc_%s=missing\n' "$f"
    fi
  done
  for t in validate_artifacts.py lint_artifacts.py build_context.py; do
    if [ -f "$ROOT/.agents/tools/session/$t" ] || [ -f "$ROOT/tools/session/$t" ]; then
      printf 'tool_%s=yes\n' "$t"
    else
      printf 'tool_%s=missing\n' "$t"
    fi
  done
  printf 'DOCTOR_DONE\n'
}

sub="${1:-}"; shift || true
case "$sub" in
  help|"" )  cmd_help "$@" ;;
  doctor)    cmd_doctor "$@" ;;
  current)   cmd_current "$@" ;;
  set)       cmd_set "$@" ;;
  new)       cmd_new "$@" ;;
  status)    cmd_status "$@" ;;
  work-root) cmd_work_root "$@" ;;
  *) die "Usage: session.sh {help|doctor|current|set <dir>|new <slug>|status [dir]|work-root}" ;;
esac
