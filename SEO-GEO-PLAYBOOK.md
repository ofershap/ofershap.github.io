# Blog SEO/GEO Playbook (master copy)

Owner: Ofer Shapira. Maintainer: Instinct (content-engine task).
Created: 2026-10-19. Last updated: 2026-10-19 (decision record added). Reviewed and updated by the 4x/day agent-readiness routine; every material change is explained in chat before editing.

## Goal
Significant Google visibility for ofershap.github.io and presence in AI answers (ChatGPT, Gemini, Perplexity). Checkpoint: 2026-11-06 (impressions by country once Search Console data flows).

## Measurement battery (free, baselines 2026-10-19)
| Tool | What it measures | Baseline | Cadence |
|---|---|---|---|
| ora.ai (`npx ax audit ofershap.github.io`) | agent readiness | 52/100 C (was 48 on 2026-10-08) | 4x/day routine |
| Ahrefs AI Visibility Checker | brand mentions in AI answers | 0 ("Ofer Shapira") | weekly |
| Semrush free AI visibility | domain AI visibility | N/A (not visible yet) | weekly |
| validator.schema.org | structured data validity | pass, 0 errors | after schema changes |
| Bing Webmaster Tools | Bing indexing/impressions | 7 impressions/7d, 0 clicks | daily sweep |
| Google Search Console | Google indexing/impressions | property verified; coverage broken historically (2/1,150 pages on 7.10), sitemap resubmitted | daily sweep |
| Cloudflare Web Analytics | real visits + AI referrals | ~20 visits/day, 4 AI referrals | daily sweep |
| HubSpot AI Search Grader | brand perception by LLM | ChatGPT 33/100, Google 50/100 (sentiment 31/40 - engines already know him a little) | quarterly |
| PageSpeed Insights | CWV/perf/SEO/a11y | pending free API key (GCP project under Instinct's email) | when key exists |

## The funnel (in priority order)
1. Indexing: valid sitemap with real lastmod (done 19.10), IndexNow ping to Bing (key live 19.10), internal links from homepage to every post (done 19.10), GSC coverage monitoring.
2. Content that can rank: the authored Q&A guides are the ranking assets - answer-first openings, FAQ schema, comparison tables with real numbers, original research. 2 new guides/day. The 780 archived LinkedIn posts are archive, not ranking assets; do not expect them to rank.
3. Topical authority: grow deliberate clusters around AI agents in practice, AI engineering leadership, and Hebrew AI-how-to; interlink cluster members.
4. Distribution/authority: canonical crossposts (dev.to/Hashnode/Medium), genuinely helpful community answers, editor pitches (Geektime workstream). New domain = authority is the bottleneck; mentions move it.
5. Agent readiness: ora.ai checklist items that fit a static blog (see below).

## What transfers from published "fast ranking" case studies
- Long-tail, low-competition queries first; a new domain does not win head terms.
- Tight interlinked topical clusters beat scattered topics.
- Publishing velocity with consistent quality (already doing).
- Freshness signals: real lastmod, updating winners.
- Unique value per page; thin templated pages do not rank (programmatic-SEO lesson).

## Honest limits (do not chase)
- ora.ai 100/100 is not reachable on a static GitHub Pages blog: HTTP Link headers, Accept/UA content negotiation, ?mode=agent, NLWeb endpoints, and the OAuth/auth.md/PAP families need a server or an authenticated API the blog does not have; a Wikipedia article is not appropriate (notability); a ChatGPT app listing needs a real app. Realistic ceiling estimate: 85-92. Payments is already N/A.
- The OpenAPI/public-api points are pursued only by documenting the real engagement API (likes/views worker), never a fake spec.

## Decisions
- 2026-10-19 (Ofer): the blog stays on ofershap.github.io - GitHub prestige over edge-programmability. No own-domain move. ora target on this domain: 85-92. Server-edge checks are out of scope (Accept/UA content negotiation, HTTP Link headers, ?mode=agent, NLWeb endpoints), plus Wikipedia (notability), ChatGPT app listing (needs a real app) and sandbox environment (theatre for a blog).

## Standing rules
Free tactics only. No Buffer mutations from this routine. Publishing to the blog is pre-approved. Report to main only on score change, real obstacle, or a paid step.
