# Cloud-Native Agent Integration Map

## sk-ai-integration-pro

- **When**: Designing the agent logic that runs on K8s.
- **Ownership split**:
  - `sk-cloud-native-agent-pro`: Infrastructure, deployment, scaling.
  - `sk-ai-integration-pro`: Agent logic, prompts, tools, RAG.

## sk-docker-pro

- **When**: Building container images for agents.
- **Ownership split**:
  - `sk-cloud-native-agent-pro`: K8s deployment and orchestration.
  - `sk-docker-pro`: Dockerfile, multi-stage build, image optimization.

## sk-mcp-server-pro

- **When**: Deploying MCP servers as K8s services.
- **Ownership split**:
  - `sk-cloud-native-agent-pro`: K8s Service discovery and networking.
  - `sk-mcp-server-pro`: MCP server design, transport, auth.

## sk-infrastructure-as-code-pro

- **When**: Managing K8s manifests with IaC tools.
- **Ownership split**:
  - `sk-cloud-native-agent-pro`: What to deploy and why.
  - `sk-infrastructure-as-code-pro`: Terraform / Pulumi / Helm implementation.

## sk-network-infra-pro

- **When**: Designing service mesh or ingress for agents.
- **Ownership split**:
  - `sk-cloud-native-agent-pro`: Agent-specific networking needs.
  - `sk-network-infra-pro`: Service mesh, ingress, TLS termination.
