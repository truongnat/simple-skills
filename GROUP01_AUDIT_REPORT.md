# Audit Group 01 — Quy trình phát triển & phân tích yêu cầu

**Repo:** `simple-skills`
**Phạm vi:** 33 skill trong Group 01, không đánh giá toàn bộ 222 skill.
**Mốc audit:** commit `9d065c43a266177e7c00667ba79dfef3a0773907` (`9d065c4`).
**Mục tiêu:** tìm gap về routing, lifecycle contract, boundary, artifact handoff và tính nhất quán; sửa các lỗi hiển nhiên có rủi ro gây chạy sai.

## 1. Executive summary

- **Điểm mạnh:** Group 01 đã có tư duy contract khá tốt: đa số workflow yêu cầu step ledger, evidence, trạng thái blocked/partial và handoff; `sk-planning`, `sk-execution`, `sk-review`, `sk-done` tạo thành một xương sống có thể kiểm toán.
- **Gap lớn nhất:** Group 01 đang có **hai thế hệ contract**: 26/33 skill chỉ có `name` + `description`, trong khi 7 skill `*-pro` có metadata routing (`sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`). Router vì vậy không có tín hiệu đồng nhất.
- **Gap lifecycle:** `sk-execution` và `sk-executing-pro` cùng sở hữu execution nhưng dùng artifact/state model khác nhau; `sk-verification` và `sk-verify-pro` cũng trùng mục tiêu. Chưa có một bảng precedence/canonical route đủ rõ để tránh kích hoạt hai skill cùng lúc.
- **Gap tham chiếu:** một số skill `*-pro` từng trỏ tới `planning-pro`, tên không tồn tại trong Group 01; `sk-scaffold` từng chứa lệnh `git sk-init` không hợp lệ. Các lỗi rõ ràng này đã được sửa trong working tree.
- **Đánh giá tổng thể:** **Needs improvement — P1**, chưa nên dùng Group 01 làm preset/routing baseline trước khi chuẩn hóa metadata và canonical lifecycle.

## 2. Inventory và cấu trúc hiện tại

### 2.1. 33 skill thuộc Group 01

`sk-api-ba`, `sk-ba-dashboard`, `sk-ba-handoff`, `sk-ba-integrate`, `sk-ba-kg`, `sk-ba-test`, `sk-basic-design`, `sk-brainstorming`, `sk-business-analysis`, `sk-detail-design`, `sk-discussing-pro`, `sk-done`, `sk-executing-pro`, `sk-execution`, `sk-gap-analysis`, `sk-grill-me-pro`, `sk-init`, `sk-investigate`, `sk-planning`, `sk-quick-fix`, `sk-review`, `sk-review-pr`, `sk-scaffold`, `sk-specify`, `sk-story-spec`, `sk-sync`, `sk-tester`, `sk-to-issues-pro`, `sk-to-prd-pro`, `sk-user-flow`, `sk-ux-wireframe`, `sk-verification`, `sk-verify-pro`.

### 2.2. Phân lớp sở hữu đề xuất

| Lớp | Skill | Vai trò |
|---|---|---|
| Entry/context | `sk-scaffold`, `sk-init`, `sk-sync`, `sk-investigate` | xác định repo, context, drift và root cause |
| Discovery/BA | `sk-brainstorming`, `sk-discussing-pro`, `sk-grill-me-pro`, `sk-business-analysis`, `sk-specify`, `sk-story-spec`, `sk-gap-analysis` | làm rõ problem, requirement, rule, AC |
| Product/design artifacts | `sk-user-flow`, `sk-ux-wireframe`, `sk-basic-design`, `sk-detail-design`, các `sk-ba-*` | chuyển requirement thành artifact có thể handoff |
| Planning/backlog | `sk-planning`, `sk-to-prd-pro`, `sk-to-issues-pro` | plan, PRD và vertical slices |
| Delivery | `sk-quick-fix`, `sk-execution`, `sk-executing-pro`, `sk-tester` | đường tắt, implementation, test lifecycle |
| Gates/closure | `sk-review`, `sk-review-pr`, `sk-verification`, `sk-verify-pro`, `sk-done` | review, proof, close task |

Điểm cần lưu ý: `sk-to-prd-pro`/`sk-to-issues-pro` là product/backlog tooling có side effect GitHub, không nên được router xem là bước bắt buộc của mọi feature lifecycle.

## 3. Findings theo severity

### F-01 — P1: Metadata/routing không đồng nhất

**Evidence:** kiểm kê 33 `SKILL.md` cho thấy chỉ 7 skill có toàn bộ các field `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`; 26 skill còn lại chỉ có `name` và `description`.

**Ảnh hưởng:** router không thể phân biệt ổn định `process`/`domain`, role phù hợp, compatibility và mức ưu tiên; alias và preset dễ bị suy diễn từ tên thư mục.

**Cải thiện:**
1. Chuẩn hóa frontmatter tối thiểu cho cả 33 skill.
2. Bổ sung `aliases` chỉ khi alias đã được dùng trong docs/router; không tự sinh alias hàng loạt.
3. Gán tag theo capability thật, ví dụ `requirements`, `design`, `planning`, `execution`, `quality-gate`.
4. Thêm CI validator: field bắt buộc, enum `sk-kind`, semver, compatibility và duplicate alias.

**Acceptance:** 33/33 skill có metadata hợp lệ; router test với prompt ambiguity trả về một canonical skill hoặc hỏi lựa chọn, không chạy song song hai owner.

### F-02 — P1: Hai owner cho execution

**Evidence:** `skills/sk-execution/SKILL.md:16-18, 20-47` định nghĩa execution theo `TASKS.md`, `EXECUTION.md`, progress board và 4 step files. `skills/sk-executing-pro/SKILL.md:22-35, 47-102` lại nói đây là “single execution skill”, dùng checkpoint/adaptive replanning, `state.json`, `checkpoint.log`, coder/reviewer nodes.

**Ảnh hưởng:** một task có thể bị route vào hai workflow với output và recovery model khác nhau; `planning-pro` được nhắc trong bản cũ nhưng không tồn tại, còn canonical repo là `sk-planning`.

**Cải thiện đề xuất:** chọn một trong hai phương án, không duy trì trạng thái hiện tại:

- **Khuyến nghị:** giữ `sk-execution` làm compatibility facade cho workflow artifact hiện hữu; chuyển logic production-grade vào `sk-executing-pro`, ghi rõ `sk-executing-pro` là canonical owner và `sk-execution` chỉ route/bridge.
- Hoặc ngược lại, nếu hệ thống hiện tại không hỗ trợ `state.json`/checkpoint engine, hạ `sk-executing-pro` thành reference pattern, không cho router invoke trực tiếp.

**Acceptance:** có đúng một canonical execution owner; mọi execution skill khác có `When Not To Use`, alias và handoff tới owner đó; test resume/blocked dùng cùng một state vocabulary.

### F-03 — P1: Hai owner cho verification

**Evidence:** `sk-verification/SKILL.md:19-45, 87-101` và `sk-verify-pro/SKILL.md:22-49, 91-110` cùng làm claim-to-evidence verification, downgrade khi thiếu proof và block completion. Khác biệt chính là một bên output summary/evidence, một bên bắt buộc `VERIFY.md`.

**Ảnh hưởng:** dễ chạy trùng; không rõ `VERIFY.md` có bắt buộc ở mọi task hay chỉ ở professional path; `sk-done` chưa chỉ ra một verification owner duy nhất.

**Cải thiện:** hợp nhất thành một canonical `sk-verify-pro` hoặc biến `sk-verification` thành lite facade. Quy định rõ:

- Lite: summary + evidence list, không bắt buộc artifact nếu task không có session.
- Full/pro: `artifacts/<task-id>/VERIFY.md`, claim matrix, blockers và human checks.

**Acceptance:** `sk-done`, `sk-review`, `sk-execution` cùng trỏ tới cùng owner; status enum và output path nhất quán.

### F-04 — P1: Artifact path và progress ledger chưa có SSOT duy nhất

**Evidence:** nhiều workflow yêu cầu `artifacts/<task-id>/PROGRESS.md`; `sk-planning` yêu cầu session có `PLAN.md` + `TASKS.md` (`SKILL.md:19-24, 63-82`); `sk-init` chỉ trả về danh sách file/facts qua output (`sk-init/SKILL.md:18-20`); `sk-executing-pro` thêm `state.json` và `checkpoint.log` (`SKILL.md:91-98`).

**Ảnh hưởng:** khó tự động resume, khó kiểm tra artifact tồn tại, dễ tạo `PLAN.md` ở session root nhưng `VERIFY.md` ở `artifacts/<task-id>`.

**Cải thiện:** tạo một shared session-artifacts contract reference dùng chung cho Group 01, quy định:

```text
artifacts/<task-id>/
  CONTEXT.md
  DISCUSSION.md (optional)
  BUSINESS_ANALYSIS.md / PRD.md / design artifacts (as applicable)
  PLAN.md
  TASKS.md
  PROGRESS.md
  EXECUTION.md
  REVIEW.md or REVIEW_PR.md
  VERIFY.md
  DONE.md
```

Skill nào không tạo file phải ghi rõ `artifact_mode: none` và trả facts inline.

### F-05 — P1: Reference tới skill không tồn tại / contract không executable

**Evidence trước khi sửa:** `sk-executing-pro`, `sk-to-prd-pro`, `sk-to-issues-pro` dùng tên `planning-pro`; catalog Group 01 có `sk-planning`, không có `planning-pro`. `sk-scaffold/SKILL.md:94` chứa lệnh `git sk-init`, không phải lệnh Git hợp lệ.

**Đã cải thiện trong working tree:**

- thay các reference `planning-pro` bằng `sk-planning` trong 3 skill;
- thay `git sk-init` bằng `git init`, kèm handoff `sk-init`;
- chạy `git diff --check` thành công.

**Còn lại:** thêm script kiểm tra reference skill nội bộ, nhưng parser phải bỏ qua inline code dùng làm ví dụ/field value để tránh false positive.

### F-06 — P2: Nội dung contract có dấu hiệu bị hỏng/truncated

**Evidence trước khi sửa:** `sk-review/SKILL.md:21-23` kết thúc bằng `§ Gates C.`; `sk-done/SKILL.md:91-92` bị cắt giữa câu ở phần PR description.

**Đã cải thiện:** khôi phục thành câu hoàn chỉnh, không đổi semantics.

**Còn lại:** chạy markdown lint + check cho các dòng cụt, heading thiếu, code fence chưa đóng và YAML frontmatter parse lỗi trên toàn Group 01.

### F-07 — P2: BA/Product artifact overlap chưa có decision tree

**Evidence:** `sk-business-analysis` sở hữu problem/stakeholder/user stories/business rules/AC và Spec quality (`SKILL.md:20-34, 60-90`); `sk-specify` có 7 mode PRD/roadmap/discover/URD/BRD/PRD-epic/SRS (`SKILL.md:19-37`); `sk-to-prd-pro` lại sở hữu PRD synthesis + GitHub issue (`SKILL.md:26-30, 104-106`); `sk-story-spec` và các `sk-ba-*` cũng tạo artifact requirement/test/design chuyên biệt.

**Ảnh hưởng:** người dùng nói “viết spec/PRD” có thể vào ít nhất 3 path; trace ID, template và mức Confirm-first không chắc được giữ liên tục.

**Cải thiện:** đặt decision tree:

```text
Ý tưởng chưa rõ → sk-brainstorming / sk-discussing-pro
Cần challenge requirement + US/BR/AC → sk-business-analysis
Cần một document theo mode PRD/BRD/URD/SRS → sk-specify
Đã có context và muốn tạo PRD GitHub issue, không interview → sk-to-prd-pro
Đã có PRD và cần backlog slices → sk-to-issues-pro
```

`sk-to-prd-pro` phải luôn ghi source, assumptions và link trace IDs; không được cạnh tranh ownership với `sk-specify` về mode artifact.

### F-08 — P2: Quick path chưa nêu đủ điều kiện quay lại full lifecycle

**Evidence:** `sk-quick-fix/SKILL.md:13-16, 45-67` có ceiling 1–3 cards và handoff `sk-sync → sk-execution → sk-review → sk-done`, nhưng việc upgrade được mô tả chủ yếu theo “unclear or needs product/design decisions”.

**Gap cần bổ sung:** trigger upgrade khi thay đổi schema/public API/auth/permission/data migration, khi có nhiều hơn 3 independently verifiable outputs, hoặc khi không có AC/Verify falsifiable.

**Acceptance:** quick-fix có bảng `upgrade_trigger → target path → required artifact`, và test với 5 scenario boundary.

### F-09 — P2: Tester mạnh nhưng kết nối với lifecycle chưa thật sự canonical

**Evidence:** `sk-tester/SKILL.md:21-32, 44-62` bao phủ 8 bước STLC và nhiều artifact; `sk-ba-test/SKILL.md:19-25, 46-65` lại tạo checklist/cases trước deep tester. `sk-execution` ghi “does NOT do independent sk-review” nhưng không nêu rõ khi nào test execution thuộc `sk-tester` hay `sk-execution`.

**Cải thiện:** tách rõ:

- `sk-ba-test`: test design nhẹ, pre-implementation, không claim runtime pass.
- `sk-tester`: canonical QA/STLC và go/no-go.
- `sk-execution`: implementation verification per task, không thay thế QA cycle.

Bổ sung mapping `REQ/US/AC → TESTCASE → EXECUTION evidence → TEST_SUMMARY`.

## 4. Strengths nên giữ nguyên

1. **Evidence-first:** `sk-execution`, `sk-review`, `sk-verification`, `sk-done` đều chống claim “done” không có proof.
2. **Blocked state khá rõ:** nhiều skill yêu cầu stop, ghi blocker và resume từ earliest incomplete step.
3. **Traceability tốt:** BA có BR/AC; planning có task index/micro-cards; tester có traceability matrix.
4. **Greenfield guard đúng hướng:** `sk-scaffold` phân biệt scaffold với `sk-init` và cấm overwrite project hiện hữu.
5. **PR review an toàn:** `sk-review-pr` bảo vệ current branch/dirty worktree và phân biệt remote-diff với runtime verification.

## 5. Kế hoạch cải thiện theo wave

### Wave 1 — Contract integrity (P0/P1, nên làm trước routing)

- [x] Sửa malformed lines trong `sk-review` và `sk-done`.
- [x] Sửa `git sk-init` trong `sk-scaffold`.
- [x] Sửa reference `planning-pro` thành `sk-planning`.
- [ ] Thêm markdown/YAML/reference validator chạy trên 33 skill.
- [ ] Viết shared session-artifacts contract reference dùng chung.

### Wave 2 — Canonical ownership (P1)

- [ ] Quyết định owner duy nhất cho execution: `sk-executing-pro` hoặc `sk-execution`.
- [ ] Quyết định owner duy nhất cho verification: `sk-verify-pro` hoặc `sk-verification`.
- [ ] Cập nhật tất cả `When To Use`, `When Not To Use`, `Limitations`, `Handoff` theo decision.
- [ ] Chuẩn hóa status enum: `todo`, `in_progress`, `blocked`, `skipped`, `complete` hoặc một enum tương đương; không dùng đồng thời `sk-done` như status và tên skill nếu không có lý do tương thích.

### Wave 3 — Router metadata và BA decision tree (P1/P2)

- [ ] Chuẩn hóa frontmatter 33/33.
- [ ] Tạo routing matrix gồm trigger, primary skill, supporting skill, forbidden pairing, output artifact.
- [ ] Thêm decision tree cho BA/PRD/spec/story/design.
- [ ] Thêm ambiguity tests cho các prompt: “write spec”, “review code”, “verify done”, “execute plan”, “make test cases”.

### Wave 4 — Testability và maintenance (P2)

- [ ] Test quick-fix upgrade triggers.
- [ ] Test end-to-end traceability từ AC đến test summary.
- [ ] Markdown lint, YAML parse, local-link/reference check và duplicate alias check trong CI.
- [ ] Review lại các câu prose bị cắt hoặc artifact names không nhất quán.

## 6. Target lifecycle sau khi cải thiện

```text
[greenfield?]
  ├─ yes → sk-scaffold → sk-init
  └─ no  → sk-init

context stale/drift? → sk-sync
unknown root cause? → sk-investigate

idea/requirement
  → sk-brainstorming / sk-discussing-pro
  → sk-business-analysis OR sk-specify (exactly one primary)
  → sk-user-flow / sk-basic-design / sk-detail-design (as needed)
  → sk-planning
  → canonical execution owner
  → canonical review owner (sk-review or sk-review-pr, not both unless PR exists)
  → canonical verification owner
  → sk-done

quick clear fix:
  sk-quick-fix → sk-sync → canonical execution → sk-review → verify → sk-done
```

`sk-to-prd-pro` và `sk-to-issues-pro` là nhánh product/backlog có điều kiện, không nằm trên happy path bắt buộc.

## 7. Definition of improved

Group 01 đạt mức sẵn sàng làm routing baseline khi:

- 33/33 `SKILL.md` parse được frontmatter và có metadata tối thiểu.
- Không còn reference tới skill/command không tồn tại.
- Có đúng một owner cho execution và một owner cho verification.
- Mọi artifact đều theo cùng `artifacts/<task-id>/` contract hoặc khai báo rõ `artifact_mode: none`.
- BA/PRD/spec paths có decision tree và boundary test.
- CI phát hiện markdown malformed, duplicate alias, broken local references và status enum drift.
- Có test case cho các trạng thái `complete`, `partial`, `blocked`, `skipped`, `needs-human-confirmation`.

## 8. Thay đổi đã thực hiện trong đợt audit này

Sáu file đã được chỉnh sửa, chỉ ở mức sửa lỗi hiển nhiên và reference:

- `skills/sk-review/SKILL.md`
- `skills/sk-done/SKILL.md`
- `skills/sk-scaffold/SKILL.md`
- `skills/sk-executing-pro/SKILL.md`
- `skills/sk-to-prd-pro/SKILL.md`
- `skills/sk-to-issues-pro/SKILL.md`

Validation đã chạy: `git diff --check` — **pass**. Chưa tạo commit.


## 9. Post-remediation status — 2026-09-29

Các đề xuất trong audit đã được triển khai trong working tree:

- **Metadata:** 33/33 skill có `name`, `description`, `sk-kind`, `sk-version`, `sk-tags`, `sk-roles`, `sk-compatible`.
- **Canonical ownership:** `sk-executing-pro` là execution owner; `sk-execution` là legacy compatibility facade. `sk-verify-pro` là verification owner; `sk-verification` là lite compatibility facade.
- **Artifact SSOT:** thêm `docs/GROUP01_SESSION_ARTIFACTS.md` với canonical path, artifact ownership, state vocabulary và handoff minimum.
- **Routing:** thêm `docs/GROUP01_ROUTING.md` với decision matrix, overlap rules và Quick Fix upgrade triggers.
- **QA boundary:** `sk-tester` đã được làm rõ là owner của QA/STLC/go-no-go; `sk-ba-test` chỉ làm test design trước implementation; execution chỉ verify AC per task.
- **Contract fixes:** xóa các reference `planning-pro`, sửa `git sk-init`, khôi phục text bị truncate và sửa broken links tới shared contract.
- **Guardrails:** thêm `tools/validate_group01.py` và `tests/test_group01_contract.py`; validator kiểm tra metadata, semver, kind, duplicate alias, fenced Markdown, canonical ownership, stale references, required docs và local Markdown links.

### Verification cuối

```text
python3 tools/validate_group01.py        PASS
python3 tests/test_group01_contract.py   PASS
python3 -m py_compile tools/validate_group01.py tests/test_group01_contract.py  PASS
git diff --check                         PASS
```

### Còn lại ngoài phạm vi tự động hóa

Không còn gap contract/routing nào trong danh sách audit cần sửa ngay. Quyết định product-level về việc có đổi tên/xóa các facade legacy là breaking change; hiện đã chọn phương án tương thích an toàn: giữ facade, ghi rõ canonical owner và cấm invoke trùng trong cùng task.
