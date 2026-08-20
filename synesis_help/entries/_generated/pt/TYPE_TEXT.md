---
id: TYPE_TEXT
title: "TEXT"
category: field_type
summary: "Texto curto de uma linha."
syntax: FIELD <nome> TYPE TEXT SCOPE <escopo> [...] END FIELD
see_also: [SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 40
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# TEXT

## Sintaxe

```synesis
FIELD <nome> TYPE TEXT
    SCOPE <escopo>
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_text TYPE TEXT
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
