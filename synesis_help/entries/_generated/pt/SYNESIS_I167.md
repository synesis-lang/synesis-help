---
id: SYNESIS_I167
title: "SYNESIS_I167"
category: diagnostic
summary: "Modo Alpaca embutido com template cujo bundle de CHAIN tem qualificador."
severity: Informação
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_I167 — Informação

## Descrição

Modo Alpaca embutido com template cujo bundle de CHAIN tem qualificador.

## Mensagem do compilador

```text
`exemplo`: the built-in Alpaca pairs do not carry `nome_do_campo`, which
  qualifies `exemplo` in a BUNDLE: every relation is exported as if asserted.
  Declare the composition with `EXPORT ALPACA` and `MAP exemplo, nome_do_campo TO OUTPUT`.
```

## Onde aparece

- **AlpacaLegacyDropsQualifier**: `block`, `field_name`, `chain_field`
