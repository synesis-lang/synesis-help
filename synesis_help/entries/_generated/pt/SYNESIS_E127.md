---
id: SYNESIS_E127
title: "SYNESIS_E127"
category: diagnostic
summary: "NAMESPACE que nao e IRI absoluto terminado em / ou #."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E127 — Erro

## Descrição

NAMESPACE que nao e IRI absoluto terminado em / ou #.

## Mensagem do compilador

```text
`exemplo`: `NAMESPACE valor` must be an absolute IRI ending
  in `/` or `#`, for example `https://example.org/id/project/`.
```

## Onde aparece

- **InvalidNamespace**: `block`, `value`
