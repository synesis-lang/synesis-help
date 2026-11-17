---
id: SYNESIS_E129
title: "SYNESIS_E129"
category: diagnostic
summary: "prefLabel derivado do nome coincide com um rotulo de outro conceito."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E129 — Erro

## Descrição

prefLabel derivado do nome coincide com um rotulo de outro conceito.

## Mensagem do compilador

```text
`exemplo`: the preferred label of `exemplo`, derived from the name
  ("exemplo"), matches a label of `exemplo`. Declare a
  LABEL PREFERRED for one of the two.
```

## Onde aparece

- **DerivedLabelConflict**: `block`, `concept`, `label`, `other`
