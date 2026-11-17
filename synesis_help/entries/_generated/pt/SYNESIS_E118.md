---
id: SYNESIS_E118
title: "SYNESIS_E118"
category: diagnostic
summary: "Ciclo na hierarquia (uniao das especies)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E118 — Erro

## Descrição

Ciclo na hierarquia (uniao das especies).

## Mensagem do compilador

```text
The hierarchy has a cycle: e -> x -> e -> m -> p -> l -> o.
  A concept cannot be, directly or indirectly, broader than itself.
```

## Onde aparece

- **CyclicHierarchy**: `path`
