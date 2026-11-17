---
id: SYNESIS_E053
title: "SYNESIS_E053"
category: diagnostic
summary: "Operador invalido na declaracao ARITY. (erro 53)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E053 — Erro

## Descrição

Operador invalido na declaracao ARITY. (erro 53)

## Mensagem do compilador

```text
The `ARITY` declaration of the field 'nome_do_campo' uses an
  unrecognized operator: `exemplo`.
  The valid operators are: `>=`, `>`, `<=`, `<`, `=`.
  For example: `ARITY >= 2` means 'at least two concepts per chain'.
```

## Onde aparece

- **InvalidArityOperator**: `field_name`, `operator`
