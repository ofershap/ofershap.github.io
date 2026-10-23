#!/usr/bin/env python3
"""Build English versions of authored Q&A guides from authored-en.json (en master)
+ authored-source.json (shared facts). Runs AFTER build_authored and build_translations.
Decisions (DDD 23.10): same slug under /en/posts/; en only (approved scope);
hreflang he<->en + x-default->he on both pages, injected idempotently; sitemap and
/en/ index and llms.txt updated additively; homepage stays Hebrew."""
from pathlib import Path
import json,html,re,markdown
from datetime import date as _date_cls
ROOT=Path(__file__).resolve().parent;BASE='https://ofershap.github.io';E=html.escape

def build():
 en=json.loads((ROOT/'authored-en.json').read_text())
 he={r['slug']:r for r in json.loads((ROOT/'authored-source.json').read_text())}
 today=_date_cls.today().isoformat();urls=[]
 for slug,g in en.items():
  r=he[slug];url=BASE+'/en/posts/'+slug+'/';heurl=BASE+'/posts/'+slug+'/'
  title=g['title'];summary=g['summary'];body=g['body']
  alttags='<link rel="alternate" hreflang="he" href="'+heurl+'"><link rel="alternate" hreflang="en" href="'+url+'"><link rel="alternate" hreflang="x-default" href="'+heurl+'">'
  nav='<nav class="language-links" aria-label="Languages" dir="ltr"><a href="'+heurl+'">Original (עברית)</a> · <a href="'+url+'" lang="en" hreflang="en">English</a></nav>'
  # inject into the Hebrew page (idempotent)
  hef=ROOT/'posts'/slug/'index.html';h=hef.read_text()
  h=re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">','',h)
  h=re.sub(r'<nav class="language-links".*?</nav>','',h,flags=re.S)
  h=h.replace('</head>',alttags+'</head>',1);h=h.replace('</h1>','</h1>'+nav,1);hef.write_text(h)
  article={'@context':'https://schema.org','@type':'Article','headline':title,'datePublished':r['published_at'],'dateModified':today,'inLanguage':'en','url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'Ofer Shapira','url':BASE+'/for-ai/','description':g['bio']},'citation':r['sources'],'translationOfWork':{'@type':'CreativeWork','url':heurl}}
  faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in g['faq']]}
  crumb={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Ofer Shapira','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'Guides','item':BASE+'/en/'},{'@type':'ListItem','position':3,'name':title,'item':url}]}
  schemas=json.dumps([article,faq,crumb],ensure_ascii=False).replace('<','\\u003c')
  faqhtml=''.join('<h3>'+E(q)+'</h3><p>'+E(a)+'</p>' for q,a in g['faq'])
  extra='<section class="geo-summary"><h2>'+E(title)+'</h2><p>'+E(summary)+'</p></section>'
  note=g.get('source_note','The workflow and examples here are the author\'s own. Prices, when mentioned, are his service rates, not market data.')
  rel=r['related'];relurl=(BASE+'/en/posts/'+rel+'/') if rel in en else ('/posts/'+rel+'/')
  rellabel=en[rel]['related_label'] if rel in en else g['related_label']+(' (Hebrew)' if rel not in en else '')
  sources='<section class="geo-sources"><h2>Sources and further reading</h2><p>'+E(note)+'</p><ul>'+''.join('<li><a href="'+E(u,quote=True)+'">'+E(l)+'</a></li>' for u,l in zip(r['sources'],g['source_labels']))+'</ul><p><a href="'+relurl+'">'+E(rellabel)+'</a></p></section>'
  footer='<aside class="author-card"><h2>About the author</h2><p>'+E(g['bio'])+'</p><p dir="ltr"><a href="https://github.com/ofershap">GitHub projects</a> · <a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a> · <a href="/for-ai/">About</a></p></aside>'
  render=body
  if r.get('single_summary'):render=re.sub(r'^\s*\*\*Short answer:\*\* .*?\n\n','',body,count=1,flags=re.S)
  rendered=markdown.markdown(render)
  rendered=re.sub(r'https://[^\s<]+',lambda m:'<a href="'+m[0].rstrip('.,')+'">'+m[0].rstrip('.,')+'</a>'+m[0][len(m[0].rstrip('.,')):],rendered)
  page='<!doctype html><html lang="en" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(title)+' | Ofer Shapira</title><meta name="description" content="'+E(summary[:160],quote=True)+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="'+url+'index.md">'+alttags+'<meta property="og:type" content="article"><meta property="og:title" content="'+E(title,quote=True)+'"><meta property="og:description" content="'+E(summary[:160],quote=True)+'"><meta property="og:url" content="'+url+'"><meta name="twitter:card" content="summary"><script src="/webmcp.js" defer></script><script type="application/ld+json">'+schemas+'</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/en/">English</a><a href="/">Writing</a></nav></header><main><article data-authored="qa" itemscope itemtype="https://schema.org/BlogPosting"><meta itemprop="author" content="Ofer Shapira"><h1 itemprop="headline">'+E(title)+'</h1>'+nav+'<p class="byline"><time itemprop="datePublished" datetime="'+r['published_at']+'">'+r['published_at'][:10]+'</time> · Q&amp;A guide · Updated: <time itemprop="dateModified" datetime="'+today+'">'+today+'</time></p>'+'<section class="personal-hook"><p>'+E(g.get('hook',''))+'</p></section>'+extra+'<section class="original-body" itemprop="articleBody">'+rendered+'</section>'+sources+'<section class="geo-faq"><h2>Frequently asked questions</h2>'+faqhtml+'</section>'+footer+'</article><footer><a href="/en/">All English posts</a></footer></main></body></html>'
  p=ROOT/'en'/'posts'/slug;p.mkdir(parents=True,exist_ok=True)
  (p/'index.html').write_text(page)
  (p/'original.md').write_text('Title: '+title+'\n\n'+body)
  md_body=re.sub(r'^\s*\*\*Short answer:\*\* .*?\n\n','',body,count=1,flags=re.S)
  md='---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\npublished: '+r['published_at']+'\nupdated: '+today+'\nlang: en\ncanonical: '+url+'\noriginal: '+heurl+'\n---\n\n# '+title+'\n\n'+summary+'\n\n## In depth\n\n'+md_body+'\n\n'+('## From my experience\n\n'+g.get('hook','')+'\n\n' if g.get('hook') else '')+'## Frequently asked questions\n\n'+''.join('### '+q+'\n\n'+a+'\n\n' for q,a in g['faq'])+'## About the author\n\n'+g['bio']+'\n\nLast updated: '+today+'\n'
  (p/'index.md').write_text(md);urls.append((slug,title,url,heurl))
 # sitemap: strip old entries for these en authored urls, add current
 sm=ROOT/'sitemap.xml';s=sm.read_text()
 for slug,t,u,hu in urls:s=re.sub(r'<url><loc>'+re.escape(u)+r'</loc></url>','',s)
 s=s.replace('</urlset>',''.join('<url><loc>'+u+'</loc></url>'for slug,t,u,hu in urls)+'</urlset>');sm.write_text(s)
 # /en/ index: idempotent guides section
 ei=ROOT/'en'/'index.html'
 if ei.exists():
  s=ei.read_text();s=re.sub(r'<section class="en-guides".*?</section>','',s,flags=re.S)
  sec='<section class="en-guides"><h2>Guides (English)</h2><ul class="post-list">'+''.join('<li><a href="/en/posts/'+slug+'/">'+E(t)+'</a></li>'for slug,t,u,hu in urls)+'</ul></section>'
  s=s.replace('</main>',sec+'</main>',1);ei.write_text(s)
 # llms.txt: idempotent English guides section
 lp=ROOT/'llms.txt';lt=lp.read_text()
 lt=re.sub(r'\n## English guides\n.*?(?=\n## |\Z)','',lt,flags=re.S)
 lt+='\n## English guides\n\n'+''.join('- ['+t+']('+u+')\n  - Markdown: '+u+'index.md\n  - Original (Hebrew): '+hu+'\n'for slug,t,u,hu in urls)
 lp.write_text(lt)
 print('Built',len(urls),'English authored guides')
 import build_lastmod as _lm;_lm.run()
if __name__=='__main__':build()
