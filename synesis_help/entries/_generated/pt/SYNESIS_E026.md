---
id: SYNESIS_E026
title: "SYNESIS_E026"
category: diagnostic
summary: "Valor decimal em campo SCALE com intervalo inteiro. (erro 26)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E026 — Erro

## Descricao

Valor decimal em campo SCALE com intervalo inteiro. (erro 26)

## Mensagem do compilador

```text
O valor `valor` tem casas decimais, mas o campo `nome_do_campo`
  foi declarado com um intervalo de inteiros (`FORMAT [1..1]`).
  Este campo aceita apenas numeros inteiros.
  Use um valor inteiro dentro do intervalo, ou peca ao coordenador do
  projeto que ajuste o FORMAT para aceitar decimais (ex: `FORMAT [1.5..1.5]`).
```

## Onde aparece

- **DecimalInIntegerScale**: `field_name`, `value`, `min_val`, `max_val`
