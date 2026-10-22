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
    if 'trustManifest' in e:
        assert e['trustManifest']['identity'] == 'did:web:ofershap.github.io', 'only our honest did:web identity'

card = json.loads((WK / 'mcp' / 'recipe-library.json').read_text())
assert card['$schema'] == 'https://static.modelcontextprotocol.io/schemas/v1/server-card.schema.json'
assert card['name'] == 'recipe-library' and card['version'] and card['description']
remote = card['remotes'][0]
assert remote['type'] == 'streamable-http' and remote['url'] == 'https://recipes.gitshow.dev/mcp'
assert {t['name'] for t in card['_meta']['dev.ofershap/tools']} == {'list_recipes', 'get_recipe'}
assert json.loads((WK / 'mcp' / 'server-card.json').read_text()) == card, 'server-card.json must mirror recipe-library.json'
mcp_manifest = json.loads((WK / 'mcp.json').read_text())
assert mcp_manifest['servers'][0]['endpoint'] == 'https://recipes.gitshow.dev/mcp'
did = json.loads((WK / 'did.json').read_text())
assert did['id'] == 'did:web:ofershap.github.io'
assert 'https://github.com/ofershap' in did['alsoKnownAs']
assert ard['host']['identifier'] == 'did:web:ofershap.github.io'
tm = ard['entries'][0]['trustManifest']
assert tm['identity'] == 'did:web:ofershap.github.io'
assert tm['provenance'][0]['sourceId'] == 'https://github.com/ofershap/ofershap.github.io'
assert 'signature' not in tm and 'attestations' not in tm, 'no trust claims we cannot prove'

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
assert len(llms) < 30000, f'llms.txt must stay slim for agent readers, got {len(llms)} chars'
_recent = llms.split('## Recent original-language posts', 1)[1].split('## Existing essays', 1)[0]
assert _recent.count('- [') <= 26, f'recent posts section capped at 25 posts + index pointer, got {_recent.count(chr(45)+chr(32)+chr(91))}'
assert 'posts/llms.txt' in _recent  # full index pointer survives trimming

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
assert 'recipes.gitshow.dev/health' in llms and 'recipe-library.json' in llms  # endpoint itself lives in the server card; llms.txt links resolve on GET
