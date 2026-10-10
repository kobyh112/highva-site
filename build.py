#!/usr/bin/env python3
"""Builds the Highva website (highva.app) into plain HTML files.

    python3 build.py

Pages:
  index.html          home          (content/home.html)
  privacy/index.html  Privacy Policy (content/privacy.md)
  terms/index.html    Terms of Use   (content/terms.md)
  support/index.html  Support + FAQ  (content/support.html)

The two legal documents are written in a small part of Markdown: headings
(#, ##), paragraphs, bullet and numbered lists, **bold**, and plain web
links and email addresses (made clickable). Text in [square brackets] is a
placeholder to fill in, shown with a dashed underline.

No dependencies beyond Python 3. Commit the generated HTML: GitHub Pages
serves the files as they are.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://highva.app"
EMAIL = "support@highva.app"

PAGES = [
    # (output, title, description, source, nav key)
    ("index.html", "Highva", "Set your vision. Create a system. Break goals into daily tasks, protect your streaks, reflect nightly, and get coaching inspired by history's brightest minds. Coming soon to the App Store.", "home.html", "home"),
    ("privacy/index.html", "Privacy Policy · Highva", "What Highva stores, what it shares with its AI provider, what it counts with analytics, and your choices.", "privacy.md", "privacy"),
    ("terms/index.html", "Terms of Use · Highva", "The terms for using Highva.", "terms.md", "terms"),
    ("support/index.html", "Support · Highva", "Contact Highva support and answers to common questions.", "support.html", "support"),
]


def inline(text: str) -> str:
    """Escapes text, then adds bold, links, emails and placeholder marks."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(https?://[^\s<)]+[^\s<).,;:])", r'<a href="\1">\1</a>', out)
    out = re.sub(r"(?<![\w.@/])([\w.+-]+@[\w-]+\.[\w.]+[\w])", r'<a href="mailto:\1">\1</a>', out)
    out = re.sub(r"\[([^\]]+)\]", r'<span class="fill">[\1]</span>', out)
    return out


def markdown(md: str) -> str:
    """The small Markdown subset above → HTML."""
    blocks: list[tuple[str, str]] = []  # (kind, text): h1, h2, p, ul, ol
    cur: list | None = None
    for raw in md.split("\n"):
        line = raw.strip()
        if not line:
            cur = None
            continue
        item = re.match(r"^(-|\d+\.)\s+(.*)$", line)
        if line.startswith("# "):
            blocks.append(cur := ["h1", line[2:]])
        elif line.startswith("## "):
            blocks.append(cur := ["h2", line[3:]])
        elif item:
            blocks.append(cur := ["ul" if item.group(1) == "-" else "ol", item.group(2)])
        elif cur and cur[0] in ("p", "ul", "ol") and not re.match(r"^\*\*[^*]+:\*\*", line):
            cur[1] += " " + line
        else:
            blocks.append(cur := ["p", line])
    out: list[str] = []
    open_list = None
    for kind, text in blocks:
        if kind in ("ul", "ol"):
            if open_list != kind:
                if open_list:
                    out.append(f"</{open_list}>")
                out.append(f"<{kind}>")
                open_list = kind
            out.append(f"  <li>{inline(text)}</li>")
            continue
        if open_list:
            out.append(f"</{open_list}>")
            open_list = None
        out.append(f"<{kind}>{inline(text)}</{kind}>")
    if open_list:
        out.append(f"</{open_list}>")
    return "\n".join(out)


def page(out: str, title: str, description: str, body: str, key: str) -> str:
    depth = out.count("/")
    up = "../" * depth
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{up}{href}"{current if k == key else ""}>{label}</a>'
        for k, href, label in [("privacy", "privacy/", "Privacy"), ("terms", "terms/", "Terms"), ("support", "support/", "Support")]
    )
    url = SITE + "/" + out.replace("index.html", "")
    main_class = "home" if key == "home" else "doc"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="theme-color" content="#0A0A0B">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="{up or './'}" aria-label="Highva home"><img src="{up}assets/mark.svg" alt="" width="28" height="28"><span>Highva</span></a>
  <nav>{nav}</nav>
</header>
<main class="{main_class}">
{body}
</main>
<footer class="bottom">
  <nav><a href="{up}privacy/">Privacy Policy</a><a href="{up}terms/">Terms of Use</a><a href="{up}support/">Support</a></nav>
  <p>© 2026 Highva · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</footer>
</body>
</html>
"""


def main() -> None:
    for out, title, description, source, key in PAGES:
        text = (ROOT / "content" / source).read_text()
        body = markdown(text) if source.endswith(".md") else text.strip()
        target = ROOT / out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(out, title, description, body, key))
        print("wrote", out)


if __name__ == "__main__":
    main()
