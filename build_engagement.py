#!/usr/bin/env python3
"""Idempotently add engagement controls without changing the article body."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parent

def build():
 aliases={}
 for lang in ['en','ar','es','zh-Hans']:
  for id,d in json.loads((ROOT/'translations'/f'{lang}.json').read_text())['posts'].items():aliases[f'/{lang}/posts/linkedin-{id}/']='/'+d['path'].strip('/')+'/'
 pages=list(ROOT.glob('posts/*/index.html'))+list(ROOT.glob('essays/*/index.html'))
 for lang in ['en','ar','es','zh-Hans']:pages+=list(ROOT.glob(lang+'/posts/*/index.html'))
 labels={
 'en':('Like','Share','Copy link','Views are counted from October 7, 2026. No advertising cookies. Likes use an anonymous browser identifier.','Privacy'),
 'he':('אהבתי','שיתוף','העתק קישור','הצפיות נספרות מ-7 באוקטובר 2026. בלי עוגיות פרסום. לייקים משתמשים במזהה דפדפן אנונימי.','פרטיות'),
 'ar':('أعجبني','مشاركة','نسخ الرابط','يبدأ عدّ المشاهدات في 7 أكتوبر 2026. لا توجد ملفات تعريف ارتباط إعلانية. يستخدم الإعجاب معرّف متصفح مجهولاً.','الخصوصية'),
 'es':('Me gusta','Compartir','Copiar enlace','Las visitas se cuentan desde el 7 de octubre de 2026. Sin cookies publicitarias. Los me gusta usan un identificador anónimo del navegador.','Privacidad'),
 'zh-Hans':('点赞','分享','复制链接','浏览量从2026年10月7日开始统计。不使用广告Cookie。点赞使用匿名浏览器标识。','隐私')}
 keys=[]
 for p in pages:
  s=p.read_text();s=re.sub(r'<!-- engagement:start -->.*?<!-- engagement:end -->','',s,flags=re.S);s=s.replace('<script defer src="/engagement.js"></script>','')
  lang=re.search(r'<html[^>]*lang="([^"]+)"',s)[1];l=labels.get(lang,labels['en']);path='/'+str(p.parent.relative_to(ROOT))+'/';key=aliases.get(path,path)
  if path not in aliases:keys.append(key)
  box='<!-- engagement:start --><section class="engagement" data-key="'+html.escape(key,quote=True)+'" data-lang="'+lang+'" aria-label="'+l[1]+'"><div class="engagement-actions"><button class="engagement-like" type="button" aria-pressed="false" disabled><span aria-hidden="true">♡</span> <span class="like-label">'+l[0]+'</span> <span class="like-count">-</span></button><button class="engagement-share" type="button">'+l[1]+' ↗</button><button class="engagement-copy" type="button">'+l[2]+'</button><a class="engagement-network" data-network="linkedin" href="#" rel="noopener noreferrer" target="_blank">LinkedIn</a><a class="engagement-network" data-network="x" href="#" rel="noopener noreferrer" target="_blank">X</a></div><p class="engagement-status" aria-live="polite"></p><p class="engagement-privacy"><a href="/privacy/">'+l[4]+'</a></p></section><!-- engagement:end -->'
  # Near the end of the article, before the footer/author card, not inside prose.
  marker='<aside class="author-card"'
  if marker in s:s=s.replace(marker,box+marker,1)
  elif '</article>' in s:s=s.replace('</article>',box+'</article>',1)
  else:s=s.replace('<footer',box+'<footer',1)
  s=s.replace('</body>','<script defer src="/engagement.js"></script></body>',1);p.write_text(s)
 # Backend allowlist is derived from actual public originals.
 worker=ROOT/'engagement-backend/worker.js';w=worker.read_text();w=re.sub(r'const allowed = new Set\(.*?\);','const allowed = new Set('+json.dumps(sorted(set(keys)))+');',w,count=1);worker.write_text(w)
 print('Engagement added to',len(pages),'article pages')
if __name__=='__main__':build()
