---
id: SYNESIS_E087
title: "SYNESIS_E087"
category: diagnostic
summary: "Prefixo de indice `[N]` em VALUES de campo ENUMERATED. (erro 87)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E087 — Erro

## Descrição

Prefixo de indice `[N]` em VALUES de campo ENUMERATED. (erro 87)

## Mensagem do compilador

```text
The field 'nome_do_campo' is of type `ENUMERATED`, but its values use
  an index prefix (`[0]`, `[1]`, ...). The index exists to establish an
  ORDER among the values and only takes effect in `ORDERED` fields, where it is
  the data written in the annotations. In `ENUMERATED` there is no order: the data is
  the label itself, and the index would be ignored.
  Remove the `[N]` prefixes or change the field type to `ORDERED`.
```

## Onde aparece

- **IndexOnEnumeratedValue**: `field_name`
