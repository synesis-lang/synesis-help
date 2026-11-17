---
id: SYNESIS_E138
title: "SYNESIS_E138"
category: diagnostic
summary: "Campo de ONTOLOGY numa PHASE ANNOTATIONS, ou de SOURCE/ITEM numa PHASE ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E138 — Erro

## Descrição

Campo de ONTOLOGY numa PHASE ANNOTATIONS, ou de SOURCE/ITEM numa PHASE ONTOLOGY.

## Mensagem do compilador

```text
`exemplo`: the field `nome_do_campo` belongs to scope exemplo.
  PHASE ANNOTATIONS produces SOURCE and ITEM fields; PHASE ONTOLOGY, ONTOLOGY fields.
```

## Onde aparece

- **PhaseScopeMismatch**: `phase`, `field_name`, `field_scope`
