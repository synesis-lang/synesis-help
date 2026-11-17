---
id: SYNESIS_E047
title: "SYNESIS_E047"
category: diagnostic
summary: "TYPE CHAIN sem declaracao ARITY. (erro 47)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E047 — Erro

## Descrição

TYPE CHAIN sem declaracao ARITY. (erro 47)

## Mensagem do compilador

```text
The field 'nome_do_campo' is of type CHAIN, but does not declare `ARITY`.
  Without ARITY, the compiler cannot check whether the chains written by
  researchers have the minimum number of concepts required.
  Add a declaration such as `ARITY >= 2` to ensure that every chain
  connects at least two concepts.
```

## Onde aparece

- **ChainWithoutArity**: `field_name`
