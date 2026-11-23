---
id: MOD_ROLE
title: "ROLE"
category: modifier
summary: "Declares the function of an ONTOLOGY field in the organizing principle: label, note, hierarchy or consolidation."
syntax: "ROLE <LABEL|NOTE|HIERARCHY> <species> | ROLE USE"
see_also: [BLOCK_ONTOLOGY, BLOCK_FIELD, BLOCK_EXPORT, BLOCK_PHASE, SYNESIS_E104, SYNESIS_E107, SYNESIS_E110, SYNESIS_E118, SYNESIS_E145, SYNESIS_E148, CASE_TOPICAL_INDEX]
source: authored
order: 90
requires_synesis: ">=0.15.0"
---

# ROLE

## Description

The **type** of a field gives the form of the value (`TEXT`, `CODE`...). The
`ROLE` line gives the **function** of the field in the organizing principle
of the project: what it is for the concept (a name, a definition, a position
in a hierarchy).

With the function declared, the compiler validates the structure (labels that
do not repeat, hierarchies without cycles) and every tool reads the field by
its role, not its name: the SKOS export, the `synesis-coder` phases, the graph
and the LSP. The field name stays free (`definition`, `meaning`,
`kind_of`...).

## Syntax

```synesis
FIELD <name> TYPE <type>
    SCOPE ONTOLOGY
    ROLE <FAMILY> [<SPECIES>]
END FIELD
```

`[ ]` optional · `<>` value to replace

## Catalogue

| Role | Type | Meaning | SKOS |
|---|---|---|---|
| `LABEL PREFERRED` | TEXT | display label (one per concept) | `prefLabel` |
| `LABEL ALTERNATIVE` | TEXT | synonyms and variants | `altLabel` |
| `LABEL HIDDEN` | TEXT | old or misspelled forms, for search only | `hiddenLabel` |
| `NOTE DEFINITION` | TEXT | the definition of the concept | `definition` |
| `NOTE USAGE` | TEXT | when to apply the code | `scopeNote` |
| `NOTE EXAMPLE` | TEXT | a typical case | `example` |
| `NOTE COUNTEREXAMPLE` | TEXT | a similar case it does not apply to | `syn:counterExample` |
| `HIERARCHY KIND` | CODE | is a kind of (generic) | `broader` |
| `HIERARCHY PART` | CODE | is part of (partitive) | `broader` |
| `HIERARCHY INSTANCE` | CODE | is a case of (instance) | `broader` |
| `USE` | CODE | this name is deprecated; the indicated concept holds | label of the target |

## Example

```synesis
FIELD definition TYPE TEXT
    SCOPE ONTOLOGY
    ROLE NOTE DEFINITION
END FIELD

FIELD used_for TYPE TEXT
    SCOPE ONTOLOGY
    ROLE LABEL ALTERNATIVE
END FIELD

FIELD kind_of TYPE CODE
    SCOPE ONTOLOGY
    ROLE HIERARCHY KIND
END FIELD
```

```synesis
ONTOLOGY smishing
    definition: Phishing carried out through SMS messages.
    used_for: SMS phishing, text-message phishing
    kind_of: phishing
END ONTOLOGY
```

## USE: consolidating two names

When two blocks name the same concept, the deprecated one keeps only the
`USE` field, pointing to the concept that holds:

```synesis
ONTOLOGY voice_phishing
    use: vishing
END ONTOLOGY
```

The annotations (`.syn`) do not change. Counts, hierarchy, graph and SKOS add
the deprecated name to its target, and the deprecated name becomes a label of
the target. `synesis-coder consolidate` makes this edit with a manifest and is
reversible (`--revert`).

## Rules

- Only on fields with `SCOPE ONTOLOGY` (`SYNESIS_E108`); a role outside the
  catalogue is an error (`SYNESIS_E104`); `LABEL`, `NOTE` and `HIERARCHY`
  require a species (`SYNESIS_E106`).
- The type must match the role: `LABEL`/`NOTE` on TEXT, `HIERARCHY`/`USE` on
  CODE (`SYNESIS_E107`).
- At most one `NOTE DEFINITION`, one `LABEL PREFERRED` and one `USE` field per
  template (`SYNESIS_E110`).
- A label term belongs to one concept only (`SYNESIS_E115`, `SYNESIS_E116`).
- A hierarchy always points to the broader concept, accepts several parents
  and cannot have a cycle (`SYNESIS_E117`, `SYNESIS_E118`).
- `USE` points to a concept that holds, never to itself nor to another
  deprecated one, and the deprecated block has no other fields
  (`SYNESIS_E145` to `SYNESIS_E149`).

## See also

`BLOCK_ONTOLOGY`, `BLOCK_EXPORT`, `BLOCK_PHASE`, `BLOCK_FIELD`,
`CASE_TOPICAL_INDEX`
