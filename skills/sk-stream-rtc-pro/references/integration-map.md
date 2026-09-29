# Stream / RTC — integration map

| Skill | Combine when |
|-------|----------------|
| **`sk-websocket-pro`** | Signaling channel reliability, reconnect, backpressure, message ordering. |
| **`sk-performance-tuning-pro`** | End-to-end latency, CPU/GPU, thread scheduling, tail QoE. |
| **`sk-security-pro`** | DTLS/SRTP assumptions, token handling, recording/consent, abuse cases. |
| **`sk-deployment-pro`** | TURN geo, SFU autoscale, CDN for broadcast fallback, rollout. |
| **`sk-network-infra-pro`** | UDP blocked paths, firewall allowlists, DNS/TLS to TURN/SFU edges. |
| **`sk-nestjs-pro`** / **`sk-nextjs-pro`** | Signaling/control REST or WebSocket backends, auth at join. |
| **`sk-react-native-pro`** | Mobile capture/background lifecycle, native RTC modules. |
| **`sk-api-design-pro`** | Pure HTTP control-plane API design without media semantics. |

**Boundary:** **`sk-stream-rtc-pro`** owns **media path, session lifecycle, ICE/TURN topology, and QoS policy**; **`sk-api-design-pro`** owns **generic HTTP API** shape when signaling is not the primary topic.
