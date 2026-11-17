---
id: SYNESIS_E137
title: "SYNESIS_E137"
category: diagnostic
summary: "O mesmo campo em FIELDS de duas fases."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E137 — Erro

## Descrição

O mesmo campo em FIELDS de duas fases.

## Mensagem do compilador

```text
`exemplo`: the field `nome_do_campo` is already produced by `exemplo`.
  Each field is produced by a single phase.
```

## Onde aparece

- **FieldInTwoPhases**: `phase`, `field_name`, `first_phase`
