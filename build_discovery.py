from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parent;base='https://ofershap.github.io';E=html.escape
repos=json.loads((root/'project-links.json').read_text())
# Only exact project-name mentions get contextual links. Generic topic resemblance is not proof.
chosen=['pr-rulebook','real-browser-mcp','cursor-usage-tracker','agents-control-tower','cursor-office','gitshow','readme-builder','ai-context-kit','cursor-plan-preview','mcp-server-anydoc']
count=links=0
for f in [*root.glob('posts/*/index.html'),*root.glob('essays/*/index.html')]:
 s=f.read_text();s=re.sub(r'<section class="related-projects">.*?</section>','',s,flags=re.S);s=re.sub(r'<aside class="author-card".*?</aside>','',s,flags=re.S);he=bool(re.search(r'<html[^>]*lang="he"',s));a=re.search(r'<article[^>]*>(.*?)</article>',s,re.S)
 if not a:a=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)
 if not a:raise ValueError(str(f))
 text=html.unescape(re.sub('<[^>]+>',' ',a[1]));related=[]
 for name in chosen:
  if name in repos and re.search(r'(?<![\w-])'+re.escape(name)+r'(?![\w-])',text,re.I):related.append(repos[name]);links+=1
 related_html=''
 if related:related_html='<section class="related-projects"><h2>'+('פרויקטים שהוזכרו בפוסט' if he else 'Projects mentioned in this post')+'</h2><ul>'+''.join('<li><a href="'+E(r['html_url'],quote=True)+'">'+E(r['full_name'].split('/')[-1])+'</a></li>' for r in related)+'</ul></section>'
 bio=('אני עופר שפירא, מוביל צוות AI Engineering ובונה כלי קוד פתוח: כלי פיתוח, שרתי MCP, ספריות TypeScript ו-GitHub Actions. כאן אני כותב על AI, פיתוח וניהול צוותי הנדסה.' if he else 'I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.')
 footer='<aside class="author-card" aria-label="'+('על הכותב' if he else 'About the author')+'"><h2>'+('על עופר שפירא' if he else 'About Ofer Shapira')+'</h2><p>'+bio+'</p><p><a href="https://github.com/ofershap">'+('לפרויקטים שלי ב-GitHub' if he else 'Explore my projects on GitHub')+'</a> · <a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a> · <a href="/for-ai/">'+('על הבלוג' if he else 'About this blog')+'</a></p></aside>'
 closing='</article>' if '</article>' in s else '</main>';s=s.replace(closing,related_html+footer+closing,1);f.write_text(s);count+=1
 md=f.with_suffix('.md')
 if md.exists():
  v=md.read_text();v=re.split(r'\n\n## (?:על עופר שפירא|About Ofer Shapira)\n',v)[0];v+='\n\n## '+('על עופר שפירא' if he else 'About Ofer Shapira')+'\n\n'+bio+'\n\n[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)\n';md.write_text(v)
css=root/'style.css';css.write_text(css.read_text().split('\n.author-card,.related-projects')[0]+'\n.author-card,.related-projects{margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--border,#ddd)}.author-card h2,.related-projects h2{font-size:1.2rem}.author-card p{font-size:.95rem;line-height:1.7}\n')
(root/'for-ai').mkdir(exist_ok=True)
body='''<h1>Ofer Shapira: AI engineering and open-source tools</h1><p>Ofer Shapira (עופר שפירא) is an AI Engineering Team Lead and open-source builder based in Israel. He builds focused developer tools, MCP servers, TypeScript libraries, React tools and GitHub Actions.</p><h2>What is in this blog</h2><p>This is Ofer's personal writing archive: first-hand posts on AI agents, software architecture, coding tools and leading engineering teams. It includes original Hebrew and English LinkedIn posts, selected existing English translations, and longer essays.</p><p>Original-language posts keep their original text and link to their LinkedIn source. Dates refer to the original publication, not the date they were added here. Some older media is only available at the original source. This archive is not a promise that every example or product claim remains current.</p><h2>Identity and projects</h2><ul><li><a href="https://github.com/ofershap">Ofer's GitHub profile and open-source projects</a></li><li><a href="https://www.linkedin.com/in/ofershap/">Ofer's LinkedIn profile</a></li></ul><h2>Reading and citation</h2><p>Use each article's canonical URL and original publication date when citing it. Markdown versions are available as index.md next to each article. Do not treat historic posts as current documentation for the products they discuss.</p><ul><li><a href="/">Search all writing</a></li><li><a href="/llms.txt">Site index</a></li><li><a href="/llms-full.txt">Full text archive</a></li><li><a href="/sitemap.xml">Sitemap</a></li><li><a href="/feed.xml">RSS</a></li></ul>'''
schema={'@context':'https://schema.org','@type':'ProfilePage','url':base+'/for-ai/','mainEntity':{'@type':'Person','name':'Ofer Shapira','alternateName':'עופר שפירא','url':base+'/','sameAs':['https://github.com/ofershap','https://www.linkedin.com/in/ofershap/'],'jobTitle':'AI Engineering Team Lead'}}
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>About Ofer Shapira and this blog</title><meta name="description" content="Ofer Shapira: AI engineering team lead, open-source builder and author of first-hand writing on AI agents and engineering leadership."><link rel="canonical" href="'+base+'/for-ai/"><link rel="stylesheet" href="/style.css"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head><body><header><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a><a href="https://github.com/ofershap">GitHub</a></nav></header><main><article>'+body+'</article><footer><a href="/">All writing</a></footer></main></body></html>'
(root/'for-ai/index.html').write_text(page)
p=root/'llms.txt';s=p.read_text();s=re.sub(r'## About and full text.*?## Recent original-language posts','## Recent original-language posts',s,flags=re.S);s=s.replace('## Recent original-language posts','## About and full text\n\n- [About Ofer and this blog]('+base+'/for-ai/)\n- [Full text archive]('+base+'/llms-full.txt)\n\n## Recent original-language posts');p.write_text(s)
full=['# Ofer Shapira: writing archive\n\nOriginal source and publication date are listed per article. Historical posts are not current product documentation.\n']
for md in sorted([*root.glob('posts/*/index.md'),*root.glob('essays/*/index.md')]):
 full.append('\n\n---\n\nCanonical URL: '+base+'/'+str(md.parent.relative_to(root))+'/\n\n'+md.read_text())
(root/'llms-full.txt').write_text(''.join(full))
p=root/'sitemap.xml';s=p.read_text();s=s.replace('<url><loc>'+base+'/for-ai/</loc></url>','').replace('</urlset>','<url><loc>'+base+'/for-ai/</loc></url></urlset>');p.write_text(s)
p=root/'index.html';s=p.read_text().replace(' · <a href="/for-ai/">About</a>','').replace('<a href="/feed.xml">RSS</a>','<a href="/feed.xml">RSS</a> · <a href="/for-ai/">About</a>');p.write_text(s)
print('Author cards:',count,'Exact-name project links:',links,'Full archive bytes:',(root/'llms-full.txt').stat().st_size)
