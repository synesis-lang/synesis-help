---
id: SYNESIS_E047
title: "SYNESIS_E047"
category: diagnostic
summary: "TYPE CHAIN sem declaracao ARITY. (erro 47)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E047 — Erro

## Descricao

TYPE CHAIN sem declaracao ARITY. (erro 47)

## Mensagem do compilador

```text
O campo 'nome_do_campo' e do tipo CHAIN, mas nao declara `ARITY`.
  Sem ARITY, o compilador nao pode verificar se as cadeias escritas pelos
  pesquisadores tem o numero minimo de conceitos exigidos.
  Adicione uma declaracao como `ARITY >= 2` para garantir que toda cadeia
  tenha ao menos dois conceitos conectados.
```

## Onde aparece

- **ChainWithoutArity**: `field_name`
