---
id: SYNESIS_E086
title: "SYNESIS_E086"
category: diagnostic
summary: "VALUES definido em campo que nao e ORDERED nem ENUMERATED. (erro 86)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E086 — Erro

## Descricao

VALUES definido em campo que nao e ORDERED nem ENUMERATED. (erro 86)

## Mensagem do compilador

```text
O campo 'nome_do_campo' define um bloco `VALUES`, mas seu tipo e
  `TEXT`. Blocos `VALUES` enumeram as opcoes validas de um
  vocabulario fechado — eles so tem efeito em campos `ORDERED` (opcoes com
  ordem, ex.: Baixo, Medio, Alto) ou `ENUMERATED` (opcoes sem ordem).
  Em `TEXT` a lista seria ignorada na validacao.
  Remova o bloco `VALUES` ou altere o tipo para `ORDERED`/`ENUMERATED`.
```

## Onde aparece

- **ValuesOnNonEnumerable**: `field_name`, `field_type`
