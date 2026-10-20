#!/usr/bin/env python3
"""Guard the markdown agent docs: exist, real links only, homepage alternate registered."""
from pathlib import Path
import re

R = Path(__file__).resolve().parent

agents = (R / 'agents.md').read_text()
assert agents.startswith('---\n') and '# Agents: how to use this site' in agents
assert 'https://recipes.gitshow.dev/mcp' in agents and 'no authentication' in agents
for path in ('/llms.txt', '/llms-full.txt', '/feed.xml', '/sitemap.xml', '/openapi.json',
             '/.well-known/ard.json', '/.well-known/agent-skills/index.json', '/posts/llms.txt'):
    assert path in agents, path

idx = (R / 'index.md').read_text()
assert idx.startswith('---\n') and '# Ofer Shapira' in idx
for path in ('/about/', '/for-ai/', '/posts/', '/llms.txt', '/agents.md'):
    assert path in idx, path

repo = (R / 'AGENTS.md').read_text()
assert 'build_' in repo and 'test_' in repo and 'github.io' in repo

home = (R / 'index.html').read_text()
assert '<link rel="alternate" type="text/markdown" href="/index.md">' in home

llms = (R / 'llms.txt').read_text()
assert '/agents.md' in llms

for fake in ('gpt-5', 'chatgpt-app', 'oauth', 'sandbox', 'api key'):
    blob = agents.lower()
    assert fake not in blob, 'no capability theater: ' + fake

# every site-internal URL in agents.md must resolve to a real file
for u in re.findall(r'https://ofershap\.github\.io(/[^\s|)]+)', agents):
    if '<' in u: continue
    local = R / u.lstrip('/')
    assert local.exists() or (local / 'index.html').exists() or (local / 'index.md').exists(), u
print('test_agent_docs: OK')
