#!/usr/bin/env python3
"""Correct misassigned molecular-diagram URLs in Blind Test HTML pages."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

CORRECTIONS = {
    "1.BlindTest/VIII/BTVIII.html": "BTVIII.png",
    "1.BlindTest/XII/BTXII.html": "BTXII.png",
    "1.BlindTest/XIII/BTXIII.html": "BTXIII.png",
    "1.BlindTest/XIV/BTXIV.html": "BTXIV.png",
    "1.BlindTest/XIX/BTXIX/BTXIX.html": "BTXIX.png",
    "1.BlindTest/XV/BTXV/BTXV.html": "BTXV.png",
    "1.BlindTest/XVI/BTXVI.html": "BTXVI.png",
    "1.BlindTest/XVII/BTXVII.html": "BTXVII.png",
    "1.BlindTest/XX/BTXX.html": "BTXX.png",
    "1.BlindTest/XXI/GallicAcidMH.html": "GallicAcidMH.png",
    "1.BlindTest/XXIII/BXXIII.html": "BXXIII.png",
    "1.BlindTest/XXIV/BTXXIV.html": "BTXXIV.png",
    "1.BlindTest/XXIX/BTXXIX.html": "BTXXIX.png",
    "1.BlindTest/XXVC/BTXXVC.html": "BTXXVC.png",
    "1.BlindTest/XXVI/BTXXVI.html": "BTXXVI.png",
    "1.BlindTest/XXVII/XXVII.html": "XXVII.png",
    "1.BlindTest/XXXI/BTXXXI.html": "BTXXXI.png",
    "1.BlindTest/XXXIII/XXXIII.html": "XXXIII.png",
}

BASE = (
    "https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/"
    "main/0.MolecularDiagrams/"
)
MOLECULAR_SRC = re.compile(
    r'(?P<prefix><img\b[^>]*\bsrc=")'
    r'https://raw\.githubusercontent\.com/LouisePrice/CPOSS_Database/'
    r'main/0\.MolecularDiagrams/[^"]+'
    r'(?P<suffix>"[^>]*>)',
    re.I,
)


for relative_path, filename in CORRECTIONS.items():
    html = ROOT / relative_path
    if not (ROOT / "0.MolecularDiagrams" / filename).exists():
        raise FileNotFoundError(filename)
    source = html.read_text(encoding="utf-8")
    updated, count = MOLECULAR_SRC.subn(
        lambda match: match.group("prefix") + BASE + filename + match.group("suffix"),
        source,
        count=1,
    )
    if count != 1:
        raise ValueError(f"{relative_path}: expected one molecular diagram, found {count}")
    html.write_text(updated, encoding="utf-8")

print(f"Corrected {len(CORRECTIONS)} Blind Test molecular diagrams.")
