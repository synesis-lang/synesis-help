---
id: SYNESIS_E048
title: "SYNESIS_E048"
category: diagnostic
summary: "ARITY incompativel com numero de RELATIONS declaradas. (erro 48)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E048 — Erro

## Descrição

ARITY incompativel com numero de RELATIONS declaradas. (erro 48)

## Mensagem do compilador

```text
O campo 'nome_do_campo' declara `ARITY >= 2`, o que exige
  pelo menos 2 conceitos por cadeia — mas apenas 2
  relacao(oes) esta(ao) definida(s) em `RELATIONS`. Para conectar 2
  conceitos em sequencia, sao necessarias pelo menos 1 relacoes.
  Adicione as relacoes faltantes ao bloco `RELATIONS` ou reduza o valor de `ARITY`.
```

## Onde aparece

- **ArityRelationsMismatch**: `field_name`, `arity`, `n_relations`
