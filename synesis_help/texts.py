# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Textos longos da CLI: ajuda de escrita e creditos.

Ficam separados de `cli.py` para que a logica de comandos permaneca legivel.
"""

from __future__ import annotations

__version__ = "0.2.1"

AUTHOR = "Christian Maciel De Britto"
YEAR = "2026"
ORCID = "https://orcid.org/0000-0003-1431-3924"
REPO = "https://github.com/synesis-lang/synesis-help"
DOCS = "https://synesis-lang.github.io/synesis-docs"

EPILOG = """\
exemplos:
  synesis-help                      abre o guia (TUI)
  synesis-help lookup CHAIN         consulta um verbete no terminal
  synesis-help lookup E047 --format=json
  synesis-help docs                 como escrever e corrigir verbetes
  synesis-help credits              autoria, licenca e como citar

no guia:
  setas   mover / rolar        F2   referencias cruzadas
  Enter   avancar              F3   busca incremental
  Tab     trocar de painel     Esc  sair
"""

WRITING_GUIDE = f"""\
ESCREVENDO NO GUIA
==================

Onde o conteudo vive
--------------------
  synesis_help/entries/
  ├── _generated/pt/   gerado do compilador — NUNCA editar a mao
  └── authored/pt/     conteudo humano — e aqui que voce escreve

O que o compilador sabe sobre si mesmo (matriz tipo x propriedade, codigos de
erro, mensagens) e derivado por sondagem, nunca copiado. Assim o guia nao pode
divergir do compilador. O que exige julgamento metodologico — para que serve
cada tipo, quando usar, exemplos — e autoral, e vive separado.


Corrigir um texto existente
---------------------------
1. Descubra o arquivo: o nome e o `id` do verbete.
       synesis-help lookup TYPE_CHAIN --format=json

2. Se o caminho contem `_generated/`, NAO edite — veja a secao adiante.

3. Edite o .md em synesis_help/entries/authored/pt/

4. Reconstrua e confira:
       python tools/validate_entries.py   links, ids, frontmatter
       python tools/check_examples.py     exemplos ainda compilam
       synesis-help build                 regrava o indice

   O guia le o indice compilado, nao os .md.
   SEM `build`, SUA EDICAO NAO APARECE.


Acrescentar um verbete
----------------------
Crie synesis_help/entries/authored/pt/<ID>.md — o nome do arquivo E o `id`:

    ---
    id: MOD_EXEMPLO
    title: "EXEMPLO"
    category: modifier
    summary: "Uma frase. E o que aparece no indice."
    syntax: "EXEMPLO <valor> [OPCIONAL <n>]"
    see_also: [BLOCK_FIELD, SYNESIS_E020]
    source: authored
    order: 50
    ---

    # EXEMPLO

    ## Descricao
    O que e e para que serve.

    ## Sintaxe
    (bloco de codigo com a forma completa)

    ## Regras
    - Uma regra por linha, citando o codigo do erro.

    ## Exemplo
    (bloco de codigo que compila)

Depois:  python tools/generate_index.py && synesis-help build

`order` define a posicao dentro da categoria: menor vem primeiro, 100 e o
padrao, empate cai no alfabetico. A ordem e DIDATICA — do panorama ao
detalhe — e nao alfabetica: "Por onde comecar" precisa abrir o guia.

Categorias validas:
  overview · block · field_type · modifier · linkage
  ecosystem · glossary

As categorias block, field_type, modifier e linkage EXIGEM `syntax` no
frontmatter e uma secao "## Sintaxe" no corpo — o validador cobra.

Convencao de `id`:
  BLOCK_    bloco               BLOCK_ONTOLOGY
  TYPE_     tipo de campo       TYPE_CHAIN
  MOD_      modificador         MOD_SCOPE
  GUIDE_    panorama            GUIDE_START
  GLOS_     glossario           GLOS_BIBREF
  (diagnostico usa o proprio codigo: SYNESIS_E047)

O `id` e a chave de tudo — cross-references, links e o contrato JSON.
Escolha e nao mude; o titulo pode mudar a vontade.


Corrigir um verbete gerado
--------------------------
Os 82 verbetes em _generated/ vem do compilador. Edita-los e inutil: a proxima
regeneracao sobrescreve, e o CI acusa.

  A regra em si .............. no compilador (synesis/)
  A mensagem do erro ......... synesis/ast/results.py, em to_diagnostic()
  Resumo do tipo ............. tools/generate_entries.py, dict TYPE_SUMMARY
  Ajuda de um modulo ......... o proprio --help da ferramenta
                               (tools/generate_ecosystem.py so captura)
  Rotulos de secao ........... tools/generate_entries.py, dict L

Para ACRESCENTAR prosa a um verbete gerado, crie um arquivo com o MESMO `id`
em authored/pt/. O build funde os dois, e o autoral vence.


Regras de escrita
-----------------
Acentuacao   Escreva com acentos. Se esquecer:
                 python tools/fix_accents.py --check   relata
                 python tools/fix_accents.py           corrige
             So a prosa e tocada — codigo e campos tecnicos ficam intactos.

Codigo       Maximo 72 colunas, recuo de 4 espacos, sem TAB. Todo exemplo que
             comeca com TEMPLATE ou FIELD e COMPILADO de verdade contra o
             synesis instalado. Exemplo errado no guia e pior que exemplo
             ausente.

Registro     Este e um guia de REFERENCIA (Diataxis): descreve a maquina,
             sucinta e ordenadamente. Tutorial, discussao metodologica e
             estudo de caso pertencem a synesis-docs-sources.

see_also     So `id`s existentes — link quebrado falha o build.

Documentacao completa: {REPO}
"""

CREDITS = f"""\
  synesis-help {__version__}

  Guia de referencia rapida da linguagem Synesis

  Copyright (c) {YEAR} {AUTHOR}
  {ORCID}

  LICENCA
  -------
  AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception

  Este programa e software livre: voce pode redistribui-lo e/ou modifica-lo
  sob os termos da GNU Affero General Public License, versao 3, publicada
  pela Free Software Foundation.

  Distribuido na esperanca de ser util, mas SEM QUALQUER GARANTIA; sem
  sequer a garantia implicita de COMERCIALIZACAO ou ADEQUACAO A UM FIM
  ESPECIFICO. Consulte a GNU AGPL para mais detalhes.

  Excecao de saida de dados: os dados produzidos por este software NAO sao
  cobertos pela AGPL. Ver LICENSE.exception.

  Texto integral: LICENSE e LICENSE.exception, na raiz do repositorio.

  INSPIRACAO
  ----------
  Norton Guides (1985), de Warren Woodford — sistema de ajuda residente que
  definiu o padrao de consulta rapida para programadores, e cuja ergonomia
  este guia procura reviver: offline, instantaneo, navegavel pelo teclado.

  CONTEUDO
  --------
  Os verbetes de diagnostico e de tipo de campo sao derivados por sondagem do
  compilador Synesis — a documentacao nao pode divergir do que o compilador
  faz. Os demais sao autorais.

  COMO CITAR
  ----------
  De Britto, C. M. ({YEAR}). synesis-help: guia de referencia da linguagem
  Synesis (versao {__version__}) [Software]. {REPO}

  ECOSSISTEMA
  -----------
  synesis          compilador da linguagem
  synesis-lsp      language server
  synesis-graph    exportacao para bancos de grafo
  synesis-coder    anotacao assistida por IA
  synesis-vscode   extensao do editor
  synesis-help     este guia

  {DOCS}
"""
