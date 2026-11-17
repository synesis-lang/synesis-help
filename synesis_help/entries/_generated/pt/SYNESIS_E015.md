---
id: SYNESIS_E015
title: "SYNESIS_E015"
category: diagnostic
summary: "Conceito em chain contendo espacos. (erro 15)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E015 — Erro

## Descrição

Conceito em chain contendo espacos. (erro 15)

## Mensagem do compilador

```text
The element `exemplo` contains spaces, which are not allowed
  in concept names. The compiler reads each space as a
  separator between distinct elements of the chain.
  Replace the spaces with underscores: `exemplo`.
```

## Onde aparece

- **ConceptWithSpaces**: `concept`
