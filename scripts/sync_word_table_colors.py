#!/usr/bin/env python3
"""Copy DOCX table fills and border colours into same-folder HTML files."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
TABLE_RE = re.compile(r"<table\b.*?</table>", re.I | re.S)
ROW_RE = re.compile(r"<tr\b.*?</tr>", re.I | re.S)
CELL_RE = re.compile(r"<(th|td)\b([^>]*)>", re.I)
STYLE_RE = re.compile(r'\sstyle="([^"]*)"', re.I)


def attr(element: ET.Element, name: str, default: str | None = None) -> str | None:
    return element.get(W + name, default)


def css_color(value: str | None) -> str:
    if not value or value.lower() == "auto":
        return "#000000"
    return "#" + value.upper()


def border_css(border: ET.Element | None) -> str:
    if border is None:
        return "none"
    kind = attr(border, "val", "single")
    if kind in {"nil", "none"}:
        return "none"
    width = max(int(attr(border, "sz", "4")) / 8, 0.5)
    style = {
        "dashed": "dashed",
        "dashSmallGap": "dashed",
        "dotDash": "dashed",
        "dotDotDash": "dashed",
        "dotted": "dotted",
        "double": "double",
    }.get(kind, "solid")
    return f"{width:g}pt {style} {css_color(attr(border, 'color'))}"


def table_formatting(docx: Path) -> list[list[list[dict[str, str]]]]:
    with zipfile.ZipFile(docx) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))

    result = []
    for table in root.iter(W + "tbl"):
        table_borders: dict[str, ET.Element] = {}
        tbl_pr = table.find(W + "tblPr")
        if tbl_pr is not None:
            borders = tbl_pr.find(W + "tblBorders")
            if borders is not None:
                table_borders = {
                    side: borders.find(W + side)
                    for side in ("top", "right", "bottom", "left", "insideH", "insideV")
                }

        rows = []
        tr_elements = table.findall(W + "tr")
        for row_index, row in enumerate(tr_elements):
            cells = []
            tc_elements = row.findall(W + "tc")
            for col_index, cell in enumerate(tc_elements):
                tc_pr = cell.find(W + "tcPr")
                styles: dict[str, str] = {}
                if tc_pr is not None:
                    shading = tc_pr.find(W + "shd")
                    if shading is not None:
                        fill = attr(shading, "fill")
                        if fill and fill.lower() != "auto":
                            styles["background-color"] = css_color(fill)
                        elif fill and fill.lower() == "auto":
                            styles["background-color"] = "transparent"

                direct: dict[str, ET.Element] = {}
                if tc_pr is not None:
                    tc_borders = tc_pr.find(W + "tcBorders")
                    if tc_borders is not None:
                        direct = {
                            side: tc_borders.find(W + side)
                            for side in ("top", "right", "bottom", "left")
                        }

                defaults = {
                    "top": table_borders.get("top" if row_index == 0 else "insideH"),
                    "bottom": table_borders.get(
                        "bottom" if row_index == len(tr_elements) - 1 else "insideH"
                    ),
                    "left": table_borders.get("left" if col_index == 0 else "insideV"),
                    "right": table_borders.get(
                        "right" if col_index == len(tc_elements) - 1 else "insideV"
                    ),
                }
                for side in ("top", "right", "bottom", "left"):
                    border = direct.get(side)
                    if border is None:
                        border = defaults.get(side)
                    if border is not None:
                        styles[f"border-{side}"] = border_css(border)
                span = 1
                if tc_pr is not None:
                    grid_span = tc_pr.find(W + "gridSpan")
                    if grid_span is not None:
                        span = int(attr(grid_span, "val", "1"))
                cells.extend(dict(styles) for _ in range(span))
            rows.append(cells)
        result.append(rows)
    return result


def add_styles(opening_tag: re.Match[str], additions: dict[str, str]) -> str:
    tag, attrs = opening_tag.group(1), opening_tag.group(2)
    existing_match = STYLE_RE.search(attrs)
    declarations: dict[str, str] = {}
    if existing_match:
        for declaration in existing_match.group(1).split(";"):
            if ":" in declaration:
                key, value = declaration.split(":", 1)
                declarations[key.strip()] = value.strip()
        attrs = STYLE_RE.sub("", attrs, count=1)
    declarations.update(additions)
    style = ";".join(f"{key}:{value}" for key, value in declarations.items())
    return f'<{tag}{attrs} style="{style}">'


def synchronize(html: Path, docx: Path, dry_run: bool) -> tuple[int, int]:
    source = html.read_text(encoding="utf-8")
    formatting = table_formatting(docx)
    html_tables = list(TABLE_RE.finditer(source))
    if len(html_tables) > len(formatting):
        raise ValueError(
            f"table count mismatch: HTML={len(html_tables)}, DOCX={len(formatting)}"
        )
    # A few source Word files contain a table that was intentionally omitted
    # from the HTML. Existing HTML tables still map in document order.
    formatting = formatting[: len(html_tables)]

    replacements: list[tuple[int, int, str]] = []
    styled_cells = 0
    for table_index, table_match in enumerate(html_tables):
        block = table_match.group(0)
        html_rows = list(ROW_RE.finditer(block))
        word_rows = formatting[table_index]
        if len(html_rows) != len(word_rows):
            raise ValueError(
                f"table {table_index + 1} row mismatch: "
                f"HTML={len(html_rows)}, DOCX={len(word_rows)}"
            )
        row_replacements: list[tuple[int, int, str]] = []
        for row_index, row_match in enumerate(html_rows):
            row_block = row_match.group(0)
            html_cells = list(CELL_RE.finditer(row_block))
            word_cells = word_rows[row_index]
            if len(html_cells) != len(word_cells):
                # Legacy conversion expanded/contracted a handful of merged
                # Word rows instead of emitting colspan. Project the Word grid
                # proportionally onto the HTML cells in those exceptional rows.
                word_cells = [
                    word_cells[min(index * len(word_cells) // len(html_cells), len(word_cells) - 1)]
                    for index in range(len(html_cells))
                ]
            cell_replacements = []
            for cell_match, styles in zip(html_cells, word_cells):
                if styles:
                    updated = add_styles(cell_match, styles)
                    cell_replacements.append((cell_match.start(), cell_match.end(), updated))
                    styled_cells += 1
            for start, end, updated in reversed(cell_replacements):
                row_block = row_block[:start] + updated + row_block[end:]
            row_replacements.append((row_match.start(), row_match.end(), row_block))
        for start, end, updated in reversed(row_replacements):
            block = block[:start] + updated + block[end:]
        replacements.append((table_match.start(), table_match.end(), block))

    updated_source = source
    for start, end, updated in reversed(replacements):
        updated_source = updated_source[:start] + updated + updated_source[end:]

    updated_source = updated_source.replace(
        "th,td{border:1px solid #bbb;",
        "th,td{border:0.5pt solid #000;",
    ).replace(
        "vertical-align:top} th{background:#f3f4f5}",
        "vertical-align:top} th{background:transparent}",
    )
    if not dry_run and updated_source != source:
        html.write_text(updated_source, encoding="utf-8")
    return len(formatting), styled_cells


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    dry_run = "--dry-run" in sys.argv
    pairs = []
    for html in root.rglob("*.html"):
        docx = html.with_suffix(".docx")
        if docx.exists() and not docx.name.startswith("~$"):
            pairs.append((html, docx))

    failures = []
    total_tables = total_cells = 0
    for html, docx in sorted(pairs):
        try:
            tables, cells = synchronize(html, docx, dry_run)
            total_tables += tables
            total_cells += cells
        except Exception as error:
            failures.append(f"{html.relative_to(root)}: {error}")

    print(
        f"{'Checked' if dry_run else 'Updated'} {len(pairs) - len(failures)} files, "
        f"{total_tables} tables, {total_cells} cells."
    )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
