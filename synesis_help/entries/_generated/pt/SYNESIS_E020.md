---
id: SYNESIS_E020
title: "SYNESIS_E020"
category: diagnostic
summary: "Campo REQUIRED ausente."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E020 — Erro

## Descricao

Campo REQUIRED ausente.

## Mensagem do compilador

```text
O campo `nome_do_campo` e obrigatorio neste bloco ITEM,
  mas nao foi encontrado.
  Adicione a linha `nome_do_campo: <valor>` ao bloco antes de
  `END ITEM`.
```

## Onde aparece

- **MissingRequiredField**: `field_name`, `block_type`
