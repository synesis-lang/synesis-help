---
id: SYNESIS_E070
title: "SYNESIS_E070"
category: diagnostic
summary: "Mesmo @bibref declarado em dois blocos SOURCE no mesmo arquivo. (erro 70)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E070 — Erro

## Descrição

Mesmo @bibref declarado em dois blocos SOURCE no mesmo arquivo. (erro 70)

## Mensagem do compilador

```text
The reference `@@autor2024` appears in two different SOURCE blocks
  in the file `arquivo.syn`. Each bibliographic reference can have
  only one SOURCE block per file.
  Merge the two SOURCE blocks into one, or split the annotations
  into separate `.syn` files.
```

## Onde aparece

- **DuplicateSourceBibref**: `bibref`, `filename`
