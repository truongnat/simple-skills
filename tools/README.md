# Agent tools

Each local tool has its own folder. Installers copy this tree to
`.agents/tools/`.

| Tool | Purpose |
|---|---|
| [`choice-reader/`](./choice-reader/) | Read the latest matching user choice from decision JSONL logs. |
| [`decision-server/`](./decision-server/) | Serve visual decision HTML with shared styles, receive browser events, and log user choices. |
| [`policy/`](./policy/) | Security boundary: redact secrets/PII before disk, guard dangerous shell commands, budget hard-stop for paid provider calls. |
| [`providers/`](./providers/) | Compile the skill catalog for a provider (claude / cursor / codex / gemini). |
| [`session-serve/`](./session-serve/) | Find the latest visual-decision session and launch the decision server. |
| [`session/`](./session/) | Work-layer session state machine: step ledger, artifact validation, nested git commit (auto-redacts via policy). |
| [`video-keyframes/`](./video-keyframes/) | Sample video recordings into timestamped image evidence for agent analysis. |

## policy/

Security boundary ported from aix `@x/policy` + `@x/core` budget, dependency-free:

```bash
# Redact secrets/PII from stdin or a file (in place with --write)
echo "api_key=abcdefghijklmnop12345678 dev@example.com" | python3 policy/redact.py
python3 policy/redact.py PLAN.md --write --report

# Guard a shell command before the agent runs it
python3 policy/denylist.py "rm -rf /"          # DENIED, exit 1
python3 policy/denylist.py "ls -la"            # ALLOWED, exit 0

# Budget hard-stop for paid provider loops
python3 policy/budget.py check --usd-spent 10.01 --usd-limit 10   # exit 1
```

`session.sh commit` auto-redacts `.md/.txt/.json/.yaml/.log/.csv` files in the
Work layer before the nested-git commit. `session.sh policy` reports health.

## providers/

Compile the 222-skill catalog to a provider layout (port of aix `@x/providers`):

```bash
python3 providers/compile.py --provider claude --skills-root skills --target out
python3 providers/compile.py --provider all --skills-root skills --target out
sk compile --provider cursor     # via the sk CLI
```

Emits provider-specific trees: `.claude-plugin/` + `content/skills/` (claude),
`.cursor/rules/*.mdc` (cursor), `.codex/skills/` (codex), `.agents/skills/` +
`gemini-extension.json` (gemini).
