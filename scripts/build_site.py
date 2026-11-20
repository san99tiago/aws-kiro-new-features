#!/usr/bin/env python3
"""Render research/*.md into site/research/*.html plus a manifest.json.

Uses only the standard library, with a small Markdown subset renderer
(headings, bullet and ordered lists, links, bold, inline code, code blocks, paragraphs).
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "research"
OUT = ROOT / "site" / "research"

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../styles.css">
<script>(function(){{var r=document.documentElement,s=localStorage.getItem("theme"),d=window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches;r.setAttribute("data-theme",s||(d?"dark":"light"));window.addEventListener("DOMContentLoaded",function(){{document.getElementById("theme-toggle").addEventListener("click",function(){{var n=r.getAttribute("data-theme")==="dark"?"light":"dark";r.setAttribute("data-theme",n);localStorage.setItem("theme",n);}});}});}})();</script>
</head><body>
<header class="topbar"><a class="brand" href="../index.html">Kiro News</a>
<div class="flags" aria-label="Latinoamérica"><span role="img" aria-label="Argentina" title="Argentina">🇦🇷</span><span role="img" aria-label="Bolivia" title="Bolivia">🇧🇴</span><span role="img" aria-label="Brasil" title="Brasil">🇧🇷</span><span role="img" aria-label="Chile" title="Chile">🇨🇱</span><span role="img" aria-label="Colombia" title="Colombia">🇨🇴</span><span role="img" aria-label="Costa Rica" title="Costa Rica">🇨🇷</span><span role="img" aria-label="Cuba" title="Cuba">🇨🇺</span><span role="img" aria-label="República Dominicana" title="República Dominicana">🇩🇴</span><span role="img" aria-label="Ecuador" title="Ecuador">🇪🇨</span><span role="img" aria-label="El Salvador" title="El Salvador">🇸🇻</span><span role="img" aria-label="Guatemala" title="Guatemala">🇬🇹</span><span role="img" aria-label="Haití" title="Haití">🇭🇹</span><span role="img" aria-label="Honduras" title="Honduras">🇭🇳</span><span role="img" aria-label="México" title="México">🇲🇽</span><span role="img" aria-label="Nicaragua" title="Nicaragua">🇳🇮</span><span role="img" aria-label="Panamá" title="Panamá">🇵🇦</span><span role="img" aria-label="Paraguay" title="Paraguay">🇵🇾</span><span role="img" aria-label="Perú" title="Perú">🇵🇪</span><span role="img" aria-label="Uruguay" title="Uruguay">🇺🇾</span><span role="img" aria-label="Venezuela" title="Venezuela">🇻🇪</span></div>
<nav><a href="index.html">All reports</a><a href="latest.html">Latest</a>
<button id="theme-toggle" type="button" aria-label="Toggle dark or light theme">Theme</button></nav></header>
<main>
{body}
</main>
<footer><p>Apache 2.0. Copyright 2026 Santiago Garcia Arango.</p></footer>
</body></html>
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)

    def link(m):
        url = m.group(2).replace("&amp;", "&")
        if not re.match(r"^(https?://|#|[\w./-]+$)", url):
            return m.group(0)
        return '<a href="%s">%s</a>' % (html.escape(url, quote=True), m.group(1))

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def render(md):
    out, in_list, in_code, para = [], None, False, []

    def flush():
        nonlocal para
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</%s>" % in_list)
            in_list = None

    for line in md.splitlines():
        if line.startswith("```"):
            flush()
            close_list()
            out.append("</pre>" if in_code else "<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            close_list()
            n = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
        elif re.match(r"^\s*([-*]|\d+[.)])\s+", line):
            flush()
            kind = "ol" if re.match(r"^\s*\d", line) else "ul"
            if in_list != kind:
                close_list()
                out.append('<%s class="list">' % kind)
                in_list = kind
            out.append("<li>%s</li>" % inline(re.sub(r"^\s*([-*]|\d+[.)])\s+", "", line)))
        elif not line.strip():
            flush()
            close_list()
        else:
            close_list()
            para.append(line.strip())
    flush()
    close_list()
    if in_code:
        out.append("</pre>")
    return "\n".join(out)


def title_of(md, fallback):
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(
        (p for p in SRC.glob("*.md") if p.name not in ("README.md", "latest.md")), reverse=True
    )
    manifest = []
    # latest.md is rendered only as latest.html, never listed as a report.
    for p in files:
        md = p.read_text(encoding="utf-8")
        title = title_of(md, p.stem)
        name = p.stem + ".html"
        (OUT / name).write_text(
            PAGE.format(title=html.escape(title), body=render(md)), encoding="utf-8"
        )
        manifest.append({"title": title, "href": "research/" + name})

    dated = [p for p in files if re.match(r"\d{4}-\d{2}-\d{2}-summary\.md$", p.name)]
    latest_src = dated[0] if dated else (SRC / "latest.md")
    latest_md = latest_src.read_text(encoding="utf-8") if latest_src.exists() else "# Latest\n\nNo report yet."
    (OUT / "latest.html").write_text(
        PAGE.format(title="Latest report", body=render(latest_md)), encoding="utf-8"
    )

    items = "\n".join(
        '<li><a href="%s">%s</a></li>'
        % (html.escape(Path(m["href"]).name, quote=True), html.escape(m["title"]))
        for m in manifest
    ) or "<li>No reports yet.</li>"
    body = '<h1>All research reports</h1>\n<ul class="list">\n%s\n</ul>' % items
    (OUT / "index.html").write_text(
        PAGE.format(title="All research reports", body=body), encoding="utf-8"
    )
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Rendered %d report(s)" % len(manifest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
