---
id: MOD_METADATA
title: "METADATA"
category: modifier
summary: "Optional project block with version, authorship and dates."
syntax: "METADATA ... END METADATA"
see_also: [BLOCK_PROJECT, SYNESIS_W067]
source: authored
order: 70
---

# METADATA

## Description

Optional block inside `PROJECT`, with data about the project itself, not
about the analysed data. For a description a reader needs (what the corpus
is, what was coded), use `DESCRIPTION` in the `PROJECT`: it travels with the
exports.

## Syntax

```synesis
METADATA
    version: <n>
    author: <text>
    [created: <date>]
    [modified: <date>]
    [dataset: <text>]
END METADATA
```

`[ ]` optional · `<>` value to replace

## Example

```synesis
METADATA
    version: 1.0
    author: Research team
    created: 2026-03-01
    modified: 2026-08-08
END METADATA
```

## Fields

| Field | Required |
|---|---|
| `version` | yes |
| `author` | yes |
| `created` | no |
| `modified` | no |
| `dataset` | no |

## Rules

- `modified` earlier than `created` raises a warning (`SYNESIS_W067`).

## See also

`BLOCK_PROJECT`, `SYNESIS_W067`
