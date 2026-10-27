#!/usr/bin/env python3
"""Audit existing archive media. Use --require IDs after each sync; never treat
missing assets or source-only flags as completion. No downloads or mutations.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,json,re,sys,hashlib,urllib.parse
ROOT=Path(__file__).resolve().parent
SOURCE_PATHS={}
def sourceid(u):
 m=re.search(r'(?:activity-|urn:li:(?:share|activity|ugcPost):)(\d{19})',u or '')
 return m[1] if m else None
class SourceLinks(HTMLParser):
 def __init__(self,s):self.depth=0;self.found=[];super().__init__();self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ('p','div','section')and 'post-source'in a.get('class','').split():self.depth=1
  elif self.depth and t in ('p','div','section'):self.depth+=1
  if self.depth and t=='a':
   id=sourceid(a.get('href',''))
   if id:self.found.append(id)
 def handle_endtag(self,t):
  if self.depth and t in ('p','div','section'):self.depth-=1

def index_sources():
 for p in ROOT.glob('posts/*/index.html'):
  h=p.read_text();ids=set(SourceLinks(h).found)
  for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',h,re.S):
   try:obj=json.loads(m[1]);items=obj if isinstance(obj,list) else [obj]
   except (ValueError,TypeError):continue
   for item in items:
    if not isinstance(item,dict)or item.get('@type') not in ('BlogPosting','Article'):continue
    u=item.get('isBasedOn','');u=u.get('url','') if isinstance(u,dict) else u
    id=sourceid(u) if isinstance(u,str) else None
    if id:ids.add(id)
  for id in ids:SOURCE_PATHS.setdefault(id,[]).append(p)

class Page(HTMLParser):
 def __init__(self,s):self.images=[];self.videos=[];self.links=[];super().__init__();self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='img':self.images.append(a.get('src',''))
  if t in ('video','source')and a.get('src'):self.videos.append(a['src'])
  if t=='a':self.links.append(a.get('href',''))
def audit(r):
 p=ROOT/'posts'/('linkedin-'+r['id'])/'index.html'
 if not p.exists():
  paths=SOURCE_PATHS.get(sourceid(r.get('source')) or r['id'],[])
  if len(paths)!=1:return {'id':r['id'],'state':'unmapped-or-ambiguous-page','complete':False}
  p=paths[0]
 s=p.read_text();page=Page(s);d=p.parent
 bound=SOURCE_PATHS.get(sourceid(r.get('source'))or r['id'],[])
 if len(bound)!=1 or bound[0]!=p:return {'id':r['id'],'state':'unmapped-or-ambiguous-source-binding','complete':False}
 def local_path(u):
  if not u or urllib.parse.urlsplit(u).scheme or u.startswith('//'):return None
  path=(ROOT/u.lstrip('/')if u.startswith('/')else d/u).resolve()
  return path if path.is_relative_to(ROOT.resolve())else None
 def asset(u):
  m=re.search(r'/dms/(?:image|document)/(?:pl/|media/)?v2/([^/]+)/',u or'')
  return m[1]if m else None
 proof_path=ROOT/'archive-media-manifest.json'
 proofs=json.loads(proof_path.read_text()).get('assets',[])if proof_path.exists()else[]
 errors=[];verified={'image':set(),'video':set(),'document':set()}
 for v in proofs:
  if v.get('record_id')!=r['id']:continue
  if v.get('post_source')!=r.get('source'):errors.append('proof-wrong-post-source');continue
  kind=v.get('kind');refs=page.images if kind=='image'else page.videos if kind=='video'else page.links if kind=='document'else[]
  f=(ROOT/v.get('local_path','')).resolve()
  if not f.is_relative_to(d.resolve())or not f.is_file():errors.append('proof-wrong-local-path');continue
  if not any(local_path(u)==f for u in refs):errors.append('proof-not-rendered');continue
  data=f.read_bytes()
  if hashlib.sha256(data).hexdigest()!=v.get('sha256'):errors.append('proof-digest-mismatch');continue
  decoded=v.get('decoded',{});fmt=decoded.get('format');signature=False
  if kind=='image':
   signature=(fmt=='JPEG'and data.startswith(b'\xff\xd8\xff'))or(fmt=='PNG'and data.startswith(b'\x89PNG\r\n\x1a\n'))or(fmt=='GIF'and data.startswith((b'GIF87a',b'GIF89a')) )or(fmt=='WEBP'and data[:4]==b'RIFF'and data[8:12]==b'WEBP')
   signature=signature and decoded.get('width',0)>0 and decoded.get('height',0)>0
  elif kind=='video':signature=f.suffix.lower()=='.mp4'and data[4:8]==b'ftyp'and decoded.get('duration',0)>0 and decoded.get('played_frames',0)>0
  elif kind=='document':signature=f.suffix.lower()=='.pdf'and data.startswith(b'%PDF-')and decoded.get('pages',0)>0
  if not signature:errors.append('proof-type-or-decode-invalid');continue
  original_id=asset(v.get('source_media'))
  if kind=='video':
   match=re.search(r'/vid/v2/([^/]+)/',v.get('source_media',''));original_id=match[1]if match else None
  if not original_id or original_id!=v.get('source_asset_id'):errors.append('proof-source-asset-invalid');continue
  verified[kind].add(original_id)
 expected=set(asset(u)or u for u in r.get('images','').splitlines()if u.startswith('https:'))
 missing=expected-verified['image']
 if missing:errors.append('unverified-original-images')
 if r.get('video_url'):
  # video asset identifier must match the exact original source, not any local video
  original=re.search(r'/vid/v2/([^/]+)/',r['video_url'])
  if not original or original[1]not in verified['video']:errors.append('unverified-original-video')
 if r.get('document_url')and asset(r['document_url'])not in verified['document']:errors.append('unverified-original-document')
 count=len(verified['image'])
 if r.get('media_available_on_source'):errors.append('unresolved-source-media')
 if 'התמונות והסרטונים זמינים בפוסט המקורי.'in s or'View the original images and videos on LinkedIn.'in s:errors.append('public-filler')
 return {'id':r['id'],'expected_images':len(expected),'rendered_local_images':count,'errors':errors,'path':str(p.relative_to(ROOT)),'complete':not errors}
def main():
 p=argparse.ArgumentParser();p.add_argument('--require',nargs='+',default=[]);p.add_argument('--json',action='store_true');args=p.parse_args();records=json.loads((ROOT/'archive-source.json').read_text());index_sources();rows=[audit(r)for r in records];selected=[r for r in rows if r['id']in args.require];missing=set(args.require)-{r['id']for r in selected}
 if args.json:print(json.dumps({'records':len(rows),'media_audit':rows},ensure_ascii=False,indent=2))
 else:print('Media audit:',len(rows),'records;',sum(r['complete']for r in rows),'pass asset checks;',sum(not r['complete']for r in rows),'need verification or assets.')
 if args.require:
  for r in selected:
   if not r['complete']:print('INCOMPLETE',r,file=sys.stderr)
  if missing:print('UNKNOWN SOURCE IDS',sorted(missing),file=sys.stderr)
  return int(bool(missing)or any(not r['complete']for r in selected))
 return 0
if __name__=='__main__':sys.exit(main())
