---
id: SYNESIS_E010
title: "SYNESIS_E010"
category: diagnostic
summary: "Relacao nao definida no template."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E010 — Erro

## Descrição

Relacao nao definida no template.

## Mensagem do compilador

```text
The relation `exemplo` used in this chain is not declared in the
  template for this field.
  Did you mean `EXEMPLO_B`?
  Available relations: `exemplo_a`, `exemplo_b`.
  Use one of the listed relations or ask the project coordinator
  to add the new relation to the template.
```

## Onde aparece

- **InvalidChainRelation**: `relation`, `valid_relations`, `relation_descriptions`
