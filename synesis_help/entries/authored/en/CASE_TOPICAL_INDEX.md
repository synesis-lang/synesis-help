---
id: CASE_TOPICAL_INDEX
title: "A topical index as a vocabulary"
category: case_study
summary: "A classic topical index turned into a controlled vocabulary: hierarchy and synonyms by ROLE, merged names by USE, published as SKOS."
see_also: [GUIDE_CASE_STUDIES, MOD_ROLE, BLOCK_ONTOLOGY, BLOCK_EXPORT, TYPE_CODE, BLOCK_PHASE]
source: authored
order: 70
---

# A topical index as a vocabulary

Adapted from real projects that converted public-domain topical indexes and
concordances of a classic text. Topics, passages and notes here are fictitious.

## Research question

*Can an old topical index become a reusable vocabulary, with its implicit
hierarchy made explicit?* A printed index lists topics and the passages under
them. It hides structure: some topics are kinds of others, some are parts,
some are the same topic under two names.

## Corpus and unit

- **SOURCE:** one section of the index.
- **ITEM:** one entry: the topic assigned to a passage, with an optional note
  and cross-reference.
- **ONTOLOGY:** the topics, with definition, hierarchy (`kind_of`,
  `part_of`), alternative labels and `USE` for duplicate names.

## Template

```synesis
# index.synt
TEMPLATE index

ITEM FIELDS
    REQUIRED entry, passage
    OPTIONAL note
END ITEM FIELDS

ONTOLOGY FIELDS
    OPTIONAL definition, kind_of, part_of, used_for, use
END ONTOLOGY FIELDS

FIELD entry TYPE CODE
    SCOPE ITEM
    DESCRIPTION Topic under which the index lists the passage.
END FIELD

FIELD passage TYPE TEXT
    SCOPE ITEM
    DESCRIPTION Reference of the passage, as printed.
END FIELD

FIELD note TYPE MEMO
    SCOPE ITEM
END FIELD

FIELD definition TYPE TEXT
    SCOPE ONTOLOGY
    ROLE NOTE DEFINITION
END FIELD

FIELD kind_of TYPE CODE
    SCOPE ONTOLOGY
    ROLE HIERARCHY KIND
END FIELD

FIELD part_of TYPE CODE
    SCOPE ONTOLOGY
    ROLE HIERARCHY PART
END FIELD

FIELD used_for TYPE TEXT
    SCOPE ONTOLOGY
    ROLE LABEL ALTERNATIVE
END FIELD

FIELD use TYPE CODE
    SCOPE ONTOLOGY
    ROLE USE
END FIELD
```

## Annotation

```synesis
# entries.syn
SOURCE @index_c
END SOURCE

ITEM @index_c
    entry: courage
    passage: Book II, 4
END ITEM

ITEM @index_c
    entry: fortitude
    passage: Book III, 9
    note: The index lists the same idea under a second name.
END ITEM
```

```synesis
# topics.syno
ONTOLOGY virtue
    definition: Settled disposition to act well.
END ONTOLOGY

ONTOLOGY courage
    definition: Firmness of mind in the face of danger.
    used_for: bravery
    kind_of: virtue
END ONTOLOGY

ONTOLOGY fortitude
    use: courage
END ONTOLOGY

ONTOLOGY endurance
    definition: Bearing hardship over time.
    part_of: courage
END ONTOLOGY
```

`fortitude` keeps only `use`: the annotation that cites it does not change,
but counts, hierarchy, graph and SKOS add it to `courage`, and "fortitude"
becomes a label of `courage`.

## Project and exports

```synesis
# index.synp
PROJECT index

TEMPLATE "index.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "entries.syn"
INCLUDE ONTOLOGY "topics.syno"

EXPORT SKOS vocabulary
    OUTPUT "out/topics.ttl"
    NAMESPACE "https://example.org/id/topics/"
    LANGUAGE en
    ALIAS_LABEL ALTERNATIVE
END EXPORT

END PROJECT
```

After compiling, the summary reports the profile of the organizing model
(for example, a thesaurus with a multi-relation taxonomy).

## Design decisions

- **Roles, not names.** `kind_of` and `part_of` could be called anything;
  `ROLE HIERARCHY KIND` and `PART` are what the compiler checks (no cycles,
  parents must exist) and what SKOS reads.
- **Kind and part are different.** Endurance is part of courage, not a kind
  of it; mixing them would make every "is a" query wrong.
- **USE instead of deleting.** Merging duplicate topics keeps the original
  annotations intact and reversible (`synesis-coder consolidate --revert`).
- **SKOS is an artifact, not the source.** The `.syno` stays the working
  vocabulary; the Turtle file is regenerated on every export.

## Adapt it

- Any index, glossary or codebook: start with `definition` and `kind_of`,
  add labels when synonyms show up.
- To let the AI coder propose the hierarchy, add `PHASE` blocks
  (definitions, synonyms, taxonomy) and review a sample (`BLOCK_PHASE`).

## See also

`MOD_ROLE`, `BLOCK_ONTOLOGY`, `BLOCK_EXPORT`, `TYPE_CODE`, `BLOCK_PHASE`,
`GUIDE_CASE_STUDIES`
