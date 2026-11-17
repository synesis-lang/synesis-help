---
id: SYNESIS_E048
title: "SYNESIS_E048"
category: diagnostic
summary: "ARITY incompativel com numero de RELATIONS declaradas. (erro 48)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E048 — Erro

## Descrição

ARITY incompativel com numero de RELATIONS declaradas. (erro 48)

## Mensagem do compilador

```text
The field 'nome_do_campo' declares `ARITY >= 2`, which requires
  at least 2 concepts per chain — but only 2
  relation(s) are defined in `RELATIONS`. To connect 2
  concepts in sequence, at least 1 relations are needed.
  Add the missing relations to the `RELATIONS` block or lower the `ARITY` value.
```

## Onde aparece

- **ArityRelationsMismatch**: `field_name`, `arity`, `n_relations`
