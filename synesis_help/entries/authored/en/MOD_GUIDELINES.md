---
id: MOD_GUIDELINES
title: "GUIDELINES"
category: modifier
summary: "Instructions for filling the field, for human coders and for AI: your coding protocol."
syntax: "GUIDELINES ... END GUIDELINES"
see_also: [BLOCK_FIELD, MOD_DESCRIPTION, GUIDE_REVIEW, ECO_CODER]
source: authored
order: 30
---

# GUIDELINES

## Description

Free text with **instructions on how to fill** the field. Accepted on any
type.

It is the difference between a template only you understand and one the
whole team (or an AI assistant) can follow. `DESCRIPTION` says what the field
is; `GUIDELINES` says how to fill it well.

## Syntax

```synesis
FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION Codes assigned to the excerpt.
    GUIDELINES
        Assign at most three codes per excerpt.
        Prefer the most specific code that fits.
        Do not create a code without registering it in the ontology.
        Correct: code: smishing (the excerpt describes SMS lures)
        Wrong: code: phishing (when the excerpt is specific about SMS)
    END GUIDELINES
END FIELD
```

## What works

- **Correct/Wrong pairs** carry a rule that dense prose loses. One concrete
  pair per decision the coder will face.
- **Tests** in a sentence: "Test: is every A a B?" separates `KIND_OF` from
  `PART_OF` better than a definition.
- **No `#` inside `GUIDELINES`.** There a `#` line is not a comment: it reaches
  the AI coder as text. Use `#` only for section titles outside the block.
- **No language keyword at the start of a line** (`Include`, `Item`, `Source`,
  `Field`, `End`, `Bundle`...): the parser can alter such lines. Rephrase
  ("To include..." → "Add...").
- **The unit.** Say what one value covers ("one status per chain; chains of
  the same ITEM can have different statuses").

## Use with AI

`synesis-coder` reads `GUIDELINES` as part of the prompt. A vague instruction
here produces vague coding there. The coder warns when a field has no
guidelines; `--require-guidelines` (or `SYNESIS_CODER_REQUIRE_GUIDELINES`)
turns the warning into a stop. The graph stores them in `ProjectContext`, so
whoever queries the data later reads your criteria.

## See also

`BLOCK_FIELD`, `MOD_DESCRIPTION`, `GUIDE_REVIEW`, `ECO_CODER`
