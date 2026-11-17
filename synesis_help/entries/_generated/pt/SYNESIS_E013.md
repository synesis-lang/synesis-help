---
id: SYNESIS_E013
title: "SYNESIS_E013"
category: diagnostic
summary: "Chain sem operador -> entre elementos. (erro 13)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E013 — Erro

## Descrição

Chain sem operador -> entre elementos. (erro 13)

## Mensagem do compilador

```text
The elements of this chain are not separated by the `->` operator.
  Without the arrow, the compiler cannot tell where one element
  ends and the next one begins.
  Value found: `exemplo`
  Rewrite it connecting the elements with `->`, for example:
  `ConceptA -> ConceptB` or `ConceptA -> RELATION -> ConceptB`
```

## Onde aparece

- **ChainWithoutArrowOperator**: `raw_value`
