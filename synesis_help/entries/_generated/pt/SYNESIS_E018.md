---
id: SYNESIS_E018
title: "SYNESIS_E018"
category: diagnostic
summary: "BUNDLE declarado com apenas um campo. (erro 18)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E018 — Erro

## Descrição

BUNDLE declarado com apenas um campo. (erro 18)

## Mensagem do compilador

```text
The bundle `e, x, e, m, p, l, o` in the template was declared with only one field.
  A bundle needs at least two fields — it exists to ensure that
  related information always appears together.
  This problem is in the template definition. If you are not the author
  of the template, tell the project coordinator.
  Add the other fields to the bundle or remove the BUNDLE declaration,
  making the field simply REQUIRED or OPTIONAL.
```

## Onde aparece

- **SingleFieldBundle**: `bundle_fields`
