---
id: SYNESIS_E016
title: "SYNESIS_E016"
category: diagnostic
summary: "Campo de BUNDLE ausente (violacao de pareamento)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E016 — Erro

## Descrição

Campo de BUNDLE ausente (violacao de pareamento).

## Mensagem do compilador

```text
The fields `exemplo_a, exemplo_b` form an indivisible bundle in this block
  — they represent compound information and must always appear together.
  One or more bundle fields are missing: `exemplo_b`.
  Add the missing fields or remove all fields of the bundle.
  A partial bundle is not valid.
```

## Onde aparece

- **MissingBundleField**: `bundle_fields`, `present_fields`
