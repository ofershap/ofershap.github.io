#!/usr/bin/env python3
"""Add real lastmod dates to sitemap.xml.

Each URL's lastmod is the datePublished already declared in the page's own
JSON-LD schema (never fabricated). Pages without one (homepage, about, for-ai)
get the build date. Idempotent; every builder calls run() at the end.
"""
from pathlib import Path
import datetime
import html
import re

R = Path(__file__).resolve().parent
BASE = 'https://ofershap.github.io'


def _date_for(url: str, today: str) -> str:
    path = url.replace(BASE + '/', '').strip('/')
    f = R / path / 'index.html' if path else R / 'index.html'
    if f.exists():
        m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', f.read_text())
        if m:
            return m[1][:10]
    return today



def _md_siblings():
    """Serve post-level <slug>.md next to each posts/<slug>/ directory."""
    posts = R / 'posts'
    if posts.exists():
        for d in posts.iterdir():
            md = d / 'index.md'
            if d.is_dir() and md.exists():
                (posts / (d.name + '.md')).write_text(md.read_text())

def run() -> None:
    _md_siblings()
    p = R / 'sitemap.xml'
    s = p.read_text()
    today = datetime.date.today().isoformat()

    seen = set()

    def repl(m):
        if m[1] in seen:
            return ''
        seen.add(m[1])
        url = html.unescape(m[1])
        return '<url><loc>' + m[1] + '</loc><lastmod>' + _date_for(url, today) + '</lastmod></url>'

    s = re.sub(r'<url><loc>([^<]+)</loc>(?:<lastmod>[^<]*</lastmod>)?</url>', repl, s)
    p.write_text(s)


if __name__ == '__main__':
    run()
