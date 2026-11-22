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
OUT = OUT / "_generated" / "pt"

#: Modulos do ecossistema, na ordem em que se encontram no fluxo de trabalho.
MODULES = [
    {
        "id": "ECO_SYNESIS",
        "cmd": "synesis",
        "title": "synesis",
        "role": "compilador",
        "order": 10,
        "summary": "Compilador da linguagem: valida, compila e exporta.",
        "note": (
            "E o nucleo do ecossistema. Todos os outros modulos dependem "
            "dele, e nenhum reimplementa suas regras."
        ),
    },
    {
        "id": "ECO_LSP",
        "cmd": "synesis-lsp",
        "title": "synesis-lsp",
        "role": "language server",
        "order": 20,
        "has_subcommands": False,
        "summary": "Servidor LSP: realce, hover, autocomplete e navegacao.",
        "note": (
            "Nao e chamado a mao: o editor o inicia. Instale-o e a extensao "
            "do VS Code o encontra sozinha."
        ),
    },
    {
        "id": "ECO_CODER",
        "cmd": "synesis-coder",
        "title": "synesis-coder",
        "role": "anotacao assistida por IA",
        "order": 30,
        "summary": "Gera anotacoes validas a partir de texto, guiado pelo template.",
        "note": (
            "O template define os campos e as restricoes — nada e fixo no "
            "codigo. A qualidade do resultado depende do que voce escreve em "
            "`GUIDELINES`."
        ),
    },
    {
        "id": "ECO_GRAPH",
        "cmd": "synesis-graph",
        "title": "synesis-graph",
        "role": "exportacao para grafos",
        "order": 40,
        "summary": "Converte projetos compilados em bancos de grafo e visualizacoes.",
        "note": (
            "Consome o artefato do `synesis compile`, nao os `.syn` diretamente.\n\n"
            "**O grafo exportado se descreve.** Ao sincronizar com um banco "
            "(ArcadeDB ou Neo4j), o `synesis-graph` grava um vertice "
            "`ProjectContext` com o contexto do proprio projeto: a `DESCRIPTION` "
            "do `.synp`, e o template inteiro como documento legivel — cada campo "
            "com tipo, escopo, descricao, escala de valores e **GUIDELINES**, mais "
            "as arestas do grafo com sua direcao.\n\n"
            "Isso importa porque o schema de um banco e sintaxe sem semantica: ele "
            "diz que existe um vertice `Aspect` com a propriedade `name`, mas nao "
            "que `Aspect` e uma escala ordenada nem o que cada valor significa. "
            "As `GUIDELINES` que voce escreveu sao o seu protocolo de codificacao — "
            "as regras de decisao que dizem o que conta como instancia valida de um "
            "campo. Sem elas no grafo, quem consulta precisa inferir seu criterio a "
            "partir dos dados; com elas, passa a conhece-lo.\n\n"
            "O contexto viaja com os dados, nao com a ferramenta: qualquer "
            "consumidor do grafo o recebe — o Claude Desktop, qualquer cliente MCP, "
            "o studio do proprio banco, ou um colega que receba uma copia. E e "
            "derivado do seu template, entao dois projetos diferentes produzem "
            "contextos diferentes.\n\n"
            "Para ler: `MATCH (p:ProjectContext) RETURN p.description, "
            "p.template_doc`."
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
        "<!-- GERADO AUTOMATICAMENTE por tools/generate_ecosystem.py."
        " Nao edite. -->",
        "",
        f"# {mod['title']}",
        "",
        "## Descricao",
        "",
        f"Papel no ecossistema: **{mod['role']}**"
        + (f" · versao {version}" if version else ""),
        "",
        mod["note"],
        "",
        "## Uso",
        "",
        "```text",
        help_text,
        "```",
        "",
        (
            f"Para os parametros de um subcomando: `{mod['cmd']} <comando>"
            " --help`."
            if mod.get("has_subcommands", True)
            else f"Executavel unico, sem subcomandos: o editor o inicia."
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
        print(f"AVISO: nao instalado(s), verbete nao gerado: {', '.join(missing)}")

    OUT.mkdir(parents=True, exist_ok=True)
    if args.check:
        drift = [
            eid for eid, content in entries.items()
            if not (OUT / f"{eid}.md").exists()
            or (OUT / f"{eid}.md").read_text(encoding="utf-8") != content
        ]
        if drift:
            print(f"DIVERGENCIA: {len(drift)} verbete(s): {', '.join(drift)}")
            return 1
        print(f"OK: {len(entries)} verbetes de ecossistema sincronizados")
        return 0

    for eid, content in entries.items():
        (OUT / f"{eid}.md").write_text(content, encoding="utf-8")
    print(f"Gerados {len(entries)} verbetes de ecossistema em {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
