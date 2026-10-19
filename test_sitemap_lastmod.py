"""Regression: every sitemap URL carries a real lastmod date."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
sitemap = (root/'sitemap.xml').read_text()
locs = re.findall(r'<loc>([^<]+)</loc>', sitemap)
lastmods = re.findall(r'<lastmod>([^<]+)</lastmod>', sitemap)
assert len(locs) == len(set(locs)) == len(lastmods) and locs, f'{len(locs)} locs vs {len(lastmods)} lastmods'
assert all(re.fullmatch(r'\d{4}-\d{2}-\d{2}', m) for m in lastmods)
by_url = dict(zip(locs, lastmods))
sample = next(u for u in locs if '/posts/linkedin-' in u and not re.search(r'/(en|ar|es|zh-Hans)/', u))
page = (root/sample.replace('https://ofershap.github.io/','').strip('/')/'index.html').read_text()
published = re.search(r'"datePublished"\s*:\s*"([^"]+)"', page)[1][:10]
assert by_url[sample] == published, (sample, by_url[sample], published)
translated = next(u for u in locs if '/en/posts/linkedin-' in u)
tpage = (root/translated.replace('https://ofershap.github.io/','').strip('/')/'index.html').read_text()
tpublished = re.search(r'"datePublished"\s*:\s*"([^"]+)"', tpage)[1][:10]
assert by_url[translated] == tpublished
print(f'{len(locs)} sitemap URLs all carry real lastmod dates; archive and translation spot-checks match datePublished.')
