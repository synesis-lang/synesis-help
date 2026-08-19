---
id: MOD_SCOPE
title: "SCOPE"
category: modifier
summary: "Define em que tipo de bloco um campo pode ser usado."
syntax: "SCOPE <SOURCE|ITEM|ONTOLOGY>"
see_also: [BLOCK_FIELD, BLOCK_FIELDS_SPEC, GUIDE_PRIMITIVES, LINKAGE_SCOPES, SYNESIS_E006]
source: authored
order: 10
---

# SCOPE

## Descrição

`SCOPE` responde: **onde este campo pode aparecer?** E obrigatório em toda
definição de `FIELD`.

| Escopo | O campo descreve |
|---|---|
| `SOURCE` | a proveniência — de onde a informação vem |
| `ITEM` | a ocorrência — a unidade registrada |
| `ONTOLOGY` | a conceituacao — o conceito em si |

Os três aceitam os mesmos tipos de campo; ver `GUIDE_PRIMITIVES`.

## Sintaxe

```synesis
FIELD nome TYPE TEXT
    SCOPE ITEM
END FIELD
```

## Regras

- O `SCOPE` declarado no `FIELD` precisa concordar com o bloco `... FIELDS`
  que lista o campo (`SYNESIS_E006`).
- `IDENTIFIES` e `REFERS TO` exigem `SCOPE SOURCE` (`SYNESIS_E078`) —
  ver `LINKAGE_SCOPES`.

## Ver também

`BLOCK_FIELD`, `BLOCK_FIELDS_SPEC`, `LINKAGE_SCOPES`
