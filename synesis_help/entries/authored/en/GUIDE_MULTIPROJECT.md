---
id: GUIDE_MULTIPROJECT
title: "Connected projects"
category: overview
summary: "How independent projects link through shared entities (IDENTIFIES / REFERS TO)."
see_also: [MOD_IDENTIFIES, LINKAGE_SCOPES, BLOCK_SOURCE, GUIDE_PRIMITIVES, SYNESIS_W083, SYNESIS_I080, CASE_LINKED_PROFILES]
source: authored
order: 50
---

# Connected projects

## The problem

Research rarely fits a single project. Heterogeneous sources (CVs, public
profiles, publications, institutional records) have different structures,
fields and collection rhythms.

Putting everything in one project produces a bloated template, full of
optional fields that apply to only part of the data. Keeping them apart,
without links, prevents any cross analysis.

## The solution: shared entities

Each project stays independent, with its own template and compilation. What
joins them are **entities**: one project declares `IDENTIFIES` of an entity,
the others point to it with `REFERS TO`.

The model is the C linker's: each unit compiles alone; external references
are resolved only when you compile the set.

## Example topology

An aggregate with three entities and six projects:

| Project | Entity it owns | Entities it references |
|---|---|---|
| `profiles` | `profile` | `researcher`, `company` |
| `cvs` | `researcher` | — |
| `companies` | `company` | — |
| `publications` | — | `researcher` |
| `posts` | — | `profile` |
| `repositories` | — | `profile` |

Three owners, three referrers. Each entity has **one** owner
(`SYNESIS_E081`).

## Two design decisions

**1. Who owns each entity.** The owner should be the project with the widest
coverage of the key. If the identifier is in 100% of the profiles and 62% of
the CVs, the profiles project is the natural owner.

**2. Which path the link takes.** In the example, `posts` and
`repositories` reference `profile`, not `researcher`, even when the final
interest is the researcher. The reason is semantic: a post is evidence of the
**public profile**, not of the academic CV. The chain profile → CV belongs to
whoever holds both keys. A direct link would work technically and would lie
about provenance.

## Compilation

```bash
synesis compile profiles/               # alone: I080 on external references
synesis compile profiles/ cvs/          # link step: resolves the references
```

Compiled alone, a project with `REFERS TO` reports `SYNESIS_I080`:
information, not an error. External references cannot be resolved in
isolation, and that is expected.

## Orphans

In the link step, a `REFERS TO` without a match becomes `SYNESIS_W083`, a
warning. In real corpora absence is normal: not every professional has a CV,
not every company cited is in the reference list. Treat the warning as a
coverage inventory, not a defect queue.

## See also

`MOD_IDENTIFIES`, `LINKAGE_SCOPES`, `CASE_LINKED_PROFILES`,
`SYNESIS_W083`, `SYNESIS_E081`
