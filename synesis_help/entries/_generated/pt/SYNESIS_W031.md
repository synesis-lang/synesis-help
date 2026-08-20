---
id: SYNESIS_W031
title: "SYNESIS_W031"
category: diagnostic
summary: "Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W031 — Aviso

## Descrição

Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31)

## Mensagem do compilador

```text
O codigo `CODIGO_A` aparece mais de uma vez no campo `nome_do_campo`
  neste bloco. Codigos repetidos nao acrescentam informacao e podem
  distorcer a contagem nas exportacoes.
  Remova a ocorrencia duplicada e mantenha o codigo apenas uma vez.
```

## Onde aparece

- **DuplicateCodeInField**: `field_name`, `code`
