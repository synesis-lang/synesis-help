---
id: SYNESIS_E008
title: "SYNESIS_E008"
category: diagnostic
summary: "Chain qualificada usada mas template nao define RELATIONS. (erro 8)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E008 — Erro

## Descrição

Chain qualificada usada mas template nao define RELATIONS. (erro 8)

## Mensagem do compilador

```text
This chain uses named relations (e.g. `Concept -> RELATION -> Concept`),
  but the template does not define a `RELATIONS` block for the field
  `nome_do_campo`.
  If the template uses simple chains, rewrite the chain without relations:
  `Concept -> Concept`. If you want named relations, ask the
  project coordinator to add a `RELATIONS` block to the template.
```

## Onde aparece

- **QualifiedChainWithoutRelations**: `field_name`
