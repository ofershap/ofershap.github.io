#!/usr/bin/env python3
"""Idempotent readiness upgrade for post pages from retired generators.
Every posts/*/index.html gets the full agent-readiness set: Open Graph,
Microdata (BlogPosting), markdown alternate link, WebMCP registration."""
from pathlib import Path
import re, html, json
R = Path(__file__).resolve().parent
TAG = '<script src="/webmcp.js" defer></script>'
E = html.escape
upgraded = skipped = 0
for f in sorted(R.glob('posts/*/index.html')):
    s = f.read_text()
    if 'itemscope' in s and TAG in s:
        skipped += 1
        continue
    title_m = re.search(r'<title>(.*?)</title>', s)
    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', s)
    date_m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', s)
    title = re.sub(r'\s*\|.*$', '', title_m[1]).strip() if title_m else f.parent.name
    # Open Graph gaps
    if 'property="og:title"' not in s:
        og = ('<meta property="og:type" content="article">'
              f'<meta property="og:title" content="{E(title, quote=True)}">'
              + (f'<meta property="og:description" content="{desc_m[1]}">' if desc_m else '')
              + (f'<meta property="og:url" content="{canon_m[1]}">' if canon_m else '')
              + '<meta name="twitter:card" content="summary">')
        s = s.replace('</head>', og + '</head>', 1)
    # WebMCP registration
    if TAG not in s:
        s = s.replace('</head>', TAG + '</head>', 1)
    # Microdata on <main> (these pages predate <article>)
    if 'itemscope' not in s:
        meta = '<meta itemprop="author" content="Ofer Shapira">'
        if date_m:
            meta += f'<meta itemprop="datePublished" content="{date_m[1]}">'
        s = s.replace('<main>', '<main itemscope itemtype="https://schema.org/BlogPosting">' + meta, 1)
        s = re.sub(r'<h1>', '<h1 itemprop="headline">', s, count=1)
        # articleBody: from after the byline/nav block to the first trailing block.
        m = re.search(r'(<p class="byline".*?</p>)', s, re.S)
        if m:
            start = m.end(1)
            tail = re.search(r'<(div class="links"|section class="related-projects"|div class="engagement-actions"|footer)', s[start:])
            end = start + tail.start() if tail else s.find('</main>', start)
            if end > start:
                s = s[:start] + '<div itemprop="articleBody">' + s[start:end] + '</div>' + s[end:]
    f.write_text(s)
    upgraded += 1
print('post upgrade:', upgraded, 'upgraded,', skipped, 'already current')
