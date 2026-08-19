---
id: SYNESIS_E030
title: "SYNESIS_E030"
category: diagnostic
summary: "Valor SCALE fora do intervalo [min..max]."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E030 — Erro

## Descricao

Valor SCALE fora do intervalo [min..max].

## Mensagem do compilador

```text
O valor `1.5` esta fora do intervalo permitido para o campo
  `nome_do_campo`. Este campo aceita apenas valores entre
  `1.5` e `1.5`.
  Corrija o valor para que fique dentro desse intervalo.
```

## Onde aparece

- **ScaleOutOfRange**: `field_name`, `value`, `min_value`, `max_value`
