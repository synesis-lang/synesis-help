---
id: SYNESIS_E086
title: "SYNESIS_E086"
category: diagnostic
summary: "VALUES definido em campo que nao e ORDERED nem ENUMERATED. (erro 86)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E086 — Erro

## Descrição

VALUES definido em campo que nao e ORDERED nem ENUMERATED. (erro 86)

## Mensagem do compilador

```text
The field 'nome_do_campo' defines a `VALUES` block, but its type is
  `TEXT`. `VALUES` blocks list the valid options of a
  closed vocabulary — they only take effect in `ORDERED` fields (options with
  an order, e.g. Low, Medium, High) or `ENUMERATED` fields (options without order).
  In `TEXT` the list would be ignored during validation.
  Remove the `VALUES` block or change the type to `ORDERED`/`ENUMERATED`.
```

## Onde aparece

- **ValuesOnNonEnumerable**: `field_name`, `field_type`
