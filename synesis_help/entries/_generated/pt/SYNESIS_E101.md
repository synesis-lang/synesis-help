---
id: SYNESIS_E101
title: "SYNESIS_E101"
category: diagnostic
summary: "Conceito citado num campo CODE do ONTOLOGY sem bloco ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E101 — Erro

## Descrição

Conceito citado num campo CODE do ONTOLOGY sem bloco ONTOLOGY.

## Mensagem do compilador

```text
The field `nome_do_campo` cites the concept `exemplo`, which has no
  ONTOLOGY block. In a CODE field of the organizing model, each item must be a
  declared concept: create the block `ONTOLOGY exemplo` or fix the name.
```

## Onde aparece

- **UndeclaredConcept**: `field_name`, `concept`, `suggestions`
