#!/usr/bin/env python3
"""Guard the agent-discovery files: real entries only, spec-shaped, consistent."""
from pathlib import Path
import hashlib
import json

R = Path(__file__).resolve().parent
WK = R / '.well-known'

ard = json.loads((WK / 'ard.json').read_text())
assert json.loads((WK / 'ai-catalog.json').read_text()) == ard, 'ai-catalog.json must mirror ard.json'
assert len(ard['entries']) >= 2
for e in ard['entries']:
    assert e['identifier'].startswith('urn:air:ofershap.github.io:'), e['identifier']
    assert e['displayName'] and e['type']
    assert ('url' in e) != ('data' in e), 'exactly one of url/data'
    assert 2 <= len(e['representativeQueries']) <= 5
    assert 'trustManifest' not in e, 'no fabricated trust data'

card = json.loads((WK / 'mcp' / 'recipe-library.json').read_text())
assert card['endpoint'] == 'https://recipes.gitshow.dev/mcp' and card['authentication'] == 'none'
assert {t['name'] for t in card['tools']} == {'list_recipes', 'get_recipe'}

idx = json.loads((WK / 'agent-skills' / 'index.json').read_text())
assert idx['$schema'] == 'https://schemas.agentskills.io/discovery/0.2.0/schema.json'
skill = idx['skills'][0]
skill_file = WK / 'agent-skills' / 'recipe-library-mcp' / 'SKILL.md'
assert skill['url'] == '/.well-known/agent-skills/recipe-library-mcp/SKILL.md'
assert skill['digest'] == 'sha256:' + hashlib.sha256(skill_file.read_bytes()).hexdigest()
assert skill_file.read_text().startswith('---\nname: recipe-library-mcp')

cat = json.loads((WK / 'api-catalog').read_text())
linkset = cat['linkset'][0]
assert linkset['service-desc'][0]['href'] == 'https://ofershap.github.io/openapi.json'

llms = (R / 'llms.txt').read_text()
assert '## When to use this site' in llms
assert '/docs/llms.txt' in llms
assert (R / 'docs' / 'llms.txt').read_text().startswith('# Engagement API documentation')

blob = json.dumps(ard) + json.dumps(card) + skill_file.read_text()
for fake in ('gpt-5', 'chatgpt-app', 'oauth', 'sandbox'):
    assert fake not in blob.lower(), 'no capability theater: ' + fake
print('test_agent_discovery: OK')

# Round-2 lock-ins: specVersion, MCP endpoint visibility, api-catalog items, second section index
ard2 = json.loads((WK / 'ard.json').read_text())
assert ard2['specVersion'] == '1.0'
assert ard2['entries'][0]['metadata']['mcpEndpoint'] == 'https://recipes.gitshow.dev/mcp'
cat2 = json.loads((WK / 'api-catalog').read_text())
assert len(cat2['linkset'][0]['item']) == 2
assert '## When to use this skill' in skill_file.read_text()
assert '/posts/llms.txt' in (R / 'llms.txt').read_text()
assert (R / 'posts' / 'llms.txt').exists()
