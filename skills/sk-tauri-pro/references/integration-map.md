# Tauri — integration map

| Skill | Combine when |
|-------|----------------|
| **`sk-react-pro`** | Webview UI (hooks, state, a11y, perf) — not invoke/Rust boundary. |
| **`sk-typescript-pro`** | Typed `invoke` contracts, shared DTO types across web/Rust boundary. |
| **`sk-security-pro`** | CSP, capability review, path/open-url/shell policies, threat modeling. |
| **`sk-testing-pro`** | Rust tests, Playwright/Cypress against packaged app, CI matrices. |
| **`sk-deployment-pro`** | Installers, signing, notarization, updater channels. |
| **`sk-performance-tuning-pro`** | Large IPC payloads, startup latency, memory churn. |
| **`sk-docker-pro`** | Cross-compile Linux/Windows containers for CI. |
| **`sk-electron-pro`** | **Comparison only** — not for implementing Tauri. |

**Boundary:** **`sk-tauri-pro`** owns **Tauri config, Rust commands, capabilities, packaging, updater**; SPA internals → **`sk-react-pro`** (or other UI skill).
