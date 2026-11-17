---
id: SYNESIS_E073
title: "SYNESIS_E073"
category: diagnostic
summary: "Arquivo .syn declarado em INCLUDE ANNOTATIONS nao encontrado. (erro 73)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E073 — Erro

## Descrição

Arquivo .syn declarado em INCLUDE ANNOTATIONS nao encontrado. (erro 73)

## Mensagem do compilador

```text
The annotations file `arquivo.syn` is declared in INCLUDE ANNOTATIONS
  but was not found. The annotations it should contain are neither
  loaded nor validated.
  Check that the name is correct and that the file exists. The path must be
  relative to the folder of the project file (`.synp`).
```

## Onde aparece

- **MissingAnnotationsFile**: `filename`
