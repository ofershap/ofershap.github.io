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
 records=json.loads((ROOT/'archive-source.json').read_text());seen={};created=0;new_pages=[]
 for r in records:
  if not re.fullmatch(r'\d{19}',r['id']):raise ValueError('Invalid source ID')
  if r['id'] in seen:raise ValueError('Duplicate source ID')
  seen[r['id']]=r
  if r.get('existing') or not r['text'].strip():continue
  text=r['text'];title=r.get('title') or text.strip().splitlines()[0][:130];he=bool(re.search('[\u0590-\u05ff]',text));lang='he' if he else 'en';direction='rtl' if he else 'ltr'
  path=ROOT/'posts'/('linkedin-'+r['id']);path.mkdir(exist_ok=True);url=BASE+'/posts/'+path.name+'/'
  d=r['published_at'][:10];desc=' '.join(text.split())[:160];body='\n'.join('<p>'+linkify(p).replace('\n','<br>')+'</p>' for p in re.split(r'\n\s*\n',text) if p.strip())
  media=[u for u in r.get('images','').splitlines() if u.startswith('https://')];assets=''
  local_media=sorted([f for f in path.glob('image-*') if f.suffix.lower() in {'.jpg','.jpeg','.png','.webp','.gif'}])
  if local_media:
   assets=''.join('<figure><img src="'+f.name+'" alt="'+E(('מדיה מהפוסט המקורי: ' if he else 'Original post media: ')+title,quote=True)+'" loading="lazy"></figure>' for f in local_media)
  # Only preserved original source assets are embedded; never remote expiring URLs.
  local_videos=sorted([f for f in path.glob('video-*') if f.suffix.lower() in {'.mp4','.webm','.mov'}])
  for f in local_videos:
   assets+='<video controls preload="metadata" style="max-width:100%"><source src="'+E(f.name,quote=True)+'"></video>'
  for f in sorted(path.glob('document-*.pdf')):
   assets+='<p><a href="'+E(f.name,quote=True)+'">'+('המסמך המקורי מהפוסט' if he else 'Original post document')+'</a></p>'
  # Missing media is a failed completion gate, never replaced by public filler.
  schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':desc,'datePublished':r['published_at'],'inLanguage':lang,'url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'Ofer Shapira','url':BASE+'/'},'isBasedOn':r['source']}
  if local_media:schema['image']=[url+f.name for f in local_media]
  breadcrumb={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Ofer Shapira','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'Writing','item':BASE+'/#archive'},{'@type':'ListItem','position':3,'name':title,'item':url}]}
  schema_text=json.dumps([schema,breadcrumb],ensure_ascii=False).replace('<',chr(92)+'u003c')
  disable_engagement = r.get('engagement') == 'off' or ('data-engagement="off"' in (path/'index.html').read_text() if (path/'index.html').exists() else False)
  page=f'''<!doctype html>
<html lang="{lang}" dir="{direction}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} | Ofer Shapira</title><meta name="description" content="{E(desc,quote=True)}"><link rel="canonical" href="{url}"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/rss+xml" href="/feed.xml"><link rel="alternate" type="text/markdown" href="{url}index.md"><meta property="og:type" content="article"><meta property="og:title" content="{E(title,quote=True)}"><meta property="og:description" content="{E(desc,quote=True)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><script src="/webmcp.js" defer></script><script type="application/ld+json">{schema_text}</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a><a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a></nav></header><main><article itemscope itemtype="https://schema.org/BlogPosting"><meta itemprop="author" content="Ofer Shapira"><h1 itemprop="headline">{E(title)}</h1><p class="byline" dir="ltr"><time itemprop="datePublished" datetime="{E(r['published_at'])}">{d}</time></p><p class="post-source">{'פורסם במקור ב' if he else 'Originally published on'} <a href="{E(r['source'],quote=True)}">LinkedIn</a></p><div itemprop="articleBody">{body}</div>{assets}</article><footer dir="ltr"><a href="/">All writing</a> · <a href="/feed.xml">RSS</a><p class="copyright">© Ofer Shapira</p></footer></main></body></html>'''
  page=page.replace('<html ', '<html data-engagement="off" ',1) if disable_engagement else page
  new_pages.append((title,url,r['source']));(path/'index.html').write_text(page);(path/'index.md').write_text('---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\n'+'published: '+r['published_at']+'\nsource: '+r['source']+'\n'+'lang: '+lang+'\ncanonical: '+url+'\n---\n\n# '+title+'\n\n'+text+'\n\nOriginal source: '+r['source']+'\nPublished: '+r['published_at']+'\n'+''.join('\n![Original post media]('+f.name+')\n' for f in local_media)+''.join('\n[Original post video]('+f.name+')\n' for f in local_videos)+''.join('\n[Original post document]('+f.name+')\n' for f in sorted(path.glob('document-*.pdf'))));created+=1
 # Append missing records to the homepage, sorted together with preserved existing entries.
 home=ROOT/'index.html';s=home.read_text();match=re.search(r'<ul class="post-list">(.*?)</ul>',s,re.S);items=[]
 for m in re.finditer(r'<li\b[^>]*>(.*?)</li>',match[1],re.S):
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
  title=r.get('title') or r['text'].strip().splitlines()[0][:130];desc=' '.join(r['text'].split())[:160];d=r['published_at'][:10];he=bool(re.search('[\u0590-\u05ff]',r['text']));direction='rtl' if he else 'ltr'
  items.append((d,f'<li dir="{direction}"><a class="post-title" href="{url}">{E(title)}</a><div class="post-meta">{d} · '+('עברית' if he else 'English')+f'</div><p class="post-excerpt">{E(desc)}</p></li>',url))
 items.sort(key=lambda x:x[0],reverse=True);parts=[];year=None
 for d,item,u in items:
  if d[:4]!=year:year=d[:4];parts.append('<li class="year-group"><h2 class="year">'+year+'</h2></li>')
  parts.append(item)
 s=s[:match.start(1)]+'\n'.join(parts)+s[match.end(1):];home.write_text(s)
 # Include every real HTML content page, without fabricated last-modification times.
 pages=[f for f in ROOT.glob('posts/*/index.html')]+[f for f in ROOT.glob('essays/*/index.html')]+[f for f in ROOT.glob('docs/index.html')]+[f for f in ROOT.glob('contact/index.html')];urls=[BASE+'/']+[BASE+'/'+str(f.parent.relative_to(ROOT))+'/' for f in pages]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+E(u)+'</loc></url>' for u in urls)+'</urlset>\n';(ROOT/'sitemap.xml').write_text(sitemap)
 import build_lastmod as _lm;_lm.run()
 # RSS only newest50 published articles; no private performance metadata.
 from email.utils import format_datetime
 rss=['<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Ofer Shapira</title><link>'+BASE+'/</link><description>AI engineering, agents and software leadership.</description>']
 for d,item,u in items[:50]:
  content=(ROOT/u.strip('/')/'index.html').read_text();title=html.unescape(re.search(r'<h1[^>]*>(.*?)</h1>',content,re.S)[1]);dm=re.search(r'"datePublished"\s*:\s*"([^"]+)"',content);dt=datetime.datetime.fromisoformat(dm[1]) if dm else datetime.datetime.fromisoformat(d)
  if dt.tzinfo is None:dt=dt.replace(tzinfo=datetime.timezone.utc)
  rss.append('<item><title>'+E(re.sub('<.*?>','',title))+'</title><link>'+BASE+u+'</link><guid isPermaLink="true">'+BASE+u+'</guid><pubDate>'+format_datetime(dt)+'</pubDate></item>')
 rss.append('</channel></rss>');(ROOT/'feed.xml').write_text('\n'.join(rss))

 # Cap the "Recent original-language posts" section of llms.txt (ora.ai wants llms.txt slim, <30K chars); the full list lives in posts/llms.txt.
 # Rebuilt deterministically from post frontmatter, newest first, so the newest posts are always present even after mass rebuilds.
 def trim_recent(keep=20):
  lp=ROOT/'llms.txt';lt=lp.read_text();marker='## Recent original-language posts\n'
  i=lt.find(marker)
  if i<0:return
  j=lt.find('\n## ',i+len(marker))
  rows=[]
  for md in ROOT.glob('posts/*/index.md'):
   parts=md.read_text().split('---')
   if len(parts)<3:continue
   fm=parts[1]
   def field(name):
    m=re.search(r'^'+name+r': (.*)$',fm,re.M);return m[1].strip() if m else ''
   t=field('title');pub=field('published');src=field('source');can=field('canonical')
   if not t or not pub:continue
   t=json.loads(t);can=can or BASE+'/posts/'+md.parent.name+'/';src=src or can
   rows.append((pub,t,can,src))
  rows.sort(reverse=True)
  pointer='- [Full post index](https://ofershap.github.io/posts/llms.txt) - every published post with markdown and original-source links.'
  body='\n'+'\n\n'.join('- ['+t+']('+u+')\n  - Markdown: '+u+'index.md\n  - Original: '+src for pub,t,u,src in rows[:keep])+'\n\n'+pointer+'\n'
  lt=lt[:i+len(marker)]+body+lt[j if j>0 else len(lt):]
  lp.write_text(lt)
 trim_recent(20)
 print('Generated',created,'original-language pages;',len(pages),'article pages;',len(items),'homepage entries')
if __name__=='__main__':
 build()
 from build_authored import build as build_authored
 build_authored()
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'build_discovery.py')],check=True)
 subprocess.run([sys.executable,str(ROOT/'build_post_upgrade.py')],check=True)
 if (ROOT/'translations').exists():subprocess.run([sys.executable,str(ROOT/'build_translations.py')],check=True)
 if (ROOT/'authored-en.json').exists():subprocess.run([sys.executable,str(ROOT/'build_authored_en.py')],check=True)

 subprocess.run([sys.executable,str(ROOT/"build_engagement.py")],check=True)

# Cloudflare Web Analytics beacon - keep site-wide injection idempotent on every rebuild (build_beacon.run is a no-op when present).
import build_beacon as _beacon; _beacon.run()
