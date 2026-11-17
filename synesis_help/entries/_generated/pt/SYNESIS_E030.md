---
id: SYNESIS_E030
title: "SYNESIS_E030"
category: diagnostic
summary: "Valor SCALE fora do intervalo [min..max]."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E030 — Erro

## Descrição

Valor SCALE fora do intervalo [min..max].

## Mensagem do compilador

```text
The value `1.5` is outside the allowed range for the field
  `nome_do_campo`. This field only accepts values between
  `1.5` and `1.5`.
  Fix the value so it falls within this range.
```

## Onde aparece

- **ScaleOutOfRange**: `field_name`, `value`, `min_value`, `max_value`
