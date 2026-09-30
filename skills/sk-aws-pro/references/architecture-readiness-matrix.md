# AWS architecture readiness matrix

| Well-Architected concern | Readiness evidence |
|---|---|
| Security | IAM trust/policy review, boundary controls, encryption/key ownership, audit trail |
| Reliability | Multi-AZ dependency map, backup/restore test, health checks, failover and quota plan |
| Performance | Workload profile, scaling trigger, latency target, bottleneck and capacity headroom |
| Cost | Unit-cost model, tagging, retention, idle-resource detection, budget alert |
| Operations | IaC plan, deployment/rollback, observability, incident owner and runbook |
| Sustainability | Utilization, lifecycle/retention, right-sizing, and workload efficiency assumptions |

For each resource record region/AZ, data classification, dependency, failure mode, owner, recovery point/time objective, and evidence source. A diagram or Terraform plan alone is not proof of readiness.
