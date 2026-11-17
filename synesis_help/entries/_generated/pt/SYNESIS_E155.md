---
id: SYNESIS_E155
title: "SYNESIS_E155"
category: diagnostic
summary: "Verificacao editorial do SKOS gerado (sem prefLabel, sem posicao, esquema sem topo...)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E155 — Erro

## Descrição

Verificacao editorial do SKOS gerado (sem prefLabel, sem posicao, esquema sem topo...).

## Mensagem do compilador

```text
`exemplo`: SKOS quality check "exemplo" — 2 case(s).

  Editorial, not a violation of SKOS: the file was written. Tools such as VocBench (ICV)
  and qSKOS report the same group.
```

## Onde aparece

- **SkosQualityNotice**: `block`, `condition`, `count`, `examples`
