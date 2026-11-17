---
id: SYNESIS_E059
title: "SYNESIS_E059"
category: diagnostic
summary: "Valores duplicados dentro de um mesmo bloco VALUES. (erro 59)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E059 — Erro

## Descrição

Valores duplicados dentro de um mesmo bloco VALUES. (erro 59)

## Mensagem do compilador

```text
The field 'nome_do_campo' has the value `valor` declared more than
  once in the `VALUES` block. Duplicate values are ambiguous and may
  produce inconsistent results in exports.
  Remove the duplicate entry.
```

## Onde aparece

- **DuplicateValue**: `field_name`, `value`
