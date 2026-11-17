---
id: SYNESIS_E049
title: "SYNESIS_E049"
category: diagnostic
summary: "TYPE ORDERED sem bloco VALUES. (erro 49)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E049 — Erro

## Descrição

TYPE ORDERED sem bloco VALUES. (erro 49)

## Mensagem do compilador

```text
The field 'nome_do_campo' is of type ORDERED, but does not define a
  `VALUES` block with the valid options and their order. Without it, there is no
  way to validate the values entered or show the scale to researchers.
  Add a `VALUES` block listing the options in ascending order.
```

## Onde aparece

- **OrderedWithoutValues**: `field_name`
