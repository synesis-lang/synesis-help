---
id: GUIDE_REVIEW
title: "Reviewing AI annotation"
category: overview
summary: "The review pipeline: check anchors, propose, canonicalize and accept corrections without losing data."
see_also: [ECO_CODER, GUIDE_ECOSYSTEM, MOD_GUIDELINES, GUIDE_FILES, TYPE_CHAIN]
source: authored
order: 70
---

# Reviewing AI annotation

## The problem

LLM-generated annotation is not finished data. The model writes blocks that
are syntactically valid (the compiler accepts them) and still claims things
the source does not support. Compiling without errors says the **form** is
right, not that the **reading** is.

The review pipeline separates two things extraction mixes up: **proposing** a
correction and **accepting** it. The researcher accepts.

## The three phases

| Phase | Command | Reads | Writes | LLM |
|---|---|---|---|---|
| 1 | `critique` | `.syn` | `.synr` | yes |
| 2 | `normalize` | `.synr` | `.synr` | yes |
| 3 | `incorporate` | `.synr` | `.syn` | **no** |

No phase changes the original `.syn`. The review lives in its own file, the
`.synr`, and becomes annotation only in the final step, which is
deterministic.

```text
annotations/corpus.syn
        │  critique
        ▼
revisions/corpus.synr        ← proposals, in # REVISION blocks
        │  normalize
        ▼
revisions/corpus.synr        ← codes canonicalized across the corpus
        │  incorporate
        ▼
annotations/corpus_final.syn ← accepted, no LLM
```

## `anchor`: the check that costs nothing

Before spending tokens on `critique`, run `anchor`. Without any LLM it checks
whether each quoted excerpt **actually occurs** in the source text, and puts
every quotation in one of three states:

| State | Meaning |
|---|---|
| literal | the excerpt occurs exactly as written |
| anchored | it occurs after normalizing spacing, quotes and case |
| not found | it does not occur: the model rewrote instead of quoting |

```text
synesis-coder anchor annotations/corpus.syn --project project.synp
synesis-coder anchor annotations/ --source-dir texts/ --json report.json
```

`--literal` accepts only exact matches; `--strict` exits with code 1 when any
excerpt is not found, which suits continuous integration. It complements the
compiler, which validates enums, ranges, required fields, `BUNDLE` and chain
relations, but cannot know whether a quotation occurs in the source.

## 1. `critique`: propose

Rereads each `ITEM` against the source excerpt it annotates and writes
`# REVISION` blocks for what it judges defective.

```text
synesis-coder critique --project project.synp annotations/corpus.syn
```

`--sensitivity` sets the volume: `lenient` (exploratory corpus, only what is
clearly wrong), `standard` (default), `strict` (final corpus, full manual
review). A number from `0.0` to `1.0` is also accepted. High sensitivity
produces **more false positives**, not more truth: the model starts flagging
readings the template allows.

## 2. `normalize`: canonicalize

`critique` looks at one `ITEM` at a time and does not know that
`Social_Acceptance`, `social_acceptance` and `SocialAcceptance` are the same
concept. `normalize` looks at the whole corpus and unifies.

```text
synesis-coder normalize --project project.synp \
    --output-dir revisions/ revisions/*.synr
```

`--confidence` (default `0.65`) is the floor to accept a unification.

## 3. `incorporate`: accept

Applies the `.synr` and writes the final `.syn`. It **does not call an LLM**:
it is the phase you can repeat, audit and version.

```text
synesis-coder incorporate --backup revisions/corpus.synr
```

An ambiguous correction is **rejected, not guessed**. When several chains
share a source node, a correction that does not identify its target uniquely
would be applied to the first occurrence and erase a value it did not
address. The command prefers not to apply and to say so. Use `--backup`
whenever the target already exists.

## `refine`: optional

`refine` re-extracts the flagged `ITEM` blocks, using the critique as
context. It is opt-in and uses an LLM. Unlike `incorporate`, it **rewrites**
instead of applying point corrections: use it when the problem is the whole
reading of the item, not one field.

## Recommended order

```text
1. anchor       # free, offline: fix what it reports first
2. critique     # --sensitivity standard
3. (read the .synr)
4. normalize    # only meaningful over the whole corpus
5. incorporate  # --backup
6. synesis compile
```

Step 3 is not decoration. The `.synr` is readable text, made to be read: it is
where you decide what enters your data.

## See also

`ECO_CODER`, `GUIDE_ECOSYSTEM`, `MOD_GUIDELINES`, `GUIDE_FILES`
