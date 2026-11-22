---
id: SYNESIS_E164
title: "SYNESIS_E164"
category: diagnostic
summary: "Campo de ONTOLOGY, ou de SOURCE com valor fora do .syn (ON BIBLIOGRAPHY/ON DATASET)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E164 — Erro

## Descrição

Campo de ONTOLOGY, ou de SOURCE com valor fora do .syn (ON BIBLIOGRAPHY/ON DATASET).

## Mensagem do compilador

```text
`exemplo`: the field `nome_do_campo` cannot enter an Alpaca key yet
  (exemplo). Planned for a later version; use ITEM fields and SOURCE fields
  written in the annotation files.
```

## Onde aparece

- **AlpacaFieldNotSupported**: `block`, `field_name`, `reason`
