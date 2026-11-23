---
id: CASE_NEWS_FRAMING
title: "Framing in news coverage"
category: case_study
summary: "Content analysis of news stories: metadata from records, story-level frame coding at SOURCE, quoted framing devices at ITEM."
see_also: [GUIDE_CASE_STUDIES, MOD_ON_BIBLIOGRAPHY, MOD_SCOPE, TYPE_SCALE, TYPE_DATE, BLOCK_SOURCE]
source: authored
order: 40
---

# Framing in news coverage

Adapted from a real study of how newspapers cover a religious group over
several election cycles. Outlets, stories and excerpts are fictitious.

## Research question

*How do newspapers frame the group, and does the framing change in election
years?* The study follows Entman's four framing functions (problem
definition, causal interpretation, moral evaluation, treatment
recommendation) and codes them at two levels.

## Corpus and unit

- **SOURCE:** one news story. Its metadata (date, outlet, section, election
  year) comes from a TOML record exported by the collection script.
  The **story-level** coding (genre, dominant frame, homogeneity of sources)
  is written in the SOURCE block.
- **ITEM:** one quoted framing device: an excerpt that performs one of the
  four functions, with who speaks.
- **No ontology.** The categories are closed lists in the template; nothing
  emerges from the data, so no `.syno` is needed.

## Template

```synesis
# framing.synt
TEMPLATE framing

SOURCE FIELDS
    REQUIRED story ON DATASET "story.id"
    REQUIRED published ON DATASET "story.published"
    REQUIRED outlet ON DATASET "story.outlet"
    REQUIRED election_year ON DATASET "story.election_year"
    REQUIRED genre, dominant_frame, homogeneity
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED excerpt, function, speaker
END ITEM FIELDS

FIELD story TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES story
END FIELD

FIELD published TYPE DATE
    SCOPE SOURCE
END FIELD

FIELD outlet TYPE TEXT
    SCOPE SOURCE
END FIELD

FIELD election_year TYPE ENUMERATED
    SCOPE SOURCE
    VALUES
        yes: published in an election year
        no: published in another year
    END VALUES
END FIELD

FIELD genre TYPE ENUMERATED
    SCOPE SOURCE
    VALUES
        News: factual report
        Opinion: column or editorial
        Interview: questions and answers
    END VALUES
END FIELD

FIELD dominant_frame TYPE ENUMERATED
    SCOPE SOURCE
    DESCRIPTION Frame that organizes the story as a whole.
    VALUES
        Conflict: disputes between actors
        Morality: values, norms, behaviour
        Power: influence on politics and the state
        Human_interest: personal stories and faith
    END VALUES
    GUIDELINES
        Choose the frame of the headline and lead first.
        Correct: Power (lead about votes and alliances)
        Wrong: Morality (one quote about values, late in text)
    END GUIDELINES
END FIELD

FIELD homogeneity TYPE SCALE
    SCOPE SOURCE
    FORMAT [1..5]
    DESCRIPTION How one-sided the voices in the story are.
END FIELD

FIELD excerpt TYPE QUOTATION
    SCOPE ITEM
END FIELD

FIELD function TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Framing function the excerpt performs.
    VALUES
        Problem: defines a problem
        Cause: attributes a cause
        Moral: passes a moral judgement
        Remedy: recommends a treatment
    END VALUES
END FIELD

FIELD speaker TYPE TEXT
    SCOPE ITEM
    DESCRIPTION Who says it: journalist, or the role of the source.
END FIELD
```

## Annotation

```toml
# records/story_017.toml
[story]
id = "story_017"
published = "2022-08-14"
outlet = "Daily A"
election_year = "yes"
```

```synesis
# annotations/story_017.syn
SOURCE @story_017
    genre: News
    dominant_frame: Power
    homogeneity: 4
END SOURCE

ITEM @story_017
    excerpt: "Leaders are negotiating support in exchange for posts."
    function: Problem
    speaker: journalist
END ITEM

ITEM @story_017
    excerpt: "The alliance reflects the growth of the congregations."
    function: Cause
    speaker: political scientist
END ITEM
```

## Project and exports

```synesis
# framing.synp
PROJECT framing

TEMPLATE "framing.synt"
INCLUDE DATASET "records/"
INCLUDE ANNOTATIONS "annotations/"

QUESTIONS
    Q1: Does the dominant frame shift in election years?
    Q2: Who performs moral evaluation: journalists or sources?
END QUESTIONS

EXPORT XLS team
    OUTPUT "out/framing.xlsx"
END EXPORT

END PROJECT
```

## Design decisions

- **Two levels of coding.** What characterizes the story (genre, frame) is a
  SOURCE field; what a sentence does (a framing function) is an ITEM. Mixing
  them would multiply the story frame by the number of excerpts.
- **Metadata is not typed.** Date, outlet and election year come from the
  collection records, so they cannot be mistyped and stay consistent with the
  original archive.
- **A scale for homogeneity.** `SCALE [1..5]` gives an ordinal judgement that
  can be averaged per outlet and year.
- **Guidelines settle the hard case.** The Correct/Wrong pair tells coders
  which signal wins when the lead and a late quote disagree.

## Adapt it

- Other framing schemes: replace the values of `dominant_frame` and
  `function`; keep the two levels.
- For inter-coder agreement, run two coders on the same records into two
  annotation folders and compare the exported tables.

## See also

`MOD_ON_BIBLIOGRAPHY`, `MOD_SCOPE`, `TYPE_SCALE`, `TYPE_DATE`,
`BLOCK_SOURCE`, `GUIDE_CASE_STUDIES`
