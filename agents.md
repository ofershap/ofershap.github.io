---
title: "Agents: how to use this site"
description: "Machine-readable entry points and citation rules for Ofer Shapira's blog"
---

# Agents: how to use this site

Ofer Shapira's blog - first-hand writing on AI engineering, agents, software architecture and engineering leadership, in Hebrew and English.

## Machine-readable resources

| Resource | URL |
|---|---|
| Contact | https://ofershap.github.io/contact/ |
| Site map for LLMs | https://ofershap.github.io/llms.txt |
| Full-text archive (all posts) | https://ofershap.github.io/llms-full.txt |
| This file | https://ofershap.github.io/agents.md |
| Homepage (markdown) | https://ofershap.github.io/index.md |
| Writing archive index | https://ofershap.github.io/posts/llms.txt |
| Engagement API docs index | https://ofershap.github.io/docs/llms.txt |
| RSS feed | https://ofershap.github.io/feed.xml |
| XML sitemap | https://ofershap.github.io/sitemap.xml |
| OpenAPI spec (engagement API) | https://ofershap.github.io/openapi.json |
| Agent resource discovery (ARD) | https://ofershap.github.io/.well-known/ard.json |
| AI resource catalog | https://ofershap.github.io/.well-known/ai-catalog.json |
| API catalog (api-catalog RFC) | https://ofershap.github.io/.well-known/api-catalog |
| MCP server card | https://ofershap.github.io/.well-known/mcp/recipe-library.json |
| Agent skills index | https://ofershap.github.io/.well-known/agent-skills/index.json |

## Per-post markdown

Every post page serves a markdown version at `index.md` inside its directory, e.g. `https://ofershap.github.io/posts/<slug>/index.md`, and declares it with `<link rel="alternate" type="text/markdown">`.

## MCP server

The recipe library runs a real MCP server at `https://recipes.gitshow.dev/mcp` (streamable HTTP, no authentication) with tools `list_recipes` and `get_recipe`. See the server card above for details.

## Citing

Cite pages by their canonical URL and attribute to Ofer Shapira (עופר שפירא). Each post links its original source and publication date.
