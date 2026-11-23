---
id: BLOCK_QUESTIONS
title: "QUESTIONS"
category: block
summary: "Competency questions: what the structure of the project must be able to answer."
syntax: "QUESTIONS <id>: <text> [<id>: <text>] END QUESTIONS"
file: ".synp"
see_also: [BLOCK_PROJECT, BLOCK_PHASE, BLOCK_EXPORT, SYNESIS_E091, SYNESIS_E092, SYNESIS_E093]
source: authored
order: 75
requires_synesis: ">=0.15.0"
---

# QUESTIONS

## Description

**Competency questions** state what the project must be able to answer when
it is done. They steer the template (which fields and roles exist) and serve
as the acceptance test of the organizing principle: if a question cannot be
answered from what was coded, structure is missing.

The questions travel with the project: they appear in the compiled JSON, in
the graph context and in the prompts of the `synesis-coder` phases.

## Syntax

```synesis
QUESTIONS
    <id>: <text>
    [<id>: <text>]
END QUESTIONS
```

`[ ]` optional · `<>` value to replace

The block lives inside `PROJECT`, in the `.synp`.

## Example

```synesis
QUESTIONS
    Q1: Which evidence deals with phishing or its subtypes?
    Q2: Which concepts have neither direct nor indirect evidence?
    Q3: Under which labels is each kind of scam known?
END QUESTIONS
```

## Writing good questions

- Ask about **the data**, not about the world: "Which relations are only
  hypothesized?" can be answered from a `status` field; "Is phishing
  growing?" cannot.
- One question per answerable query. If answering needs a field that does
  not exist, add the field or drop the question.
- Revisit them after the pilot: a question nobody can answer from the pilot
  data shows a gap in the template.

## Rules

- Each line has the form `<id>: <text>` (`SYNESIS_E091`) with non-empty text
  (`SYNESIS_E092`).
- Identifiers do not repeat in the project (`SYNESIS_E093`).

## See also

`BLOCK_PROJECT`, `BLOCK_PHASE`, `BLOCK_EXPORT`
