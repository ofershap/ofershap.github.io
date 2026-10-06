# Ofer Shapira's writing archive

A static personal writing site hosted on GitHub Pages. No paid service, tracking script, or external build API is required.

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
