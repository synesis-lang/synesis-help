---
id: SYNESIS_W031
title: "SYNESIS_W031"
category: diagnostic
summary: "Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W031 — Aviso

## Descrição

Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31)

## Mensagem do compilador

```text
The code `CODIGO_A` appears more than once in the field `nome_do_campo`
  in this block. Repeated codes add no information and may
  distort the counts in exports.
  Remove the duplicate occurrence and keep the code only once.
```

## Onde aparece

- **DuplicateCodeInField**: `field_name`, `code`
