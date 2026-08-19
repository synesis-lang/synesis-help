---
id: BLOCK_FIELDS_SPEC
title: "SOURCE / ITEM / ONTOLOGY FIELDS"
category: block
summary: "Lista quais campos são obrigatórios, opcionais ou pareados em cada escopo."
syntax: "<ESCOPO> FIELDS [REQUIRED|OPTIONAL|BUNDLE] <campo>[, ...] END <ESCOPO> FIELDS"
file: ".synt"
see_also: [BLOCK_TEMPLATE, BLOCK_FIELD, MOD_BUNDLE, MOD_SCOPE, SYNESIS_E020, SYNESIS_E039, SYNESIS_E057]
source: authored
order: 30
---

# SOURCE FIELDS / ITEM FIELDS / ONTOLOGY FIELDS

## Descrição

Enquanto `FIELD` **define** um campo, estes blocos dizem **quais campos valem
em cada escopo** e com que exigência.

## Sintaxe

```synesis
<SOURCE|ITEM|ONTOLOGY> FIELDS
    [REQUIRED <campo>[, <campo> ...]]
    [OPTIONAL <campo>[, <campo> ...]]
    [BUNDLE <campo>, <campo>[, ...]]
    [REQUIRED BUNDLE <campo>, <campo>]
    [<REQUIRED|OPTIONAL> <campo> ON BIBLIOGRAPHY]
    [<REQUIRED|OPTIONAL> <campo> ON DATASET "<arquivo>"]
END <SOURCE|ITEM|ONTOLOGY> FIELDS
```

`[ ]` opcional · `<>` valor a substituir · `|` alternativa

`ON BIBLIOGRAPHY` e `ON DATASET` valem apenas em `SOURCE FIELDS`.

## Exemplo

```synesis
ITEM FIELDS
    REQUIRED citacao, code
    OPTIONAL nota
    REQUIRED BUNDLE resumo, chain
END ITEM FIELDS
```

## Qualificadores

| Qualificador | Significado |
|---|---|
| `REQUIRED` | precisa estar presente no bloco (`SYNESIS_E020`) |
| `OPTIONAL` | pode aparecer ou não |
| `BUNDLE` | campos que so valem juntos — ver `MOD_BUNDLE` |

## Regras

- Um bloco por escopo (`SYNESIS_E057`).
- Campo listado precisa ter `FIELD` correspondente (`SYNESIS_E039`).
- `FIELD` definido precisa ser listado em algum bloco (`SYNESIS_E042`).
- O `SCOPE` do `FIELD` deve bater com o escopo do bloco (`SYNESIS_E006`).

## Ver também

`BLOCK_TEMPLATE`, `BLOCK_FIELD`, `MOD_BUNDLE`, `MOD_SCOPE`
