---
id: SYNESIS_E079
title: "SYNESIS_E079"
category: diagnostic
summary: "Campo REQUIRED ... ON BIBLIOGRAPHY sem valor no .bib do SOURCE. (erro 79)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E079 — Erro

## Descrição

Campo REQUIRED ... ON BIBLIOGRAPHY sem valor no .bib do SOURCE. (erro 79)

## Mensagem do compilador

```text
The field `nome_do_campo` was declared `REQUIRED ... ON BIBLIOGRAPHY`,
  so its value must come from the SOURCE's `.bib` entry — not from the text.
  But the entry `@autor2024` has no `nome_do_campo` field.
  Add `nome_do_campo = {...}` to the entry `@autor2024` in the
  `.bib` file, or remove the `ON BIBLIOGRAPHY` requirement from the template.
```

## Onde aparece

- **MissingBibliographyValue**: `field_name`, `bibref`
