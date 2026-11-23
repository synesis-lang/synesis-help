---
id: CASE_SURVEY_RESPONSES
title: "Open-ended survey answers"
category: case_study
summary: "Answers to one open question, with respondent variables at SOURCE, so text and profile can be crossed in lexical and statistical tools."
see_also: [GUIDE_CASE_STUDIES, BLOCK_SOURCE, TYPE_ENUMERATED, TYPE_TOPIC, TYPE_CHAIN, BLOCK_EXPORT]
source: authored
order: 60
---

# Open-ended survey answers

Adapted from a classic teaching corpus of answers to one open question about
a stigmatized illness, used in lexical analysis courses. Answers here are
fictitious.

## Research question

*How do social representations of the illness vary with schooling and
knowledge?* The answers are short and many. Lexical tools (word frequencies,
descending hierarchical classification) need each text tied to the variables
of its author.

## Corpus and unit

- **SOURCE:** one respondent, with the survey variables (sex, schooling,
  self-declared knowledge) as closed lists.
- **ITEM:** the answer, literal, and optionally the associations the
  respondent makes, as a simple chain.
- **ONTOLOGY:** the ideas that appear in chains, grouped by topic.

## Template

```synesis
# survey.synt
TEMPLATE survey

SOURCE FIELDS
    REQUIRED sex, schooling, knowledge
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED answer
    OPTIONAL chain
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description
    OPTIONAL group
END ONTOLOGY FIELDS

FIELD sex TYPE ENUMERATED
    SCOPE SOURCE
    VALUES
        female: declared female
        male: declared male
    END VALUES
END FIELD

FIELD schooling TYPE ENUMERATED
    SCOPE SOURCE
    VALUES
        basic: up to lower secondary
        upper: upper secondary
    END VALUES
END FIELD

FIELD knowledge TYPE ENUMERATED
    SCOPE SOURCE
    DESCRIPTION Self-declared knowledge about the illness.
    VALUES
        low: knows little
        high: knows a lot
    END VALUES
END FIELD

FIELD answer TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION The whole answer, as written by the respondent.
    GUIDELINES
        Copy the answer whole; do not correct spelling.
    END GUIDELINES
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    DESCRIPTION Ideas the respondent links, in the order given.
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD

FIELD group TYPE TOPIC
    SCOPE ONTOLOGY
    DESCRIPTION Broad theme the idea belongs to.
END FIELD
```

The chain has no `RELATIONS`: it is a **simple chain**, recording that the
respondent associates ideas without naming how.

## Annotation

```synesis
# answers.syn
SOURCE @r001
    sex: female
    schooling: upper
    knowledge: low
END SOURCE

ITEM @r001
    answer: "It is a disease that brings fear and prejudice."
    chain: illness -> fear -> prejudice
END ITEM

SOURCE @r002
    sex: male
    schooling: basic
    knowledge: high
END SOURCE

ITEM @r002
    answer: "Prevention and treatment exist today."
END ITEM
```

```synesis
# ideas.syno
ONTOLOGY illness
    description: The illness named as such.
    group: disease
END ONTOLOGY

ONTOLOGY fear
    description: Fear of contagion or of the diagnosis.
    group: emotion
END ONTOLOGY

ONTOLOGY prejudice
    description: Negative judgement of people with the illness.
    group: stigma
END ONTOLOGY
```

## Project and exports

```synesis
# survey.synp
PROJECT survey

TEMPLATE "survey.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "answers.syn"
INCLUDE ONTOLOGY "ideas.syno"

EXPORT CSV tables
    OUTPUT "out/csv"
END EXPORT

END PROJECT
```

The CSV tables put the respondent variables next to each answer: the input
lexical tools expect, without hand-made coding lines.

## Design decisions

- **Respondent = SOURCE.** Variables belong to the person, not to the
  answer; coding them once lets every answer inherit them.
- **The answer is a QUOTATION.** It stays literal and checkable, spelling
  included, which lexical statistics depend on.
- **Chains are optional and simple.** Many answers associate nothing; when
  they do, the order of ideas is the data, and naming relations would be
  interpretation the respondent did not make.

## Adapt it

- More questions: add one QUOTATION field per question, or one ITEM per
  question with a `question` ENUMERATED field.
- Each respondent's `@bibref` needs an entry in the `.bib`; generate it with
  a script from the survey export.

## See also

`BLOCK_SOURCE`, `TYPE_ENUMERATED`, `TYPE_TOPIC`, `TYPE_CHAIN`,
`BLOCK_EXPORT`, `GUIDE_CASE_STUDIES`
