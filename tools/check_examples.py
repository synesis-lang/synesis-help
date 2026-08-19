# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Compila os exemplos das entries contra o compilador instalado.

Secao 5.4 do estudo: e onde o conteudo autoral apodrece. Uma regra nova no
compilador invalida em silencio um exemplo escrito meses antes.

Verifica dois formatos:
  - templates completos (comecam com TEMPLATE), compilados como estao;
  - fragmentos `FIELD ... END FIELD`, embrulhados num template minimo.

Fragmentos de .synp/.syn/.syno e formas esquematicas (com `<placeholder>`) sao
contados como nao verificaveis — honestidade e melhor que falso verde.

Uso:
    python tools/check_examples.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from synesis.parser.template_loader import load_template_from_string, validate_template

ROOT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries"
FENCE = re.compile(r"```synesis\n(.*?)```", re.DOTALL)

#: Largura maxima de uma linha de exemplo. Blocos sao lidos num painel de
#: terminal: passar disso quebra a linha ou exige rolagem horizontal, e o
#: recuo deixa de comunicar a estrutura.
MAX_WIDTH = 72
INDENT = 4


def check_style(src: str) -> list[str]:
    """Problemas de apresentacao — nao de sintaxe."""
    issues: list[str] = []
    for n, line in enumerate(src.split("\n"), 1):
        if not line.strip():
            continue
        if "\t" in line:
            issues.append(f"linha {n}: TAB (use {INDENT} espacos)")
        if len(line) > MAX_WIDTH:
            issues.append(f"linha {n}: {len(line)} colunas (max {MAX_WIDTH})")
        if line.rstrip() != line:
            issues.append(f"linha {n}: espaco no fim")
        indent = len(line) - len(line.lstrip())
        if indent % INDENT:
            issues.append(f"linha {n}: recuo {indent} nao e multiplo de {INDENT}")
    return issues


def main() -> int:
    checked = skipped = 0
    failures: list[tuple[str, str]] = []

    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT)
        for block in FENCE.findall(md.read_text(encoding="utf-8")):
            src = block.strip()

            # Estilo vale para todo bloco, inclusive os esquematicos:
            # legibilidade nao depende de o exemplo ser compilavel.
            for issue in check_style(src):
                failures.append((str(rel), f"estilo — {issue}"))

            if "<" in src and ">" in src:
                skipped += 1  # forma esquematica (<nome>, <TIPO>), nao codigo real
                continue
            if src.startswith("FIELD "):
                # Fragmento: embrulha num template minimo para poder compilar.
                name_match = re.match(r"FIELD\s+(\w+)", src)
                if not name_match:
                    skipped += 1
                    continue
                field = name_match.group(1)
                scope_match = re.search(r"SCOPE\s+(\w+)", src)
                scope = scope_match.group(1) if scope_match else "ITEM"
                src = (
                    f"TEMPLATE conformance\n"
                    f"{scope} FIELDS\n    REQUIRED {field}\nEND {scope} FIELDS\n"
                    f"{src}"
                )
            elif not src.startswith("TEMPLATE"):
                skipped += 1
                continue
            checked += 1
            try:
                result = validate_template(load_template_from_string(src))
                codes = [e.CODE for e in result.errors]
                if codes:
                    failures.append((str(rel), ", ".join(codes)))
            except Exception as exc:  # noqa: BLE001
                failures.append((str(rel), f"{type(exc).__name__}: {exc}"))

    if failures:
        print(f"FALHOU: {len(failures)} exemplo(s) nao compilam\n")
        for path, err in failures:
            print(f"  {path}: {err}")
        return 1

    print(f"OK: {checked} exemplo(s) compilam limpos ({skipped} nao verificaveis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
