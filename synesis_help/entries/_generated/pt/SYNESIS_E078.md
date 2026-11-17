---
id: SYNESIS_E078
title: "SYNESIS_E078"
category: diagnostic
summary: "IDENTIFIES/REFERS TO em campo que nao e SCOPE SOURCE. (erro 78)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E078 — Erro

## Descrição

IDENTIFIES/REFERS TO em campo que nao e SCOPE SOURCE. (erro 78)

## Mensagem do compilador

```text
The field `nome_do_campo` uses `exemplo`, but it is declared with
  `SCOPE ITEM`. The linkage modifiers (`IDENTIFIES` / `REFERS TO`)
  only make sense in `SCOPE SOURCE` fields — linkage between projects
  works on SOURCEs (collection units), not on ITEMs or concepts.
  Move the modifier to a SOURCE field, or remove it from this field.
```

## Onde aparece

- **LinkageModifierOutsideSource**: `field_name`, `modifier`, `scope`
