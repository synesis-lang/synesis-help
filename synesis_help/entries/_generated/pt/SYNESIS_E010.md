---
id: SYNESIS_E010
title: "SYNESIS_E010"
category: diagnostic
summary: "Relacao nao definida no template."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E010 — Erro

## Descrição

Relacao nao definida no template.

## Mensagem do compilador

```text
A relacao `exemplo` usada nesta cadeia nao esta declarada no
  template para este campo.
  Voce quis dizer `EXEMPLO_B`?
  Relacoes disponiveis: `exemplo_a`, `exemplo_b`.
  Use uma das relacoes listadas ou peca ao coordenador do projeto
  que inclua a nova relacao no template.
```

## Onde aparece

- **InvalidChainRelation**: `relation`, `valid_relations`, `relation_descriptions`
