---
id: SYNESIS_E121
title: "SYNESIS_E121"
category: diagnostic
summary: "Hierarquia pela rota de nome (`parent`/`is_a`)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E121 — Erro

## Descrição

Hierarquia pela rota de nome (`parent`/`is_a`).

## Mensagem do compilador

```text
The field `nome_do_campo` of `exemplo` becomes hierarchy only by its NAME.
  This route will be removed: declare the field as CODE with `ROLE HIERARCHY KIND`.
```

## Onde aparece

- **DeprecatedNameBasedHierarchy**: `concept`, `field_name`
