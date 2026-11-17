---
id: SYNESIS_E148
title: "SYNESIS_E148"
category: diagnostic
summary: "Bloco preterido com outros campos alem do USE."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E148 — Erro

## Descrição

Bloco preterido com outros campos alem do USE.

## Mensagem do compilador

```text
`exemplo` is an alias (USE) and still has .
  Move the content to the target first (synesis-coder consolidate transfers it
  and archives what does not fit): an alias has only the USE field.
```

## Onde aparece

- **AliasWithContent**: `concept`, `fields`
