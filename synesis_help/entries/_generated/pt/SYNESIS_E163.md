---
id: SYNESIS_E163
title: "SYNESIS_E163"
category: diagnostic
summary: "Campos de dois bundles diferentes: nao ha uma unidade unica por linha."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E163 — Erro

## Descrição

Campos de dois bundles diferentes: nao ha uma unidade unica por linha.

## Mensagem do compilador

```text
`exemplo`: the fields come from more than one BUNDLE: .
  One BUNDLE sets the lines (one line per occurrence); fields outside it are
  context. Fields of two bundles would pair occurrences that do not belong together.
```

## Onde aparece

- **AlpacaMultipleBundles**: `block`, `bundles`
