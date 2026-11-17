---
id: SYNESIS_E011
title: "SYNESIS_E011"
category: diagnostic
summary: "Chain qualificada com estrutura incorreta."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E011 — Erro

## Descrição

Chain qualificada com estrutura incorreta.

## Mensagem do compilador

```text
The structure of this chain is incorrect: `exemplo_a -> exemplo_b`
  Found:    exemplo_a -> exemplo_b
  Expected: [Concept] -> [RELATION] -> [Concept]
  In qualified chains, even positions are always relation types,
  not concepts. Review the order of the elements.
```

## Onde aparece

- **MalformedQualifiedChain**: `elements`
