---
title: "Engagement API documentation"
canonical: https://ofershap.github.io/docs/
lang: en
---

# Engagement API

Public engagement API of ofershap.github.io: anonymous view and like counters, OpenAPI-documented, no authentication.

Base URL: `https://blog-engagement.ofers.workers.dev`

## Endpoints

- `GET /health` - Service health check
- `GET /stats` - Read engagement counters for one article
- `POST /stats` - Record a view, like or unlike for one article

## Scope

These are the only public endpoints. There is no public write access to content, no admin API and no authenticated surface to document.

Full documentation: https://ofershap.github.io/docs/
