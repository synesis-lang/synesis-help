---
id: TYPE_SCALE
title: "SCALE"
category: field_type
summary: "Valor numérico dentro de um intervalo declarado."
syntax: FIELD <nome> TYPE SCALE SCOPE <escopo> FORMAT [<min>..<max>] [...] END FIELD
see_also: [SYNESIS_E051, SYNESIS_E055, SYNESIS_E056, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 90
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SCALE

## Sintaxe

```synesis
FIELD <nome> TYPE SCALE
    SCOPE <escopo>
    FORMAT [<min>..<max>]
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_scale TYPE SCALE
    SCOPE ITEM
    FORMAT [0..5]
END FIELD
```

## Propriedades

| Propriedade | Situação | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `ARITY` | Proibido | SYNESIS_E055 |
| `RELATIONS` | Proibido | SYNESIS_E056 |
| `VALUES` | Proibido | SYNESIS_E086 |
| `FORMAT` | Obrigatório | SYNESIS_E051 |

## Regras

- **`FORMAT` é obrigatório.** O campo 'nome_do_campo' e do tipo SCALE, mas nao declara o intervalo

## Ver também

`SYNESIS_E051`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
