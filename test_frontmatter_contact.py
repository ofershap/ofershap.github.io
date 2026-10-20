#!/usr/bin/env python3
"""Guard markdown frontmatter on post pages and the /contact page."""
from pathlib import Path
import re

R = Path(__file__).resolve().parent

mds = list((R / 'posts').glob('*/index.md'))
assert len(mds) > 700, len(mds)
for f in mds:
    head = f.read_text()[:800]
    assert head.startswith('---\n'), str(f)
    fm = head.split('---', 2)[1]
    for field in ('title:', 'published:', 'lang:', 'canonical: https://ofershap.github.io/posts/'):
        assert field in fm, (str(f), field)
# archive posts also carry the original source
archive = [f for f in mds if 'linkedin-' in f.name or 'whatsapp' in f.name]
sample = (R / 'posts' / 'linkedin-7507319211346731008' / 'index.md').read_text()
assert 'source: https://www.linkedin.com/' in sample.split('---', 2)[1]

html = (R / 'contact' / 'index.html').read_text()
md = (R / 'contact' / 'index.md').read_text()
for blob in (html, md):
    assert 'linkedin.com/in/ofershap' in blob and 'github.com/ofershap' in blob
    assert 'mailto:' not in blob, 'no invented email'

llms = (R / 'llms.txt').read_text()
assert '/agents.md' in llms and '/contact/' in llms
sm = (R / 'sitemap.xml').read_text()
assert re.search(r'<url><loc>https://ofershap\.github\.io/contact/</loc><lastmod>\d{4}-\d{2}-\d{2}</lastmod></url>', sm)
home = (R / 'index.html').read_text()
assert '/contact/' in home
print('test_frontmatter_contact: OK')
