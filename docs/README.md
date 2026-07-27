# Docs layout (source)

Kit prose and machine config live here. On install, most files are **flattened**
into `.agents/` for agent UX; Thinking methods keep a subfolder.

Do **not** treat this tree as the runtime path. Agents on a host project read
`.agents/…` (and root `AGENTS.md`).

## Taxonomy

| Folder | Role | Install target |
| --- | --- | --- |
| [`AGENTS.md`](./AGENTS.md) | Short host entrypoint | Project root `AGENTS.md` |
| [`guides/`](./guides/) | Start, routing, upgrade, BA alias map | `.agents/<file>` (flat) |
| [`policy/`](./policy/) | Shared preamble, full policy, Kit vs Work | `.agents/<file>` (flat) |
| [`thinking/`](./thinking/) | Session-wide Thinking methods (normative detail) | `.agents/thinking/<file>` |
| [`conventions/`](./conventions/) | Code comments, design system, third-party skills | `.agents/<file>` (flat) |
| [`config/`](./config/) | Settings defaults, schemas, profiles, gitignore snippet | `.agents/settings.yaml`, `.agents/tools/session/artifact-schemas.json`, installer inputs |
| [`examples/`](./examples/) | Good/bad session shapes | `.agents/examples/` |

## Reading order (agents)

1. Root `AGENTS.md` → `.agents/START_HERE.md`
2. `.agents/settings.yaml` (+ `PRJ_REFERENCE.md` after `init`)
3. `.agents/SKILL_PREAMBLE.md` when invoking a first-party skill
4. Skill `SKILL.md` Contract
5. Deep dives only when needed: `AGENT_POLICY.md`, `AGENT_WORK.md`,
   `.agents/thinking/…`, `MIGRATION.md`

## Thinking methods

Index: [`thinking/README.md`](./thinking/README.md).

Ops summary stays in `policy/SKILL_PREAMBLE.md` → Thinking methods.
Full normative text lives under `thinking/` (progressive disclosure).

## Source vs installed path cheat sheet

| Source | Installed |
| --- | --- |
| `docs/AGENTS.md` | `AGENTS.md` |
| `docs/guides/START_HERE.md` | `.agents/START_HERE.md` |
| `docs/guides/WHAT_NEXT.md` | `.agents/WHAT_NEXT.md` |
| `docs/guides/MIGRATION.md` | `.agents/MIGRATION.md` |
| `docs/guides/BA_SKILLS.md` | `.agents/BA_SKILLS.md` |
| `docs/policy/SKILL_PREAMBLE.md` | `.agents/SKILL_PREAMBLE.md` |
| `docs/policy/AGENT_POLICY.md` | `.agents/AGENT_POLICY.md` |
| `docs/policy/AGENT_WORK.md` | `.agents/AGENT_WORK.md` |
| `docs/thinking/outcome-first.md` | `.agents/thinking/outcome-first.md` |
| `docs/thinking/input-process-output.md` | `.agents/thinking/input-process-output.md` |
| `docs/thinking/make-implicit-explicit.md` | `.agents/thinking/make-implicit-explicit.md` |
| `docs/thinking/small-batch.md` | `.agents/thinking/small-batch.md` |
| `docs/conventions/CODE_COMMENTS.md` | `.agents/CODE_COMMENTS.md` |
| `docs/conventions/DESIGN_SYSTEM.md` | `.agents/DESIGN_SYSTEM.md` |
| `docs/conventions/THIRD_PARTY_SKILLS.md` | `.agents/THIRD_PARTY_SKILLS.md` |
| `docs/config/settings.yaml` | `.agents/settings.yaml` (merge on install) |
| `docs/config/artifact-schemas.json` | `.agents/tools/session/artifact-schemas.json` |
| `docs/examples/` | `.agents/examples/` |
