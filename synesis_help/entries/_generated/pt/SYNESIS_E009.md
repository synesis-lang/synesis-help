---
id: SYNESIS_E009
title: "SYNESIS_E009"
category: diagnostic
summary: "Chain simples usada mas template exige RELATIONS. (erro 9)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E009 — Erro

## Descrição

Chain simples usada mas template exige RELATIONS. (erro 9)

## Mensagem do compilador

```text
The template requires chains to use named relations, but this chain
  was written without relations for the field `nome_do_campo`.
  Available relations: `exemplo_a`, `exemplo_b`.
  Rewrite the chain as: `Concept -> RELATION -> Concept`.
```

## Onde aparece

- **SimpleChainWithRelationsRequired**: `field_name`, `valid_relations`
