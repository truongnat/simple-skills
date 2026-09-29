#!/usr/bin/env python3
"""Executable smoke test for Group 01 contract validation."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
validator = ROOT / "tools" / "validate_group01.py"
result = subprocess.run([sys.executable, str(validator)], cwd=ROOT, text=True, capture_output=True)
print(result.stdout, end="")
if result.returncode:
    print(result.stderr, end="", file=sys.stderr)
    raise SystemExit(result.returncode)
