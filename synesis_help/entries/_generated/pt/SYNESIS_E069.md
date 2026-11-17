---
id: SYNESIS_E069
title: "SYNESIS_E069"
category: diagnostic
summary: "Dois FIELD com o mesmo nome no template. (erro 69)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E069 — Erro

## Descrição

Dois FIELD com o mesmo nome no template. (erro 69)

## Mensagem do compilador

```text
The field 'nome_do_campo' is defined more than once in the template.
  Field names must be unique. Remove the duplicate definition or rename
  one of the fields if they represent different information.
```

## Onde aparece

- **DuplicateFieldName**: `field_name`
