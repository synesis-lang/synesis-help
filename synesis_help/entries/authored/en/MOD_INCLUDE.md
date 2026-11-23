---
id: MOD_INCLUDE
title: "INCLUDE"
category: modifier
summary: "Declares the files that make up the project."
syntax: "INCLUDE [SHARED] <BIBLIOGRAPHY|ANNOTATIONS|ONTOLOGY|DATASET> \"<file>\""
see_also: [BLOCK_PROJECT, GUIDE_FILES, MOD_ON_BIBLIOGRAPHY, SYNESIS_E061, SYNESIS_E062, SYNESIS_E075, SYNESIS_E084]
source: authored
order: 60
---

# INCLUDE

## Description

Declares, in the `.synp`, which files belong to the project. Nothing is
loaded by discovery: what is not declared does not enter the analysis.

## Syntax

```synesis
INCLUDE <BIBLIOGRAPHY|ANNOTATIONS|ONTOLOGY|DATASET> "<file>"
INCLUDE SHARED ONTOLOGY "<path>"
```

`<>` value to replace · `|` alternative

## Example

```synesis
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS  "interviews/"
INCLUDE ONTOLOGY     "concepts.syno"
INCLUDE DATASET      "records/"

INCLUDE SHARED ONTOLOGY "../common/concepts.syno"
```

## Types

| Type | File | For |
|---|---|---|
| `BIBLIOGRAPHY` | `.bib` | references of the sources |
| `ANNOTATIONS` | `.syn` or folder | `SOURCE` and `ITEM` blocks |
| `ONTOLOGY` | `.syno` | `ONTOLOGY` blocks |
| `DATASET` | `.toml` or folder | structured records, one per source |

A folder is read recursively. Glob patterns (`"sources/*.bib"`) are accepted
for bibliographies and annotations.

## SHARED

`INCLUDE SHARED ONTOLOGY` points to an ontology **outside** the project
folder, useful when several projects share one vocabulary. It is the only
case where a path may leave the folder (`SYNESIS_E075`), and it applies only
to `ONTOLOGY` (`SYNESIS_E084`). In the exports the path is written relative
to the project folder (`../common/concepts.syno`).

## Rules

- A declared file that does not exist: `SYNESIS_E073`, `SYNESIS_E074`,
  `SYNESIS_E063`.
- A file that exists but was not declared: `SYNESIS_E061`, `SYNESIS_E062`.
- A commented-out line (`# INCLUDE ...`) is ignored.

## See also

`BLOCK_PROJECT`, `GUIDE_FILES`, `MOD_ON_BIBLIOGRAPHY`, `SYNESIS_E075`,
`SYNESIS_E084`
