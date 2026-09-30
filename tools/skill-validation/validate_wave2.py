#!/usr/bin/env python3
"""Deterministic Wave 2 content and routing gates."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
P1 = {
    'sk-accounting-pro': 'references/accounting-validation-matrix.md',
    'sk-expo-data-fetching': 'references/data-fetching-validation-matrix.md',
    'sk-expo-native-ui': 'references/native-ui-validation-matrix.md',
    'sk-financial-analysis-pro': 'references/financial-model-validation.md',
    'sk-fintech-integration-pro': 'references/fintech-integration-validation.md',
    'sk-github-actions-templates': 'references/workflow-validation-matrix.md',
    'sk-hybrid-cloud-networking': 'references/hybrid-network-troubleshooting-and-rollback.md',
    'sk-mlops-pro': 'references/mlops-evaluation-and-release-matrix.md',
    'sk-solidity-security': 'references/solidity-attack-and-invariant-matrix.md',
}
P2 = ['sk-spring-boot-pro','sk-django-pro','sk-biz-model','sk-engineering-management-pro','sk-fullstack-rag-pro','sk-ai-agents-pro','sk-ai-red-teaming-pro','sk-data-science-pro','sk-data-engineering-pro','sk-machine-learning-pro','sk-office-common','sk-pdf','sk-pptx','sk-xlsx','sk-docx','sk-clean-architecture','sk-debugging-strategies','sk-javascript-testing-patterns','sk-microservices-patterns','sk-stride-analysis-patterns']
ROUTES = {
    'accounting close/reconciliation': 'sk-accounting-pro',
    'payment webhook/idempotency': 'sk-fintech-integration-pro',
    'Expo cache/cancellation': 'sk-expo-data-fetching',
    'native safe-area/accessibility': 'sk-expo-native-ui',
    'GitHub workflow permissions/rollback': 'sk-github-actions-templates',
    'model drift/canary': 'sk-mlops-pro',
    'reentrancy/storage collision': 'sk-solidity-security',
    'schema migration/restore': 'sk-database-migration',
    'final claim evidence': 'sk-verify-pro',
}
errors = []
for name, rel in P1.items():
    skill = ROOT/'skills'/name
    ref = skill/rel
    if not ref.is_file(): errors.append(f'{name}: missing {rel}'); continue
    skill_text = (skill/'SKILL.md').read_text()
    text = ref.read_text()
    if f'./{rel}' not in skill_text: errors.append(f'{name}: reference not linked')
    rows = [line for line in text.splitlines() if line.startswith('| ') and not line.startswith('|---') and 'Scenario' not in line]
    if not 6 <= len(rows) <= 10: errors.append(f'{name}: expected 6-10 matrix rows, got {len(rows)}')
    for marker in ('Expected result', 'Evidence', 'failure', 'limitation', 'Next owner', 'sk-verify-pro'):
        if marker.lower() not in text.lower(): errors.append(f'{name}: missing {marker}')
    if 'final release status' not in text.lower(): errors.append(f'{name}: missing non-final-owner guard')
for name in P2:
    p = ROOT/'skills'/name/'references'/'worked-scenarios-and-evidence.md'
    if not p.is_file(): errors.append(f'{name}: missing worked scenario pack'); continue
    text = p.read_text().lower()
    for marker in ('positive scenario','negative or edge scenario','expected evidence','sk-verify-pro'):
        if marker not in text: errors.append(f'{name}: missing {marker}')
fixture = ROOT/'tools/skill-validation/wave2-routing-fixtures.md'
if not fixture.is_file(): errors.append('routing fixture missing')
else:
    known = {p.name for p in (ROOT/'skills').glob('sk-*') if p.is_dir()}
    for prompt, owner in ROUTES.items():
        if owner not in known: errors.append(f'{prompt}: owner {owner} missing')
        if prompt not in fixture.read_text(): errors.append(f'{prompt}: fixture row missing')
if errors:
    print('WAVE2_VALIDATION FAIL')
    print('\n'.join(f'- {e}' for e in errors))
    raise SystemExit(1)
print(f'WAVE2_VALIDATION PASS p1={len(P1)} p2={len(P2)} routes={len(ROUTES)}')
