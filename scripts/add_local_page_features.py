#!/usr/bin/env python3
"""Add local download panels and recovered publication DOI links."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from lxml import html as lxml_html


ROOT = Path(__file__).resolve().parent.parent

# Publication DOI links recovered from the pre-synchronization local pages.
PAPER_DOIS = {
    "1.BlindTest/IV/Azabicyclononanedione.html": ["10.1021/ja0687466"],
    "1.BlindTest/XIII/BTXIII.html": ["10.1016/j.cplett.2008.02.113"],
    "1.BlindTest/XIX/BTXIX/BTXIX.html": ["10.1107/S0108768111042868"],
    "1.BlindTest/XV/BTXV/BTXV.html": ["10.1107/S0108768109004066"],
    "1.BlindTest/XVI/BTXVI.html": ["10.1107/S0108768111042868"],
    "1.BlindTest/XVII/BTXVII.html": ["10.1107/S0108768111042868"],
    "1.BlindTest/XVIII/BTXVIII.html": ["10.1107/S0108768111042868"],
    "1.BlindTest/XX/BTXX.html": [
        "10.1107/S0108768111042868",
        "10.1016/j.ijpharm.2011.03.058",
        "10.1039/c8fd00010g",
    ],
    "1.BlindTest/XXI/GallicAcidMH.html": ["10.1107/S0108768111042868"],
    "1.BlindTest/XXII/BTXXII.html": ["10.1107/S2052520616007447"],
    "1.BlindTest/XXIII/BXXIII.html": [
        "10.1107/S2052520616007447",
        "10.1039/c8fd00010g",
    ],
    "1.BlindTest/XXIV/BTXXIV.html": ["10.1107/S2052520616007447"],
    "1.BlindTest/XXIX/BTXXIX.html": ["10.1107/S2052520624007492"],
    "1.BlindTest/XXVC/BTXXVC.html": ["10.1107/S2052520616007447"],
    "1.BlindTest/XXVI/BTXXVI.html": [
        "10.1107/S2052520616007447",
        "10.1039/c8fd00010g",
    ],
    "1.BlindTest/XXVII/XXVII.html": [
        "10.1107/S2052520624007492",
        "10.1107/S2052520624008679",
    ],
    "1.BlindTest/XXVIII/BTXXVIII.html": [
        "10.1107/S2052520624007492",
        "10.1107/S2052520624008679",
    ],
    "1.BlindTest/XXX/2CannabinolTetramethylpyrazine/2CannabinolTetramethylpyrazine.html": [
        "10.1107/S2052520624007492"
    ],
    "1.BlindTest/XXX/Cannabinol/Cannabinol.html": ["10.1107/S2052520624007492"],
    "1.BlindTest/XXX/Cannabinol2Tetramethylpyrazine/Cannabinol2Tetramethylpyrazine.html": [
        "10.1107/S2052520624007492"
    ],
    "1.BlindTest/XXX/CannabinolTetramethylpyrazine/CannabinolTetramethylpyrazine.html": [
        "10.1107/S2052520624007492"
    ],
    "1.BlindTest/XXX/Tetramethylpyrazine/Tetramethylpyrazine.html": [
        "10.1107/S2052520624007492"
    ],
    "1.BlindTest/XXXI/BTXXXI.html": [
        "10.1107/S2052520624007492",
        "10.1107/S2052520624008679",
    ],
    "1.BlindTest/XXXIII/XXXIII.html": [
        "10.1107/S2052520624007492",
        "10.1107/S2052520624008679",
    ],
    "Acridine/Acridine.html": ["10.1021/acs.cgd.9b00557"],
    "Alloxan/Alloxan.html": ["10.1021/cg049661o"],
    "AminobenzoicAcid/AminobenzoicAcid.html": ["10.1021/ct8004326"],
    "Aspirin/Aspirin.html": ["10.1021/cg049922u"],
}

FEATURE_CSS = """
.local-feature-section{margin-top:2.5rem;padding:1.25rem 1.5rem;border:1px solid #d8dce1;border-radius:.45rem;background:#f7f9fb}
.local-feature-section h2{margin-top:0}
.local-feature-section li+li{margin-top:.35rem}
.doi-link{display:inline-block;padding:.2rem .45rem;border:1px solid #1558a6;border-radius:.3rem;color:#1558a6;background:#fff;text-decoration:underline;font-weight:700;overflow-wrap:anywhere}
.doi-link:hover,.doi-link:focus{color:#fff;background:#1558a6}
"""

FEATURE_RE = re.compile(
    r'\n?<section class="local-feature-section (?:paper-links|dataset-downloads)">'
    r".*?</section>\n?",
    re.I | re.S,
)


def synced_pages() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.html")
        if '<main class="cposs-content">' in path.read_text(errors="ignore")
    )


def zip_links(source: str) -> list[str]:
    document = lxml_html.fromstring(source)
    links = []
    for href in document.xpath('//main[@class="cposs-content"]//a/@href'):
        if urlparse(href).path.lower().endswith(".zip"):
            links.append(href)
    return list(dict.fromkeys(links))


def feature_section(title: str, class_name: str, items: list[tuple[str, str]]) -> str:
    links = "".join(
        f'<li><a{(" class=\"doi-link\"" if class_name == "paper-links" else "")} '
        f'href="{html.escape(href, quote=True)}"'
        f'{(" target=\"_blank\" rel=\"noopener\"" if class_name == "paper-links" else " download")}>'
        f"{html.escape(label)}</a></li>"
        for href, label in items
    )
    return (
        f'<section class="local-feature-section {class_name}">'
        f"<h2>{html.escape(title)}</h2><ul>{links}</ul></section>"
    )


def main() -> None:
    pages = synced_pages()
    if len(pages) != 49:
        raise ValueError(f"expected 49 synchronized pages, found {len(pages)}")

    paper_pages = 0
    download_links = 0
    for page in pages:
        relative = page.relative_to(ROOT).as_posix()
        source = FEATURE_RE.sub("\n", page.read_text(encoding="utf-8"))
        source = re.sub(r"\s*</main>", "\n</main>", source, count=1)
        if FEATURE_CSS.strip() not in source:
            source = source.replace("</style>", FEATURE_CSS + "</style>", 1)

        sections = []
        dois = PAPER_DOIS.get(relative, [])
        if dois:
            paper_pages += 1
            sections.append(
                feature_section(
                    "Paper DOI",
                    "paper-links",
                    [(f"https://doi.org/{doi}", f"Open paper ({doi})") for doi in dois],
                )
            )

        downloads = zip_links(source)
        if not downloads:
            raise ValueError(f"{relative}: no existing ZIP dataset links found")
        download_links += len(downloads)
        sections.append(
            feature_section(
                "Dataset downloads",
                "dataset-downloads",
                [
                    (href, unquote(Path(urlparse(href).path).name))
                    for href in downloads
                ],
            )
        )
        source = source.replace("</main>", "\n" + "\n".join(sections) + "\n</main>", 1)
        page.write_text(source, encoding="utf-8")

    print(
        f"Enhanced {len(pages)} pages with {download_links} dataset downloads; "
        f"restored paper DOI links on {paper_pages} pages."
    )


if __name__ == "__main__":
    main()
