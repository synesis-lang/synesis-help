---
id: BLOCK_EXPORT
title: "EXPORT"
category: block
summary: "Declares the artifacts of the project (JSON, CSV, XLS, ALPACA, OKF, SKOS) and runs them with synesis export."
syntax: "EXPORT <format> [<name>] OUTPUT \"<file>\" [<property> <value>] [MAP RELATIONS <relations> TO <role>] [MAP <fields> TO INSTRUCTION|INPUT|OUTPUT] END EXPORT"
file: ".synp"
see_also: [BLOCK_PROJECT, MOD_ROLE, BLOCK_ONTOLOGY, SYNESIS_E094, SYNESIS_E095, SYNESIS_E099, SYNESIS_E122, SYNESIS_E127, SYNESIS_E150, SYNESIS_E153, SYNESIS_E158, SYNESIS_E162, SYNESIS_E163, SYNESIS_I166, CASE_LITERATURE_REVIEW]
source: authored
order: 77
requires_synesis: ">=0.15.0"
---

# EXPORT

## Description

Each `EXPORT` block declares one artifact of the project.
`synesis export project.synp` runs them all; `synesis export project.synp
skos` runs only the blocks of that format (or with that name). A problem in
one block stops only that artifact; the others are written.

| Format | What it writes | For |
|---|---|---|
| `JSON` | the compiled project | dashboards, scripts, synesis-graph |
| `CSV` | one table per scope, with traceability | spreadsheets, R, pandas |
| `XLS` | one workbook | sharing with the team |
| `ALPACA` | instruction/input/output JSONL | fine-tuning language models |
| `OKF` | a bundle of the project | exchange (experimental) |
| `SKOS` | the organizing model in Turtle | vocabularies, linked data |

All paths in the outputs are relative to the folder of the `.synp`.

## Syntax

```synesis
EXPORT <format> [<name>]
    OUTPUT "<file>"
    [<property> <value>]
    [MAP RELATIONS <relation>[, <relation>] TO <role>]
    [MAP <field>[, <field>] TO INSTRUCTION|INPUT|OUTPUT]
END EXPORT
```

`[ ]` optional · `<>` value to replace

| Format | Required | Optional |
|---|---|---|
| `JSON`, `OKF` | `OUTPUT` | `GENERATED_AT` |
| `CSV`, `XLS` | `OUTPUT` | — |
| `ALPACA` | `OUTPUT` | `INSTRUCTION` |
| `SKOS` | `OUTPUT`, `NAMESPACE`, `LANGUAGE` | `GENERATED_AT`, `MIN_SOURCES`, `ALIAS_LABEL`, `REGISTRY` |

## Example

```synesis
EXPORT SKOS corroborated
    OUTPUT "out/fraud.ttl"
    NAMESPACE "https://example.org/id/fraud/"
    LANGUAGE en
    MIN_SOURCES 2
    MAP RELATIONS KIND_OF TO HIERARCHY KIND
    MAP RELATIONS MITIGATES, EXPLOITS TO RELATED
END EXPORT
```

## SKOS

The **SKOS** format publishes the organizing principle as a SKOS vocabulary
(a knowledge organization system) in Turtle. It reads the function of each
field from the `ROLE` lines of the template: labels, definition, hierarchy.

- **IRIs:** each concept gets `NAMESPACE` + `concept/` + name. The
  `NAMESPACE` belongs to the project: a domain the team controls, ending in
  `/` or `#` (`SYNESIS_E127`).
- **`MAP RELATIONS`:** brings `CHAIN` relations (what sources state) into a
  role **in this artifact only**: `HIERARCHY KIND|PART|INSTANCE` or
  `RELATED`. The `.syno`, dashboards and graph do not see the mapping.
- **`MIN_SOURCES`:** minimum number of distinct sources stating a pair for it
  to enter the file. Two blocks with different thresholds separate
  corroborated pairs from candidates.
- **`ALIAS_LABEL HIDDEN|ALTERNATIVE`:** how the name of a deprecated block
  (`USE`) enters its target; the default is `HIDDEN`.
- **`REGISTRY "<file>"`** with `synesis export --publish`: records the
  published IRIs. A published IRI whose concept became deprecated is exported
  as obsolete (`owl:deprecated`, `dcterms:isReplacedBy`) instead of
  disappearing. With `--publish`, an unreadable registry is an error
  (`SYNESIS_E152`) and nothing is written; `OUTPUT` and `REGISTRY` on the
  same file are always refused (`SYNESIS_E157`).
- **Changing the `NAMESPACE`** is the researcher's decision and blocks
  nothing: registry IRIs in another namespace are only reported
  (`SYNESIS_E156`).

## ALPACA

Writes a JSONL for fine-tuning language models: each line has
`instruction`, `input` and `output`, all three as text.

- **Without `MAP` or `INSTRUCTION`:** built-in pairs chosen by the compiler.
  They do not carry the qualifier of a BUNDLE with a `CHAIN` (for example,
  the epistemic status), and the notice `SYNESIS_I167` says so.
- **With `MAP <fields> TO INSTRUCTION|INPUT|OUTPUT`** (synesis 0.16.0 and
  later): you declare which fields form each key. The instruction is a fixed
  text (`INSTRUCTION`) or a field (`MAP <field> TO INSTRUCTION`), never both.

```synesis
EXPORT ALPACA mechanism
    OUTPUT "out/mechanism.jsonl"
    INSTRUCTION Identify the causal relation in the excerpt.
    MAP excerpt TO INPUT
    MAP chain, status, justification TO OUTPUT
END EXPORT
```

- **One line per what:** a `BUNDLE` in the map sets the lines, one per
  occurrence. Fields outside it are context, repeated in every line. Without
  a bundle, one line per `ITEM`.
- **Text:** one field in a key gives only its value; several give one block
  per field, labelled by its name, in the order of the `MAP`. A `CHAIN`
  enters with all its triples.
- **Card:** next to the JSONL, `<name>.card.json` records the composition,
  the counts, the values of the qualifiers and the fields left out.

## Rules

- An unknown format is an error (`SYNESIS_E094`); so is a property the format
  does not accept (`SYNESIS_E095`, `SYNESIS_E096`).
- `MAP RELATIONS` exists only in `SKOS` (`SYNESIS_E099`) and only with
  relations declared in the `RELATIONS` of `CHAIN` fields (`SYNESIS_E122`).
- `MAP <fields> TO` exists only in `ALPACA`, with the targets `INSTRUCTION`,
  `INPUT` and `OUTPUT`, without `FROM` (`SYNESIS_E165`). `OUTPUT` is required
  (`SYNESIS_E158`) and there is exactly one source of instruction
  (`SYNESIS_E159`).
- An OUTPUT field also in INPUT or INSTRUCTION is refused (`SYNESIS_E162`):
  the answer would be in the prompt.
- Fields from two bundles in one block are refused (`SYNESIS_E163`).
- A qualifier of the bundle left out of the map is only a notice
  (`SYNESIS_I166`): the file is written.
- `ALIAS_LABEL` accepts `HIDDEN` or `ALTERNATIVE` (`SYNESIS_E150`).
- A registry IRI without a block or a `USE` that replaces it is a warning
  (`SYNESIS_E153`): the published concept vanished without a successor.

## See also

`MOD_ROLE`, `BLOCK_ONTOLOGY`, `BLOCK_PROJECT`, `CASE_LITERATURE_REVIEW`
