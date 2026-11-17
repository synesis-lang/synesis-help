---
id: SYNESIS_E017
title: "SYNESIS_E017"
category: diagnostic
summary: "Campos de BUNDLE com quantidades diferentes."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E017 — Erro

## Descrição

Campos de BUNDLE com quantidades diferentes.

## Mensagem do compilador

```text
BUNDLE (exemplo_a, exemplo_b) has different counts: exemplo_a=2, exemplo_b=3
  Every bundle field must appear the same number of times.
  Add or remove entries to make the counts equal.
```

## Onde aparece

- **BundleCountMismatch**: `bundle_fields`, `counts`
