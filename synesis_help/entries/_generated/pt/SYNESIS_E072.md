---
id: SYNESIS_E072
title: "SYNESIS_E072"
category: diagnostic
summary: "Entrada em arquivo .bib nao esta em formato BibTeX valido. (erro 72)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E072 — Erro

## Descrição

Entrada em arquivo .bib nao esta em formato BibTeX valido. (erro 72)

## Mensagem do compilador

```text
The entry `@exemplo` in the references file `arquivo.syn`
  is not valid BibTeX and was ignored by the compiler. Because of
  that, any `@bibref` pointing to it will be reported as not
  found.
  A valid BibTeX entry has three parts: a type, the citation key
  in braces, and comma-separated fields using `=`:
    @book{exemplo,
        title = {Title of the work},
        year = {2024}
    }
  Check that the entry starts with a type (@book, @article, @misc...),
  that the key is in braces `{ }`, and that each field uses `=` (not `:`).
```

## Onde aparece

- **MalformedBibliographyEntry**: `filename`, `entry_key`
