#!/usr/bin/env python3
"""Generate the markdown agent docs: /agents.md, /index.md and repo AGENTS.md,
and register the homepage markdown alternate link. Idempotent."""
from pathlib import Path
import re

R = Path(__file__).resolve().parent
SITE = 'https://ofershap.github.io'

AGENTS_MD = '''---\ntitle: "Agents: how to use this site"\ndescription: "Machine-readable entry points and citation rules for Ofer Shapira's blog"\n---\n\n# Agents: how to use this site

Ofer Shapira's blog - first-hand writing on AI engineering, agents, software architecture and engineering leadership, in Hebrew and English.

## Machine-readable resources

| Resource | URL |
|---|---|
| Site map for LLMs | {S}/llms.txt |
| Full-text archive (all posts) | {S}/llms-full.txt |
| This file | {S}/agents.md |
| Homepage (markdown) | {S}/index.md |
| Writing archive index | {S}/posts/llms.txt |
| Engagement API docs index | {S}/docs/llms.txt |
| RSS feed | {S}/feed.xml |
| XML sitemap | {S}/sitemap.xml |
| OpenAPI spec (engagement API) | {S}/openapi.json |
| Agent resource discovery (ARD) | {S}/.well-known/ard.json |
| AI resource catalog | {S}/.well-known/ai-catalog.json |
| API catalog (api-catalog RFC) | {S}/.well-known/api-catalog |
| MCP server card | {S}/.well-known/mcp/recipe-library.json |
| Agent skills index | {S}/.well-known/agent-skills/index.json |

## Per-post markdown

Every post page serves a markdown version at `index.md` inside its directory, e.g. `{S}/posts/<slug>/index.md`, and declares it with `<link rel="alternate" type="text/markdown">`.

## MCP server

The recipe library runs a real MCP server at `https://recipes.gitshow.dev/mcp` (streamable HTTP, no authentication) with tools `list_recipes` and `get_recipe`. See the server card above for details.

## Citing

Cite pages by their canonical URL and attribute to Ofer Shapira (עופר שפירא). Each post links its original source and publication date.
'''.format(S=SITE)

INDEX_MD = '''---\ntitle: "Ofer Shapira"\ndescription: "AI engineering, agents and software leadership - first-hand writing in Hebrew and English"\nlang: en\n---\n\n# Ofer Shapira

AI engineering, agents and software leadership - first-hand, dated writing in Hebrew and English.

- About: {S}/about/ ([English bio]({S}/about/en/))
- For AI assistants: {S}/for-ai/
- Writing archive: {S}/posts/ (recent posts listed in {S}/llms.txt)
- Essays: {S}/essays/
- English section: {S}/en/
- Recipe library MCP server: https://recipes.gitshow.dev/mcp

Machine-readable entry points: {S}/llms.txt, {S}/agents.md, {S}/feed.xml, {S}/sitemap.xml.
'''.format(S=SITE)

AGENTS_REPO = '''# AGENTS.md - working on this repository

Static blog of Ofer Shapira, served by GitHub Pages from this repo root. No framework; Python build scripts generate and patch the HTML.

## Build and test

- Build scripts are `build_*.py` (idempotent; run with `python3 build_<name>.py`).
- Tests are `test_*.py`; run all with `for t in test_*.py; do python3 "$t"; done`. All must pass before pushing.
- Pushing to `main` deploys the live site at https://ofershap.github.io/.

## Conventions

- Content is Hebrew-first with English companions; keep original-language source text byte-exact.
- Never fabricate capabilities: agent-facing files (`.well-known/`, `openapi.json`, llms.txt) describe only real, live endpoints. The test suites enforce this.
- The engagement API (`engagement-backend/`, Cloudflare worker) is the only dynamic backend; document it honestly, no auth theater.
- Recipe collection terminology: "ספרייה"/"ספריית המתכונים" in Hebrew, "Recipe library" in English.
'''

(R / 'agents.md').write_text(AGENTS_MD)
(R / 'index.md').write_text(INDEX_MD)
(R / 'AGENTS.md').write_text(AGENTS_REPO)

p = R / 'index.html'
s = p.read_text()
link = '<link rel="alternate" type="text/markdown" href="/index.md">'
if 'type="text/markdown"' not in s:
    s = s.replace('<link rel="alternate" type="application/rss+xml"',
                  link + '<link rel="alternate" type="application/rss+xml"', 1)
    p.write_text(s)
print('build_agent_docs: OK')
