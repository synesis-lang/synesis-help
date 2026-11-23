---
id: CASE_CAUSATION_CODING
title: "Causation coding in interviews"
category: case_study
summary: "Causation coding of training interviews: chains with a mediator (ARITY >= 3), each paired with a summary, and concepts typed by causal role."
see_also: [GUIDE_CASE_STUDIES, GUIDE_CHAINS, TYPE_CHAIN, MOD_BUNDLE, BLOCK_ONTOLOGY, TYPE_TOPIC]
source: authored
order: 90
---

# Causation coding in interviews

Adapted from a teaching replication of causation coding (Saldaña) applied to
a public-speaking course. Answers are fictitious.

## Research question

*Through which mechanisms does the course change how participants speak in
public?* Causation coding records antecedent → mediator → outcome triplets
from what participants say about their own change.

## Corpus and unit

- **SOURCE:** one participant, with a short profile.
- **ITEM:** one statement, its outcome category, and a `REQUIRED BUNDLE` of a
  summary and a chain with at least three concepts.
- **ONTOLOGY:** the concepts, each typed as antecedent, mediator or outcome,
  and grouped by topic.

## Template

```synesis
# causation.synt
TEMPLATE causation

SOURCE FIELDS
    REQUIRED profile
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED quote, outcome
    REQUIRED BUNDLE summary, chain
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED description, role
    OPTIONAL group
END ONTOLOGY FIELDS

FIELD profile TYPE TEXT
    SCOPE SOURCE
END FIELD

FIELD quote TYPE QUOTATION
    SCOPE ITEM
END FIELD

FIELD outcome TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Kind of change the statement reports.
    VALUES
        Confidence: feels safer when speaking
        Technique: uses a method learned in class
        Reach: speaks in situations avoided before
    END VALUES
END FIELD

FIELD summary TYPE MEMO
    SCOPE ITEM
    DESCRIPTION The mechanism in one sentence.
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 3
    DESCRIPTION Antecedent, mediator and outcome, in that order.
    RELATIONS
        CAUSES: one factor directly produces another
        ENABLES: one factor creates conditions for another
        AMPLIFIES: one factor strengthens another
        RESTRICTS: one factor limits another
    END RELATIONS
    GUIDELINES
        Always name the mediator: what changed in between.
        Correct: practice -> ENABLES -> calm -> CAUSES -> clarity
        Wrong: practice -> CAUSES -> clarity (no mediator)
    END GUIDELINES
END FIELD

FIELD description TYPE TEXT
    SCOPE ONTOLOGY
END FIELD

FIELD role TYPE ENUMERATED
    SCOPE ONTOLOGY
    DESCRIPTION Position of the concept in the causal design.
    VALUES
        antecedent: what the participant brings or does first
        mediator: what changes in between
        outcome: the change reported
    END VALUES
END FIELD

FIELD group TYPE TOPIC
    SCOPE ONTOLOGY
END FIELD
```

## Annotation

```synesis
# interviews.syn
SOURCE @participant_07
    profile: engineer, avoided meetings before the course
END SOURCE

ITEM @participant_07
    quote: "Rehearsing out loud calmed me, so I speak clearly now."
    outcome: Confidence
    summary: Rehearsal lowers anxiety, which makes speech clearer.
    chain: rehearsal -> ENABLES -> calm -> CAUSES -> clarity
END ITEM
```

```synesis
# concepts.syno
ONTOLOGY rehearsal
    description: Practising the talk out loud before giving it.
    role: antecedent
    group: practice
END ONTOLOGY

ONTOLOGY calm
    description: Lower anxiety while speaking.
    role: mediator
    group: emotion
END ONTOLOGY

ONTOLOGY clarity
    description: Speech that listeners follow easily.
    role: outcome
    group: performance
END ONTOLOGY
```

## Project and exports

```synesis
# causation.synp
PROJECT causation

TEMPLATE "causation.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "interviews.syn"
INCLUDE ONTOLOGY "concepts.syno"

EXPORT JSON graph
    OUTPUT "out/causation.json"
END EXPORT

END PROJECT
```

The JSON feeds `synesis-graph`, where the mechanisms become paths that can
be counted by outcome category.

## Design decisions

- **`ARITY >= 3` is the method.** It makes the mediator mandatory, which is
  what distinguishes causation coding from listing causes.
- **Summary and chain in one bundle.** The sentence explains the chain; one
  without the other cannot compile.
- **Roles in the ontology.** Typing concepts as antecedent, mediator or
  outcome lets a reviewer check that chains start and end in the right place.

## Adapt it

- Process tracing or realist evaluation: rename the roles (context,
  mechanism, outcome) and keep `ARITY >= 3`.
- Add a `status` qualifier to the bundle when participants speculate about
  causes instead of reporting them (`CASE_LITERATURE_REVIEW`).

## See also

`GUIDE_CHAINS`, `TYPE_CHAIN`, `MOD_BUNDLE`, `BLOCK_ONTOLOGY`, `TYPE_TOPIC`,
`GUIDE_CASE_STUDIES`
