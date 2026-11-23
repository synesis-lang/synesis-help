---
id: BLOCK_FIELD
title: "FIELD"
category: block
summary: "Defines a field: name, type, scope, rules of filling and the guidelines for coders."
syntax: "FIELD <name> TYPE <type> SCOPE <scope> [DESCRIPTION <text>] [GUIDELINES ... END GUIDELINES] END FIELD"
file: ".synt"
see_also: [BLOCK_TEMPLATE, MOD_SCOPE, MOD_GUIDELINES, MOD_DESCRIPTION, TYPE_CODE, TYPE_CHAIN, SYNESIS_E022]
source: authored
order: 40
---

# FIELD

## Description

A `FIELD` declares one field of the research: the smallest unit of the
template, with name, type and scope. The type decides which additional
properties are required, allowed or forbidden; see the entry of the type you
chose (`TYPE_CHAIN`, `TYPE_SCALE`, ...).

## Syntax

```synesis
FIELD <name> TYPE <type>
    SCOPE <SOURCE|ITEM|ONTOLOGY>
    [DESCRIPTION <text>]
    [ARITY <operator> <n>]
    [FORMAT [<min>..<max>]]
    [RELATIONS ... END RELATIONS]
    [VALUES ... END VALUES]
    [IDENTIFIES <entity>]
    [REFERS TO <entity>]
    [ROLE <family> [<species>]]
    [CONTEXT FROM DATASET <section>]
    [GUIDELINES ... END GUIDELINES]
END FIELD
```

`[ ]` optional · `<>` value to replace

Not every property applies to every type; the matrix is in each `TYPE_*`
entry. `SCOPE` is always required.

## Example

```synesis
FIELD excerpt TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Literal excerpt that supports the analysis.
    GUIDELINES
        Copy 1 to 3 continuous sentences, without paraphrasing.
        The excerpt must make sense without the surrounding text.
    END GUIDELINES
END FIELD
```

## Properties by type

Universal, accepted by every type: `DESCRIPTION`, `GUIDELINES`,
`CONTEXT FROM DATASET`. The others belong to specific types: `ARITY` and
`RELATIONS` to `CHAIN`, `FORMAT` to `SCALE`, `VALUES` to `ENUMERATED` and
`ORDERED`. `ROLE` declares the function of an ONTOLOGY field in the organizing
model (`MOD_ROLE`).

## Rules

- A field used in a data file without a matching `FIELD` is an error
  (`SYNESIS_E022`).
- A property on the wrong type is refused with a specific message: `ARITY`
  only on CHAIN (`SYNESIS_E055`), `FORMAT` only on SCALE (`SYNESIS_E054`),
  `RELATIONS` only on CHAIN (`SYNESIS_E056`), `VALUES` only on ORDERED and
  ENUMERATED (`SYNESIS_E086`).
- `IDENTIFIES` and `REFERS TO` exist only in `SCOPE SOURCE` (`SYNESIS_E078`).
- Write `GUIDELINES` in every field: `synesis-coder` warns when a field has
  none, and `--require-guidelines` turns the warning into a stop.

## See also

`BLOCK_TEMPLATE`, `MOD_SCOPE`, `MOD_GUIDELINES`, `MOD_DESCRIPTION`,
`TYPE_CODE`, `TYPE_CHAIN`
