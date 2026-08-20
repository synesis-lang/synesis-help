---
id: SYNESIS_E053
title: "SYNESIS_E053"
category: diagnostic
summary: "Operador invalido na declaracao ARITY. (erro 53)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E053 — Erro

## Descrição

Operador invalido na declaracao ARITY. (erro 53)

## Mensagem do compilador

```text
A declaracao `ARITY` do campo 'nome_do_campo' usa um operador
  nao reconhecido: `exemplo`.
  Os operadores validos sao: `>=`, `>`, `<=`, `<`, `=`.
  Por exemplo: `ARITY >= 2` significa 'ao menos dois conceitos por cadeia'.
```

## Onde aparece

- **InvalidArityOperator**: `field_name`, `operator`
