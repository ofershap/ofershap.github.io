#!/usr/bin/env python3
"""Publish honest public documentation for the real engagement API.

Documents ONLY what engagement-backend/worker.js actually serves:
GET /health and GET/POST /stats on https://blog-engagement.ofers.workers.dev.
The /admin endpoints are private and intentionally undocumented.
"""
from pathlib import Path
import html
import json

R = Path(__file__).resolve().parent
BASE = 'https://ofershap.github.io'
API = 'https://blog-engagement.ofers.workers.dev'
E = html.escape

SPEC = {
    'openapi': '3.1.0',
    'info': {
        'title': 'ofershap.github.io Engagement API',
        'version': '1.0.0',
        'description': ('Anonymous engagement counters (views and likes) for articles on '
                        'ofershap.github.io. No authentication. Requests must come from the '
                        'site origin (CORS enforced). Rate limited per IP.'),
        'contact': {'name': 'Ofer Shapira', 'url': BASE + '/about/en/'},
    },
    'servers': [{'url': API, 'description': 'Cloudflare Workers production'}],
    'paths': {
        '/health': {
            'get': {
                'operationId': 'getHealth',
                'summary': 'Service health check',
                'responses': {
                    '200': {'description': 'Service is up', 'content': {'application/json': {'schema': {
                        'type': 'object',
                        'properties': {'ok': {'type': 'boolean'}, 'version': {'type': 'string'},
                                       'counting_since': {'type': 'string', 'format': 'date'}},
                        'required': ['ok', 'version']}}}}},
            }
        },
        '/stats': {
            'get': {
                'operationId': 'getStats',
                'summary': 'Read engagement counters for one article',
                'parameters': [
                    {'name': 'key', 'in': 'query', 'required': True,
                     'schema': {'type': 'string'},
                     'description': "Article path as served on the site, e.g. /posts/some-article/. Only published article paths are accepted."},
                    {'name': 'client', 'in': 'query', 'required': True,
                     'schema': {'type': 'string', 'pattern': '^[a-f0-9]{32}$'},
                     'description': 'Random 32-hex client identifier generated and stored by the reader browser; used only to deduplicate views and likes.'},
                ],
                'responses': {
                    '200': {'description': 'Counters for the article', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Stats'}}}},
                    '400': {'description': 'Invalid parameters', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '403': {'description': 'Origin header missing or not allowed', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '404': {'description': 'Unknown path', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '429': {'description': 'Rate limited (30 requests per minute per IP)', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                },
            },
            'post': {
                'operationId': 'recordEngagement',
                'summary': 'Record a view, like or unlike for one article',
                'requestBody': {'required': True, 'content': {'application/json': {'schema': {
                    'type': 'object',
                    'properties': {
                        'key': {'type': 'string', 'description': 'Article path, same rule as the GET parameter.'},
                        'client': {'type': 'string', 'pattern': '^[a-f0-9]{32}$'},
                        'action': {'type': 'string', 'enum': ['view', 'like', 'unlike']},
                    },
                    'required': ['key', 'client', 'action'],
                }}}},
                'responses': {
                    '200': {'description': 'Updated counters', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Stats'}}}},
                    '400': {'description': 'Invalid JSON or parameters', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '403': {'description': 'Origin header missing or not allowed', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '405': {'description': 'Method not allowed', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '413': {'description': 'Body over 1 KB', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                    '429': {'description': 'Rate limited', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}},
                },
            },
        },
    },
    'components': {'schemas': {
        'Stats': {
            'type': 'object',
            'properties': {
                'likes': {'type': 'integer', 'minimum': 0},
                'liked': {'type': 'boolean', 'description': 'Whether this client id already liked the article.'},
                'views': {'type': 'integer', 'minimum': 0,
                          'description': 'Present only after the article passes the public view threshold; omitted below it.'},
            },
            'required': ['likes', 'liked'],
        },
        'Error': {'type': 'object', 'properties': {'error': {'type': 'string'}}, 'required': ['error']},
    }},
}

BODY = '''<h1>Engagement API</h1>
<p>This site runs a small public API that keeps per-article view and like counters. It is anonymous, requires no authentication and no account, and is documented here so both people and AI agents can integrate against something real instead of guessing.</p>
<h2>Base URL</h2>
<p><code>https://blog-engagement.ofers.workers.dev</code> (Cloudflare Workers). The machine-readable contract is the <a href="/openapi.json">OpenAPI specification at /openapi.json</a>.</p>
<h2>Rules that apply to every request</h2>
<ul>
<li>Send the header <code>Origin: https://ofershap.github.io</code>. Other origins get <code>403</code>.</li>
<li><code>key</code> is the article path exactly as served here, for example <code>/posts/agent-long-creative-build-feedback/</code>. Unknown paths are rejected.</li>
<li><code>client</code> is a random 32-character lowercase hex id your client generates once and reuses; it deduplicates views and likes. No personal data is stored: IPs are salted and hashed for rate limiting only.</li>
<li>Rate limit: 30 requests per minute per IP, then <code>429</code>.</li>
<li>All errors are JSON: <code>{"error": "..."}</code> with status codes 400, 403, 404, 405, 413 or 429.</li>
</ul>
<h2>GET /health</h2>
<p>Liveness check, no parameters.</p>
<pre>curl https://blog-engagement.ofers.workers.dev/health
{"ok":true,"version":"1","counting_since":"2026-10-07"}</pre>
<h2>GET /stats</h2>
<p>Read counters for one article.</p>
<pre>curl -H "Origin: https://ofershap.github.io" \\
  "https://blog-engagement.ofers.workers.dev/stats?key=/posts/agent-long-creative-build-feedback/&amp;client=0123456789abcdef0123456789abcdef"
{"likes":0,"liked":false}</pre>
<p>The <code>views</code> field appears only after an article passes the public view threshold; below it the field is omitted on purpose.</p>
<h2>POST /stats</h2>
<p>Record one engagement. Body is JSON with <code>key</code>, <code>client</code> and <code>action</code> (one of <code>view</code>, <code>like</code>, <code>unlike</code>).</p>
<pre>curl -X POST -H "Origin: https://ofershap.github.io" -H "Content-Type: application/json" \\
  -d '{"key":"/posts/agent-long-creative-build-feedback/","client":"0123456789abcdef0123456789abcdef","action":"like"}' \\
  https://blog-engagement.ofers.workers.dev/stats
{"likes":1,"liked":true}</pre>
<p>A view counts once per client per day; a like is idempotent per client and can be withdrawn with <code>unlike</code>.</p>
<h2>Scope</h2>
<p>These are the only public endpoints. There is no public write access to content, no admin API and no authenticated surface to document; what is not listed here does not exist publicly.</p>'''


def build():
    (R / 'openapi.json').write_text(json.dumps(SPEC, ensure_ascii=False, indent=2))
    d = R / 'docs'
    d.mkdir(exist_ok=True)
    url = BASE + '/docs/'
    schema = {'@context': 'https://schema.org', '@type': 'TechArticle', 'headline': 'Engagement API documentation',
              'url': url, 'inLanguage': 'en', 'datePublished': '2026-10-19',
              'author': {'@type': 'Person', 'name': 'Ofer Shapira', 'url': BASE + '/about/en/'},
              'about': {'@type': 'APIReference', 'name': 'ofershap.github.io Engagement API', 'url': url}}
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Engagement API documentation | Ofer Shapira</title>'
            '<meta name="description" content="Public engagement API of ofershap.github.io: anonymous view and like counters, OpenAPI-documented, no authentication.">'
            '<link rel="canonical" href="' + url + '"><link rel="stylesheet" href="/style.css">'
            '<link rel="alternate" type="text/markdown" href="' + url + 'index.md"><script src="/webmcp.js" defer></script>'
            '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>'
            '</head><body><header><span class="site-name"><a href="/">Ofer Shapira</a></span>'
            '<nav><a href="/">Writing</a><a href="/about/en/">About</a></nav></header>'
            '<main><article>' + BODY + '</article>'
            '<footer><a href="/">All writing</a> · <a href="/feed.xml">RSS</a></footer></main></body></html>')
    (d / 'index.html').write_text(page)
    md = ['---', 'title: "Engagement API documentation"', 'canonical: ' + url, 'lang: en', '---', '',
          '# Engagement API', '',
          'Public engagement API of ofershap.github.io: anonymous view and like counters, '
          'OpenAPI-documented, no authentication.', '',
          'Base URL: `' + SPEC['servers'][0]['url'] + '`', '', '## Endpoints', '']
    for pth, ops in SPEC['paths'].items():
        for m, op in ops.items():
            md.append('- `' + m.upper() + ' ' + pth + '` - ' + op.get('summary', ''))
    md += ['', '## Scope', '',
           'These are the only public endpoints. There is no public write access to content, '
           'no admin API and no authenticated surface to document.', '',
           'Full documentation: ' + url]
    (R / 'docs.md').write_text('\n'.join(md) + '\n')
    if (d / 'llms.txt').exists():
        (d / 'llms.txt.md').write_text((d / 'llms.txt').read_text())
    # Homepage footer link so the docs are discoverable from the front page.
    p = R / 'index.html'
    s = p.read_text()
    if 'href="/docs/"' not in s:
        s = s.replace('<a href="https://gitshow.dev/ofershap">GitShow</a>',
                      '<a href="https://gitshow.dev/ofershap">GitShow</a>\n      <a href="/docs/">API</a>')
        p.write_text(s)
    # Sitemap entry (build_lastmod assigns the date).
    sp = R / 'sitemap.xml'
    sm = sp.read_text()
    if '<loc>' + url + '</loc>' not in sm:
        sm = sm.replace('</urlset>', '<url><loc>' + url + '</loc></url></urlset>')
        sp.write_text(sm)
    import build_lastmod
    build_lastmod.run()
    print('docs built')


if __name__ == '__main__':
    build()
