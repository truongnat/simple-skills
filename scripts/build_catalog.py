#!/usr/bin/env python3
"""Build catalog.json — the machine-readable skill catalog for init.

Reads every skill dir under `skills/`, extracts frontmatter (name, description,
x-kind, x-version, x-tags, x-roles, x-compatible, aliases), and writes
`catalog.json` at the repo root with:

  - meta:        version + generated-at + skill count
  - skills:      full metadata per skill (for init to pick by tag/profile/alias)
  - fits:        detect-stack → skill list (init uses this to "build fit")
  - raw_urls:    per-skill raw GitHub URL template so init can fetch the
                 SKILL.md + supporting files on demand (Option B: catalog on
                 GitHub, init fetches what it needs)

Usage:
  python scripts/build_catalog.py [--owner truongnat] [--repo simple-skills]
                                  [--branch main] [--out catalog.json]
  python scripts/build_catalog.py --check   # compare to committed catalog.json
                                            # (ignores meta.generated_at)

Exit 0 on success; 1 if a skill fails validation (name mismatch, missing
description, bad semver, etc.) or if --check finds catalog.json stale.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
OUT_DEFAULT = ROOT / "catalog.json"

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SKILL_KINDS = {"process", "domain", "reference"}
# Tuple (not set): list(PROVIDERS) must be stable across PYTHONHASHSEED / CI.
PROVIDERS = ("claude", "codex", "cursor", "gemini")

# detect-stack → skill ids. init merges every matching group.
FITS: dict[str, list[str]] = {
    "nodejs": [
        "nodejs-backend-patterns", "javascript-pro", "typescript-pro",
        "api-design-pro", "api-design-principles", "testing-pro",
        "javascript-testing-patterns", "e2e-testing-patterns",
    ],
    "react": [
        "react-pro", "nextjs-pro", "nextjs-15-pro", "shadcn-mastery-pro",
        "frontend-design-pro", "frontend-design", "design-system-pro",
        "design-system-patterns", "a11y-design-pro", "accessibility-compliance",
        "seo-pro", "ui-ux-system-pro",
    ],
    "vue": ["vue-pro", "frontend-design-pro", "a11y-design-pro"],
    "angular": ["angular-pro", "frontend-design-pro", "a11y-design-pro"],
    "mobile": [
        "react-native-pro", "flutter-pro", "ios-pro", "android-pro",
        "mobile-design-pro", "expo-native-ui", "expo-data-fetching",
    ],
    "python": [
        "python-pro", "fastapi-pro", "django-pro", "data-science-pro",
        "data-analysis-pro", "machine-learning-pro",
    ],
    "fastapi": ["fastapi-pro", "api-design-pro", "api-security-pro"],
    "go": ["go-pro", "api-design-pro"],
    "rust": ["rust-pro", "api-design-pro"],
    "java": ["java-pro", "spring-boot-pro"],
    "typescript": ["typescript-pro", "api-design-pro"],
    "database-postgres": [
        "postgresql-pro", "postgres-patterns", "prisma-postgres",
        "postgresql-table-design", "sql-optimization-patterns",
        "sql-data-access-pro", "database-migration",
    ],
    "database-mongo": ["mongodb-pro"],
    "database-redis": ["redis-pro", "caching-pro"],
    "database-elasticsearch": ["elasticsearch-pro"],
    "docker": ["docker-pro", "docker-compose-pro", "deployment-pro"],
    "kubernetes": ["kubernetes-pro", "infrastructure-as-code-pro", "network-infra-pro"],
    "cloud-aws": ["aws-pro", "deployment-pro", "cloud-native-agent-pro"],
    "cloud-gcp": ["deployment-pro", "cloud-native-agent-pro"],
    "cloud-azure": ["azure-storage", "deployment-pro"],
    "cloudflare": ["cloudflare-pro", "vercel-deployment-pro", "deployment-pro"],
    "security": [
        "security-pro", "security-review", "api-security-pro",
        "auth-pro", "auth-implementation-patterns", "sast-configuration",
        "stride-analysis-patterns", "ai-red-teaming-pro",
    ],
    "microservices": [
        "microservices-pro", "microservices-patterns", "system-design-pro",
        "system-design", "distributed-tracing", "hybrid-cloud-networking",
        "architecture-patterns", "architecture-decision-records",
    ],
    "testing": [
        "testing-pro", "test-driven-development-pro", "ttd-pro",
        "javascript-testing-patterns", "e2e-testing-patterns", "tester",
        "bug-discovery-pro",
    ],
    "data-engineering": [
        "data-engineering-pro", "data-science-pro", "data-analysis-pro",
        "mlops-pro", "machine-learning-pro",
    ],
    "ai-agents": [
        "ai-agents-pro", "agent-evaluation-pro", "mcp-server-pro",
        "prompt-engineering-pro", "a2a-protocol-pro", "parallel-agents-pro",
    ],
    "graphql": ["graphql-pro"],
    "websocket": ["websocket-pro", "stream-rtc-pro"],
    "documentation": ["docs", "technical-writing-pro", "writing-skills"],
    "business-analysis": [
        "business-analysis", "specify",
        "story-spec", "gap-analysis", "user-flow", "to-prd-pro",
        "product-management-pro", "market-research-pro", "report-writer",
    ],
    "office-docs": ["docx", "xlsx", "pptx", "pdf", "excel-doc-convert"],
}


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return None if end < 0 else text[4:end]


def _value(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:[ \t]*(.*)$", fm, re.MULTILINE)
    if not m:
        return ""
    first = m.group(1).strip()
    if first:
        if not first.startswith((">", "|")):
            return first.strip().strip("'\"")
    else:
        # Empty value with no block marker → list key (x-tags etc.), not a scalar.
        return ""
    lines: list[str] = []
    for line in fm[m.end() :].splitlines():
        if not line.strip():
            lines.append("")
            continue
        if re.match(r"^\s{2,}", line):
            lines.append(line.lstrip())
        else:
            break
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).strip()


def _list(fm: str, key: str) -> list[str]:
    raw = _value(fm, key)
    if not raw:
        # Block-style list: key:\n  - item
        m = re.search(rf"^{key}:[ \t]*(.*)$", fm, re.MULTILINE)
        if m and not m.group(1).strip():
            items: list[str] = []
            for line in fm[m.end() :].splitlines():
                if not line.strip():
                    continue
                if re.match(r"^\s+-\s+", line):
                    items.append(line.strip()[2:].strip().strip("'\""))
                else:
                    break
            return items
        return []
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [v.strip().strip("'\"") for v in raw.split(",") if v.strip()]


def _has_subdir(skill_dir: Path, name: str) -> bool:
    """True if a child directory exists whose name matches `name` case-insensitively.

    Vendor skills ship `Scripts/` (capital S). Linux CI is case-sensitive;
    macOS volumes often are not — a lowercase-only check disagrees across OS.
    """
    want = name.casefold()
    return any(p.is_dir() and p.name.casefold() == want for p in skill_dir.iterdir())


def comparable_catalog(catalog: dict) -> dict:
    """Catalog payload used for freshness checks (timestamp is not content)."""
    meta = {k: v for k, v in catalog["meta"].items() if k != "generated_at"}
    return {"meta": meta, "skills": catalog["skills"], "fits": catalog["fits"]}


def build_catalog(owner: str, repo: str, branch: str) -> dict:
    errors: list[str] = []
    skills: list[dict] = []
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"

    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            # Helpers (e.g. office-common) ship shared code, not a SKILL.md.
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{name}: missing/invalid frontmatter")
            continue

        fm_name = _value(fm, "name") or name
        if fm_name != name:
            errors.append(f"{name}: frontmatter name {fm_name!r} != dir name")
        description = _value(fm, "description")
        if not description:
            errors.append(f"{name}: missing description")
        version = _value(fm, "x-version") or "0.1.0"
        if not SEMVER_RE.match(version):
            errors.append(f"{name}: x-version {version!r} not semver")
        kind = _value(fm, "x-kind") or "domain"
        if kind not in SKILL_KINDS:
            errors.append(f"{name}: x-kind {kind!r} invalid")
        compatible = _list(fm, "x-compatible") or list(PROVIDERS)
        for prov in compatible:
            if prov not in PROVIDERS:
                errors.append(f"{name}: x-compatible {prov!r} invalid")

        skills.append(
            {
                "id": name,
                "name": fm_name,
                "description": description,
                "kind": kind,
                "version": version,
                "tags": _list(fm, "x-tags"),
                "roles": _list(fm, "x-roles"),
                "compatible": compatible,
                "aliases": _list(fm, "aliases"),
                "has_references": _has_subdir(skill_dir, "references"),
                "has_templates": _has_subdir(skill_dir, "templates"),
                "has_scripts": _has_subdir(skill_dir, "scripts"),
                "raw_skill": f"{raw_base}/skills/{name}/SKILL.md",
            }
        )

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return {}

    return {
        "meta": {
            "version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "skill_count": len(skills),
            "raw_base": raw_base,
        },
        "skills": skills,
        "fits": FITS,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="truongnat")
    parser.add_argument("--repo", default="simple-skills")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--out", type=Path, default=OUT_DEFAULT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate and compare to committed catalog.json (ignore generated_at)",
    )
    args = parser.parse_args()

    catalog = build_catalog(args.owner, args.repo, args.branch)
    if not catalog:
        return 1

    if args.check:
        if not OUT_DEFAULT.is_file():
            print("ERROR: catalog.json missing — run scripts/build_catalog.py", file=sys.stderr)
            return 1
        committed = json.loads(OUT_DEFAULT.read_text(encoding="utf-8"))
        if comparable_catalog(committed) != comparable_catalog(catalog):
            print("catalog.json is stale — run scripts/build_catalog.py", file=sys.stderr)
            return 1
        print(f"catalog OK: {catalog['meta']['skill_count']} skills")
        return 0

    args.out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {args.out} ({catalog['meta']['skill_count']} skills, "
          f"{len(catalog['fits'])} detect groups)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
