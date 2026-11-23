---
id: GUIDE_CASE_STUDIES
title: "Case studies: start from a design"
category: overview
summary: "Nine complete projects adapted from real research, and how to pick the one closest to yours."
see_also: [CASE_LITERATURE_REVIEW, CASE_FACTOR_REVIEW, CASE_PASSAGE_LEXICON, CASE_NEWS_FRAMING, CASE_LINKED_PROFILES, CASE_SURVEY_RESPONSES, CASE_TOPICAL_INDEX, CASE_PARTICIPATORY_DIAGNOSIS, CASE_CAUSATION_CODING]
source: authored
order: 15
---

# Case studies: start from a design

## Why start here

A template is a research design written down. The fastest way to write
yours is to start from a design that already works and change its
vocabulary. Each case below is a **complete project** (template,
annotations, ontology, project file and exports) adapted from real research
done with Synesis. Names, sources and excerpts are fictitious; the designs
are real.

Every case compiles: the guide's own checks build each project and run the
compiler on it whenever the guide or the compiler changes.

## Pick by research design

| If your research is... | Start from | Key pattern |
|---|---|---|
| a systematic or scoping review of mechanisms | `CASE_LITERATURE_REVIEW` | chain + epistemic status in a BUNDLE |
| a review of factors and their effects | `CASE_FACTOR_REVIEW` | sign and condition per relation |
| a close reading of one term across texts | `CASE_PASSAGE_LEXICON` | TOML records, two-language quotations |
| content or frame analysis of media | `CASE_NEWS_FRAMING` | story-level and excerpt-level coding |
| an assessment combining several sources | `CASE_LINKED_PROFILES` | linked projects, shared rubric |
| open-ended survey answers | `CASE_SURVEY_RESPONSES` | respondent variables at SOURCE |
| a vocabulary, index or codebook | `CASE_TOPICAL_INDEX` | ROLE hierarchy, USE, SKOS |
| a participatory or SWOT diagnosis | `CASE_PARTICIPATORY_DIAGNOSIS` | importance scale, dimensions |
| causal or process analysis of interviews | `CASE_CAUSATION_CODING` | ARITY >= 3, causal roles |

## Pick by pattern

| You need to... | Look at |
|---|---|
| keep whether a claim is asserted, hypothesized or denied | `CASE_LITERATURE_REVIEW` |
| attach direction and conditions to each effect | `CASE_FACTOR_REVIEW` |
| take metadata from structured records instead of typing it | `CASE_PASSAGE_LEXICON`, `CASE_NEWS_FRAMING` |
| code once per source what holds for the whole source | `CASE_NEWS_FRAMING`, `CASE_SURVEY_RESPONSES` |
| link independent projects by a shared entity | `CASE_LINKED_PROFILES` |
| share one ontology between projects | `CASE_LINKED_PROFILES` |
| order categories and write them as an index | `CASE_FACTOR_REVIEW` |
| build a taxonomy and publish it as SKOS | `CASE_TOPICAL_INDEX`, `CASE_LITERATURE_REVIEW` |
| produce fine-tuning data that keeps the status | `CASE_LITERATURE_REVIEW` |
| force a mediator in every causal chain | `CASE_CAUSATION_CODING` |

## How each case is written

Every case follows the same path, so readers and agents know where to look:

1. **Research question**: what the design must answer.
2. **Corpus and unit**: what SOURCE, ITEM and ONTOLOGY stand for.
3. **Template**: the `.synt`, with `GUIDELINES` where judgement is needed.
4. **Annotation**: `.syn`, `.syno` and, when used, TOML records.
5. **Project and exports**: the `.synp` with `QUESTIONS` and `EXPORT`.
6. **Design decisions**: why the template is shaped this way.
7. **Adapt it**: what to change for neighbouring designs.

Each code block starts with the name of its file (`# review.synt`). Copy
the blocks into files with those names and run `synesis compile` on the
`.synp`; a `references.bib` with the cited keys is the only thing to add.

## From case to your project

1. Copy the closest case.
2. Rename fields and values to the vocabulary of your field; keep the
   structure (what is SOURCE, what is ITEM, what is bundled).
3. Rewrite the `GUIDELINES` with Correct/Wrong pairs from your own material.
4. Code a pilot of 10 to 20 sources, compile, and read the diagnostics.
5. Check the `QUESTIONS`: if the pilot cannot answer one, the template is
   missing a field.

## See also

`GUIDE_START`, `GUIDE_PRIMITIVES`, `BLOCK_TEMPLATE`, `MOD_GUIDELINES`
