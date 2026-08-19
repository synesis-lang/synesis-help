# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Contratos de empacotamento: versao, citacao e changelog em acordo.

CITATION.cff defasado ja aconteceu duas vezes no ecossistema — a versao e
declarada em quatro lugares e nada obrigava os quatro a concordarem. Estes
testes sao a obrigacao.

Nao usam PyYAML: as tres chaves conferidas sao escalares no topo do arquivo,
e uma dependencia a mais no CI so para ler `version:` nao se paga.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import tomllib

REPO_ROOT = Path(__file__).resolve().parent.parent


def _declared_version() -> str:
    """A versao do pyproject e a fonte de verdade; as demais a seguem."""
    data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return data["project"]["version"]


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
        data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        # O pyproject carrega a expressao SPDX completa (AGPL + excecao); o
        # CFF so aceita identificador de lista fechada, entao guarda a AGPL.
        # O contrato e que a AGPL apareca nos dois, nao que sejam iguais.
        assert _cff_field("license") in data["project"]["license"]


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
        data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        patterns = data["tool"]["setuptools"]["package-data"]["synesis_help"]
        assert any("entries" in p for p in patterns), patterns
