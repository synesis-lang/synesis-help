---
id: SYNESIS_E020
title: "SYNESIS_E020"
category: diagnostic
summary: "Campo REQUIRED ausente."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E020 — Erro

## Descrição

Campo REQUIRED ausente.

## Mensagem do compilador

```text
The field `nome_do_campo` is required in this ITEM block,
  but it was not found.
  Add the line `nome_do_campo: <value>` to the block before
  `END ITEM`.
```

## Onde aparece

- **MissingRequiredField**: `field_name`, `block_type`
