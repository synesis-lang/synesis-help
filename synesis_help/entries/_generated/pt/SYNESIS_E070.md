---
id: SYNESIS_E070
title: "SYNESIS_E070"
category: diagnostic
summary: "Mesmo @bibref declarado em dois blocos SOURCE no mesmo arquivo. (erro 70)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E070 — Erro

## Descrição

Mesmo @bibref declarado em dois blocos SOURCE no mesmo arquivo. (erro 70)

## Mensagem do compilador

```text
A referencia `@@autor2024` aparece em dois blocos SOURCE diferentes
  no arquivo `arquivo.syn`. Cada referencia bibliografica pode ter
  apenas um bloco SOURCE por arquivo.
  Unifique os dois blocos SOURCE em um unico, ou distribua as anotacoes
  em arquivos `.syn` separados.
```

## Onde aparece

- **DuplicateSourceBibref**: `bibref`, `filename`
