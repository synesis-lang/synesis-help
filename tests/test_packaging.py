# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Contratos de empacotamento: versao, citacao e changelog em acordo.

CITATION.cff defasado ja aconteceu duas vezes no ecossistema — a versao e
declarada em quatro lugares e nada obrigava os quatro a concordarem. Estes
testes sao a obrigacao.

Nao usam PyYAML nem tomllib: as chaves conferidas sao escalares simples, e
`tomllib` so entrou na stdlib no Python 3.11 — este pacote suporta 3.10
(`requires-python = ">=3.10"`), onde o import quebraria a coleta inteira da
suite. Uma dependencia a mais so para ler `version:` nao se paga.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _declared_version() -> str:
    """A versao do pyproject e a fonte de verdade; as demais a seguem."""
    text = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    # Ancorado em `[project]`: um `version` de outra secao nao serve.
    project = text.split("[project]", 1)[1]
    m = re.search(r'^version\s*=\s*"([^"]+)"', project, re.MULTILINE)
    assert m, "pyproject.toml: `version` nao encontrado em [project]"
    return m.group(1)


def _cff_field(name: str) -> str | None:
    """Le uma chave escalar de topo do CITATION.cff."""
    text = (REPO_ROOT / "CITATION.cff").read_text(encoding="utf-8")
    m = re.search(rf'^{name}:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    return m.group(1).strip() if m else None


class TestVersionConsistency:
    def test_module_version_matches_pyproject(self):
        from synesis_help.texts import __version__

        assert __version__ == _declared_version()

    def test_citation_version_matches_pyproject(self):
        assert _cff_field("version") == _declared_version()

    def test_citation_has_release_date(self):
        """Sem `date-released` o GitHub gera citacao sem ano de publicacao."""
        date = _cff_field("date-released")
        assert date is not None, "CITATION.cff sem `date-released`"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", date), date

    def test_citation_license_matches_pyproject(self):
        text = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        m = re.search(r'^license\s*=\s*"([^"]+)"', text, re.MULTILINE)
        assert m, "pyproject.toml: `license` nao encontrado"
        # O pyproject carrega a expressao SPDX completa (AGPL + excecao); o
        # CFF so aceita identificador de lista fechada, entao guarda a AGPL.
        # O contrato e que a AGPL apareca nos dois, nao que sejam iguais.
        assert _cff_field("license") in m.group(1)


class TestChangelog:
    @pytest.mark.parametrize("name", ["CHANGELOG.md", "CHANGELOG.pt.md"])
    def test_changelog_documents_current_version(self, name):
        """Publicar versao ausente do CHANGELOG deixa o historico mentindo."""
        text = (REPO_ROOT / name).read_text(encoding="utf-8")
        assert f"## [{_declared_version()}]" in text

    @pytest.mark.parametrize("name", ["CHANGELOG.md", "CHANGELOG.pt.md"])
    def test_released_version_has_comparison_link(self, name):
        """Cabecalho `## [x.y.z]` sem link no rodape renderiza como texto cru."""
        text = (REPO_ROOT / name).read_text(encoding="utf-8")
        version = _declared_version()
        needle = "\n[" + version + "]: http"
        assert needle in text, f"{name}: falta o link de `[{version}]` no rodape"

    @pytest.mark.parametrize("name", ["CHANGELOG.md", "CHANGELOG.pt.md"])
    def test_changelog_entry_count_matches_index(self, name):
        """A contagem citada no changelog envelhece a cada verbete novo."""
        total = len(list((REPO_ROOT / "synesis_help" / "entries").rglob("*.md")))
        text = (REPO_ROOT / name).read_text(encoding="utf-8")
        m = re.search(r"—\s*(\d+)\s+(entries|verbetes)", text)
        assert m, f"{name}: contagem de verbetes nao encontrada"
        assert int(m.group(1)) == total, (
            f"{name} diz {m.group(1)} verbetes; ha {total} em disco"
        )


class TestPackageData:
    def test_entries_are_packaged(self):
        """Sem as entries o comando instala e abre vazio."""
        text = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        section = text.split("[tool.setuptools.package-data]", 1)
        assert len(section) == 2, "pyproject.toml sem [tool.setuptools.package-data]"
        m = re.search(r"^synesis_help\s*=\s*\[([^\]]*)\]", section[1], re.MULTILINE)
        assert m, "package-data sem a chave `synesis_help`"
        assert "entries" in m.group(1), m.group(1)
