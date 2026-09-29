# CLI — integration map

| Skill | When |
|-------|------|
| **`sk-code-packaging-pro`** | Entry points, `bin`, publish, semver for argv contract |
| **`sk-security-pro`** | Secrets (env vs argv), dangerous defaults, path traversal |
| **`sk-testing-pro`** | Golden `--help`, subprocess tests, exit code assertions |
| **`sk-javascript-pro`** | Node `bin`, ESM/CJS, shebang, `npx` behavior |
| **`sk-typescript-pro`** | Typed argv boundaries if using TS for CLI |
| **`sk-docker-pro`** | CLI inside container (TTY, `-i`, PATH), exec non-interactive |
| **`sk-repo-tooling-pro`** | Internal repo scripts vs shipped user-facing CLIs |

**Boundary:** **`sk-cli-pro`** owns **argv UX**, **stdio/exit contracts**, **signals/pipes**, **completions conceptually**; runtime-specific APIs stay in language skills and parse libraries’ docs.
