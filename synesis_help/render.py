# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Renderiza o corpo de uma entry na estetica Norton Guides.

Nao usamos o widget Markdown do Textual: as cores dele sao proprias e nao
distinguem os papeis que o guia precisa marcar (keyword, placeholder,
diagnostico). Aqui o Markdown e convertido a mao para `rich.Text`.
"""

from __future__ import annotations

import re
import unicodedata
from typing import TYPE_CHECKING

from rich.console import Console
from rich.text import Text

if TYPE_CHECKING:
    from .index import Entry, Guide

_RULE = "─"

#: Console apenas para medir largura na quebra de linha — nada e impresso.
_CONSOLE = Console(file=None, width=200)

_H2 = re.compile(r"^##\s+(.*)")
_H1 = re.compile(r"^#\s+(.*)")
_FENCE = re.compile(r"^```(\w*)")
_TABLE_SEP = re.compile(r"^\|[\s:|-]+\|$")
_ORDERED = re.compile(r"^\d+\.\s")


#: Negrito e codigo numa varredura unica. Processar em duas passagens
#: quebrava `**`codigo` em negrito**`, que ocorre no texto gerado: a primeira
#: passagem consumia as crases e a segunda recebia `**` sem par.
_INLINE_TOKEN = re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")


def _grammar_keywords() -> frozenset[str]:
    """Keywords da linguagem, lidas da gramatica do compilador instalado.

    Mesma disciplina do resto do projeto: nada de lista paralela que envelhece
    quando a linguagem ganha uma palavra nova.
    """
    try:
        from importlib.resources import files

        text = (
            files("synesis.grammar").joinpath("synesis.lark").read_text("utf-8")
        )
        found = {m.group(1).upper() for m in re.finditer(r"^KW_(\w+)\.", text, re.M)}
        if found:
            return frozenset(found)
    except Exception:  # noqa: BLE001 - gramatica indisponivel
        pass
    # Piso minimo para o realce nao sumir se a gramatica nao for legivel.
    return frozenset({"FIELD", "TYPE", "SCOPE", "END", "TEMPLATE", "PROJECT"})


KEYWORDS = _grammar_keywords()

#: Realce de sintaxe. A ordem importa: comentario e string primeiro, senao
#: uma keyword dentro de um deles seria colorida por engano.
_SYNTAX = re.compile(
    r"(?P<comment>#[^\n]*)"
    r'|(?P<string>"[^"]*")'
    r"|(?P<placeholder><[^>]+>)"
    r"|(?P<diagnostic>SYNESIS_[EWI]\d+)"
    r"|(?P<bibref>@[\w:-]+)"
    r"|(?P<word>[A-Za-z_][\w-]*)"
    r"|(?P<punct>[\[\]|·…:,>=-]+)"
)


#: `nome:` no inicio de uma linha e atribuicao de campo. O nome pertence ao
#: template (estrutura); o que vem depois e dado do pesquisador. Sem esta
#: distincao "papel: mediador" sai todo da mesma cor, e um campo chamado
#: `code` seria pintado como a keyword CODE.
_FIELD_ASSIGN = re.compile(r"^(\s*)([A-Za-z_][\w-]*)(\s*:)")


def _code_span(code: str) -> Text:
    """Realce de sintaxe da linguagem Synesis.

    Distingue os papeis que um editor distingue — keyword, string, comentario,
    referencia bibliografica, placeholder — em vez de pintar tudo de uma cor.
    """
    out = Text()
    pos = 0

    assign = _FIELD_ASSIGN.match(code)
    if assign:
        out.append(assign.group(1), style="code_plain")
        out.append(assign.group(2), style="field")
        out.append(assign.group(3), style="punct")
        pos = assign.end()
    # A varredura comeca depois do "nome:" ja tratado, senao o proprio nome
    # seria reprocessado e voltaria a ser keyword.
    for m in _SYNTAX.finditer(code, pos):
        out.append(code[pos : m.start()], style="code_plain")
        kind = m.lastgroup
        token = m.group()
        if kind == "word":
            style = "keyword" if token.upper() in KEYWORDS else "code_plain"
            out.append(token, style=style)
        else:
            out.append(token, style=_SYNTAX_STYLE[kind])
        pos = m.end()
    out.append(code[pos:], style="code_plain")
    return out


_SYNTAX_STYLE = {
    "comment": "comment",
    "string": "string",
    "placeholder": "placeholder",
    "diagnostic": "diagnostic",
    "bibref": "bibref",
    "punct": "punct",
}


def _emit_table(
    out: Text,
    rows: list[list[str]],
    guide: "Guide | None",
    known: set[str],
    width: int,
) -> None:
    """Escreve uma tabela medindo as colunas pelo conteudo real.

    Larguras fixas cortavam texto mesmo com espaco sobrando a direita. Aqui
    cada coluna pede o que precisa; se a soma exceder a largura util, o
    excedente sai da coluna mais larga — a que tem mais folga para ceder.
    """
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    gap = 2
    budget = width - 2 - gap * (n - 1)

    # Mede o texto JA renderizado: crases e ** somem na conversao, e contar
    # os caracteres da marcacao desalinharia a coluna seguinte.
    cooked = [[_inline(c, guide, known) for c in row] for row in rows]
    need = [max(len(cooked[r][i].plain) for r in range(len(rows))) for i in range(n)]
    while sum(need) > budget:
        widest = need.index(max(need))
        if need[widest] <= 8:
            break  # nao vale mais espremer: corta no fim
        need[widest] -= 1

    for row in cooked:
        out.append("  ")
        for i, seg in enumerate(row):
            room = need[i]
            if len(seg.plain) > room:
                seg = seg[: max(1, room - 1)]
                seg.append("…", style="punct")
            if i < n - 1:
                seg.pad_right(room - len(seg.plain) + gap)
            out.append_text(seg)
        out.append("\n")


def _inline(line: str, guide: "Guide | None", known: set[str]) -> Text:
    """Converte marcacao inline, destacando codigo e referencias cruzadas.

    Um `codigo` que casa com o id de outra entry vira link navegavel (ciano);
    os demais ficam amarelos, como as keywords do guia original.
    """
    out = Text()
    pos = 0
    for m in _INLINE_TOKEN.finditer(line):
        out.append(line[pos : m.start()], style="body")
        bold, code = m.group(1), m.group(2)
        if bold is not None:
            # Negrito pode conter crases: reprocessa o interior.
            inner = _inline(bold, guide, known)
            inner.stylize("strong")
            out.append_text(inner)
        elif code in known:
            # Referencia no meio do texto tambem e acionavel por clique.
            ref = Text(code, style="link_ref")
            ref.apply_meta({"@click": f"app.open('{code}')", "ref": code})
            out.append_text(ref)
        else:
            out.append_text(_code_span(code))
        pos = m.end()
    out.append(line[pos:], style="body")
    return out


def _unwrap(body: str) -> list[str]:
    """Junta as linhas de cada paragrafo de prosa numa linha so.

    O Markdown fonte quebra em 79 colunas, e um `**negrito**` pode atravessar
    a quebra. Como a renderizacao e linha a linha, o par nunca fecharia. Blocos
    de codigo, tabelas, listas e cabecalhos ficam intactos.
    """
    out: list[str] = []
    buf: list[str] = []
    in_code = False

    def flush() -> None:
        if buf:
            out.append(" ".join(buf))
            buf.clear()

    for line in body.split("\n"):
        if _FENCE.match(line):
            flush()
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        stripped = line.strip()
        # "- " e "* " sao itens de lista; "**" inicia negrito e e prosa comum.
        # "1." e item de lista numerada — sem isso vira um paragrafo colado.
        is_bullet = stripped[:2] in ("- ", "* ") or _ORDERED.match(stripped)
        is_special = (
            not stripped
            or is_bullet
            or stripped.startswith(("#", "|", ">", "<!--"))
            or line.startswith("    ")
        )
        if is_special:
            flush()
            # Item de lista abre um paragrafo proprio: as linhas seguintes
            # sao continuacao dele, nao texto solto.
            if is_bullet:
                buf.append(stripped)
            else:
                out.append(line)
        else:
            buf.append(stripped)
    flush()
    return out


def _is_seealso(heading: str) -> bool:
    """Reconhece o cabecalho 'Ver tambem' com ou sem acento."""
    norm = unicodedata.normalize("NFKD", heading.lower())
    norm = "".join(c for c in norm if not unicodedata.combining(c))
    return norm.strip() in ("ver tambem", "see also")


def _spaced(heading: str) -> str:
    """Cabecalho de secao: maiusculas, sem espacamento entre letras."""
    return heading.upper()



def render_entry(entry: "Entry", guide: "Guide", width: int = 76) -> Text:
    """Corpo completo da entry, pronto para exibicao."""
    known = {e for e in entry.see_also}
    # Referencias podem aparecer no corpo sem estar em see_also.
    known |= {
        r[0] for r in guide.con.execute("SELECT id FROM entry")
    }

    out = Text()
    out.append(entry.title, style="title")
    out.append("\n")
    out.append(_RULE * min(width, max(len(entry.title), 40)), style="rule")
    out.append("\n")
    if entry.summary:
        out.append(entry.summary + "\n", style="summary")
    out.append("\n")

    in_code = False
    in_comment = False
    skip_section = False
    table: list[list[str]] = []
    for raw in _unwrap(entry.body):
        # Comentarios HTML (aviso de arquivo gerado) sao para quem edita o
        # Markdown, nao para quem consulta o guia.
        if in_comment:
            if "-->" in raw:
                in_comment = False
            continue
        if raw.lstrip().startswith("<!--"):
            if "-->" not in raw:
                in_comment = True
            continue

        fence = _FENCE.match(raw)
        if fence:
            in_code = not in_code
            continue

        if in_code:
            # Mesma separacao de papeis do codigo inline: keyword, placeholder
            # e pontuacao de estrutura em cores distintas.
            out.append("    ")
            out.append_text(_code_span(raw))
            out.append("\n")
            continue

        if _TABLE_SEP.match(raw.strip()):
            continue

        h1 = _H1.match(raw)
        if h1:
            continue  # o titulo ja foi impresso no cabecalho

        h2 = _H2.match(raw)
        if h2:
            heading = h2.group(1).strip()
            # A secao "Ver tambem" do corpo e substituida pela versao
            # acionavel, montada ao final a partir de `see_also`. Sem isso
            # ela apareceria duas vezes.
            if _is_seealso(heading):
                skip_section = True
                continue
            skip_section = False
            out.append("\n")
            out.append(_spaced(heading), style="section")
            out.append("\n")
            continue

        if skip_section:
            continue

        if raw.strip().startswith("|"):
            table.append([c.strip() for c in raw.strip().strip("|").split("|")])
            continue

        # Fim da tabela: agora que todas as linhas sao conhecidas, as colunas
        # podem ser medidas pelo conteudo real em vez de largura fixa.
        if table:
            _emit_table(out, table, guide, known, width)
            table = []

        if raw.startswith(">"):
            out.append("  │ ", style="rule")
            out.append_text(_inline(raw.lstrip("> "), guide, known))
            out.append("\n")
            continue

        if not raw.strip():
            out.append("\n")
            continue

        # Item de lista: hifen vira bullet tipografico, "1." mantem o numero.
        # A continuacao alinha sob o texto, nao sob o marcador.
        stripped = raw.lstrip()
        num = _ORDERED.match(stripped)
        if stripped.startswith(("- ", "* ")) or num:
            if num:
                mark, rest = num.group().strip() + " ", stripped[num.end() :]
            else:
                mark, rest = "• ", stripped[2:]
            pad = 2 + len(mark)
            body = _inline(rest, guide, known)
            for j, piece in enumerate(body.wrap(_CONSOLE, width - pad) or [body]):
                if j == 0:
                    out.append("  ")
                    out.append(mark, style="rule")
                else:
                    out.append(" " * pad)
                out.append_text(piece)
                out.append("\n")
            continue

        # Paragrafo de prosa: estiliza primeiro, quebra depois. Quebrar o
        # texto cru partiria `**negrito**` ao meio e deixaria os asteriscos
        # visiveis na tela.
        para = _inline(raw, guide, known)
        para.rstrip()
        for piece in para.wrap(_CONSOLE, width) or [para]:
            out.append_text(piece)
            out.append("\n")

    targets = [(r, guide.get(r)) for r in entry.see_also]
    targets = [(r, t) for r, t in targets if t is not None]
    if targets:
        out.append("\n")
        out.append(_spaced("Ver tambem"), style="section")
        out.append("\n")
        # Grid alinhado: o rotulo ocupa largura fixa, a glosa comeca sempre na
        # mesma coluna. Sem sublinhado — o ♦ e o alinhamento ja marcam o item.
        label_w = min(24, max(len(r) for r, _ in targets) + 2)
        for ref, target in targets:
            link = Text()
            link.append("  ♦ ", style="link_mark")
            link.append(ref.ljust(label_w), style="link_ref")
            room = width - label_w - 6
            glosa = target.summary
            if len(glosa) > room:
                glosa = glosa[: max(1, room - 1)] + "…"
            link.append(glosa, style="dim_body")
            # apply_meta ANTES de anexar: aplicado depois, incidiria sobre o
            # texto ja copiado e o clique se perderia.
            # `app.` qualifica o namespace: sem isso a acao e procurada no
            # widget que recebeu o clique, nao no App.
            link.apply_meta({"@click": f"app.open('{ref}')"})
            out.append_text(link)
            out.append("\n")
    return out


def entry_links(entry: "Entry", guide: "Guide") -> list[str]:
    """Ids alcancaveis a partir desta entry, na ordem de exibicao."""
    return [ref for ref in entry.see_also if guide.get(ref)]
