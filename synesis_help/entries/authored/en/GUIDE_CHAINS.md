---
id: GUIDE_CHAINS
title: "Chains in practice"
category: overview
summary: "How to design RELATIONS, ARITY and BUNDLE qualifiers so chains say something."
see_also: [TYPE_CHAIN, MOD_BUNDLE, BLOCK_ONTOLOGY, MOD_GUIDELINES, SYNESIS_E007, SYNESIS_E010, SYNESIS_E048, CASE_LITERATURE_REVIEW]
source: authored
order: 40
---

# Chains in practice

## What a chain records

`CHAIN` links concepts by named relations:

```text
shyness -> CAUSES -> fear_of_speaking -> RESTRICTS -> public_speaking
```

The reading is direct: shyness causes fear of speaking, which restricts
public speaking. What was prose becomes verifiable structure, and every link
can be counted, queried and traced back to its excerpt.

## Designing RELATIONS

The set of relations is a theoretical decision, not a vocabulary list. A few
well-separated relations are worth more than many overlapping ones.

```synesis
FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 3
    RELATIONS
        CAUSES: one factor directly produces another
        ENABLES: one factor creates conditions for another
        AMPLIFIES: one factor strengthens another already present
        RESTRICTS: one factor limits or reduces another
    END RELATIONS
END FIELD
```

`CAUSES`, `ENABLES` and `AMPLIFIES` differ: direct production, creating a
condition, intensifying what already exists. If two relations cannot be told
apart in one sentence, they are the same relation. Give each relation a test
in its description ("Test: is every A a B?") when coders confuse them.

## ARITY sets the shape of the argument

`ARITY` is not only a technical minimum; it expresses the analytic design.
`ARITY >= 3` requires three concepts, that is, a chain with a **mediator**:
antecedent → mediator → outcome. It forces the coder to state *through what*
the cause passes instead of recording loose pairs. `ARITY >= 2` accepts a
single edge, which suits taxonomies and literature reviews. When the template
declares `RELATIONS`, the number of relations must fit the arity
(`SYNESIS_E048`).

## A chain is a claim: qualify it with a BUNDLE

A chain says that a relation exists. Sources rarely say only that: they
hypothesize, test, deny, or find no evidence. Put the qualifiers next to the
chain in a `BUNDLE`, so each chain carries its own status:

```synesis
FIELD status TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION How the text presents the chain right before it.
    VALUES
        Asserted: the text states the relation as a finding or fact
        Hypothetical: the text proposes it without asserting it
        Negated: the text states the relation does not hold
        Inconclusive: the text reports no clear evidence
    END VALUES
END FIELD
```

```text
ITEM FIELDS
    OPTIONAL BUNDLE chain, status, justification
END ITEM FIELDS
```

Each `chain:` line pairs by position with its own `status:` and
`justification:`. Without the qualifier, a hypothesis and a finding look
identical in every export. `CASE_LITERATURE_REVIEW` shows the full design,
and the Alpaca export (`BLOCK_EXPORT`) carries the status into fine-tuning
data.

## Combining with the ontology

Chains are stronger when concepts declare their role:

```synesis
ONTOLOGY shyness
    role: antecedent
END ONTOLOGY

ONTOLOGY fear_of_speaking
    role: mediator
END ONTOLOGY
```

With `role` declared, a reader can check whether a chain respects the
theoretical design without rebuilding the whole analysis.

## Frequent errors

| Situation | Code |
|---|---|
| fewer concepts than the arity requires | `SYNESIS_E007` |
| relation not declared in the template | `SYNESIS_E010` |
| missing `->` operator | `SYNESIS_E013` |
| concept with the same name as a relation | `SYNESIS_E014` |
| concept with spaces | `SYNESIS_E015` |

## See also

`TYPE_CHAIN`, `MOD_BUNDLE`, `BLOCK_ONTOLOGY`, `CASE_LITERATURE_REVIEW`,
`SYNESIS_E007`, `SYNESIS_E048`
