---
id: SYNESIS_E077
title: "SYNESIS_E077"
category: diagnostic
summary: "Dois SOURCEs com o mesmo valor num campo IDENTIFIES. (erro 77)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E077 — Erro

## Descricao

Dois SOURCEs com o mesmo valor num campo IDENTIFIES. (erro 77)

## Mensagem do compilador

```text
O campo `nome_do_campo` identifica a entidade `exemplo` (IDENTIFIES),
  ou seja, cada valor deve corresponder a um unico SOURCE — como uma chave
  primaria. Mas o valor `valor` aparece em dois SOURCEs:
    `exemplo` e `exemplo`.
  Se sao a mesma entidade, unifique os dois SOURCEs. Se sao entidades
  distintas, corrija o valor de `nome_do_campo` em um deles.
```

## Onde aparece

- **DuplicateIdentityValue**: `field_name`, `entity`, `value`, `first_bibref`, `duplicate_bibref`
