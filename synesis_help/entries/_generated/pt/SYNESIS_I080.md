---
id: SYNESIS_I080
title: "SYNESIS_I080"
category: diagnostic
summary: "INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80)."
severity: Informação
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_I080 — Informação

## Descrição

INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80)

## Mensagem do compilador

```text
This project references the external entity `exemplo` (`REFERS TO` in `nome_do_campo`).
  The links are not materialized in this artifact. To resolve them,
  compile this project together with the project that declares `IDENTIFIES exemplo`.
```

## Onde aparece

- **ExternalReferenceDeclared**: `entity`, `field_name`
