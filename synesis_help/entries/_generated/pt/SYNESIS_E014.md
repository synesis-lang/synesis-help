---
id: SYNESIS_E014
title: "SYNESIS_E014"
category: diagnostic
summary: "Conceito em posicao de codigo com nome identico a uma relacao. (erro 14)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E014 — Erro

## Descrição

Conceito em posicao de codigo com nome identico a uma relacao. (erro 14)

## Mensagem do compilador

```text
The element `exemplo` appears in this chain in a concept position,
  but it is also declared as a relation in the template for the field
  `nome_do_campo`. This ambiguity keeps the compiler from
  determining the element's role in the chain.
  Rename the concept in the organizing model so it differs from the
  relation names, or rename the relation in the template.
```

## Onde aparece

- **ConceptNameMatchesRelation**: `name`, `field_name`
