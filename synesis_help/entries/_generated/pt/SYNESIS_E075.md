---
id: SYNESIS_E075
title: "SYNESIS_E075"
category: diagnostic
summary: "Caminho declarado no .synp aponta para fora do diretorio do projeto. (erro 75)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E075 — Erro

## Descrição

Caminho declarado no .synp aponta para fora do diretorio do projeto. (erro 75)

## Mensagem do compilador

```text
O caminho `arquivo.syn` declarado no projeto aponta para fora da pasta
  do projeto. Por seguranca, o compilador so carrega arquivos contidos na
  pasta onde esta o `.synp` (ou em suas subpastas).
  Mova o arquivo para dentro da pasta do projeto e ajuste o caminho.
```

## Onde aparece

- **IncludePathEscapesProject**: `filename`
