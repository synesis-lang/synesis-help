---
id: SYNESIS_E050
title: "SYNESIS_E050"
category: diagnostic
summary: "TYPE ENUMERATED sem bloco VALUES. (erro 50)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E050 — Erro

## Descrição

TYPE ENUMERATED sem bloco VALUES. (erro 50)

## Mensagem do compilador

```text
The field 'nome_do_campo' is of type ENUMERATED, but does not define a
  `VALUES` block with the valid options. Without it, any value would be accepted,
  losing control over the vocabulary.
  Add a `VALUES` block listing every option accepted for this field.
```

## Onde aparece

- **EnumeratedWithoutValues**: `field_name`
