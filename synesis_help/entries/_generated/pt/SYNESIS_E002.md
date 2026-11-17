---
id: SYNESIS_E002
title: "SYNESIS_E002"
category: diagnostic
summary: "ITEM sem SOURCE correspondente."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E002 — Erro

## Descrição

ITEM sem SOURCE correspondente.

## Mensagem do compilador

```text
This ITEM references `@@autor2024`, but there is no SOURCE block with
  that reference in this file. Every ITEM needs a matching SOURCE
  in the same file.
  Create a `SOURCE @@autor2024` block before this ITEM, or check
  that the reference is correct.
```

## Onde aparece

- **OrphanItem**: `bibref`
