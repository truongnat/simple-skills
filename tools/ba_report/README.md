# BA Report — Visual HTML Reports for Business Analysis

Convert BA markdown artifacts into visual HTML reports for testers, PMs, and non-technical stakeholders.

## What it does

- **Parses** BA markdown files (BUSINESS_ANALYSIS.md, USER_FLOW.md, PRD.md, etc.)
- **Renders** them as styled HTML using the `.ss-*` design system
- **Serves** via HTTP or generates static HTML
- **Visualizes** Mermaid diagrams, tables, and structured data
- **Navigates** multiple artifacts with sticky sidebar

## Supported artifacts

- `BUSINESS_ANALYSIS.md` — Business rules, user stories, acceptance criteria
- `USER_FLOW.md` — User journeys, happy paths, error flows
- `PRD.md` — Product requirements, features, scope
- `BRD.md` — Business goals, risks, ROI
- `URD.md` — Personas, needs, journeys
- `SPEC_SRS.md` — Functional/non-functional requirements
- `MODEL.md` — Business models, diagrams (Mermaid)
- `DISCOVER.md` — Idea validation, go/no-go
- `ROADMAP.md` — Now/Next/Later priorities
- `PRD_EPIC.md` — Epic-level requirements

## Usage

### Serve latest BA session (auto-opens browser)

```bash
python tools/ba-report/serve.py
```

### Serve specific session

```bash
python tools/ba-report/serve.py Task-1-demo
```

### Custom port

```bash
python tools/ba-report/serve.py --port 9000
```

### Don't auto-open browser

```bash
python tools/ba-report/serve.py --no-open
```

### Run server directly

```bash
python tools/ba-report/server.py --sessions-dir .agent-work/sessions --open
```

## How it works

1. **Parser** (`parser.py`) — Reads BA markdown and extracts sections, tables, Mermaid diagrams
2. **Renderer** (`renderer.py`) — Converts parsed data to styled HTML using `.ss-*` classes
3. **Server** (`server.py`) — Serves HTML reports via HTTP (stdlib only, no dependencies)
4. **Launcher** (`serve.py`) — Finds sessions with BA artifacts and starts server

## Architecture

```
tools/ba-report/
├── server.py       # HTTP server (stdlib http.server)
├── parser.py       # Markdown → structured data (regex, no deps)
├── renderer.py     # Structured data → HTML (.ss-* classes)
├── ba-report.css   # BA-specific styles (extends decision-server theme)
├── ba-report.js    # Mermaid init, navigation, smooth scroll
├── serve.py        # Launcher (finds sessions, starts server)
└── README.md       # This file
```

**Zero external dependencies** — Python stdlib only. CDN for Tailwind + Mermaid (client-side).

## Design system

Uses the same `.ss-*` design system as `decision-server`:

- `.ss-page`, `.ss-header`, `.ss-nav`, `.ss-main` — Layout
- `.ss-card`, `.ss-table`, `.ss-table-wrap` — Components
- `.ss-ba-nav`, `.ss-ba-artifact` — BA-specific
- `.ss-termaid` — Diagram container
- Status badges for `pass`/`fail`/`blocked`/`confirmed`/`unknown`

## API endpoints

- `GET /` — List all sessions with BA artifacts
- `GET /<session>/` — Show full BA report for session
- `GET /ba-report.css` — Serve BA styles
- `GET /ba-report.js` — Serve BA interactivity
- `GET /api/sessions` — JSON list of sessions
- `GET /api/health` — Health check

## Integration with skills

BA skills can call the report generator after writing artifacts:

```bash
# In business-analysis/steps/step-04-self-check.md
python .agents/tools/ba-report/serve.py --session . --no-open
```

## Testing

```bash
# Create test session
bash .agents/tools/session/session.sh new ba-test

# Copy BA template to session
cp skills/business-analysis/templates/BUSINESS_ANALYSIS.template.md \
   .agent-work/sessions/Task-N-ba-test/BUSINESS_ANALYSIS.md

# Launch report server
python tools/ba-report/serve.py

# Open in browser at http://127.0.0.1:8766
```

## Requirements

- Python ≥3.11
- Sessions with BA artifacts in `.agent-work/sessions/`

## Limitations

- Tailwind CDN loaded from `cdn.tailwindcss.com` (no SRI — dynamic CDN)
- Mermaid diagrams require internet connection (CDN)
- No dark mode (follows decision-server pattern)
- No offline mode (CDN dependencies)

## Future enhancements

- Static HTML generation (`--generate` flag)
- Search/filter functionality
- Export to PDF
- Offline Mermaid (bundle locally)
- Dark mode support

## License

MIT — part of [simple-skills](https://github.com/truongnat/simple-skills)
