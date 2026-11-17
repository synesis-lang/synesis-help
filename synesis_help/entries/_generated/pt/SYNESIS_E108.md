---
id: SYNESIS_E108
title: "SYNESIS_E108"
category: diagnostic
summary: "ROLE num campo fora de SCOPE ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E108 — Erro

## Descrição

ROLE num campo fora de SCOPE ONTOLOGY.

## Mensagem do compilador

```text
ROLE exemplo in the field `nome_do_campo` (SCOPE ITEM): roles only apply
  to SCOPE ONTOLOGY fields.
  Hierarchy adopted by the project: move the field to SCOPE ONTOLOGY.
  Hierarchy stated by the source: use a relation in the CHAIN (e.g. TIPO_DE).
```

## Onde aparece

- **RoleOutsideOntology**: `field_name`, `role`, `scope`
