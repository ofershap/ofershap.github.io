"""Regression: attributed li elements and authored guides share newest-first order."""
from pathlib import Path
import re
import homepage_order

root = Path(__file__).resolve().parent
page = (root/'index.html').read_text()
inner = re.search(r'<ul class="post-list">(.*?)</ul>', page, re.S)[1]
hrefs = re.findall(r'<a class="post-title" href="([^"]+)"', inner)
assert len(hrefs) == len(set(hrefs)) == 780
assert '/posts/whatsapp-agent-cost-israel/' in hrefs
assert any('/posts/linkedin-' in href for href in hrefs)
dates = []
for href in hrefs:
    article = (root/href.strip('/')/'index.html').read_text()
    date = re.search(r'"datePublished"\s*:\s*"([^"]+)"',article)
    dates.append(date[1][:10] if date else '0000-00-00')
assert dates == sorted(dates,reverse=True)
assert dates[0] == '2026-10-18'
homepage_order.sort_homepage(root)
assert (root/'index.html').read_text() == page
print(f'{len(hrefs)} unique entries sorted newest-first across authored guides and archive; idempotent.')
