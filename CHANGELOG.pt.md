# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e o projeto adota [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

**Idioma:** [English](CHANGELOG.md) | [Português](CHANGELOG.pt.md)

---

## [0.3.0] — 2026-11-17

O guia passa a sair em português — 183 verbetes — cobrindo o
synesis 0.15.

### Adicionado

- **`MOD_ROLE`**: a função de um campo de ONTOLOGY no modelo organizador
  (`LABEL`, `NOTE`, `HIERARCHY`, `USE`), com a propriedade SKOS de cada uma.
- **`BLOCK_QUESTIONS`, `BLOCK_PHASE`, `BLOCK_EXPORT`**: os blocos do `.synp`
  para questões de competência, o plano de produção executado por
  `synesis-coder phase` e os artefatos do projeto (SKOS com `MAP RELATIONS`,
  `ALIAS_LABEL`, `REGISTRY` e `synesis export --publish`; IRIs a partir do
  `NAMESPACE` do projeto).
- Verbetes gerados para os diagnósticos `SYNESIS_E089`–`SYNESIS_E157`.

### Alterado

- **`BLOCK_ONTOLOGY` explica os blocos ONTOLOGY como princípios
  organizadores**: o mesmo mecanismo serve a uma lista plana, um tesauro, uma
  taxonomia ou uma ontologia leve, e o compilador informa o perfil de cada
  projeto.
- **A saída da própria ferramenta é em inglês** (ajuda, `docs`, `credits`,
  rótulos da TUI). Os verbetes seguem no locale `pt`; os de diagnóstico citam
  as mensagens do compilador, que agora são em inglês.

### Corrigido

- `tools/generate_entries.py` não escapa mais as aspas duas vezes em resumos
  com `:` (`SYNESIS_E091`, `SYNESIS_E092`).

## [0.2.1] — 2026-08-24

### Alterado

- **O verbete do `synesis-graph` agora cobre o `ProjectContext`.** Desde o
  `synesis-graph` 0.8.0, exportar para um banco grava também o contexto do
  próprio projeto no grafo: a `DESCRIPTION` do `.synp` e o template inteiro como
  documento legível — cada campo com tipo, escopo, descrição, escala de valores e
  **GUIDELINES**, mais as arestas do grafo com sua direção.

  O guia precisava dizer isso, porque muda o valor de escrever um bom template. O
  schema de um banco é sintaxe sem semântica: diz que existe um vértice `Aspect`
  com a propriedade `name`, mas não que `Aspect` é uma escala ordenada nem o que
  cada valor significa. As `GUIDELINES` que o pesquisador escreve são o seu
  protocolo de codificação — as regras de decisão que dizem o que conta como
  instância válida de um campo. Sem elas no grafo, quem consulta precisa inferir
  esse critério a partir dos dados.

  O `ECO_GRAPH` é gerado a partir do `--help` da ferramenta, então a explicação
  vive no campo `note` autoral do gerador, onde a regeneração a preserva.

- **O `GUIDE_ECOSYSTEM` ganhou a seção "O que o grafo leva junto"**, com o ponto
  que mais interessa a quem escreve um template: boas `GUIDELINES` rendem duas
  vezes — guiam o `synesis-coder` na anotação e viajam com o grafo depois.

- A regeneração dos verbetes de ecossistema também atualizou as versões
  registradas de `ECO_CODER`, `ECO_LSP` e `ECO_SYNESIS`, que estavam defasadas.

## [0.2.0] — 2026-08-20

O guia passa a sair em português — 110 verbetes — com os dois novos
diagnósticos do compilador abaixo. Exige `synesis>=0.12.0`, que os introduz.

### Adicionado

- **`SYNESIS_E087` e `SYNESIS_E088`**, regerados a partir do compilador. Eles
  governam os dois lados da distinção índice/rótulo em vocabulários fechados:
  `E087` recusa o prefixo de índice `[N]` num bloco `VALUES` de `ENUMERATED`
  (que não tem ordem, logo não tem índice), e `E088` recusa escrever o rótulo
  onde um campo `ORDERED` espera o índice.

- **Seção "Valor na anotação"** em `TYPE_ORDERED` e `TYPE_ENUMERATED`. As
  entradas geradas descreviam como cada tipo se *declara*, mas nunca o que se
  *escreve* na anotação — justamente a distinção que os dois diagnósticos novos
  passam a exigir. Ambas também passam a apontar para o seu diagnóstico.

### Corrigido

- **O exemplo de `ENUMERATED` ensinava sintaxe inválida.** O trecho de `VALUES`
  era compartilhado pelos dois tipos de vocabulário fechado e trazia `[1]`/`[2]`,
  hoje `SYNESIS_E087` em `ENUMERATED`. O trecho passa a variar por tipo:
  `ORDERED` mantém a forma indexada (que exige), `ENUMERATED` a dispensa.

  O `tools/check_examples.py` pega essa classe de defasagem — ele compila todo
  exemplo `FIELD` e apontou o bloco pelo código do erro.

---

## [0.1.0] — 2026-08-18

Primeira publicação: conteúdo, índice e TUI.

O guia sai com 108 verbetes em português. 86 deles são **derivados** — 82 por
sondagem do compilador (`synesis.language_info`, `synesis.ast.results`) e 4 do
`--help` de cada módulo instalado —, de modo que a documentação não pode
divergir do que as ferramentas de fato fazem. Os 22 restantes são autorais e
cobrem o que exige julgamento metodológico: para que serve cada construção,
quando usá-la e exemplos trabalhados.

### Adicionado

**Conteúdo — 108 verbetes em português**

- 71 diagnósticos, 10 tipos de campo e 1 verbete de ligação **derivados do
  compilador** por sondagem de `synesis.language_info` e
  `synesis.ast.results`. Nunca escritos à mão: mudança de regra no compilador
  é refletida pela regeneração.
- 20 verbetes autorais: blocos da linguagem (`PROJECT`, `TEMPLATE`, `FIELD`,
  `SOURCE`, `ITEM`, `ONTOLOGY`, `<ESCOPO> FIELDS`), modificadores (`SCOPE`,
  `GUIDELINES`, `DESCRIPTION`, `INCLUDE`, `BUNDLE`, `METADATA`,
  `IDENTIFIES`/`REFERS TO`, `ON BIBLIOGRAPHY`/`ON DATASET`) e sete panoramas
  (`GUIDE_START`, `GUIDE_FILES`, `GUIDE_PRIMITIVES`, `GUIDE_CHAINS`,
  `GUIDE_MULTIPROJECT`, `GUIDE_ECOSYSTEM`, `GUIDE_REVIEW`).
- **`GUIDE_REVIEW`** documenta o pipeline de revisão do `synesis-coder`
  (`anchor` → `critique` → `normalize` → `incorporate`). É a etapa que o
  pesquisador mais tende a pular e menos pode pular: anotação gerada por LLM
  compila sem erro e ainda assim afirma o que a fonte não sustenta. O verbete
  diz o que cada fase lê e escreve, quais delas chamam LLM, e por que o
  `incorporate` rejeita correção ambígua em vez de adivinhar o alvo.
- **`.synr` acrescentado à tabela de extensões** do `GUIDE_FILES`, com a razão
  de ser a única que nunca aparece num `INCLUDE`: é artefato de trabalho do
  `synesis-coder`, não parte do projeto.
- Todo verbete de referência apresenta a **sintaxe completa** — obrigatório sem
  colchetes, opcional entre `[ ]`, alternativas com `|` — na convenção clássica
  dos guias de referência. Nada de `...` no lugar da estrutura.

**Ferramentas**

- `tools/generate_entries.py` — gera as entries derivadas; `--check` falha se
  houver divergência (trava de CI).
- `tools/generate_index.py` — monta o `INDEX.md`, o índice mestre.
- `tools/validate_entries.py` — frontmatter, `id` único, integridade do grafo
  de referências cruzadas e presença de seção de sintaxe nos verbetes de
  referência.
- `tools/check_examples.py` — compila cada exemplo contra o `synesis`
  instalado e cobra o estilo dos blocos de código (72 colunas, recuo de 4, sem
  TAB, sem espaço no fim).
- `tools/generate_ecosystem.py` — gera os verbetes `ECO_*` a partir do
  `--help` de cada módulo instalado, de modo que um subcomando novo chega ao
  guia por regeneração, não por transcrição. `--check` falha se houver
  divergência.
  - **Valores resolvidos do ambiente são omitidos.** `synesis-coder --help`
    imprime `(Current: <modelo>)`, que é o modelo configurado NA MÁQUINA que
    gerou o verbete — não uma propriedade do pacote. Passa a ser
    `(Current: set by SYNESIS_CODER_MODEL)`: o verbete documenta *como* se
    define o valor em vez de publicar o `.env` de quem gerou, e deixa de mudar
    a cada regeneração em outra máquina.
  - **`generate_entries.py --check` não acusa mais os `ECO_*` como órfãos.**
    Os dois geradores gravam em `entries/_generated/pt/` e cada um só conhece
    a própria saída, então o check ficava permanentemente vermelho — e um
    check sempre vermelho é um check ignorado, que é justamente o que
    esconderia um órfão de verdade.

**Integração contínua**

- `.github/workflows/ci.yml` — testes em 3 versões de Python x 3 sistemas
  operacionais, lint, auditoria de dependências, varredura de segredos, build
  e publicação no PyPI em tags `v*`. GitHub Actions pinadas por SHA de commit.
- **Job `content`** — a verificação de que este pacote precisa e os outros
  não: 86 dos seus 108 verbetes são *derivados* do compilador e do `--help`
  dos módulos irmãos. Um verbete que discorda da ferramenta é pior que verbete
  ausente, porque o pesquisador confia no que lê. Roda `validate_entries`,
  `check_examples`, `generate_entries --check` e `generate_index --check`.
  - `generate_ecosystem.py --check` **não** entra no CI, deliberadamente: ele
    lê o `--help` dos módulos irmãos, que não estão instalados no runner —
    compararia o verbete contra a ausência da ferramenta e falharia sempre.
- **`tools/check_wheel.py`** — garante que as entries entraram no wheel. Um
  wheel sem elas instala sem erro, o comando roda, e o guia responde "nada
  encontrado" para tudo: falha silenciosa, a pior classe.
- `.github/workflows/cla.yml` — CLA Assistant, com as assinaturas centralizadas
  em `synesis-lang/cla-signatures`.
- `.github/dependabot.yml` — PRs de versão desligados, como no restante do
  ecossistema; os *security updates* seguem ativos.
- **Ruff configurado** com a base do ecossistema (`select = ["F", "I"]`).
  Rodar o ruff sem configuração acusava 23 achados, nenhum deles um defeito —
  e um CI vermelho no primeiro commit ensina a ignorar o CI.

**Pacote**

- `synesis_help.index` — compila as entries Markdown em SQLite + FTS5.
- `synesis_help.render` — renderiza o corpo dos verbetes com cor por papel.
- `synesis_help.app` — TUI em Textual: barra de título, dois painéis, barra de
  teclas.
- `synesis_help.cli` — `build`, `lookup`, `lookup --format=json` e a TUI como
  comando padrão.
- Teclas: `↑`/`↓` movem, `Enter` abre, `F2` abre as referências cruzadas, `F3`
  (ou `/`) busca incremental, `Backspace` volta, `Tab` alterna painel, `Esc`
  sai.

### Navegação (revisão após o primeiro teste de uso)

Era difícil saber qual painel estava ativo: o item destacado ficava ciano tanto
no painel com foco quanto sem. Três pistas redundantes de foco, usando
recursos que o terminal moderno oferece e o DOS não tinha:

- **Moldura acesa.** Cada painel tem borda e título próprios; o ativo acende.
  É a pista que o olho encontra antes de ler.
- **Barra de seleção só no painel ativo.** No painel inativo a seleção fica
  apenas marcada, sem barra — mostra "onde você estava", não
  "onde você está".
- **Rodapé contextual.** A barra de teclas passa a listar o que funciona no
  painel com foco (`↑↓ Categoria` · `↵ Ir aos verbetes` em Categorias;
  `↑↓ Verbete` · `↵ Ler` · `F2 Ver também` em Verbetes; `↑↓ Rolar` no corpo).

Também: `Enter` numa categoria agora avança para a lista de verbetes (antes não
fazia nada, travando a navegação por teclado), o painel de conteúdo virou
região rolável e focável, e a tabela do corpo passou a respeitar a largura do
painel em vez de quebrar linha.

### Referências cruzadas acionáveis

"Ver também" era texto inerte — justamente o gesto que definia o Norton
Guides. Agora cada referência é navegável de três formas:

- **Clique do mouse**, no item de "Ver também" ou em qualquer `` `REF` ``
  citada no meio do texto.
- **Teclas `1`–`9`**, pelo número exibido à esquerda de cada referência.
- **`F2`**, que traz todas para a lista lateral.

`Backspace` volta em qualquer caso.

> A causa da inércia era dupla: o Textual 3.x descarta `meta` ao converter
> `rich.Text` em `Content`, e a ação precisava do namespace `app.` para ser
> resolvida no App em vez de no widget clicado.

### Paleta "Retro-Editorial"

A silhueta é dos anos 80; as cores, não. Saem o azul e o amarelo puros do CGA
— vibrantes, mas agressivos numa tela de LCD — e entra uma paleta em que cada
cor carrega um **papel na hierarquia da informação**, nunca decora:

| Papel | Cor |
|---|---|
| Fundo | midnight blue `#1B2233` — profundidade sem preto absoluto |
| Corpo | prata `#D6DCE8` |
| Cabeçalhos | ciano brilhante `#5FD7E4` + negrito — ancoragem ao rolar |
| Palavras-chave | amarelo dourado `#E8C161` + negrito |
| Placeholders | verde menta `#8FD9A8` + *itálico* — "isto você digita" |
| Diagnósticos | laranja coral `#F08A63` |
| Referências | azul celeste `#7FB4E8`, sem sublinhado; inverte no foco |
| Símbolos (`[ ]`, `<`, `·`) | cinza médio `#7A849B` |

A distinção **keyword × placeholder** é o ganho central: dourado diz "isto é do
sistema", verde itálico diz "isto você substitui". Vale no bloco de sintaxe e
no código inline.

As constantes são nomeadas pelo papel (`C_KEYWORD`, `C_PLACEHOLDER`), não pela
cor — trocar a paleta não exige tocar no CSS nem no renderizador. Um teste
trava a hierarquia para que ela não se degrade em edições futuras.

### Realce de sintaxe nos blocos de código

Os blocos de código deixam de ser uma mancha de uma cor só e passam a
distinguir os mesmos papéis que um editor distingue:

| Elemento | Cor |
|---|---|
| Palavras-chave (`FIELD`, `END`, `TYPE`…) | amarelo dourado |
| Identificadores do pesquisador | prata (neutro, para a keyword saltar) |
| Comentários (`# ...`) | cinza médio *itálico* |
| Strings (`"..."`) | rosa suave |
| Referências (`@silva2024`) | azul celeste *itálico* |
| Placeholders (`<nome>`) | verde menta *itálico* |
| Diagnósticos (`SYNESIS_E047`) | laranja coral |

As **42 palavras-chave são lidas da gramática** do compilador instalado
(`synesis.lark`), não de uma lista paralela — mesma disciplina do resto do
projeto: uma palavra nova na linguagem passa a ser realçada sem que ninguém
edite o guia.

### Acentuação e nome de campo

- **Prosa autoral acentuada.** Os 20 verbetes escritos à mão foram corrigidos
  (333 palavras). A ferramenta `tools/fix_accents.py` usa o dicionário
  português do `pyspellchecker` e só aceita a sugestão quando ela é **a mesma
  palavra acentuada** — nunca uma troca por outra ("template" → "empate").
  Blocos de código, trechos entre crases e os campos técnicos do frontmatter
  (`id`, `see_also`, `syntax`) ficam intactos: um acento dentro de um exemplo
  o tornaria inválido.
- **Os 82 verbetes gerados ficam sem acento**, deliberadamente. Reproduzem a
  prosa de `to_diagnostic()`, que hoje também é sem acento; corrigi-los aqui
  criaria uma segunda verdade e a regeneração desfaria o trabalho. A
  acentuação de `results.py` é projeto do compilador.
- **Nome de campo em cor própria.** Em `papel: mediador`, o nome pertence ao
  template (estrutura) e o valor é dado do pesquisador — agora se distinguem.
  Resolve também um erro sutil: um campo chamado `code` era pintado como a
  keyword `CODE` da linguagem.

### Ecossistema no guia

Cinco verbetes novos sobre as ferramentas ao redor da linguagem: `synesis`
(compilador), `synesis-lsp`, `synesis-coder`, `synesis-graph`, mais um
panorama (`O ecossistema`) com o fluxo de trabalho e o que cada ferramenta
consome.

O conteúdo é **capturado do `--help` de cada módulo instalado**, não
transcrito — `tools/generate_ecosystem.py`. Se o `synesis-coder` ganhar um
subcomando, ele aparece na próxima regeneração.

O que é filtrado na captura: caminhos do interpretador local, versão do
Python e linhas de log. O `--help` do language server imprime o caminho do
próprio executável; incluí-lo tornaria o guia diferente para cada pessoa que
o gerasse.

### Ordem de apresentação

Os verbetes eram listados em **ordem alfabética**, o que punha "Por onde
começar" em 4º lugar e `DATE` antes de `CODE` — nenhum dos dois ajuda quem
chega agora. A ordem passa a ser **editorial**, via campo `order` no
frontmatter (menor primeiro; 100 é o padrão; empate cai no alfabético):

- **Panorama:** Por onde começar → Arquivos → Primitivos → Cadeias →
  Projetos conectados (do primeiro contato ao tópico avançado).
- **Blocos:** PROJECT → TEMPLATE → FIELDS → FIELD → SOURCE → ITEM → ONTOLOGY
  (a ordem em que se escreve um projeto).
- **Tipos:** QUOTATION, CODE, MEMO, TEXT, CHAIN antes de ENUMERATED, SCALE,
  DATE (uso corrente antes do especializado).

Vale igualmente na TUI e no `INDEX.md`.

### Acabamento tipográfico

- **`♦` na categoria ativa** e **`►` no verbete selecionado**. O CSS não dava
  conta — `border-left` pinta todos os itens, não só o destacado —, então o
  marcador entra no próprio texto do rótulo.
- **"Ver também" em grid de diamantes**, com a glosa alinhada em coluna fixa e
  sem sublinhado: o `♦` e o alinhamento já marcam o item.
- **Bullets tipográficos** (`•`) no lugar do hífen do Markdown.

### Acabamento visual

- **Molduras arredondadas** (`╭─╮`) nos três painéis — o toque moderno sobre a
  base vintage.
- **Contador de posição** no título da moldura (`Verbetes 2/10`), e o título
  muda conforme a origem da lista (categoria, busca ou referências).

### Corrigido durante o teste

- **Tabelas cortavam texto.** As colunas tinham largura fixa, então
  "ponto de entrada; amarra tudo" virava "…amarra tud…" mesmo sobrando espaço
  à direita. Agora a tabela é medida como bloco: cada coluna pede o que
  precisa e, se a soma exceder a largura, o excedente sai da coluna mais
  larga. A medição usa o texto **já renderizado** — contar as crases e
  asteriscos da marcação desalinhava a coluna seguinte.
- **Listas numeradas viravam um parágrafo colado.** `1.` `2.` `3.` não eram
  reconhecidas como itens e o reagrupamento de parágrafos as unia numa linha
  só. Agora cada item abre parágrafo próprio, com a continuação alinhada sob
  o texto e não sob o número.
- **Captura do language server era intermitente.** O `synesis-lsp` passa a
  ouvir a entrada padrão logo após imprimir a ajuda e, sem `stdin` fechado,
  ficava bloqueado até o timeout — o verbete saía ou não conforme a execução.
- **`F10 Créditos` não aparecia no rodapé.** A barra de teclas foi editada
  depois que o atalho entrou, e a substituição mirou um texto já alterado. O
  rodapé agora separa as teclas do painel ativo das globais, e cabe em 80
  colunas — antes a linha chegava a 102 e o `Esc` sumia em terminal estreito.
- **"Ver também" duplicado.** A seção vinha duas vezes: uma do corpo Markdown,
  outra montada a partir de `see_also`. O renderizador agora suprime a do
  corpo e mantém só a acionável.
- **Busca (F3) com moldura dupla e sem linha de base.** O `Input` do Textual já
  desenha a própria borda e havia outra em volta; além disso o campo era
  declarado antes da barra de status e, com `dock: bottom`, acabava por baixo
  dela. Virou uma linha só, acima do rodapé, com as teclas no placeholder.
- **`**negrito**` aparecia cru.** Duas causas: o negrito podia envolver
  `` `código` `` (a varredura em duas passagens quebrava o par) e podia
  atravessar a quebra de linha do Markdown fonte. Agora a marcação é resolvida
  numa varredura única, os parágrafos são reunidos antes de renderizar, e a
  quebra ocorre **depois** da estilização — quebrar antes partia o negrito ao
  meio.

- **As entries não iam no pacote.** Ficavam em `entries/` na raiz do
  repositório, fora de `synesis_help/`, então o wheel saía sem conteúdo: quem
  instalasse via `pip` teria o comando sem guia. Movidas para
  `synesis_help/entries/` e declaradas em `package-data`. Verificado instalando
  o wheel num ambiente virgem.
- **Busca privilegiava o texto mais longo.** Procurar "chain" devolvia
  `SYNESIS_E056` antes de `TYPE_CHAIN`, porque o FTS5 pontua por frequência do
  termo. A ordenação agora põe casamento de título à frente do ranking.
- **Comentário HTML vazava no corpo.** O aviso "GERADO AUTOMATICAMENTE"
  aparecia na TUI e no JSON do `lookup`. Removido na indexação.
- **IDs duplicados ao trocar de categoria.** `ListView.clear()` é assíncrono no
  Textual e o lote seguinte era inserido antes da remoção. Os ids passaram a
  ser rastreados num array paralelo ao índice do widget.

### Notas

- **Somente português.** A tradução está *bloqueada* pelo compilador, não
  apenas adiada: a prosa dos diagnósticos vem de `results.py` em português, e
  traduzi-la aqui criaria uma segunda fonte de verdade. A estrutura já está
  pronta (diretório por locale, chave `(id, locale)`, catálogo de rótulos,
  cadeia de seleção de idioma), de modo que acrescentar um idioma depois seja
  tradução, não refatoração.
- Verbetes sobre `VALUES` fora de `ORDERED`/`ENUMERATED` e sobre
  `CONTEXT FROM DATASET` estão deliberadamente ausentes, à espera de decisão de
  produto no compilador.

### Achados reportados ao núcleo

Registrados em `synesis-planning/synesis-help/achados_geracao_2026-08-08.md`:

- `SYNESIS_E064` é compartilhado por três classes de erro distintas — o único
  código que não é 1:1 entre os 71.
- O guia de referência oficial (Apêndice A de `guia_referencia.qmd`) mostra os
  metadados de template em linha própria, o que **não compila**; a gramática
  exige que fiquem inline no header do `TEMPLATE`.

---

[0.3.0.dev0]: https://github.com/synesis-lang/synesis-help/compare/v0.2.1...HEAD
[0.3.0]: https://github.com/synesis-lang/synesis-help/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/synesis-lang/synesis-help/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/synesis-lang/synesis-help/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/synesis-lang/synesis-help/releases/tag/v0.1.0
