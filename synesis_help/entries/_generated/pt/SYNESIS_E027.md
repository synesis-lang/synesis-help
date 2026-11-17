---
id: SYNESIS_E027
title: "SYNESIS_E027"
category: diagnostic
summary: "Valor fora da lista ENUMERATED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E027 — Erro

## Descrição

Valor fora da lista ENUMERATED.

## Mensagem do compilador

```text
The value `valor` is not recognized for the field `nome_do_campo`.
  This field only accepts values from a closed list.
  Available values: `exemplo_a`, `exemplo_b`.
```

## Onde aparece

- **InvalidEnumeratedValue**: `field_name`, `value`, `valid_values`
