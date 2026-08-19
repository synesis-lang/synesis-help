---
id: SYNESIS_E055
title: "SYNESIS_E055"
category: diagnostic
summary: "ARITY declarado em campo que nao e TYPE CHAIN. (erro 55)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E055 — Erro

## Descricao

ARITY declarado em campo que nao e TYPE CHAIN. (erro 55)

## Mensagem do compilador

```text
O campo 'nome_do_campo' declara `ARITY`, mas seu tipo e `TEXT`.
  A declaracao `ARITY` e exclusiva de campos do tipo CHAIN.
  Este problema esta na definicao do template.
  Remova a declaracao `ARITY` ou altere o tipo do campo para `CHAIN`.
```

## Onde aparece

- **ArityOnNonChain**: `field_name`, `field_type`
