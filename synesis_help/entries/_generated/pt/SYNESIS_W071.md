---
id: SYNESIS_W071
title: "SYNESIS_W071"
category: diagnostic
summary: "Dois blocos ONTOLOGY com description identica. (erro 71)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W071 — Aviso

## Descrição

Dois blocos ONTOLOGY com description identica. (erro 71)

## Mensagem do compilador

```text
Os conceitos `exemplo` e `exemplo` tem exatamente
  a mesma descricao. Isso geralmente indica um erro de copia — dois
  conceitos distintos nao devem ter definicoes identicas.
  Revise as definicoes e diferencie as descricoes, ou verifique se os
  dois conceitos deveriam ser um unico.
```

## Onde aparece

- **DuplicateOntologyDescription**: `concept_a`, `concept_b`
