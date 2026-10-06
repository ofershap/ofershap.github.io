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
