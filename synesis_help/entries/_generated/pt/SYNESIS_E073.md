---
id: SYNESIS_E073
title: "SYNESIS_E073"
category: diagnostic
summary: "Arquivo .syn declarado em INCLUDE ANNOTATIONS nao encontrado. (erro 73)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E073 — Erro

## Descrição

Arquivo .syn declarado em INCLUDE ANNOTATIONS nao encontrado. (erro 73)

## Mensagem do compilador

```text
O arquivo de anotacoes `arquivo.syn` esta declarado em INCLUDE ANNOTATIONS
  mas nao foi encontrado. As anotacoes que ele deveria conter nao serao
  carregadas nem validadas.
  Verifique se o nome esta correto e se o arquivo existe. O caminho deve ser
  relativo a pasta onde esta o arquivo de projeto (`.synp`).
```

## Onde aparece

- **MissingAnnotationsFile**: `filename`
