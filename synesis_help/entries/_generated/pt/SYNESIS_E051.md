---
id: SYNESIS_E051
title: "SYNESIS_E051"
category: diagnostic
summary: "TYPE SCALE sem declaracao FORMAT. (erro 51)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E051 — Erro

## Descrição

TYPE SCALE sem declaracao FORMAT. (erro 51)

## Mensagem do compilador

```text
O campo 'nome_do_campo' e do tipo SCALE, mas nao declara o intervalo
  numerico permitido. Sem o intervalo, o compilador nao pode verificar se
  os valores estao dentro da faixa esperada.
  Adicione uma declaracao como `FORMAT [0..10]` para definir o valor
  minimo e maximo aceitos.
```

## Onde aparece

- **ScaleWithoutFormat**: `field_name`
