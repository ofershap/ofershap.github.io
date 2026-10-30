#!/usr/bin/env python3
"""Guard against duplicate homepage introductions after identity rebuilds."""
from pathlib import Path
import re
import subprocess
import tempfile,shutil

root = Path(__file__).resolve().parent
_snapshot=tempfile.TemporaryDirectory()
work=Path(_snapshot.name)/'site';shutil.copytree(root,work,ignore=shutil.ignore_patterns('.git','__pycache__'))
root=work
before = (root / 'index.html').read_text()
archive = re.search(r'<ul class="post-list">.*?</ul>', before, re.S)[0]
stable = None
for _ in range(2):
    subprocess.run(['python3','build_identity.py'],cwd=root,check=True)
    page = (root / 'index.html').read_text()
    assert page.count('<section class="archive-intro"') == 1
    assert '<section class="identity-intro"' not in page
    assert page.count('id="archive-title"') == 1
    assert page.count('I’m Ofer Shapira, an AI Engineering Team Lead') == 1
    assert re.search(r'<ul class="post-list">.*?</ul>', page, re.S)[0] == archive
    for href in ['/about/', '/about/en/', '/feed.xml', 'https://www.linkedin.com/in/ofershap/']:
        assert f'href="{href}"' in page
    if stable is not None: assert page == stable, 'Identity rebuild must be idempotent'
    stable = page
print('One homepage hero and bio; archive and links preserved; rebuild idempotent.')
