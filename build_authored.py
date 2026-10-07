#!/usr/bin/env python3
"""Render reviewed original Q&A separately from the LinkedIn archive."""
from pathlib import Path
import json,html,re,markdown,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent;BASE='https://ofershap.github.io';E=html.escape

def build():
 source=ROOT/'authored-source.json'
 if not source.exists():return
 rows=json.loads(source.read_text());items=[]
 for r in rows:
  slug=r['slug'];assert re.fullmatch('[a-z0-9-]+',slug)
  p=ROOT/'posts'/slug;p.mkdir(exist_ok=True);url=BASE+'/posts/'+slug+'/'
  raw=r['body'];title=raw.splitlines()[0].split(': ',1)[1];body='\n'.join(raw.splitlines()[1:])
  article={'@context':'https://schema.org','@type':'Article','headline':title,'datePublished':r['published_at'],'inLanguage':'he','url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'עופר שפירא','url':BASE+'/for-ai/','description':r['bio']},'citation':r['sources']}
  faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in r['faq']]}
  faqhtml=''.join('<h3>'+E(q)+'</h3><p>'+E(a)+'</p>' for q,a in r['faq'])
  summary=raw.split('**תשובה קצרה:** ',1)[1].split('\n',1)[0]
  extra='<section class="geo-summary"><h2>בקצרה</h2><p>'+E(summary)+'</p>'+(('<p>'+E(r['note'])+'</p>') if r.get('note') else '')+'</section>'
  sources='<section class="geo-sources"><h2>מקורות ופרטים נוספים</h2><p>התהליך מתואר מניסיונו של הכותב. המחירים, כשמופיעים, הם מחירי השירות שלו ולא נתוני שוק.</p><ul>'+''.join('<li><a href="'+E(u,quote=True)+'">'+E(label)+'</a></li>' for u,label in zip(r['sources'],r['source_labels']))+'</ul><p><a href="/posts/'+r['related']+'/">'+E(r['related_label'])+'</a></p></section>'
  footer='<aside class="author-card"><h2>על הכותב</h2><p>'+E(r['bio'])+'</p><p><a href="https://israeli-ai-agency.pages.dev/services/">שירותי הסוכנות</a> · <a href="/for-ai/">על הבלוג</a></p></aside>'
  schemas=json.dumps([article,faq],ensure_ascii=False).replace('<','\\u003c')
  page='<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(title)+' | עופר שפירא</title><meta name="description" content="'+E(summary[:160],quote=True)+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="'+url+'index.md"><script type="application/ld+json">'+schemas+'</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a></nav></header><main><article data-authored="qa"><h1>'+E(title)+'</h1><p class="byline"><time datetime="'+r['published_at']+'">'+r['published_at'][:10]+'</time> · מדריך שאלה ותשובה</p>'+extra+'<section class="original-body">'+markdown.markdown(body)+'</section>'+sources+'<section class="geo-faq"><h2>שאלות נפוצות</h2>'+faqhtml+'</section>'+footer+'</article><footer><a href="/">כל הפוסטים</a></footer></main></body></html>'
  rendered=markdown.markdown(body)
  rendered=re.sub(r'https://[^\s<]+',lambda m:'<a href="'+m[0].rstrip('.,')+'">'+m[0].rstrip('.,')+'</a>'+m[0][len(m[0].rstrip('.,')):],rendered)
  page=page.replace(markdown.markdown(body),rendered)
  (p/'index.html').write_text(page);(p/'original.md').write_text(raw)
  (p/'index.md').write_text(raw+'\n\n## בקצרה\n\n'+summary+'\n\n'+r.get('note','')+'\n\n## שאלות נפוצות\n\n'+''.join('### '+q+'\n\n'+a+'\n\n' for q,a in r['faq'])+'## על הכותב\n\n'+r['bio']+'\n')
  href='/posts/'+slug+'/'
  items.append('<li dir="rtl"><a class="post-title" href="'+href+'">'+E(title)+'</a><div class="post-meta">'+r['published_at'][:10]+' · עברית · שאלה ותשובה</div><p class="post-excerpt">'+E(summary)+'</p></li>')
 s=(ROOT/'index.html').read_text()
 for r in rows:s=re.sub(r'<li[^>]*><a class="post-title" href="/posts/'+r['slug']+'/".*?</li>','',s,flags=re.S)
 marker=re.search(r'<li class="year-group">.*?</li>',s,re.S)
 if marker:s=s[:marker.end()]+''.join(items)+s[marker.end():]
 (ROOT/'index.html').write_text(s)
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
 ET.ElementTree(feed).write(ROOT/'feed.xml',encoding='utf-8',xml_declaration=True)
 for r in rows:
  loc=BASE+'/posts/'+r['slug']+'/'
  p=ROOT/'sitemap.xml';s=p.read_text()
  if '<loc>'+loc+'</loc>' not in s:s=s.replace('</urlset>','<url><loc>'+loc+'</loc></url></urlset>');p.write_text(s)
 p=ROOT/'llms.txt';s=p.read_text();s=re.split('\n## Original service Q&A\n',s)[0];s+='\n## Original service Q&A\n\n'+''.join('- ['+r['body'].splitlines()[0].split(': ',1)[1]+']('+BASE+'/posts/'+r['slug']+'/)\n' for r in rows);p.write_text(s)
 print('Authored Q&A:',len(rows))
if __name__=='__main__':build()
