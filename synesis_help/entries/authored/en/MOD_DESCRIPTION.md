---
id: MOD_DESCRIPTION
title: "DESCRIPTION"
category: modifier
summary: "A short sentence saying what a field records."
syntax: "DESCRIPTION <text>"
see_also: [BLOCK_FIELD, MOD_GUIDELINES]
source: authored
order: 20
---

# DESCRIPTION

## Description

Says **what** the field records. Accepted on any field type.

It shows up in the editor's completion and hover, it heads the field in the
AI coder's prompt, and it labels the field in the graph context. It is the
sentence the team reads while filling the field: one good line here saves a
recurring doubt.

## Syntax

```synesis
FIELD quote TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Literal excerpt transcribed from the source.
END FIELD
```

## Writing it well

- Say what the value **is**, not how to find it (that goes in `GUIDELINES`).
- Name the unit: "Epistemic status of the chain right before it, as the text
  presents it" is better than "Status".
- For a qualifier in a `BUNDLE`, say what it qualifies.

## DESCRIPTION or GUIDELINES?

| | Answers |
|---|---|
| `DESCRIPTION` | what this field is |
| `GUIDELINES` | how to fill it well |

Use both when the field requires judgement.

## See also

`BLOCK_FIELD`, `MOD_GUIDELINES`
