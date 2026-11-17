---
id: SYNESIS_E052
title: "SYNESIS_E052"
category: diagnostic
summary: "Sintaxe invalida na declaracao FORMAT de campo SCALE. (erro 52)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E052 — Erro

## Descrição

Sintaxe invalida na declaracao FORMAT de campo SCALE. (erro 52)

## Mensagem do compilador

```text
The range declared in `FORMAT` for the field 'nome_do_campo' is not
  in the expected format: `exemplo`
  The correct format uses brackets and two dots as separator: `[minimum..maximum]`.
  Valid examples: `[1..5]`, `[0..100]`, `[0.0..1.0]`.
```

## Onde aparece

- **InvalidFormatSyntax**: `field_name`, `format_str`
