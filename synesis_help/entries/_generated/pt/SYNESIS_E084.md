---
id: SYNESIS_E084
title: "SYNESIS_E084"
category: diagnostic
summary: "INCLUDE SHARED usado com tipo diferente de ONTOLOGY. (erro 84)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E084 — Erro

## Descrição

INCLUDE SHARED usado com tipo diferente de ONTOLOGY. (erro 84)

## Mensagem do compilador

```text
`INCLUDE SHARED` is only valid for `ONTOLOGY`, but it was used with
  `exemplo` (`exemplo`).
  The word `SHARED` allows a target OUTSIDE the project folder — it exists
  to share the conceptual vocabulary (the organizing model) between projects
  of the same study. The other includes must stay inside the project.
  Remove `SHARED`, or move the file into the project folder.
```

## Onde aparece

- **SharedOnlyForOntology**: `include_type`, `path`
