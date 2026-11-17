---
id: SYNESIS_E005
title: "SYNESIS_E005"
category: diagnostic
summary: "ONTOLOGY presente mas template nao declara ONTOLOGY FIELDS. (erro 5)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E005 — Erro

## Descrição

ONTOLOGY presente mas template nao declara ONTOLOGY FIELDS. (erro 5)

## Mensagem do compilador

```text
The project has ONTOLOGY blocks, but the template does not declare any
  field in `ONTOLOGY FIELDS`. Without this, the fields of the
  concepts cannot be validated.
  This problem is in the template definition. If you are not the author
  of the template, tell the project coordinator.
  To fix it, add to the template:
      ONTOLOGY FIELDS
          REQUIRED field_name
      END ONTOLOGY FIELDS
```

## Onde aparece

- **OntologyWithoutTemplateFields**: —
