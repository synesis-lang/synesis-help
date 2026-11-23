---
id: BLOCK_FIELDS_SPEC
title: "SOURCE / ITEM / ONTOLOGY FIELDS"
category: block
summary: "Lists which fields are required, optional, forbidden or bundled in each scope."
syntax: "<SCOPE> FIELDS [REQUIRED|OPTIONAL|FORBIDDEN|BUNDLE] <field>[, <field>] END <SCOPE> FIELDS"
file: ".synt"
see_also: [BLOCK_TEMPLATE, BLOCK_FIELD, MOD_BUNDLE, MOD_SCOPE, MOD_ON_BIBLIOGRAPHY, SYNESIS_E020, SYNESIS_E039, SYNESIS_E057]
source: authored
order: 30
---

# SOURCE FIELDS / ITEM FIELDS / ONTOLOGY FIELDS

## Description

While `FIELD` **defines** a field, these blocks say **which fields apply in
each scope** and how strictly.

## Syntax

```synesis
<SOURCE|ITEM|ONTOLOGY> FIELDS
    [REQUIRED <field>[, <field>]]
    [OPTIONAL <field>[, <field>]]
    [FORBIDDEN <field>[, <field>]]
    [REQUIRED BUNDLE <field>, <field>[, <field>]]
    [OPTIONAL BUNDLE <field>, <field>[, <field>]]
    [<REQUIRED|OPTIONAL> <field> ON BIBLIOGRAPHY]
    [<REQUIRED|OPTIONAL> <field> ON DATASET "<section.key>"]
END <SOURCE|ITEM|ONTOLOGY> FIELDS
```

`[ ]` optional · `<>` value to replace · `|` alternative

`ON BIBLIOGRAPHY` and `ON DATASET` apply only in `SOURCE FIELDS`: the value
comes from the `.bib` entry or from the TOML record, not from the annotation.

## Example

```synesis
ITEM FIELDS
    REQUIRED excerpt, code
    OPTIONAL note
    REQUIRED BUNDLE summary, chain
END ITEM FIELDS
```

## Qualifiers

| Qualifier | Meaning |
|---|---|
| `REQUIRED` | must be present in the block (`SYNESIS_E020`) |
| `OPTIONAL` | may appear or not |
| `FORBIDDEN` | must not appear in this scope (`SYNESIS_E021`) |
| `REQUIRED BUNDLE` | fields that only make sense together, at least once |
| `OPTIONAL BUNDLE` | the same pairing, but the group may be absent |

A `BUNDLE` aligns occurrences by position: the first `chain:` pairs with the
first `status:`, the second with the second. See `MOD_BUNDLE`.

## Rules

- One block per scope (`SYNESIS_E057`).
- A listed field needs a matching `FIELD` (`SYNESIS_E039`).
- A defined `FIELD` must be listed in some block (`SYNESIS_E042`).
- The `SCOPE` of the `FIELD` must match the block (`SYNESIS_E006`).

## See also

`BLOCK_TEMPLATE`, `BLOCK_FIELD`, `MOD_BUNDLE`, `MOD_SCOPE`,
`MOD_ON_BIBLIOGRAPHY`
