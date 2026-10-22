---
title: "Agent authentication on ofershap.github.io"
description: "Which credentials an agent needs to use this site and its public endpoints: none."
---

# Agent authentication on ofershap.github.io

How an agent gets access to this site and its public endpoints, and exactly which credentials exist: none. Every surface listed here is public and keyless. This file lives at `/auth.md`, the conventional discovery path from the WorkOS auth.md spec (https://github.com/workos/auth.md). This site is static writing plus two read-only public APIs; it implements no registration, no tokens and no OAuth, and this file documents that honestly rather than performing an auth flow that does not exist.

## Discover

- All read surfaces are public and require no authentication: every page and its `index.md` markdown sibling, `/llms.txt`, `/llms-full.txt`, `/feed.xml`, `/sitemap.xml`, `/agents.md`, `/index.md`, `/.well-known/ard.json`, `/.well-known/ai-catalog.json`, `/.well-known/mcp/server-card.json`, `/openapi.json` and `/docs/`.
- The recipe-library MCP server at `https://recipes.gitshow.dev/mcp` (streamable HTTP POST) is public, read-only and keyless; tools `list_recipes` and `get_recipe`. Live status: `https://recipes.gitshow.dev/health`.
- The engagement API documented in `/openapi.json` (`/health`, `/stats` and the per-article counter endpoints) is public and keyless. It counts anonymous views and likes only.
- There is no `/.well-known/oauth-protected-resource` (RFC 9728) and no `agent_auth` metadata block, because no endpoint here is OAuth-protected.

## Pick a method

- No credential - this is the only method, and it covers every surface. Do not send an `Authorization` header, an API key or a cookie; they are never required and never checked.

## Register

There is no registration: no account, no sign-up endpoint, no `agent_auth.identity_endpoint`, and no `anonymous`, `service_auth`, or `identity_assertion` registration type. Nothing on this site issues API keys or tokens.

## Claim

There is no claim ceremony and no `agent_auth.claim_endpoint`. No credential exists to claim.

## Use credentials

Not applicable: no endpoint accepts or requires a credential. A request with no `Authorization` header is the complete, correct form.

## Errors

- No endpoint returns `401` or `403` for missing credentials, because none are required.
- There are no per-caller rate limits beyond the hosting platforms' own (GitHub Pages and the API workers). If a `429` ever appears, back off and retry; it is not an auth signal.

## Revocation

There is nothing to revoke: no keys, no tokens, no sessions, and no RFC 7009 `revocation_endpoint`, because no credentials are ever issued.

Questions: contact Ofer Shapira via https://ofershap.github.io/contact/ .
