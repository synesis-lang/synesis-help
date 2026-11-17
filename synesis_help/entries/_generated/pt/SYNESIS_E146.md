---
id: SYNESIS_E146
title: "SYNESIS_E146"
category: diagnostic
summary: "USE que aponta para um conceito que tambem e preterido."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E146 — Erro

## Descrição

USE que aponta para um conceito que tambem e preterido.

## Mensagem do compilador

```text
`exemplo` uses `exemplo`, which is also an alias (uses `exemplo`).
  Point directly to `exemplo`: an alias always points to the concept that remains.
```

## Onde aparece

- **UseChain**: `concept`, `target`, `final`
