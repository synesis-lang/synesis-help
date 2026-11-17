---
id: BLOCK_EXPORT
title: "EXPORT"
category: block
summary: "Declara os artefatos do projeto (JSON, CSV, XLS, OKF, SKOS) e executa todos com synesis export."
syntax: "EXPORT <formato> [<nome>] OUTPUT \"<arquivo>\" [<propriedade> <valor>] [MAP RELATIONS <relações> TO <papel>] END EXPORT"
file: ".synp"
see_also: [BLOCK_PROJECT, MOD_ROLE, BLOCK_ONTOLOGY, SYNESIS_E094, SYNESIS_E095, SYNESIS_E099, SYNESIS_E122, SYNESIS_E127, SYNESIS_E150, SYNESIS_E153]
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
END EXPORT
```

`[ ]` opcional · `<>` valor a substituir

| Formato | Obrigatórias | Opcionais |
|---|---|---|
| `JSON`, `OKF` | `OUTPUT` | `GENERATED_AT` |
| `CSV`, `XLS`, `ALPACA` | `OUTPUT` | — |
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

## Regras

- Formato desconhecido é erro (`SYNESIS_E094`); propriedade fora das aceitas
  pelo formato também (`SYNESIS_E095`, `SYNESIS_E096`).
- `MAP RELATIONS` só existe em `SKOS` (`SYNESIS_E099`) e só com relações
  declaradas nas `RELATIONS` dos campos `CHAIN` (`SYNESIS_E122`).
- `ALIAS_LABEL` aceita `HIDDEN` ou `ALTERNATIVE` (`SYNESIS_E150`).
- Um IRI do registro sem bloco nem `USE` que o substitua é aviso
  (`SYNESIS_E153`): o conceito publicado sumiu sem sucessor.

## Ver também

`MOD_ROLE`, `BLOCK_ONTOLOGY`, `BLOCK_PROJECT`
