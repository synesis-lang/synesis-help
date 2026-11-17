---
id: SYNESIS_E153
title: "SYNESIS_E153"
category: diagnostic
summary: "IRI registrado como publicado sem bloco nem USE que o substitua."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E153 — Erro

## Descrição

IRI registrado como publicado sem bloco nem USE que o substitua.

## Mensagem do compilador

```text
`exemplo`: the published IRI `exemplo` no longer has a block in the project.
  A published concept does not vanish: consolidate it with USE (it is exported as
  deprecated, with isReplacedBy) instead of deleting or renaming the block.
```

## Onde aparece

- **PublishedIriWithoutBlock**: `block`, `iri`
