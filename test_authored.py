import json,re,hashlib,subprocess,xml.etree.ElementTree as ET
from pathlib import Path
P=Path(__file__).resolve().parent
rows=json.loads((P/'authored-source.json').read_text())
for r in rows:
 f=P/'posts'/r['slug'];assert hashlib.sha256((f/'original.md').read_bytes()).hexdigest()==r['sha256']
 s=(f/'index.html').read_text();schemas=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',s)[1]);assert schemas[0]['@type']=='Article';assert schemas[1]['@type']=='FAQPage'
 for q,a in r['faq']:assert q in s and a.replace('"','&quot;') in s
 assert r['bio'] in s;assert 'Originally published' not in s and 'פורסם במקור' not in s
for f in ['sitemap.xml','feed.xml']:ET.parse(P/f)
files=[P/'index.html',P/'feed.xml',P/'sitemap.xml',P/'llms.txt']+[P/'posts'/r['slug']/'index.html' for r in rows]
before={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
subprocess.run(['python3','build_authored.py'],cwd=P,check=True)
assert before=={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
print('Four original bodies, visible FAQs, schema, XML and idempotence passed.')
