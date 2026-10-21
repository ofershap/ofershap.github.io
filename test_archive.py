#!/usr/bin/env python3
from pathlib import Path
import json,re,xml.etree.ElementTree as ET,hashlib,html
ROOT=Path(__file__).resolve().parent
records=json.loads((ROOT/'archive-source.json').read_text());ids=set();errors=[]
for r in records:
 assert r['id'] not in ids;ids.add(r['id'])
 assert hashlib.sha256(r['text'].encode()).hexdigest()==r['sha256']
 if r['existing'] or not r['text'].strip():continue
 p=ROOT/'posts'/('linkedin-'+r['id'])/'index.html'
 assert p.exists(),p
 s=p.read_text();assert html.escape(r['source'],quote=True) in s
 for paragraph in re.split(r'\n\s*\n',r['text']):
  if not paragraph.strip():continue
  # Link markup must not change published prose.
  assert html.escape(paragraph.splitlines()[0].split('https://')[0]) in s
for p in ROOT.glob('posts/*/index.html'):
 s=p.read_text();assert '<h1' in s
 for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(m[1])
for p in ['sitemap.xml','feed.xml']:ET.parse(ROOT/p)
print('Validated',len(ids),'source records; structured data, original text hashes, source links and XML passed.')

# Per-post publication checklist (routine gate): every archived post must ship the full
# agent-readiness set - OG tags, JSON-LD, markdown alternate, Microdata, WebMCP script,
# semantic markup (no onclick), and an llms.txt entry.
import re as _re
from pathlib import Path as _P
_llms=_P('llms.txt').read_text()
_sitemap=_P('sitemap.xml').read_text()
_checked=0
for _f in sorted(_P('.').glob('posts/*/index.html'))[:100000]:
    _h=_f.read_text(); _u='https://ofershap.github.io/posts/'+_f.parent.name+'/'
    for _og in ('og:type','og:title','og:description','og:url'):
        assert f'property="{_og}"' in _h, (_f,_og)
    assert 'application/ld+json' in _h, (_f,'ld+json')
    assert 'rel="alternate" type="text/markdown"' in _h, (_f,'alternate link')
    assert _f.parent.joinpath('index.md').exists(), (_f,'index.md missing')
    assert 'itemtype="https://schema.org/BlogPosting"' in _h, (_f,'microdata')
    assert 'itemprop="headline"' in _h and 'itemprop="datePublished"' in _h and 'itemprop="articleBody"' in _h, (_f,'microdata fields')
    assert '<script src="/webmcp.js" defer></script>' in _h, (_f,'webmcp')
    assert 'onclick=' not in _h and 'role="button"' not in _h, (_f,'semantic markup')
    _dm=_re.search(r'"datePublished"\s*:\s*"([^"]+)"',_h)
    if _dm and _dm[1][:10]>='2026-10-21':
        assert _u in _llms, (_f,'llms.txt entry for new post')
    assert _u in _sitemap, (_f,'sitemap entry')
    _checked+=1
print('per-post checklist: OK on',_checked,'posts')
