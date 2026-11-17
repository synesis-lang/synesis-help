---
id: SYNESIS_E026
title: "SYNESIS_E026"
category: diagnostic
summary: "Valor decimal em campo SCALE com intervalo inteiro. (erro 26)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E026 — Erro

## Descrição

Valor decimal em campo SCALE com intervalo inteiro. (erro 26)

## Mensagem do compilador

```text
The value `valor` has decimals, but the field `nome_do_campo`
  was declared with an integer range (`FORMAT [1..1]`).
  This field only accepts integers.
  Use an integer within the range, or ask the project coordinator
  to adjust FORMAT to accept decimals (e.g. `FORMAT [1.5..1.5]`).
```

## Onde aparece

- **DecimalInIntegerScale**: `field_name`, `value`, `min_val`, `max_val`
