---
id: SYNESIS_E111
title: "SYNESIS_E111"
category: diagnostic
summary: "Campo HIERARCHY declarado REQUIRED."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E111 — Erro

## Descrição

Campo HIERARCHY declarado REQUIRED.

## Mensagem do compilador

```text
The field `nome_do_campo` (exemplo) is REQUIRED. That would demand a parent
  for every concept, and no finite hierarchy without cycles satisfies the rule:
  some concept has to be at the top. Declare the field as OPTIONAL.
```

## Onde aparece

- **RequiredHierarchy**: `field_name`, `role`
