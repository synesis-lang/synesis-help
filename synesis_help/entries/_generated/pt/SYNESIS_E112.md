---
id: SYNESIS_E112
title: "SYNESIS_E112"
category: diagnostic
summary: "Campo do ONTOLOGY com nome de chave canonica do JSON."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E112 — Erro

## Descrição

Campo do ONTOLOGY com nome de chave canonica do JSON.

## Mensagem do compilador

```text
The ONTOLOGY field `nome_do_campo` has the name of a key the compiler
  reserves for the concept in the JSON (concept, location, frequency, source_count,
  parent_chains; or description, when another field has ROLE NOTE DEFINITION).
  The field value would overwrite the key. Rename the field.
```

## Onde aparece

- **ReservedOntologyFieldName**: `field_name`
