# synesis-help

Guia de referência rápida da linguagem Synesis, offline e instantâneo — inspirado nos
[Norton Guides](https://harbour.github.io/ng/c52g01b/menu.html) do ecossistema Clipper.

Sintaxe, descrição, exemplo, ver também. Nada além disso.

**Versão 0.1.0** — conteúdo, índice e TUI. Ver [CHANGELOG.md](CHANGELOG.md).
Estudo de arquitetura: [`synesis-planning/synesis-help/estudo_synesis_help.md`](../synesis-planning/synesis-help/estudo_synesis_help.md).

## Uso

```bash
synesis-help                       # abre a TUI
synesis-help build                 # recompila o índice
synesis-help lookup CHAIN          # consulta no terminal
synesis-help lookup CHAIN --format=json   # contrato de invocação externa
```

### Teclas

O painel ativo é o de moldura acesa; a barra inferior mostra as teclas que
funcionam nele.

| Tecla | Ação |
|---|---|
| `↑` `↓` | mover na lista / rolar o texto |
| `Enter` | avançar (categoria → verbetes → texto) |
| `F2` | abrir as referências cruzadas ("Ver também") |
| `F3` ou `/` | busca incremental |
| `Backspace` | voltar |
| `Tab` | alternar painel |
| `Esc` | sair |

## Conteúdo atual

108 verbetes em português — ver [INDEX.md](INDEX.md).

| Categoria | Verbetes | Origem |
|---|---|---|
| Panorama | 7 | autoral |
| Blocos | 7 | autoral |
| Tipos de campo | 10 | gerado do compilador |
| Modificadores | 8 | autoral |
| Ligação entre projetos | 1 | gerado do compilador |
| Ecossistema | 4 | capturado do `--help` dos módulos |
| Diagnósticos | 71 | gerado do compilador |

## Como o conteúdo é mantido

```
synesis_help/entries/
├── _generated/pt/     # gerado do compilador — NUNCA editar à mão
└── authored/pt/       # conteúdo humano — é aqui que você escreve
```

O que o compilador sabe sobre si mesmo (matriz tipo×propriedade, códigos de erro,
mensagens de diagnóstico) é **derivado por sondagem**, nunca copiado. Assim o guia não
pode divergir do compilador: se uma regra muda, a regeneração reflete.

O que exige julgamento metodológico — para que serve cada tipo, quando usar, exemplos —
é autoral, e vive separado.

---

# Escrevendo no guia

## Corrigir um texto existente

1. **Descubra o arquivo.** O nome é o `id` do verbete, mostrado no rodapé do
   índice e no `lookup`:

   ```bash
   synesis-help lookup TYPE_CHAIN --format=json | head -3
   ```

2. **Verifique de onde ele vem.** Se o caminho contém `_generated/`, **não
   edite**: a regeneração vai desfazer. Veja [Corrigir um verbete gerado](#corrigir-um-verbete-gerado).

3. **Edite** o `.md` em `synesis_help/entries/authored/pt/`.

4. **Reconstrua e confira:**

   ```bash
   python tools/validate_entries.py   # links, ids, frontmatter
   python tools/check_examples.py     # exemplos ainda compilam
   synesis-help build                 # regrava o índice
   ```

> O guia lê o índice compilado, não os `.md`. **Sem `build`, sua edição não
> aparece.**

## Acrescentar um verbete novo

Crie `synesis_help/entries/authored/pt/<ID>.md` — o nome do arquivo **é** o `id`:

````markdown
---
id: MOD_EXEMPLO
title: "EXEMPLO"
category: modifier
summary: "Uma frase. É o que aparece no índice."
syntax: "EXEMPLO <valor> [OPCIONAL <n>]"
see_also: [BLOCK_FIELD, SYNESIS_E020]
source: authored
order: 50
---

# EXEMPLO

## Descrição

O que é e para que serve.

## Sintaxe

```synesis
FIELD nome TYPE TEXT
    SCOPE ITEM
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Regras

- Uma regra por linha, citando o código do erro (`SYNESIS_E020`).

## Exemplo

```synesis
FIELD citacao TYPE QUOTATION
    SCOPE ITEM
END FIELD
```
````

Depois: `python tools/generate_index.py && synesis-help build`.

`order` define a posição dentro da categoria: menor vem primeiro, 100 é o
padrão, empate cai no alfabético. A ordem é **didática** — do panorama ao
detalhe — e não alfabética.

### Categorias válidas

`overview` · `block` · `field_type` · `modifier` · `linkage` ·
`ecosystem` · `glossary`

`block`, `field_type`, `modifier` e `linkage` **exigem** `syntax` no frontmatter
e uma seção `## Sintaxe` no corpo — o validador cobra.

### Convenção de `id`

| Categoria | Prefixo | Exemplo |
|---|---|---|
| Bloco | `BLOCK_` | `BLOCK_ONTOLOGY` |
| Tipo de campo | `TYPE_` | `TYPE_CHAIN` |
| Modificador | `MOD_` | `MOD_SCOPE` |
| Panorama | `GUIDE_` | `GUIDE_START` |
| Glossário | `GLOS_` | `GLOS_BIBREF` |
| Diagnóstico | o próprio código | `SYNESIS_E047` |

O `id` é a chave de tudo: cross-references, links e o contrato JSON. Escolha e
não mude — o título pode mudar à vontade.

## Corrigir um verbete gerado

Os 86 verbetes em `_generated/` vêm do compilador (82 dele; 4 do
`--help` dos módulos, via `generate_ecosystem.py`). Editá-los é inútil: a
próxima regeneração sobrescreve, e o CI acusa (`generate_entries.py --check`).

| O que está errado | Onde corrigir |
|---|---|
| A regra em si (o que é obrigatório/proibido) | `synesis/` — é o compilador que decide |
| A mensagem do erro | `synesis/ast/results.py`, no `to_diagnostic()` |
| A frase de resumo do tipo | `tools/generate_entries.py`, dicionário `TYPE_SUMMARY` |
| Rótulos ("Obrigatório", "Sintaxe") | `tools/generate_entries.py`, dicionário `L` |

Para **acrescentar** prosa a um verbete gerado, crie um arquivo com o **mesmo
`id`** em `authored/pt/`. O build funde os dois, e o autoral vence.

## Regras de escrita

**Acentuação.** Escreva com acentos. Se esquecer:

```bash
python tools/fix_accents.py --check   # relata
python tools/fix_accents.py           # corrige
```

Só a prosa é tocada — código, crases e campos técnicos do frontmatter ficam
intactos.

**Blocos de código.** Máximo **72 colunas**, recuo de 4 espaços, sem TAB. Todo
exemplo que começa com `TEMPLATE` ou `FIELD` é **compilado de verdade** contra o
`synesis` instalado. Se não compilar, o CI falha — é proposital: exemplo errado
no guia é pior que exemplo ausente.

**Registro.** Este é um guia de *referência* (Diátaxis): descreve a máquina,
sucinta e ordenadamente. Tutorial, discussão metodológica e estudo de caso
pertencem a `synesis-docs-sources`.

**`see_also`.** Só `id`s existentes — link quebrado falha o build, não vira 404
silencioso.

## Ferramentas

```bash
python tools/fix_accents.py --check        # acentuação da prosa autoral
python tools/generate_entries.py           # gera entries derivadas
python tools/generate_ecosystem.py         # captura o --help dos módulos
python tools/generate_entries.py --check   # falha se houver drift (CI)
python tools/generate_index.py             # gera INDEX.md
python tools/validate_entries.py           # frontmatter, ids únicos, links
python tools/check_examples.py             # exemplos compilam de verdade
```

`check_examples.py` compila cada exemplo contra o `synesis` instalado. É o que impede
que um exemplo escrito hoje apodreça em silêncio quando o compilador evoluir.

## Localização

O guia é em português. A estrutura está pronta para outros idiomas (diretório por
locale, `id` invariante, rótulos em catálogo), mas a tradução está **bloqueada** pelo
compilador: as mensagens de diagnóstico vêm de `results.py` em português, e traduzi-las
por fora criaria uma segunda fonte de verdade. Ver §7 do estudo.

## Instalação

```bash
pip install synesis-help
```

Requer Python 3.10+ e o compilador `synesis` 0.11.0+, que vem como dependência
— os verbetes derivados são gerados por sondagem dele.

A partir do repositório:

```bash
git clone https://github.com/synesis-lang/synesis-help
cd synesis-help
pip install -e ".[dev]"
synesis-help build     # compila o índice a partir das entries
```

O índice (`guide.db`) não é versionado: é construído na primeira execução, ou
por `synesis-help build` depois de editar um verbete.

## Relação com o ecossistema

Depende de [`synesis`](https://github.com/synesis-lang/synesis) e importa
`synesis.language_info` e `synesis.ast.results` como fonte de verdade derivada.

## Licença

Distribuído sob a **GNU Affero General Public License, versão 3 apenas
(AGPL-3.0-only), com a Exceção de Saída de Dados Synesis** — ver
[LICENSE](LICENSE) e [LICENSE.exception](LICENSE.exception).

Identificador SPDX: `LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception`

**O que você extrai do guia é seu.** O texto que você copia de um verbete para
o seu template, script ou artigo não é coberto pela AGPL e não carrega
obrigação de copyleft em relação ao Synesis. A exceção existe para que o guia
possa ser usado como fonte de consulta sem contaminar o trabalho de quem
consulta. Ver `LICENSE.exception`.

O copyleft vale para o **guia como software**: modificá-lo e distribuí-lo — ou
oferecê-lo como serviço em rede — exige publicar o código sob a mesma licença.

## Como citar

De Britto, C. M. (2026). *synesis-help: guia de referência da linguagem
Synesis* (versão 0.1.0) [Software]. https://github.com/synesis-lang/synesis-help

Ver [CITATION.cff](CITATION.cff) — o GitHub o lê e oferece a citação pronta.
