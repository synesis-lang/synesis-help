---
id: SYNESIS_E058
title: "SYNESIS_E058"
category: diagnostic
summary: "Valor em bloco VALUES com espaco no inicio ou fim. (erro 58)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E058 — Erro

## Descrição

Valor em bloco VALUES com espaco no inicio ou fim. (erro 58)

## Mensagem do compilador

```text
The value `"valor"` declared in the field 'nome_do_campo' has
  whitespace at the start or end. These invisible spaces would
  keep the value from being recognized when used in the annotations.
  Remove the extra spaces around the value in the template declaration.
```

## Onde aparece

- **ValueWithWhitespace**: `field_name`, `value`
