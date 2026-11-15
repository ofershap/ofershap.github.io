from pathlib import Path
import json,re,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent;ids=None
for lang in ['en','ar','es','zh-Hans']:
 data=json.loads((root/'translations'/(lang+'.json')).read_text())['posts']
 if ids is None:ids=set(data)
 assert set(data)==ids and len(ids)==100
 for id,r in data.items():
  f=root/lang/'posts'/('linkedin-'+id)/'index.html';s=f.read_text();assert 'translation-notice'not in s and 'class="author-card"'in s
  got=dict(re.findall(r'hreflang="([^"]+)" href="([^"]+)"',s))
  os_=(root/r['path']/'index.html').read_text();origlang=re.search(r'<html[^>]*lang="([^"]+)"',os_)[1]
  origurl='https://ofershap.github.io/'+r['path'].strip('/')+'/'
  variants={l:'https://ofershap.github.io/'+l+'/posts/linkedin-'+id+'/' for l in ['en','ar','es','zh-Hans']}
  expect=dict(variants)
  if origlang not in variants:expect[origlang]=origurl
  expect['x-default']=origurl
  assert got==expect,(f,sorted(got))
  assert r['source_link'].replace('&','&amp;')in s
  for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(m[1])
  for u in re.findall(r'(?:href|src)="(/[^"]*)"',s):assert(root/u.lstrip('/')).exists(),(f,u)
  assert not re.search('impressions_snapshot|likes_snapshot|comments_snapshot',s)
ET.parse(root/'sitemap.xml');print('400 translation schemas, source links, hreflang, internal paths and no private metrics passed')
