"""One chronological order for original essays, authored guides and archive posts."""
from pathlib import Path
import re


def sort_homepage(root: Path):
    path = root / 'index.html'
    page = path.read_text()
    match = re.search(r'<ul class="post-list">(.*?)</ul>', page, re.S)
    entries = []
    seen = set()
    for found in re.finditer(r'<li\b[^>]*>.*?</li>', match[1], re.S):
        item = found[0]
        href = re.search(r'href="([^"]+)"', item)
        if not href or href[1] in seen:
            continue
        article = root / href[1].strip('/') / 'index.html'
        if not article.exists():
            continue
        published = re.search(r'"datePublished"\s*:\s*"([^"]+)"', article.read_text())
        date = published[1][:10] if published else '0000-00-00'
        entries.append((date, item))
        seen.add(href[1])
    entries.sort(key=lambda row: row[0], reverse=True)
    parts = []
    year = None
    for date, item in entries:
        if date[:4] != year:
            year = date[:4]
            parts.append(f'<li class="year-group"><h2 class="year">{year}</h2></li>')
        parts.append(item)
    path.write_text(page[:match.start(1)] + '\n'.join(parts) + page[match.end(1):])
