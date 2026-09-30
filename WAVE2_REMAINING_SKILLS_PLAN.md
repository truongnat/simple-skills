# Wave 2 — Kế hoạch xử lý các nhóm skill còn lại

**Repo:** `simple-skills`
**Catalog:** 222 skill packages
**Baseline sau Wave 0–1:** contract validator pass, catalog validator pass, 0 overlap pair ở Jaccard `>= 0.72`
**Phạm vi Wave 2:** nâng chất lượng nội dung, scenario/evidence coverage và routing của các skill chưa được xử lý trực tiếp trong Wave 0–1; không mở lại 78 Boundary leads đã đóng.

## 1. Mục tiêu và nguyên tắc

### Mục tiêu

1. Đưa các skill high-risk còn thiếu **expected evidence** lên mức production-ready.
2. Xử lý các nhóm skill còn lại theo ownership domain, không mass-insert boilerplate.
3. Giữ `SKILL.md` ngắn và navigable; nội dung lớn đưa vào `references/` hoặc `templates/`.
4. Mỗi thay đổi phải có decision map, worked scenario, failure modes, verification evidence và handoff phù hợp với domain.
5. Sau mỗi wave con phải chạy catalog validator, link/fence checks và targeted quality checks.

### Không làm

- Không đổi threshold overlap để che cảnh báo.
- Không merge skill chỉ vì cùng domain.
- Không copy nguyên một Boundary vào nhiều skill.
- Không đưa command-first workflow vào các skill guidance-only.
- Không overwrite các file untracked/user-owned đang có trong working tree.
- Không coi heuristic “thiếu test signal” là bằng chứng skill kém nếu domain phù hợp với checklist/golden output.

## 2. Tình trạng hiện tại cần giữ làm baseline

| Check | Kết quả hiện tại |
|---|---:|
| Catalog inventory | 222/222 skills |
| Catalog validator | PASS, 0 errors |
| Wave 0 boundary validator | PASS, 13/13 target skills |
| Catalog-wide boundary overlap ở threshold `>= 0.72` | 0 pairs |
| Python syntax cho validation tools | PASS |
| Stale generic handoff coi `sk-verification` là final owner | Không còn |
| Baseline trước Wave 1 | 78 lifecycle/BA pairs |

Wave 0–1 đã xử lý ownership contract của Group 01. Wave 2 không nên thay lại 13 Boundary đó trừ khi phát hiện routing regression cụ thể.

## 3. Phạm vi ưu tiên

### P0 — giữ ổn định nền tảng

Các guardrail hiện có phải chạy ở đầu và cuối mỗi wave con:

```bash
python3 tools/skill-validation/validate_boundary_contracts.py
python3 .work/skill-validation/validate_current_skills.py
python3 .work/skill-validation/generate_overlap_handoff_report.py
python3 -m py_compile tools/skill-validation/*.py .work/skill-validation/*.py
```

Acceptance: tất cả pass; overlap report không quay lại cặp generic đã đóng; mọi thay đổi có `git diff --check` pass.

### P1 — 9 skill high-risk còn thiếu scenario/evidence matrix

| Nhóm | Skill | Artifact cần thêm | Nội dung bắt buộc |
|---|---|---|---|
| 09 Finance/Business | `sk-accounting-pro` | `references/accounting-validation-matrix.md` và sửa reference thiếu | double-entry balance, period close, reversal, FX, reconciliation, audit trail |
| 03 Expo/Framework | `sk-expo-data-fetching` | state/verification matrix | HTTP error, malformed payload, timeout, offline queue, cancellation, token refresh concurrency, cache invalidation, environment leakage |
| 03 Expo/Framework | `sk-expo-native-ui` | platform/UI verification matrix | iOS/Android/web, safe area, dynamic type, accessibility labels/focus, dark mode, reduced motion, keyboard, touch target, visual regression |
| 09 Finance/Business | `sk-financial-analysis-pro` | `references/financial-model-validation.md` và sửa reference thiếu | DCF/comps, assumptions, sensitivity, units, periods, known-answer output |
| 09 Finance/Business | `sk-fintech-integration-pro` | `references/fintech-integration-validation.md` và sửa reference thiếu | idempotency, webhook replay/signature, duplicate events, timeout/retry, refund/chargeback, rate limits, token leakage, reconciliation |
| 10 Git/Tooling | `sk-github-actions-templates` | workflow validation matrix | YAML parse, least privilege, fork secrets, concurrency, matrix failure, artifact retention, pinning, approval, rollback, reusable inputs |
| 07 Cloud/Infra | `sk-hybrid-cloud-networking` | troubleshooting/rollback reference | BGP convergence, dual-tunnel failover, asymmetric routing, MTU, packet loss, DNS, rollback; sửa malformed related-skill bullet |
| 04 Data/AI | `sk-mlops-pro` | evaluation/release matrix | reproducibility, schema/data drift, model regression, canary rollback, feature freshness, serving SLO, alert thresholds |
| 06 Security | `sk-solidity-security` | attack/invariant matrix | reentrancy, access control, oracle manipulation, upgrade/storage collision, integer/rounding, signature replay, pause/emergency invariants |

**Thứ tự P1:**

1. Finance/fintech/accounting — missing references là lỗi deterministic và rủi ro audit cao.
2. Hybrid networking + GitHub Actions — rollback/permission failure có blast radius vận hành.
3. Solidity security — security invariants cần rõ trước khi gọi testing owner.
4. MLOps — drift/release evidence.
5. Expo — mobile/runtime state matrices.

### P2 — 21 skill/cluster cần worked scenario hoặc golden-output evidence

| Cluster | Skill(s) | Wave 2 output |
|---|---|---|
| Backend/framework | `sk-spring-boot-pro`, `sk-django-pro` | REST/service worked example; unit, integration, security, transaction, migration and query-count evidence |
| Business/process | `sk-biz-model`, `sk-engineering-management-pro` | 2–4 worked scenarios with assumptions, decision criteria, expected artifact, failure/uncertainty handling |
| AI/agent | `sk-fullstack-rag-pro`, `sk-ai-agents-pro`, `sk-ai-red-teaming-pro` | evaluation fixtures for groundedness, safety, tool failure, prompt injection, latency/cost and regression |
| Data/ML | `sk-data-science-pro`, `sk-data-engineering-pro`, `sk-machine-learning-pro` | representative fixture, schema/data assumptions, expected verification output |
| Artifact formats | `sk-office-common`, `sk-pdf`, `sk-pptx`, `sk-xlsx`, `sk-docx` | golden-output checks for layout, metadata, formulas, pagination, accessibility and round-trip conversion |
| Architecture/testing/security | `sk-clean-architecture`, `sk-debugging-strategies`, `sk-javascript-testing-patterns`, `sk-microservices-patterns`, `sk-stride-analysis-patterns` | one positive + one negative scenario with expected routing/decision/evidence |

P2 chỉ bắt đầu sau khi P1 pass. Với artifact formats, ưu tiên deterministic fixture/golden output hơn prose test.

## 4. Execution waves chi tiết

### Wave 2A — Contract and reference integrity

**Phạm vi:** 9 P1 skill có missing reference, malformed section hoặc thiếu validation anchor.

**Tasks:**

1. Kiểm tra mọi reference path trước khi viết nội dung.
2. Tạo reference file theo đúng progressive disclosure; không nhồi toàn bộ matrix vào `SKILL.md`.
3. Thêm navigation link trong `SKILL.md` với điều kiện đọc rõ ràng.
4. Sửa malformed bullets/empty sections trong networking.
5. Với mỗi skill, thêm một verification response shape tối thiểu: `claim`, `criteria`, `evidence`, `limitations`, `next owner`.

**Gate:**

- Không còn reference path thiếu.
- Mỗi P1 có ít nhất 6–10 scenario rows domain-specific.
- Mỗi row có expected result/evidence, không chỉ tên test.
- Catalog validator và local-link check pass.

### Wave 2B — High-risk evidence review

**Phạm vi:** rà soát chéo P1 theo owner downstream.

**Handoff rules:**

- `sk-tester` thực thi test cases/fixtures.
- `sk-review` hoặc `sk-review-pr` tạo findings.
- `sk-verify-pro` là owner của pass/block/defer.
- Domain skill không tự claim final release status.

**Tasks:**

1. Kiểm tra mỗi matrix có failure, recovery/rollback và limitation case.
2. Kiểm tra secret/token/PII leakage không bị đưa vào fixture thật.
3. Kiểm tra các cặp domain gần nhau: fintech ↔ API security, MLOps ↔ data engineering, Expo ↔ JavaScript testing, GitHub Actions ↔ deployment.
4. Ghi canonical next owner trong từng reference.

**Gate:** không có skill nào tự nhận test execution hoặc final verification nếu đó không phải owner; handoff packet map được criterion → evidence.

### Wave 2C — P2 worked scenarios và artifact evidence

**Phạm vi:** 6 cluster ở mục P2.

**Tasks:**

1. Chọn một representative skill mỗi cluster trước.
2. Review pattern bằng validator và manual inspection.
3. Chỉ fan-out sang các skill còn lại khi scenario thực sự khác domain.
4. Với docs/artifact skill, mô tả golden-output assertions thay vì tạo runtime dependency không cần thiết.

**Gate:** mỗi skill có ít nhất một positive và một negative/edge scenario; artifact skill có output-level evidence.

### Wave 2D — Catalog routing regression

**Phạm vi:** tất cả nhóm 01–10, tập trung các adjacency đã biết.

**Routing fixtures tối thiểu:**

| Prompt class | Expected primary owner | Forbidden ambiguity |
|---|---|---|
| accounting close/reconciliation | `sk-accounting-pro` | không route sang generic finance prose |
| payment webhook/idempotency | `sk-fintech-integration-pro` | không để API design thay business integration |
| Expo cache/cancellation | `sk-expo-data-fetching` | không route sang native UI/testing |
| native safe-area/accessibility | `sk-expo-native-ui` | không route sang data-fetching |
| GitHub workflow permissions/rollback | `sk-github-actions-templates` | không route sang generic CI prose |
| model drift/canary | `sk-mlops-pro` | không route sang generic ML only |
| reentrancy/storage collision | `sk-solidity-security` | không route sang generic security only |
| schema migration/restore | `sk-database-migration` | không route sang application framework |
| final claim evidence | `sk-verify-pro` | không invoke `sk-verification` in parallel |

**Gate:** một primary owner hoặc hỏi clarification; không có invocation song song của hai owner cho cùng claim.

## 5. Phân bổ theo taxonomy 10 nhóm

| Nhóm | Số skill | Tình trạng | Wave 2 focus |
|---|---:|---|---|
| 01 Lifecycle/BA | 33 | Wave 0–1 canonical ownership đã xử lý | routing regression và artifact SSOT; không rewrite hàng loạt |
| 02 Architecture/API/backend | 18 | core packs đã có | P2 worked scenarios cho clean architecture/microservices; compatibility regression |
| 03 Language/framework | 28 | core packs đã có | Expo P1; Spring Boot/Django P2; framework adjacency |
| 04 Data/AI/agents | 17 | core packs đã có | MLOps P1; RAG/agents/data/ML P2 |
| 05 Frontend/UI/UX | 29 | core packs đã có | Expo native P1; golden/visual/accessibility regression |
| 06 Security/testing/reliability | 20 | core packs đã có | Solidity P1; debugging/JS testing/STRIDE P2 |
| 07 Cloud/infra/deployment | 17 | core packs đã có | hybrid networking P1; rollback/permissions checks |
| 08 Databases/data access | 10 | core packs đã có | migration/schema evidence regression; no broad rewrite |
| 09 Documents/research/business | 24 | core packs đã có | accounting/financial/fintech P1; business/artifact P2 |
| 10 Git/tooling/meta | 26 | core packs đã có | GitHub Actions P1; tool/router capability regression |

## 6. Guardrails cho file và Git

Working tree hiện có các thay đổi cũ chưa commit. Trước khi bắt đầu từng wave con:

1. Không reset, clean hoặc checkout destructive.
2. Không overwrite `.idea/`, `PHASE1_6_SKILL_UPGRADE_SUMMARY.md` hoặc các artifact untracked khi chưa có quyết định của owner.
3. Tách thay đổi theo nhóm commit/patch logic: validator, P1 domain packs, P2 scenarios, routing fixtures.
4. Chạy `git diff --check` và liệt kê status trước/sau.
5. Không coi file report regenerate là source of truth nếu generator chưa được cập nhật dynamic headings/counts.

## 7. Definition of Done cho Wave 2

- [ ] 9 P1 skills có reference path hợp lệ và scenario/evidence matrix.
- [ ] Mỗi P1 có failure/recovery/limitation cases.
- [ ] 21 P2 skill/cluster có worked scenario hoặc golden-output evidence phù hợp.
- [ ] Không có duplicate final owner giữa domain skill và `sk-verify-pro`.
- [ ] Routing fixture pass cho các adjacency ở mục 2D.
- [ ] Catalog validator pass với 222/222 skills.
- [ ] Boundary overlap report pass và không quay lại 78 pair.
- [ ] Link/fence/YAML/JSON/script syntax checks pass.
- [ ] Mỗi changed file có lý do domain-specific và handoff rõ.
- [ ] Báo cáo Wave 2 cập nhật summary, evidence và remaining risks.

## 8. Quyết định đề xuất

**Nên triển khai Wave 2A → 2B trước, sau đó mới 2C → 2D.** Lý do:

- P1 có lỗi deterministic (missing reference, malformed section) và rủi ro domain cao.
- P2 cần pattern ổn định để không tạo thêm boilerplate.
- Routing regression chỉ đáng tin sau khi evidence/hand-off contracts của P1 đã rõ.

**Không nên mở rộng Wave 2 thành rewrite 180 skill còn lại.** Catalog consistency đã pass; chỉ xử lý skill có finding cụ thể hoặc adjacency có risk. Phần còn lại duy trì bằng validator và review-on-change.
