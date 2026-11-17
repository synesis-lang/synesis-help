---
id: SYNESIS_E116
title: "SYNESIS_E116"
category: diagnostic
summary: "Termo de LABEL igual ao nome de outro conceito."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E116 — Erro

## Descrição

Termo de LABEL igual ao nome de outro conceito.

## Mensagem do compilador

```text
The label `exemplo` of `exemplo` is the name of the concept `exemplo`.
  A label cannot be another concept with a block. If both name the same
  thing, consolidate them with USE (synesis-coder consolidate).
```

## Onde aparece

- **LabelConflictsWithConcept**: `concept`, `term`, `other`
