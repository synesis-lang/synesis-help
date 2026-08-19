---
id: SYNESIS_E050
title: "SYNESIS_E050"
category: diagnostic
summary: "TYPE ENUMERATED sem bloco VALUES. (erro 50)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E050 — Erro

## Descricao

TYPE ENUMERATED sem bloco VALUES. (erro 50)

## Mensagem do compilador

```text
O campo 'nome_do_campo' e do tipo ENUMERATED, mas nao define um bloco
  `VALUES` com as opcoes validas. Sem isso, qualquer valor seria aceito,
  perdendo o controle sobre o vocabulario.
  Adicione um bloco `VALUES` listando todas as opcoes aceitas para este campo.
```

## Onde aparece

- **EnumeratedWithoutValues**: `field_name`
