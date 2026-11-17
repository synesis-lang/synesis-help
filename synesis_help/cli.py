# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Interface de linha de comando do synesis-help."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from .index import Guide, build
from .texts import CREDITS, EPILOG, WRITING_GUIDE, __version__

PKG = Path(__file__).resolve().parent
ENTRIES = PKG / "entries"
#: O indice acompanha o pacote. Se o diretorio for somente-leitura (instalacao
#: de sistema), cai para o diretorio de cache do usuario.
DB = PKG / "data" / "guide.db"


def _user_db() -> Path:
    """Indice no cache do usuario (stdlib apenas, sem dependencia extra)."""
    base = os.environ.get("XDG_CACHE_HOME") or os.environ.get("LOCALAPPDATA")
    root = Path(base) if base else Path.home() / ".cache"
    return root / "synesis-help" / "guide.db"


def _ensure_db() -> Path:
    """Devolve um indice utilizavel, construindo-o na primeira execucao."""
    if DB.exists():
        return DB
    try:
        build(ENTRIES, DB)
        return DB
    except OSError:
        # Instalacao somente-leitura: constroi no cache do usuario.
        fallback = _user_db()
        if not fallback.exists():
            build(ENTRIES, fallback)
        return fallback


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="synesis-help",
        description="Quick reference guide to the Synesis language.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--version", action="version", version=f"synesis-help {__version__}"
    )
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("build", help="compile the entries into the SQLite index")

    p_lookup = sub.add_parser("lookup", help="look up an entry")
    p_lookup.add_argument("termo", metavar="term")
    p_lookup.add_argument(
        "--format", choices=("text", "json"), default="text",
        help="json exposes the external invocation contract",
    )

    sub.add_parser("docs", help="how to write and fix entries")
    sub.add_parser("credits", help="authorship, license and how to cite")

    args = ap.parse_args(argv)

    if args.cmd == "docs":
        print(WRITING_GUIDE)
        return 0

    if args.cmd == "credits":
        print(CREDITS)
        return 0

    if args.cmd == "build":
        try:
            n = build(ENTRIES, DB)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(f"Index compiled: {DB} ({n} entries)")
        return 0

    if args.cmd == "lookup":
        guide = Guide(_ensure_db())
        entry = guide.get(args.termo) or next(iter(guide.search(args.termo)), None)
        if entry is None:
            print(f"Nothing found for '{args.termo}'.", file=sys.stderr)
            return 1
        if args.format == "json":
            print(json.dumps({
                "id": entry.id,
                "title": entry.title,
                "category": entry.category,
                "locale": "pt",
                "summary": entry.summary,
                "syntax": entry.syntax,
                "body": entry.body,
                "see_also": list(entry.see_also),
            }, ensure_ascii=False, indent=2))
        else:
            print(f"{entry.title}\n{'-' * len(entry.title)}")
            if entry.syntax:
                print(f"\n  {entry.syntax}\n")
            print(entry.body)
        return 0

    # Sem subcomando: abre a TUI.
    from .app import run

    run(_ensure_db())
    return 0


if __name__ == "__main__":
    sys.exit(main())
