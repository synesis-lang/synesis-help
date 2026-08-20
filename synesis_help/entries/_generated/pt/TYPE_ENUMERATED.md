---
id: TYPE_ENUMERATED
title: "ENUMERATED"
category: field_type
summary: "Valor escolhido de uma lista fechada, sem ordem."
syntax: FIELD <nome> TYPE ENUMERATED SCOPE <escopo> VALUES ... END VALUES [...] END FIELD
see_also: [SYNESIS_E050, SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E087, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 70
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

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
        baixo: intensidade baixa
        alto: intensidade alta
    END VALUES
END FIELD
```

## Valor na anotação

O valor gravado é o **rótulo** declarado em `VALUES`:

```synesis
zone: Method
```

Diferente de `ORDERED`, aqui não há índice: `ENUMERATED` não tem ordem, então o prefixo `[N]` no bloco `VALUES` é recusado com `SYNESIS_E087`.

## Propriedades

| Propriedade | Situação | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `ARITY` | Proibido | SYNESIS_E055 |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `RELATIONS` | Proibido | SYNESIS_E056 |
| `VALUES` | Obrigatório | SYNESIS_E050 |

## Regras

- **`VALUES` é obrigatório.** O campo 'nome_do_campo' e do tipo ENUMERATED, mas nao define um bloco

## Ver também

`SYNESIS_E050`, `SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E087`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
