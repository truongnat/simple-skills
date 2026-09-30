# Gate decision evidence

Use this compact record before allowing a protected next command:

```yaml
decision: allow | block | defer
requested_action: <exact next command or action>
verification:
  status: fresh | stale | pending | blocked
  artifact: <path or artifact ID>
  checked_at: <timestamp>
review:
  status: passed | findings_open | not_required
  artifact: <path or artifact ID>
blockers: []
reason: <evidence-based explanation>
next_step: <command, owner, or question>
```

Allow only when verification is fresh, required review findings are resolved, blockers are empty, and the requested action is within the declared scope. Block when evidence is missing or stale; defer when a named owner or user decision is required.
