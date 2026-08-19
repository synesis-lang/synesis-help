---
id: SYNESIS_E076
title: "SYNESIS_E076"
category: diagnostic
summary: "Arquivo declarado no .synp existe mas nao pode ser lido/parseado. (erro 76)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E076 — Erro

## Descricao

Arquivo declarado no .synp existe mas nao pode ser lido/parseado. (erro 76)

## Mensagem do compilador

```text
O arquivo `arquivo.syn` foi encontrado mas nao pode ser lido pelo
  compilador:
    exemplo
  Verifique se o arquivo esta salvo em codificacao UTF-8 e se nao esta
  corrompido ou aberto exclusivamente por outro programa.
```

## Onde aparece

- **UnreadableIncludedFile**: `filename`, `reason`
