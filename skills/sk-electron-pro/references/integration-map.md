# Electron — integration map

| Combined skill | Why | `sk-electron-pro` owns | Other skill owns |
|----------------|-----|----------------------|------------------|
| **`sk-react-pro`** | Renderer UI | IPC contracts, `webPreferences` | Components, hooks |
| **`sk-security-pro`** | Threat model | IPC hardening, sandbox narrative | Org-wide policies |
| **`sk-testing-pro`** | E2E | Playwright Electron harness | Test cases |
| **`sk-deployment-pro`** | Release | Channels, artifacts | Infra outside desktop |
| **`sk-ci-cd-pro`** | Build matrix | electron-builder/Forge in CI | Workflow YAML, cache |
| **`sk-design-system-pro`** | Dense desktop UI | IPC boundaries | Shortcuts, density, focus |
| **`sk-docker-pro`** | Headless CI / Linux packaging tests | Electron test harness assumptions | Container base images |
| **`sk-tauri-pro`** | Alternative stack | — | Tauri-only patterns |

**Handoff:** Signing/notarization steps often need **platform** docs + Apple/Microsoft accounts — document owner.
