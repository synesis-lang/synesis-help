---
id: BLOCK_EXPORT
title: "EXPORT"
category: block
summary: "Declara os artefatos do projeto (JSON, CSV, XLS, ALPACA, OKF, SKOS) e executa todos com synesis export."
syntax: "EXPORT <formato> [<nome>] OUTPUT \"<arquivo>\" [<propriedade> <valor>] [MAP RELATIONS <relações> TO <papel>] [MAP <campos> TO INSTRUCTION|INPUT|OUTPUT] END EXPORT"
file: ".synp"
see_also: [BLOCK_PROJECT, MOD_ROLE, BLOCK_ONTOLOGY, SYNESIS_E094, SYNESIS_E095, SYNESIS_E099, SYNESIS_E122, SYNESIS_E127, SYNESIS_E150, SYNESIS_E153, SYNESIS_E158, SYNESIS_E162, SYNESIS_E163, SYNESIS_I166]
source: authored
order: 77
requires_synesis: ">=0.15.0"
---

# EXPORT

## Descrição

Cada bloco `EXPORT` declara um artefato do projeto. `synesis export
projeto.synp` executa todos; `synesis export projeto.synp skos` executa só os
blocos daquele formato (ou daquele nome).

O formato **SKOS** publica o princípio organizador como vocabulário SKOS (um
sistema de organização do conhecimento) em Turtle (`.ttl`). Ele lê a função de cada campo nas linhas `ROLE` do template:
rótulos, definição, hierarquia.

## Sintaxe

```synesis
EXPORT <formato> [<nome>]
    OUTPUT "<arquivo>"
    [<propriedade> <valor>]
    [MAP RELATIONS <relação>[, <relação>] TO <papel>]
    [MAP <campo>[, <campo>] TO INSTRUCTION|INPUT|OUTPUT]
END EXPORT
```

`[ ]` opcional · `<>` valor a substituir

| Formato | Obrigatórias | Opcionais |
|---|---|---|
| `JSON`, `OKF` | `OUTPUT` | `GENERATED_AT` |
| `CSV`, `XLS` | `OUTPUT` | — |
| `ALPACA` | `OUTPUT` | `INSTRUCTION` |
| `SKOS` | `OUTPUT`, `NAMESPACE`, `LANGUAGE` | `GENERATED_AT`, `MIN_SOURCES`, `ALIAS_LABEL`, `REGISTRY` |

## Exemplo

```synesis
EXPORT SKOS corroborado
    OUTPUT "saida/fraudes.ttl"
    NAMESPACE "https://example.org/id/fraudes/"
    LANGUAGE pt-BR
    MIN_SOURCES 2
    MAP RELATIONS TIPO_DE TO HIERARCHY KIND
    MAP RELATIONS MITIGA, EXPLORA TO RELATED
END EXPORT
```

## SKOS

- **IRIs:** cada conceito recebe `NAMESPACE` + `concept/` + nome. O
  `NAMESPACE` é do projeto: um domínio que a equipe controla, terminado em `/`
  ou `#` (`SYNESIS_E127`).
- **`MAP RELATIONS`:** leva relações da `CHAIN` (o que as fontes afirmam) a um
  papel **só neste artefato**: `HIERARCHY KIND|PART|INSTANCE` ou `RELATED`.
  O `.syno`, os painéis e o grafo não veem esse mapeamento.
- **`MIN_SOURCES`:** número mínimo de fontes distintas que afirmam o par para
  ele entrar no arquivo.
- **`ALIAS_LABEL HIDDEN|ALTERNATIVE`:** como o nome de um bloco preterido
  (`USE`) entra no alvo; o padrão é `HIDDEN`.
- **`REGISTRY "<arquivo>"`** com `synesis export --publish`: registra os IRIs
  publicados. Um IRI já publicado cujo conceito virou preterido sai como
  obsoleto (`owl:deprecated`, `dcterms:isReplacedBy`) em vez de sumir.
  Com `--publish`, registro ilegível é erro (`SYNESIS_E152`) e nada é
  gravado; `OUTPUT` e `REGISTRY` no mesmo arquivo são sempre recusados
  (`SYNESIS_E157`).
- **Mudar o `NAMESPACE`** é decisão do pesquisador e não bloqueia nada: IRIs
  do registro em outro namespace saem só como aviso (`SYNESIS_E156`), porque
  ficam fora da conferência.

## ALPACA

Gera um JSONL para afinar modelos de linguagem: cada linha tem
`instruction`, `input` e `output`, as três como texto.

- **Sem `MAP` nem `INSTRUCTION`:** pares embutidos, escolhidos pelo
  compilador. Eles não levam o qualificador de um bundle com `CHAIN`
  (por exemplo, o estatuto), e o aviso `SYNESIS_I167` diz isso.
- **Com `MAP <campos> TO INSTRUCTION|INPUT|OUTPUT`** (desde a 0.16.0): o
  pesquisador declara quais campos formam cada chave. A instrução é
  um texto fixo (`INSTRUCTION`) ou um campo (`MAP <campo> TO
  INSTRUCTION`), nunca os dois.

```synesis
EXPORT ALPACA mecanismo
    OUTPUT "saida/mecanismo.jsonl"
    INSTRUCTION Identifique a relação causal no trecho.
    MAP trecho TO INPUT
    MAP chain, estatuto, justificativa TO OUTPUT
END EXPORT
```

- **Uma linha por quê:** um `BUNDLE` no mapa define as linhas, uma por
  ocorrência. Os campos fora dele são contexto, repetido em cada linha.
  Sem bundle, uma linha por `ITEM`.
- **Texto:** um campo na chave sai só com o valor; vários saem
  rotulados pelo nome, na ordem do `MAP`. A `CHAIN` entra com todas as
  triplas.
- **Cartão:** ao lado do JSONL, `<nome>.card.json` registra a
  composição, as contagens e os campos que ficaram de fora.

## Regras

- Formato desconhecido é erro (`SYNESIS_E094`); propriedade fora das aceitas
  pelo formato também (`SYNESIS_E095`, `SYNESIS_E096`).
- `MAP RELATIONS` só existe em `SKOS` (`SYNESIS_E099`) e só com relações
  declaradas nas `RELATIONS` dos campos `CHAIN` (`SYNESIS_E122`).
- `MAP <campos> TO` só existe em `ALPACA`, com os alvos `INSTRUCTION`,
  `INPUT` e `OUTPUT`, sem `FROM` (`SYNESIS_E165`). O `OUTPUT` é
  obrigatório (`SYNESIS_E158`), e há exatamente uma origem de instrução
  (`SYNESIS_E159`).
- Campo do `OUTPUT` também em `INPUT` ou `INSTRUCTION` é recusado
  (`SYNESIS_E162`): a resposta estaria no prompt.
- Campos de dois bundles no mesmo bloco são recusados (`SYNESIS_E163`).
- Parceiro qualificador do bundle fora do mapa é só informativo
  (`SYNESIS_I166`): o arquivo é gerado.
- `ALIAS_LABEL` aceita `HIDDEN` ou `ALTERNATIVE` (`SYNESIS_E150`).
- Um IRI do registro sem bloco nem `USE` que o substitua é aviso
  (`SYNESIS_E153`): o conceito publicado sumiu sem sucessor.

## Ver também

`MOD_ROLE`, `BLOCK_ONTOLOGY`, `BLOCK_PROJECT`
