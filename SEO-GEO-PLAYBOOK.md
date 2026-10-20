# Blog SEO/GEO Playbook (master copy)

Owner: Ofer Shapira. Maintainer: Instinct (content-engine task).
Created: 2026-10-19. Last updated: 2026-10-19 (north star set). Reviewed and updated by the 4x/day agent-readiness routine; every material change is explained in chat before editing.

## North star (set 2026-10-19, Ofer)
The explicit success measure: the name "Ofer Shapira" / "עופר שפירא" appears in AI chat answers (ChatGPT and other assistants) for relevant queries. The ora score and the rest of the battery are means, not the target. Every 4x/day routine report states name visibility: which free tool was queried, with what query, and whether and where the name appeared. Free name-visibility checks: Ahrefs AI Visibility Checker, HubSpot AI Search Grader, LLMrefs and Waikay (after signup), and direct prompts to free-tier assistant web UIs when accessible.

## Goal
Significant Google visibility for ofershap.github.io and presence in AI answers (ChatGPT, Gemini, Perplexity). Checkpoint: 2026-11-06 (impressions by country once Search Console data flows).

## Measurement battery (free, baselines 2026-10-19)
| Tool | What it measures | Baseline | Cadence |
|---|---|---|---|
| ora.ai (`npx ax audit ofershap.github.io --max-age=1`) | agent readiness | 79/100 B (20.10 21:19 fresh scan after homepage ItemList-of-recent-writing (Schema type breadth 0->1/2, wants 2 more homepage-matching types); was 78 same day 17:21 after top-level-Person-with-description + sameAs + post-level .md siblings + docs.md cluster: sameAs 0->2, JSON-LD structured data 3->4, Markdown URL fallback 1->2 all pass; was 76 same day after the BreadcrumbList/Blog-schema cluster; 73 on 19.10 after the agent-discovery cluster: real /.well-known ard.json+ai-catalog.json+MCP server card+agent-skills index+api-catalog+SKILL.md for the live recipe-library MCP, llms.txt when-to-use + section indexes; was 59 same day after the API docs cluster, 52 same morning, 48 on 2026-10-08) | 4x/day routine |
| Ahrefs AI Visibility Checker | brand mentions in AI answers | 0 ("Ofer Shapira") | weekly |
| Semrush free AI visibility | domain AI visibility | N/A (not visible yet) | weekly |
| validator.schema.org | structured data validity | pass, 0 errors | after schema changes |
| Bing Webmaster Tools | Bing indexing/impressions | 117 pages indexed, 2 clicks / 28 impressions in 6 months (21.10 WMT Site Explorer; earlier curl site: readings of 0 were automated-query blocking) | daily sweep |
| Bing WMT AI Performance | Microsoft Copilot grounding citations | 11 citations / 7 days, rising (peak 7 on 18.10) - first measured AI-engine citation signal | daily sweep |
| Google Search Console | Google indexing/impressions | property verified; coverage broken historically (2/1,150 pages on 7.10), sitemap resubmitted | daily sweep |
| Cloudflare Web Analytics | real visits + AI referrals | ~20 visits/day, 4 AI referrals | daily sweep |
| duck.ai direct prompt ("Who is Ofer Shapira, the AI engineering blogger?") | name presence in a live assistant answer | 19.10: NAME APPEARS - mostly-accurate profile (AI engineering lead, 15+ yrs, Cursor adoption for 50+ engineers, agents for small businesses in Israel); sources labeled hashnode.com/hashnode.dev (old crossposts), ofershap.github.io not cited | rotation in 4x/day routine |
| HubSpot AI Search Grader | brand perception by LLM | ChatGPT 31, Google 50, Perplexity 65 (20.10; sentiment 31/40 - engines already know him a little). Form inputs for comparability: company "Ofer Shapira", geography Israel, products "AI engineering consulting, AI agents and developer tools", industry "Software and AI" | quarterly |
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
Free tactics only. No Buffer mutations from this routine. Publishing to the blog is pre-approved. Report to main only on score change, name-visibility change, real obstacle, or a paid step; each report states the current name-visibility finding.
