# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Gera o indice mestre do guia — o 'menu' no espirito do Norton Guides.

Uma linha por verbete: identificador, titulo e a frase de resumo. E a tela de
entrada da navegacao, e o unico lugar onde o guia inteiro cabe de uma vez.

Uso:
    python tools/generate_index.py
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "synesis_help" / "entries"
OUT = ROOT / "INDEX.md"

# Ordem de apresentacao: do panorama ao detalhe, erros por ultimo.
ORDER = [
    ("overview", "Panorama", "Comece por aqui."),
    ("block", "Blocos", "As estruturas da linguagem."),
    ("field_type", "Tipos de campo", "O que cada TYPE aceita."),
    ("modifier", "Modificadores", "Propriedades de campo e de projeto."),
    ("linkage", "Ligacao entre projetos", "IDENTIFIES e REFERS TO."),
    ("ecosystem", "Ecossistema", "As ferramentas ao redor da linguagem."),
    ("diagnostic", "Diagnosticos", "Todo erro, aviso e informacao do compilador."),
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def main() -> int:
    by_cat: dict[str, list[dict[str, str]]] = defaultdict(list)
    for md in sorted(ENTRIES.rglob("*.md")):
        fm = parse_frontmatter(md.read_text(encoding="utf-8"))
        if fm.get("id"):
            by_cat[fm.get("category", "?")].append(fm)

    total = sum(len(v) for v in by_cat.values())
    lines = [
        "# Guia Synesis — Indice",
        "",
        f"{total} verbetes. Consulta rapida da linguagem Synesis.",
        "",
        "> Gerado por `tools/generate_index.py`. Nao edite a mao.",
        "",
    ]

    for cat, title, blurb in ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines += [f"## {title}", "", f"*{blurb}*", ""]
        if cat == "diagnostic":
            lines += ["| Codigo | Situacao |", "|---|---|"]
            for fm in sorted(items, key=lambda x: x["id"]):
                sev = fm.get("severity", "")
                mark = {"Aviso": " ⚠", "Informacao": " ℹ"}.get(sev, "")
                lines.append(f"| [`{fm['id']}`]({fm['id']}){mark} | {fm.get('summary','')} |")
        else:
            lines += ["| Verbete | Descricao |", "|---|---|"]
            # Mesma ordem didatica da TUI: `order` primeiro, titulo no
            # empate. Alfabetico poria "Por onde comecar" em 4o lugar.
            key = lambda x: (int(x.get("order", 100)), x.get("title", ""))
            for fm in sorted(items, key=key):
                lines.append(
                    f"| [**{fm.get('title')}**]({fm['id']}) | {fm.get('summary','')} |"
                )
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Indice gerado: {OUT} ({total} verbetes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
