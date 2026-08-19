---
id: TYPE_ORDERED
title: "ORDERED"
category: field_type
summary: "Valor escolhido de uma lista fechada, com ordem."
syntax: FIELD <nome> TYPE ORDERED SCOPE <escopo> VALUES ... END VALUES [...] END FIELD
see_also: [SYNESIS_E049, SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 80
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# ORDERED

## Sintaxe

```synesis
FIELD <nome> TYPE ORDERED
    SCOPE <escopo>
    VALUES ... END VALUES
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_ordered TYPE ORDERED
    SCOPE ITEM
    VALUES
        [1] baixo: intensidade baixa
        [2] alto: intensidade alta
    END VALUES
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
| `VALUES` | Obrigatorio | SYNESIS_E049 |

## Regras

- **`VALUES` e obrigatorio.** O campo 'nome_do_campo' e do tipo ORDERED, mas nao define um bloco

## Ver tambem

`SYNESIS_E049`, `SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
