# Báo cáo phân nhóm skills — simple-skills

**Phạm vi:** chỉ thư mục `skills/` của repo hiện tại
**Nguồn:** 222 thư mục `skills/sk-*/` và `SKILL.md` tương ứng
**Nguyên tắc:** phân nhóm theo chức năng chính; một số skill có thể hợp lý ở nhiều nhóm nhưng được đặt một lần ở nhóm sở hữu chính.

## 1. Tổng quan

Repo `simple-skills` là một catalog gồm **222 reusable Agent Skills** cho coding, architecture, product, design, security, data và operations. Tất cả skill đều tuân theo quy ước:

```text
skills/sk-<skill-name>/SKILL.md
```

Có thể nhìn catalog như 3 lớp:

1. **Lifecycle/process:** định hướng yêu cầu, thiết kế, lập kế hoạch, thực thi, review và xác minh.
2. **Domain/technology:** architecture, backend, frontend, mobile, data, AI, security, cloud và database.
3. **Meta/tooling:** routing, Git, skill authoring, repo tooling, agent coordination và knowledge workflow.

## 2. Taxonomy 10 nhóm

### Nhóm 01 — Quy trình phát triển & phân tích yêu cầu — 33 skill

Bao phủ từ làm rõ ý tưởng, BA/spec, thiết kế sơ bộ/chi tiết, lập kế hoạch, thực thi, review đến đóng task.

`sk-api-ba`, `sk-ba-dashboard`, `sk-ba-handoff`, `sk-ba-integrate`, `sk-ba-kg`, `sk-ba-test`, `sk-basic-design`, `sk-brainstorming`, `sk-business-analysis`, `sk-detail-design`, `sk-discussing-pro`, `sk-done`, `sk-executing-pro`, `sk-execution`, `sk-gap-analysis`, `sk-grill-me-pro`, `sk-init`, `sk-investigate`, `sk-planning`, `sk-quick-fix`, `sk-review`, `sk-review-pr`, `sk-scaffold`, `sk-specify`, `sk-story-spec`, `sk-sync`, `sk-tester`, `sk-to-issues-pro`, `sk-to-prd-pro`, `sk-user-flow`, `sk-ux-wireframe`, `sk-verification`, `sk-verify-pro`

**Luồng trung tâm:**

```text
brainstorm/discuss → business-analysis/specify → basic-design → detail-design
→ planning → execution → review → verification → done
```

### Nhóm 02 — Kiến trúc, API & backend — 18 skill

Bao phủ thiết kế hệ thống, boundary, API contract, authentication, backend pattern, microservices và realtime backend.

`sk-api-design-principles`, `sk-api-design-pro`, `sk-architecture-decision-records`, `sk-architecture-patterns`, `sk-clean-architecture`, `sk-clean-code-architecture-pro`, `sk-fullstack-pro`, `sk-graphql-pro`, `sk-microservices-patterns`, `sk-microservices-pro`, `sk-nestjs-pro`, `sk-nestjs-neo4j-pro`, `sk-nodejs-backend-patterns`, `sk-senior-architect`, `sk-senior-backend`, `sk-system-design`, `sk-system-design-pro`, `sk-websocket-pro`

### Nhóm 03 — Ngôn ngữ & framework ứng dụng — 28 skill

Các skill chuyên sâu theo ngôn ngữ/framework, cùng một số stack app cụ thể.

`sk-algorithm-pro`, `sk-android-pro`, `sk-angular-pro`, `sk-blockchain-pro`, `sk-bun-cli-pro`, `sk-cpp-pro`, `sk-django-pro`, `sk-electron-pro`, `sk-expo-data-fetching`, `sk-expo-native-ui`, `sk-fastapi-pro`, `sk-flutter-pro`, `sk-game-dev-pro`, `sk-go-pro`, `sk-ios-pro`, `sk-java-pro`, `sk-javascript-pro`, `sk-javascript-testing-patterns`, `sk-nextjs-15-pro`, `sk-nextjs-pro`, `sk-python-pro`, `sk-react-native-pro`, `sk-react-pro`, `sk-rust-pro`, `sk-spring-boot-pro`, `sk-tauri-pro`, `sk-typescript-pro`, `sk-vue-pro`

### Nhóm 04 — Data, AI & agent systems — 17 skill

Bao phủ AI/LLM integration, agent, multi-agent protocol, evaluation, RAG, ML/MLOps và xử lý nội dung multimodal.

`sk-a2a-protocol-pro`, `sk-ag-ui-pro`, `sk-agent-evaluation-pro`, `sk-ai-agents-pro`, `sk-ai-design-pro`, `sk-ai-integration-pro`, `sk-cloud-native-agent-pro`, `sk-content-analysis-pro`, `sk-data-analysis-pro`, `sk-data-engineering-pro`, `sk-data-science-pro`, `sk-fullstack-rag-pro`, `sk-gemini-api-dev`, `sk-machine-learning-pro`, `sk-mlops-pro`, `sk-prompt-engineering-pro`, `sk-stream-rtc-pro`

### Nhóm 05 — Frontend, UI/UX & visual design — 29 skill

Bao phủ frontend patterns, design system, accessibility, responsive/mobile design, visual style, motion, Figma và SEO giao diện.

`sk-3d-motion-pro`, `sk-a11y-design-pro`, `sk-accessibility-compliance`, `sk-design-system-patterns`, `sk-design-system-pro`, `sk-design-taste-frontend`, `sk-figma-mcp-pro`, `sk-frontend-design`, `sk-frontend-design-pro`, `sk-frontend-patterns`, `sk-high-end-visual-design`, `sk-image-processing-pro`, `sk-industrial-brutalist-ui`, `sk-minimalist-ui`, `sk-mobile-design-pro`, `sk-motion-design-pro`, `sk-platform-design-pro`, `sk-redesign-existing-projects`, `sk-senior-frontend`, `sk-seo-pro`, `sk-shadcn-mastery-pro`, `sk-sustainable-design-pro`, `sk-ui-design-brain-pro`, `sk-ui-reverse-engineer-pro`, `sk-ui-stack-pro`, `sk-ui-ux-system-pro`, `sk-ux-design-pro`, `sk-visual-design-foundations`, `sk-web-component-design`

### Nhóm 06 — Security, testing & reliability — 20 skill

Bao phủ threat modeling, application/API/AI security, secure auth, SAST, debugging, performance, test strategy và E2E.

`sk-ai-red-teaming-pro`, `sk-api-security-pro`, `sk-auth-implementation-patterns`, `sk-auth-pro`, `sk-bug-discovery-pro`, `sk-debugging-investigation`, `sk-debugging-strategies`, `sk-distributed-tracing`, `sk-e2e-testing-patterns`, `sk-nextjs-security-scan`, `sk-performance-tuning-pro`, `sk-sast-configuration`, `sk-security-pro`, `sk-security-review`, `sk-senior-security`, `sk-solidity-security`, `sk-stride-analysis-patterns`, `sk-systematic-debugging-pro`, `sk-test-driven-development-pro`, `sk-testing-pro`

### Nhóm 07 — Cloud, infrastructure & deployment — 17 skill

Bao phủ cloud provider, container, IaC, networking, CI/CD, release, VPS và deployment platform.

`sk-aws-pro`, `sk-azure-storage`, `sk-caching-pro`, `sk-ci-cd-pro`, `sk-cloudflare-pro`, `sk-deploy-workflow`, `sk-deployment-pipeline-design`, `sk-deployment-pro`, `sk-docker-compose-pro`, `sk-docker-pro`, `sk-github-actions-templates`, `sk-hybrid-cloud-networking`, `sk-infrastructure-as-code-pro`, `sk-kubernetes-pro`, `sk-network-infra-pro`, `sk-vercel-deployment-pro`, `sk-vps-devops-pro`

### Nhóm 08 — Databases & data access — 10 skill

Bao phủ database engine, schema, migrations, SQL access, query optimization, caching store và Prisma Postgres.

`sk-database-migration`, `sk-elasticsearch-pro`, `sk-mongodb-pro`, `sk-postgres-patterns`, `sk-postgresql-pro`, `sk-postgresql-table-design`, `sk-prisma-postgres`, `sk-redis-pro`, `sk-sql-data-access-pro`, `sk-sql-optimization-patterns`

### Nhóm 09 — Tài liệu, nghiên cứu & business — 24 skill

Bao phủ finance/accounting, product/strategy, research, technical writing, office formats, PDF/PPTX/XLSX và knowledge artifacts.

`sk-accounting-pro`, `sk-biz-model`, `sk-devrel-pro`, `sk-docs`, `sk-docx`, `sk-engineering-management-pro`, `sk-excel-doc-convert`, `sk-financial-analysis-pro`, `sk-fintech-integration-pro`, `sk-market-research-pro`, `sk-ocr-pro`, `sk-office-common`, `sk-pdf`, `sk-pdf-pro`, `sk-pptx`, `sk-product-management-pro`, `sk-report-writer`, `sk-research`, `sk-reverse-doc`, `sk-strategic-consulting-pro`, `sk-technical-writing-pro`, `sk-web-research-pro`, `sk-writing-skills`, `sk-xlsx`

### Nhóm 10 — Git, tooling, platform & meta-skills — 26 skill

Bao phủ Git/worktree, CLI/tooling, repo automation, routing, agent coordination, knowledge base, skill authoring và platform entry points.

`sk-claude-code-pro`, `sk-cli-pro`, `sk-code-packaging-pro`, `sk-code-review-pro`, `sk-feedback-pro`, `sk-gatekeeper`, `sk-git-operations-pro`, `sk-git-worktree-pro`, `sk-karpathy-coding-pro`, `sk-kb-workflow`, `sk-mapping-codebase`, `sk-mcp-server-pro`, `sk-parallel-agents-pro`, `sk-remember-pro`, `sk-repo-tooling-pro`, `sk-router-pro`, `sk-self-improve-agent-pro`, `sk-skill-authoring`, `sk-skill-creator-pro`, `sk-skills-self-review-pro`, `sk-sync-custom-to-repo`, `sk-tool-discovery`, `sk-ttd-pro`, `sk-using-aix`, `sk-using-harness`, `sk-vibe-coding-pro`

## 3. Tổng hợp số lượng

| Nhóm | Số skill |
|---|---:|
| 01. Quy trình phát triển & phân tích yêu cầu | 33 |
| 02. Kiến trúc, API & backend | 18 |
| 03. Ngôn ngữ & framework ứng dụng | 28 |
| 04. Data, AI & agent systems | 17 |
| 05. Frontend, UI/UX & visual design | 29 |
| 06. Security, testing & reliability | 20 |
| 07. Cloud, infrastructure & deployment | 17 |
| 08. Databases & data access | 10 |
| 09. Tài liệu, nghiên cứu & business | 24 |
| 10. Git, tooling, platform & meta-skills | 26 |
| **Tổng** | **222** |

## 4. Các cụm có quan hệ gần hoặc chồng lấn

### 4.1. Lifecycle skills là “xương sống”

`sk-using-aix`, `sk-router-pro`, `sk-init`, `sk-sync`, `sk-planning`, `sk-execution`, `sk-review`, `sk-verification` và `sk-done` tạo thành lớp điều phối quy trình. Đây không phải các domain skill độc lập mà là entry point/gate cho nhiều task.

### 4.2. Bản thường và bản `-pro`

Repo có nhiều cặp cùng chủ đề, ví dụ:

- `sk-frontend-design` / `sk-frontend-design-pro`
- `sk-system-design` / `sk-system-design-pro`
- `sk-pdf` / `sk-pdf-pro`
- `sk-review` / `sk-review-pr`
- `sk-testing-pro` / `sk-test-driven-development-pro` / `sk-tester`
- `sk-clean-architecture` / `sk-clean-code-architecture-pro`
- `sk-nextjs-pro` / `sk-nextjs-15-pro`

Nên mô tả rõ **khi nào chọn bản nền tảng, khi nào chọn bản production-grade/chuyên sâu** để router không kích hoạt dư thừa.

### 4.3. Security xuyên nhiều nhóm

Security xuất hiện ở API, auth, AI, Next.js, Solidity, cloud và database. Nhóm 06 là nơi định tuyến chính; các skill domain nên được xem là chuyên ngành bổ sung thay vì thay thế security baseline.

### 4.4. Data/AI và backend/database giao nhau

RAG, data engineering, MLOps, PostgreSQL, Redis, Elasticsearch và API/backend thường cần phối hợp. Nên giữ boundary theo trách nhiệm:

- AI/data: model, pipeline, evaluation, retrieval.
- Backend/API: service boundary, contract, request lifecycle.
- Database: schema, transaction, query, migration, persistence.

### 4.5. BA artifact workflow

`sk-business-analysis`, `sk-specify`, `sk-story-spec`, `sk-user-flow`, `sk-ux-wireframe`, `sk-basic-design`, `sk-detail-design`, `sk-to-prd-pro` và các skill `sk-ba-*` tạo thành một nhóm workflow nghiệp vụ khá riêng, có thể được đóng gói thành preset “BA/Product Discovery”.

## 5. Các điểm cần rà soát trong catalog

1. **Mô tả metadata chưa đồng đều:** một số skill có description dạng placeholder như `Skill: ...`, `>-`, hoặc `>+`; nên chuẩn hóa để router có tín hiệu kích hoạt tốt hơn.
2. **Tên dễ gây nhầm:** `sk-pdf`/`sk-pdf-pro`, `sk-docs`/`sk-docx`, `sk-execution`/`sk-executing-pro`, `sk-verification`/`sk-verify-pro` cần boundary rõ.
3. **Skill chuyên stack rất dày:** React/Next.js/React Native/Expo, PostgreSQL/Prisma/SQL, Docker/deployment/CI-CD có nhiều lớp; nên có bảng precedence hoặc router hints.
4. **Một số skill có thể được xem là alias/preset:** `sk-senior-*`, `sk-fullstack-pro`, `sk-system-design-pro`, `sk-router-pro`, `sk-using-aix` và các workflow BA.
5. **Không nên gộp thư mục vật lý chỉ vì cùng nhóm:** README quy định mỗi skill là một đơn vị độc lập, dễ cài đặt và composable. Taxonomy này nên dùng cho catalog/routing trước; chỉ di chuyển thư mục khi có quyết định compatibility rõ ràng.

## 6. Kết luận

`simple-skills` không phải một bộ vài chục skill runtime, mà là một catalog **222 skill** với trục chính:

```text
Process/lifecycle
    + Domain engineering (architecture, backend, frontend, data, AI, security)
    + Platform operations (cloud, database, deployment)
    + Artifacts & knowledge (docs, research, business)
    + Meta tooling (router, Git, agents, skill authoring)
```

Phân nhóm trên phản ánh đúng repo hiện tại và phù hợp để làm catalog, routing rules, preset cài đặt hoặc rà soát trùng lặp.
