---
id: SYNESIS_E029
title: "SYNESIS_E029"
category: diagnostic
summary: "Valor fora do range ORDERED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E029 — Erro

## Descrição

Valor fora do range ORDERED.

## Mensagem do compilador

```text
The value `valor` is not valid for the field `nome_do_campo`.
  This field uses an ordered scale with specific options.
  Opcoes disponiveis: `exemplo_a`, `exemplo_b`.
  You can use the text label or the position number on the scale.
```

## Onde aparece

- **InvalidOrderedValue**: `field_name`, `value`, `valid_options`
