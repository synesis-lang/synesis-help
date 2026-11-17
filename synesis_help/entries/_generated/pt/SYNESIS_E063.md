---
id: SYNESIS_E063
title: "SYNESIS_E063"
category: diagnostic
summary: "Arquivo .bib declarado no projeto nao encontrado no caminho indicado. (erro 63)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E063 — Erro

## Descrição

Arquivo .bib declarado no projeto nao encontrado no caminho indicado. (erro 63)

## Mensagem do compilador

```text
The bibliographic references file `arquivo.syn` declared in the
  project was not found. Without it, no `@bibref` reference can
  be validated.
  Check that the file exists and that the path is correct. The path
  must be relative to the folder of the project file (`.synp`).
```

## Onde aparece

- **MissingBibliographyFile**: `filename`, `no_matches`
