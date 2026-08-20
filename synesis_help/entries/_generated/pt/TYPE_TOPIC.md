---
id: TYPE_TOPIC
title: "TOPIC"
category: field_type
summary: "Termo único, sem espaços, para agrupar unidades."
syntax: FIELD <nome> TYPE TOPIC SCOPE <escopo> [...] END FIELD
see_also: [SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 60
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

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

`SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
