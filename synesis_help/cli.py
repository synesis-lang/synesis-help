# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Command line of synesis-help.

Two audiences, one index:
- people open the keyboard-driven guide (no arguments);
- agents and scripts use `lookup`, `search` and `list` with `--format=json`.

JSON contract (stable keys) and exit codes: 0 found, 1 not found, 2 usage error.
Every JSON answer carries `help_version`, `synesis_version` (the compiler the
generated entries were derived from) and `locale`.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from .index import CATEGORY_LABEL, CATEGORY_ORDER, Entry, Guide, build
from .texts import CREDITS, EPILOG, WRITING_GUIDE, __version__

PKG = Path(__file__).resolve().parent
ENTRIES = PKG / "entries"
#: The index ships with the package. On a read-only install it falls back to
#: the user cache directory.
DB = PKG / "data" / "guide.db"

EXIT_FOUND, EXIT_NOT_FOUND, EXIT_USAGE = 0, 1, 2


def _user_db() -> Path:
    """Index in the user cache (stdlib only)."""
    base = os.environ.get("XDG_CACHE_HOME") or os.environ.get("LOCALAPPDATA")
    root = Path(base) if base else Path.home() / ".cache"
    return root / "synesis-help" / "guide.db"


def _ensure_db() -> Path:
    """A usable index, built on first run (or rebuilt if it predates the package)."""
    for candidate in (DB, _user_db()):
        if candidate.exists() and _current(candidate):
            return candidate
    try:
        build(ENTRIES, DB)
        return DB
    except (OSError, RuntimeError):
        fallback = _user_db()
        build(ENTRIES, fallback)
        return fallback


def _current(db: Path) -> bool:
    """False when the index lacks the metadata of this version (built by an older one)."""
    try:
        guide = Guide(db)
    except Exception:  # noqa: BLE001
        return False
    try:
        return guide.meta("locale") == "en"
    finally:
        guide.close()


def _envelope(guide: Guide) -> dict[str, Any]:
    return {
        "help_version": __version__,
        "synesis_version": guide.meta("synesis_version"),
        "locale": "en",
    }


def _brief(entry: Entry) -> dict[str, Any]:
    return {
        "id": entry.id,
        "title": entry.title,
        "category": entry.category,
        "summary": entry.summary,
        "syntax": entry.syntax,
    }


def _full(entry: Entry) -> dict[str, Any]:
    return {**_brief(entry), "body": entry.body, "see_also": list(entry.see_also)}


def _print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def _suggest(guide: Guide, term: str, exclude: str = "") -> list[Entry]:
    return [e for e in guide.search_any(term, limit=6) if e.id != exclude][:5]


def _cmd_lookup(guide: Guide, term: str, fmt: str) -> int:
    entry, how = guide.find(term)
    if entry is None:
        suggestions = _suggest(guide, term)
        if fmt == "json":
            _print_json({**_envelope(guide), "query": term, "found": False,
                         "suggestions": [_brief(e) for e in suggestions]})
        else:
            print(f"Nothing found for '{term}'.", file=sys.stderr)
            if suggestions:
                print("Did you mean:", file=sys.stderr)
                for e in suggestions:
                    print(f"  {e.id:<24} {e.summary}", file=sys.stderr)
        return EXIT_NOT_FOUND
    if fmt == "json":
        payload = {**_envelope(guide), "query": term, "found": True, "match": how, **_full(entry)}
        if how == "search":
            payload["suggestions"] = [_brief(e) for e in _suggest(guide, term, exclude=entry.id)]
        _print_json(payload)
    else:
        print(f"{entry.title}  [{entry.id} · {entry.category_label}]")
        print("-" * len(entry.title))
        if entry.syntax:
            print(f"\n  {entry.syntax}\n")
        print(entry.body)
    return EXIT_FOUND


def _cmd_search(guide: Guide, query: str, fmt: str, limit: int) -> int:
    results = guide.search(query, limit=limit) or guide.search_any(query, limit=limit)
    if fmt == "json":
        _print_json({**_envelope(guide), "query": query, "count": len(results),
                     "results": [_brief(e) for e in results]})
    elif results:
        for e in results:
            print(f"{e.id:<26} {e.category_label:<13} {e.summary}")
    else:
        print(f"Nothing found for '{query}'.", file=sys.stderr)
    return EXIT_FOUND if results else EXIT_NOT_FOUND


def _cmd_list(guide: Guide, category: str | None, fmt: str) -> int:
    if category and category not in CATEGORY_LABEL:
        known = ", ".join(k for k, _l in CATEGORY_ORDER)
        print(f"Unknown category '{category}'. Known: {known}.", file=sys.stderr)
        return EXIT_USAGE
    entries = guide.all(category)
    if fmt == "json":
        cats = [{"key": k, "label": label, "count": n} for k, label, n in guide.categories()]
        _print_json({**_envelope(guide), "categories": cats,
                     "count": len(entries), "entries": [_brief(e) for e in entries]})
    else:
        current = None
        for e in entries:
            if e.category != current:
                current = e.category
                print(f"\n{e.category_label}")
            print(f"  {e.id:<26} {e.summary}")
    return EXIT_FOUND


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="synesis-help",
        description="Quick reference guide to the Synesis language, for people and agents.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--version", action="version", version=f"synesis-help {__version__}")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("build", help="compile the entries into the SQLite index")

    fmt_help = "json is the stable contract for agents and scripts"
    p_lookup = sub.add_parser("lookup", help="show one entry (ID, title or term)")
    p_lookup.add_argument("term", help="entry ID (SYNESIS_E047, TYPE_CHAIN), its short form (E047) or a word")
    p_lookup.add_argument("--format", choices=("text", "json"), default="text", help=fmt_help)

    p_search = sub.add_parser("search", help="full-text search over all entries")
    p_search.add_argument("query", nargs="+", help="words to look for")
    p_search.add_argument("--format", choices=("text", "json"), default="text", help=fmt_help)
    p_search.add_argument("--limit", type=int, default=10, help="maximum results (default 10)")

    p_list = sub.add_parser("list", help="list the entries, optionally of one category")
    p_list.add_argument("--category", help="overview, block, field_type, modifier, linkage, "
                                           "case_study, ecosystem or diagnostic")
    p_list.add_argument("--format", choices=("text", "json"), default="text", help=fmt_help)

    sub.add_parser("docs", help="how to write and fix entries")
    sub.add_parser("credits", help="authorship, license and how to cite")

    args = ap.parse_args(argv)

    if args.cmd == "docs":
        print(WRITING_GUIDE)
        return EXIT_FOUND
    if args.cmd == "credits":
        print(CREDITS)
        return EXIT_FOUND
    if args.cmd == "build":
        try:
            n = build(ENTRIES, DB)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return EXIT_NOT_FOUND
        print(f"Index compiled: {DB} ({n} entries)")
        return EXIT_FOUND

    if args.cmd in ("lookup", "search", "list"):
        guide = Guide(_ensure_db())
        try:
            if args.cmd == "lookup":
                return _cmd_lookup(guide, args.term, args.format)
            if args.cmd == "search":
                return _cmd_search(guide, " ".join(args.query), args.format, max(1, args.limit))
            return _cmd_list(guide, args.category, args.format)
        finally:
            guide.close()

    # No subcommand: open the TUI.
    from .app import run

    run(_ensure_db())
    return EXIT_FOUND


if __name__ == "__main__":
    sys.exit(main())
