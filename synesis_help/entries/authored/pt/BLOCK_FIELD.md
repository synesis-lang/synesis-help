---
id: BLOCK_FIELD
title: "FIELD"
category: block
summary: "Define um campo: nome, tipo, escopo e regras de preenchimento."
syntax: "FIELD <nome> TYPE <tipo> SCOPE <escopo> [DESCRIPTION ...] [...] END FIELD"
file: ".synt"
see_also: [BLOCK_TEMPLATE, MOD_SCOPE, MOD_GUIDELINES, TYPE_CODE, TYPE_CHAIN, SYNESIS_E022]
source: authored
order: 40
---

# FIELD

## Descrição

Um `FIELD` declara um campo da pesquisa. E a unidade mínima do template: nome,
tipo e escopo. O tipo determina quais propriedades adicionais são obrigatórias,
permitidas ou proibidas — consulte a entry do tipo escolhido.

## Sintaxe

```synesis
FIELD <nome> TYPE <tipo>
    SCOPE <SOURCE|ITEM|ONTOLOGY>
    [DESCRIPTION <texto>]
    [ARITY <operador> <n>]
    [FORMAT [<min>..<max>]]
    [RELATIONS ... END RELATIONS]
    [VALUES ... END VALUES]
    [IDENTIFIES <entidade>]
    [REFERS TO <entidade>]
    [CONTEXT FROM DATASET <campo>]
    [GUIDELINES ... END GUIDELINES]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

Nem toda propriedade vale para todo tipo — a matriz esta na entry de cada
`TYPE_*`. `SCOPE` e sempre obrigatório.

## Exemplo

```synesis
FIELD citacao TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION trecho literal que sustenta a analise
    GUIDELINES
        Extraia de 1 a 3 frases continuas.
        O trecho deve ser inteligivel sem o texto ao redor.
    END GUIDELINES
END FIELD
```

## Propriedades por tipo

Cada tipo aceita um conjunto próprio de propriedades. O compilador e a fonte
dessa regra — veja `TYPE_CHAIN`, `TYPE_SCALE`, `TYPE_ENUMERATED` e demais.

Universais, aceitas por qualquer tipo: `DESCRIPTION`, `GUIDELINES`,
`CONTEXT FROM DATASET`.

## Regras

- Campo usado num arquivo de dados sem `FIELD` correspondente e erro
  (`SYNESIS_E022`).
- Propriedade fora do tipo correto e barrada com mensagem especifica:
  `ARITY` so em CHAIN (`SYNESIS_E055`), `FORMAT` so em SCALE (`SYNESIS_E054`),
  `RELATIONS` so em CHAIN (`SYNESIS_E056`), `VALUES` so em ORDERED/ENUMERATED
  (`SYNESIS_E086`).
- `IDENTIFIES` e `REFERS TO` so existem em `SCOPE SOURCE` (`SYNESIS_E078`).

## Ver também

`BLOCK_TEMPLATE`, `MOD_SCOPE`, `MOD_GUIDELINES`, `TYPE_CODE`, `TYPE_CHAIN`
