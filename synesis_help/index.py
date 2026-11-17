# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Compila as entries Markdown num indice SQLite com busca full-text.

E o equivalente moderno do arquivo .NG compilado: as entries vivem em Markdown
(faceis de editar e revisar), mas a consulta e feita sobre um indice binario
que abre instantaneamente e busca em milissegundos.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional

#: Ordem de apresentacao das categorias no painel esquerdo.
CATEGORY_ORDER = [
    ("overview", "Overview"),
    ("block", "Blocks"),
    ("field_type", "Field types"),
    ("modifier", "Modifiers"),
    ("linkage", "Linkage"),
    ("ecosystem", "Ecosystem"),
    ("diagnostic", "Diagnostics"),
]
CATEGORY_LABEL = dict(CATEGORY_ORDER)


@dataclass(frozen=True)
class Entry:
    id: str
    title: str
    category: str
    summary: str
    syntax: str
    body: str
    see_also: tuple[str, ...]
    source: str
    #: Posicao dentro da categoria. Menor vem primeiro; 100 e o padrao, e
    #: empate cai no alfabetico. Serve para que a ordem seja DIDATICA — do
    #: panorama ao detalhe — e nao alfabetica por acidente.
    order: int = 100

    @property
    def category_label(self) -> str:
        return CATEGORY_LABEL.get(self.category, self.category)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Devolve (metadados, corpo). Sem frontmatter, metadados vazios."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[3:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, text[end + 4 :].lstrip("\n")


_COMMENT = re.compile(r"<!--.*?-->\s*", re.DOTALL)


def _strip_comments(body: str) -> str:
    """Remove comentarios HTML — sao nota para quem edita, nao conteudo."""
    return _COMMENT.sub("", body).lstrip("\n")


def _parse_list(raw: str) -> tuple[str, ...]:
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:-1] if raw.endswith("]") else raw[1:]
    return tuple(x.strip().strip('"`') for x in raw.split(",") if x.strip())


def read_entries(root: Path) -> Iterator[Entry]:
    """Le as entries de disco, mesclando geradas e autorais pelo `id`.

    Uma entry autoral com o mesmo `id` de uma gerada substitui o corpo: e a
    camada de sobreposicao descrita no estudo (secao 4.3).
    """
    merged: dict[str, Entry] = {}
    # Geradas primeiro, autorais depois — as ultimas vencem.
    for sub in ("_generated", "authored"):
        base = root / sub
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            meta, body = _parse_frontmatter(md.read_text(encoding="utf-8"))
            eid = meta.get("id")
            if not eid:
                continue
            merged[eid] = Entry(
                id=eid,
                title=meta.get("title", eid),
                category=meta.get("category", "?"),
                summary=meta.get("summary", ""),
                syntax=meta.get("syntax", ""),
                body=_strip_comments(body),
                see_also=_parse_list(meta.get("see_also", "")),
                source=meta.get("source", "?"),
                order=int(meta.get("order", 100)),
            )
    yield from merged.values()


SCHEMA = """
CREATE TABLE entry (
    id        TEXT PRIMARY KEY,
    title     TEXT NOT NULL,
    category  TEXT NOT NULL,
    summary   TEXT,
    syntax    TEXT,
    body      TEXT,
    source    TEXT,
    "order"   INTEGER NOT NULL DEFAULT 100,
    locale    TEXT NOT NULL DEFAULT 'pt'
);
CREATE TABLE link (
    from_id TEXT NOT NULL,
    to_id   TEXT NOT NULL
);
CREATE INDEX idx_link_from ON link(from_id);
CREATE INDEX idx_entry_cat ON entry(category);
CREATE VIRTUAL TABLE entry_fts USING fts5(
    id UNINDEXED, title, summary, body,
    tokenize = 'unicode61 remove_diacritics 2'
);
"""


def build(entries_dir: Path, db_path: Path) -> int:
    """(Re)constroi o indice. Devolve o numero de entries gravadas."""
    if db_path.exists():
        try:
            db_path.unlink()
        except PermissionError as exc:  # pragma: no cover - Windows
            # No Windows o arquivo nao pode ser removido enquanto outra
            # instancia o mantem aberto (uma TUI rodando, por exemplo).
            raise RuntimeError(
                f"The index is in use and cannot be rebuilt:"
                f" {db_path}\nClose the guide (synesis-help) and try again."
            ) from exc
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    try:
        con.executescript(SCHEMA)
        rows = list(read_entries(entries_dir))
        con.executemany(
            'INSERT INTO entry (id,title,category,summary,syntax,body,'
            'source,"order") VALUES (?,?,?,?,?,?,?,?)',
            [
                (e.id, e.title, e.category, e.summary, e.syntax, e.body,
                 e.source, e.order)
                for e in rows
            ],
        )
        con.executemany(
            "INSERT INTO link (from_id,to_id) VALUES (?,?)",
            [(e.id, t) for e in rows for t in e.see_also],
        )
        con.executemany(
            "INSERT INTO entry_fts (id,title,summary,body) VALUES (?,?,?,?)",
            [(e.id, e.title, e.summary, e.body) for e in rows],
        )
        con.commit()
        return len(rows)
    finally:
        con.close()


class Guide:
    """Consulta somente-leitura sobre o indice compilado."""

    def __init__(self, db_path: Path) -> None:
        self.con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self.con.row_factory = sqlite3.Row

    def _entry(self, row: sqlite3.Row) -> Entry:
        see = [
            r["to_id"]
            for r in self.con.execute(
                "SELECT to_id FROM link WHERE from_id=?", (row["id"],)
            )
        ]
        return Entry(
            id=row["id"],
            title=row["title"],
            category=row["category"],
            summary=row["summary"] or "",
            syntax=row["syntax"] or "",
            body=row["body"] or "",
            see_also=tuple(see),
            source=row["source"] or "?",
            order=row["order"] if "order" in row.keys() else 100,
        )

    def categories(self) -> list[tuple[str, str, int]]:
        """(chave, rotulo, contagem) na ordem de apresentacao."""
        counts = {
            r["category"]: r["n"]
            for r in self.con.execute(
                "SELECT category, COUNT(*) n FROM entry GROUP BY category"
            )
        }
        return [
            (key, label, counts[key])
            for key, label in CATEGORY_ORDER
            if key in counts
        ]

    def by_category(self, category: str) -> list[Entry]:
        rows = self.con.execute(
            'SELECT * FROM entry WHERE category=? ORDER BY "order", title',
            (category,),
        )
        return [self._entry(r) for r in rows]

    def get(self, entry_id: str) -> Optional[Entry]:
        row = self.con.execute(
            "SELECT * FROM entry WHERE id=?", (entry_id,)
        ).fetchone()
        return self._entry(row) if row else None

    def search(self, query: str, limit: int = 60) -> list[Entry]:
        """Busca full-text. Termos parciais casam por prefixo."""
        query = query.strip()
        if not query:
            return []
        # Cada termo vira prefixo, para busca incremental enquanto digita.
        terms = " ".join(f'"{t}"*' for t in re.findall(r"\w+", query))
        if not terms:
            return []
        # Quem procura "chain" quer o verbete CHAIN, nao o erro que mais
        # repete a palavra. Casamento no titulo/id vem primeiro; so depois
        # entra o ranking de relevancia do FTS.
        like = f"{query.lower()}%"
        try:
            rows = self.con.execute(
                "SELECT e.* FROM entry_fts f JOIN entry e ON e.id=f.id"
                " WHERE entry_fts MATCH ?"
                " ORDER BY"
                "   CASE WHEN lower(e.title) = ? THEN 0"
                "        WHEN lower(e.title) LIKE ? THEN 1"
                "        WHEN lower(e.id) LIKE ? THEN 2"
                "        ELSE 3 END,"
                "   rank"
                " LIMIT ?",
                (terms, query.lower(), like, like, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            return []
        return [self._entry(r) for r in rows]

    def total(self) -> int:
        return self.con.execute("SELECT COUNT(*) FROM entry").fetchone()[0]

    def close(self) -> None:
        self.con.close()
