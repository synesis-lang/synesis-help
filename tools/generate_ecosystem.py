# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Gera os verbetes dos modulos do ecossistema a partir do `--help` deles.

Mesma disciplina dos demais geradores: a fonte e a ferramenta instalada, nao
uma transcricao que envelhece. Se o `synesis-coder` ganha um subcomando, ele
aparece aqui na proxima regeneracao.

O que NAO entra: caminhos locais, versoes de interpretador e qualquer coisa
que descreva a maquina de quem gerou — isso mudaria a cada execucao e nao
interessa a quem le o guia.

Uso:
    python tools/generate_ecosystem.py
    python tools/generate_ecosystem.py --check
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries"
OUT = OUT / "_generated" / "en"

#: Modules of the ecosystem, in the order they meet in the workflow.
MODULES = [
    {
        "id": "ECO_SYNESIS",
        "cmd": "synesis",
        "title": "synesis",
        "role": "compiler",
        "order": 10,
        "summary": "The language compiler: validates, compiles and exports.",
        "note": (
            "The core of the ecosystem. Every other module depends on it, and "
            "none reimplements its rules. `synesis compile` validates a project; "
            "`synesis export` runs the `EXPORT` blocks of the `.synp`."
        ),
    },
    {
        "id": "ECO_LSP",
        "cmd": "synesis-lsp",
        "title": "synesis-lsp",
        "role": "language server",
        "order": 20,
        "has_subcommands": False,
        "summary": "LSP server: highlighting, hover, completion and navigation.",
        "note": (
            "Not run by hand: the editor starts it. Install it and the VS Code "
            "extension finds it by itself."
        ),
    },
    {
        "id": "ECO_CODER",
        "cmd": "synesis-coder",
        "title": "synesis-coder",
        "role": "AI-assisted annotation",
        "order": 30,
        "summary": "Writes valid annotations from text, guided by the template.",
        "note": (
            "The template defines the fields and their constraints; nothing is "
            "fixed in code. The quality of the result depends on what you write "
            "in `GUIDELINES`. The coder reads the `.env` of the project folder "
            "(model, keys, `SYNESIS_CODER_LANGUAGE`)."
        ),
    },
    {
        "id": "ECO_GRAPH",
        "cmd": "synesis-graph",
        "title": "synesis-graph",
        "role": "graph export",
        "order": 40,
        "summary": "Turns compiled projects into graph databases and visualizations.",
        "note": (
            "Consumes the artifact of `synesis compile`, not the `.syn` files.\n\n"
            "**The exported graph describes itself.** When syncing with a database "
            "(ArcadeDB or Neo4j), `synesis-graph` writes a `ProjectContext` vertex "
            "with the context of the project: the `DESCRIPTION` of the `.synp` and "
            "the whole template as a readable document (each field with type, "
            "scope, description, value scale and **GUIDELINES**), plus the graph "
            "edges with their direction.\n\n"
            "A database schema is syntax without semantics: it says there is an "
            "`Aspect` vertex with a `name`, not that `Aspect` is an ordered scale "
            "or what each value means. Your `GUIDELINES` are your coding protocol. "
            "With them in the graph, whoever queries it (Claude Desktop, any MCP "
            "client, the database studio, a colleague with a copy) knows your "
            "criteria instead of guessing them.\n\n"
            "To read it: `MATCH (p:ProjectContext) RETURN p.description, "
            "p.template_doc`."
        ),
    },
    {
        "id": "ECO_HELP",
        "cmd": "synesis-help",
        "title": "synesis-help",
        "role": "reference guide (people and agents)",
        "order": 50,
        "summary": "This guide: TUI for people, JSON lookup and search for agents.",
        "note": (
            "Run without arguments for the keyboard-driven guide. Agents and "
            "scripts use the JSON contract:\n\n"
            "- `synesis-help search <words> --format=json` finds entries by text;\n"
            "- `synesis-help lookup <ID or term> --format=json` returns one entry "
            "(with suggestions when nothing matches exactly);\n"
            "- `synesis-help list [--category <name>] --format=json` shows what "
            "exists.\n\n"
            "Exit codes: 0 found, 1 not found, 2 usage error. Every JSON answer "
            "carries `help_version` and `synesis_version` (the compiler the "
            "generated entries were derived from), so an agent can tell whether "
            "the guide matches the installed compiler."
        ),
    },
]

#: Linhas do `--help` que descrevem a MAQUINA, nao a ferramenta.
_LOCAL = re.compile(
    r"^\s*(Interpreter|Core Module|Runtime Environment|Python \d)",
    re.IGNORECASE,
)
_PATHY = re.compile(r"[A-Za-z]:\\|/home/|/usr/|site-packages")

#: Valores que a ferramenta resolve do AMBIENTE (variavel, `.env`) e imprime
#: na ajuda como se fossem proprios. `synesis-coder --help` mostra
#: "(Current: <modelo>)", que e o modelo configurado NESTA maquina — nao um
#: padrao do pacote. Sem esta substituicao o verbete publicaria a configuracao
#: de quem gerou, e mudaria a cada regeneracao em maquina diferente.
_ENV_VALUE = re.compile(r"\(Current: [^)]*\)")
_ENV_PLACEHOLDER = "(Current: set by SYNESIS_CODER_MODEL)"


def redact_env(line: str) -> str:
    """Troca valor vindo do ambiente por como se define esse valor."""
    return _ENV_VALUE.sub(_ENV_PLACEHOLDER, line)


def capture(cmd: str) -> tuple[str, str] | None:
    """Roda `cmd --help` e devolve (versao, corpo util)."""
    if shutil.which(cmd) is None:
        return None
    try:
        proc = subprocess.run(
            [cmd, "--help"], capture_output=True, text=True, timeout=60,
            encoding="utf-8", errors="replace",
            # `stdin` fechado: o language server passa a ouvir a entrada
            # padrao logo apos imprimir a ajuda e, sem isto, fica bloqueado
            # ate o timeout — falha intermitente, conforme o terminal.
            stdin=subprocess.DEVNULL,
        )
    except (OSError, subprocess.SubprocessError):
        return None

    raw = (proc.stdout or "") + (proc.stderr or "")
    if not raw.strip():
        return None

    version = ""
    kept: list[str] = []
    for line in raw.splitlines():
        if not version:
            m = re.search(r"\(v([\d.]+)\)", line)
            if m:
                version = m.group(1)
        # Descarta o que descreve a maquina de quem gerou.
        if _LOCAL.match(line) or _PATHY.search(line):
            continue
        # Copyright e licenca ja vivem na pagina de creditos.
        if re.match(r"^\s*(Copyright|Licensed under|https://)", line):
            continue
        # Ruido de execucao: o servidor comeca a servir ao ser invocado.
        if re.match(r"^\s*\[(INFO|DEBUG|WARNING)\]", line):
            continue
        kept.append(redact_env(line.rstrip()))

    # Remove o cabecalho de titulo (o verbete ja tem o seu) e linhas vazias
    # em excesso.
    while kept and (not kept[0].strip() or kept[0].isupper()):
        kept.pop(0)
    body: list[str] = []
    for line in kept:
        if not line.strip() and body and not body[-1].strip():
            continue
        body.append(line)
    return version, "\n".join(body).strip()


def build_entry(mod: dict, version: str, help_text: str) -> str:
    see = [m["id"] for m in MODULES if m["id"] != mod["id"]][:3]
    see.append("GUIDE_ECOSYSTEM")
    header = [
        "---",
        f"id: {mod['id']}",
        f'title: "{mod["title"]}"',
        "category: ecosystem",
        f'summary: "{mod["summary"]}"',
        f"see_also: [{', '.join(see)}]",
        "source: generated",
        f"order: {mod['order']}",
    ]
    if version:
        header.append(f'version: "{version}"')
    header.append("---")

    parts = [
        "\n".join(header),
        "",
        "<!-- GENERATED by tools/generate_ecosystem.py. Do not edit. -->",
        "",
        f"# {mod['title']}",
        "",
        "## Description",
        "",
        f"Role in the ecosystem: **{mod['role']}**"
        + (f" · version {version}" if version else ""),
        "",
        mod["note"],
        "",
        "## Usage",
        "",
        "```text",
        help_text,
        "```",
        "",
        (
            f"For the options of a subcommand: `{mod['cmd']} <command>"
            " --help`."
            if mod.get("has_subcommands", True)
            else "Single executable, no subcommands: the editor starts it."
        ),
        "",
    ]
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    entries: dict[str, str] = {}
    missing: list[str] = []
    for mod in MODULES:
        got = capture(mod["cmd"])
        if got is None:
            missing.append(mod["cmd"])
            continue
        version, help_text = got
        entries[mod["id"]] = build_entry(mod, version, help_text)

    if missing:
        print(f"WARNING: not installed, entry not generated: {', '.join(missing)}")

    OUT.mkdir(parents=True, exist_ok=True)
    if args.check:
        drift = [
            eid for eid, content in entries.items()
            if not (OUT / f"{eid}.md").exists()
            or (OUT / f"{eid}.md").read_text(encoding="utf-8") != content
        ]
        if drift:
            print(f"DRIFT: {len(drift)} entr(ies): {', '.join(drift)}")
            return 1
        print(f"OK: {len(entries)} ecosystem entries in sync")
        return 0

    for eid, content in entries.items():
        (OUT / f"{eid}.md").write_text(content, encoding="utf-8")
    print(f"Generated {len(entries)} ecosystem entries in {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
