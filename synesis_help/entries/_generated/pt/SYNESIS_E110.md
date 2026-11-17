---
id: SYNESIS_E110
title: "SYNESIS_E110"
category: diagnostic
summary: "Dois campos com NOTE DEFINITION, ou dois com LABEL PREFERRED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E110 — Erro

## Descrição

Dois campos com NOTE DEFINITION, ou dois com LABEL PREFERRED.

## Mensagem do compilador

```text
The role `exemplo` is already on the field `exemplo`; `nome_do_campo`
  cannot have it too. The template has at most one field with this role.
```

## Onde aparece

- **DuplicateUniqueRole**: `field_name`, `role`, `first_field`
