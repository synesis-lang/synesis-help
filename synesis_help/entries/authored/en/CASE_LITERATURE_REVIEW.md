---
id: CASE_LITERATURE_REVIEW
title: "Literature review of mechanisms"
category: case_study
summary: "Systematic review that maps how sources relate concepts, keeping whether each relation is asserted, hypothesized or denied."
see_also: [GUIDE_CASE_STUDIES, GUIDE_CHAINS, MOD_BUNDLE, TYPE_CHAIN, MOD_ROLE, BLOCK_EXPORT, CASE_FACTOR_REVIEW]
source: authored
order: 10
---

# Literature review of mechanisms

Adapted from a real review of a few hundred abstracts on digital fraud.
Names, sources and excerpts here are fictitious.

## Research question

*Which mechanisms does the literature propose for digital fraud, and how
firmly does it support each one?* A review that only lists relations
overstates the field: half of what articles say about mechanisms is
hypothesis, open question or negative result.

## Corpus and unit

- **SOURCE:** one article (abstract or full text), anchored in the `.bib`.
  Context fields describe the study once: method, data source, setting.
- **ITEM:** one rhetorical move of the text (objective, method, result...)
  with its literal excerpt, and zero or more relations stated in it.
- **ONTOLOGY:** the concepts that appear in the chains, organized as a
  taxonomy (`kind_of`, `part_of`) with synonyms.

## Template

```synesis
# review.synt
TEMPLATE review

SOURCE FIELDS
    REQUIRED method
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED excerpt, zone
    OPTIONAL BUNDLE chain, status, justification
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED definition
    OPTIONAL kind_of, part_of, used_for
END ONTOLOGY FIELDS

FIELD method TYPE TEXT
    SCOPE SOURCE
    DESCRIPTION Research design of the study, in a few words.
END FIELD

FIELD excerpt TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Literal excerpt covering one rhetorical zone.
    GUIDELINES
        Copy 1 to 3 consecutive sentences, without paraphrase.
    END GUIDELINES
END FIELD

FIELD zone TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Rhetorical function of the excerpt.
    VALUES
        Objective: what the study sets out to do
        Method: how it was done
        Result: what was found
        Conclusion: what the authors infer
    END VALUES
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    DESCRIPTION Relation between concepts named in the excerpt.
    RELATIONS
        KIND_OF: A is a type of B. Test: is every A a B?
        PART_OF: A is a component or stage of B
        EXPLOITS: A takes advantage of B to work
        IMITATES: A passes itself off as B
        MITIGATES: A prevents, detects or reduces B
    END RELATIONS
END FIELD

FIELD status TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION How the text presents the chain right before it.
    VALUES
        Asserted: stated as a finding or established fact
        Hypothetical: proposed, expected or suggested
        Investigated: asked or examined, without an answer
        Negated: the relation does not hold
        Inconclusive: no clear or significant evidence
    END VALUES
    GUIDELINES
        One status per chain; chains of one ITEM may differ.
        Correct: training -> MITIGATES -> clicks (Asserted)
        Wrong: one status for two chains with different support
    END GUIDELINES
END FIELD

FIELD justification TYPE MEMO
    SCOPE ITEM
    DESCRIPTION Why the chain and its status follow from the text.
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
```

The `status` field is what keeps the review honest. Without it, a chain from
a "we hypothesize that..." sentence and one from a "results show..." sentence
are the same row in every export.

## Annotation

```synesis
# annotations.syn
SOURCE @author2023
    method: randomized field experiment with employees
END SOURCE

ITEM @author2023
    excerpt: "We expect urgency cues to exploit time pressure."
    zone: Objective
    chain: urgency_cue -> EXPLOITS -> time_pressure
    status: Hypothetical
    justification: "We expect" marks a hypothesis, not a result.
END ITEM

ITEM @author2023
    excerpt: "Training reduced clicks but did not change reporting."
    zone: Result
    chain: awareness_training -> MITIGATES -> phishing_click
    status: Asserted
    justification: The reduction is reported as a result.
    chain: awareness_training -> MITIGATES -> underreporting
    status: Negated
    justification: The text states reporting did not change.
END ITEM
```

One ITEM, two chains, two statuses: the `BUNDLE` pairs them by position.

```synesis
# concepts.syno
ONTOLOGY phishing
    definition: Fraud that lures victims with deceptive messages.
END ONTOLOGY

ONTOLOGY urgency_cue
    definition: Element of a message that demands immediate action.
    part_of: phishing
END ONTOLOGY

ONTOLOGY time_pressure
    definition: Perceived lack of time to evaluate a request.
END ONTOLOGY

ONTOLOGY awareness_training
    definition: Instruction that teaches users to spot lures.
    used_for: security awareness training
END ONTOLOGY

ONTOLOGY phishing_click
    definition: Opening a malicious link in a lure.
END ONTOLOGY

ONTOLOGY underreporting
    definition: Users not reporting lures they received.
END ONTOLOGY
```

## Project and exports

```synesis
# review.synp
PROJECT review

TEMPLATE "review.synt"
INCLUDE BIBLIOGRAPHY "references.bib"
INCLUDE ANNOTATIONS "annotations.syn"
INCLUDE ONTOLOGY "concepts.syno"

QUESTIONS
    Q1: Which mechanisms are only hypothesized, never tested?
    Q2: Which countermeasures have negative results?
END QUESTIONS

EXPORT JSON panel
    OUTPUT "out/review.json"
END EXPORT

EXPORT SKOS corroborated
    OUTPUT "out/review.ttl"
    NAMESPACE "https://example.org/id/review/"
    LANGUAGE en
    MIN_SOURCES 2
    MAP RELATIONS KIND_OF TO HIERARCHY KIND
    MAP RELATIONS EXPLOITS, MITIGATES TO RELATED
END EXPORT

EXPORT ALPACA mechanism
    OUTPUT "out/mechanism.jsonl"
    INSTRUCTION Identify the relation and how the text presents it.
    MAP excerpt TO INPUT
    MAP chain, status, justification TO OUTPUT
END EXPORT

END PROJECT
```

- The **SKOS** block turns relations stated by at least two sources into a
  vocabulary, without touching the `.syno`.
- The **Alpaca** block writes one training line per chain with its status, so
  a fine-tuned model learns to tell hypothesis from finding.

## Design decisions

- **Status is a qualifier, not a separate item.** It lives in the same BUNDLE
  as the chain, because a status belongs to one specific relation.
- **Relations carry a test.** "Is every A a B?" in `KIND_OF` keeps coders from
  using it for parts or causes.
- **Method is coded once per source.** Repeating it in every ITEM would let
  copies diverge.
- **Hierarchy comes from the ontology, associations from chains.** What
  sources state (chains) stays separate from what the project adopts
  (`kind_of`, `part_of`).

## Adapt it

- Other review topics: rename the relations; keep the status scale.
- Grading certainty more finely: replace `status` by an `ORDERED` scale.
- To count findings per study design, add `design` as an ENUMERATED SOURCE
  field and filter by it in the JSON.

## See also

`GUIDE_CHAINS`, `MOD_BUNDLE`, `MOD_ROLE`, `BLOCK_EXPORT`,
`CASE_FACTOR_REVIEW`, `GUIDE_CASE_STUDIES`
