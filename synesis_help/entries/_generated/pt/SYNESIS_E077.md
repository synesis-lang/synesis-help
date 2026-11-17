---
id: SYNESIS_E077
title: "SYNESIS_E077"
category: diagnostic
summary: "Dois SOURCEs com o mesmo valor num campo IDENTIFIES. (erro 77)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E077 — Erro

## Descrição

Dois SOURCEs com o mesmo valor num campo IDENTIFIES. (erro 77)

## Mensagem do compilador

```text
The field `nome_do_campo` identifies the entity `exemplo` (IDENTIFIES),
  so each value must match a single SOURCE — like a primary
  key. But the value `valor` appears in two SOURCEs:
    `exemplo` and `exemplo`.
  If they are the same entity, merge the two SOURCEs. If they are distinct
  entities, fix the value of `nome_do_campo` in one of them.
```

## Onde aparece

- **DuplicateIdentityValue**: `field_name`, `entity`, `value`, `first_bibref`, `duplicate_bibref`
