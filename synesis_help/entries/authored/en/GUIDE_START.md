---
id: GUIDE_START
title: "Where to start"
category: overview
summary: "The four files of a Synesis project, the order to write them, and the first compile."
see_also: [GUIDE_PRIMITIVES, GUIDE_FILES, BLOCK_PROJECT, BLOCK_TEMPLATE, BLOCK_ITEM, GUIDE_CASE_STUDIES]
source: authored
order: 10
---

# Where to start

## The idea in one sentence

Synesis makes analysis **verifiable**: you declare the rules of your coding
once, and the compiler enforces them on every unit you analyse. The result is
structured data (JSON, CSV, Excel, graph, SKOS, fine-tuning datasets) that
keeps the path back to the exact excerpt that supports each claim.

## The four files

| File | Role | Main block |
|---|---|---|
| `.synp` | entry point; ties everything together | `PROJECT` |
| `.synt` | the rules: which fields exist and how they are written | `TEMPLATE`, `FIELD` |
| `.syno` | the conceptual system | `ONTOLOGY` |
| `.syn` | the data: provenance and occurrences | `SOURCE`, `ITEM` |

Add a BibTeX `.bib` with the references: it anchors every `SOURCE` to a
citable work. Before writing, learn the three primitives and what each one
means in **your** methodology: `GUIDE_PRIMITIVES`.

## Order of writing

1. **`.synp` first.** The skeleton: name, template and the `INCLUDE` lines
   you will need. It is the only file the compiler looks for by itself; every
   other file must be declared in it.
2. **`.synt` next.** Deciding the fields before the data avoids rework. Start
   small (an excerpt and a code), then grow. Write `GUIDELINES` in every
   field: they are your coding protocol, and the AI coder reads them.
3. **`.syn`**: provenance and occurrences, `SOURCE` and `ITEM`.
4. **`.syno` last**, and it grows during the analysis: register a concept
   when it appears in the coding, not before.

## Minimal flow

```synesis
# template.synt
TEMPLATE minimal
ITEM FIELDS
    REQUIRED quote, code
END ITEM FIELDS
FIELD quote TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Literal excerpt from the source.
END FIELD
FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION Concept the excerpt is evidence of.
END FIELD
```

```synesis
# data.syn
SOURCE @author2024
END SOURCE

ITEM @author2024
    quote: "the river rose without warning"
    code: extreme_event
END ITEM
```

```synesis
# concepts.syno
ONTOLOGY extreme_event
END ONTOLOGY
```

## Next step

Run `synesis compile project.synp` in the project folder. Every reported
problem has a code (`SYNESIS_E0NN`) with its own entry in this guide:
`synesis-help lookup E047`.

To see complete projects built for real research designs, open
`GUIDE_CASE_STUDIES`.

## See also

`GUIDE_PRIMITIVES`, `GUIDE_FILES`, `BLOCK_TEMPLATE`, `BLOCK_ITEM`,
`GUIDE_CASE_STUDIES`
