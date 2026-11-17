---
id: SYNESIS_E130
title: "SYNESIS_E130"
category: diagnostic
summary: "prefLabel derivado coincide com altLabel/hiddenLabel do mesmo conceito (S13)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E130 — Erro

## Descrição

prefLabel derivado coincide com altLabel/hiddenLabel do mesmo conceito (S13).

## Mensagem do compilador

```text
`exemplo`: the preferred label derived from `exemplo` ("exemplo")
  is also an alternative or hidden label of the same concept (SKOS S13).
  Remove the term from LABEL ALTERNATIVE/HIDDEN or declare a LABEL PREFERRED.
```

## Onde aparece

- **DerivedLabelOverlap**: `block`, `concept`, `label`
