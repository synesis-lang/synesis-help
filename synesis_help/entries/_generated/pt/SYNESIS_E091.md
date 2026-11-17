---
id: SYNESIS_E091
title: "SYNESIS_E091"
category: diagnostic
summary: "Linha de QUESTIONS fora da forma `<id>: <texto>`."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E091 — Erro

## Descrição

Linha de QUESTIONS fora da forma `<id>: <texto>`.

## Mensagem do compilador

```text
The line `exemplo` in the QUESTIONS block has no identifier.
  Each competency question is a line `<id>: <text>`, for example
  `Q1: Which tactics appear in each channel?`. The identifier starts with
  a letter or `_` and lets manifests, tests and the graph cite the question.
  Add an identifier before `:`.
```

## Onde aparece

- **QuestionWithoutId**: `line`
