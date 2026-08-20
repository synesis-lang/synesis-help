---
id: SYNESIS_I080
title: "SYNESIS_I080"
category: diagnostic
summary: "\"INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80).\""
severity: Informação
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_I080 — Informação

## Descrição

INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80)

## Mensagem do compilador

```text
Este projeto referencia a entidade externa `exemplo` (`REFERS TO` em `nome_do_campo`).
  As ligacoes nao estao materializadas neste artefato. Para resolve-las,
  compile este projeto junto com o projeto que declara `IDENTIFIES exemplo`.
```

## Onde aparece

- **ExternalReferenceDeclared**: `entity`, `field_name`
