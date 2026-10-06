#!/usr/bin/env python3
from pathlib import Path
import json,re,html,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent;BASE='https://ofershap.github.io';E=html.escape
NAMES={'en':'English','ar':'العربية','es':'Español','zh-Hans':'简体中文'}
NOTICE={'en':'Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.','ar':'ترجمة آلية للمنشور الأصلي، لم يراجعها مترجم بشري. قد لا تكون المعلومات التاريخية محدثة.','es':'Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.','zh-Hans':'本页为原文的机器翻译，未经人工译者审核。历史信息可能已发生变化。'}
BIO={'en':'Ofer Shapira is an AI Engineering Team Lead and open-source builder. Explore his developer tools, MCP servers and TypeScript libraries.','ar':'عوفر شابيرا قائد فريق هندسة الذكاء الاصطناعي ومطور مشاريع مفتوحة المصدر. اكتشف أدوات التطوير وخوادم MCP ومكتبات TypeScript التي يبنيها.','es':'Ofer Shapira lidera un equipo de ingeniería de IA y crea proyectos de código abierto. Explora sus herramientas de desarrollo, servidores MCP y bibliotecas TypeScript.','zh-Hans':'Ofer Shapira 是 AI 工程团队负责人和开源开发者。欢迎了解他的开发工具、MCP 服务器和 TypeScript 库。'}
def linked(text):
 out=[];pos=0
 for m in re.finditer(r'https?://[^\s<>]+',text):out.extend([E(text[pos:m.start()]),'<a href="'+E(m[0],quote=True)+'" rel="noopener noreferrer">'+E(m[0])+'</a>']);pos=m.end()
 return ''.join(out)+E(text[pos:])
def build():
 data={l:json.loads((ROOT/'translations'/(l+'.json')).read_text())['posts']for l in NAMES};assert all(set(v)==set(data['en']) for v in data.values())
 sources={r['id']:r for r in json.loads((ROOT/'archive-source.json').read_text())};repos=json.loads((ROOT/'project-links.json').read_text());urls=[]
 for id in data['en']:
  r=data['en'][id];original=ROOT/r['path'].strip('/')/'index.html';assert original.exists(),r['path'];orig=original.read_text();origlang=re.search(r'<html[^>]*lang="([^"]+)"',orig)[1];origurl=BASE+'/'+r['path'].strip('/')+'/'
  variants={l:BASE+'/'+l+'/posts/linkedin-'+id+'/' for l in NAMES};alts={**variants,origlang:origurl} if origlang not in variants else {**variants}
  alttags=''.join('<link rel="alternate" hreflang="'+l+'" href="'+u+'">'for l,u in alts.items())+'<link rel="alternate" hreflang="x-default" href="'+origurl+'">'
  nav='<nav class="language-links" aria-label="Languages" dir="ltr"><a href="'+origurl+'">Original</a> · '+ ' · '.join('<a href="'+u+'" lang="'+l+'" hreflang="'+l+'">'+NAMES[l]+'</a>'for l,u in variants.items())+'</nav>'
  orig=re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">','',orig);orig=re.sub(r'<nav class="language-links".*?</nav>','',orig,flags=re.S);orig=orig.replace('</head>',alttags+'</head>',1);orig=orig.replace('</h1>','</h1>'+nav,1);original.write_text(orig)
  media=re.findall(r'<figure>.*?</figure>',orig,re.S);mediahtml=''.join(media)
  mediahtml=re.sub(r'src="(image-[^"]+)"',lambda m:'src="'+origurl+m[1]+'"',mediahtml)
  for lang,posts in data.items():
   p=posts[id];assert p['source_link']==sources[id]['source'] and p['published_at']==sources[id]['published_at'];title=p['title'];short=title[:160];text=p['text'];url=variants[lang];direction='rtl'if lang=='ar'else'ltr'
   body='\n'.join('<p>'+linked(x).replace('\n','<br>')+'</p>'for x in re.split(r'\n\s*\n',text)if x.strip());desc=' '.join(text.split())[:160]
   related=[r for name,r in repos.items()if re.search(r'(?<![\w-])'+re.escape(name)+r'(?![\w-])',sources[id]['text'],re.I)]
   projects='<ul>'+''.join('<li><a href="'+r['html_url']+'"><bdi>'+E(r['full_name'])+'</bdi></a></li>'for r in related)+'</ul>'if related else''
   schema={'@context':'https://schema.org','@type':'BlogPosting','headline':short,'datePublished':p['published_at'],'inLanguage':lang,'url':url,'mainEntityOfPage':url,'author':{'@type':'Person','name':'Ofer Shapira','url':BASE+'/for-ai/'},'isBasedOn':p['source_link'],'translationOfWork':{'@type':'CreativeWork','url':origurl}}
   st=json.dumps(schema,ensure_ascii=False).replace('<',chr(92)+'u003c');path=ROOT/lang/'posts'/('linkedin-'+id);path.mkdir(parents=True,exist_ok=True)
   page='<!doctype html><html lang="'+lang+'" dir="'+direction+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(short)+' | Ofer Shapira</title><meta name="description" content="'+E(desc,quote=True)+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="'+url+'index.md">'+alttags+'<script type="application/ld+json">'+st+'</script></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/'+lang+'/">'+NAMES[lang]+'</a><a href="/">Writing</a></nav></header><main><article><h1>'+E(short)+'</h1>'+nav+'<p class="translation-notice">'+NOTICE[lang]+'</p><p class="byline" dir="ltr"><time datetime="'+p['published_at']+'">'+p['published_at'][:10]+'</time> · <a href="'+E(p['source_link'],quote=True)+'">LinkedIn</a></p>'+body+mediahtml+projects+'<aside class="author-card"><h2>Ofer Shapira</h2><p>'+BIO[lang]+'</p><p dir="ltr"><a href="https://github.com/ofershap">GitHub projects</a> · <a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a> · <a href="/for-ai/">About</a></p></aside></article><footer><a href="/'+lang+'/">'+NAMES[lang]+'</a></footer></main></body></html>'
   (path/'index.html').write_text(page);(path/'index.md').write_text('# '+title+'\n\n'+NOTICE[lang]+'\n\n'+text+'\n\nOriginal: '+origurl+'\nSource: '+p['source_link']+'\nPublished: '+p['published_at']+'\n');urls.append(url)
 for lang,posts in data.items():
  items=''.join('<li><a href="/ '+lang+'/posts/linkedin-'+id+'/">'+E(r['title'][:160])+'</a><p class="post-meta">'+r['published_at'][:10]+'</p></li>'for id,r in posts.items()).replace('href="/ ','href="/')
  (ROOT/lang/'index.html').write_text('<!doctype html><html lang="'+lang+'" dir="'+('rtl'if lang=='ar'else'ltr')+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+NAMES[lang]+' | Ofer Shapira</title><link rel="canonical" href="'+BASE+'/'+lang+'/"><link rel="stylesheet" href="/style.css"></head><body><header><a href="/">Ofer Shapira</a></header><main><h1>'+NAMES[lang]+'</h1><p>'+NOTICE[lang]+'</p><ul class="post-list">'+items+'</ul></main></body></html>');urls.append(BASE+'/'+lang+'/')
 sitemap=ROOT/'sitemap.xml';s=sitemap.read_text();s=re.sub(r'<url><loc>'+BASE+r'/(en|ar|es|zh-Hans)/.*?</url>','',s);s=s.replace('</urlset>',''.join('<url><loc>'+u+'</loc></url>'for u in urls)+'</urlset>');sitemap.write_text(s)
 for filename in ['index.html','llms.txt']:
  p=ROOT/filename;s=p.read_text()
  if filename=='index.html':
   s=re.sub(r'<nav class="archive-languages".*?</nav>','',s,flags=re.S);s=s.replace('<section class="archive-tools"','<nav class="archive-languages" aria-label="Translations">'+' · '.join('<a href="/'+l+'/">'+NAMES[l]+'</a>'for l in NAMES)+'</nav><section class="archive-tools"',1)
  else:
   s=s.split('\n## Machine translation experiment')[0]+'\n## Machine translation experiment\n\n'+''.join('- ['+NAMES[l]+']('+BASE+'/'+l+'/): 100 translated posts. Machine translated; not human-reviewed.\n'for l in NAMES)
  p.write_text(s)
 print('Generated',len(urls)-4,'translations and 4 language indexes')
if __name__=='__main__':build()
