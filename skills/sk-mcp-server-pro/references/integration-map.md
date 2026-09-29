# MCP Server Integration Map

## When to combine with other skills

### sk-api-design-pro

- **When**: The MCP server wraps a broader HTTP API.
- **Ownership split**:
  - `sk-mcp-server-pro`: MCP primitives, transport, auth at the MCP boundary.
  - `sk-api-design-pro`: REST endpoint design, pagination, versioning, idempotency, rate limiting at the HTTP layer.

### sk-security-pro

- **When**: Threat modeling, penetration testing, defense-in-depth.
- **Ownership split**:
  - `sk-mcp-server-pro`: Input validation, auth middleware, audit logging at the MCP boundary.
  - `sk-security-pro`: Broader threat model, abuse scenarios, infrastructure hardening.

### sk-auth-pro

- **When**: OAuth 2.1, identity federation, SSO, token lifecycle.
- **Ownership split**:
  - `sk-mcp-server-pro`: OAuth 2.1 integration into the MCP server (endpoints, scopes).
  - `sk-auth-pro`: Identity architecture, token rotation, federation protocols, break-glass.

### sk-docker-pro / sk-deployment-pro

- **When**: Packaging and deploying the MCP server.
- **Ownership split**:
  - `sk-mcp-server-pro`: Server code, health checks, graceful shutdown.
  - `sk-docker-pro`: Dockerfile, multi-stage build, image scanning.
  - `sk-deployment-pro`: Rollout strategy, canary, rollback.

### sk-testing-pro / sk-ci-cd-pro

- **When**: Regression testing, CI integration.
- **Ownership split**:
  - `sk-mcp-server-pro`: MCP Inspector validation, client integration tests.
  - `sk-testing-pro`: Test pyramid, flaky test diagnosis, property-based testing.
  - `sk-ci-cd-pro`: Pipeline config, test gates, artifact publishing.
