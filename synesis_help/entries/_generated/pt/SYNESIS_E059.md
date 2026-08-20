---
id: SYNESIS_E059
title: "SYNESIS_E059"
category: diagnostic
summary: "Valores duplicados dentro de um mesmo bloco VALUES. (erro 59)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E059 — Erro

## Descrição

Valores duplicados dentro de um mesmo bloco VALUES. (erro 59)

## Mensagem do compilador

```text
O campo 'nome_do_campo' tem o valor `valor` declarado mais de
  uma vez no bloco `VALUES`. Valores duplicados causam ambiguidade e podem
  gerar resultados inconsistentes na exportacao.
  Remova a entrada duplicada.
```

## Onde aparece

- **DuplicateValue**: `field_name`, `value`
