# Router precedence and ambiguity matrix

| Decision | Evidence | Action |
|---|---|---|
| Explicit skill named | User names a concrete skill and scope fits | Route directly; do not broaden unnecessarily |
| Single domain match | One owner has clear boundary and required inputs | Select it and state handoff |
| Multiple matches | Trigger overlap or adjacent ownership | Compare boundaries, choose primary owner, list collaborators |
| Missing context | Product, file intent, version or decision materially changes route | Ask the smallest clarifying question |
| Conflicting skills | Two owners claim the same artifact | Prefer canonical owner; record why the other is supporting |
| High-risk side effect | Ship/delete/publish/security/account action | Require explicit evidence and gate before execution |

Routing evidence should include user intent, current state, candidate skills, chosen owner, assumptions, unresolved ambiguity and next handoff. Never route from filenames alone when file content changes the decision.
