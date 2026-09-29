# A2A Integration Map

## sk-mcp-server-pro

- **When**: Each agent needs MCP tool access.
- **Ownership split**:
  - `sk-a2a-protocol-pro`: Agent coordination, task delegation.
  - `sk-mcp-server-pro`: Tool design, transport, auth for each agent's tools.

## sk-ai-integration-pro

- **When**: Designing the LLM and reasoning inside each agent.
- **Ownership split**:
  - `sk-a2a-protocol-pro`: Inter-agent communication.
  - `sk-ai-integration-pro`: Intra-agent reasoning, prompts, RAG.

## sk-api-design-pro

- **When**: A2A interacts with broader HTTP APIs.
- **Ownership split**:
  - `sk-a2a-protocol-pro`: A2A protocol implementation.
  - `sk-api-design-pro`: REST/GraphQL API design for non-agent endpoints.

## sk-security-pro

- **When**: Threat modeling multi-agent attack surface.
- **Ownership split**:
  - `sk-a2a-protocol-pro`: A2A auth, capability scoping.
  - `sk-security-pro`: Infrastructure hardening, pentesting, abuse scenarios.
