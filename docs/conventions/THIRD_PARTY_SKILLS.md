# Third-Party Skills

The skills below are vendored from skills.sh sources. They were selected from
established maintainers, checked for a redistribution-friendly license, and
imported only when Gen Agent Trust Hub and Socket reported Safe / 0 alerts.
Skills with Snyk High Risk (for example `secrets-management`) were excluded.

| Category | Skills | Source | Revision | License |
|---|---|---|---|---|
| Web frontend | `web-component-design`, `accessibility-compliance` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Design system | `design-system-patterns`, `visual-design-foundations` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Frontend taste | `design-taste-frontend`, `minimalist-ui`, `high-end-visual-design`, `industrial-brutalist-ui`, `redesign-existing-projects` | [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | vendored MIT copy | MIT |
| Frontend taste (Anthropic) | `frontend-design` | [anthropics/skills](https://github.com/anthropics/skills) | `2235be7c60b551f5de82ade908fd3816455afcda` | Apache-2.0 |
| Apps | `expo-native-ui`, `expo-data-fetching` | [expo/skills](https://github.com/expo/skills) | `8d72763f53c4fe11ed3ae0441b921bda821d2a74` | MIT |
| Backend / API | `nodejs-backend-patterns`, `api-design-principles` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Database | `postgresql-table-design`, `sql-optimization-patterns`, `database-migration` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Networking | `microservices-patterns`, `hybrid-cloud-networking` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Architecture | `architecture-patterns`, `architecture-decision-records` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Security | `sast-configuration`, `auth-implementation-patterns`, `stride-analysis-patterns` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Testing | `javascript-testing-patterns`, `e2e-testing-patterns` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| DevOps / CI | `deployment-pipeline-design`, `github-actions-templates` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |
| Observability / debug | `distributed-tracing`, `debugging-strategies` | [wshobson/agents](https://github.com/wshobson/agents) | `b6af3711058190e4b5c5274b9758498fe626ec5a` | MIT |

### Upstream metadata exception (Expo)

`expo-native-ui` and `expo-data-fetching` keep their upstream
`agents/openai.yaml` files. That metadata is **optional host tooling only**.
They remain third-party skills: no first-party `Contract (mandatory)`, not listed
in `docs/config/first-party-skills.json`, and not validated as report/office skills.
Do not treat the presence of `openai.yaml` as a first-party signal.

Office document skills (`xlsx`, `docx`, `pptx`, `pdf`) are first-party Python
skills in this repository (MIT). Anthropic document skills were intentionally
not vendored: their license does not permit retaining or redistributing copies
outside Anthropic services.

## MIT License — wshobson/agents

Copyright (c) 2024 Seth Hobson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## MIT License — Expo

Copyright (c) 2025-present 650 Industries, Inc. (aka Expo)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Vendored from aix

<!-- AIX_VENDORED_SKILLS -->

| Category | Skills | Source | Revision | License |
|---|---|---|---|---|
| AI engineering | `3d-motion-pro`, `a11y-design-pro`, `a2a-protocol-pro`, `accounting-pro`, `ag-ui-pro`, `agent-evaluation-pro`, `ai-agents-pro`, `ai-design-pro`, `ai-integration-pro`, `ai-red-teaming-pro`, `algorithm-pro`, `android-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `angular-pro`, `api-design-pro`, `api-security-pro`, `auth-pro`, `aws-pro`, `azure-storage`, `blockchain-pro`, `bug-discovery-pro`, `bun-cli-pro`, `caching-pro`, `ci-cd-pro`, `claude-code-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `clean-architecture`, `clean-code-architecture-pro`, `cli-pro`, `cloud-native-agent-pro`, `cloudflare-pro`, `code-packaging-pro`, `code-review-pro`, `content-analysis-pro`, `cpp-pro`, `data-analysis-pro`, `data-engineering-pro`, `data-science-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `debugging-investigation`, `deploy-workflow`, `deployment-pro`, `design-system-pro`, `devrel-pro`, `discussing-pro`, `django-pro`, `docker-compose-pro`, `docker-pro`, `elasticsearch-pro`, `electron-pro`, `engineering-management-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `executing-pro`, `fastapi-pro`, `feedback-pro`, `figma-mcp-pro`, `financial-analysis-pro`, `fintech-integration-pro`, `flutter-pro`, `frontend-design-pro`, `frontend-patterns`, `fullstack-pro`, `fullstack-rag-pro`, `game-dev-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `gatekeeper`, `gemini-api-dev`, `git-operations-pro`, `git-worktree-pro`, `go-pro`, `graphql-pro`, `grill-me-pro`, `image-processing-pro`, `infrastructure-as-code-pro`, `ios-pro`, `java-pro`, `javascript-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `karpathy-coding-pro`, `kb-workflow`, `kubernetes-pro`, `machine-learning-pro`, `mapping-codebase`, `market-research-pro`, `mcp-server-pro`, `microservices-pro`, `mlops-pro`, `mobile-design-pro`, `mongodb-pro`, `motion-design-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `nestjs-neo4j-pro`, `nestjs-pro`, `network-infra-pro`, `nextjs-15-pro`, `nextjs-pro`, `nextjs-security-scan`, `ocr-pro`, `parallel-agents-pro`, `pdf-pro`, `performance-tuning-pro`, `platform-design-pro`, `postgres-patterns` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `postgresql-pro`, `prisma-postgres`, `product-management-pro`, `prompt-engineering-pro`, `python-pro`, `react-native-pro`, `react-pro`, `redis-pro`, `remember-pro`, `repo-tooling-pro`, `report-writer`, `router-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `rust-pro`, `security-pro`, `security-review`, `self-improve-agent-pro`, `senior-architect`, `senior-backend`, `senior-frontend`, `senior-security`, `seo-pro`, `shadcn-mastery-pro`, `skill-authoring`, `skill-creator-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `skills-self-review-pro`, `solidity-security`, `spring-boot-pro`, `sql-data-access-pro`, `strategic-consulting-pro`, `stream-rtc-pro`, `sustainable-design-pro`, `sync-custom-to-repo`, `system-design`, `system-design-pro`, `systematic-debugging-pro`, `tauri-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `technical-writing-pro`, `test-driven-development-pro`, `testing-pro`, `to-issues-pro`, `to-prd-pro`, `tool-discovery`, `ttd-pro`, `typescript-pro`, `ui-design-brain-pro`, `ui-reverse-engineer-pro`, `ui-stack-pro`, `ui-ux-system-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `using-aix`, `using-harness`, `ux-design-pro`, `vercel-deployment-pro`, `verification`, `verify-pro`, `vibe-coding-pro`, `vps-devops-pro`, `vue-pro`, `web-research-pro`, `websocket-pro`, `writing-skills` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |



| Category | Skills | Source | Revision | License |
|---|---|---|---|---|
| AI engineering | `3d-motion-pro`, `a11y-design-pro`, `a2a-protocol-pro`, `accounting-pro`, `ag-ui-pro`, `agent-evaluation-pro`, `ai-agents-pro`, `ai-design-pro`, `ai-integration-pro`, `ai-red-teaming-pro`, `algorithm-pro`, `android-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `angular-pro`, `api-design-pro`, `api-security-pro`, `auth-pro`, `aws-pro`, `azure-storage`, `blockchain-pro`, `bug-discovery-pro`, `bun-cli-pro`, `caching-pro`, `ci-cd-pro`, `claude-code-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `clean-architecture`, `clean-code-architecture-pro`, `cli-pro`, `cloud-native-agent-pro`, `cloudflare-pro`, `code-packaging-pro`, `code-review-pro`, `content-analysis-pro`, `cpp-pro`, `data-analysis-pro`, `data-engineering-pro`, `data-science-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `debugging-investigation`, `deploy-workflow`, `deployment-pro`, `design-system-pro`, `devrel-pro`, `discussing-pro`, `django-pro`, `docker-compose-pro`, `docker-pro`, `elasticsearch-pro`, `electron-pro`, `engineering-management-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `executing-pro`, `fastapi-pro`, `feedback-pro`, `figma-mcp-pro`, `financial-analysis-pro`, `fintech-integration-pro`, `flutter-pro`, `frontend-design-pro`, `frontend-patterns`, `fullstack-pro`, `fullstack-rag-pro`, `game-dev-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `gatekeeper`, `gemini-api-dev`, `git-operations-pro`, `git-worktree-pro`, `go-pro`, `graphql-pro`, `grill-me-pro`, `image-processing-pro`, `infrastructure-as-code-pro`, `ios-pro`, `java-pro`, `javascript-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `karpathy-coding-pro`, `kb-workflow`, `kubernetes-pro`, `machine-learning-pro`, `mapping-codebase`, `market-research-pro`, `mcp-server-pro`, `microservices-pro`, `mlops-pro`, `mobile-design-pro`, `mongodb-pro`, `motion-design-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `nestjs-neo4j-pro`, `nestjs-pro`, `network-infra-pro`, `nextjs-15-pro`, `nextjs-pro`, `nextjs-security-scan`, `ocr-pro`, `parallel-agents-pro`, `pdf-pro`, `performance-tuning-pro`, `platform-design-pro`, `postgres-patterns` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `postgresql-pro`, `prisma-postgres`, `product-management-pro`, `prompt-engineering-pro`, `python-pro`, `react-native-pro`, `react-pro`, `redis-pro`, `remember-pro`, `repo-tooling-pro`, `report-writer`, `router-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `rust-pro`, `security-pro`, `security-review`, `self-improve-agent-pro`, `senior-architect`, `senior-backend`, `senior-frontend`, `senior-security`, `seo-pro`, `shadcn-mastery-pro`, `skill-authoring`, `skill-creator-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `skills-self-review-pro`, `solidity-security`, `spring-boot-pro`, `sql-data-access-pro`, `strategic-consulting-pro`, `stream-rtc-pro`, `sustainable-design-pro`, `sync-custom-to-repo`, `system-design`, `system-design-pro`, `systematic-debugging-pro`, `tauri-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `technical-writing-pro`, `test-driven-development-pro`, `testing-pro`, `to-issues-pro`, `to-prd-pro`, `tool-discovery`, `ttd-pro`, `typescript-pro`, `ui-design-brain-pro`, `ui-reverse-engineer-pro`, `ui-stack-pro`, `ui-ux-system-pro` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |
| AI engineering | `using-aix`, `using-harness`, `ux-design-pro`, `vercel-deployment-pro`, `verification`, `verify-pro`, `vibe-coding-pro`, `vps-devops-pro`, `vue-pro`, `web-research-pro`, `websocket-pro`, `writing-skills` | [truongnat/aix](https://github.com/truongnat/aix) | `26381fc6b35fff7fcf312313649d7c379c97fc24` | MIT |

