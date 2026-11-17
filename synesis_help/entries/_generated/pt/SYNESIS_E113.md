---
id: SYNESIS_E113
title: "SYNESIS_E113"
category: diagnostic
summary: "Mais de um termo em LABEL PREFERRED num conceito."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E113 — Erro

## Descrição

Mais de um termo em LABEL PREFERRED num conceito.

## Mensagem do compilador

```text
The concept `exemplo` has 7 preferred labels (e, x, e, m, p, l, o).
  LABEL PREFERRED takes a single term; the others go in LABEL ALTERNATIVE.
```

## Onde aparece

- **MultiplePreferredLabels**: `concept`, `terms`
