---
id: SYNESIS_E013
title: "SYNESIS_E013"
category: diagnostic
summary: "Chain sem operador -> entre elementos. (erro 13)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E013 — Erro

## Descricao

Chain sem operador -> entre elementos. (erro 13)

## Mensagem do compilador

```text
Os elementos desta cadeia nao estao separados pelo operador `->`.
  Sem a seta, o compilador nao consegue identificar onde um elemento
  termina e o proximo comeca.
  Valor encontrado: `exemplo`
  Reescreva conectando os elementos com `->`, por exemplo:
  `ConceitoA -> ConceitoB` ou `ConceitoA -> RELACAO -> ConceitoB`
```

## Onde aparece

- **ChainWithoutArrowOperator**: `raw_value`
