#!/usr/bin/env python3
"""Export Fenamate Word figures and restore their placement in HTML."""

from __future__ import annotations

import html as html_std
import string
import zipfile
from pathlib import Path

from lxml import etree, html


ROOT = Path(__file__).resolve().parent.parent
FAMILY = ROOT / "1.FenamateFamily"
ASSETS = ROOT / "0.Landscapes"
RAW_BASE = (
    "https://raw.githubusercontent.com/LouisePrice/"
    "CPOSS_Database/main/0.Landscapes/"
)

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"

# figure number -> layout. Paragraph figures become responsive grids; table
# figures retain the two-column labelled table already present in HTML.
CONFIG = {
    "FenamicAcid": {
        "title": "Fenamic Acid",
        "figures": {2: "grid", 3: "grid", 4: "table"},
    },
    "FlufenamicAcid": {
        "title": "Flufenamic Acid",
        "figures": {2: "grid", 3: "table"},
    },
    "MefenamicAcid": {
        "title": "Mefenamic Acid",
        "figures": {2: "grid", 3: "table"},
    },
    "NiflumicAcid": {
        "title": "Niflumic Acid",
        "figures": {2: "grid"},
    },
    "TolfenamicAcid": {
        "title": "Tolfenamic Acid",
        "figures": {2: "grid", 3: "table", 4: "table"},
    },
}

CSS = """
.word-figure-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;align-items:start;margin:1.25rem 0}
.word-figure-grid img{display:block;width:100%;height:auto;object-fit:contain}
.word-figure-grid img:last-child:nth-child(odd){grid-column:1/-1;max-width:calc(50% - .5rem);justify-self:center}
.word-figure-table img{display:block;width:100%;height:auto;margin-top:.5rem;object-fit:contain}
@media (max-width:700px){.word-figure-grid{grid-template-columns:1fr}.word-figure-grid img:last-child:nth-child(odd){grid-column:auto;max-width:none}}
"""


def word_figure_groups(docx: Path) -> dict[int, list[tuple[str, bytes]]]:
    """Return figure-numbered image groups in Word document order."""
    with zipfile.ZipFile(docx) as archive:
        root = etree.fromstring(archive.read("word/document.xml"))
        rel_root = etree.fromstring(archive.read("word/_rels/document.xml.rels"))
        relationships = {
            item.get("Id"): item.get("Target")
            for item in rel_root.findall(PR + "Relationship")
        }

        body = root.find(W + "body")
        pending: list[tuple[str, bytes]] = []
        groups: dict[int, list[tuple[str, bytes]]] = {}
        for element in body:
            for blip in element.iter(A + "blip"):
                target = relationships.get(blip.get(R + "embed"), "")
                if target.startswith("media/"):
                    pending.append(
                        (Path(target).name, archive.read("word/" + target))
                    )
            text = "".join(node.text or "" for node in element.iter(W + "t")).strip()
            if text.lower().startswith("figure") and pending:
                number_text = text.split(".", 1)[0].split()[-1]
                if number_text.isdigit():
                    groups[int(number_text)] = pending
                    pending = []
        return groups


def asset_name(stem: str, figure: int, panel: int, total: int) -> str:
    if total == 1:
        return f"{stem}_Figure{figure}.png"
    label = string.ascii_lowercase[panel]
    return f"{stem}_Figure{figure}{label}.png"


def image_element(url: str, alt: str) -> etree._Element:
    element = etree.Element("img")
    element.set("src", url)
    element.set("alt", alt)
    element.set("loading", "lazy")
    return element


def is_image_container(element: etree._Element | None) -> bool:
    if element is None:
        return False
    if element.get("class") == "word-figure-grid":
        return True
    if element.tag != "p":
        return False
    return bool(element.xpath(".//img")) and not "".join(element.itertext()).strip()


def restore_page(stem: str, config: dict) -> tuple[int, int]:
    page = FAMILY / f"{stem}.html"
    docx = FAMILY / f"{stem}.docx"
    groups = word_figure_groups(docx)
    expected = {1, *config["figures"]}
    if set(groups) != expected:
        raise ValueError(f"{stem}: Word figures {sorted(groups)} != {sorted(expected)}")

    document = html.parse(str(page))
    root = document.getroot()
    captions = [
        paragraph
        for paragraph in root.xpath("//p")
        if "".join(paragraph.itertext()).strip().lower().startswith("figure")
    ]
    if len(captions) < len(groups):
        raise ValueError(f"{stem}: only {len(captions)} HTML figure captions")

    exported = 0
    references = 0
    for figure, layout in config["figures"].items():
        images = groups[figure]
        urls = []
        seen_names = {}
        for panel, (media_name, data) in enumerate(images):
            if media_name not in seen_names:
                name = asset_name(stem, figure, panel, len(images))
                (ASSETS / name).write_bytes(data)
                seen_names[media_name] = name
                exported += 1
            name = seen_names[media_name]
            urls.append((name, RAW_BASE + name))

        caption = captions[figure - 1]
        if layout == "grid":
            previous = caption.getprevious()
            while is_image_container(previous):
                remove = previous
                previous = previous.getprevious()
                remove.getparent().remove(remove)

            grid = etree.Element("div")
            grid.set("class", "word-figure-grid")
            for panel, (name, url) in enumerate(urls):
                label = string.ascii_lowercase[panel] if len(urls) > 1 else ""
                alt = f'{config["title"]} figure {figure}'
                if label:
                    alt += f", panel {label}"
                grid.append(image_element(url, alt))
                references += 1
            caption.addprevious(grid)
        else:
            table = caption.getprevious()
            while table is not None and table.tag != "table":
                table = table.getprevious()
            if table is None:
                raise ValueError(f"{stem}: no table before figure {figure}")
            table.set("class", "word-figure-table")
            for old_image in table.xpath(".//img"):
                old_image.getparent().remove(old_image)
            cells = table.xpath("./thead/tr/th|./thead/tr/td|./tbody/tr/th|./tbody/tr/td")
            if len(cells) < len(urls):
                raise ValueError(
                    f"{stem} figure {figure}: {len(cells)} cells for {len(urls)} images"
                )
            for panel, ((name, url), cell) in enumerate(zip(urls, cells)):
                for old_break in cell.xpath("./br"):
                    old_break.getparent().remove(old_break)
                cell.append(etree.Element("br"))
                label = string.ascii_lowercase[panel]
                cell.append(
                    image_element(
                        url,
                        f'{config["title"]} figure {figure}, panel {label}',
                    )
                )
                references += 1

    source = html.tostring(root, encoding="unicode", method="html", doctype="<!doctype html>")
    if CSS.strip() not in source:
        source = source.replace("</style>", CSS + "</style>", 1)
    source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
    page.write_text(source, encoding="utf-8")
    return exported, references


def main() -> None:
    total_assets = total_references = 0
    for stem, config in CONFIG.items():
        assets, references = restore_page(stem, config)
        total_assets += assets
        total_references += references
        print(f"{stem}: exported {assets} assets, restored {references} placements")
    print(
        f"Exported {total_assets} unique figure assets and restored "
        f"{total_references} HTML image placements."
    )


if __name__ == "__main__":
    main()
