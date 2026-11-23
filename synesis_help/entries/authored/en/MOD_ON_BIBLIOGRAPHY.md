---
id: MOD_ON_BIBLIOGRAPHY
title: "ON BIBLIOGRAPHY / ON DATASET"
category: modifier
summary: "A field whose value comes from the .bib or from a TOML record, not from the annotation."
syntax: "<REQUIRED|OPTIONAL> <field> ON BIBLIOGRAPHY | <REQUIRED|OPTIONAL> <field> ON DATASET \"<path.in.record>\""
see_also: [BLOCK_SOURCE, BLOCK_FIELDS_SPEC, MOD_INCLUDE, MOD_IDENTIFIES, SYNESIS_E079, SYNESIS_E085, CASE_NEWS_FRAMING, CASE_PASSAGE_LEXICON]
source: authored
order: 50
---

# ON BIBLIOGRAPHY / ON DATASET

## Description

Declares that the value of a field is **not typed in the annotation**: it
comes from outside.

- `ON BIBLIOGRAPHY`: the value comes from the BibTeX entry of the `SOURCE`.
- `ON DATASET`: the value comes from a TOML record (one file per record), at
  the given path.

It avoids retyping what is already recorded, and the divergence retyping
produces. Metadata of a news story, the reference and original text of a
passage, the identifiers of a CV: all belong in records, not in annotations.

## Syntax

```synesis
SOURCE FIELDS
    REQUIRED year ON BIBLIOGRAPHY
    REQUIRED interview ON DATASET "interview.id"
    OPTIONAL region ON DATASET "interview.region"
END SOURCE FIELDS

FIELD interview TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES interview
END FIELD
```

```toml
# records/s1.toml, paired with SOURCE @s1
[interview]
id = "s1"
region = "Northeast"
```

The string after `ON DATASET` is a **path inside the record** (dot notation),
not a file name. The files come from `INCLUDE DATASET "records/"` in the
`.synp`.

## Rules

- Value missing in the `.bib`: `SYNESIS_E079`.
- Value missing in the dataset: `SYNESIS_E085`.
- The records must be declared with `INCLUDE DATASET` (file, folder or glob).
- A `SCOPE SOURCE` field with `IDENTIFIES` and `ON DATASET` is the key: the
  value at that path of the record must equal the bibref of the `SOURCE`.
- One field per clause: `REQUIRED a, b ON DATASET "x"` is an error.
- In the compiled JSON the values sit in the `dataset` section, by bibref.
- To give a section of the record to the AI coder as context while it fills a
  field (without taking the value from it), use `CONTEXT FROM DATASET` in the
  `FIELD`.
- These fields cannot enter a declared Alpaca export yet (`SYNESIS_E164`).

## See also

`BLOCK_SOURCE`, `MOD_INCLUDE`, `MOD_IDENTIFIES`, `CASE_NEWS_FRAMING`,
`CASE_PASSAGE_LEXICON`, `SYNESIS_E079`, `SYNESIS_E085`
