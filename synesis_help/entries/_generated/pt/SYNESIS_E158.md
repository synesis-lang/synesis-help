---
id: SYNESIS_E158
title: "SYNESIS_E158"
category: diagnostic
summary: "Modo declarado (MAP de campos ou INSTRUCTION) sem `MAP ... TO OUTPUT`."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E158 — Erro

## Descrição

Modo declarado (MAP de campos ou INSTRUCTION) sem `MAP ... TO OUTPUT`.

## Mensagem do compilador

```text
`exemplo`: no `MAP <fields> TO OUTPUT`. The output is what the model learns
  to produce, so it must be declared. Each key of the Alpaca line comes from `MAP <fields> TO INSTRUCTION | INPUT | OUTPUT`.
  Without any MAP or INSTRUCTION the block keeps the built-in Alpaca pairs.
```

## Onde aparece

- **AlpacaOutputMapMissing**: `block`
