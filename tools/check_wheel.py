# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Confere que as entries entraram no wheel construido.

As entries SAO o produto. Um wheel sem elas instala sem erro, o comando abre
sem erro, e o guia responde "nada encontrado" para tudo — falha silenciosa,
que e a pior classe. E exatamente o que uma refatoracao do `package-data` no
pyproject.toml pode perder sem que nenhum teste perceba.

Uso:
    python tools/check_wheel.py            # procura em dist/
    python tools/check_wheel.py caminho.whl
"""

from __future__ import annotations

import glob
import sys
import zipfile
from pathlib import Path

#: Piso deliberadamente folgado: o objetivo e pegar "zero" ou "quase nada",
#: nao cravar a contagem exata — esta cresce a cada verbete novo, e um numero
#: exato aqui viraria uma segunda fonte de verdade a manter.
MIN_ENTRIES = 100


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    wheels = args or sorted(glob.glob("dist/*.whl"))
    if not wheels:
        print("ERRO: nenhum wheel encontrado em dist/", file=sys.stderr)
        return 1

    wheel = Path(wheels[0])
    names = zipfile.ZipFile(wheel).namelist()
    entries = [n for n in names if "/entries/" in n and n.endswith(".md")]

    print(f"{wheel.name}: {len(entries)} verbetes")
    if len(entries) < MIN_ENTRIES:
        print(
            f"ERRO: o wheel traz {len(entries)} verbetes; esperado {MIN_ENTRIES}+."
            "\nVerifique `[tool.setuptools.package-data]` no pyproject.toml.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
