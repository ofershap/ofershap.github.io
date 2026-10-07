# Blog engagement

Runs on the existing Cloudflare Workers Free plan using a SQLite Durable Object. No upgrade or paid resource. Exceeding free limits produces errors instead of charges. Frontend remains readable if the service fails.

Views start 2026-10-07, once per anonymous browser/article/UTC day; this is not a unique-person metric. Translations share original article counts. Likes are reversible, browser-based and not proof of identity. Public endpoints return likes only. Owner dashboard: /admin, with access key stored in the vault. Owner view totals API: GET /admin/stats with the separately vaulted bearer credential. Never commit admin or rate-limit secrets.

Deployment source: worker.js and wrangler.jsonc. Required secrets: ADMIN_TOKEN, RATE_SALT. Regenerate the article allowlist with `python3 build_engagement.py` and redeploy when new articles are added. Browser identifiers with unliked inactive views expire after 90 days; IP rate hashes expire within an hour. Rate limiting is a basic deterrent, not perfect bot protection.

Owner statistics are available to the assistant through the authenticated endpoint; request a report by article. Cloudflare account dashboard also exposes the database. No historical traffic or like counts are backfilled.

## Optional public views (activated 2026-10-07)

`PUBLIC_VIEWS=true` was activated with owner approval on 2026-10-07. Set `PUBLIC_VIEWS=false` to hide public views. and optionally `PUBLIC_VIEWS_THRESHOLD` (default 100). The public API omits the view field unless enabled and the count is strictly greater than the threshold. Counts of 100 or less remain private. The frontend only shows the field when the backend returns it. Turning the switch off hides counts again. This is per-article browser-day views, shared by translations, not unique people. Update the privacy notice if activating.
