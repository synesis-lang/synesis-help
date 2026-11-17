---
id: SYNESIS_E123
title: "SYNESIS_E123"
category: diagnostic
summary: "Relacao presente em mais de um campo CHAIN, sem FROM."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E123 — Erro

## Descrição

Relacao presente em mais de um campo CHAIN, sem FROM.

## Mensagem do compilador

```text
`exemplo`: the relation `exemplo` exists in more than one CHAIN field ().
  Say which with `MAP RELATIONS exemplo FROM <field> TO ...`.
```

## Onde aparece

- **AmbiguousRelation**: `block`, `relation`, `fields`
