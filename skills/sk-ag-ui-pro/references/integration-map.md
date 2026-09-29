# AG-UI Integration Map

## sk-ai-integration-pro

- **When**: Designing the agent backend that powers the UI.
- **Ownership split**:
  - `sk-ag-ui-pro`: Frontend components, state sync, user interaction.
  - `sk-ai-integration-pro`: Agent backend, prompts, tools, RAG.

## sk-frontend-design-pro

- **When**: Designing the visual aesthetic and component style.
- **Ownership split**:
  - `sk-ag-ui-pro`: Agent-interactive components and patterns.
  - `sk-frontend-design-pro`: Visual design, accessibility, brand consistency.

## sk-react-pro / sk-nextjs-pro

- **When**: Implementing in React / Next.js.
- **Ownership split**:
  - `sk-ag-ui-pro`: Agent-specific components and state management.
  - `sk-react-pro` / `sk-nextjs-pro`: Framework patterns, routing, SSR considerations.

## sk-a2a-protocol-pro

- **When**: Frontend interacts with a multi-agent system.
- **Ownership split**:
  - `sk-ag-ui-pro`: Frontend integration with the Gateway or coordinator.
  - `sk-a2a-protocol-pro`: Multi-agent orchestration behind the frontend.

## sk-auth-pro

- **When**: UI needs user authentication and authorization.
- **Ownership split**:
  - `sk-ag-ui-pro`: Auth UI components (login, logout, session display).
  - `sk-auth-pro`: Auth architecture, token lifecycle, session management.
