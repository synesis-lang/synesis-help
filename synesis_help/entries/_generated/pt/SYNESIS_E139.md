---
id: SYNESIS_E139
title: "SYNESIS_E139"
category: diagnostic
summary: "INPUT produzido só por uma fase POSTERIOR (ordem das fases)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E139 — Erro

## Descrição

INPUT produzido só por uma fase POSTERIOR (ordem das fases).

## Mensagem do compilador

```text
`exemplo`: `nome_do_campo` (INPUT) is only produced by a later phase.
  In this order, the phase reads whatever value exists before it; move it later.
```

## Onde aparece

- **InputNotAvailable**: `phase`, `field_name`
