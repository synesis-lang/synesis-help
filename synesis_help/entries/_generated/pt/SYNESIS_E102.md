---
id: SYNESIS_E102
title: "SYNESIS_E102"
category: diagnostic
summary: "Item vazio numa lista (`a, , b`) de um campo CODE do ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E102 — Erro

## Descrição

Item vazio numa lista (`a, , b`) de um campo CODE do ONTOLOGY.

## Mensagem do compilador

```text
The list in the field `nome_do_campo` has an empty item (two commas
  in a row, or a comma at the start or end). Remove the extra comma.
```

## Onde aparece

- **InvalidValueForm**: `field_name`
