---
id: GUIDE_FILES
title: "Files and extensions"
category: overview
summary: "Which file holds what, how they reference each other, and the rule that catches everyone."
see_also: [GUIDE_START, BLOCK_PROJECT, MOD_INCLUDE, SYNESIS_E061, SYNESIS_E062, GUIDE_REVIEW]
source: authored
order: 20
---

# Files and extensions

## Reference table

| Extension | Content | How many |
|---|---|---|
| `.synp` | project: template, includes, metadata, questions, exports | exactly 1 |
| `.synt` | template: fields, types, scopes, guidelines | 1 per project |
| `.syno` | ontology: concepts and their properties | 0 or more |
| `.syn` | annotations: `SOURCE` and `ITEM` blocks | 0 or more |
| `.bib` | BibTeX bibliography | 1 or more |
| `.toml` | dataset records (`INCLUDE DATASET`) | 0 or more |
| `.synr` | proposed revisions (`# REVISION`) | 0 or more |

The `.synr` is the only one that does **not** go into an `INCLUDE`: it is not
part of the project but a work artifact of `synesis-coder`, read and consumed
by `incorporate`. See `GUIDE_REVIEW`.

## How they reference each other

```text
project.synp
├── TEMPLATE "template.synt"
├── INCLUDE BIBLIOGRAPHY "refs.bib"
├── INCLUDE ANNOTATIONS "annotations/"
├── INCLUDE ONTOLOGY "concepts.syno"
└── INCLUDE DATASET "records/"
```

A folder is read recursively. `INCLUDE DATASET` is optional: TOML records,
one per source.

The `.synp` is the only file the compiler looks for by itself; all the others
must be declared in it. Paths are relative to the folder of the `.synp`, and
every export writes paths relative to that folder too, so two copies of a
project produce the same output.

## The rule that catches everyone

A `.syn` or `.syno` that exists in the folder but was **not** declared in an
`INCLUDE` is an error (`SYNESIS_E061`, `SYNESIS_E062`). The `.synr` is outside
this rule, which is why it is best kept in a separate folder (`revisions/`).

This is deliberate: a data file silently ignored is worse than a missing one,
because the analysis becomes incomplete without anyone noticing.

## Empty files

A `.syn` or `.syno` that is empty or holds only comments is accepted: it
contributes no block and raises no error. This is the normal state of a
`.syno` at the start of a project.

## See also

`GUIDE_START`, `BLOCK_PROJECT`, `MOD_INCLUDE`, `GUIDE_REVIEW`
