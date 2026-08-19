---
id: SYNESIS_E049
title: "SYNESIS_E049"
category: diagnostic
summary: "TYPE ORDERED sem bloco VALUES. (erro 49)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E049 — Erro

## Descricao

TYPE ORDERED sem bloco VALUES. (erro 49)

## Mensagem do compilador

```text
O campo 'nome_do_campo' e do tipo ORDERED, mas nao define um bloco
  `VALUES` com as opcoes validas e sua ordem. Sem isso, nao ha como
  validar os valores inseridos nem apresentar a escala aos pesquisadores.
  Adicione um bloco `VALUES` listando as opcoes em ordem crescente.
```

## Onde aparece

- **OrderedWithoutValues**: `field_name`
