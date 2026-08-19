---
id: TYPE_CHAIN
title: "CHAIN"
category: field_type
summary: "Cadeia de conceitos ligados por relacoes."
syntax: FIELD <nome> TYPE CHAIN SCOPE <escopo> ARITY <operador> <n> [...] END FIELD
see_also: [SYNESIS_E047, SYNESIS_E054, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 50
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# CHAIN

## Sintaxe

```synesis
FIELD <nome> TYPE CHAIN
    SCOPE <escopo>
    ARITY <operador> <n>
    [RELATIONS ... END RELATIONS]
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
END FIELD
```

## Propriedades

| Propriedade | Situacao | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `RELATIONS` | Permitido | - |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `VALUES` | Proibido | SYNESIS_E086 |
| `ARITY` | Obrigatorio | SYNESIS_E047 |

## Regras

- **`ARITY` e obrigatorio.** O campo 'nome_do_campo' e do tipo CHAIN, mas nao declara `ARITY`.

## Ver tambem

`SYNESIS_E047`, `SYNESIS_E054`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
