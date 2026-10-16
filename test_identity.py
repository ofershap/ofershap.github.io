#!/usr/bin/env python3
"""Guard against duplicate homepage introductions after identity rebuilds."""
from pathlib import Path
import re
import build_identity

root = Path(__file__).resolve().parent
before = (root / 'index.html').read_text()
archive = re.search(r'<ul class="post-list">.*?</ul>', before, re.S)[0]
for _ in range(2):
    build_identity.build()
    page = (root / 'index.html').read_text()
    assert page.count('<section class="archive-intro"') == 1
    assert '<section class="identity-intro"' not in page
    assert page.count('id="archive-title"') == 1
    assert page.count('I’m Ofer Shapira, an AI Engineering Team Lead') == 1
    assert re.search(r'<ul class="post-list">.*?</ul>', page, re.S)[0] == archive
    for href in ['/about/', '/about/en/', '/feed.xml', 'https://www.linkedin.com/in/ofershap/']:
        assert f'href="{href}"' in page
    assert page == before, 'Identity rebuild must be idempotent'
print('One homepage hero and bio; archive and links preserved; rebuild idempotent.')
