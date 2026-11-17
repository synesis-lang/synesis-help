---
id: SYNESIS_E057
title: "SYNESIS_E057"
category: diagnostic
summary: "Dois ou mais blocos SCOPE FIELDS no mesmo template. (erro 57)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E057 — Erro

## Descrição

Dois ou mais blocos SCOPE FIELDS no mesmo template. (erro 57)

## Mensagem do compilador

```text
The template has more than one `ITEM FIELDS` block. Only one block
  of this kind is allowed per template — two would make it ambiguous
  which fields are valid in the blocks.
  Merge all declarations into a single `ITEM FIELDS` block.
```

## Onde aparece

- **DuplicateScopeBlock**: `scope`
