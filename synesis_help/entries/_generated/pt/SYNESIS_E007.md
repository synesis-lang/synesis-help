---
id: SYNESIS_E007
title: "SYNESIS_E007"
category: diagnostic
summary: "Violacao de ARITY em cadeia causal."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E007 — Erro

## Descrição

Violacao de ARITY em cadeia causal.

## Mensagem do compilador

```text
This chain has too few elements. The template requires `exemplo` concepts,
  but only `2` were found.
  A chain must connect at least two concepts with `->`.
  Add the missing elements until the minimum requirement is met.
```

## Onde aparece

- **ChainArityViolation**: `expected`, `found`
