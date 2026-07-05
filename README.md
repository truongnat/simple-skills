# simple-skills

Bộ skill và quy tắc tối giản cho AI agent, tập trung vào workflow rõ ràng, dễ đọc và dễ mở rộng. Repo này không cố biến skill thành một framework phức tạp; thay vào đó, nó cung cấp các mẫu làm việc ngắn gọn cho agent khi xử lý task.

## Mục tiêu

- Giúp agent làm việc theo một vòng đời rõ ràng: suy nghĩ → lập kế hoạch → thực thi → review → kết thúc.
- Khuyến khích tạo artifact và session thay vì chạy task một cách mơ hồ.
- Dễ dàng cài đặt vào bất kỳ repo nào bằng cách tạo thư mục `.agents`.

## Cài đặt

Chạy lệnh trong thư mục dự án cần cài skill. Script sẽ tạo thư mục `.agents/` tại đó:

```text
.agents/
├── AGENTS.md
├── DESIGN_SYSTEM.md
├── TOOLS.md
└── skills/
    ├── brainstorming/
    ├── planning/
    └── ...
```

### Linux / macOS

```bash
curl -fsSL https://raw.githubusercontent.com/truongnat/simple-skills/main/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/truongnat/simple-skills/main/install.ps1 | iex
```

### Cài từ repo đã clone

Nếu đã clone repo này, có thể chạy script trực tiếp:

```bash
# Linux / macOS
./install.sh

# Windows (PowerShell)
./install.ps1

# Windows (CMD)
install.cmd
```

## Skills hiện có

| Skill | Mục đích |
| --- | --- |
| `brainstorming` | Làm rõ mục tiêu, phạm vi, trade-off trước khi bắt đầu |
| `planning` | Chia task, dependency, acceptance criteria và Definition of Done |
| `sync` | Đồng bộ hiểu biết codebase, git state và context (mặc định read-only) |
| `execution` | Ghi lại từng bước thực thi và thay đổi đã làm |
| `review` | Review tính đúng đắn, regression risk, security và maintainability |
| `done` | Tổng kết công việc, tạo PR message và handoff |
| `investigate` | Tìm hiểu, debug hoặc phân tích trước khi quyết định implement |
| `research` | Nghiên cứu nội bộ hoặc bên ngoài trước khi đưa ra quyết định |
| `review-pr` | Review pull request hoặc diff một cách có cấu trúc |
| `tester` | Tạo test case, kiểm chứng và ghi nhận evidence |
| `business-analysis` | Làm rõ yêu cầu nghiệp vụ, scope và tài liệu quy trình |

## Cấu trúc repo

```text
simple-skills/
├── docs/
│   ├── AGENTS.md          # Entrypoint quy tắc chung cho agent
│   ├── DESIGN_SYSTEM.md   # Chuẩn thiết kế artifact
│   └── TOOLS.md           # Reference về các công cụ hỗ trợ
├── skills/
│   └── <skill-name>/
│       └── SKILL.md       # Mô tả skill, workflow và contract
├── install.sh             # Cài đặt cho Linux / macOS
├── install.ps1            # Cài đặt cho Windows (PowerShell)
└── install.cmd            # Wrapper gọi install.ps1 trên Windows
```

## Cách dùng nhanh

Sau khi cài đặt, agent sẽ đọc `.agents/AGENTS.md` làm entrypoint. Với mỗi task, nên tạo một session riêng:

```text
.agents/sessions/<Task-<number>-<short-description>>/
├── DISCUSSION.md    # brainstorming
├── PLAN.md          # planning
├── EXECUTION.md     # execution
├── REVIEW.md        # review
└── DONE.md          # done
```

Chi tiết workflow xem [docs/AGENTS.md](docs/AGENTS.md).

## Phát triển

Repo vẫn có `package.json` cho tooling TypeScript/Rolldown nếu sau này cần mở rộng. Việc cài đặt skill không yêu cầu Node.js — chỉ cần `curl` trên Linux/macOS hoặc PowerShell trên Windows.
