# WebSocket — integration map

| Skill | Combine when |
|-------|----------------|
| **`sk-security-pro`** | AuthZ per event, rate limits, token leakage, CSRF on cookie auth upgrades. |
| **`sk-performance-tuning-pro`** | Kernel tuning, GC pauses, event loop lag under fan-out. |
| **`sk-stream-rtc-pro`** | WebRTC signaling often rides WebSocket — separate media from signaling concerns. |
| **`sk-nestjs-pro` / `sk-nextjs-pro`** | Framework gateway adapters, middleware order. |
| **`sk-deployment-pro`** | Ingress idle timeouts, TLS termination, sticky sessions. |
| **`sk-network-infra-pro`** | L4/L7 idle timeouts, TCP keepalive vs app heartbeat, path to upgrade. |
| **`sk-api-design-pro`** | Idempotent command handlers, dedup keys for at-least-once delivery. |

**Boundary:** `sk-websocket-pro` owns connection semantics; infra specifics split per deployment skill.
