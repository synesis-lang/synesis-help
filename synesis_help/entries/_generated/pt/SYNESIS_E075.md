---
id: SYNESIS_E075
title: "SYNESIS_E075"
category: diagnostic
summary: "Caminho declarado no .synp aponta para fora do diretorio do projeto. (erro 75)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E075 — Erro

## Descrição

Caminho declarado no .synp aponta para fora do diretorio do projeto. (erro 75)

## Mensagem do compilador

```text
The path `arquivo.syn` declared in the project points outside the
  project folder. For safety, the compiler only loads files inside the
  folder of the `.synp` (or its subfolders).
  Move the file into the project folder and fix the path.
```

## Onde aparece

- **IncludePathEscapesProject**: `filename`
