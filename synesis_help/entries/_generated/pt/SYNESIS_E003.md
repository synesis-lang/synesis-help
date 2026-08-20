---
id: SYNESIS_E003
title: "SYNESIS_E003"
category: diagnostic
summary: "SOURCE sem ITEMs associados."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E003 — Erro

## Descrição

SOURCE sem ITEMs associados.

## Mensagem do compilador

```text
O bloco `SOURCE @@autor2024` nao possui nenhum ITEM associado. Um SOURCE
  existe para contextualizar unidades de analise — sem ITEMs, a fonte foi
  registrada mas nunca analisada.
  Verifique se ha ITEMs com essa referencia em outro arquivo do projeto,
  ou adicione pelo menos um ITEM a este SOURCE.
```

## Onde aparece

- **SourceWithoutItems**: `bibref`
