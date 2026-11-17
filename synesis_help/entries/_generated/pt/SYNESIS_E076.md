---
id: SYNESIS_E076
title: "SYNESIS_E076"
category: diagnostic
summary: "Arquivo declarado no .synp existe mas nao pode ser lido/parseado. (erro 76)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E076 — Erro

## Descrição

Arquivo declarado no .synp existe mas nao pode ser lido/parseado. (erro 76)

## Mensagem do compilador

```text
The file `arquivo.syn` was found but could not be read by the
  compiler:
    exemplo
  Check that the file is saved as UTF-8 and is not
  corrupted or locked by another program.
```

## Onde aparece

- **UnreadableIncludedFile**: `filename`, `reason`
