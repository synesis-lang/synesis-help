---
id: SYNESIS_E085
title: "SYNESIS_E085"
category: diagnostic
summary: "Campo REQUIRED ... ON DATASET sem valor no registro do dataset TOML. (erro 85)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E085 — Erro

## Descrição

Campo REQUIRED ... ON DATASET sem valor no registro do dataset TOML. (erro 85)

## Mensagem do compilador

```text
The field `nome_do_campo` was declared `REQUIRED ... ON DATASET`,
  so its value must come from the SOURCE's TOML record — not from the text.
  But the record `@autor2024` has no value at the path
  `exemplo`.
  Check the TOML section/field, or remove the `ON DATASET` requirement
  from the template.
```

## Onde aparece

- **MissingDatasetValue**: `field_name`, `bibref`, `dataset_path`
