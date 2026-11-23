# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Validate the entry graph of the guide.

Checks:
  1. frontmatter present, with the minimum keys and a known category
  2. `id` unique and equal to the file name
  3. every `see_also` resolves to an existing `id`
  4. construct entries (block, field type, modifier, linkage) declare `syntax`
     and have a `## Syntax` section, without bare "..." in place of structure
  5. the guide is in English: Portuguese section headings are refused
  6. case studies have the sections every case study shares

Usage:
    python tools/validate_entries.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries"
LOCALE = "en"
REQUIRED_KEYS = {"id", "title", "category", "summary", "source"}
CATEGORIES = {
    "overview", "block", "field_type", "modifier", "linkage",
    "case_study", "ecosystem", "diagnostic",
}

#: Categories that document a construct of the language: they must show its form.
SYNTAX_CATEGORIES = {"block", "field_type", "modifier", "linkage"}

#: Every case study walks the same path, so readers (and agents) know where to look.
CASE_SECTIONS = (
    "## Research question",
    "## Template",
    "## Annotation",
    "## Design decisions",
    "## Adapt it",
)

#: Headings of the former Portuguese guide. Finding one means an entry was not migrated.
PT_HEADINGS = re.compile(
    r"^## (Descrição|Sintaxe|Regras|Exemplo|Exemplos|Ver também|Propriedades|"
    r"Mensagem do compilador|Onde aparece|Valor na anotação)\s*$",
    re.MULTILINE,
)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip('"')
    return out


def parse_list(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:-1] if raw.endswith("]") else raw[1:]
    return [x.strip().strip('"`') for x in raw.split(",") if x.strip()]


def check(root: Path = ROOT) -> tuple[list[str], dict[str, Path]]:
    problems: list[str] = []
    ids: dict[str, Path] = {}
    links: list[tuple[str, str, Path]] = []

    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root)
        if len(rel.parts) > 2 and rel.parts[1] != LOCALE:
            problems.append(f"{rel}: outside the `{LOCALE}` locale (the guide is English-only)")
        text = md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            problems.append(f"{rel}: no frontmatter")
            continue

        missing = REQUIRED_KEYS - fm.keys()
        if missing:
            problems.append(f"{rel}: frontmatter without {sorted(missing)}")
        category = fm.get("category", "")
        if category and category not in CATEGORIES:
            problems.append(f"{rel}: unknown category '{category}'")

        if category in SYNTAX_CATEGORIES:
            syn = fm.get("syntax", "")
            if not syn:
                problems.append(f"{rel}: category '{category}' without `syntax`")
            else:
                # "..." is fine inside [ ] (abbreviates the inside of a block)
                # and in "X ... END X". Bare between keywords it hides the
                # structure the reader needs to see.
                bare = re.sub(r"\[[^\]]*\]", "", syn)
                bare = re.sub(r"\.\.\.\s*END\s+\w+", "", bare)
                if "..." in bare:
                    problems.append(
                        f"{rel}: `syntax` uses '...' in place of structure "
                        f"(show the parts, inside [ ] when optional)"
                    )
            if "## Syntax" not in text:
                problems.append(f"{rel}: no `## Syntax` section")

        if category == "case_study":
            for section in CASE_SECTIONS:
                if section not in text:
                    problems.append(f"{rel}: case study without `{section}`")

        heading = PT_HEADINGS.search(text)
        if heading:
            problems.append(f"{rel}: Portuguese heading `{heading.group(0).strip()}` (the guide is English-only)")

        eid = fm.get("id")
        if not eid:
            continue
        if eid != md.stem:
            problems.append(f"{rel}: id '{eid}' differs from the file name")
        if eid in ids:
            problems.append(f"{rel}: duplicate id '{eid}'")
        ids[eid] = md
        for target in parse_list(fm.get("see_also", "")):
            links.append((eid, target, md))

    for src, target, path in links:
        if target not in ids:
            problems.append(f"{path.relative_to(root)}: see_also '{target}' does not exist")
    return problems, ids


def main() -> int:
    problems, ids = check()
    if problems:
        print(f"FAILED: {len(problems)} problem(s) in {len(ids)} entries\n")
        for p in problems:
            print(f"  {p}")
        return 1
    by_cat: dict[str, int] = defaultdict(int)
    for path in ids.values():
        fm = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
        by_cat[fm.get("category", "?")] += 1
    cats = ", ".join(f"{k}={v}" for k, v in sorted(by_cat.items()))
    print(f"OK: {len(ids)} valid entries ({cats})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
