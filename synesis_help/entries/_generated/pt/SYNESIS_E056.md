---
id: SYNESIS_E056
title: "SYNESIS_E056"
category: diagnostic
summary: "RELATIONS definido em campo que nao e TYPE CHAIN. (erro 56)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E056 — Erro

## Descrição

RELATIONS definido em campo que nao e TYPE CHAIN. (erro 56)

## Mensagem do compilador

```text
The field 'nome_do_campo' defines a `RELATIONS` block, but its type is
  `TEXT`, not `CHAIN`. `RELATIONS` blocks describe the possible
  kinds of link between concepts — they only make sense in fields
  of type CHAIN. Remove the `RELATIONS` block or change the type to `CHAIN`.
```

## Onde aparece

- **RelationsOnNonChain**: `field_name`, `field_type`
