---
id: BLOCK_TEMPLATE
title: "TEMPLATE"
category: block
summary: "Defines which fields exist, of what type, where they can be used and how to fill them."
syntax: "TEMPLATE <name> [version: \"<v>\"] [<SCOPE> FIELDS ... END <SCOPE> FIELDS] [FIELD ... END FIELD]"
file: ".synt"
see_also: [BLOCK_FIELD, BLOCK_FIELDS_SPEC, BLOCK_PROJECT, MOD_GUIDELINES, SYNESIS_E069, SYNESIS_E042, GUIDE_CASE_STUDIES]
source: authored
order: 20
---

# TEMPLATE

## Description

The template is the **constitution of the project**. It answers three
questions, and the compiler enforces the answers in every data file:

1. Which fields exist? `FIELD` blocks.
2. Of what type is each one? `TYPE`.
3. Where can each field appear? `SCOPE` and the `... FIELDS` blocks.

A fourth answer turns it into a coding protocol: **how** to fill each field,
written in `GUIDELINES`. The AI coder reads them as instructions, the graph
stores them as context, and a second coder reads them as the rulebook.

Writing the template first is what separates an auditable analysis from a
spreadsheet with improvised column names.

## Syntax

```synesis
TEMPLATE <name> [version: "<v>"] [author: "<name>"]

[SOURCE FIELDS
    <requirements>
END SOURCE FIELDS]

[ITEM FIELDS
    <requirements>
END ITEM FIELDS]

[ONTOLOGY FIELDS
    <requirements>
END ONTOLOGY FIELDS]

FIELD <name> TYPE <type>
    SCOPE <scope>
    <properties>
END FIELD
```

`[ ]` optional · `<>` value to replace

Metadata (`version`, `author`) goes **on the same line** as the name. On its
own line it does not compile.

## Example

```synesis
TEMPLATE interviews version: "1.0"

ITEM FIELDS
    REQUIRED code
    OPTIONAL note
END ITEM FIELDS

FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION Concepts assigned to the unit.
    GUIDELINES
        Assign the concept the excerpt is evidence of, not its topic.
        Correct: code: distrust (the speaker doubts the agency)
        Wrong: code: agency (only names who is discussed)
    END GUIDELINES
END FIELD

FIELD note TYPE MEMO
    SCOPE ITEM
    DESCRIPTION Why this code applies to this excerpt.
END FIELD
```

## Rules

- Field names are unique in the template (`SYNESIS_E069`).
- Every defined `FIELD` must be listed in some `... FIELDS` block
  (`SYNESIS_E042`): a field defined and never used is noise.
- Every listed field needs a matching `FIELD` (`SYNESIS_E039`).
- The `SCOPE` of the `FIELD` must agree with the block that lists it
  (`SYNESIS_E006`).
- One `... FIELDS` block per scope (`SYNESIS_E057`).
- `#` comments are titles for the human reader; inside `GUIDELINES` they
  reach the AI coder, outside they do not.

## See also

`BLOCK_FIELD`, `BLOCK_FIELDS_SPEC`, `MOD_GUIDELINES`, `BLOCK_PROJECT`,
`GUIDE_CASE_STUDIES`, `SYNESIS_E069`, `SYNESIS_E042`
