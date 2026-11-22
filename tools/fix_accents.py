# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Restaura a acentuacao da prosa das entries.

O conteudo autoral foi escrito sem acentos. Isto corrige a prosa **sem tocar
no codigo**: blocos cercados, trechos entre crases, frontmatter tecnico,
identificadores e nomes de campo permanecem exatamente como estao — um acento
dentro de um exemplo o tornaria invalido.

Usa o dicionario portugues do `pyspellchecker`: palavras que existem em
portugues (`esta`, `e`, `tem`, `para`) nao sao mexidas, o que evita o erro
classico de trocar a conjuncao "e" pelo verbo "é".

Uso:
    python tools/fix_accents.py --check    # relata, nao grava
    python tools/fix_accents.py            # grava
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from spellchecker import SpellChecker

#: Apenas a camada autoral. As entries geradas reproduzem a prosa do
#: compilador (`to_diagnostic()`), que hoje tambem e sem acento — corrigi-las
#: aqui criaria uma segunda verdade e a regeneracao desfaria o trabalho.
#: A acentuacao de `results.py` e projeto do compilador, nao deste guia.
ROOT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries" / "authored"

#: Termos do dominio que o dicionario nao conhece e nao deve "corrigir".
KEEP = {
    "synesis", "template", "templates", "bibref", "bibrefs", "bibtex",
    "toml", "json", "sqlite", "id", "ids", "lattes", "linkedin", "github",
    "slug", "slugs", "dataset", "datasets", "commit", "wheel", "pip",
    "markdown", "frontmatter", "parser", "linker", "lark", "enum",
    "grounded", "theory", "process", "tracing", "frames", "knowledge",
    "graph", "workspace", "arity", "scope", "chain", "chains", "code",
    "codes", "item", "items", "source", "sources", "ontology", "project",
    "field", "fields", "values", "relations", "format", "guidelines",
    "description", "metadata", "include", "shared", "bundle", "required",
    "optional", "forbidden", "identifies", "refers", "quotation", "memo",
    "text", "date", "scale", "enumerated", "ordered", "topic", "end",
    "on", "bibliography", "annotations", "from", "context", "type",
}

#: Trechos que nao podem ser tocados: codigo, marcacao, identificadores.
#: O frontmatter NAO entra inteiro: `summary` e `title` sao prosa exibida ao
#: usuario e precisam de acento. Protegidos sao os campos tecnicos (`id`,
#: `see_also`, `syntax`), linha a linha.
_PROTECTED = re.compile(
    r"```.*?```"          # blocos de codigo
    r"|`[^`]*`"           # codigo inline
    # `[^\n]*` e nao `.*`: DOTALL faz o ponto casar com quebra de linha e a
    # protecao engoliria o frontmatter inteiro.
    r"|^(?:id|category|source|see_also|syntax|file|severity"
    r"|requires_synesis):[^\n]*"  # campos tecnicos do frontmatter
    r"|\[\[?[^\]]*\]\]?"  # links e rotulos
    r"|\b[A-Z][A-Z0-9_]{2,}\b"  # SYNESIS_E047, ONTOLOGY, REDE_APOIO
    r"|\b\w+\.(syn|synt|syno|synp|bib|toml|md|py)\b"  # nomes de arquivo
    r"|@[\w:-]+",         # bibrefs
    re.DOTALL | re.MULTILINE,
)

_WORD = re.compile(r"\b[a-zà-ÿ]+\b", re.IGNORECASE)


def fix_prose(text: str, checker: SpellChecker) -> tuple[str, int]:
    """Corrige a prosa, preservando os trechos protegidos."""
    changes = 0

    def fix_chunk(chunk: str) -> str:
        def fix_word(m: re.Match[str]) -> str:
            nonlocal changes
            word = m.group()
            low = word.lower()
            if low in KEEP or len(low) < 3:
                return word
            # Ja tem acento, ou e palavra portuguesa valida: nao mexe.
            if any(ord(c) > 127 for c in word) or low in checker:
                return word
            fixed = checker.correction(low)
            if not fixed or fixed == low:
                return word
            # So aceita a sugestao se for a MESMA palavra acentuada —
            # nunca uma troca por outra palavra ("template" -> "empate").
            if _strip(fixed) != low:
                return word
            changes += 1
            if word.isupper():
                return fixed.upper()
            if word[0].isupper():
                return fixed.capitalize()
            return fixed

        return _WORD.sub(fix_word, chunk)

    out: list[str] = []
    pos = 0
    for m in _PROTECTED.finditer(text):
        out.append(fix_chunk(text[pos : m.start()]))
        out.append(m.group())
        pos = m.end()
    out.append(fix_chunk(text[pos:]))
    return "".join(out), changes


def _strip(word: str) -> str:
    """Remove acentos, para comparar 'nao' com 'não'."""
    import unicodedata

    norm = unicodedata.normalize("NFKD", word)
    return "".join(c for c in norm if not unicodedata.combining(c))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="relata, nao grava")
    args = ap.parse_args()

    checker = SpellChecker(language="pt")
    total = touched = 0

    for md in sorted(ROOT.rglob("*.md")):
        original = md.read_text(encoding="utf-8")
        fixed, n = fix_prose(original, checker)
        if n:
            total += n
            touched += 1
            if not args.check:
                md.write_text(fixed, encoding="utf-8")
            print(f"  {md.relative_to(ROOT)}: {n} palavra(s)")

    verb = "seriam corrigidas" if args.check else "corrigidas"
    print(f"\n{total} palavra(s) {verb} em {touched} arquivo(s).")
    return 1 if (args.check and total) else 0


if __name__ == "__main__":
    sys.exit(main())
