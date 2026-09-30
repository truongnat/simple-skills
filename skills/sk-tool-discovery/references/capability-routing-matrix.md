# Tool capability routing matrix

| Needed capability | Discover/check | Safe fallback | Record |
|---|---|---|---|
| Read/search files | File tools, `rg`, repository search | Narrow `find` + direct read | Scope and freshness |
| Inspect Git state | `git status`, `git diff`, `git log` | Read-only equivalent | Branch, HEAD, dirty files |
| Validate content | Repo validator/test command | Small deterministic checker | Command and result |
| Render/inspect artifact | Renderer or format-specific inspector | Structural check with limitation | Artifact, version, skipped visual checks |
| External fact | Approved web/source route | Block or ask for source | URL/path, date, provenance |
| High-impact action | Capability plus authorization | Stop and request confirmation | Exact payload and gate evidence |

Route by capability, not by remembered tool name. If no safe fallback exists, report the missing capability instead of simulating success.
