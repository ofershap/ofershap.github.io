#!/usr/bin/env python3
"""Render reviewed original Q&A separately from the LinkedIn archive."""
from pathlib import Path
import json,html,re,markdown,xml.etree.ElementTree as ET
from datetime import date as _date_cls
ROOT=Path(__file__).resolve().parent;BASE='https://ofershap.github.io';E=html.escape

def build():
 source=ROOT/'authored-source.json'
 if not source.exists():return
 rows=json.loads(source.read_text());items=[];today=_date_cls.today().isoformat()
 for r in rows:
  slug=r['slug'];assert re.fullmatch('[a-z0-9-]+',slug)
  p=ROOT/'posts'/slug;p.mkdir(exist_ok=True);url=BASE+'/posts/'+slug+'/'
  raw=r['body'];title=raw.splitlines()[0].split(': ',1)[1];body='\n'.join(raw.splitlines()[1:])
  article={'@context':'https://schema.org','@type':'Article','headline':title,'datePublished':r['published_at'],'dateModified':today,'inLanguage':'he','url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'עופר שפירא','url':BASE+'/for-ai/','description':r['bio']},'citation':r['sources']}
  faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in r['faq']]}
  faqhtml=''.join('<h3>'+E(q)+'</h3><p>'+E(a)+'</p>' for q,a in r['faq'])
  summary=raw.split('**תשובה קצרה:** ',1)[1].split('\n',1)[0]
  extra='<section class="geo-summary"><h2>'+E(title)+'</h2><p>'+E(summary)+'</p>'+(('<p>'+E(r['note'])+'</p>') if r.get('note') else '')+'</section>'
  sources='<section class="geo-sources"><h2>מקורות ופרטים נוספים</h2><p>התהליך מתואר מניסיונו של הכותב. המחירים, כשמופיעים, הם מחירי השירות שלו ולא נתוני שוק.</p><ul>'+''.join('<li><a href="'+E(u,quote=True)+'">'+E(label)+'</a></li>' for u,label in zip(r['sources'],r['source_labels']))+'</ul><p><a href="/posts/'+r['related']+'/">'+E(r['related_label'])+'</a></p></section>'
  footer='<aside class="author-card"><h2>על הכותב</h2><p>'+E(r['bio'])+'</p><p><a href="https://dibbur.pages.dev">דיבור - הקלדה קולית בעברית למק</a> · <a href="https://israeli-ai-agency.pages.dev/services/">שירותי הסוכנות</a> · <a href="/for-ai/">על הבלוג</a></p></aside>'
  breadcrumb={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'עופר שפירא','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'מדריכים','item':BASE+'/'} ,{'@type':'ListItem','position':3,'name':title,'item':url}]}
  schemas=json.dumps([article,faq,breadcrumb],ensure_ascii=False).replace('<','\u003c')
  page='<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(title)+' | עופר שפירא</title><meta name="description" content="'+E(summary[:160],quote=True)+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="'+url+'index.md"><meta property="og:type" content="article"><meta property="og:title" content="'+E(title)+'"><meta property="og:description" content="'+E(summary[:160],quote=True)+'"><meta property="og:url" content="'+url+'"><meta name="twitter:card" content="summary"><script src="/webmcp.js" defer></script><script type="application/ld+json">'+schemas+'</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a></nav></header><main><article data-authored="qa" itemscope itemtype="https://schema.org/BlogPosting"><meta itemprop="author" content="Ofer Shapira"><h1 itemprop="headline">'+E(title)+'</h1><p class="byline"><time itemprop="datePublished" datetime="'+r['published_at']+'">'+r['published_at'][:10]+'</time> · מדריך שאלה ותשובה · עודכן: <time itemprop="dateModified" datetime="'+today+'">'+today+'</time></p>'+'<section class="personal-hook"><p>'+E(r.get('hook',''))+'</p></section>'+extra+'<section class="original-body" itemprop="articleBody">'+markdown.markdown(body)+'</section>'+sources+'<section class="geo-faq"><h2>שאלות נפוצות</h2>'+faqhtml+'</section>'+footer+'</article><footer><a href="/">כל הפוסטים</a></footer></main></body></html>'
  if r.get('single_summary'):
   clean_body=re.sub(r'^\s*\*\*תשובה קצרה:\*\* .*?\n\n', '', body, count=1, flags=re.S)
   page=page.replace(markdown.markdown(body),markdown.markdown(clean_body))
   page=page.replace('התהליך מתואר מניסיונו של הכותב. המחירים, כשמופיעים, הם מחירי השירות שלו ולא נתוני שוק.',E(r['source_note']))
  rendered=markdown.markdown(body)
  rendered=re.sub(r'https://[^\s<]+',lambda m:'<a href="'+m[0].rstrip('.,')+'">'+m[0].rstrip('.,')+'</a>'+m[0][len(m[0].rstrip('.,')):],rendered)
  page=page.replace(markdown.markdown(body),rendered)
  # Keep parity with the full chain: beacon first (same position build_beacon uses), then hreflang + language nav before </head> when an English version exists - so rebuilding build_authored alone is idempotent (test_authored).
  import build_beacon as _bb
  page=_bb.inject(page)
  if (ROOT/'authored-en.json').exists() and r['slug'] in json.loads((ROOT/'authored-en.json').read_text()):
   enurl=BASE+'/en/posts/'+r['slug']+'/'
   page=page.replace('</head>','<link rel="alternate" hreflang="he" href="'+url+'"><link rel="alternate" hreflang="en" href="'+enurl+'"><link rel="alternate" hreflang="x-default" href="'+url+'"></head>',1)
   page=page.replace('</h1>','</h1>'+'<nav class="language-links" aria-label="Languages" dir="ltr"><a href="'+url+'">Original (עברית)</a> · <a href="'+enurl+'" lang="en" hreflang="en">English</a></nav>',1)
  (p/'index.html').write_text(page);(p/'original.md').write_text(raw)
  md_body=re.sub(r'^\s*\*\*תשובה קצרה:\*\* .*?\n\n','',body,count=1,flags=re.S)
  md='---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\npublished: '+r['published_at']+'\nupdated: '+today+'\nlang: he\ncanonical: '+url+'\n---\n\n# '+title+'\n\n'+summary+'\n\n'+(r.get('note','')+'\n\n' if r.get('note') else '')+'## הרחבה\n\n'+md_body+'\n\n'+('## מהניסיון שלי\n\n'+r.get('hook','')+'\n\n' if r.get('hook') else '')+'## שאלות נפוצות\n\n'+''.join('### '+q+'\n\n'+a+'\n\n' for q,a in r['faq'])+'## על הכותב\n\n'+r['bio']+'\n\nעודכן לאחרונה: '+today+'\n'
  (p/'index.md').write_text(md)
  href='/posts/'+slug+'/'
  items.append('<li dir="rtl"><a class="post-title" href="'+href+'">'+E(title)+'</a><div class="post-meta">'+r['published_at'][:10]+' · עברית · שאלה ותשובה</div><p class="post-excerpt">'+E(summary)+'</p></li>')
 s=(ROOT/'index.html').read_text()
 for r in rows:s=re.sub(r'<li[^>]*><a class="post-title" href="/posts/'+r['slug']+'/".*?</li>','',s,flags=re.S)
 marker=re.search(r'<li class="year-group">.*?</li>',s,re.S)
 if marker:s=s[:marker.end()]+''.join(items)+s[marker.end():]
 (ROOT/'index.html').write_text(s)
 from homepage_order import sort_homepage
 sort_homepage(ROOT)
 # Add new originals without rewriting existing feed dates or entries.
 feed=ET.fromstring((ROOT/'feed.xml').read_text());ch=feed.find('channel')
 from email.utils import format_datetime
 from datetime import datetime
 for r in reversed(rows):
  url=BASE+'/posts/'+r['slug']+'/'
  for item in list(ch.findall('item')):
   if item.findtext('link')==url:ch.remove(item)
  i=ET.Element('item')
  for tag,val in [('title',r['body'].splitlines()[0].split(': ',1)[1]),('link',url),('guid',url),('pubDate',format_datetime(datetime.fromisoformat(r['published_at'])))]:ET.SubElement(i,tag).text=val
  ch.insert(3,i)
 from email.utils import parsedate_to_datetime
 feed_items=sorted(ch.findall('item'),key=lambda item:parsedate_to_datetime(item.findtext('pubDate')),reverse=True)
 for item in list(ch.findall('item')):ch.remove(item)
 for item in feed_items[:50]:ch.append(item)
 ET.ElementTree(feed).write(ROOT/'feed.xml',encoding='utf-8',xml_declaration=True)
 for r in rows:
  loc=BASE+'/posts/'+r['slug']+'/'
  p=ROOT/'sitemap.xml';s=p.read_text()
  if '<loc>'+loc+'</loc>' not in s:s=s.replace('</urlset>','<url><loc>'+loc+'</loc></url></urlset>');p.write_text(s)
 p=ROOT/'llms.txt';s=p.read_text();head,_,rest=s.partition('\n## Original service Q&A\n');tail='';m=re.search('\n## (?!Original service Q&A)',rest);tail=rest[m.start():] if m else '';s=head+'\n## Original service Q&A\n\n'+''.join('- ['+r['body'].splitlines()[0].split(': ',1)[1]+']('+BASE+'/posts/'+r['slug']+'/)\n' for r in rows);s=s+tail;p.write_text(s)
 print('Authored Q&A:',len(rows))
 import build_lastmod as _lm;_lm.run()
if __name__=='__main__':build()

# Cloudflare Web Analytics beacon - keep site-wide injection idempotent on every rebuild (build_beacon.run is a no-op when present).
import build_beacon as _beacon; _beacon.run()
