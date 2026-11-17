---
id: SYNESIS_E032
title: "SYNESIS_E032"
category: diagnostic
summary: "Campo TOPIC recebendo valor com espacos. (erro 32)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E032 — Erro

## Descrição

Campo TOPIC recebendo valor com espacos. (erro 32)

## Mensagem do compilador

```text
The value `valor` of the field `nome_do_campo` contains spaces, which
  is not allowed in TOPIC fields. Spaces are read as
  separators and would make the grouping ambiguous.
  Use underscores instead of spaces. For example: `valor`.
```

## Onde aparece

- **TopicWithSpaces**: `field_name`, `value`
