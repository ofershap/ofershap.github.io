#!/usr/bin/env python3
"""One-time idempotent migration: add YAML frontmatter to the standalone English
post markdown files that predate the frontmatter generators. Derives title and
canonical from the sibling index.html, date from the markdown Date: line."""
from pathlib import Path
import json, re
from datetime import datetime

R = Path(__file__).resolve().parent
count = 0
for md in (R / 'posts').glob('*/index.md'):
    text = md.read_text()
    if text.startswith('---\n'):
        continue
    html_path = md.parent / 'index.html'
    html = html_path.read_text() if html_path.exists() else ''
    title_m = re.search(r'<title>(.*?)</title>', html)
    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    date_m = re.search(r'^Date: (\d{4}-\d{2}-\d{2})', text, re.M)
    if not date_m:
        long_m = re.search(r'^([A-Z][a-z]+ \d{1,2}, \d{4})', text, re.M)
        assert long_m, str(md)
        date_iso = datetime.strptime(long_m[1], '%B %d, %Y').date().isoformat()
    else:
        date_iso = date_m[1]
    assert title_m and canon_m, str(md)
    title = re.sub(r'\s*\|.*$', '', title_m[1]).strip()
    fm = ('---\ntitle: ' + json.dumps(title, ensure_ascii=False) + '\n'
          + 'published: ' + date_iso + '\nlang: en\ncanonical: ' + canon_m[1] + '\n---\n\n')
    md.write_text(fm + text)
    count += 1
print('build_frontmatter_en:', count, 'files migrated')
