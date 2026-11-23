# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""The JSON contract agents rely on: keys, versions, matches and exit codes."""

from __future__ import annotations

import json

import pytest

from synesis_help.cli import EXIT_FOUND, EXIT_NOT_FOUND, EXIT_USAGE, main
from synesis_help.texts import __version__

ENVELOPE = {"help_version", "synesis_version", "locale"}
BRIEF = {"id", "title", "category", "summary", "syntax"}


def _json(capsys, argv: list[str]) -> tuple[int, dict]:
    code = main(argv)
    return code, json.loads(capsys.readouterr().out)


def test_lookup_by_id_carries_versions_and_full_entry(capsys) -> None:
    code, data = _json(capsys, ["lookup", "TYPE_CHAIN", "--format=json"])
    assert code == EXIT_FOUND
    assert ENVELOPE | BRIEF | {"body", "see_also", "found", "match", "query"} <= set(data)
    assert data["help_version"] == __version__
    assert data["synesis_version"]  # derived from the generated entries
    assert data["locale"] == "en"
    assert data["id"] == "TYPE_CHAIN" and data["match"] == "id"


@pytest.mark.parametrize("term,expected,how", [
    ("E047", "SYNESIS_E047", "prefix"),
    ("chain", "TYPE_CHAIN", "title"),
    ("export", "BLOCK_EXPORT", "title"),
])
def test_lookup_short_forms(capsys, term, expected, how) -> None:
    code, data = _json(capsys, ["lookup", term, "--format=json"])
    assert code == EXIT_FOUND
    assert data["id"] == expected and data["match"] == how


def test_lookup_not_found_exits_1_with_suggestions_shape(capsys) -> None:
    code, data = _json(capsys, ["lookup", "qqzzxx", "--format=json"])
    assert code == EXIT_NOT_FOUND
    assert data["found"] is False and isinstance(data["suggestions"], list)


def test_syntax_has_no_escaped_quotes(capsys) -> None:
    """The frontmatter escapes quotes; the contract must not carry the backslashes."""
    _code, data = _json(capsys, ["lookup", "BLOCK_EXPORT", "--format=json"])
    assert '\\"' not in data["syntax"] and 'OUTPUT "<file>"' in data["syntax"]


def test_search_finds_case_studies(capsys) -> None:
    code, data = _json(capsys, ["search", "bundle", "status", "--format=json"])
    assert code == EXIT_FOUND
    assert ENVELOPE | {"query", "count", "results"} <= set(data)
    ids = [r["id"] for r in data["results"]]
    assert "CASE_LITERATURE_REVIEW" in ids
    assert all(BRIEF <= set(r) for r in data["results"])


def test_search_nothing_exits_1(capsys) -> None:
    code, data = _json(capsys, ["search", "qqzzxx", "--format=json"])
    assert code == EXIT_NOT_FOUND and data["count"] == 0


def test_list_category(capsys) -> None:
    code, data = _json(capsys, ["list", "--category", "case_study", "--format=json"])
    assert code == EXIT_FOUND
    assert data["count"] == len(data["entries"]) >= 9
    assert {c["key"] for c in data["categories"]} >= {"case_study", "diagnostic"}


def test_list_unknown_category_is_usage_error(capsys) -> None:
    assert main(["list", "--category", "nope"]) == EXIT_USAGE


def test_every_case_study_names_no_real_project() -> None:
    """Case studies describe designs, not who used them."""
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent / "synesis_help" / "entries" / "authored" / "en"
    for md in root.glob("CASE_*.md"):
        text = md.read_text(encoding="utf-8")
        assert "fictitious" in text.lower(), f"{md.name}: must say its data is fictitious"
