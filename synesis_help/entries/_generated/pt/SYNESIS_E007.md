---
id: SYNESIS_E007
title: "SYNESIS_E007"
category: diagnostic
summary: "Violacao de ARITY em cadeia causal."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E007 — Erro

## Descricao

Violacao de ARITY em cadeia causal.

## Mensagem do compilador

```text
Esta cadeia tem poucos elementos. O template exige `exemplo` conceitos,
  mas foram encontrados apenas `2`.
  Uma cadeia precisa conectar pelo menos dois conceitos com `->`.
  Acrescente os elementos faltantes ate satisfazer o requisito minimo.
```

## Onde aparece

- **ChainArityViolation**: `expected`, `found`
