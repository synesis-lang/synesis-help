---
id: SYNESIS_W071
title: "SYNESIS_W071"
category: diagnostic
summary: "Dois blocos ONTOLOGY com description identica. (erro 71)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W071 — Aviso

## Descrição

Dois blocos ONTOLOGY com description identica. (erro 71)

## Mensagem do compilador

```text
The concepts `exemplo` and `exemplo` have exactly
  the same description. This usually indicates a copy error — two
  distinct concepts should not have identical definitions.
  Review the definitions and make the descriptions differ, or check whether
  the two concepts should be a single one.
```

## Onde aparece

- **DuplicateOntologyDescription**: `concept_a`, `concept_b`
