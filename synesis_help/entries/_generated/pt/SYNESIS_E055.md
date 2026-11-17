---
id: SYNESIS_E055
title: "SYNESIS_E055"
category: diagnostic
summary: "ARITY declarado em campo que nao e TYPE CHAIN. (erro 55)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E055 — Erro

## Descrição

ARITY declarado em campo que nao e TYPE CHAIN. (erro 55)

## Mensagem do compilador

```text
The field 'nome_do_campo' declares `ARITY`, but its type is `TEXT`.
  The `ARITY` declaration is exclusive to CHAIN fields.
  This problem is in the template definition.
  Remove the `ARITY` declaration or change the field type to `CHAIN`.
```

## Onde aparece

- **ArityOnNonChain**: `field_name`, `field_type`
