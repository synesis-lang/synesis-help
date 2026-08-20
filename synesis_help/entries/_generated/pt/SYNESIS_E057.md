---
id: SYNESIS_E057
title: "SYNESIS_E057"
category: diagnostic
summary: "Dois ou mais blocos SCOPE FIELDS no mesmo template. (erro 57)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E057 — Erro

## Descrição

Dois ou mais blocos SCOPE FIELDS no mesmo template. (erro 57)

## Mensagem do compilador

```text
O template contem mais de um bloco `ITEM FIELDS`. Apenas um bloco
  desse tipo e permitido por template — ter dois causaria ambiguidade sobre
  quais campos sao validos nos conceitos.
  Unifique todas as declaracoes em um unico bloco `ITEM FIELDS`.
```

## Onde aparece

- **DuplicateScopeBlock**: `scope`
