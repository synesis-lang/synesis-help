---
id: TYPE_TOPIC
title: "TOPIC"
category: field_type
summary: "Termo unico, sem espacos, para agrupar unidades."
syntax: FIELD <nome> TYPE TOPIC SCOPE <escopo> [...] END FIELD
see_also: [SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 60
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# TOPIC

## Sintaxe

```synesis
FIELD <nome> TYPE TOPIC
    SCOPE <escopo>
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_topic TYPE TOPIC
    SCOPE ITEM
END FIELD
```

## Propriedades

| Propriedade | Situacao | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `ARITY` | Proibido | SYNESIS_E055 |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `RELATIONS` | Proibido | SYNESIS_E056 |
| `VALUES` | Proibido | SYNESIS_E086 |

## Regras

- Nenhuma propriedade obrigatoria. O campo funciona apenas com `SCOPE`.

## Ver tambem

`SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
