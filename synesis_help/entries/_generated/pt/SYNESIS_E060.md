---
id: SYNESIS_E060
title: "SYNESIS_E060"
category: diagnostic
summary: "Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E060 — Erro

## Descrição

Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60)

## Mensagem do compilador

```text
The `ARITY` declaration of the field 'nome_do_campo' uses the value
  `valor`, which is not an integer.
  ARITY counts concepts per chain and must be an integer.
  For example: `ARITY >= 2`, not `ARITY >= 2.0`.
```

## Onde aparece

- **NonIntegerArityValue**: `field_name`, `value`
