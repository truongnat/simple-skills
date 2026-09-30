# Repository tooling capability and artifact lifecycle

| Goal | Preconditions | Command family | Evidence |
|---|---|---|---|
| Skill content changed | Repo root, `dist/` state known | `validate-skills`, then `build-skill-index` | Validator result and index timestamp/hash |
| KB docs changed | Corpus scope and memory budget known | `build-kb`, then `verify-kb` | Build manifest, verification result, freshness |
| Many local questions | KB built and query scope known | `query-kb-batch` | Batch size, duration, result count, errors |
| Project map/wiki | Source path and output target known | `index-project`, `generate-wiki` | Output path, source revision, warnings |
| Missing artifact | Build trigger confirmed | Build only the relevant artifact | Before/after existence and version |

Do not rebuild unrelated indexes. Record cwd, tool version, inputs, outputs, memory/batch assumptions, staleness and safe fallback when a preferred capability is unavailable.
