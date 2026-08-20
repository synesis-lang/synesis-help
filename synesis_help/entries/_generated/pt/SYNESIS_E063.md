---
id: SYNESIS_E063
title: "SYNESIS_E063"
category: diagnostic
summary: "Arquivo .bib declarado no projeto nao encontrado no caminho indicado. (erro 63)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E063 — Erro

## Descrição

Arquivo .bib declarado no projeto nao encontrado no caminho indicado. (erro 63)

## Mensagem do compilador

```text
O arquivo de referencias bibliograficas `arquivo.syn` declarado no
  projeto nao foi encontrado. Sem ele, nenhuma referencia `@bibref` pode
  ser validada.
  Verifique se o arquivo existe e se o caminho esta correto. O caminho
  deve ser relativo a pasta onde esta o arquivo de projeto (`.synp`).
```

## Onde aparece

- **MissingBibliographyFile**: `filename`
