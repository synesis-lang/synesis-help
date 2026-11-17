---
id: SYNESIS_E051
title: "SYNESIS_E051"
category: diagnostic
summary: "TYPE SCALE sem declaracao FORMAT. (erro 51)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E051 — Erro

## Descrição

TYPE SCALE sem declaracao FORMAT. (erro 51)

## Mensagem do compilador

```text
The field 'nome_do_campo' is of type SCALE, but does not declare the allowed
  numeric range. Without the range, the compiler cannot check whether
  the values fall within the expected interval.
  Add a declaration such as `FORMAT [0..10]` to set the minimum
  and maximum accepted values.
```

## Onde aparece

- **ScaleWithoutFormat**: `field_name`
