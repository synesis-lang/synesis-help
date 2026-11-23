---
id: CASE_LINKED_PROFILES
title: "Assessment across linked sources"
category: case_study
summary: "Two independent projects (CVs and public posts) evaluate people with one rubric, linked by IDENTIFIES / REFERS TO and a shared ontology."
see_also: [GUIDE_CASE_STUDIES, GUIDE_MULTIPROJECT, MOD_IDENTIFIES, MOD_INCLUDE, TYPE_SCALE, SYNESIS_I080, SYNESIS_W083]
source: authored
order: 50
---

# Assessment across linked sources

Adapted from a real project that assessed candidates for an innovation
programme from several kinds of source. People and records here are
fictitious.

## Research question

*How strong is each candidate on each criterion of a rubric, and which kind
of source supports the score?* CVs, public posts and code repositories have
different structures. Forcing them into one template would bury each in
optional fields; keeping them unlinked would prevent any profile.

## Corpus and unit

- **Two projects**, each with its own template, compiled alone or together.
  The CV project **owns** the entity `researcher` (`IDENTIFIES`); the posts
  project **refers** to it (`REFERS TO`).
- **ITEM (both):** one excerpt as evidence for one criterion, with a score
  and a justification.
- **ONTOLOGY:** the rubric criteria, in **one shared** `.syno` that both
  projects include with `INCLUDE SHARED ONTOLOGY`.

## Template

The CV project: the key comes from the record and identifies the person.

```synesis
# cvs/cvs.synt
TEMPLATE cvs

SOURCE FIELDS
    REQUIRED person ON DATASET "person.id"
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED excerpt, criterion, score, justification
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description
END ONTOLOGY FIELDS

FIELD person TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES researcher
END FIELD

FIELD excerpt TYPE QUOTATION
    SCOPE ITEM
END FIELD

FIELD criterion TYPE CODE
    SCOPE ITEM
    DESCRIPTION Rubric criterion the excerpt is evidence for.
END FIELD

FIELD score TYPE SCALE
    SCOPE ITEM
    FORMAT [0..3]
    GUIDELINES
        0 no evidence, 1 mention, 2 practice, 3 leadership.
        Score only what the excerpt shows, not what it implies.
    END GUIDELINES
END FIELD

FIELD justification TYPE MEMO
    SCOPE ITEM
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD
```

The posts project: same rubric, and a field that points to the person.

```synesis
# posts/posts.synt
TEMPLATE posts

SOURCE FIELDS
    REQUIRED author
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED excerpt, criterion, score, justification
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description
END ONTOLOGY FIELDS

FIELD author TYPE TEXT
    SCOPE SOURCE
    REFERS TO researcher
END FIELD

FIELD excerpt TYPE QUOTATION
    SCOPE ITEM
END FIELD

FIELD criterion TYPE CODE
    SCOPE ITEM
END FIELD

FIELD score TYPE SCALE
    SCOPE ITEM
    FORMAT [0..3]
END FIELD

FIELD justification TYPE MEMO
    SCOPE ITEM
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD
```

## Annotation

```toml
# cvs/records/p042.toml
[person]
id = "p042"
```

```synesis
# cvs/annotations.syn
SOURCE @p042
END SOURCE

ITEM @p042
    excerpt: "Coordinated a team of six in a funded prototype."
    criterion: leadership
    score: 3
    justification: Coordination of a team is stated, with a result.
END ITEM
```

```synesis
# posts/annotations.syn
SOURCE @post_0815
    author: p042
END SOURCE

ITEM @post_0815
    excerpt: "Shared our open-source tool for field surveys."
    criterion: open_collaboration
    score: 2
    justification: Releasing a tool is practice, not leadership.
END ITEM
```

```synesis
# common/rubric.syno
ONTOLOGY leadership
    description: Leads people or projects to a result.
END ONTOLOGY

ONTOLOGY open_collaboration
    description: Shares work openly and builds on others' work.
END ONTOLOGY
```

## Project and exports

```synesis
# cvs/cvs.synp
PROJECT cvs

TEMPLATE "cvs.synt"
INCLUDE DATASET "records/"
INCLUDE ANNOTATIONS "annotations.syn"
INCLUDE SHARED ONTOLOGY "../common/rubric.syno"

END PROJECT
```

```synesis
# posts/posts.synp
PROJECT posts

TEMPLATE "posts.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "annotations.syn"
INCLUDE SHARED ONTOLOGY "../common/rubric.syno"

END PROJECT
```

```text
synesis compile posts/posts.synp              # alone: I080 for the reference
synesis compile cvs/cvs.synp posts/posts.synp # link step: resolves p042
```

## Design decisions

- **The owner has the widest coverage.** Every candidate has a CV record, so
  the CV project owns `researcher`; posts may be missing for some.
- **Orphans are an inventory.** A post whose author has no CV becomes a
  warning (`SYNESIS_W083`) in the link step, not an error.
- **One rubric, one file.** The shared ontology keeps the criteria identical
  in both projects; a criterion renamed in one would otherwise split scores.
- **Score and justification together.** The scale gives comparability; the
  memo keeps the reason auditable.

## Adapt it

- More sources (repositories, publications): one project each, all with
  `REFERS TO researcher`.
- When a post is evidence of a public profile rather than of the person, add
  a `profile` entity and point posts to it (`GUIDE_MULTIPROJECT`).

## See also

`GUIDE_MULTIPROJECT`, `MOD_IDENTIFIES`, `MOD_INCLUDE`, `TYPE_SCALE`,
`SYNESIS_I080`, `SYNESIS_W083`, `GUIDE_CASE_STUDIES`
