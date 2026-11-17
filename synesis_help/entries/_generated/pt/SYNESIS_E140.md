---
id: SYNESIS_E140
title: "SYNESIS_E140"
category: diagnostic
summary: "Campos de um BUNDLE em fases diferentes."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E140 — Erro

## Descrição

Campos de um BUNDLE em fases diferentes.

## Mensagem do compilador

```text
`exemplo`: the fields of the BUNDLE (e, x, e, m, p, l, o) are in different
  phases. Fields of a BUNDLE are produced together (the cross rule between
  them is lost when they are split).
```

## Onde aparece

- **BundleSplitAcrossPhases**: `phase`, `bundle`
