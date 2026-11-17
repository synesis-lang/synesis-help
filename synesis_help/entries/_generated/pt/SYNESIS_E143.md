---
id: SYNESIS_E143
title: "SYNESIS_E143"
category: diagnostic
summary: "OUTPUT fora dos .syno locais citados como arquivo."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E143 — Erro

## Descrição

OUTPUT fora dos .syno locais citados como arquivo.

## Mensagem do compilador

```text
`exemplo`: `OUTPUT exemplo` is not a local .syno of the project. The destination
  must be an INCLUDE ONTOLOGY cited as a file (not a folder or pattern) and
  outside INCLUDE SHARED.
```

## Onde aparece

- **PhaseOutputNotLocal**: `phase`, `output`
