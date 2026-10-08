from pathlib import Path
import json,re,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent;ids=None
for lang in ['en','ar','es','zh-Hans']:
 data=json.loads((root/'translations'/(lang+'.json')).read_text())['posts']
 if ids is None:ids=set(data)
 assert set(data)==ids and len(ids)==100
 for id,r in data.items():
  f=root/lang/'posts'/('linkedin-'+id)/'index.html';s=f.read_text();assert 'translation-notice'not in s and 'class="author-card"'in s
  assert len(re.findall(r'<link[^>]*hreflang=',s))>=5
  assert r['source_link'].replace('&','&amp;')in s
  for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(m[1])
  for u in re.findall(r'(?:href|src)="(/[^"]*)"',s):assert(root/u.lstrip('/')).exists(),(f,u)
  assert not re.search('impressions_snapshot|likes_snapshot|comments_snapshot',s)
ET.parse(root/'sitemap.xml');print('400 translation schemas, source links, hreflang, internal paths and no private metrics passed')
