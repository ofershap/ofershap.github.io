"""Inject the Cloudflare Web Analytics beacon into every HTML page (idempotent).

Runs last in the rebuild chain. Site-wide analytics only - this is NOT the
engagement widget and ignores data-engagement="off" (that flag governs the
likes/views widget from build_engagement.py only).
Token belongs to the ofershap.github.io host site in Cloudflare Web Analytics.
"""
import pathlib, sys

BEACON = ("<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
          "data-cf-beacon='{\"token\": \"101273038ea14fe3b8146df29641a001\"}'></script>")
MARK = "static.cloudflareinsights.com/beacon.min.js"

def inject(html):
    """Idempotent: insert the beacon before </head> unless already present."""
    if MARK in html or "</head>" not in html:
        return html
    return html.replace("</head>", BEACON + "</head>", 1)


def run():
    root = pathlib.Path(".")
    changed = 0
    skipped = 0
    for p in sorted(root.rglob("*.html")):
        if ".git" in p.parts:
            continue
        s = p.read_text(encoding="utf-8")
        if MARK in s:
            skipped += 1
            continue
        if "</head>" not in s:
            continue
        p.write_text(inject(s), encoding="utf-8")
        changed += 1
    print("beacon injected: %d pages, already present: %d" % (changed, skipped))


if __name__ == "__main__":
    run()
