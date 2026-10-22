#!/usr/bin/env python3
"""Build /community-apps - public Hebrew RTL directory of 73 community-built AI projects.
Source: community thread in the Israeli Claude Facebook group (Oct 2026), names and like
counts intentionally stripped for privacy. Idempotent."""
import json, html
from pathlib import Path

R = Path(__file__).resolve().parent
SITE = 'https://ofershap.github.io'
SLUG = '/community-apps/'
DATA = json.loads(Path('/tmp/apps.json').read_text(encoding='utf-8'))
APPS, NOLINK = DATA['apps'], DATA['nolink']

CAT = {
 'בקלפי':'קהילה ואזרחות','אותיות בדרך':'ילדים ולימוד','יוניקורד':'פנאי ותחביבים',
 'מסע במערכת השמש':'ילדים ולימוד','PashutFree':'משפחה ובריאות','חניונים':'רכב ותחבורה',
 'בא לי בשר':'אוכל ובילוי','Reel Trouble':'משחקים','מפת השפע':'קהילה ואזרחות',
 '120':'משחקים','KolTorah':'ילדים ולימוד','AstroAI':'פנאי ותחביבים','Cla64':'קריירה',
 'KeepBoard':'כלים אישיים','דף צמח':'ילדים ולימוד','DailyGrowers':'פנאי ותחביבים',
 'ספיר יודאיקה':'פנאי ותחביבים','ORCA':'כלים לעסק','בדרך לרישיון':'קריירה',
 'CAT - Come And Talk':'קהילה ואזרחות','StockFlow':'כלים לעסק','Passriva':'כלים אישיים',
 'פרקי אבות עם AI':'ילדים ולימוד','Navega Studio':'משחקים','iListen':'פנאי ותחביבים',
 'Limoo':'ילדים ולימוד','Iseraj (السراج)':'ילדים ולימוד','HexWave':'פנאי ותחביבים',
 'Agent Synth':'פנאי ותחביבים','Dedinka':'ילדים ולימוד','Mark-It':'כלים אישיים',
 'מה יש פה':'אוכל ובילוי','Clubzzy':'כלים לעסק','Algolinks':'כלים לעסק',
 'CabinetOS':'כלים לעסק','SpaceX 2037':'משחקים','בוליט':'קהילה ואזרחות',
 'Skippy':'קריירה','ExitPro':'פיננסים','Baby Match':'משפחה ובריאות',
 'Split':'פיננסים','RiDo':'כלים אישיים','learnbythebook':'ילדים ולימוד',
 'קלכלן':'פיננסים','Formy (פורמי)':'כלים לעסק','ניפגשים.לייב':'כלים לעסק',
 'VibeQA':'כלים לעסק','mikee (מייקי)':'כלים לעסק','1lev1':'כלים לעסק',
 'PRAXA':'כלים לעסק','Lord of the Land':'כלים לעסק','Plans 360':'כלים לעסק',
 'מאצ׳ חופש':'פיננסים','רדאר המניות':'פיננסים','Motoryk':'רכב ותחבורה','בדוק לי':'רכב ותחבורה',
 'Webzz':'כלים לעסק','Cassaboom':'כלים לעסק','VirtoSite':'כלים לעסק',
}
for a in APPS:
    a['cat'] = CAT[a['name']]
CATS = sorted({a['cat'] for a in APPS})

def esc(s): return html.escape(s or '', quote=True)

cards = []
for i, a in enumerate(APPS):
    dom = a['url'].split('/')[2]
    if a['img']:
        media = f'<img class="shot" src="{esc(a["img"])}" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.outerHTML=\'<div class=tile>{esc(a["name"].strip()[0])}</div>\'">'
    else:
        media = f'<div class="tile">{esc(a["name"].strip()[0])}</div>'
    cards.append(
      f'<a class="card" data-cat="{esc(a["cat"])}" data-name="{esc(a["name"])}" href="{esc(a["url"])}" target="_blank" rel="noreferrer">'
      f'{media}<div class="cbody"><div class="cname">{esc(a["name"])}</div>'
      f'<div class="cdesc">{esc(a["desc"])}</div><div class="cdom" dir="ltr">{esc(dom)}</div></div></a>')

chips = '<button class="chip on" data-cat="*">הכל (' + str(len(APPS)) + ')</button>' + ''.join(
    f'<button class="chip" data-cat="{esc(c)}">{esc(c)} ({sum(1 for a in APPS if a["cat"]==c)})</button>' for c in CATS)

nolink_items = ''.join(f'<li>{esc(d)}</li>' for d in NOLINK)

items_jsonld = ','.join(
    '{"@type":"SoftwareApplication","name":' + json.dumps(a['name'], ensure_ascii=False) +
    ',"url":' + json.dumps(a['url'], ensure_ascii=False) +
    ',"description":' + json.dumps(a['desc'], ensure_ascii=False) +
    ',"applicationCategory":' + json.dumps(a['cat'], ensure_ascii=False) + '}' for a in APPS)
jsonld = ('{"@context":"https://schema.org","@type":"CollectionPage",'
 '"name":"73 מיזמים שאנשים בנו עם AI","inLanguage":"he",'
 '"url":"' + SITE + SLUG + '",'
 '"author":{"@type":"Person","name":"עופר שפירא","url":"' + SITE + '/"},'
 '"mainEntity":{"@type":"ItemList","numberOfItems":' + str(len(APPS)) + ',"itemListElement":[' + items_jsonld + ']}}')

CSS = '''
.controls{position:sticky;top:0;background:#fff;padding:.8rem 0 .6rem;border-bottom:1px solid #eee;z-index:5}
.controls input[type=search]{width:100%;padding:.6rem .8rem;font-size:1rem;border:1px solid #ccc;border-radius:8px;margin-bottom:.6rem;font-family:inherit}
.chips{display:flex;gap:.4rem;overflow-x:auto;padding-bottom:.4rem;-webkit-overflow-scrolling:touch}
.chip{white-space:nowrap;border:1px solid #ccc;background:#fff;border-radius:999px;padding:.3rem .8rem;font-size:.85rem;cursor:pointer;font-family:inherit}
.chip.on{background:#111;color:#fff;border-color:#111}
.sortrow{display:flex;align-items:center;gap:.5rem;margin-top:.4rem;font-size:.85rem;color:#555}
.sortrow select{font-family:inherit;font-size:.85rem;padding:.2rem .4rem}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.2rem 0}
@media(max-width:900px){.grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.grid{grid-template-columns:1fr}}
.card{border:1px solid #e3e3e3;border-radius:10px;overflow:hidden;text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:box-shadow .15s}
.card:hover{box-shadow:0 4px 18px rgba(0,0,0,.09)}
.shot{width:100%;aspect-ratio:16/9;object-fit:cover;background:#f4f4f4;display:block}
.tile{width:100%;aspect-ratio:16/9;background:#eef1f5;display:flex;align-items:center;justify-content:center;font-size:2.6rem;color:#667}
.cbody{padding:.7rem .9rem .9rem}
.cname{font-weight:700;margin-bottom:.25rem}
.cdesc{font-size:.88rem;line-height:1.55;color:#333}
.cdom{font-size:.75rem;color:#888;margin-top:.5rem}
.count{font-size:.85rem;color:#777;margin-top:.6rem}
.nolink{line-height:2;padding-inline-start:1.2rem}
.note{font-size:.82rem;color:#777;margin-top:1.5rem}
.credit{font-size:.85rem;color:#666;margin-top:2rem;border-top:1px solid #eee;padding-top:1rem}
'''

HTML = '''<!doctype html>
<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>73 מיזמים שאנשים בנו עם AI | עופר שפירא</title><meta name="description" content="אוסף של 73 מיזמים שאנשים מהקהילה בישראל בנו עם כלי AI: משחקים, אפליקציות לימוד לילדים, כלים לעסקים, פיננסים, מוזיקה ועוד. כל מיזם עם קישור חי."><link rel="canonical" href="%%S%%%%SLUG%%"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="%%S%%%%SLUG%%index.md"><meta property="og:title" content="73 מיזמים שאנשים בנו עם AI"><meta property="og:description" content="מה אנשים באמת בונים עם כלי AI: 73 מיזמים מהקהילה, מפסנתר ועד גלגל המזלות."><meta property="og:url" content="%%S%%%%SLUG%%"><meta property="og:type" content="website"><script src="/webmcp.js" defer></script><script type="application/ld+json">%%JSONLD%%</script><style>%%CSS%%</style></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a><a href="https://www.linkedin.com/in/ofershap/">LinkedIn</a></nav></header><main><article>
<h1>73 מיזמים שאנשים בנו עם AI</h1>
<p>באוקטובר 2026 נפתח בקבוצה העברית של קלוד בפייסבוק שרשור אחד פשוט: ״תראו מה בניתם״. התשובות מספרות את הסיפור הכי טוב על דמוקרטיזציה של קוד: אנשים בלי רקע בפיתוח בונים אפליקציות אמיתיות לכל דבר. משחק לימוד עברית לכיתה א׳, אתר אקורדים עם 1,400 שירים, השוואת חניונים, קורא שבב דרכון, מערכת ERP לייבוא תרופות, משחקי חלל. כמה מהמיזמים כבר עם לקוחות משלמים.</p>
<p>אספתי את כל מה ששותף בשרשור לדף אחד, בלי שמות הכותבים ובלי מונחי פייסבוק. רק המיזמים עצמם. 59 עם קישור חי, עוד 14 ששותפו במילים בלבד.</p>
<div class="controls"><input type="search" id="q" placeholder="חיפוש חופשי..." aria-label="חיפוש"><div class="chips">%%CHIPS%%</div><div class="sortrow"><label for="sort">מיון:</label><select id="sort"><option value="alpha">א-ת</option><option value="cat">קטגוריה</option></select><span class="count" id="count"></span></div></div>
<div class="grid" id="grid">%%CARDS%%</div>
<h2>שותפו בשרשור בלי קישור</h2>
<ul class="nolink">%%NOLINK%%</ul>
<p class="note">הערת כיסוי: נאספו 74 מתוך כ-88 תגובות ברמה הראשונה בשרשור (פייסבוק חוסם צפייה מלאה בלי התחברות), ותגובות משנה לא נפתחו. ייתכן שחסרים מיזמים בודדים. הקישורים אומתו מול האתרים החיים ב-22.10.2026.</p>
<p lang="en" dir="ltr" style="font-size:.85rem;color:#777">A directory of 73 projects built by community members in Israel using AI coding tools (Claude Code, Cursor, Codex): games, kids' education, business tools, finance, music and more. Curated by Ofer Shapira from a public community thread, October 2026.</p>
<p class="credit">אסף וערך: <a href="/about/">עופר שפירא</a>. מקור: שרשור קהילתי בקבוצת ״קלוד - הקהילה הישראלית״ בפייסבוק, אוקטובר 2026.</p>
</article><footer dir="ltr"><a href="/">All writing</a> · <a href="/feed.xml">RSS</a><p class="copyright">© Ofer Shapira</p></footer></main>
<script>
var q=document.getElementById('q'),grid=document.getElementById('grid'),count=document.getElementById('count'),sortSel=document.getElementById('sort');
var cards=[].slice.call(grid.children),cat='*';
function apply(){
 var t=q.value.trim();
 var shown=0;
 cards.forEach(function(c){
  var ok=(cat==='*'||c.dataset.cat===cat)&&(!t||(c.dataset.name+' '+c.textContent).indexOf(t)>-1);
  c.style.display=ok?'':'none';if(ok)shown++;
 });
 count.textContent='מוצגים '+shown+' מתוך '+cards.length;
}
function sortBy(mode){
 var arr=cards.slice();
 arr.sort(function(a,b){
  if(mode==='cat'){var d=a.dataset.cat.localeCompare(b.dataset.cat,'he');if(d)return d;}
  return a.dataset.name.localeCompare(b.dataset.name,'he');
 });
 arr.forEach(function(c){grid.appendChild(c);});
}
document.querySelectorAll('.chip').forEach(function(b){b.addEventListener('click',function(){
 document.querySelectorAll('.chip').forEach(function(x){x.classList.remove('on');});
 b.classList.add('on');cat=b.dataset.cat;apply();
});});
q.addEventListener('input',apply);
sortSel.addEventListener('change',function(){sortBy(sortSel.value);apply();});
sortBy('alpha');apply();
</script>
</body></html>'''

htmlout = (HTML.replace('%%S%%', SITE).replace('%%SLUG%%', SLUG)
           .replace('%%JSONLD%%', jsonld).replace('%%CSS%%', CSS)
           .replace('%%CHIPS%%', chips).replace('%%CARDS%%', ''.join(cards))
           .replace('%%NOLINK%%', nolink_items))

md_lines = ['---', 'title: "73 מיזמים שאנשים בנו עם AI - עופר שפירא"', 'lang: he', '---', '',
 '# 73 מיזמים שאנשים בנו עם AI', '',
 'אוסף של עופר שפירא משרשור קהילתי בקבוצת קלוד הישראלית בפייסבוק (אוקטובר 2026). לדף המלא עם סינון ותמונות: ' + SITE + SLUG, '']
for c in CATS:
    md_lines.append('## ' + c)
    for a in APPS:
        if a['cat'] == c:
            md_lines.append('- [' + a['name'] + '](' + a['url'] + ') - ' + a['desc'])
    md_lines.append('')
md_lines.append('## שותפו בלי קישור')
for d in NOLINK:
    md_lines.append('- ' + d)

d = R / 'community-apps'
d.mkdir(exist_ok=True)
(d / 'index.html').write_text(htmlout, encoding='utf-8')
(d / 'index.md').write_text('\n'.join(md_lines) + '\n', encoding='utf-8')
print('build_community_apps: OK')

sm = R / 'sitemap.xml'; s = sm.read_text()
if SLUG not in s:
    s = s.replace('</urlset>', '<url><loc>' + SITE + SLUG + '</loc></url></urlset>')
    sm.write_text(s)

llms = R / 'llms.txt'; s = llms.read_text()
if SLUG not in s:
    s = s.replace('- [Contact](https://ofershap.github.io/contact/)\n',
                  '- [Contact](https://ofershap.github.io/contact/)\n- [73 community-built AI projects](https://ofershap.github.io/community-apps/)\n', 1)
    llms.write_text(s)

ag = R / 'agents.md'; s = ag.read_text()
if SLUG not in s:
    s = s.replace('| Site map for LLMs |', '| 73 community-built AI projects | ' + SITE + SLUG + ' |\n| Site map for LLMs |', 1)
    ag.write_text(s)
print('build_community_apps links: OK')
