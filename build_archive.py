#!/usr/bin/env python3
"""Build the static archive from approved, already-published personal posts.
Never import queued drafts or posts by other authors. Existing translations keep their URLs.
"""
from pathlib import Path
import json,re,html,datetime,xml.etree.ElementTree as ET,urllib.parse
ROOT=Path(__file__).resolve().parent;BASE='https://ofershap.github.io'
E=html.escape

def linkify(text):
 out=[];pos=0
 for m in re.finditer(r'https?://[^\s<>]+',text):
  out.append(E(text[pos:m.start()]));url=m[0];out.append('<a href="'+E(url,quote=True)+'" rel="noopener noreferrer">'+E(url)+'</a>');pos=m.end()
 out.append(E(text[pos:]));return ''.join(out)

def build():
 records=json.loads((ROOT/'archive-source.json').read_text());seen={};created=0
 for r in records:
  if not re.fullmatch(r'\d{19}',r['id']):raise ValueError('Invalid source ID')
  if r['id'] in seen:raise ValueError('Duplicate source ID')
  seen[r['id']]=r
  if r.get('existing') or not r['text'].strip():continue
  text=r['text'];title=text.strip().splitlines()[0][:130];he=bool(re.search('[\u0590-\u05ff]',text));lang='he' if he else 'en';direction='rtl' if he else 'ltr'
  path=ROOT/'posts'/('linkedin-'+r['id']);path.mkdir(exist_ok=True);url=BASE+'/posts/'+path.name+'/'
  d=r['published_at'][:10];desc=' '.join(text.split())[:160];body='\n'.join('<p>'+linkify(p).replace('\n','<br>')+'</p>' for p in re.split(r'\n\s*\n',text) if p.strip())
  media=[u for u in r.get('images','').splitlines() if u.startswith('https://')];assets=''
  local_media=sorted(path.glob('image-*.jpg'))
  if local_media:
   assets=''.join('<figure><img src="'+f.name+'" alt="'+E(('מדיה מהפוסט המקורי: ' if he else 'Original post media: ')+title,quote=True)+'" loading="lazy"></figure>' for f in local_media)
  if media and len(local_media)<len(media):
   assets+='<section class="source-media"><h2>'+('מדיה מהפוסט המקורי' if he else 'Original post media')+'</h2><p>'+('התמונות והסרטונים זמינים בפוסט המקורי בלינקדאין.' if he else 'View the original images and videos on LinkedIn.')+'</p></section>'
  schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':desc,'datePublished':r['published_at'],'inLanguage':lang,'url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'Ofer Shapira','url':BASE+'/'},'isBasedOn':r['source']}
  if local_media:schema['image']=[url+f.name for f in local_media]
  schema_text=json.dumps(schema,ensure_ascii=False).replace('<',chr(92)+'u003c')
  page=f'''<!doctype html>
<html lang="{lang}" dir="{direction}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} | Ofer Shapira</title><meta name="description" content="{E(desc,quote=True)}"><link rel="canonical" href="{url}"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/rss+xml" href="/feed.xml"><link rel="alternate" type="text/markdown" href="{url}index.md"><meta property="og:type" content="article"><meta property="og:title" content="{E(title,quote=True)}"><meta property="og:description" content="{E(desc,quote=True)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><script type="application/ld+json">{schema_text}</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a><a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a></nav></header><main><article><h1>{E(title)}</h1><p class="byline" dir="ltr"><time datetime="{E(r['published_at'])}">{d}</time></p><p class="post-source">{'פורסם במקור ב' if he else 'Originally published on'} <a href="{E(r['source'],quote=True)}">LinkedIn</a></p>{body}{assets}</article><footer dir="ltr"><a href="/">All writing</a> · <a href="/feed.xml">RSS</a><p class="copyright">© Ofer Shapira</p></footer></main></body></html>'''
  (path/'index.html').write_text(page);(path/'index.md').write_text('# '+title+'\n\n'+text+'\n\nOriginal source: '+r['source']+'\nPublished: '+r['published_at']+'\n');created+=1
 # Append missing records to the homepage, sorted together with preserved existing entries.
 home=ROOT/'index.html';s=home.read_text();match=re.search(r'<ul class="post-list">(.*?)</ul>',s,re.S);items=[]
 for m in re.finditer(r'<li>(.*?)</li>',match[1],re.S):
  item=m[0];href=re.search(r'href="([^"]+)"',item)
  if not href:continue
  f=ROOT/href[1].strip('/')/'index.html'
  if not f.exists():continue
  content=f.read_text();dm=re.search(r'"datePublished"\s*:\s*"([^"]+)"',content);date=dm[1][:10] if dm else '0000-00-00';items.append((date,item,href[1]))
 have={x[2] for x in items}
 for r in records:
  if r.get('existing') or not r['text'].strip():continue
  url='/posts/linkedin-'+r['id']+'/'
  if url in have:continue
  title=r['text'].strip().splitlines()[0][:130];desc=' '.join(r['text'].split())[:160];d=r['published_at'][:10];he=bool(re.search('[\u0590-\u05ff]',r['text']));direction='rtl' if he else 'ltr'
  items.append((d,f'<li dir="{direction}"><a class="post-title" href="{url}">{E(title)}</a><div class="post-meta">{d} · '+('עברית' if he else 'English')+f'</div><p class="post-excerpt">{E(desc)}</p></li>',url))
 items.sort(key=lambda x:x[0],reverse=True);parts=[];year=None
 for d,item,u in items:
  if d[:4]!=year:year=d[:4];parts.append('<li class="year-group"><h2 class="year">'+year+'</h2></li>')
  parts.append(item)
 s=s[:match.start(1)]+'\n'.join(parts)+s[match.end(1):];home.write_text(s)
 # Include every real HTML content page, without fabricated last-modification times.
 pages=[f for f in ROOT.glob('posts/*/index.html')]+[f for f in ROOT.glob('essays/*/index.html')];urls=[BASE+'/']+[BASE+'/'+str(f.parent.relative_to(ROOT))+'/' for f in pages]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+E(u)+'</loc></url>' for u in urls)+'</urlset>\n';(ROOT/'sitemap.xml').write_text(sitemap)
 # RSS only newest50 published articles; no private performance metadata.
 from email.utils import format_datetime
 rss=['<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Ofer Shapira</title><link>'+BASE+'/</link><description>AI engineering, agents and software leadership.</description>']
 for d,item,u in items[:50]:
  content=(ROOT/u.strip('/')/'index.html').read_text();title=html.unescape(re.search(r'<h1[^>]*>(.*?)</h1>',content,re.S)[1]);dm=re.search(r'"datePublished"\s*:\s*"([^"]+)"',content);dt=datetime.datetime.fromisoformat(dm[1]) if dm else datetime.datetime.fromisoformat(d)
  if dt.tzinfo is None:dt=dt.replace(tzinfo=datetime.timezone.utc)
  rss.append('<item><title>'+E(re.sub('<.*?>','',title))+'</title><link>'+BASE+u+'</link><guid isPermaLink="true">'+BASE+u+'</guid><pubDate>'+format_datetime(dt)+'</pubDate></item>')
 rss.append('</channel></rss>');(ROOT/'feed.xml').write_text('\n'.join(rss))
 print('Generated',created,'original-language pages;',len(pages),'article pages;',len(items),'homepage entries')
if __name__=='__main__':
 build()
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'build_discovery.py')],check=True)
