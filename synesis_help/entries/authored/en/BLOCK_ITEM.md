---
id: BLOCK_ITEM
title: "ITEM"
category: block
summary: "Unit of occurrence: what was observed or recorded, always tied to a SOURCE."
syntax: "ITEM @<bibref> <field>: <value> [<field>: <value>] END ITEM"
file: ".syn"
see_also: [BLOCK_SOURCE, BLOCK_ONTOLOGY, GUIDE_PRIMITIVES, MOD_BUNDLE, TYPE_CODE, TYPE_CHAIN, SYNESIS_E002, SYNESIS_E023]
source: authored
order: 60
---

# ITEM

## Description

`ITEM` is the **unit of occurrence**. It answers:

> What concrete unit am I recording?

It is the most flexible of the three primitives. Depending on the method, an
`ITEM` is a coded excerpt, an incident, a recording unit, a narrative
episode, an argument, a piece of causal evidence, an utterance, a review
finding, a requirement, an extracted proposition or a relation.

What does not change: an `ITEM` always belongs to a `SOURCE`. An occurrence
without provenance is not evidence.

## Syntax

```synesis
ITEM @<bibref>
    <field>: <value>
    [<field>: <value>]
END ITEM
```

`[ ]` optional · `<>` value to replace

Which fields are accepted comes from `ITEM FIELDS` in the template. A field
may repeat inside one ITEM when the design needs several occurrences (several
chains, each with its own BUNDLE partners).

## Rules

- Every `ITEM` needs a `SOURCE` with the same `@bibref` (`SYNESIS_E002`).
- An empty `ITEM` is an error (`SYNESIS_E023`).
- Codes used must be defined in the ontology (`SYNESIS_E004`).
- Fields required by the template must be present (`SYNESIS_E020`); forbidden
  ones, absent (`SYNESIS_E021`).
- A long value can continue on the next lines, indented under the field.

## Example

```synesis
ITEM @author2024
    quote: "when the river rose, it was the neighbour who warned us"
    code: support_network, informal_alert
    chain: informal_alert -> PRECEDES -> support_network
END ITEM
```

## See also

`GUIDE_PRIMITIVES`, `BLOCK_SOURCE`, `BLOCK_ONTOLOGY`, `MOD_BUNDLE`,
`TYPE_CODE`, `SYNESIS_E002`
