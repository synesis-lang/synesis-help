---
id: SYNESIS_E003
title: "SYNESIS_E003"
category: diagnostic
summary: "SOURCE sem ITEMs associados."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E003 — Erro

## Descrição

SOURCE sem ITEMs associados.

## Mensagem do compilador

```text
The `SOURCE @@autor2024` block has no associated ITEM. A SOURCE
  exists to give context to units of analysis — without ITEMs, the source was
  registered but never analyzed.
  Check whether ITEMs with this reference exist in another project file,
  or add at least one ITEM to this SOURCE.
```

## Onde aparece

- **SourceWithoutItems**: `bibref`
