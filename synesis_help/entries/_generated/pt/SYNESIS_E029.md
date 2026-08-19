---
id: SYNESIS_E029
title: "SYNESIS_E029"
category: diagnostic
summary: "Valor fora do range ORDERED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E029 — Erro

## Descricao

Valor fora do range ORDERED.

## Mensagem do compilador

```text
O valor `valor` nao e valido para o campo `nome_do_campo`.
  Este campo usa uma escala ordenada com opcoes especificas.
  Opcoes disponiveis: `exemplo_a`, `exemplo_b`.
  Voce pode usar o rotulo textual ou o numero de posicao na escala.
```

## Onde aparece

- **InvalidOrderedValue**: `field_name`, `value`, `valid_options`
