#!/usr/bin/env python3
"""Guard the public API documentation: it must stay honest and complete."""
from pathlib import Path
import json

R = Path(__file__).resolve().parent

spec = json.loads((R / 'openapi.json').read_text())
paths = set(spec['paths'])
assert paths == {'/health', '/stats'}, 'only real public endpoints documented: %s' % paths
assert '/admin' not in json.dumps(spec), 'admin endpoints must never be documented'
assert spec['servers'][0]['url'] == 'https://blog-engagement.ofers.workers.dev'
for method in spec['paths']['/stats'].values():
    codes = set(method['responses'])
    assert '200' in codes and any(c.startswith('4') for c in codes), 'JSON error responses must be documented'
stats_post = spec['paths']['/stats']['post']['requestBody']['content']['application/json']['schema']
assert stats_post['properties']['action']['enum'] == ['view', 'like', 'unlike']

docs = (R / 'docs' / 'index.html').read_text()
assert '/openapi.json' in docs, 'docs page must link the spec'
assert 'blog-engagement.ofers.workers.dev' in docs, 'docs page must name the real base URL'
assert '/admin' not in docs, 'docs page must not mention admin endpoints'
assert 'canonical' in docs and 'application/ld+json' in docs

home = (R / 'index.html').read_text()
assert 'href="/docs/"' in home, 'homepage must link the API docs'

sitemap = (R / 'sitemap.xml').read_text()
assert '<loc>https://ofershap.github.io/docs/</loc>' in sitemap, 'docs page must be in the sitemap'
print('test_api_docs: OK')
