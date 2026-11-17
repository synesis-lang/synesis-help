"""Testes de fumaca do indice e da TUI."""

from __future__ import annotations

from pathlib import Path

import pytest
from textual.widgets import Static

from synesis_help.app import GuideApp
from synesis_help.index import Guide, build

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def db(tmp_path_factory) -> Path:
    path = tmp_path_factory.mktemp("guide") / "guide.db"
    build(ROOT / "synesis_help" / "entries", path)
    return path


def test_index_has_all_entries(db: Path) -> None:
    guide = Guide(db)
    assert guide.total() >= 100
    assert {c[0] for c in guide.categories()} >= {
        "block", "field_type", "diagnostic", "modifier", "overview"
    }


def test_body_has_no_html_comments(db: Path) -> None:
    """O aviso de arquivo gerado e para quem edita, nao para quem consulta."""
    guide = Guide(db)
    entry = guide.get("TYPE_CHAIN")
    assert entry is not None
    assert "<!--" not in entry.body


def test_search_ranks_by_relevance(db: Path) -> None:
    guide = Guide(db)
    assert guide.search("chain")[0].id == "TYPE_CHAIN"
    # Busca por prefixo: incremental enquanto digita.
    assert any(e.id == "TYPE_CHAIN" for e in guide.search("cha"))


def test_cross_references_resolve(db: Path) -> None:
    guide = Guide(db)
    for entry in guide.by_category("field_type"):
        for ref in entry.see_also:
            assert guide.get(ref) is not None, f"{entry.id} -> {ref}"


def test_body_renders_cleanly(db: Path) -> None:
    """Sem markup cru e sem secao repetida.

    "Ver também" aparecia duas vezes: uma do corpo Markdown, outra montada
    a partir de `see_also`. E `**negrito**` sobrevivia quando envolvia
    `código` ou quando atravessava a quebra de linha do fonte.
    """
    from synesis_help.render import render_entry

    guide = Guide(db)
    for row in guide.con.execute("SELECT id FROM entry"):
        text = render_entry(guide.get(row[0]), guide, width=66).plain
        assert "**" not in text, f"{row[0]}: negrito cru"
        assert text.count("V E R   T A M B E M") <= 1, f"{row[0]}: duplicado"


def test_tables_are_not_truncated(db: Path) -> None:
    """Colunas medidas pelo conteúdo, não por largura fixa.

    Larguras fixas cortavam texto ("ponto de entrada; amarra tud…") mesmo
    havendo espaço livre à direita.
    """
    from synesis_help.render import render_entry

    guide = Guide(db)
    text = render_entry(guide.get("GUIDE_FILES"), guide, width=66).plain
    assert "projeto: template, inclusões, metadados" in text
    assert "exatamente 1" in text
    for line in text.split("\n"):
        assert len(line) <= 66, repr(line)


def test_authored_prose_is_accented() -> None:
    """A prosa autoral usa português correto.

    As entries geradas ficam de fora: reproduzem `to_diagnostic()`, que hoje
    também é sem acento — acentuá-las aqui criaria uma segunda verdade e a
    regeneração desfaria o trabalho.
    """
    import re

    authored = ROOT / "synesis_help" / "entries" / "authored"
    for md in authored.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        assert any(ord(c) > 127 and c.isalpha() for c in text), (
            f"{md.name}: prosa sem nenhum acento"
        )
        # Blocos de código ficam de fora: acentuar um exemplo o tornaria
        # inválido, e o texto dentro deles é dado, não prosa.
        prose = re.sub(r"```.*?```|`[^`]*`", "", text, flags=re.DOTALL)
        for wrong in (" nao ", " sao ", " codigo ", " descricao "):
            assert wrong not in prose.lower(), f"{md.name}: '{wrong.strip()}'"


def test_field_names_differ_from_values(db: Path) -> None:
    """`campo: valor` — o nome pertence ao template, o valor é do dado."""
    from synesis_help.render import _code_span

    text = _code_span("    papel: mediador")
    styles = {
        text.plain[s.start : s.end].strip(): str(s.style) for s in text.spans
    }
    assert styles.get("papel") == "field"
    assert styles.get("mediador") == "code_plain"

    # Um campo chamado `code` não pode ser pintado como a keyword CODE.
    text = _code_span("    code: EVENTO_EXTREMO")
    styles = {
        text.plain[s.start : s.end].strip(): str(s.style) for s in text.spans
    }
    assert styles.get("code") == "field"


def test_code_blocks_are_highlighted(db: Path) -> None:
    """Blocos de código distinguem os papéis, como faz um editor."""
    from synesis_help.render import KEYWORDS, render_entry

    assert "FIELD" in KEYWORDS and "ONTOLOGY" in KEYWORDS

    guide = Guide(db)
    text = render_entry(guide.get("GUIDE_START"), guide, width=66)
    styles: dict[str, list[str]] = {}
    for span in text.spans:
        styles.setdefault(str(span.style), []).append(
            text.plain[span.start : span.end]
        )

    assert any(t == "TEMPLATE" for t in styles.get("keyword", []))
    assert any(t.startswith('"') for t in styles.get("string", []))
    assert any(t.startswith("#") for t in styles.get("comment", []))
    assert any(t.startswith("@") for t in styles.get("bibref", []))


def test_entries_are_in_didactic_order(db: Path) -> None:
    """A ordem é editorial, não alfabética.

    Alfabético punha "Por onde começar" em 4º lugar e `DATE` antes de `CODE`
    — nenhum dos dois ajuda quem chega agora.
    """
    guide = Guide(db)
    assert [e.id for e in guide.by_category("overview")][:3] == [
        "GUIDE_START", "GUIDE_FILES", "GUIDE_PRIMITIVES"
    ]
    # Blocos na ordem em que se escreve um projeto.
    assert [e.id for e in guide.by_category("block")][:2] == [
        "BLOCK_PROJECT", "BLOCK_TEMPLATE"
    ]
    # Tipos: os de uso corrente antes dos especializados.
    types = [e.id for e in guide.by_category("field_type")]
    assert types[0] == "TYPE_QUOTATION"
    assert types.index("TYPE_CODE") < types.index("TYPE_DATE")


def test_statusbar_lists_global_keys(db: Path) -> None:
    """As teclas globais aparecem em qualquer foco — e cabem em 80 colunas."""
    app = GuideApp(db)
    for focus in ("categories", "entries", "content", ""):
        line = app._status_text(focus)
        assert "F10 Credits" in line, focus
        assert "F3 Search" in line and "Esc" in line
        assert len(line) <= 80, f"{focus}: {len(line)} colunas"


def test_ecosystem_entries_are_portable(db: Path) -> None:
    """Os verbetes do ecossistema descrevem a ferramenta, não a máquina.

    O `--help` do language server imprime caminhos do interpretador local;
    incluí-los tornaria o guia diferente para cada pessoa que o gerasse.
    """
    guide = Guide(db)
    entries = guide.by_category("ecosystem")
    assert {e.id for e in entries} >= {"ECO_SYNESIS", "ECO_CODER", "ECO_GRAPH"}

    for entry in entries:
        body = entry.body
        assert "site-packages" not in body, entry.id
        assert "C:\\" not in body and "/home/" not in body, entry.id
        assert "Interpreter" not in body, entry.id
        assert "[INFO]" not in body, entry.id

    # O compilador vem primeiro: é dele que os outros dependem.
    assert entries[0].id == "ECO_SYNESIS"


def test_cli_documents_itself(capsys) -> None:
    """`--help`, `docs` e `credits` respondem sem depender do índice."""
    from synesis_help.cli import main

    assert main(["docs"]) == 0
    out = capsys.readouterr().out
    assert "authored/pt" in out and "WITHOUT `build`" in out

    assert main(["credits"]) == 0
    out = capsys.readouterr().out
    assert "AGPL-3.0-only" in out
    assert "Copyright" in out
    assert "Norton Guides" in out


def test_license_files_exist() -> None:
    """A licença precisa acompanhar o código — declará-la não basta."""
    for name in ("LICENSE", "LICENSE.exception"):
        path = ROOT / name
        assert path.exists(), f"{name} ausente"
        assert path.stat().st_size > 1000, f"{name} truncado"
    assert "AFFERO" in (ROOT / "LICENSE").read_text(encoding="utf-8")[:400].upper()


@pytest.mark.asyncio
async def test_credits_page_opens(db: Path) -> None:
    app = GuideApp(db)
    async with app.run_test(size=(96, 26)) as pilot:
        await pilot.pause()
        await pilot.press("f10")
        await pilot.pause()
        body = app.query_one("#body", Static).render().plain
        assert "Copyright" in body and "AGPL" in body


async def _open(app, pilot, entry_id: str) -> None:
    """Abre um verbete pelo `id`.

    Navegar por número de teclas amarra o teste à ordem de apresentação, que
    é editorial e muda.
    """
    app.action_open(entry_id)
    await pilot.pause()


@pytest.mark.asyncio
async def test_navigation(db: Path) -> None:
    app = GuideApp(db)
    async with app.run_test(size=(96, 30)) as pilot:
        await pilot.pause()
        assert app.current is not None

        # Trocar de categoria carrega o primeiro verbete dela.
        await pilot.press("down")
        await pilot.pause()
        first = app.current

        # F2 abre as referencias cruzadas; backspace volta.
        await pilot.press("f2")
        await pilot.pause()
        await pilot.press("backspace")
        await pilot.pause()
        assert app.current == first


@pytest.mark.asyncio
async def test_focus_is_visible(db: Path) -> None:
    """O painel ativo precisa se distinguir do inativo.

    Sem isso o usuario nao sabe para onde as setas vao — foi a queixa que
    motivou esta revisao de navegacao.
    """
    app = GuideApp(db)
    async with app.run_test(size=(96, 26)) as pilot:
        await pilot.pause()
        cats = app.query_one("#categories")
        entries = app.query_one("#entries")

        assert cats.has_focus_within
        active = cats.styles.border_top[1]
        inactive = entries.styles.border_top[1]
        assert active != inactive, "painel ativo e inativo pintam igual"

        await pilot.press("tab")
        await pilot.pause()
        assert entries.has_focus_within


@pytest.mark.asyncio
async def test_cross_references_are_actionable(db: Path) -> None:
    """"Ver também" precisa navegar — é o gesto central do Norton Guides.

    Cobre as duas formas: tecla numérica e clique do mouse.
    """
    app = GuideApp(db)
    async with app.run_test(size=(100, 40)) as pilot:
        await pilot.pause()
        await _open(app, pilot, "TYPE_CHAIN")
        origin = app.current
        assert origin == "TYPE_CHAIN"

        # Tecla numérica abre a n-ésima referência.
        await pilot.press("1")
        await pilot.pause()
        assert app.current != origin
        await pilot.press("backspace")
        await pilot.pause()
        assert app.current == origin

        # Clique sobre a referência renderizada: rola até "Ver também".
        app.query_one("#content").scroll_end(animate=False)
        await pilot.pause()

        body = app.query_one("#body", Static)
        spot = None
        for y, strip in enumerate(
            app.screen._compositor.render_strips(app.screen.size)
        ):
            x = 0
            for segment in strip._segments:
                meta = getattr(segment.style, "meta", None)
                if meta and meta.get("@click"):
                    spot = (x + 2 - body.region.x, y - body.region.y)
                    break
                x += len(segment.text)
            if spot:
                break
        assert spot is not None, "nenhuma referência clicável na tela"

        await pilot.click("#body", offset=spot)
        await pilot.pause()
        assert app.current != origin, "clique não navegou"


@pytest.mark.asyncio
async def test_palette_encodes_hierarchy(db: Path) -> None:
    """Cada papel tem sua cor: a paleta é semântica, não decorativa."""
    from synesis_help.app import C_KEYWORD, C_LINK, C_PLACEHOLDER

    app = GuideApp(db)
    async with app.run_test(size=(100, 30)) as pilot:
        await pilot.pause()
        await _open(app, pilot, "TYPE_CHAIN")

        by_color: dict[str, set[str]] = {}
        for strip in app.screen._compositor.render_strips(app.screen.size):
            for segment in strip._segments:
                text = segment.text.strip()
                color = getattr(segment.style, "color", None)
                if text and color and color.triplet:
                    by_color.setdefault(color.triplet.hex.lower(), set()).add(text)

        # <placeholder> em verde menta, keyword em dourado.
        placeholders = by_color.get(C_PLACEHOLDER.lower(), set())
        assert any(t.startswith("<") for t in placeholders), placeholders
        assert "ARITY" in by_color.get(C_KEYWORD.lower(), set())

        # Referência em azul celeste, não no cinza padrão de link do Textual.
        app.query_one("#content").scroll_end(animate=False)
        await pilot.pause()
        refs = set()
        for strip in app.screen._compositor.render_strips(app.screen.size):
            for segment in strip._segments:
                meta = getattr(segment.style, "meta", None)
                if meta and meta.get("@click"):
                    refs.add(segment.style.color.triplet.hex.lower())
        assert C_LINK.lower() in refs, refs


@pytest.mark.asyncio
async def test_status_bar_follows_focus(db: Path) -> None:
    app = GuideApp(db)
    async with app.run_test(size=(96, 26)) as pilot:
        await pilot.pause()
        assert "Category" in app._status_text("categories")
        assert "Read" in app._status_text("entries")
        assert "Scroll" in app._status_text("content")


@pytest.mark.asyncio
async def test_incremental_search(db: Path) -> None:
    app = GuideApp(db)
    async with app.run_test(size=(96, 30)) as pilot:
        await pilot.pause()
        await pilot.press("f3")
        for ch in "arity":
            await pilot.press(ch)
        await pilot.pause()
        assert app._listed, "busca nao retornou resultados"
        assert app.current in app._listed
