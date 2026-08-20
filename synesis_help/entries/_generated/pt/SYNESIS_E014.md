---
id: SYNESIS_E014
title: "SYNESIS_E014"
category: diagnostic
summary: "Conceito em posicao de codigo com nome identico a uma relacao. (erro 14)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E014 — Erro

## Descrição

Conceito em posicao de codigo com nome identico a uma relacao. (erro 14)

## Mensagem do compilador

```text
O elemento `exemplo` aparece nesta cadeia em posicao de conceito,
  mas tambem esta declarado como relacao no template para o campo
  `nome_do_campo`. Essa ambiguidade impede o compilador de
  determinar o papel do elemento na cadeia.
  Renomeie o conceito na ontologia para que seja distinto dos nomes
  de relacao, ou renomeie a relacao no template.
```

## Onde aparece

- **ConceptNameMatchesRelation**: `name`, `field_name`
