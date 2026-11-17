---
id: SYNESIS_W067
title: "SYNESIS_W067"
category: diagnostic
summary: "Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W067 — Aviso

## Descrição

Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67)

## Mensagem do compilador

```text
The modification date `exemplo` is earlier than the creation date
  `exemplo` declared in the project's METADATA block. A project cannot
  have been modified before it existed.
  Check the dates and fix the wrong one. The expected format
  is `YYYY-MM-DD`.
```

## Onde aparece

- **ModifiedBeforeCreated**: `modified`, `created`
