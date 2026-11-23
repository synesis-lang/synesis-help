---
id: BLOCK_SOURCE
title: "SOURCE"
category: block
summary: "Unit of provenance: where the information comes from."
syntax: "SOURCE @<bibref> [<field>: <value>] END SOURCE"
file: ".syn"
see_also: [BLOCK_ITEM, GUIDE_PRIMITIVES, MOD_ON_BIBLIOGRAPHY, MOD_IDENTIFIES, SYNESIS_E001, SYNESIS_E003, SYNESIS_E070]
source: authored
order: 50
---

# SOURCE

## Description

`SOURCE` is the **unit of provenance**. It answers one question:

> Where does this information come from?

Do not assume it is a document. Depending on the research design, a `SOURCE`
can be an interview, an article, a case, a person, a statute, an experiment,
an administrative record, a web page, a news story or a passage of an ancient
text.

What they share is the function: anchoring evidence in a citable origin. That
is what makes the analysis traceable: every analysed excerpt points, in the
end, to a real source.

## Syntax

```synesis
SOURCE @<bibref>
    [<field>: <value>]
    [<field>: <value>]
END SOURCE
```

`[ ]` optional · `<>` value to replace

Which fields are accepted (and which are required) comes from `SOURCE FIELDS`
in the template. SOURCE fields are the place for **context that holds for the
whole source**: method, population, period, technology, country. Coding them
once per source keeps them out of every ITEM.

## Rules

- The `@bibref` must exist in the `.bib` file (`SYNESIS_E001`).
- A `@bibref` cannot open two `SOURCE` blocks in the same file
  (`SYNESIS_E070`).
- A `SOURCE` without any `ITEM` raises a warning (`SYNESIS_E003`): a source
  registered and never analysed is usually an oversight.
- Fields marked `ON BIBLIOGRAPHY` take their value from the `.bib`; if it is
  missing there, the compiler warns (`SYNESIS_E079`). Fields marked
  `ON DATASET` take it from the TOML record.

## Particularity

`SOURCE` is the only scope that accepts `IDENTIFIES` and `REFERS TO`
(`SYNESIS_E078`). The reason is conceptual: what links projects is
**provenance** (the same municipality, case, person, institution), not the
analysed occurrence nor the concept.

## Example

```synesis
SOURCE @author2024
    method: semi-structured interviews
    context: riverside community, March 2024
END SOURCE
```

## See also

`GUIDE_PRIMITIVES`, `BLOCK_ITEM`, `MOD_ON_BIBLIOGRAPHY`, `MOD_IDENTIFIES`,
`SYNESIS_E001`
