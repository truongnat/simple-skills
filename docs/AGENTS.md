# Agent Rules

This is the **short entrypoint** for AI agents. Follow it strictly, then read the
detailed policy.

## Must-read order (every task)

1. `.agents/settings.yaml` and `.agents/PRJ_REFERENCE.md`
2. `.agents/SKILL_PREAMBLE.md` (Language + Work layout + Memory + Thinking
   methods + **Readable writing**) when invoking a first-party skill —
   artifacts live under `.agent-work/`; write so a teammate understands on
   first pass
3. `.agents/AGENT_POLICY.md` — **full** settings, security, workflow, gates, artifacts
4. `.agents/AGENT_WORK.md` when unsure about Kit vs Work
5. The skill’s `SKILL.md` Contract (and step files when present)

Re-read settings at the start of every task and every skill invocation. Never
cache `language` or other settings across turns. Default language: `en`.

## Architecture (map)

| Path | Role |
| --- | --- |
| `AGENTS.md` | This short entrypoint |
| `.agents/` | **Kit** — skills, tools, settings, policy (installer) |
| `.agents/AGENT_POLICY.md` | Detailed mandatory policy |
| `.agents/settings.yaml` | Lean knobs: language, branch, report format, docs |
| `.agents/PRJ_REFERENCE.md` | Generated project facts |
| `.agents/SKILL_PREAMBLE.md` | Language, Work, Memory, Thinking, Readable writing, Scale |
| `.agents/skills/` | Invokable skills (+ `office-common` helper) |
| `.agents/tools/` | session, decision-server, choice-reader, … |
| `.agent-work/` | **Work** — sessions + memory (nested git; see AGENT_WORK.md) |
| `.agent-work/sessions/` | Per-task artifacts; pointer `.current` |
| `.agent-work/memory/` | Durable lessons (vital few) (`done` writes) |
| `.agents/DESIGN_SYSTEM.md` | HTML report theme |
| `.agents/CODE_COMMENTS.md` | Comment convention |
| `.agents/THIRD_PARTY_SKILLS.md` | Vendored attributions |

### Skill architecture

- `SKILL.md` is authoritative. First-party skills have **Contract (mandatory)** +
  `agents/openai.yaml`.
- Inventory: repo `docs/first-party-skills.json`. Install packs:
  `docs/install-profiles.json` (`core` default; `office` / `frontend` / `backend` / `all`).
- Third-party skills keep upstream structure; Expo may ship `openai.yaml` without
  being first-party (see THIRD_PARTY_SKILLS.md).
- Validate: `python scripts/validate_skills.py` and
  `python .agents/tools/session/validate_artifacts.py`.
- Kit vs Work layout: [docs/AGENT_WORK.md](./AGENT_WORK.md) (installed as
  `.agents/AGENT_WORK.md`).

## Skill compliance

1. Read preamble (when pointed) → `SKILL.md` fully → obey Contract.
2. Produce required artifacts; stop when safety or Spec quality blocks.
3. Do not rely on `agents/openai.yaml` alone.
4. Before `review` pass / `done` complete, run artifact schema validation on the
   active session (see AGENT_POLICY.md).

## Hard stops (summary)

Full text in `.agents/AGENT_POLICY.md`. Never: leak secrets; send code off-machine
without consent; run irreversible destructive commands without confirmation;
weaken auth/validation/TLS; introduce injection; add untrusted dependencies
silently; hide security findings.

## Workflow (summary)

- One active session via `bash .agents/tools/session/session.sh current|new|status`.
- Choose **Quick / Lite / Full** once (see AGENT_POLICY Scale & Quick path).
- Full lifecycle: brainstorming → (BA) → design → planning → sync → execution →
  review → done. Quick skips BA/design/Spec matrices; Lite may skip BA/design.
- Brainstorming: **diverge then converge**; one focused question per message when clarifying.
- Planning TASK cards need **Dev context** with `[Source: …]` (no inventing).
- Sync sets **Implementation readiness** `PASS` | `CONCERNS` | `FAIL` before execution.
- Progress from `session.sh status` only; `COMPLETE: yes` required for done.
- Reports: short executive summary + developer overview; **Readable writing** mandatory.

## Detailed policy

**Everything else lives in** `.agents/AGENT_POLICY.md` (Security, Office skills,
Decision/visual gates, Video evidence, Contract table, Session discipline,
Memory, Lifecycle, Post-done loop, Docs wiki, Artifact format/quality, DX).
If this entrypoint and the policy conflict, **AGENT_POLICY.md wins** on detail;
this file wins only as the required reading order.
