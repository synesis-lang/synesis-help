---
id: SYNESIS_E052
title: "SYNESIS_E052"
category: diagnostic
summary: "Sintaxe invalida na declaracao FORMAT de campo SCALE. (erro 52)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E052 — Erro

## Descrição

Sintaxe invalida na declaracao FORMAT de campo SCALE. (erro 52)

## Mensagem do compilador

```text
O intervalo declarado em `FORMAT` para o campo 'nome_do_campo' nao
  esta no formato esperado: `exemplo`
  O formato correto usa colchetes e dois pontos como separador: `[minimo..maximo]`.
  Exemplos validos: `[1..5]`, `[0..100]`, `[0.0..1.0]`.
```

## Onde aparece

- **InvalidFormatSyntax**: `field_name`, `format_str`
