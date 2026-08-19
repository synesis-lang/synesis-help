---
id: SYNESIS_E018
title: "SYNESIS_E018"
category: diagnostic
summary: "BUNDLE declarado com apenas um campo. (erro 18)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E018 — Erro

## Descricao

BUNDLE declarado com apenas um campo. (erro 18)

## Mensagem do compilador

```text
O bundle `e, x, e, m, p, l, o` no template foi declarado com apenas um campo.
  Um bundle precisa de pelo menos dois campos — ele existe para garantir
  que informacoes relacionadas aparecam sempre juntas.
  Este problema esta na definicao do template. Se voce nao e o autor
  do template, avise o coordenador do projeto.
  Adicione os demais campos ao bundle ou remova a declaracao BUNDLE,
  tornando o campo simplesmente REQUIRED ou OPTIONAL.
```

## Onde aparece

- **SingleFieldBundle**: `bundle_fields`
