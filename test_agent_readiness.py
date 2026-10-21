#!/usr/bin/env python3
"""Agent-readiness surfaces: A2A agent card, NLWeb schemamap, llms.txt resolvable links,
homepage BlogPosting breadth, real contact page content."""
import json, re, sys, xml.dom.minidom
from pathlib import Path
R = Path(__file__).resolve().parent
fails = []
def check(name, cond):
    if not cond: fails.append(name)

card = json.loads((R/'.well-known/agent-card.json').read_text())
for k in ['name','description','url','provider','version','capabilities','authentication','defaultInputModes','defaultOutputModes','skills']:
    check('agent-card missing '+k, k in card)
check('agent-card url', card['url'] == 'https://ofershap.github.io/')
check('agent-card no auth', card['authentication']['schemes'] == [])
check('agent-card skills', len(card['skills']) >= 2 and all('id' in sk and 'description' in sk for sk in card['skills']))
check('agent-card real mcp endpoint', 'https://recipes.gitshow.dev/mcp' in json.dumps(card))

robots = (R/'robots.txt').read_text()
check('robots schemamap directive', 'schemamap: https://ofershap.github.io/schemamap.xml' in robots)
sm = xml.dom.minidom.parse(str(R/'schemamap.xml'))
check('schemamap points to rss feed', 'https://ofershap.github.io/feed.xml' in sm.toxml())

llms = (R/'llms.txt').read_text()
check('llms.txt no bare mcp link', '](https://recipes.gitshow.dev/mcp)' not in llms)
check('llms.txt health link resolves pattern', 'https://recipes.gitshow.dev/health' in llms)

home = (R/'index.html').read_text()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', home, re.S)
wil = [json.loads(b) for b in blocks if '"Writing by Ofer Shapira"' in b]
check('writing ItemList exists', len(wil) == 1)
if wil:
    els = wil[0]['itemListElement']
    check('writing ItemList BlogPosting items', all(e.get('item',{}).get('@type')=='BlogPosting' for e in els))
    check('writing ItemList dates', all('datePublished' in e.get('item',{}) for e in els))

contact = (R/'contact/index.html').read_text()
for needle in ['עופר שפירא', 'ישראל', 'linkedin.com/in/ofershap', 'github.com/ofershap', 'Contact Ofer Shapira', 'chat.whatsapp.com']:
    check('contact missing '+needle, needle in contact)

if fails:
    print('FAILS:'); [print(' -', f) for f in fails]; sys.exit(1)
print('test_agent_readiness: OK')
