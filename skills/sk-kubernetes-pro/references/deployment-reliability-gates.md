# Kubernetes deployment reliability gates

| Gate | Expected evidence |
|---|---|
| Scheduling | Requests/limits, affinity/taints, capacity and disruption budget are compatible |
| Startup/readiness | Startup, readiness, and liveness probes represent distinct states |
| Rollout | Strategy, max unavailable/surge, progress deadline, and pause trigger are explicit |
| Traffic | Service/Ingress routing, graceful termination, connection draining, and TLS are verified |
| Security | Service account, RBAC, Pod Security, network policy, and secret source are least-privilege |
| State | PVC/storage backup, ordering, and recovery behavior are documented |
| Observability | Logs, metrics, traces, alerts, and correlation identifiers are available |
| Failure | CrashLoop, node loss, dependency outage, image pull failure, and rollback are rehearsed |

Do not treat a successful apply as a healthy deployment; require rollout health, application probes, traffic behavior, and rollback evidence.
