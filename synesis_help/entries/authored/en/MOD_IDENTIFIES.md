---
id: MOD_IDENTIFIES
title: "IDENTIFIES / REFERS TO"
category: modifier
summary: "Links independent projects: a primary key on one side, a foreign key on the other."
syntax: "IDENTIFIES <entity> | REFERS TO <entity>"
see_also: [LINKAGE_SCOPES, GUIDE_MULTIPROJECT, BLOCK_SOURCE, SYNESIS_E077, SYNESIS_E078, SYNESIS_E081, SYNESIS_W083, CASE_LINKED_PROFILES]
source: authored
order: 80
---

# IDENTIFIES / REFERS TO

## Description

The pair that **links independent projects** without merging them.

One project declares `IDENTIFIES` on a field: that field becomes the key that
identifies an entity, and the project is its **owner**. Another project
declares `REFERS TO` with the same label: it points to that entity.

Each project still compiles alone. The link is resolved only when you compile
them together (the *link step*). `IDENTIFIES` is also how a dataset record
becomes a SOURCE: the key of the TOML record identifies the source
(`MOD_ON_BIBLIOGRAPHY`).

## Syntax

```synesis
FIELD <name> TYPE <type>
    SCOPE SOURCE
    <IDENTIFIES|REFERS TO> <entity>
END FIELD
```

`<>` value to replace · `|` alternative

## Example

```synesis
FIELD staff_id TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES researcher
END FIELD
```

```synesis
FIELD author_id TYPE TEXT
    SCOPE SOURCE
    REFERS TO researcher
END FIELD
```

The first field belongs to the project that owns the entity; the second to a
project that points to it.

## Who should own it

Pick as owner the project with the **widest coverage** of the key. If an
identifier appears in 100% of the records of one project and 60% of another,
the first is the natural owner. The opposite choice turns normal absence into
constant noise.

## Orphans are normal

A `REFERS TO` whose value matches no `IDENTIFIES` raises a **warning**
(`SYNESIS_W083`), not an error. This is deliberate: in real corpora not every
occurrence has a match. Leave the field out when the value does not exist;
never infer the key from a similar name.

## Rules

- Only in `SCOPE SOURCE` (`SYNESIS_E078`).
- `IDENTIFIES` values are unique across the `SOURCE` blocks
  (`SYNESIS_E077`).
- Two projects cannot declare `IDENTIFIES` for the same label
  (`SYNESIS_E081`): an entity has one owner.
- Types must match on both sides (`SYNESIS_E082`).
- Compiled alone, the `REFERS TO` side reports information (`SYNESIS_I080`),
  not an error: the external reference is resolved only in the link step.

## See also

`GUIDE_MULTIPROJECT`, `LINKAGE_SCOPES`, `BLOCK_SOURCE`,
`CASE_LINKED_PROFILES`, `SYNESIS_W083`
