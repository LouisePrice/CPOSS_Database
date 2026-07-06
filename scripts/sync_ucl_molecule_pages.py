#!/usr/bin/env python3
"""Synchronize local molecule HTML content from the public UCL CPOSS pages."""

from __future__ import annotations

import html as html_std
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

from lxml import html


ROOT = Path(__file__).resolve().parent.parent
INDEX_URL = "https://www.chem.ucl.ac.uk/cposs/database/molecule_list2.html"
MOLECULE_BASE_URL = urljoin(INDEX_URL, "molecules/")

PAGE_TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>
body{{font:16px/1.5 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;max-width:1100px;margin:3rem auto;padding:0 2rem;color:#202124}}
h1,h2,h3,h4,h5,h6{{line-height:1.2;margin-top:1.6em}}
img{{max-width:100%;height:auto}}
.caption{{font-style:italic}}
.cposs-content>table{{border-collapse:collapse;width:100%;margin:1.25rem 0;display:block;overflow-x:auto}}
.cposs-content>table>tbody>tr>th,.cposs-content>table>tbody>tr>td,
.cposs-content>table>thead>tr>th,.cposs-content>table>thead>tr>td{{
border:0.5pt solid #000;padding:.45rem .6rem;text-align:left;vertical-align:top}}
.cposs-content td>table{{border-collapse:collapse;width:100%;margin:0}}
.cposs-content td>table th,.cposs-content td>table td{{border:0;padding:0;text-align:left;vertical-align:top}}
.cposs-content a{{overflow-wrap:anywhere}}
</style></head><body>
<main class="cposs-content">
{content}
</main>
</body></html>
"""


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "CPOSS consistency sync"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def remote_entries(index_bytes: bytes) -> list[tuple[str, str]]:
    document = html.fromstring(index_bytes)
    entries = []
    for anchor in document.xpath('//a[starts-with(@href, "molecules/")]'):
        href = anchor.get("href", "")
        if href.lower().endswith(".html"):
            entries.append((Path(href).name, normalize(anchor.text_content())))
    return entries


def local_page(remote_filename: str) -> Path:
    stem = Path(remote_filename).stem.casefold()
    excluded = {"index.html", "contributors.html"}
    matches = [
        path
        for path in ROOT.rglob("*.html")
        if path.name not in excluded
        and "audit_reports" not in path.parts
        and path.stem.casefold() == stem
    ]
    if len(matches) != 1:
        raise ValueError(f"{remote_filename}: expected one local match, found {matches}")
    return matches[0]


def extract_content(page_bytes: bytes) -> tuple[str, str]:
    document = html.fromstring(page_bytes)
    headings = document.xpath('//span[@class="pageheading"]')
    if not headings:
        raise ValueError("remote page has no pageheading")
    title = normalize(headings[0].text_content())
    title_headings = [
        heading
        for heading in document.xpath("//h2")
        if normalize(heading.text_content()) == title
    ]
    if not title_headings:
        raise ValueError(f"remote page has no content heading matching {title!r}")

    content_root = title_headings[0].getparent()
    content_heading = title_headings[0]
    content_heading.tag = "h1"

    children = list(content_root)
    start = children.index(content_heading)
    content_children = children[start:]
    while content_children and normalize(content_children[-1].text_content()) == "":
        content_children.pop()

    serialized = "\n".join(
        html.tostring(child, encoding="unicode", method="html")
        for child in content_children
    )
    serialized = "\n".join(line.rstrip() for line in serialized.splitlines())
    return title, serialized


def main() -> int:
    index_bytes = fetch(INDEX_URL)
    entries = remote_entries(index_bytes)
    if len(entries) != 49:
        raise ValueError(f"expected 49 molecule pages, found {len(entries)}")

    dry_run = "--dry-run" in sys.argv
    changed = 0
    for remote_filename, _ in entries:
        page_bytes = fetch(urljoin(MOLECULE_BASE_URL, remote_filename))
        title, content = extract_content(page_bytes)
        output = PAGE_TEMPLATE.format(
            title=html_std.escape(title),
            content=content,
        )
        local = local_page(remote_filename)
        if local.read_text(encoding="utf-8") != output:
            changed += 1
            if not dry_run:
                local.write_text(output, encoding="utf-8")

    print(
        f"{'Would update' if dry_run else 'Updated'} {changed} of "
        f"{len(entries)} UCL-listed local molecule pages."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
