---
id: SYNESIS_E006
title: "SYNESIS_E006"
category: diagnostic
summary: "Campo listado em SCOPE FIELDS cujo FIELD tem SCOPE diferente. (erro 6)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E006 — Erro

## Descricao

Campo listado em SCOPE FIELDS cujo FIELD tem SCOPE diferente. (erro 6)

## Mensagem do compilador

```text
O campo 'nome_do_campo' esta listado em `exemplo FIELDS`,
  mas sua definicao FIELD declara `SCOPE exemplo`.
  Cada campo listado precisa ter sua propria definicao com o mesmo escopo.
  Corrija o escopo na definicao FIELD ou mova o campo para o bloco correto.
  Este problema esta na definicao do template. Se voce nao e o autor
  do template, avise o coordenador do projeto.
```

## Onde aparece

- **FieldScopeListMismatch**: `field_name`, `listed_scope`, `actual_scope`
