---
id: SYNESIS_E054
title: "SYNESIS_E054"
category: diagnostic
summary: "FORMAT declarado em campo que nao e TYPE SCALE. (erro 54)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E054 — Erro

## Descrição

FORMAT declarado em campo que nao e TYPE SCALE. (erro 54)

## Mensagem do compilador

```text
The field 'nome_do_campo' declares `FORMAT`, but its type is `TEXT`.
  The `FORMAT [min..max]` declaration is exclusive to SCALE fields.
  This problem is in the template definition.
  Remove the `FORMAT` declaration or change the field type to `SCALE`.
```

## Onde aparece

- **FormatOnNonScale**: `field_name`, `field_type`
