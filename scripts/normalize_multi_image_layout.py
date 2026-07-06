#!/usr/bin/env python3
"""Standardize multi-image molecular and CSP figure layouts in paired HTML."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    Path("1.BlindTest/XXX/2CannabinolTetramethylpyrazine/2CannabinolTetramethylpyrazine.html"),
    Path("1.BlindTest/XXX/Cannabinol/Cannabinol.html"),
    Path("1.BlindTest/XXX/Cannabinol2Tetramethylpyrazine/Cannabinol2Tetramethylpyrazine.html"),
    Path("1.BlindTest/XXX/CannabinolTetramethylpyrazine/CannabinolTetramethylpyrazine.html"),
    Path("1.BlindTest/XXX/Tetramethylpyrazine/Tetramethylpyrazine.html"),
    Path("1.Cocrystals/CaffeineHydroxybenzoicAcidCocrystals.html"),
]

CSS = """.multi-image-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;align-items:start;margin:1.25rem 0}
.multi-image-grid img{display:block;width:100%;max-width:none;height:auto;object-fit:contain}
@media (max-width:700px){.multi-image-grid{grid-template-columns:1fr}}
"""

PARAGRAPH_RE = re.compile(r"<p>(?P<body>(?:(?!</p>).)*<img(?:(?!</p>).)*)</p>", re.I | re.S)


def classify(body: str) -> str | None:
    image_count = len(re.findall(r"<img\b", body, re.I))
    if image_count < 2:
        return None
    if "0.MolecularDiagrams/" in body:
        return "molecular-structure-grid"
    if "0.Landscapes/" in body:
        return "csp-landscape-grid"
    return None


def update(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    if ".multi-image-grid{" not in source:
        source = source.replace("</style>", CSS + "</style>", 1)

    existing_groups = source.count('class="multi-image-grid ')
    changed_groups = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed_groups
        body = match.group("body")
        kind = classify(body)
        if kind is None:
            return match.group(0)
        body = re.sub(r"\s*<br>\s*", "", body, flags=re.I)
        changed_groups += 1
        return f'<div class="multi-image-grid {kind}">{body}</div>'

    updated = PARAGRAPH_RE.sub(replace, source)
    if existing_groups + changed_groups != 2:
        raise ValueError(
            f"{path}: expected 2 multi-image groups, "
            f"found {existing_groups + changed_groups}"
        )
    path.write_text(updated, encoding="utf-8")


for relative_path in TARGETS:
    update(ROOT / relative_path)

print(f"Updated {len(TARGETS)} HTML files.")
