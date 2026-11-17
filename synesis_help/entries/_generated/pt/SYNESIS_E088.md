---
id: SYNESIS_E088
title: "SYNESIS_E088"
category: diagnostic
summary: "Campo ORDERED escrito com o rotulo em vez do indice. (erro 88)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E088 — Erro

## Descrição

Campo ORDERED escrito com o rotulo em vez do indice. (erro 88)

## Mensagem do compilador

```text
The field 'nome_do_campo' was written with the label `exemplo`,
  but in `ORDERED` fields the data written is the INDEX. The index defines the
  order of the values and admits no spelling variants; the label is
  declared in the template and shown by the editor next to the index.
  Write `nome_do_campo: 2`.
```

## Onde aparece

- **OrderedValueAsLabel**: `field_name`, `label`, `index`
