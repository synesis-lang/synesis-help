---
id: SYNESIS_E039
title: "SYNESIS_E039"
category: diagnostic
summary: "Campo listado em SCOPE FIELDS sem FIELD correspondente. (erros 39-41)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E039 — Erro

## Descrição

Campo listado em SCOPE FIELDS sem FIELD correspondente. (erros 39-41)

## Mensagem do compilador

```text
The field 'nome_do_campo' is listed in `ITEM FIELDS`,
  but there is no matching `FIELD` definition in the template.
  Add to the template:
      FIELD nome_do_campo TYPE TEXT
          SCOPE ITEM
      END FIELD
  This problem is in the template definition. If you are not the author
  of the template, tell the project coordinator.
```

## Onde aparece

- **UndefinedFieldInScopeFields**: `field_name`, `scope`
