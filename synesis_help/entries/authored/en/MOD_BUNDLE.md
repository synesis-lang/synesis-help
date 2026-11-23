---
id: MOD_BUNDLE
title: "BUNDLE"
category: modifier
summary: "Fields that form one compound piece of information and only make sense together, paired by position."
syntax: "<REQUIRED|OPTIONAL> BUNDLE <field>, <field>[, <field>]"
see_also: [BLOCK_FIELDS_SPEC, GUIDE_CHAINS, SYNESIS_E016, SYNESIS_E017, SYNESIS_E018, CASE_LITERATURE_REVIEW]
source: authored
order: 40
---

# BUNDLE

## Description

`BUNDLE` declares fields that form an **indivisible package**: all of them
appear, or none.

Two classic cases:

- **Evidence and location.** An excerpt without the page it came from is half
  evidence; the page alone says nothing.
- **A claim and its qualifiers.** A `chain` that states a relation, the
  `status` that says whether the source asserts, hypothesizes or denies it,
  and the `justification` that says why. Without the status, a hypothesis
  looks like a finding in every export.

## Syntax

```synesis
ITEM FIELDS
    REQUIRED BUNDLE excerpt, page
    OPTIONAL BUNDLE chain, status, justification
END ITEM FIELDS
```

## Pairing by position

When a bundle repeats inside one ITEM, its members pair by position: the
first `chain:` goes with the first `status:` and the first
`justification:`, the second with the second.

```synesis
ITEM @author2023
    excerpt: "Training reduced clicks, but did not increase reporting."
    chain: training -> REDUCES -> clicks
    status: Asserted
    justification: The text reports the reduction as a result.
    chain: training -> INCREASES -> reporting
    status: Negated
    justification: The text states the increase did not occur.
END ITEM
```

Exports, the graph and the Alpaca export read the bundle this way: each chain
keeps its own status.

## Rules

- A missing member: `SYNESIS_E016`.
- Members with different numbers of occurrences: `SYNESIS_E017`.
- A `BUNDLE` with a single field makes no sense and is an error
  (`SYNESIS_E018`).
- `OPTIONAL BUNDLE`: the whole group may be absent; when one member appears,
  all must.

## See also

`BLOCK_FIELDS_SPEC`, `GUIDE_CHAINS`, `CASE_LITERATURE_REVIEW`,
`SYNESIS_E016`, `SYNESIS_E017`
