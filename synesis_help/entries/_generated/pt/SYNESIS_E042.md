---
id: SYNESIS_E042
title: "SYNESIS_E042"
category: diagnostic
summary: "FIELD definido mas nao listado em nenhum SCOPE FIELDS. (erro 42)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E042 — Erro

## Descrição

FIELD definido mas nao listado em nenhum SCOPE FIELDS. (erro 42)

## Mensagem do compilador

```text
The field 'nome_do_campo' is defined in the template, but does not appear
  in any `SOURCE FIELDS`, `ITEM FIELDS` or `ONTOLOGY FIELDS` block.
  A field that is defined but not listed is never recognized in the annotations.
  Include `nome_do_campo` in the `ITEM FIELDS` block matching
  its scope, or remove the definition if it is not needed.
```

## Onde aparece

- **OrphanFieldDefinition**: `field_name`, `scope`
