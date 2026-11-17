---
id: TYPE_CHAIN
title: "CHAIN"
category: field_type
summary: "Cadeia de conceitos ligados por relações."
syntax: FIELD <nome> TYPE CHAIN SCOPE <escopo> ARITY <operador> <n> [...] END FIELD
see_also: [SYNESIS_E047, SYNESIS_E054, SYNESIS_E086, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 50
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

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

| Propriedade | Situação | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `RELATIONS` | Permitido | - |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `VALUES` | Proibido | SYNESIS_E086 |
| `ARITY` | Obrigatório | SYNESIS_E047 |

## Regras

- **`ARITY` é obrigatório.** The field 'nome_do_campo' is of type CHAIN, but does not declare `ARITY`.

## Ver também

`SYNESIS_E047`, `SYNESIS_E054`, `SYNESIS_E086`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
