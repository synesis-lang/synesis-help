---
id: TYPE_ENUMERATED
title: "ENUMERATED"
category: field_type
summary: "Valor escolhido de uma lista fechada, sem ordem."
syntax: FIELD <nome> TYPE ENUMERATED SCOPE <escopo> VALUES ... END VALUES [...] END FIELD
see_also: [SYNESIS_E050, SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 70
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# ENUMERATED

## Sintaxe

```synesis
FIELD <nome> TYPE ENUMERATED
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
FIELD exemplo_enumerated TYPE ENUMERATED
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
| `VALUES` | Obrigatorio | SYNESIS_E050 |

## Regras

- **`VALUES` e obrigatorio.** O campo 'nome_do_campo' e do tipo ENUMERATED, mas nao define um bloco

## Ver tambem

`SYNESIS_E050`, `SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
