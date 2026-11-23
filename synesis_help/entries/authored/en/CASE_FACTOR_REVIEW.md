---
id: CASE_FACTOR_REVIEW
title: "Factors, signs and conditions"
category: case_study
summary: "Review of what drives acceptance of a technology: each relation carries its sign and the condition under which it holds."
see_also: [GUIDE_CASE_STUDIES, CASE_LITERATURE_REVIEW, MOD_BUNDLE, TYPE_ORDERED, TYPE_TOPIC, MOD_SCOPE]
source: authored
order: 20
---

# Factors, signs and conditions

Adapted from a real review of several hundred abstracts on the social
acceptance of energy technologies. Sources and excerpts are fictitious.

## Research question

*Which factors raise or lower acceptance of a technology, and under which
conditions?* Factor reviews tend to flatten the literature into "X matters".
The design here keeps three things apart: the direction of the effect, the
condition that limits it, and the context of the study.

## Corpus and unit

- **SOURCE:** one study. Technology, scale and method are coded once.
- **ITEM:** one excerpt and the relations it states. Every relation comes in
  a `REQUIRED BUNDLE` with its sign and its condition.
- **ONTOLOGY:** the factors, each placed on an **ordered** aspect scale and in
  a theoretical dimension, and grouped by topic.

## Template

```synesis
# acceptance.synt
TEMPLATE acceptance

SOURCE FIELDS
    REQUIRED technology, scale
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED text
    REQUIRED BUNDLE chain, sign, condition
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description
    OPTIONAL aspect, dimension, topic
END ONTOLOGY FIELDS

FIELD technology TYPE TEXT
    SCOPE SOURCE
    DESCRIPTION Technology the study is about.
END FIELD

FIELD scale TYPE ENUMERATED
    SCOPE SOURCE
    DESCRIPTION Territorial scale of the study.
    VALUES
        Local: one site or community
        Regional: a region or several sites
        National: a country
    END VALUES
END FIELD

FIELD text TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Literal excerpt stating the relations.
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    RELATIONS
        INFLUENCES: A changes the level of B
        MODERATES: A changes the strength of an effect on B
    END RELATIONS
END FIELD

FIELD sign TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Direction of the effect stated by the chain.
    VALUES
        Positive: more A, more B
        Negative: more A, less B
        Mixed: direction depends on the case
        Null: the study found no effect
    END VALUES
END FIELD

FIELD condition TYPE TEXT
    SCOPE ITEM
    DESCRIPTION Condition under which the effect holds.
    GUIDELINES
        Write the limiting condition the text states.
        Write none when the text states no condition.
    END GUIDELINES
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD

FIELD aspect TYPE ORDERED
    SCOPE ONTOLOGY
    DESCRIPTION Aspect of the factor, from material to symbolic.
    VALUES
        [1] Economic: costs, benefits, prices
        [2] Environmental: landscape, nature, health
        [3] Social: trust, fairness, participation
        [4] Institutional: rules, procedures, actors
    END VALUES
END FIELD

FIELD dimension TYPE ENUMERATED
    SCOPE ONTOLOGY
    VALUES
        Sociopolitical: acceptance by society and policy
        Community: acceptance by people near the site
        Market: adoption by consumers and investors
    END VALUES
END FIELD

FIELD topic TYPE TOPIC
    SCOPE ONTOLOGY
END FIELD
```

## Annotation

```synesis
# annotations.syn
SOURCE @author2022
    technology: onshore wind
    scale: Local
END SOURCE

ITEM @author2022
    text: "Perceived fairness raised support, but only where
        residents took part in siting decisions."
    chain: procedural_fairness -> INFLUENCES -> local_support
    sign: Positive
    condition: residents took part in siting decisions
END ITEM

ITEM @author2022
    text: "Visual impact lowered support regardless of income."
    chain: visual_impact -> INFLUENCES -> local_support
    sign: Negative
    condition: none
END ITEM
```

The first excerpt continues on an indented line: the whole sentence is the
value.

```synesis
# factors.syno
ONTOLOGY procedural_fairness
    description: Perceived fairness of how decisions are made.
    aspect: 3
    dimension: Community
    topic: participation
END ONTOLOGY

ONTOLOGY visual_impact
    description: Change in the landscape attributed to the plant.
    aspect: 2
    dimension: Community
    topic: landscape
END ONTOLOGY

ONTOLOGY local_support
    description: Support for the project among nearby residents.
    dimension: Community
    topic: acceptance
END ONTOLOGY
```

`aspect: 3` is the index of `Social`: an ORDERED value is written as its
index, so spelling variants cannot fragment the corpus.

## Project and exports

```synesis
# acceptance.synp
PROJECT acceptance

TEMPLATE "acceptance.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "annotations.syn"
INCLUDE ONTOLOGY "factors.syno"

QUESTIONS
    Q1: Which factors have opposite signs in different studies?
    Q2: Which positive effects depend on participation?
END QUESTIONS

EXPORT CSV tables
    OUTPUT "out/csv"
END EXPORT

END PROJECT
```

## Design decisions

- **Sign and condition live with the chain.** A `REQUIRED BUNDLE` makes every
  relation carry them; a relation without its sign cannot compile.
- **`none` is a value, not an absence.** Requiring the condition forces the
  coder to check for one; "none" records that they did.
- **Context is coded once.** Technology and scale are SOURCE fields, so
  results can be compared across settings without repeating them per excerpt.
- **The aspect is ORDERED.** Order lets dashboards sort factors from material
  to symbolic; the index keeps the spelling stable.

## Adapt it

- Other technologies or policies: keep the bundle, change `RELATIONS`.
- If studies report effect sizes, add a `SCALE` field to the bundle.
- For the epistemic status of each claim, add the `status` of
  `CASE_LITERATURE_REVIEW` to the same bundle.

## See also

`CASE_LITERATURE_REVIEW`, `MOD_BUNDLE`, `TYPE_ORDERED`, `TYPE_TOPIC`,
`MOD_SCOPE`, `GUIDE_CASE_STUDIES`
