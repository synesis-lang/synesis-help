---
id: SYNESIS_E119
title: "SYNESIS_E119"
category: diagnostic
summary: "O mesmo par filho-pai em duas especies de HIERARCHY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E119 — Erro

## Descrição

O mesmo par filho-pai em duas especies de HIERARCHY.

## Mensagem do compilador

```text
`exemplo` -> `exemplo` appears as exemplo and as exemplo.
  Hierarchical situations are exclusive (Z39.19 §8.3): choose one species.
```

## Onde aparece

- **DuplicateHierarchySpecies**: `child`, `parent`, `first_species`, `second_species`
