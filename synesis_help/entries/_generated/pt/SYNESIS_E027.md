---
id: SYNESIS_E027
title: "SYNESIS_E027"
category: diagnostic
summary: "Valor fora da lista ENUMERATED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E027 — Erro

## Descrição

Valor fora da lista ENUMERATED.

## Mensagem do compilador

```text
O valor `valor` nao e reconhecido para o campo `nome_do_campo`.
  Este campo aceita apenas valores de uma lista fechada.
  Valores disponiveis: `exemplo_a`, `exemplo_b`.
```

## Onde aparece

- **InvalidEnumeratedValue**: `field_name`, `value`, `valid_values`
