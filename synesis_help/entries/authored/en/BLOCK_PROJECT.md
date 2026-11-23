---
id: BLOCK_PROJECT
title: "PROJECT"
category: block
summary: "Entry point of the project. Declares the template, the included files, and the project's questions, phases and exports."
syntax: "PROJECT <name> TEMPLATE \"<file>\" [INCLUDE <type> \"<path>\"] [METADATA ... END METADATA] [DESCRIPTION ... END DESCRIPTION] END PROJECT"
file: ".synp"
see_also: [BLOCK_TEMPLATE, MOD_INCLUDE, MOD_METADATA, BLOCK_QUESTIONS, BLOCK_PHASE, BLOCK_EXPORT, SYNESIS_E064, SYNESIS_E065, SYNESIS_E066]
source: authored
order: 10
---

# PROJECT

## Description

Every Synesis project starts here. The `.synp` file is the single entry
point: it declares which template governs the data, which annotation,
ontology and dataset files belong to the project, and where the bibliography
is. It can also state the research questions (`QUESTIONS`), the production
plan (`PHASE`) and the artifacts to produce (`EXPORT`).

There is **one** `PROJECT` block per project, at the root of its folder.

## Syntax

```synesis
PROJECT <name>

TEMPLATE "<file.synt>"

[INCLUDE BIBLIOGRAPHY "<file.bib>"]
[INCLUDE ANNOTATIONS "<file.syn or folder>"]
[INCLUDE ONTOLOGY "<file.syno>"]
[INCLUDE SHARED ONTOLOGY "<../path.syno>"]
[INCLUDE DATASET "<file.toml or folder>"]

[METADATA
    version: <n>
    author: <text>
END METADATA]

[DESCRIPTION
<free text, lines not indented>
END DESCRIPTION]

[QUESTIONS
    <id>: <text>
END QUESTIONS]

[PHASE <ANNOTATIONS|ONTOLOGY> <name>
    FIELDS <fields>
END PHASE]

[EXPORT <format> [<name>]
    OUTPUT "<file>"
END EXPORT]

END PROJECT
```

`[ ]` optional · `<>` value to replace

## Rules

- `TEMPLATE` is required; without it there is nothing to validate
  (`SYNESIS_E065`).
- One `PROJECT` block per file (`SYNESIS_E066`).
- Every `.syn` and `.syno` in the project folder must be declared in an
  `INCLUDE` (`SYNESIS_E061`, `SYNESIS_E062`). A forgotten file is invisible
  data. A folder in `INCLUDE ANNOTATIONS` is read recursively.
- Paths cannot leave the project folder (`SYNESIS_E075`), except
  `INCLUDE SHARED ONTOLOGY`.
- The `DESCRIPTION` travels with the exports: the graph stores it in its
  `ProjectContext` vertex, so write it for a reader who has never seen the
  project.

`QUESTIONS`, `PHASE` and `EXPORT` have their own entries: `BLOCK_QUESTIONS`,
`BLOCK_PHASE`, `BLOCK_EXPORT`.

## Example

```synesis
PROJECT community_resilience

TEMPLATE "template.synt"

INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "interviews/"
INCLUDE ONTOLOGY "concepts.syno"

METADATA
    version: 1.0
    author: Research team
END METADATA

DESCRIPTION
Interviews with residents after a flood, coded for coping
mechanisms and the conditions that enable them.
END DESCRIPTION

END PROJECT
```

## See also

`BLOCK_TEMPLATE`, `MOD_INCLUDE`, `MOD_METADATA`, `BLOCK_QUESTIONS`,
`BLOCK_PHASE`, `BLOCK_EXPORT`, `SYNESIS_E065`, `SYNESIS_E066`
