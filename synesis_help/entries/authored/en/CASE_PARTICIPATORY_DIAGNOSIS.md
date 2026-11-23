---
id: CASE_PARTICIPATORY_DIAGNOSIS
title: "Participatory community diagnosis"
category: case_study
summary: "Workshop and interview statements coded as SWOT factors with importance, and each factor placed in a sustainability dimension."
see_also: [GUIDE_CASE_STUDIES, TYPE_SCALE, TYPE_ENUMERATED, TYPE_CODE, BLOCK_ONTOLOGY, MOD_SCOPE]
source: authored
order: 80
---

# Participatory community diagnosis

Adapted from a teaching project with fictitious data about a coastal
village.

## Research question

*What does the community see as its strengths, weaknesses, opportunities and
threats, and how important is each?* A participatory diagnosis mixes several
kinds of source (workshops, interviews, field visits). The result must show
the factors, their weight and the dimension of sustainability they touch.

## Corpus and unit

- **SOURCE:** one activity (workshop, interview, visit), with its type.
- **ITEM:** one statement: the quote, a summary, the factor it names, its
  SWOT position and the importance participants gave it.
- **ONTOLOGY:** the factors, each in one dimension of sustainability.

## Template

```synesis
# diagnosis.synt
TEMPLATE diagnosis

SOURCE FIELDS
    REQUIRED activity
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED quote, summary, factor, swot, importance
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description, dimension
END ONTOLOGY FIELDS

FIELD activity TYPE ENUMERATED
    SCOPE SOURCE
    VALUES
        Workshop: collective session with residents
        Interview: conversation with one resident
        Visit: field observation
    END VALUES
END FIELD

FIELD quote TYPE QUOTATION
    SCOPE ITEM
END FIELD

FIELD summary TYPE MEMO
    SCOPE ITEM
    DESCRIPTION The statement in one sentence, by the facilitator.
END FIELD

FIELD factor TYPE CODE
    SCOPE ITEM
END FIELD

FIELD swot TYPE ENUMERATED
    SCOPE ITEM
    VALUES
        Strength: internal, helps
        Weakness: internal, hinders
        Opportunity: external, helps
        Threat: external, hinders
    END VALUES
    GUIDELINES
        Internal means under the community's control.
        Correct: Threat for a storm surge (outside its control)
        Wrong: Weakness for a storm surge
    END GUIDELINES
END FIELD

FIELD importance TYPE SCALE
    SCOPE ITEM
    FORMAT [1..5]
    DESCRIPTION Weight participants gave the factor.
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD

FIELD dimension TYPE ENUMERATED
    SCOPE ONTOLOGY
    VALUES
        Environmental: ecosystems and natural resources
        Social: health, education, organization
        Economic: work and income
        Cultural: traditions and identity
    END VALUES
END FIELD
```

## Annotation

```synesis
# statements.syn
SOURCE @workshop_01
    activity: Workshop
END SOURCE

ITEM @workshop_01
    quote: "The fishing association still meets every week."
    summary: Fishers keep an active collective organization.
    factor: fishers_association
    swot: Strength
    importance: 5
END ITEM

ITEM @workshop_01
    quote: "Every winter the sea takes more of the beach."
    summary: Coastal erosion advances each year.
    factor: coastal_erosion
    swot: Threat
    importance: 4
END ITEM
```

```synesis
# factors.syno
ONTOLOGY fishers_association
    description: Collective organization of local fishers.
    dimension: Social
END ONTOLOGY

ONTOLOGY coastal_erosion
    description: Loss of shoreline to the sea.
    dimension: Environmental
END ONTOLOGY
```

## Project and exports

```synesis
# diagnosis.synp
PROJECT diagnosis

TEMPLATE "diagnosis.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "statements.syn"
INCLUDE ONTOLOGY "factors.syno"

QUESTIONS
    Q1: Which threats were rated most important?
    Q2: Which dimension concentrates the weaknesses?
END QUESTIONS

EXPORT XLS report
    OUTPUT "out/diagnosis.xlsx"
END EXPORT

END PROJECT
```

## Design decisions

- **SWOT at the statement, dimension at the factor.** The same factor can be
  a strength in one workshop and a weakness in another; its dimension does
  not change.
- **Importance is the participants' weight.** A 1 to 5 scale lets the report
  rank factors without the facilitator's judgement replacing theirs.
- **The guideline fixes the classic confusion** between weakness and threat,
  with a concrete pair.

## Adapt it

- Other diagnostic frames (problem trees, PESTEL): change `swot` and
  `dimension`; keep factor as CODE.
- To show the change over time, add a `round` field to SOURCE and compare
  the exported tables.

## See also

`TYPE_SCALE`, `TYPE_ENUMERATED`, `TYPE_CODE`, `BLOCK_ONTOLOGY`, `MOD_SCOPE`,
`GUIDE_CASE_STUDIES`
