---
id: CASE_PASSAGE_LEXICON
title: "One term across a corpus of passages"
category: case_study
summary: "Exegetical study of a word family: passages come from TOML records, every occurrence is read in two languages and mapped as relations."
see_also: [GUIDE_CASE_STUDIES, MOD_ON_BIBLIOGRAPHY, MOD_IDENTIFIES, MOD_INCLUDE, TYPE_QUOTATION, TYPE_CHAIN]
source: authored
order: 30
---

# One term across a corpus of passages

Adapted from a real exegetical study of a word family in an ancient corpus.
The term, passages and readings here are fictitious.

## Research question

*How does the corpus relate one concept (here, "wisdom") to other realities?*
Each occurrence of the word family is read in its grammatical context, and
each reading becomes a relation between lemmas of the text itself.

## Corpus and unit

- **SOURCE:** one passage. Its reference and both texts (original and
  translation) come from a **TOML record**, never retyped in the annotation.
- **ITEM:** one relation of one occurrence: the lemma, its polarity, the
  excerpt in both languages, the grammatical evidence and the chain.
- **ONTOLOGY:** the lemmas, defined only by their use in the corpus.

## Template

```synesis
# lexicon.synt
TEMPLATE lexicon

SOURCE FIELDS
    REQUIRED passage ON DATASET "passage.id"
    REQUIRED reference ON DATASET "passage.reference"
    REQUIRED original ON DATASET "text.original"
    REQUIRED translation ON DATASET "text.translation"
END SOURCE FIELDS

ITEM FIELDS
    REQUIRED lemma, polarity, excerpt_tr, excerpt_or
    REQUIRED evidence, chain
    OPTIONAL note
END ITEM FIELDS

ONTOLOGY FIELDS
    REQUIRED gloss
END ONTOLOGY FIELDS

FIELD passage TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES passage
END FIELD

FIELD reference TYPE TEXT
    SCOPE SOURCE
END FIELD

FIELD original TYPE TEXT
    SCOPE SOURCE
END FIELD

FIELD translation TYPE TEXT
    SCOPE SOURCE
END FIELD

FIELD lemma TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Member of the word family in this occurrence.
    VALUES
        sophia: the noun, wisdom
        sophos: the adjective, wise
    END VALUES
END FIELD

FIELD polarity TYPE ENUMERATED
    SCOPE ITEM
    DESCRIPTION Whether the text affirms or denies the relation.
    VALUES
        affirmed: the relation holds in the text
        denied: the text negates it
        questioned: the text asks about it
    END VALUES
END FIELD

FIELD excerpt_tr TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION Excerpt of the translation that carries the reading.
END FIELD

FIELD excerpt_or TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION The same excerpt in the original language.
END FIELD

FIELD evidence TYPE MEMO
    SCOPE ITEM
    DESCRIPTION The grammar that supports the chain.
    GUIDELINES
        Name the construction: subject, object, genitive.
        Mark [implicit] when the subject is not written.
    END GUIDELINES
END FIELD

FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 2
    RELATIONS
        POSSESSES: A has or holds B
        GIVES: A grants B to someone
        REMOVES: A takes away or annuls B
    END RELATIONS
END FIELD

FIELD note TYPE MEMO
    SCOPE ITEM
END FIELD

FIELD gloss TYPE TEXT
    SCOPE ONTOLOGY
    DESCRIPTION Meaning of the lemma as used in the corpus.
END FIELD
```

## Annotation

The record holds what is fixed about the passage:

```toml
# records/a3_4.toml
[passage]
id = "a3_4"
reference = "A 3.4"

[text]
original = "ho theos didosi sophian tois tapeinois"
translation = "God gives wisdom to the humble"
```

The annotation holds only the reading:

```synesis
# annotations/a3_4.syn
SOURCE @a3_4
END SOURCE

ITEM @a3_4
    lemma: sophia
    polarity: affirmed
    excerpt_tr: God gives wisdom to the humble
    excerpt_or: ho theos didosi sophian tois tapeinois
    evidence: God is the subject of "gives"; wisdom its object.
    chain: theos -> GIVES -> sophia
END ITEM
```

```synesis
# lemmas.syno
ONTOLOGY theos
    gloss: God, as agent in the passages.
END ONTOLOGY

ONTOLOGY sophia
    gloss: Wisdom as something that can be given and lost.
END ONTOLOGY
```

## Project and exports

```synesis
# lexicon.synp
PROJECT lexicon

TEMPLATE "lexicon.synt"
INCLUDE DATASET "records/"
INCLUDE ANNOTATIONS "annotations/"
INCLUDE ONTOLOGY "lemmas.syno"

DESCRIPTION
Every occurrence of one word family in a corpus of passages,
read in translation and anchored in the original.
END DESCRIPTION

EXPORT JSON map
    OUTPUT "out/lexicon.json"
END EXPORT

END PROJECT
```

There is no `.bib`: the key of each record (`IDENTIFIES passage`) is what
identifies the SOURCE.

## Design decisions

- **Texts live in records.** Reference and both texts come from TOML via
  `ON DATASET`, so a correction to a passage is made once.
- **Two quotations per reading.** The translation is the reading reference,
  the original is the anchor; both are literal.
- **Evidence is grammatical.** The memo names the construction that licenses
  the chain, which lets a second reader check each relation.
- **Lemmas are defined by use.** The ontology glosses lemmas from the corpus,
  not from a dictionary, so the map describes the corpus.

## Adapt it

- Any corpus of short units with fixed metadata (laws, verses, aphorisms):
  keep records for the fixed part and annotations for the reading.
- To compare translations, add one QUOTATION field per translation.

## See also

`MOD_ON_BIBLIOGRAPHY`, `MOD_IDENTIFIES`, `MOD_INCLUDE`, `TYPE_QUOTATION`,
`TYPE_CHAIN`, `GUIDE_CASE_STUDIES`
