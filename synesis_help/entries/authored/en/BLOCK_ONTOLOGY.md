---
id: BLOCK_ONTOLOGY
title: "ONTOLOGY"
category: block
summary: "Organizing principle: the conceptual system that organizes the occurrences."
syntax: "ONTOLOGY <concept> [<field>: <value>] END ONTOLOGY"
file: ".syno"
see_also: [BLOCK_ITEM, GUIDE_PRIMITIVES, MOD_ROLE, BLOCK_EXPORT, TYPE_CODE, SYNESIS_E004, SYNESIS_E068, SYNESIS_W071, CASE_TOPICAL_INDEX]
source: authored
order: 70
---

# ONTOLOGY

## Description

`ONTOLOGY` is the **unit of conceptualization**. It answers:

> Through which conceptual system will the items be understood?

Do not assume it is a theme. Depending on the method, an `ONTOLOGY` block
defines a code, a category, a concept, a construct, a causal mechanism, a
normative value, an argument class, a frame, an event type, a lemma or an
entity of a knowledge graph.

## Organizing principles

The `ONTOLOGY` blocks are the **organizing principles** of the project. They
are not a formal ontology in the description-logic sense: they are the
entries of the **organizing model** (the compiler calls them *model
entries*).

The level of organization is a research decision, not a format one. The same
mechanism serves several degrees:

- **Flat list**: names and definitions only. A controlled vocabulary that
  stops the silent drift of coding; without it, `support_network`,
  `SupportNetwork` and `support_net` become three concepts for one idea.
- **Thesaurus**: with alternative and deprecated labels (`ROLE LABEL`,
  `USE`).
- **Taxonomy**: with a declared hierarchy (`ROLE HIERARCHY`).
- **Multi-relation taxonomy**: hierarchy of more than one kind (type, part,
  instance) plus associative relations, exportable as SKOS (`EXPORT SKOS`).
  No degree is called "ontology": SKOS is a knowledge organization system,
  not a formal OWL ontology.

The compiler reports the profile of each project at the end of compilation
(`Organizing model: Terminological: ... | Conceptual: ...`).

## Syntax

```synesis
ONTOLOGY <concept>
    [<field>: <value>]
    [<field>: <value>]
END ONTOLOGY
```

`[ ]` optional · `<>` value to replace

The concept name has no spaces. Which fields are accepted comes from
`ONTOLOGY FIELDS` in the template.

## Rules

- A concept name has no spaces (`SYNESIS_E015`) nor special characters
  (`SYNESIS_E033`).
- Two blocks cannot define the same concept (`SYNESIS_E068`).
- Identical descriptions in different concepts raise a warning
  (`SYNESIS_W071`): usually a conceptual duplicate.
- A code used in an `ITEM` without a definition here is an error
  (`SYNESIS_E004`).
- If there is an ontology, the template must declare `ONTOLOGY FIELDS`
  (`SYNESIS_E005`).

## Minimal example

```synesis
ONTOLOGY support_network
    definition: informal ties mobilized in a risk situation
END ONTOLOGY
```

## Structured ontologies

A concept is rarely only a name and a definition. The template can give
`ONTOLOGY` fields that express the **architecture** of your conceptual system,
and the compiler starts validating it.

**Causal role.** In designs that analyse mechanisms, each concept holds a
position in the chain:

```synesis
ONTOLOGY fear_of_speaking
    description: fear of negative evaluation when speaking in public
    role: mediator
    group: initial_barriers
END ONTOLOGY
```

With `role` as `ENUMERATED` (antecedent, mediator, outcome), the template
documents the design and lets reviewers check that chains respect it.

**Hierarchy and labels.** With a `ROLE` line in the template, an ordinary
field gets a function in the organizing principle, and the compiler validates
it:

```synesis
ONTOLOGY smishing
    definition: Phishing carried out through SMS messages.
    used_for: SMS phishing
    kind_of: phishing
END ONTOLOGY
```

Here `kind_of` (`ROLE HIERARCHY KIND`) puts the concept under `phishing`
(the compiler refuses cycles and parents without a block) and `used_for`
(`ROLE LABEL ALTERNATIVE`) records a synonym. See `MOD_ROLE`.

None of this is special syntax: they are ordinary fields declared with
`SCOPE ONTOLOGY` in the template.

## See also

`GUIDE_PRIMITIVES`, `BLOCK_ITEM`, `MOD_ROLE`, `BLOCK_EXPORT`, `TYPE_CODE`,
`TYPE_CHAIN`, `CASE_TOPICAL_INDEX`, `SYNESIS_E004`
