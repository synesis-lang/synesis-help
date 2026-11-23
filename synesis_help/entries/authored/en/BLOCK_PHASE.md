---
id: BLOCK_PHASE
title: "PHASE"
category: block
summary: "Production plan: which fields synesis-coder writes in each phase, and from what."
syntax: "PHASE <ANNOTATIONS|ONTOLOGY> <name> FIELDS <fields> [INPUT <fields>] [RULES <fields>] [OUTPUT \"<file.syno>\"] END PHASE"
file: ".synp"
see_also: [BLOCK_PROJECT, MOD_ROLE, BLOCK_QUESTIONS, ECO_CODER, SYNESIS_E133, SYNESIS_E137, SYNESIS_E139, SYNESIS_E141, SYNESIS_E142]
source: authored
order: 76
requires_synesis: ">=0.15.0"
---

# PHASE

## Description

A `PHASE` block splits the production of the organizing principle into
stages, each with its fields. Definitions first, then synonyms, then the
taxonomy: each phase reads what the previous ones produced.

The compiler validates the plan against the template (fields that exist,
order of phases, required fields covered). `synesis-coder` runs each phase.
The kind of phase follows from the roles of its fields (`ROLE`): `HIERARCHY`
fields make a **taxonomy** phase, `LABEL ALTERNATIVE`/`HIDDEN` fields a
**synonyms** phase, the others a **descriptive** phase.

## Syntax

```synesis
PHASE <ANNOTATIONS|ONTOLOGY> <name>
    FIELDS <field>[, <field>]
    [INPUT <field>[, <field>]]
    [RULES <field>[, <field>]]
    [OUTPUT "<file.syno>"]
END PHASE
```

`[ ]` optional · `<>` value to replace

`FIELDS` are what the phase produces; `INPUT`, what it reads; `OUTPUT` (only
in `ONTOLOGY`), the `.syno` it writes to.

## Example

```synesis
PHASE ONTOLOGY definitions
    FIELDS definition, aspect, topic
    INPUT excerpt, chain
END PHASE

PHASE ONTOLOGY synonyms
    FIELDS used_for, former_name
    INPUT definition, topic
END PHASE

PHASE ONTOLOGY taxonomy
    FIELDS kind_of, part_of
    INPUT definition, topic, chain
END PHASE
```

## Running it

```bash
synesis-coder phase project.synp --list                    # the plan, with the connection of each phase
synesis-coder phase project.synp definitions               # run one phase
synesis-coder review project.synp taxonomy --sample 100    # sample for human judgement
synesis-coder review project.synp taxonomy --score sample.csv
synesis-coder consolidate project.synp voice_phishing --into vishing   # USE, reversible
```

Each run writes a manifest (`<target>.<phase>.manifest.json`) with what was
proposed, applied or rejected. Running again without changes in the inputs
does not call the model. Model and connection can differ per phase:
`SYNESIS_CODER_PHASE_<NAME>_MODEL`, `_BACKEND`, `_API_URL`, `_API_KEY`, set in
the `.env` of the project folder.

## Rules

- Accepted properties: `FIELDS`, `INPUT`, `RULES` and `OUTPUT`
  (`SYNESIS_E133`).
- A field is produced by one phase only (`SYNESIS_E137`).
- A phase reads only what earlier phases produce (`SYNESIS_E139`).
- With `PHASE` blocks, every `REQUIRED` field needs a phase that produces it
  (`SYNESIS_E141`).
- Without `OUTPUT`, the project must have exactly one local `.syno`
  (`SYNESIS_E142`).

## See also

`MOD_ROLE`, `BLOCK_QUESTIONS`, `BLOCK_PROJECT`, `ECO_CODER`
