---
id: SYNESIS_E074
title: "SYNESIS_E074"
category: diagnostic
summary: "Arquivo .syno declarado em INCLUDE ONTOLOGY nao encontrado. (erro 74)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E074 — Erro

## Descrição

Arquivo .syno declarado em INCLUDE ONTOLOGY nao encontrado. (erro 74)

## Mensagem do compilador

```text
The organizing model file `arquivo.syn` is declared in INCLUDE ONTOLOGY
  but was not found. Without it, the codes used in the annotations cannot
  be validated against the organizing model.
  Check that the name is correct and that the file exists. The path must be
  relative to the folder of the project file (`.synp`).
```

## Onde aparece

- **MissingOntologyFile**: `filename`
