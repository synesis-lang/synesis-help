---
id: SYNESIS_E068
title: "SYNESIS_E068"
category: diagnostic
summary: "Dois blocos ONTOLOGY com o mesmo nome de conceito. (erro 68)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E068 — Erro

## Descrição

Dois blocos ONTOLOGY com o mesmo nome de conceito. (erro 68)

## Mensagem do compilador

```text
The concept `exemplo` is defined more than once in the
  project's organizing model:
  - exemplo
  - exemplo
  Each concept must have a unique name across the project. Check
  whether the two blocks represent the same concept — if so, merge them.
  If not, rename one of them so the names differ.
```

## Onde aparece

- **DuplicateOntologyConcept**: `concept_name`, `file_a`, `file_b`
