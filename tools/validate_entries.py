# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Valida o grafo de entries do guia.

Checa (secao 5.2 e 5.4 do estudo):
  1. frontmatter presente e com os campos minimos
  2. `id` unico dentro de cada locale
  3. todo `see_also` resolve para um `id` existente
  4. paridade de locale: nenhuma entry orfa fora de pt

Uso:
    python tools/validate_entries.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries"
BASE_LOCALE = "pt"
REQUIRED_KEYS = {"id", "title", "category", "summary", "source"}

#: Categorias que documentam uma construcao da linguagem: precisam declarar a
#: forma sintatica. Panorama e diagnostico nao descrevem uma construcao.
SYNTAX_CATEGORIES = {"block", "field_type", "modifier", "linkage"}


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


def main() -> int:
    problems: list[str] = []
    # locale -> id -> path
    ids: dict[str, dict[str, Path]] = defaultdict(dict)
    links: list[tuple[str, str, str, Path]] = []

    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT)
        locale = rel.parts[1] if len(rel.parts) > 2 else BASE_LOCALE
        text = md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            problems.append(f"{rel}: sem frontmatter")
            continue

        missing = REQUIRED_KEYS - fm.keys()
        if missing:
            problems.append(f"{rel}: frontmatter sem {sorted(missing)}")

        # Entradas de referencia precisam mostrar a forma da construcao.
        if fm.get("category") in SYNTAX_CATEGORIES:
            syn = fm.get("syntax", "")
            if not syn:
                problems.append(f"{rel}: categoria '{fm['category']}' sem `syntax`")
            else:
                # "..." e legitimo dentro de [ ] (abrevia o interior de um
                # bloco) e em "END X". Nao e legitimo solto entre keywords,
                # onde substitui a estrutura que o leitor precisa ver.
                bare = re.sub(r"\[[^\]]*\]", "", syn)  # trechos opcionais
                # "X ... END X" abrevia o interior de um bloco delimitado.
                bare = re.sub(r"\.\.\.\s*END\s+\w+", "", bare)
                if "..." in bare:
                    problems.append(
                        f"{rel}: `syntax` usa '...' no lugar da estrutura "
                        f"(mostre as partes, entre [ ] se opcionais)"
                    )
            if "## Sintaxe" not in text and "## Syntax" not in text:
                problems.append(f"{rel}: sem secao Sintaxe no corpo")

        eid = fm.get("id")
        if not eid:
            continue
        if eid != md.stem:
            problems.append(f"{rel}: id '{eid}' difere do nome do arquivo")
        if eid in ids[locale]:
            problems.append(f"{rel}: id duplicado '{eid}'")
        ids[locale][eid] = md

        for target in parse_list(fm.get("see_also", "")):
            links.append((locale, eid, target, md))

    # 3. links resolvem
    for locale, src, target, path in links:
        if target not in ids[locale] and target not in ids[BASE_LOCALE]:
            problems.append(
                f"{path.relative_to(ROOT)}: see_also '{target}' nao existe"
            )

    # 4. paridade de locale
    base = set(ids.get(BASE_LOCALE, {}))
    for locale, entries in ids.items():
        if locale == BASE_LOCALE:
            continue
        for orphan in sorted(set(entries) - base):
            problems.append(f"{locale}/{orphan}: sem correspondente em {BASE_LOCALE}")

    total = sum(len(v) for v in ids.values())
    if problems:
        print(f"FALHOU: {len(problems)} problema(s) em {total} entries\n")
        for p in problems:
            print(f"  {p}")
        return 1

    print(f"OK: {total} entries validas")
    for locale, entries in sorted(ids.items()):
        by_cat: dict[str, int] = defaultdict(int)
        for eid, path in entries.items():
            fm = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
            by_cat[fm.get("category", "?")] += 1
        cats = ", ".join(f"{k}={v}" for k, v in sorted(by_cat.items()))
        print(f"  {locale}: {len(entries)} ({cats})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
