---
id: SYNESIS_E066
title: "SYNESIS_E066"
category: diagnostic
summary: "Dois blocos PROJECT no mesmo arquivo .synp. (erro 66)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E066 — Erro

## Descrição

Dois blocos PROJECT no mesmo arquivo .synp. (erro 66)

## Mensagem do compilador

```text
This project file has two PROJECT blocks. Only one PROJECT
  block is allowed per file — the compiler would not know which of
  the two to use as the entry point.
  Remove the duplicate block or split the projects into separate `.synp` files.
```

## Onde aparece

- **DuplicateProjectBlock**: —
