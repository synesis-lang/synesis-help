---
id: SYNESIS_E060
title: "SYNESIS_E060"
category: diagnostic
summary: "\"Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60).\""
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E060 — Erro

## Descricao

Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60)

## Mensagem do compilador

```text
A declaracao `ARITY` do campo 'nome_do_campo' usa o valor
  `valor`, que nao e um numero inteiro.
  ARITY conta conceitos por cadeia e deve ser um inteiro.
  Por exemplo: `ARITY >= 2`, nao `ARITY >= 2.0`.
```

## Onde aparece

- **NonIntegerArityValue**: `field_name`, `value`
