# Ofer Shapira's writing archive

A static personal writing site hosted on GitHub Pages. No paid service or external build API is required. Views and likes use the free engagement backend described below.

## Content rules

- Preserve existing article URLs and translations.
- Import only Ofer's already-published personal posts. Never import queued drafts, company-page posts, or another author's posts.
- Match records by LinkedIn activity ID before adding a post.
- Preserve the original text and source link. Do not invent dates, facts, translations, or missing media.
- Source timestamps in the initial backfill were decoded from LinkedIn activity IDs and checked against the existing archive. Future imports should use the verified publication timestamp from the source when available.
- Media links in exports can expire. Download accessible original media into each article's folder. If an image or video is unavailable, keep an honest link to the original LinkedIn post instead of substituting an illustration.

## Rebuild

```sh
python3 build_archive.py
python3 -m http.server 8000
```

`archive-source.json` contains public post text, original URLs, timestamp provenance and text hashes. It contains no private conversation history, performance metrics, or credentials.

Before publishing, validate all JSON-LD, the sitemap and RSS XML, local links, article text/source matching, deduplication, and desktop/mobile/RTL layouts. The Pages workflow publishes the repository after a push to `main`.

## Ongoing updates

For each confirmed LinkedIn publication, add one idempotent source record with the exact published text, verified date, original URL and accessible media. Rebuild and test. Scheduled posts must not appear in this archive before they are actually published.

## Search and AI discovery

Use semantic HTML, original text, clear author/source attribution, stable canonical URLs, article structured data, a sitemap and RSS. Markdown twins provide a readable alternative. `llms.txt` is a convenience, not a promise of ranking or citations. Search engines and answer engines decide what to index and cite.

## Multilingual experiment

100 selected published posts are available in English, Arabic, Spanish and Simplified Chinese. The translations are machine-generated and not reviewed by human translators. Historical claims are preserved, not endorsed as current facts. Each translation keeps the original publication date and source URL, and links back to the archived original. Translation source JSON contains no performance metrics.

Run `python3 build_archive.py` to rebuild originals, identity/discovery files and translations. After rebuilding, run `python3 test_archive.py` and inspect mobile/RTL pages. Existing English archive URLs remain unchanged.

Measure impressions by country and language in Search Console/Bing one month after deployment, once those services are connected and have data. Do not promise indexing or AI citations.

## Engagement

Article likes, share buttons and private view counts are added by `build_engagement.py`. Views start on 2026-10-07, not at the original publication date. Browser-based estimates are not verified unique people. See `/privacy/` and `engagement-backend/README.md` for limits and deployment. No advertising widgets or marketing posts are added.

## Original service Q&A

Four separately reviewed, authored Hebrew Q&A posts are maintained in `authored-source.json` and rendered by `build_authored.py`. This is not a LinkedIn import. Their original reviewed bodies are preserved byte-exact in each `original.md`, with GEO summaries, FAQs and service links kept separate. Publication dates are actual blog dates. Discovery and engagement builders preserve these pages; engagement controls remain limited to the original archive until the backend allowlist is extended.
