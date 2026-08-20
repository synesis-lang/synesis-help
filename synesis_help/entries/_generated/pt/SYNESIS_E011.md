---
id: SYNESIS_E011
title: "SYNESIS_E011"
category: diagnostic
summary: "Chain qualificada com estrutura incorreta."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E011 — Erro

## Descrição

Chain qualificada com estrutura incorreta.

## Mensagem do compilador

```text
A estrutura desta cadeia esta incorreta: `exemplo_a -> exemplo_b`
  Encontrado: exemplo_a -> exemplo_b
  Esperado:   [Conceito] -> [RELACAO] -> [Conceito]
  Em cadeias qualificadas, posicoes pares sao sempre tipos de relacao,
  nao conceitos. Revise a ordem dos elementos.
```

## Onde aparece

- **MalformedQualifiedChain**: `elements`
