---
id: SYNESIS_E165
title: "SYNESIS_E165"
category: diagnostic
summary: "Alvo de MAP fora de INSTRUCTION/INPUT/OUTPUT, ou FROM nesses alvos."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E165 — Erro

## Descrição

Alvo de MAP fora de INSTRUCTION/INPUT/OUTPUT, ou FROM nesses alvos.

## Mensagem do compilador

```text
`exemplo`: `exemplo` is not a target of EXPORT ALPACA.
  Accepted targets: INSTRUCTION, INPUT and OUTPUT.
```

## Onde aparece

- **AlpacaMapTarget**: `block`, `target`, `with_from`
