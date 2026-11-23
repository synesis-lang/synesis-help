---
id: GUIDE_PRIMITIVES
title: "The three primitives"
category: overview
summary: "SOURCE, ITEM and ONTOLOGY: provenance, occurrence, conceptualization — and the methods they express."
see_also: [BLOCK_SOURCE, BLOCK_ITEM, BLOCK_ONTOLOGY, GUIDE_START, MOD_SCOPE, GUIDE_CASE_STUDIES]
source: authored
order: 30
---

# The three primitives

## The triad

Synesis has three data blocks. They are not successive coding stages: they
are **primitives**, the elementary structures from which different
methodologies are expressed.

| Primitive | Function | Question it answers |
|---|---|---|
| `SOURCE` | provenance | Where does the information come from? |
| `ITEM` | occurrence | What concrete unit am I recording? |
| `ONTOLOGY` | conceptualization | Through which conceptual system do I understand it? |

In epistemological terms:

> `SOURCE` says **how we know**.
> `ITEM` says **what we observed**.
> `ONTOLOGY` says **how we conceptualize** what we found.

## Why it matters

The narrow reading (document → excerpt → theme) describes thematic analysis
well and everything else badly. The functional reading lets the **same
grammar** support different methodologies without a new block for each one.

## One skeleton, many methodologies

| Methodology | `SOURCE` | `ITEM` | `ONTOLOGY` |
|---|---|---|---|
| Thematic analysis | document | coded excerpt | theme, category |
| Grounded theory | interview | incident | concept, category |
| Content analysis | document | recording unit | category |
| Narrative analysis | narrative | event, episode | event type |
| Argumentation analysis | speech | argument, premise | argument class |
| Discourse analysis | speech | utterance | discursive formation |
| Causal analysis | case | causal evidence | mechanism, condition |
| Process tracing | documentary source | observation | causal mechanism |
| Frame analysis | text | framing | frame |
| Actor analysis | case | action, interaction | actor, role |
| Knowledge extraction | document | proposition | concept, entity |
| Knowledge graph | provenance document | extracted relation | entity |
| Systematic review | article | finding | construct, factor |
| Requirements analysis | technical document | requirement | domain, component |
| Legal analysis | statute, ruling | norm, argument | legal institute |
| Exegesis | text, passage | proposition, reading | concept, lemma |

The template makes this choice: by naming the fields of each scope, you
declare which methodology you are using. `GUIDE_CASE_STUDIES` shows complete
projects for several rows of this table.

## Symmetry and asymmetry

The three scopes accept **the same field types**. A `CHAIN` works in
`SOURCE`, `ITEM` or `ONTOLOGY`; the choice is yours.

There is one deliberate asymmetry: `IDENTIFIES` and `REFERS TO` exist only in
`SCOPE SOURCE` (`SYNESIS_E078`). What links projects is **provenance**, not
the occurrence nor the concept.

## Practical consequence

Before writing the template, answer the three questions for **your**
research. The vocabulary of your field goes into the field names; the three
blocks stay the same.

## See also

`BLOCK_SOURCE`, `BLOCK_ITEM`, `BLOCK_ONTOLOGY`, `GUIDE_START`,
`GUIDE_CASE_STUDIES`
