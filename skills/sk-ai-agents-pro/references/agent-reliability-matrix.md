# Agent reliability matrix

Use this matrix before granting an agent autonomy or side effects. Record goal, allowed tools, data scope, memory policy, approval boundary, timeout, retry budget, and expected evidence.

| Risk | Scenario | Expected evidence |
|---|---|---|
| Tool misuse | Agent receives an ambiguous or destructive request | Typed validation, authorization, and approval gate before side effect |
| Prompt injection | Tool result contains instructions to change agent policy | Result treated as untrusted data; policy remains intact |
| Retry loop | Tool/network failure repeats | Bounded retry with backoff, timeout, and terminal explanation |
| State corruption | Agent resumes after partial completion | Checkpoint is idempotent and recovery state is explicit |
| Memory leakage | New task/tenant reads prior context | Scoped memory and access-control evidence |
| Multi-agent conflict | Agents produce incompatible plans | Coordinator validates schema, ownership, and conflict resolution |
| Human handoff | Confidence or risk threshold is exceeded | Human receives context, proposed action, and reason for escalation |
| Cost/latency drift | Long context or tool fan-out grows unexpectedly | Budget guard, trace, and abort behavior |

A release gate should include one positive, one denied-action, one tool-failure, one recovery, and one adversarial-context scenario.
