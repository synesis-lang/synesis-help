---
id: TYPE_CODE
title: "CODE"
category: field_type
summary: "Um ou mais conceitos da ontologia atribuídos à unidade."
syntax: FIELD <nome> TYPE CODE SCOPE <escopo> [...] END FIELD
see_also: [SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CHAIN]
source: generated
order: 20
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# CODE

## Sintaxe

```synesis
FIELD <nome> TYPE CODE
    SCOPE <escopo>
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_code TYPE CODE
    SCOPE ITEM
END FIELD
```

## Propriedades

| Propriedade | Situação | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `ARITY` | Proibido | SYNESIS_E055 |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `RELATIONS` | Proibido | SYNESIS_E056 |
| `VALUES` | Proibido | SYNESIS_E086 |

## Regras

- Nenhuma propriedade obrigatória. O campo funciona apenas com `SCOPE`.

## Ver também

`SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CHAIN`
