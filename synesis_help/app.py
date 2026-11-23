# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""TUI do Guia Synesis — estetica Norton Guides.

Tres zonas: barra de titulo, corpo em dois paineis, barra de teclas.
Paleta "Retro-Editorial": a silhueta e dos anos 80, as cores nao — cada uma
carrega um papel na hierarquia da informacao (ver bloco de constantes).
"""

from __future__ import annotations

from pathlib import Path

from rich.style import Style
from rich.text import Text
from rich.theme import Theme
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.content import Content
from textual.widgets import Input, Label, ListItem, ListView, Static

from .index import Guide
from .render import render_entry
from .texts import CREDITS

# --------------------------------------------------------------------------
# Paleta "Retro-Editorial".
#
# A silhueta e dos anos 80; as cores, nao. Em vez do azul e amarelo puros do
# CGA — vibrantes mas agressivos numa tela de LCD —, tons de profundidade que
# sustentam leitura longa. Cada cor carrega um papel na hierarquia da
# informacao, nunca decora.
#
# Nomeadas pelo PAPEL, nao pela cor: trocar a paleta nao deve exigir tocar no
# CSS nem no renderizador.
# --------------------------------------------------------------------------
C_BG = "#1B2233"        # midnight blue — fundo, profundidade sem preto puro
C_BG_SOFT = "#242C40"    # um degrau acima: barras e realces sutis
C_TEXT = "#D6DCE8"       # prata — corpo do texto
C_HEADING = "#5FD7E4"    # ciano brilhante — cabecalhos, ancoragem ao rolar
C_KEYWORD = "#E8C161"    # amarelo dourado — comandos estruturais
C_PLACEHOLDER = "#8FD9A8"  # verde menta — o que o usuario substitui
C_ALERT = "#F08A63"      # laranja coral — diagnosticos
C_LINK = "#7FB4E8"       # azul celeste — referencias
C_DIM = "#7A849B"        # cinza medio — simbolos de estrutura
C_STRING = "#D9A0C9"     # rosa suave — literais de texto no codigo
C_FIELD = "#9FC5E8"      # azul palido — nomes de campo (estrutura do template)
C_SELECT_FG = "#14192A"  # texto sobre selecao invertida

#: Estilos nomeados usados por render.py. Mesma paleta, num so lugar.
GUIDE_THEME = Theme({
    "title": Style(color=C_HEADING, bold=True),
    "section": Style(color=C_HEADING, bold=True),
    "rule": Style(color=C_DIM),
    "summary": Style(color=C_TEXT, italic=True),
    "body": Style(color=C_TEXT),
    "dim_body": Style(color=C_DIM),
    "strong": Style(color=C_TEXT, bold=True),
    "keyword": Style(color=C_KEYWORD, bold=True),
    # Placeholder em italico: diz "isto voce digita", o keyword diz "isto e
    # do sistema".
    "placeholder": Style(color=C_PLACEHOLDER, italic=True),
    "punct": Style(color=C_DIM),
    "diagnostic": Style(color=C_ALERT, bold=True),
    # Realce de sintaxe nos blocos de codigo, nas convencoes que qualquer
    # editor usa: comentario apagado, string em tom proprio, identificador
    # do usuario neutro (para a keyword dourada saltar).
    "code_plain": Style(color=C_TEXT),
    # Nome de campo: pertence ao template (estrutura), enquanto o valor ao
    # lado e dado do pesquisador. Tom proprio, entre a keyword e o texto.
    "field": Style(color=C_FIELD),
    "comment": Style(color=C_DIM, italic=True),
    "string": Style(color=C_STRING),
    "bibref": Style(color=C_LINK, italic=True),
    # Sem sublinhado: a cor e a inversao no foco ja marcam o link.
    "link_ref": Style(color=C_LINK),
    "link_num": Style(color=C_KEYWORD, bold=True),
    "link_mark": Style(color=C_LINK, bold=True),
    "code": Style(color=C_KEYWORD),
})

def _clickable(text: Text, console=None) -> Content:
    """Converte o Text do renderizador em Content, preservando os cliques.

    O Textual 3.x converte `Text` em `Content` internamente e, nessa
    conversao, descarta `meta` — que e onde `render.py` guarda o alvo de cada
    referencia. Aqui os spans com `@click` sao reaplicados sobre o Content.

    O `console` e necessario para resolver os estilos nomeados do tema
    (`title`, `keyword`, ...); sem ele a conversao tenta le-los como cor.
    """
    content = Content.from_rich_text(text, console=console)
    for span in text.spans:
        meta = getattr(span.style, "meta", None)
        click = meta.get("@click") if meta else None
        if click:
            # A cor vem depois do @click: o estilo de link padrao do Textual
            # sobrescreveria o azul celeste da referencia.
            content = content.stylize(f"@click={click}", span.start, span.end)
            content = content.stylize(C_LINK, span.start, span.end)
    return content


CSS = f"""
Screen {{
    background: {C_BG};
    color: {C_TEXT};
}}

#titlebar {{
    dock: top;
    height: 1;
    background: {C_BG_SOFT};
    color: {C_HEADING};
    text-style: bold;
    padding: 0 1;
}}

#statusbar {{
    dock: bottom;
    height: 1;
    background: {C_BG_SOFT};
    color: {C_DIM};
    padding: 0 1;
}}

/* Uma linha so, sem moldura propria: o Input ja desenha a sua, e uma segunda
   borda em volta produzia a "janela dupla". Fica acima da barra de status
   para nao encobrir a linha de teclas. */
#searchbar {{
    dock: bottom;
    height: 1;
    display: none;
    background: {C_BG_SOFT};
    color: {C_HEADING};
    border: none;
    padding: 0 1;
}}
#searchbar.visible {{ display: block; }}
#searchbar > .input--placeholder {{
    color: {C_DIM};
}}

#sidebar {{
    width: 28;
}}

/* Cada painel tem titulo proprio; a moldura do painel ativo acende em ciano.
   Sao duas pistas redundantes de foco — util em terminal com pouco contraste
   ou para quem distingue mal cores. */
#categories {{
    height: auto;
    max-height: 45%;
    background: {C_BG};
    border: round {C_DIM};
    border-title-color: {C_DIM};
    border-title-align: left;
}}

#entries {{
    background: {C_BG};
    border: round {C_DIM};
    border-title-color: {C_DIM};
    border-title-align: left;
}}

/* Foco: a moldura acende no ciano dos cabecalhos. E a pista que o olho
   encontra antes de ler qualquer coisa. */
#categories:focus-within,
#entries:focus-within,
#content:focus {{
    border: round {C_HEADING};
    border-title-color: {C_HEADING};
    border-title-style: bold;
}}

ListView {{
    background: {C_BG};
    scrollbar-background: {C_BG};
    scrollbar-color: {C_BG_SOFT};
}}

ListItem {{
    background: {C_BG};
    color: {C_TEXT};
    padding: 0 1;
}}

/* Painel INATIVO: a selecao fica apenas marcada, sem barra — mostra "onde
   voce estava", nao "onde voce esta". */
ListItem.--highlight {{
    background: {C_BG};
    color: {C_LINK};
    text-style: none;
}}

/* Painel ATIVO: barra cheia, o cursor classico do NG. */
ListView:focus > ListItem.--highlight {{
    background: {C_LINK};
    color: {C_SELECT_FG};
    text-style: bold;
}}

/* O marcador ▸ so existe no item sob o cursor do painel ativo: e o que o
   olho segue ao rolar, sem pintar a lista inteira. */
ListItem > Label {{
    width: 100%;
}}
ListView:focus > ListItem.--highlight > Label {{
    text-style: bold;
}}

#content {{
    padding: 0 1;
    background: {C_BG};
    border: round {C_DIM};
    border-title-color: {C_DIM};
    border-title-align: left;
    scrollbar-background: {C_BG};
    scrollbar-color: {C_BG_SOFT};
    scrollbar-color-hover: {C_LINK};
    scrollbar-color-active: {C_KEYWORD};
}}

Input {{
    background: {C_BG};
    color: {C_KEYWORD};
    border: none;
}}

/* Referencia sob o cursor do mouse: inversao de cor, sem sublinhado. */
#body {{
    link-color: {C_LINK};
    link-style: none;
    link-background: {C_BG};
    link-color-hover: {C_SELECT_FG};
    link-background-hover: {C_LINK};
    link-style-hover: bold;
}}
"""


class GuideApp(App):
    """Visualizador do Guia Synesis."""

    CSS = CSS
    TITLE = "Synesis Guide"

    BINDINGS = [
        Binding("escape", "escape", "Quit", priority=True),
        Binding("f3,slash", "search", "Search"),
        Binding("f2", "follow", "See also"),
        Binding("backspace", "back", "Back"),
        Binding("f1", "help", "Help"),
        Binding("f10,c", "credits", "Creditos"),
        Binding("tab", "focus_next", "Painel", show=False),
        # Atalho para as referencias cruzadas sem tirar as maos do teclado.
        *[
            Binding(str(n), f"jump({n})", f"Ref {n}", show=False)
            for n in range(1, 10)
        ],
    ]

    def __init__(self, db_path: Path) -> None:
        super().__init__()
        self.guide = Guide(db_path)
        self.history: list[str] = []
        self.current: str | None = None
        self._categories = self.guide.categories()
        self._listed: list[str] = []
        self._entry_labels: list[str] = []
        self._entries_title = "Entries"
        self._searching = False

    # ---------------------------------------------------------------- layout

    def compose(self) -> ComposeResult:
        total = self.guide.total()
        yield Static(
            f"Synesis Guide{' ' * 43}{total} entries", id="titlebar"
        )
        with Horizontal():
            with Vertical(id="sidebar"):
                yield ListView(id="categories")
                yield ListView(id="entries")
            with VerticalScroll(id="content", can_focus=True):
                yield Static(id="body")
        # Ordem importa com dock:bottom — o ultimo declarado fica mais acima.
        # A barra de status precisa ficar embaixo de tudo.
        yield Static(self._status_text(), id="statusbar")
        yield Input(
            placeholder="Search…   ↵ confirm · Esc cancel",
            id="searchbar",
        )

    def _status_text(self, focus: str = "") -> str:
        """Teclas do painel ativo — o rodape confirma onde o foco esta.

        A metade esquerda muda com o foco; a direita reune o que vale sempre,
        na ordem em que se usa: buscar, trocar de painel, sair.
        """
        local = {
            "categories": "↑↓ Category  ↵ Entries",
            "entries": "↑↓ Entry  ↵ Read  F2 Refs",
            "content": "↑↓ Scroll  F2 Refs  ⌫ Back",
        }.get(focus, "↵ Open  F2 Refs  ⌫ Back")
        # Cabe em 80 colunas: abaixo disso o terminal cortaria o "Esc".
        return f" {local}  │  F1 Help  F3 Search  F10 Credits  Tab  Esc"

    def _refresh_status(self, focus: str = "") -> None:
        self.query_one("#statusbar", Static).update(self._status_text(focus))

    def on_descendant_focus(self, event) -> None:
        node_id = getattr(event.widget, "id", "") or ""
        if node_id in ("categories", "entries", "content"):
            self._refresh_status(node_id)

    def on_mount(self) -> None:
        # Estilos do corpo (render.py) vivem no console do Rich, nao no CSS.
        self.console.push_theme(GUIDE_THEME)
        cats = self.query_one("#categories", ListView)
        cats.border_title = "Categories"
        self.query_one("#entries", ListView).border_title = "Entries"
        for _key, label, count in self._categories:
            cats.append(ListItem(Label(f"  {label:<15}{count:>4}")))
        cats.index = 0
        self._load_category(self._categories[0][0])
        cats.focus()

    # ------------------------------------------------------------- carregar

    def _mark(self, view: ListView, glyph: str, labels: list[str]) -> None:
        """Redesenha o marcador do item sob o cursor.

        O CSS nao consegue: `border-left` pinta todos os itens, nao so o
        destacado. O simbolo entra no proprio texto do Label.
        """
        for i, item in enumerate(view.children):
            label = item.query_one(Label)
            mark = glyph if i == view.index else " "
            label.update(f"{mark} {labels[i]}")

    def _fill_entries(self, entries: list, title: str = "Entries") -> None:
        """Repovoa a lista da direita.

        Os ids ficam em `self._listed`, paralelos ao indice do ListView — nao
        em `id=` do widget: `clear()` e assincrono e a remocao pode nao ter
        acontecido quando o proximo lote e inserido (DuplicateIds).
        """
        self._listed = [e.id for e in entries]
        self._entries_title = title
        self._entry_labels = [e.title for e in entries]
        lv = self.query_one("#entries", ListView)
        lv.border_title = f"{title}  {len(entries)}"
        lv.clear()
        for e in entries:
            lv.append(ListItem(Label(f"  {e.title}")))
        if entries:
            lv.index = 0
            self._show(entries[0].id, push=False)
        else:
            self.query_one("#body", Static).update("")

    def _load_category(self, category: str) -> None:
        self._fill_entries(self.guide.by_category(category))

    def _show(self, entry_id: str, push: bool = True) -> None:
        entry = self.guide.get(entry_id)
        if entry is None:
            return
        if push and self.current and self.current != entry_id:
            self.history.append(self.current)
        self.current = entry_id
        pane_width = self.query_one("#content", VerticalScroll).size.width
        body = render_entry(entry, self.guide, width=max(40, pane_width - 4))
        self.query_one("#body", Static).update(_clickable(body, self.console))
        pane = self.query_one("#content", VerticalScroll)
        pane.border_title = entry.category_label
        pane.scroll_home(animate=False)

    # -------------------------------------------------------------- eventos

    @on(ListView.Highlighted, "#categories")
    def _on_category(self, event: ListView.Highlighted) -> None:
        lv = event.list_view
        if lv.index is None:
            return
        # Diamante para a categoria ativa (item de um conjunto fixo).
        self._mark(lv, "♦", [f"{lb:<15}{n:>4}" for _k, lb, n in self._categories])
        if self._searching:
            return
        if 0 <= lv.index < len(self._categories):
            self._load_category(self._categories[lv.index][0])

    @on(ListView.Selected, "#categories")
    def _on_category_selected(self, event: ListView.Selected) -> None:
        """Enter na categoria avanca para a lista de verbetes."""
        self.query_one("#entries", ListView).focus()

    @on(ListView.Highlighted, "#entries")
    def _on_entry(self, event: ListView.Highlighted) -> None:
        lv = event.list_view
        if lv.index is None or not (0 <= lv.index < len(self._listed)):
            return
        # Contador na moldura: diz onde voce esta na lista sem contar itens.
        lv.border_title = f"{self._entries_title}  {lv.index + 1}/{len(self._listed)}"
        # Triangulo para o verbete selecionado (item de uma lista longa).
        self._mark(lv, "►", self._entry_labels)
        self._show(self._listed[lv.index], push=False)

    @on(ListView.Selected, "#entries")
    def _on_entry_selected(self, event: ListView.Selected) -> None:
        # Enter confirma a leitura: e aqui que a navegacao vira historico.
        # Percorrer a lista com as setas apenas pre-visualiza.
        if self.current:
            self.history.append(self.current)
        self.query_one("#content", VerticalScroll).focus()

    @on(Input.Changed, "#searchbar")
    def _on_search(self, event: Input.Changed) -> None:
        query = event.value.strip()
        self._fill_entries(self.guide.search(query) if query else [])

    @on(Input.Submitted, "#searchbar")
    def _on_search_done(self, event: Input.Submitted) -> None:
        self._close_search()
        self.query_one("#entries", ListView).focus()

    # ---------------------------------------------------------------- acoes

    def action_search(self) -> None:
        bar = self.query_one("#searchbar", Input)
        bar.add_class("visible")
        bar.value = ""
        self._searching = True
        bar.focus()

    def _close_search(self) -> None:
        bar = self.query_one("#searchbar", Input)
        bar.remove_class("visible")
        self._searching = False

    def action_escape(self) -> None:
        if self._searching:
            self._close_search()
            self.query_one("#entries", ListView).focus()
            return
        self.exit()

    def action_back(self) -> None:
        if self.history:
            self._show(self.history.pop(), push=False)

    def action_open(self, entry_id: str) -> None:
        """Abre uma referencia cruzada — acionada por clique no texto."""
        if self.guide.get(entry_id) is None:
            return
        self._show(entry_id)
        self.query_one("#content", VerticalScroll).focus()

    def action_jump(self, n: int) -> None:
        """Abre a n-esima referencia de 'Ver tambem' (teclas 1-9)."""
        if not self.current:
            return
        entry = self.guide.get(self.current)
        if entry is None:
            return
        targets = [r for r in entry.see_also if self.guide.get(r)]
        if 1 <= n <= len(targets):
            self.action_open(targets[n - 1])

    def action_follow(self) -> None:
        """Abre as referencias cruzadas da entry atual na lista da esquerda.

        E o gesto caracteristico do Norton Guides: saltar de um verbete para
        os relacionados sem voltar ao indice.
        """
        if not self.current:
            return
        entry = self.guide.get(self.current)
        if entry is None or not entry.see_also:
            return
        targets = [t for t in (self.guide.get(r) for r in entry.see_also) if t]
        if not targets:
            return
        self.history.append(self.current)
        self._fill_entries(targets)
        self.query_one("#entries", ListView).focus()

    def action_credits(self) -> None:
        """Pagina de creditos: autoria, licenca e como citar."""
        import textwrap

        pane = self.query_one("#content", VerticalScroll)
        width = max(40, pane.size.width - 4)
        page = Text()
        para: list[str] = []

        def flush() -> None:
            """Escreve o paragrafo acumulado, requebrado na largura real."""
            if not para:
                return
            for piece in textwrap.wrap(" ".join(para), width=width - 2) or [""]:
                page.append("  " + piece + "\n", style="body")
            para.clear()

        for line in CREDITS.split("\n"):
            stripped = line.strip()
            if not stripped:
                flush()
                page.append("\n")
            elif set(stripped) <= {"-"}:
                flush()
                page.append(line + "\n", style="rule")
            elif stripped == stripped.upper() and len(stripped) > 3:
                flush()
                page.append(line + "\n", style="section")
            elif line.startswith("  ") and "  " in stripped:
                # Linha ja tabulada (lista do ecossistema): preserva como esta.
                flush()
                page.append(line + "\n", style="body")
            else:
                # A fonte quebra em ~70 colunas; junta e requebra na largura
                # real do painel, senao a linha quebra duas vezes.
                para.append(stripped)
        flush()
        pane.border_title = "Credits"
        self.query_one("#body", Static).update(page)
        pane.scroll_home(animate=False)
        pane.focus()

    def action_help(self) -> None:
        entry = self.guide.get("GUIDE_START")
        if entry:
            self._show(entry.id)


def run(db_path: Path) -> None:
    GuideApp(db_path).run()
