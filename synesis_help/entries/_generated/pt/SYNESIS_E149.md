---
id: SYNESIS_E149
title: "SYNESIS_E149"
category: diagnostic
summary: "Depois de resolver USE, um conceito seria pai de si mesmo."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E149 — Erro

## Descrição

Depois de resolver USE, um conceito seria pai de si mesmo.

## Mensagem do compilador

```text
`exemplo` has `exemplo` in `nome_do_campo`, but `exemplo` uses
  `exemplo`: after consolidation, the concept would be its own parent.
```

## Onde aparece

- **HierarchyCollapsedByUse**: `concept`, `field_name`, `parent`
