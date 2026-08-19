---
id: SYNESIS_E009
title: "SYNESIS_E009"
category: diagnostic
summary: "Chain simples usada mas template exige RELATIONS. (erro 9)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E009 — Erro

## Descricao

Chain simples usada mas template exige RELATIONS. (erro 9)

## Mensagem do compilador

```text
O template exige que as cadeias usem relacoes nomeadas, mas esta cadeia
  foi escrita sem relacoes para o campo `nome_do_campo`.
  Relacoes disponiveis: `exemplo_a`, `exemplo_b`.
  Reescreva a cadeia no formato: `Conceito -> RELACAO -> Conceito`.
```

## Onde aparece

- **SimpleChainWithRelationsRequired**: `field_name`, `valid_relations`
