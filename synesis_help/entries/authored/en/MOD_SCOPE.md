---
id: MOD_SCOPE
title: "SCOPE"
category: modifier
summary: "Defines in which kind of block a field can be used."
syntax: "SCOPE <SOURCE|ITEM|ONTOLOGY>"
see_also: [BLOCK_FIELD, BLOCK_FIELDS_SPEC, GUIDE_PRIMITIVES, LINKAGE_SCOPES, SYNESIS_E006]
source: authored
order: 10
---

# SCOPE

## Description

`SCOPE` answers: **where can this field appear?** It is required in every
`FIELD` definition.

| Scope | The field describes |
|---|---|
| `SOURCE` | provenance: where the information comes from |
| `ITEM` | the occurrence: the recorded unit |
| `ONTOLOGY` | conceptualization: the concept itself |

The three accept the same field types; see `GUIDE_PRIMITIVES`.

## Syntax

```synesis
FIELD name TYPE TEXT
    SCOPE ITEM
END FIELD
```

## Choosing the scope

Ask what the value varies with:

- the same for the whole article, interview or record → `SOURCE`
  (method, population, period);
- different for each excerpt → `ITEM` (the quotation, the claim, its
  status);
- a property of the concept wherever it appears → `ONTOLOGY` (definition,
  parent concept, dimension).

Coding a SOURCE-level value in every ITEM repeats it and lets copies diverge.

## Rules

- The `SCOPE` declared in the `FIELD` must agree with the `... FIELDS` block
  that lists the field (`SYNESIS_E006`).
- `IDENTIFIES` and `REFERS TO` require `SCOPE SOURCE` (`SYNESIS_E078`); see
  `LINKAGE_SCOPES`.

## See also

`BLOCK_FIELD`, `BLOCK_FIELDS_SPEC`, `LINKAGE_SCOPES`
