#!/usr/bin/env python3
"""Acceptance gate: EVERY published HTML page carries the full meta/structured-data set.

Added 2026-11-15 after a live audit found language index pages, /contact/, /docs/
and /for-ai/ shipping without description/OG/JSON-LD, and translation hreflang sets
missing the original-language tag, all while the old tests passed (they checked
presence of >=5 hreflang links, never their targets).

Rules:
- Every index.html has exactly one canonical, a meta description, og:title,
  og:description, og:url, a twitter:card, and at least one parseable JSON-LD block.
- og:image is optional, but when present its URL must point at a file that exists
  in this repo (no dead or fabricated images).
- For every translated post set, the original page and all four language variants
  carry the exact same hreflang set: en, ar, es, zh-Hans, he and x-default, where
  he and x-default point at the original URL.
"""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parent
BASE = 'https://ofershap.github.io'
fail = []

def check(cond, msg):
    if not cond:
        fail.append(msg)

pages = [f for f in ROOT.rglob('index.html') if 'engagement-backend' not in f.parts]
check(len(pages) > 1200, f'expected full tree, found {len(pages)} pages')
for f in sorted(pages):
    s = f.read_text(errors='replace')
    rel = str(f.relative_to(ROOT))
    check(s.count('rel="canonical"') == 1, f'{rel}: canonical count != 1')
    check('name="description"' in s, f'{rel}: no meta description')
    for pat in ('og:title', 'og:description', 'og:url'):
        check(pat in s, f'{rel}: no {pat}')
    check('twitter:card' in s, f'{rel}: no twitter:card')
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    check(bool(blocks), f'{rel}: no JSON-LD block')
    for b in blocks:
        try:
            json.loads(b)
        except Exception as e:
            fail.append(f'{rel}: unparsable JSON-LD: {e}')
    for m in re.finditer(r'property="og:image" content="([^"]+)"', s):
        u = m[1]
        if u.startswith(BASE):
            check((ROOT / u[len(BASE):].lstrip('/')).exists(), f'{rel}: og:image missing file {u}')

langs = ['en', 'ar', 'es', 'zh-Hans']
data = {l: json.loads((ROOT / 'translations' / (l + '.json')).read_text())['posts'] for l in langs}
ids = set(data['en'])
check(len(ids) == 100, 'translation set count changed')
for pid in sorted(ids):
    orig_path = data['en'][pid]['path']
    orig_url = BASE + '/' + orig_path.strip('/') + '/'
    os_ = (ROOT / orig_path / 'index.html').read_text()
    origlang = re.search(r'<html[^>]*lang="([^"]+)"', os_)[1]
    expect = {l: BASE + '/' + l + '/posts/linkedin-' + pid + '/' for l in langs}
    if origlang not in expect:
        expect[origlang] = orig_url
    expect['x-default'] = orig_url
    targets = [ROOT / orig_path / 'index.html'] + [ROOT / l / 'posts' / ('linkedin-' + pid) / 'index.html' for l in langs]
    for f in targets:
        s = f.read_text()
        got = dict(re.findall(r'hreflang="([^"]+)" href="([^"]+)"', s))
        check(got == expect, f'{f.relative_to(ROOT)}: hreflang mismatch got {sorted(got)}')

if fail:
    print(f'META COVERAGE GATE: {len(fail)} failures')
    for x in fail[:40]:
        print(' -', x)
    sys.exit(1)
print(f'meta coverage gate passed: {len(pages)} pages, 100 translation sets, exact hreflang targets')
