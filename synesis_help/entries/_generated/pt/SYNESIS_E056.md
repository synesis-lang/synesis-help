---
id: SYNESIS_E056
title: "SYNESIS_E056"
category: diagnostic
summary: "RELATIONS definido em campo que nao e TYPE CHAIN. (erro 56)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E056 — Erro

## Descricao

RELATIONS definido em campo que nao e TYPE CHAIN. (erro 56)

## Mensagem do compilador

```text
O campo 'nome_do_campo' define um bloco `RELATIONS`, mas seu tipo e
  `TEXT`, nao `CHAIN`. Blocos `RELATIONS` descrevem os tipos
  de vinculo possiveis entre conceitos — eles so fazem sentido em campos
  do tipo CHAIN. Remova o bloco `RELATIONS` ou altere o tipo para `CHAIN`.
```

## Onde aparece

- **RelationsOnNonChain**: `field_name`, `field_type`
