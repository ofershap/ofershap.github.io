#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex and partners) so new/updated pages are recrawled fast.

Usage: python3 indexnow_ping.py [url ...]
No arguments submits every sitemap URL (full resubmit). With arguments, submit only those.
Key file: 5755fc79214e2c28b85d10b2249f1297.txt at the site root (must be live before pinging).
"""
from pathlib import Path
import json
import re
import sys
import urllib.request
import urllib.error

R = Path(__file__).resolve().parent
BASE = 'https://ofershap.github.io'
KEY = '5755fc79214e2c28b85d10b2249f1297'
KEY_LOCATION = BASE + '/' + KEY + '.txt'


def main():
    urls = sys.argv[1:]
    if not urls:
        urls = re.findall(r'<loc>([^<]+)</loc>', (R / 'sitemap.xml').read_text())
    body = json.dumps({'host': 'ofershap.github.io', 'key': KEY,
                       'keyLocation': KEY_LOCATION, 'urlList': urls}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body,
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('IndexNow accepted:', r.status, '| urls submitted:', len(urls))
    except urllib.error.HTTPError as e:
        print('IndexNow HTTP', e.code, e.read()[:300])
        sys.exit(1)


if __name__ == '__main__':
    main()
