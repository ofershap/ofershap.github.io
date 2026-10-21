#!/usr/bin/env python3
"""Build /contact - public channels only (no invented email). Idempotent."""
from pathlib import Path

R = Path(__file__).resolve().parent
SITE = 'https://ofershap.github.io'
LINKEDIN = 'https://www.linkedin.com/in/ofershap/'
WHATSAPP = 'https://chat.whatsapp.com/K4e3jxRerQs7QDAy9h8InB?mode=gi_t'
GITHUB = 'https://github.com/ofershap'

html = '''<!doctype html>
<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>יצירת קשר | עופר שפירא</title><meta name="description" content="דרכים ליצור קשר עם עופר שפירא: לינקדאין וגיטהאב."><link rel="canonical" href="{S}/contact/"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="text/markdown" href="{S}/contact/index.md"></head><body><header dir="ltr"><span class="site-name"><a href="/">Ofer Shapira</a></span><nav><a href="/">Writing</a><a href="{LI}">LinkedIn</a></nav></header><main><article><h1>יצירת קשר</h1><p>אני עופר שפירא, מוביל צוות AI Engineering, גר בישראל וכותב בעברית ובאנגלית על הנדסת AI, סוכנים ופיתוח בקוד פתוח.</p><p>הדרך הכי טובה לתפוס אותי היא הודעה בלינקדאין. אני עונה בעצמי, בדרך כלל תוך יום-יומיים. אפשר גם דרך גיטהאב, במיוחד על פרויקטים בקוד פתוח.</p><ul><li><a href="{LI}">לינקדאין - שליחת הודעה</a></li><li><a href="{GH}">גיטהאב - שליחת הודעה</a></li><li><a href="{WA}">קבוצת הוואטסאפ שלנו - עזרה ביצירת בוט משלכם</a></li></ul><p>נושאים שכיף לדבר עליהם: בניית סוכני AI, שרתי MCP, אימוץ כלי קוד בצוותים, הטמעת AI בעסקים קטנים, הרצאות וסדנאות.</p><p lang="en" dir="ltr">Contact Ofer Shapira: the best channel is a LinkedIn message. Based in Israel, writing in Hebrew and English about AI engineering, agents and open source. Replies personally, usually within a day or two.</p><p>על הבלוג עצמו: <a href="/">הכתבות</a> · <a href="/about/">מי אני</a></p></article><footer dir="ltr"><a href="/">All writing</a> · <a href="/feed.xml">RSS</a><p class="copyright">© Ofer Shapira</p></footer></main></body></html>'''.format(S=SITE, LI=LINKEDIN, GH=GITHUB, WA=WHATSAPP)

md = '''---\ntitle: "יצירת קשר - עופר שפירא"\nlang: he\n---\n\n# יצירת קשר - עופר שפירא

עופר שפירא, מוביל צוות AI Engineering, ישראל. כותב בעברית ובאנגלית על הנדסת AI, סוכנים וקוד פתוח.

- לינקדאין (הערוץ הכי טוב): {LI}
- גיטהאב: {GH}
- קבוצת וואטסאפ לעזרה ביצירת בוט: {WA}
- הבלוג: {S}/

Contact Ofer Shapira: best via LinkedIn message. Based in Israel, replies personally.
'''.format(LI=LINKEDIN, GH=GITHUB, S=SITE, WA=WHATSAPP)

d = R / 'contact'
d.mkdir(exist_ok=True)
(d / 'index.html').write_text(html)
(d / 'index.md').write_text(md)
print('build_contact: OK')

# register discovery links (idempotent)
import re
sm = R / 'sitemap.xml'; s = sm.read_text()
if '/contact/' not in s:
    s = s.replace('</urlset>', '<url><loc>' + SITE + '/contact/</loc></url></urlset>')
    sm.write_text(s)

# homepage link lives in build_identity.py archive-links (regenerated there)

llms = R / 'llms.txt'; s = llms.read_text()
if '/contact/' not in s:
    s = s.replace('- [Agent usage guide](https://ofershap.github.io/agents.md)\n',
                  '- [Agent usage guide](https://ofershap.github.io/agents.md)\n- [Contact](https://ofershap.github.io/contact/)\n', 1)
    llms.write_text(s)

ag = R / 'agents.md'; s = ag.read_text()
if '/contact/' not in s:
    s = s.replace('| Site map for LLMs |', '| Contact | {S}/contact/ |\n| Site map for LLMs |'.format(S=SITE), 1)
    ag.write_text(s)
print('build_contact links: OK')
